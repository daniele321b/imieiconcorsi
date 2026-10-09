import { GetCommand, PutCommand, QueryCommand, ScanCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { batchGet, db, getProfilo, tables } from "@imieiconcorsi/core/db";
import {
  MATERIA_IDS,
  MATERIE,
  PREFISSO_BANCA_DATI,
  REGOLE_DEFAULT,
  type BancaDati,
  type Concorso,
  type Domanda,
  type MateriaId,
  type Sessione,
} from "@imieiconcorsi/core/domain";
import { HttpError, notFound, service } from "@imieiconcorsi/core/http";
import { sortableId, timePrefix } from "@imieiconcorsi/core/ids";
import { z } from "zod";
import { calcolaEsito, pubblica, selezionaDomande } from "./logic";

/** Minuti concessi per domanda nelle simulazioni (60 domande → 60 minuti). */
const MINUTI_PER_DOMANDA = 1;

const NuovaSessione = z.object({
  tipo: z.enum(["studio", "simulazione"]),
  materie: z.array(z.enum(MATERIA_IDS)).min(1).optional(),
  concorsoId: z.string().optional(),
  /** Sessione sulle domande di una banca dati ufficiale (piani Medium e Pro) */
  bancaDatiId: z.string().optional(),
  numero: z.number().int().min(5).max(60).optional(),
});

/** Banche dati pubblicate, per la sezione Banche dati (poche righe: basta uno Scan). */
async function bancheDatiPubblicate() {
  const out: BancaDati[] = [];
  let ExclusiveStartKey: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new ScanCommand({
        TableName: tables.bancheDati,
        FilterExpression: "stato = :p",
        ExpressionAttributeValues: { ":p": "pubblicata" },
        ExclusiveStartKey,
      }),
    );
    out.push(...((res.Items ?? []) as BancaDati[]));
    ExclusiveStartKey = res.LastEvaluatedKey;
  } while (ExclusiveStartKey);
  return out;
}

const Consegna = z.object({
  risposte: z.array(z.number().int().min(0).max(9).nullable()).max(60),
});

/** Domande di una materia della banca statica, o di una banca dati ufficiale (bd#<id>). */
async function domandeDiMateria(materia: MateriaId | string) {
  const items: Domanda[] = [];
  let start: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new QueryCommand({
        TableName: tables.questions,
        KeyConditionExpression: "materia = :m",
        ExpressionAttributeValues: { ":m": materia },
        ExclusiveStartKey: start,
      }),
    );
    items.push(...((res.Items ?? []) as Domanda[]));
    start = res.LastEvaluatedKey;
  } while (start);
  return items;
}

async function getSessione(userId: string, id: string) {
  const res = await db.send(new GetCommand({ TableName: tables.attempts, Key: { userId, id } }));
  if (!res.Item) throw notFound("Sessione");
  return res.Item as Sessione;
}

/** Le domande nell'ordine in cui sono state proposte. */
async function domandeDellaSessione(s: Sessione) {
  const trovate = await batchGet<Domanda>(tables.questions, s.domande);
  const byKey = new Map(trovate.map((d) => [`${d.materia}/${d.id}`, d]));
  return s.domande.map((k) => byKey.get(`${k.materia}/${k.id}`)).filter((d): d is Domanda => !!d);
}

async function simulazioniDellaSettimana(userId: string) {
  const lunedi = new Date();
  lunedi.setUTCHours(0, 0, 0, 0);
  lunedi.setUTCDate(lunedi.getUTCDate() - ((lunedi.getUTCDay() + 6) % 7));
  const res = await db.send(
    new QueryCommand({
      TableName: tables.attempts,
      KeyConditionExpression: "userId = :u AND id >= :da",
      FilterExpression: "tipo = :t",
      ExpressionAttributeValues: { ":u": userId, ":da": timePrefix(lunedi), ":t": "simulazione" },
      Select: "COUNT",
    }),
  );
  return res.Count ?? 0;
}

/** Cosa restituire al client: le soluzioni solo se è studio o se la prova è consegnata. */
async function vista(s: Sessione) {
  const domande = await domandeDellaSessione(s);
  const conSoluzioni = s.tipo === "studio" || s.stato === "consegnata";
  const { userId, ...resto } = s;
  return { ...resto, domande: conSoluzioni ? domande : domande.map(pubblica) };
}

export const handler = service({
  "GET /materie": async ({ userId }) => {
    const profilo = await getProfilo(userId);
    const conteggi = await Promise.all(
      MATERIE.map((m) =>
        db.send(
          new QueryCommand({
            TableName: tables.questions,
            KeyConditionExpression: "materia = :m",
            ExpressionAttributeValues: { ":m": m.id },
            Select: "COUNT",
          }),
        ),
      ),
    );
    // La versione della banca è la stessa per tutte le domande: basta leggerne una.
    const una = await db.send(
      new QueryCommand({
        TableName: tables.questions,
        KeyConditionExpression: "materia = :m",
        ExpressionAttributeValues: { ":m": MATERIE[0].id },
        ProjectionExpression: "versione",
        Limit: 1,
      }),
    );
    return {
      materie: MATERIE.map((m, i) => ({ ...m, domande: conteggi[i].Count ?? 0, livello: profilo?.livelli[m.id] })),
      versione: (una.Items?.[0]?.versione as string | undefined) ?? "v1",
    };
  },

  /** Catalogo per comparto. Lo vedono tutti; aprire una banca dati richiede Medium o Pro. */
  "GET /banche-dati": async () => {
    const banche = await bancheDatiPubblicate();
    return {
      banche: banche
        .map((b) => ({
          id: b.id,
          titolo: b.titolo,
          comparto: b.comparto ?? "altro",
          anno: b.anno,
          materia: b.materia,
          domande: b.domande ?? 0,
          concorsoId: b.concorsoId,
          concorsoTitolo: b.concorsoTitolo,
        }))
        .sort((a, b) => (b.anno ?? 0) - (a.anno ?? 0) || a.titolo.localeCompare(b.titolo)),
    };
  },

  "POST /sessioni": async (ctx) => {
    const input = ctx.body(NuovaSessione);
    const profilo = await getProfilo(ctx.userId);
    if (!profilo) throw new HttpError(409, "Profilo non ancora creato");
    const { limiti } = ctx;

    let materie = input.materie;
    /** Domande ufficiali: banca dati scelta dalla sezione Banche dati, o quella del concorso. */
    let bancaDati: string | undefined;
    let infoBanca: Sessione["bancaDati"];
    if (input.bancaDatiId) {
      if (!limiti.bancheDati) {
        throw new HttpError(403, "Le banche dati ufficiali sono incluse nei piani Medium e Pro.", "LIMITE_PIANO");
      }
      const res = await db.send(new GetCommand({ TableName: tables.bancheDati, Key: { id: input.bancaDatiId } }));
      const banca = res.Item as BancaDati | undefined;
      if (!banca || banca.stato !== "pubblicata") throw notFound("Banca dati");
      bancaDati = `${PREFISSO_BANCA_DATI}${banca.id}`;
      infoBanca = { id: banca.id, titolo: banca.titolo };
      materie ??= banca.materia ? [banca.materia] : [];
    }
    if (input.concorsoId) {
      const res = await db.send(new GetCommand({ TableName: tables.concorsi, Key: { id: input.concorsoId } }));
      if (!res.Item) throw notFound("Concorso");
      const concorso = res.Item as Concorso;
      materie ??= concorso.materie;
      if (!bancaDati && input.tipo === "simulazione" && limiti.bancheDati && concorso.bancaDatiId && !input.materie) {
        bancaDati = `${PREFISSO_BANCA_DATI}${concorso.bancaDatiId}`;
        infoBanca = { id: concorso.bancaDatiId, titolo: "Banca dati ufficiale" };
      }
    }
    if (!materie?.length && !bancaDati) throw new HttpError(400, "Indica le materie, un concorso o una banca dati");

    let numero: number;
    if (input.tipo === "simulazione") {
      if (limiti.simulazioniSettimana !== null) {
        const fatte = await simulazioniDellaSettimana(ctx.userId);
        if (fatte >= limiti.simulazioniSettimana) {
          throw new HttpError(
            403,
            "Hai già usato la simulazione gratuita di questa settimana. Con Medium sono illimitate.",
            "LIMITE_PIANO",
          );
        }
      }
      numero = input.numero ?? 60;
    } else {
      numero = Math.min(input.numero ?? 10, limiti.domandePerSessioneStudio);
    }

    const fonti: string[] = bancaDati ? [bancaDati] : (materie ?? []);
    const perMateria = new Map(
      await Promise.all(fonti.map(async (m) => [m as MateriaId, await domandeDiMateria(m)] as const)),
    );
    const domande = selezionaDomande(perMateria, numero, profilo.livelli);
    if (!domande.length) throw new HttpError(409, "Non ci sono ancora domande per queste materie", "NESSUNA_DOMANDA");

    const now = new Date();
    const sessione: Sessione = {
      userId: ctx.userId,
      id: sortableId(now),
      tipo: input.tipo,
      concorsoId: input.concorsoId,
      materie: materie ?? [],
      ...(infoBanca ? { bancaDati: infoBanca } : {}),
      domande: domande.map(({ materia, id }) => ({ materia, id })),
      stato: "in-corso",
      regole: REGOLE_DEFAULT,
      creataIl: now.toISOString(),
      scadeIl:
        input.tipo === "simulazione"
          ? new Date(now.getTime() + domande.length * MINUTI_PER_DOMANDA * 60_000).toISOString()
          : undefined,
    };
    await db.send(new PutCommand({ TableName: tables.attempts, Item: sessione }));
    return vista(sessione);
  },

  "GET /sessioni/{id}": async ({ userId, params }) => vista(await getSessione(userId, params.id!)),

  "POST /sessioni/{id}/consegna": async (ctx) => {
    const { risposte } = ctx.body(Consegna);
    const sessione = await getSessione(ctx.userId, ctx.params.id!);
    if (sessione.stato === "consegnata") throw new HttpError(409, "Sessione già consegnata");

    // Il timer è lato client: allo scadere il browser consegna da solo.
    const now = new Date();
    const domande = await domandeDellaSessione(sessione);
    const esito = calcolaEsito(domande, risposte, sessione.regole);
    const aggiornata: Sessione = { ...sessione, stato: "consegnata", consegnataIl: now.toISOString(), risposte, esito };

    await db.send(
      new UpdateCommand({
        TableName: tables.attempts,
        Key: { userId: ctx.userId, id: sessione.id },
        UpdateExpression: "SET stato = :s, consegnataIl = :c, risposte = :r, esito = :e",
        ConditionExpression: "stato = :inCorso",
        ExpressionAttributeValues: {
          ":s": "consegnata",
          ":c": aggiornata.consegnataIl,
          ":r": risposte,
          ":e": esito,
          ":inCorso": "in-corso",
        },
      }),
    );
    const { userId, ...resto } = aggiornata;
    return { ...resto, domande };
  },

  "GET /me/statistiche": async ({ userId }) => {
    const res = await db.send(
      new QueryCommand({
        TableName: tables.attempts,
        KeyConditionExpression: "userId = :u",
        ExpressionAttributeValues: { ":u": userId },
        ScanIndexForward: false,
        Limit: 200,
      }),
    );
    const sessioni = ((res.Items ?? []) as Sessione[]).filter((s) => s.stato === "consegnata" && s.esito);

    const materie = new Map<MateriaId, { corrette: number; totale: number }>();
    for (const s of sessioni) {
      for (const m of s.esito!.perMateria) {
        const acc = materie.get(m.materia) ?? { corrette: 0, totale: 0 };
        acc.corrette += m.corrette;
        acc.totale += m.totale;
        materie.set(m.materia, acc);
      }
    }

    return {
      domandeRisposte: [...materie.values()].reduce((n, m) => n + m.totale, 0),
      perMateria: [...materie].map(([materia, v]) => ({
        materia,
        ...v,
        percentuale: Math.round((v.corrette / v.totale) * 100),
      })),
      simulazioni: sessioni
        .filter((s) => s.tipo === "simulazione")
        .slice(0, 20)
        .reverse()
        .map((s) => ({ id: s.id, data: s.consegnataIl!, percentuale: s.esito!.percentuale, superata: s.esito!.superata })),
      recenti: sessioni.slice(0, 5).map((s) => ({
        id: s.id,
        tipo: s.tipo,
        materie: s.materie,
        bancaDati: s.bancaDati?.titolo,
        concorsoId: s.concorsoId,
        data: s.consegnataIl!,
        percentuale: s.esito!.percentuale,
        // Tempo impiegato (le simulazioni hanno un limite; lo studio no).
        durataMs: Date.parse(s.consegnataIl!) - Date.parse(s.creataIl),
      })),
    };
  },
});
