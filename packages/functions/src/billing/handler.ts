import { randomUUID } from "node:crypto";
import { GetCommand, QueryCommand } from "@aws-sdk/lib-dynamodb";
import { db, getProfilo, tables } from "@imieiconcorsi/core/db";
import {
  periodo as durata,
  GIORNI_PREMIO_INVITO,
  PERIODO_IDS,
  PIANI,
  VERSIONE_TERMINI,
  type CodiceSconto,
  type PianoId,
} from "@imieiconcorsi/core/domain";
import { emailTornatoFree } from "@imieiconcorsi/core/email-piani";
import { env } from "@imieiconcorsi/core/env";
import { type Event, HttpError, notFound, service } from "@imieiconcorsi/core/http";
import { assegnaPiano } from "@imieiconcorsi/core/piani";
import { motivoRifiuto, normalizzaCodice, prezzoScontato } from "@imieiconcorsi/core/sconti";
import type { APIGatewayProxyEventV2, APIGatewayProxyResultV2 } from "aws-lambda";
import { z } from "zod";
import { codiceDi, usaCodiceInvito } from "./inviti";
import { chiudiOrdine, completaOrdine, leggiOrdine, salvaOrdine, type Ordine } from "./ordini";
import { creaSessione, firmaWebhookValida, leggiSessione, MINIMO_STRIPE } from "./stripe";

// Piani a pagamento. BILLING_MODE (da Terraform):
//   "stripe": l'acquisto crea un ordine e la pagina di pagamento Stripe; il piano si attiva
//             con la conferma di Stripe (webhook) o quando la pagina di ritorno trova il pagamento;
//   "mock":   stesso giro, ma l'ordine si completa subito, senza pagare (prove).

/** Acquisto (o ritorno al Free): piano, durata, consenso e codice sconto facoltativo. */
const Abbonamento = z
  .object({
    piano: z.enum(["free", "medium", "pro"]),
    periodo: z.enum(PERIODO_IDS).default("mensile"),
    /**
     * Per i piani a pagamento: l'utente chiede l'accesso immediato e prende atto che perde
     * il diritto di recesso (art. 59, c. 1, lett. o, Codice del consumo). Senza, niente acquisto.
     */
    rinunciaRecesso: z.literal(true).optional(),
    codice: z.string().max(40).optional(),
  })
  .refine((a) => a.piano === "free" || a.rinunciaRecesso === true, {
    message: "Serve il consenso all'accesso immediato con rinuncia al recesso",
    path: ["rinunciaRecesso"],
  });

/** Codice sconto da controllare prima dell'acquisto. */
const VerificaCodice = z.object({ codice: z.string().max(40) });

/** Un codice (sconto o invito) dalla tabella codici. */
async function leggiCodice(codice: string) {
  const res = await db.send(new GetCommand({ TableName: tables.codici, Key: { codice } }));
  return res.Item as CodiceSconto | undefined;
}

/** Codice valido per questo utente e piano, oppure 400 con il motivo. */
async function codiceValido(userId: string, codiceInserito: string, piano: PianoId) {
  const codice = normalizzaCodice(codiceInserito);
  const [c, profilo] = await Promise.all([leggiCodice(codice), getProfilo(userId)]);
  const motivo = motivoRifiuto(c, { piano, codiciUsati: profilo?.codiciUsati });
  if (motivo) throw new HttpError(400, motivo, "CODICE_NON_VALIDO");
  return c!;
}

/** Risposta JSON per la rotta del webhook, che non passa da service(). */
const json = (statusCode: number, body: unknown): APIGatewayProxyResultV2 => ({
  statusCode,
  headers: { "content-type": "application/json", "cache-control": "no-store" },
  body: JSON.stringify(body),
});

/** Conferme di Stripe (rotta pubblica, protetta dalla firma). Risponde 200 a tutto ciò che è firmato. */
async function webhookStripe(event: APIGatewayProxyEventV2): Promise<APIGatewayProxyResultV2> {
  const segreto = process.env.STRIPE_WEBHOOK_SECRET;
  if (!segreto) return json(503, { error: "Webhook non configurato" });
  const corpo = event.isBase64Encoded ? Buffer.from(event.body ?? "", "base64").toString("utf8") : (event.body ?? "");
  if (!firmaWebhookValida(corpo, event.headers["stripe-signature"], segreto)) return json(400, { error: "Firma non valida" });

  const evento = JSON.parse(corpo) as { type: string; data: { object: { client_reference_id?: string; payment_status?: string } } };
  const ordineId = evento.data.object.client_reference_id;
  if (!ordineId) return json(200, { ignorato: true });

  switch (evento.type) {
    case "checkout.session.completed":
      // Con i metodi "lenti" (es. bonifico) arriva completed ma non ancora paid: si aspetta async_payment_succeeded.
      if (evento.data.object.payment_status === "paid") await completaOrdine(ordineId);
      break;
    case "checkout.session.async_payment_succeeded":
      await completaOrdine(ordineId);
      break;
    case "checkout.session.async_payment_failed":
      await chiudiOrdine(ordineId, "fallito");
      break;
    case "checkout.session.expired":
      await chiudiOrdine(ordineId, "scaduto");
      break;
  }
  return json(200, { ricevuto: true });
}

/** Le rotte con login. */
const servizio = service({
  /** Piani con prezzi e limiti, piano attuale, scadenza e se l'utente può ancora usare un codice d'invito. */
  "GET /piani": async ({ userId, piano }) => {
    const profilo = await getProfilo(userId);
    return {
      piani: Object.values(PIANI),
      attuale: piano,
      periodo: profilo?.periodo,
      scadenza: profilo?.scadenzaPiano,
      modalita: process.env.BILLING_MODE,
    };
  },

  /** Il proprio codice "invita un amico" (creato la prima volta) e com'è andata. */
  "GET /me/invito": async (ctx) => {
    const [c, profilo] = await Promise.all([codiceDi(ctx.userId), getProfilo(ctx.userId)]);
    return {
      codice: c.codice,
      link: `${env("SITE_URL")}/?invito=${encodeURIComponent(c.codice)}`,
      iscritti: c.iscritti,
      premi: c.premi,
      giorniPerPremio: GIORNI_PREMIO_INVITO,
      // Si può ancora inserire il codice di un amico?
      puoiInserire: !profilo?.invitatoDa && !profilo?.ultimoAcquisto,
      invitato: !!profilo?.invitatoDa,
    };
  },

  /** L'utente inserisce il codice dell'amico che l'ha invitato (dal link o dal profilo). */
  "POST /me/invito": async (ctx) => {
    const { codice } = ctx.body(VerificaCodice);
    await usaCodiceInvito(ctx.userId, codice);
    return { ok: true };
  },

  /** Controllo del codice prima dell'acquisto, per mostrare i prezzi scontati. Non consuma il codice. */
  "POST /me/codice-sconto": async (ctx) => {
    const { codice } = ctx.body(VerificaCodice);
    const [c, profilo] = await Promise.all([leggiCodice(normalizzaCodice(codice)), getProfilo(ctx.userId)]);
    // Il piano lo sceglie dopo: qui basta che il codice valga per almeno uno dei suoi piani.
    const motivo = motivoRifiuto(c, { piano: c?.piani?.[0] ?? "medium", codiciUsati: profilo?.codiciUsati });
    if (motivo) throw new HttpError(400, motivo, "CODICE_NON_VALIDO");
    return { codice: c!.codice, percentuale: c!.percentuale, piani: c!.piani ?? ["medium", "pro"] };
  },

  /**
   * Piano Free: subito. Piano a pagamento: crea l'ordine; con Stripe risponde con l'indirizzo
   * della pagina di pagamento ({ pagamento }), altrimenti (mock, o sconto del 100%) completa
   * l'ordine subito. Dopo l'attivazione il sito rinnova il token: il gruppo Cognito è nel token.
   */
  "POST /me/abbonamento": async (ctx) => {
    const { piano, periodo, codice } = ctx.body(Abbonamento);

    if (piano === "free") {
      await assegnaPiano({ userId: ctx.userId, username: ctx.username, piano, scadenza: null });
      if (ctx.piano !== "free" && ctx.email) {
        await emailTornatoFree({ a: ctx.email, nome: ctx.nome, pianoPrecedente: ctx.piano, motivo: "scelta" });
      }
      return { piano, scadenza: null };
    }

    // Il codice si controlla adesso ma si consuma solo a pagamento riuscito (completaOrdine).
    const sconto = codice?.trim() ? await codiceValido(ctx.userId, codice, piano) : undefined;
    const prezzo = PIANI[piano].prezzo[periodo];
    let importo = sconto ? prezzoScontato(prezzo, sconto.percentuale) : prezzo;
    // Stripe non accetta meno di 0,50 €: uno sconto che scende sotto si ferma lì (il 100% resta gratis).
    if (importo > 0 && importo < MINIMO_STRIPE) importo = MINIMO_STRIPE;

    const ora = new Date().toISOString();
    const ordine: Ordine = {
      id: `ord_${randomUUID().replace(/-/g, "").slice(0, 20)}`,
      userId: ctx.userId,
      username: ctx.username,
      piano,
      periodo,
      prezzo,
      importo,
      ...(sconto ? { codiceSconto: sconto.codice, percentualeSconto: sconto.percentuale } : {}),
      stato: "in-attesa",
      // Consenso dato adesso, prima del pagamento: è quello che conta.
      consenso: { rinunciaRecesso: true, versioneTermini: VERSIONE_TERMINI, il: ora },
      creatoIl: ora,
      aggiornatoIl: ora,
    };
    await salvaOrdine(ordine);

    if (process.env.BILLING_MODE === "stripe" && importo > 0) {
      const sito = env("SITE_URL");
      const sessione = await creaSessione({
        ordineId: ordine.id,
        email: ctx.email,
        descrizione: `Piano ${PIANI[piano].nome} ${durata(periodo).giorni} giorni`,
        centesimi: Math.round(importo * 100),
        ritorno: `${sito}/app/pagamento?ordine=${ordine.id}`,
        annullato: `${sito}/app/pagamento?ordine=${ordine.id}&annullato=1`,
      });
      await salvaOrdine({ ...ordine, stripeSessionId: sessione.id });
      return { ordine: ordine.id, pagamento: sessione.url };
    }

    const completo = await completaOrdine(ordine.id);
    return { ordine: ordine.id, piano, periodo, scadenza: completo?.scadenzaPiano, importo };
  },

  /**
   * Esito di un ordine, per la pagina di ritorno da Stripe. Se la conferma di Stripe non è
   * ancora arrivata chiede direttamente a Stripe: così il piano si attiva anche senza webhook.
   */
  /**
   * Storico dei pagamenti dell'utente, dal più recente (indice perUtente della tabella ordini).
   * Anche i tentativi non completati: il sito li mostra a parte.
   */
  "GET /me/ordini": async ({ userId }) => {
    const res = await db.send(
      new QueryCommand({
        TableName: tables.ordini,
        IndexName: "perUtente",
        KeyConditionExpression: "userId = :u",
        ExpressionAttributeValues: { ":u": userId },
        ScanIndexForward: false,
        Limit: 100,
      }),
    );
    return {
      ordini: ((res.Items ?? []) as Ordine[]).map((o) => ({
        id: o.id,
        piano: o.piano,
        periodo: o.periodo,
        prezzo: o.prezzo,
        importo: o.importo,
        codiceSconto: o.codiceSconto,
        percentualeSconto: o.percentualeSconto,
        stato: o.stato,
        creatoIl: o.creatoIl,
        pagatoIl: o.pagatoIl,
        scadenzaPiano: o.scadenzaPiano,
      })),
    };
  },

  /** Stato di un ordine (pagina di ritorno da Stripe); se il webhook tarda lo si chiede a Stripe. */
  "GET /me/ordini/{id}": async (ctx) => {
    let ordine = await leggiOrdine(ctx.params.id!);
    if (!ordine || ordine.userId !== ctx.userId) throw notFound("Ordine");
    if (ordine.stato === "in-attesa" && ordine.stripeSessionId) {
      const s = await leggiSessione(ordine.stripeSessionId);
      if (s.payment_status === "paid") ordine = (await completaOrdine(ordine.id)) ?? ordine;
      else if (s.status === "expired") {
        await chiudiOrdine(ordine.id, "scaduto");
        ordine = { ...ordine, stato: "scaduto" };
      }
    }
    return {
      id: ordine.id,
      stato: ordine.stato,
      piano: ordine.piano,
      periodo: ordine.periodo,
      importo: ordine.importo,
      scadenzaPiano: ordine.scadenzaPiano,
    };
  },
});

/** Il webhook di Stripe non ha login: va gestito a parte; tutto il resto passa da service(). */
export const handler = (event: APIGatewayProxyEventV2) =>
  event.routeKey === "POST /pubblico/stripe/webhook" ? webhookStripe(event) : servizio(event as Event);
