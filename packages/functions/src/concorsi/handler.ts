import { GetCommand, PutCommand, QueryCommand } from "@aws-sdk/lib-dynamodb";
import { batchGet, db, getProfilo, tables } from "@imieiconcorsi/core/db";
import { inizioBandiScaduti } from "@imieiconcorsi/core/concorsi";
import { attivi, righeSeguiti, smettiDiSeguire } from "@imieiconcorsi/core/seguiti";
import { COMPARTO_IDS, type CompartoId, type Concorso } from "@imieiconcorsi/core/domain";
import { HttpError, notFound, service } from "@imieiconcorsi/core/http";

// Servizio "concorsi": bandi importati da inPA (lettura) e concorsi seguiti dall'utente.
// La ricerca nel sito legge di solito la lista in cache su CloudFront (jobs/cache-bandi.ts);
// GET /concorsi resta per i filtri per comparto e come riserva se la cache non c'è.
// Seguire un concorso scrive una riga nella tabella follows; smettere la tiene come storico.

/** Bandi aperti al massimo per comparto in una risposta. */
const MAX_PER_COMPARTO = 300;
/**
 * Bandi chiusi in una ricerca: sono decine di migliaia in 18 mesi. Si tengono i più
 * recenti, divisi tra i comparti cercati, per stare sotto i 6 MB di risposta della Lambda.
 */
const MAX_CHIUSI = 3000;

/** Campi delle liste: tutto tranne la descrizione completa (che pesa fino a 4 KB). */
const CAMPI_SINTESI = [
  "id", "titolo", "ente", "sedi", "comparto", "scadenza", "pubblicatoIl", "primoImportoIl", "tipoProcedura",
  "posti", "figura", "url", "materie", "materieStimate", "bancaDatiPrevista", "bancaDati", "bancaDatiId",
  "conclusoIl", "fonte", "aggiornatoIl",
] as const;
// Alcuni nomi (url, …) sono parole riservate di DynamoDB: tutti passano da #n0, #n1…
const proiezione = {
  ProjectionExpression: CAMPI_SINTESI.map((_, i) => `#n${i}`).join(", "),
  nomi: Object.fromEntries(CAMPI_SINTESI.map((c, i) => [`#n${i}`, c])),
};

/** Versione leggera per le liste: senza la descrizione completa. */
const sintesi = ({ descrizione, ...c }: Concorso) => c;

/** Query sull'indice per comparto, pagina dopo pagina, fino a `massimo` bandi. */
async function interroga(input: {
  comparto: CompartoId;
  condizione: string;
  valori: Record<string, unknown>;
  filtro?: string;
  recentiPrima?: boolean;
  massimo: number;
}) {
  const out: Concorso[] = [];
  let ExclusiveStartKey: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new QueryCommand({
        TableName: tables.concorsi,
        IndexName: "byComparto",
        KeyConditionExpression: `comparto = :c AND ${input.condizione}`,
        FilterExpression: input.filtro,
        ProjectionExpression: proiezione.ProjectionExpression,
        ExpressionAttributeNames: proiezione.nomi,
        ExpressionAttributeValues: { ":c": input.comparto, ...input.valori },
        ScanIndexForward: !input.recentiPrima,
        Limit: input.massimo - out.length,
        ExclusiveStartKey,
      }),
    );
    out.push(...((res.Items ?? []) as Concorso[]));
    ExclusiveStartKey = res.LastEvaluatedKey;
  } while (ExclusiveStartKey && out.length < input.massimo);
  return out;
}

/** Bandi di un comparto con le domande ancora aperte, dalla scadenza più vicina. */
const concorsiAperti = (comparto: CompartoId) =>
  interroga({ comparto, condizione: "scadenza >= :oggi", valori: { ":oggi": new Date().toISOString() }, massimo: MAX_PER_COMPARTO });

/** Scaduti da poco (fino a MESI_DOPO_SCADENZA mesi) e non segnati come conclusi, i più recenti prima. */
const concorsiScaduti = (comparto: CompartoId, massimo: number) =>
  interroga({
    comparto,
    condizione: "scadenza BETWEEN :da AND :oggi",
    filtro: "attribute_not_exists(conclusoIl)",
    valori: { ":da": inizioBandiScaduti(), ":oggi": new Date().toISOString() },
    recentiPrima: true,
    massimo,
  });

/** Id dei concorsi che l'utente segue adesso (senza lo storico). */
async function idSeguiti(userId: string) {
  return attivi(await righeSeguiti(userId)).map((r) => r.concorsoId);
}

/** Nome da ricordare nello storico: resta anche se il bando sparisce. */
const nomeConcorso = (c: Pick<Concorso, "ente" | "figura" | "titolo">) => `${c.ente} — ${c.figura ?? c.titolo}`.slice(0, 300);

export const handler = service({
  /**
   * ?comparto=enti-locali, ?comparto=tutti — senza parametro usa gli interessi dell'utente.
   * ?scaduti=1 aggiunge i bandi con le domande già chiuse ma il concorso non ancora finito;
   * ?scaduti=solo restituisce soltanto quelli.
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

    const aperti = query.scaduti !== "solo";
    const chiusi = query.scaduti === "1" || query.scaduti === "solo";
    const chiusiPerComparto = Math.ceil(MAX_CHIUSI / comparti.length);
    const [liste, seguiti] = await Promise.all([
      Promise.all(
        comparti.flatMap((c) => [
          ...(aperti ? [concorsiAperti(c)] : []),
          ...(chiusi ? [concorsiScaduti(c, chiusiPerComparto)] : []),
        ]),
      ),
      idSeguiti(userId),
    ]);
    const concorsi = liste
      .flat()
      .sort((a, b) => (a.scadenza ?? "").localeCompare(b.scadenza ?? ""))
      .map((c) => ({ ...c, seguito: seguiti.includes(c.id) }));
    return { concorsi };
  },

  /**
   * Un bando con tutti i dettagli (anche la descrizione), se l'utente lo segue e, se ha una
   * banca dati ufficiale collegata, il suo titolo (per il link alla consultazione).
   */
  "GET /concorsi/{id}": async ({ userId, params }) => {
    const [res, seguiti] = await Promise.all([
      db.send(new GetCommand({ TableName: tables.concorsi, Key: { id: params.id } })),
      idSeguiti(userId),
    ]);
    if (!res.Item) throw notFound("Concorso");
    const concorso = res.Item as Concorso;
    const banca = concorso.bancaDatiId
      ? await db.send(new GetCommand({ TableName: tables.bancheDati, Key: { id: concorso.bancaDatiId }, ProjectionExpression: "titolo, domande, stato" }))
      : undefined;
    const pubblicata = banca?.Item?.stato === "pubblicata";
    return {
      ...concorso,
      seguito: seguiti.includes(params.id!),
      ...(pubblicata ? { bancaDatiTitolo: banca!.Item!.titolo as string, bancaDatiDomande: banca!.Item!.domande as number } : {}),
    };
  },

  /** I concorsi seguiti dall'utente, dalla scadenza più vicina (dashboard e studio). */
  "GET /me/concorsi": async ({ userId }) => {
    const ids = await idSeguiti(userId);
    const concorsi = await batchGet<Concorso>(tables.concorsi, ids.map((id) => ({ id })));
    return {
      concorsi: concorsi
        .map((c) => ({ ...sintesi(c), seguito: true }))
        .sort((a, b) => (a.scadenza ?? "").localeCompare(b.scadenza ?? "")),
    };
  },

  /** Segue un concorso, nei limiti del piano (Free: uno solo). */
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
    // Riscrive la riga anche se era nello storico: torna seguito, con la data di oggi.
    await db.send(
      new PutCommand({
        TableName: tables.follows,
        Item: { userId, concorsoId, dal: new Date().toISOString(), titolo: nomeConcorso(concorso.Item as Concorso) },
      }),
    );
    return { ok: true };
  },

  /** Storico: tutti i concorsi seguiti, anche quelli non più seguiti, dal più recente. */
  "GET /me/storico-concorsi": async ({ userId }) => {
    const righe = await righeSeguiti(userId);
    // Righe di prima dello storico: il nome si prende dal bando, se c'è ancora.
    const senzaNome = righe.filter((r) => !r.titolo);
    const bandi = await batchGet<Concorso>(tables.concorsi, senzaNome.map((r) => ({ id: r.concorsoId })), "id, ente, figura, titolo");
    const nomi = new Map(bandi.map((c) => [c.id, nomeConcorso(c)]));
    return {
      storico: righe
        .map((r) => ({ concorsoId: r.concorsoId, titolo: r.titolo ?? nomi.get(r.concorsoId) ?? r.concorsoId, dal: r.dal, seguito: !r.rimossoIl }))
        .sort((a, b) => b.dal.localeCompare(a.dal)),
    };
  },

  /** Smette di seguire: la riga resta nello storico con la data di rimozione. */
  "DELETE /me/concorsi/{id}": async ({ userId, params }) => {
    await smettiDiSeguire(userId, params.id!);
    return { ok: true };
  },
});
