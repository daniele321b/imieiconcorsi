import { GetCommand, PutCommand, QueryCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { db, tables } from "@imieiconcorsi/core/db";
import { nomeTipoRichiesta, TIPO_RICHIESTA_IDS, type Richiesta } from "@imieiconcorsi/core/domain";
import { avvisaAdmin } from "@imieiconcorsi/core/email";
import { HttpError, notFound, service, type Ctx } from "@imieiconcorsi/core/http";
import { sortableId } from "@imieiconcorsi/core/ids";
import { z } from "zod";

// Richieste di assistenza degli utenti registrati: banca dati da aggiungere, domanda
// sbagliata, problemi di accesso o di pagamento… Ogni richiesta è un filo di messaggi tra
// l'utente e l'assistenza; l'admin risponde dal pannello (servizio admin) e riceve un'email
// per ogni nuova richiesta o messaggio dell'utente.

/** Richieste aperte (non chiuse) per utente, e richieste nuove al giorno: contro gli abusi. */
const MAX_APERTE = 5;
const MAX_AL_GIORNO = 10;

/** Dati di una nuova richiesta: tipo, testo e da dove nasce (facoltativo). */
const NuovaRichiesta = z.object({
  tipo: z.enum(TIPO_RICHIESTA_IDS),
  testo: z.string().trim().min(10, "Scrivi almeno qualche parola").max(3000),
  contesto: z
    .object({
      concorsoId: z.string().max(100).optional(),
      bancaDatiId: z.string().max(100).optional(),
      ordineId: z.string().max(100).optional(),
      domanda: z.object({ materia: z.string().max(100), id: z.string().max(100), testo: z.string().max(1500) }).optional(),
    })
    .optional(),
});

/** Un messaggio in più dell'utente in una richiesta esistente. */
const NuovoMessaggio = z.object({ testo: z.string().trim().min(2).max(3000) });

/** Perché l'utente non può aprire un'altra richiesta adesso (undefined = può). */
export function limiteRichieste(tutte: Pick<Richiesta, "stato" | "creataIl">[], ora: Date) {
  if (tutte.filter((r) => r.stato !== "chiusa").length >= MAX_APERTE) {
    return `Hai già ${MAX_APERTE} richieste aperte: aspetta una risposta o aggiungi un messaggio a una di quelle.`;
  }
  const oggi = ora.toISOString().slice(0, 10);
  if (tutte.filter((r) => r.creataIl.startsWith(oggi)).length >= MAX_AL_GIORNO) return "Hai inviato molte richieste oggi: riprova domani.";
  return undefined;
}

/** Tutte le richieste di un utente, dalla più recente. */
async function mieRichieste(userId: string) {
  const out: Richiesta[] = [];
  let ExclusiveStartKey: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new QueryCommand({
        TableName: tables.richieste,
        KeyConditionExpression: "userId = :u",
        ExpressionAttributeValues: { ":u": userId },
        ScanIndexForward: false,
        ExclusiveStartKey,
      }),
    );
    out.push(...((res.Items ?? []) as Richiesta[]));
    ExclusiveStartKey = res.LastEvaluatedKey;
  } while (ExclusiveStartKey);
  return out;
}

/** Una richiesta dell'utente; 404 se non esiste (o non è sua: la chiave contiene il suo id). */
async function leggi(userId: string, id: string) {
  const res = await db.send(new GetCommand({ TableName: tables.richieste, Key: { userId, id } }));
  if (!res.Item) throw notFound("Richiesta");
  return res.Item as Richiesta;
}

/** Email all'admin: chi scrive, il tipo, il testo e da dove nasce la richiesta. */
async function avvisa(ctx: Ctx, r: Richiesta, testo: string, nuova: boolean) {
  const c = r.contesto;
  await avvisaAdmin(
    `${nuova ? "Nuova richiesta" : "Nuovo messaggio"}: ${nomeTipoRichiesta(r.tipo)}`,
    [
      `Da: ${ctx.email ?? ctx.username} (piano ${ctx.piano})`,
      `Tipo: ${nomeTipoRichiesta(r.tipo)}`,
      c?.concorsoId ? `Concorso: ${process.env.SITE_URL ?? ""}/app/concorsi/${c.concorsoId}` : "",
      c?.bancaDatiId ? `Banca dati: ${process.env.SITE_URL ?? ""}/app/banche-dati/${c.bancaDatiId}` : "",
      c?.ordineId ? `Ordine: ${c.ordineId}` : "",
      c?.domanda ? `Domanda (${c.domanda.materia}/${c.domanda.id}): ${c.domanda.testo}` : "",
      "",
      testo,
      "",
      `Rispondi dal pannello: ${process.env.SITE_URL ?? ""}/admin/richieste`,
    ]
      // Niente righe vuote doppie dove manca il contesto.
      .filter((riga, i, righe) => riga !== "" || righe.at(i - 1) !== "")
      .join("\n"),
  ).catch((err) => console.error("Avviso richiesta all'admin non inviato", err));
}

export const handler = service({
  /** Le richieste dell'utente, dalla più recente (senza le chiavi interne). */
  "GET /me/richieste": async ({ userId }) => ({ richieste: (await mieRichieste(userId)).map(({ userId: _, username: __, ...r }) => r) }),

  /** Nuova richiesta: controlla i limiti, la salva e avvisa l'admin per email. */
  "POST /me/richieste": async (ctx) => {
    const input = ctx.body(NuovaRichiesta);
    const ora = new Date();
    const blocco = limiteRichieste(await mieRichieste(ctx.userId), ora);
    if (blocco) throw new HttpError(429, blocco);

    const richiesta: Richiesta = {
      userId: ctx.userId,
      id: sortableId(ora),
      username: ctx.username,
      tipo: input.tipo,
      stato: "aperta",
      ...(input.contesto && Object.keys(input.contesto).length ? { contesto: input.contesto } : {}),
      messaggi: [{ da: "utente", testo: input.testo, il: ora.toISOString() }],
      creataIl: ora.toISOString(),
      aggiornataIl: ora.toISOString(),
    };
    await db.send(new PutCommand({ TableName: tables.richieste, Item: richiesta }));
    await avvisa(ctx, richiesta, input.testo, true);
    const { userId: _, username: __, ...r } = richiesta;
    return r;
  },

  /** L'utente aggiunge un messaggio: una richiesta chiusa si riapre. */
  "POST /me/richieste/{id}/messaggi": async (ctx) => {
    const { testo } = ctx.body(NuovoMessaggio);
    const r = await leggi(ctx.userId, ctx.params.id!);
    if (r.messaggi.length >= 50) throw new HttpError(429, "Questa conversazione è troppo lunga: apri una nuova richiesta.");
    const ora = new Date().toISOString();
    await db.send(
      new UpdateCommand({
        TableName: tables.richieste,
        Key: { userId: ctx.userId, id: r.id },
        UpdateExpression: "SET messaggi = list_append(messaggi, :m), stato = :aperta, aggiornataIl = :o",
        ExpressionAttributeValues: { ":m": [{ da: "utente", testo, il: ora }], ":aperta": r.stato === "chiusa" ? "aperta" : r.stato, ":o": ora },
      }),
    );
    await avvisa(ctx, r, testo, false);
    return { ok: true };
  },

  /** L'utente ha visto la risposta dell'assistenza. */
  "PUT /me/richieste/{id}/letta": async (ctx) => {
    await db
      .send(
        new UpdateCommand({
          TableName: tables.richieste,
          Key: { userId: ctx.userId, id: ctx.params.id },
          UpdateExpression: "REMOVE daLeggere",
          ConditionExpression: "attribute_exists(id)",
        }),
      )
      .catch((err) => {
        if (!(err instanceof Error && err.name === "ConditionalCheckFailedException")) throw err;
      });
    return { ok: true };
  },
});
