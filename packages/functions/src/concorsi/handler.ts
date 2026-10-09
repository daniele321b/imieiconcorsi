import { DeleteCommand, GetCommand, PutCommand, QueryCommand } from "@aws-sdk/lib-dynamodb";
import { batchGet, db, getProfilo, tables } from "@imieiconcorsi/core/db";
import { inizioBandiScaduti } from "@imieiconcorsi/core/concorsi";
import { COMPARTO_IDS, type CompartoId, type Concorso } from "@imieiconcorsi/core/domain";
import { HttpError, notFound, service } from "@imieiconcorsi/core/http";

const MAX_PER_COMPARTO = 300;

/** Versione leggera per le liste: senza la descrizione completa. */
const sintesi = ({ descrizione, ...c }: Concorso) => c;

async function concorsiAperti(comparto: CompartoId) {
  const res = await db.send(
    new QueryCommand({
      TableName: tables.concorsi,
      IndexName: "byComparto",
      KeyConditionExpression: "comparto = :c AND scadenza >= :oggi",
      ExpressionAttributeValues: { ":c": comparto, ":oggi": new Date().toISOString() },
      Limit: MAX_PER_COMPARTO,
    }),
  );
  return (res.Items ?? []) as Concorso[];
}

/** Scaduti da poco (fino a MESI_DOPO_SCADENZA mesi) e non segnati come conclusi, i più recenti prima. */
async function concorsiScaduti(comparto: CompartoId) {
  const res = await db.send(
    new QueryCommand({
      TableName: tables.concorsi,
      IndexName: "byComparto",
      KeyConditionExpression: "comparto = :c AND scadenza BETWEEN :da AND :oggi",
      FilterExpression: "attribute_not_exists(conclusoIl)",
      ExpressionAttributeValues: { ":c": comparto, ":da": inizioBandiScaduti(), ":oggi": new Date().toISOString() },
      ScanIndexForward: false,
      Limit: MAX_PER_COMPARTO,
    }),
  );
  return (res.Items ?? []) as Concorso[];
}

async function idSeguiti(userId: string) {
  const res = await db.send(
    new QueryCommand({
      TableName: tables.follows,
      KeyConditionExpression: "userId = :u",
      ExpressionAttributeValues: { ":u": userId },
    }),
  );
  return (res.Items ?? []).map((i) => i.concorsoId as string);
}

export const handler = service({
  /**
   * ?comparto=enti-locali, ?comparto=tutti — senza parametro usa gli interessi dell'utente.
   * ?scaduti=1 aggiunge i bandi con le domande già chiuse ma il concorso non ancora finito.
   */
  "GET /concorsi": async ({ userId, query }) => {
    let comparti: CompartoId[];
    if (query.comparto === "tutti") {
      comparti = [...COMPARTO_IDS];
    } else if (query.comparto) {
      if (!COMPARTO_IDS.includes(query.comparto as CompartoId)) throw new HttpError(400, "Comparto sconosciuto");
      comparti = [query.comparto as CompartoId];
    } else {
      const profilo = await getProfilo(userId);
      comparti = profilo?.interessi.length ? profilo.interessi : [...COMPARTO_IDS];
    }

    const conScaduti = query.scaduti === "1";
    const [liste, seguiti] = await Promise.all([
      Promise.all(comparti.flatMap((c) => (conScaduti ? [concorsiAperti(c), concorsiScaduti(c)] : [concorsiAperti(c)]))),
      idSeguiti(userId),
    ]);
    const concorsi = liste
      .flat()
      .sort((a, b) => (a.scadenza ?? "").localeCompare(b.scadenza ?? ""))
      .map((c) => ({ ...sintesi(c), seguito: seguiti.includes(c.id) }));
    return { concorsi };
  },

  "GET /concorsi/{id}": async ({ userId, params }) => {
    const [res, seguiti] = await Promise.all([
      db.send(new GetCommand({ TableName: tables.concorsi, Key: { id: params.id } })),
      idSeguiti(userId),
    ]);
    if (!res.Item) throw notFound("Concorso");
    return { ...(res.Item as Concorso), seguito: seguiti.includes(params.id!) };
  },

  "GET /me/concorsi": async ({ userId }) => {
    const ids = await idSeguiti(userId);
    const concorsi = await batchGet<Concorso>(tables.concorsi, ids.map((id) => ({ id })));
    return {
      concorsi: concorsi
        .map((c) => ({ ...sintesi(c), seguito: true }))
        .sort((a, b) => (a.scadenza ?? "").localeCompare(b.scadenza ?? "")),
    };
  },

  "PUT /me/concorsi/{id}": async ({ userId, params, limiti }) => {
    const concorsoId = params.id!;
    const [concorso, seguiti] = await Promise.all([
      db.send(new GetCommand({ TableName: tables.concorsi, Key: { id: concorsoId } })),
      idSeguiti(userId),
    ]);
    if (!concorso.Item) throw notFound("Concorso");
    if (seguiti.includes(concorsoId)) return { ok: true };
    if (limiti.concorsiSeguiti !== null && seguiti.length >= limiti.concorsiSeguiti) {
      throw new HttpError(
        403,
        `Con il tuo piano puoi seguire ${limiti.concorsiSeguiti} concorso. Passa a Medium per seguirne quanti vuoi.`,
        "LIMITE_PIANO",
      );
    }
    await db.send(
      new PutCommand({
        TableName: tables.follows,
        Item: { userId, concorsoId, dal: new Date().toISOString() },
      }),
    );
    return { ok: true };
  },

  "DELETE /me/concorsi/{id}": async ({ userId, params }) => {
    await db.send(new DeleteCommand({ TableName: tables.follows, Key: { userId, concorsoId: params.id } }));
    return { ok: true };
  },
});
