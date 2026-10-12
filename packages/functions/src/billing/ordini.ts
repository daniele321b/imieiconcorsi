import { AdminGetUserCommand } from "@aws-sdk/client-cognito-identity-provider";
import { GetCommand, PutCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { esitoAcquisto } from "@imieiconcorsi/core/acquisti";
import { cognito, gruppiDi, userPoolId } from "@imieiconcorsi/core/cognito";
import { db, getProfilo, tables } from "@imieiconcorsi/core/db";
import { periodo as durata, GRUPPI, pianoDaGruppi, PIANI, VERSIONE_TERMINI, type Periodo } from "@imieiconcorsi/core/domain";
import { avvisaAdmin, inviaEmail } from "@imieiconcorsi/core/email";
import { dataIt } from "@imieiconcorsi/core/email-piani";
import { assegnaPiano } from "@imieiconcorsi/core/piani";
import { premiaChiHaInvitato } from "./inviti";

// Ordini dei piani a pagamento (tabella ordini). Niente dati personali: email e nome stanno
// in Cognito e si leggono al momento della conferma. Il piano si attiva solo da qui.

/** In attesa del pagamento, pagato, sessione di pagamento scaduta senza pagare, pagamento fallito. */
export type StatoOrdine = "in-attesa" | "pagato" | "scaduto" | "fallito";

/** Un tentativo di acquisto di un piano (tabella ordini). */
export interface Ordine {
  /** Codice anonimo, anche su Stripe (client_reference_id) */
  id: string;
  userId: string;
  username: string;
  piano: "medium" | "pro";
  periodo: Periodo;
  /** Prezzo di listino e importo pagato, in euro */
  prezzo: number;
  importo: number;
  codiceSconto?: string;
  percentualeSconto?: number;
  stato: StatoOrdine;
  stripeSessionId?: string;
  /** Consenso all'esecuzione immediata con rinuncia al recesso, dato prima del pagamento */
  consenso: { rinunciaRecesso: true; versioneTermini: string; il: string };
  creatoIl: string;
  aggiornatoIl: string;
  pagatoIl?: string;
  scadenzaPiano?: string;
  /** Come il pagamento ha cambiato il piano: nuovo, aggiunta al piano attuale, passaggio Medium → Pro */
  tipo?: "nuovo" | "aggiunta" | "passaggio";
  /** Passaggio a Pro: giorni Medium rimasti e giorni Pro in cui sono diventati */
  giorniRimasti?: number;
  giorniConvertiti?: number;
  /** Ultimo reinvio della ricevuta chiesto dall'utente (al massimo uno ogni 10 minuti) */
  ricevutaInviataIl?: string;
  /**
   * Email e nome di chi ha comprato, salvati sull'ordine: restano nello storico pagamenti
   * dell'admin anche se l'account viene eliminato (gli ordini si conservano 10 anni).
   */
  email?: string;
  nome?: string;
  /** Esito dell'ultima ricevuta per email: l'admin lo vede nello storico pagamenti */
  ricevuta?: { stato: "inviata" | "non inviata"; motivo?: string; il: string };
}

/** Salva sull'ordine l'esito della ricevuta; se non è partita, avvisa l'admin con il motivo. */
export async function registraRicevuta(o: Ordine, errore: string | undefined) {
  const ricevuta = { stato: errore ? "non inviata" : "inviata", ...(errore ? { motivo: errore } : {}), il: new Date().toISOString() };
  await db
    .send(new UpdateCommand({ TableName: tables.ordini, Key: { id: o.id }, UpdateExpression: "SET ricevuta = :r", ExpressionAttributeValues: { ":r": ricevuta } }))
    .catch((err) => console.error("Esito della ricevuta non salvato", err));
  if (errore) {
    await avvisaAdmin(
      `Ricevuta non inviata (ordine ${o.id})`,
      [`La ricevuta dell'ordine ${o.id} (${o.email ?? o.username}) non è partita: ${errore}.`, "", "Il piano è comunque attivo. Lo vedi anche in Pannello admin → Pagamenti."].join("\n"),
    ).catch(() => {});
  }
}

const euro = (n: number) => n.toLocaleString("it-IT", { style: "currency", currency: "EUR" });

/** Scrive un ordine nuovo. */
export async function salvaOrdine(o: Ordine) {
  await db.send(new PutCommand({ TableName: tables.ordini, Item: o }));
}

/** Un ordine per codice (undefined se non esiste). */
export async function leggiOrdine(id: string) {
  const res = await db.send(new GetCommand({ TableName: tables.ordini, Key: { id } }));
  return res.Item as Ordine | undefined;
}

/** Chiude un ordine non pagato (sessione scaduta o pagamento fallito), solo se era in attesa. */
export async function chiudiOrdine(id: string, stato: "scaduto" | "fallito") {
  try {
    await db.send(
      new UpdateCommand({
        TableName: tables.ordini,
        Key: { id },
        UpdateExpression: "SET stato = :s, aggiornatoIl = :ora",
        ConditionExpression: "stato = :attesa",
        ExpressionAttributeValues: { ":s": stato, ":attesa": "in-attesa", ":ora": new Date().toISOString() },
      }),
    );
  } catch (err) {
    if (!(err instanceof Error && err.name === "ConditionalCheckFailedException")) throw err;
  }
}

/**
 * Pagamento confermato: attiva il piano UNA volta sola, anche se arrivano insieme il webhook
 * di Stripe e la pagina di ritorno (il passaggio "in-attesa" → "pagato" è condizionato).
 * Restituisce l'ordine aggiornato.
 */
export async function completaOrdine(id: string): Promise<Ordine | undefined> {
  const ora = new Date().toISOString();
  let ordine: Ordine;
  try {
    const res = await db.send(
      new UpdateCommand({
        TableName: tables.ordini,
        Key: { id },
        UpdateExpression: "SET stato = :pagato, pagatoIl = :ora, aggiornatoIl = :ora",
        ConditionExpression: "stato = :attesa OR stato = :scaduto",
        ExpressionAttributeValues: { ":pagato": "pagato", ":attesa": "in-attesa", ":scaduto": "scaduto", ":ora": ora },
        ReturnValues: "ALL_NEW",
      }),
    );
    ordine = res.Attributes as Ordine;
  } catch (err) {
    // Già completato (o mai esistito): niente da fare.
    if (err instanceof Error && err.name === "ConditionalCheckFailedException") return leggiOrdine(id);
    throw err;
  }

  // Il piano che ha adesso (gruppo Cognito + scadenza sul profilo): i giorni comprati si
  // aggiungono, o i giorni Medium diventano Pro (core/acquisti.ts). Se nel frattempo l'acquisto
  // non è più "consentito" (caso raro: due ordini incrociati), si paga comunque: si aggiunge il tempo.
  const [gruppi, profilo] = await Promise.all([gruppiDi(ordine.username), getProfilo(ordine.userId)]);
  const attuale = { piano: pianoDaGruppi(gruppi.filter((g) => g !== GRUPPI.admin)), scadenza: profilo?.scadenzaPiano, periodo: profilo?.periodo };
  const calcolato = esitoAcquisto(attuale, { piano: ordine.piano, periodo: ordine.periodo });
  const esito = calcolato.consentito
    ? calcolato
    : {
        tipo: "aggiunta" as const,
        scadenza: new Date(Math.max(Date.now(), Date.parse(attuale.scadenza ?? "") || 0) + durata(ordine.periodo).giorni * 86_400_000).toISOString(),
        giorniRimasti: undefined,
        giorniConvertiti: undefined,
      };
  const scadenza = esito.scadenza;
  await assegnaPiano({ userId: ordine.userId, username: ordine.username, piano: ordine.piano, periodo: ordine.periodo, scadenza });

  // Prova del consenso + codice sconto usato (vale una volta per utente).
  await db.send(
    new UpdateCommand({
      TableName: tables.users,
      Key: { userId: ordine.userId },
      UpdateExpression: ordine.codiceSconto
        ? "SET ultimoAcquisto = :a, codiciUsati = list_append(if_not_exists(codiciUsati, :vuota), :c)"
        : "SET ultimoAcquisto = :a",
      ExpressionAttributeValues: {
        ":a": {
          piano: ordine.piano,
          periodo: ordine.periodo,
          il: ora,
          rinunciaRecesso: true,
          versioneTermini: ordine.consenso.versioneTermini,
          importo: ordine.importo,
          ordine: ordine.id,
          ...(ordine.codiceSconto ? { codiceSconto: ordine.codiceSconto } : {}),
        },
        ...(ordine.codiceSconto ? { ":vuota": [], ":c": [ordine.codiceSconto] } : {}),
      },
    }),
  );
  await db.send(
    new UpdateCommand({
      TableName: tables.ordini,
      Key: { id },
      UpdateExpression: "SET scadenzaPiano = :s, tipo = :t" + (esito.giorniConvertiti !== undefined ? ", giorniRimasti = :r, giorniConvertiti = :c" : ""),
      ExpressionAttributeValues: {
        ":s": scadenza,
        ":t": esito.tipo,
        ...(esito.giorniConvertiti !== undefined ? { ":r": esito.giorniRimasti, ":c": esito.giorniConvertiti } : {}),
      },
    }),
  );
  ordine = { ...ordine, scadenzaPiano: scadenza, tipo: esito.tipo, giorniRimasti: esito.giorniRimasti, giorniConvertiti: esito.giorniConvertiti };

  if (ordine.codiceSconto) {
    // Il pagamento c'è già stato: se nel frattempo il codice si è esaurito, il piano resta valido.
    await db
      .send(
        new UpdateCommand({
          TableName: tables.codici,
          Key: { codice: ordine.codiceSconto },
          UpdateExpression: "SET usi = usi + :uno",
          // Codice eliminato dall'admin nel frattempo: niente da contare (e niente codice "fantasma").
          ConditionExpression: "attribute_exists(codice)",
          ExpressionAttributeValues: { ":uno": 1 },
        }),
      )
      .catch((err) => console.error(`Uso del codice ${ordine.codiceSconto} non conteggiato`, err));
  }

  await registraRicevuta(ordine, await inviaConferma(ordine, scadenza));
  // Primo acquisto di un amico invitato: chi l'ha invitato riceve il suo mese gratis.
  await premiaChiHaInvitato(ordine.userId).catch((err) => console.error("Premio invito non assegnato", err));
  return { ...ordine, scadenzaPiano: scadenza };
}

/** Testo sicuro dentro l'HTML dell'email. */
const html = (t: string) => t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

/** Righe della ricevuta: etichetta e valore, uguali per il testo e per l'HTML. */
function righeRicevuta(o: Ordine, scadenza: string) {
  const p = PIANI[o.piano];
  const sconto = o.codiceSconto ? o.prezzo - o.importo : 0;
  const pagatoConStripe = process.env.BILLING_MODE === "stripe" && o.importo > 0;
  return [
    ["Data", dataIt(o.pagatoIl ?? o.creatoIl)],
    ["Ordine", o.id],
    ["Piano", `${p.nome} · ${durata(o.periodo).nome}`],
    ["Prezzo", euro(o.prezzo)],
    ...(o.codiceSconto ? [["Sconto", `−${euro(sconto)} (${o.percentualeSconto}% con il codice ${o.codiceSconto})`]] : []),
    ["Totale pagato", `${euro(o.importo)} IVA inclusa`],
    ["Pagamento", pagatoConStripe ? "con Stripe (carta, PayPal, Apple Pay o Google Pay)" : "nessun addebito"],
    ["Valido fino al", dataIt(scadenza)],
  ] as const;
}

/** Cosa è successo al piano che c'era già (aggiunta di tempo, passaggio da Medium a Pro). */
function notaPiano(o: Ordine) {
  if (o.tipo === "aggiunta") return `I ${durata(o.periodo).giorni} giorni si sono aggiunti al piano ${PIANI[o.piano].nome} che avevi già.`;
  if (o.tipo === "passaggio") {
    return `I ${o.giorniRimasti} giorni ${PIANI.medium.nome} che ti restavano sono diventati ${o.giorniConvertiti} giorni ${PIANI.pro.nome}, in aggiunta a quelli acquistati.`;
  }
  return undefined;
}

/**
 * Ricevuta dell'acquisto per email (testo e HTML): data, ordine, piano, prezzo, sconto, totale,
 * scadenza, più il consenso alla rinuncia al recesso (supporto durevole). Non è una fattura.
 * Parte al pagamento e, su richiesta, dalla pagina "I tuoi pagamenti". Se non parte restituisce
 * il motivo (e lo scrive nei log) invece di dare errore: un'email mancata non deve bloccare
 * l'attivazione del piano.
 */
export async function inviaConferma(o: Ordine, scadenza: string): Promise<string | undefined> {
  try {
    const utente = await cognito.send(new AdminGetUserCommand({ UserPoolId: userPoolId(), Username: o.username }));
    const email = utente.UserAttributes?.find((a) => a.Name === "email")?.Value;
    if (!email) return "l'account non ha un indirizzo email";
    const sito = process.env.SITE_URL ?? "";
    const righe = righeRicevuta(o, scadenza);
    const nota = notaPiano(o);
    const recesso = [
      "Pagamento unico: il piano NON si rinnova automaticamente. Ti avviseremo 3 giorni prima della scadenza.",
      "Hai chiesto di accedere subito ai contenuti del piano e hai preso atto che, per questo, perdi il diritto di recesso (art. 59, comma 1, lettera o, D.Lgs. 206/2005). Il pagamento non è rimborsabile, salvo i casi previsti dalla legge.",
      `Termini e condizioni, versione ${VERSIONE_TERMINI}: ${sito}/termini`,
    ];
    const fattura = "Questa è una ricevuta di cortesia, non una fattura. Per la fattura o per un problema con il pagamento, scrivici dall'Assistenza dell'app indicando il codice dell'ordine.";
    await inviaEmail({
      a: email,
      oggetto: `Ricevuta del tuo acquisto: piano ${PIANI[o.piano].nome} per ${durata(o.periodo).nome}`,
      testo: [
        "Grazie per il tuo acquisto su iMieiConcorsi. Ecco la ricevuta.",
        "",
        ...righe.map(([k, v]) => `${k}: ${v}`),
        ...(nota ? ["", nota] : []),
        "",
        ...recesso,
        "",
        fattura,
        `I tuoi pagamenti: ${sito}/app/profilo#pagamenti`,
        "",
        "Il team di iMieiConcorsi",
      ].join("\n"),
      html: [
        `<div style="font-family:Arial,Helvetica,sans-serif;max-width:560px;color:#0f172a;line-height:1.5">`,
        `<h1 style="font-size:20px;margin:0 0 4px">Ricevuta di acquisto</h1>`,
        `<p style="margin:0 0 16px;color:#475569">Grazie per il tuo acquisto su iMieiConcorsi.</p>`,
        `<table style="width:100%;border-collapse:collapse;font-size:14px">`,
        ...righe.map(
          ([k, v]) =>
            `<tr><td style="padding:8px 0;border-bottom:1px solid #e2e8f0;color:#64748b;width:40%">${html(k)}</td><td style="padding:8px 0;border-bottom:1px solid #e2e8f0;${k === "Totale pagato" ? "font-weight:bold" : ""}">${html(v)}</td></tr>`,
        ),
        `</table>`,
        nota ? `<p style="margin:16px 0 0;padding:12px;background:#f0fdf4;border-radius:8px;font-size:14px">${html(nota)}</p>` : "",
        `<p style="margin:16px 0 0"><a href="${html(sito)}/app/profilo#pagamenti" style="display:inline-block;background:#1d4ed8;color:#fff;text-decoration:none;padding:10px 16px;border-radius:8px;font-weight:bold">I tuoi pagamenti</a></p>`,
        ...recesso.map((r) => `<p style="margin:16px 0 0;font-size:12px;color:#64748b">${html(r)}</p>`),
        `<p style="margin:16px 0 0;font-size:12px;color:#64748b">${html(fattura)}</p>`,
        `</div>`,
      ].join(""),
    });
    return undefined;
  } catch (err) {
    console.error("Ricevuta dell'acquisto non inviata", err);
    // SES in sandbox scrive solo agli indirizzi verificati: lo si dice chiaramente.
    const messaggio = err instanceof Error ? err.message : String(err);
    return /not verified/i.test(messaggio)
      ? "il servizio email è ancora in modalità di prova e può scrivere solo agli indirizzi verificati"
      : "il servizio email non ha accettato l'invio";
  }
}
