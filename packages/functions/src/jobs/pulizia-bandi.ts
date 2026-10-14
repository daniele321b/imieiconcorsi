import { InvokeCommand, LambdaClient } from "@aws-sdk/client-lambda";
import { BatchWriteCommand, ScanCommand } from "@aws-sdk/lib-dynamodb";
import { inizioBandiScaduti } from "@imieiconcorsi/core/concorsi";
import { db, tables } from "@imieiconcorsi/core/db";
import { avvisaAdmin } from "@imieiconcorsi/core/email";
import type { Context } from "aws-lambda";
import { generaCacheBandi } from "./cache-bandi";
import { importaChiusi } from "./inpa-scraper";

// Domenica e mercoledì alle 3: i bandi che inPA non elenca più spariscono anche da noi.
// 1. Si rilegge l'elenco dei chiusi degli ultimi MESI_DOPO_SCADENZA mesi (circa 300 pagine):
//    ogni bando ancora elencato viene risalvato (aggiornatoIl = adesso). Una Lambda non basta
//    per tutte le pagine: a fine tempo si rilancia da sola dalla pagina successiva.
// 2. Finito il giro, si cancella ogni bando non risalvato da almeno GIORNI_MARGINE giorni:
//    gli aperti li risalva l'import di ogni mattina, i chiusi il giro di oggi.
// Prudenza: se si cancellerebbe più di MAX_QUOTA dei bandi, non si cancella nulla e l'admin
// riceve un'email (inPA potrebbe aver cambiato qualcosa).

/** Un bando sparisce solo se non è stato risalvato da almeno 3 giorni prima del giro. */
const GIORNI_MARGINE = 3;
/** Oltre un quarto dei bandi da cancellare: qualcosa non va, non si cancella nulla. */
const MAX_QUOTA = 0.25;
const lambda = new LambdaClient({});

/** Evento del job: vuoto alla partenza della domenica, poi la pagina da cui riprendere. */
interface Evento {
  daPagina?: number;
  /** Inizio del giro (ISO): uguale per tutti i pezzi dello stesso giro */
  inizio?: string;
}

/** Bandi da cancellare: non risalvati dall'inizio del giro meno il margine. */
export function daCancellare<T extends { aggiornatoIl?: string }>(righe: T[], inizio: string) {
  const limite = new Date(Date.parse(inizio) - GIORNI_MARGINE * 86_400_000).toISOString();
  return righe.filter((r) => !r.aggiornatoIl || r.aggiornatoIl < limite);
}

/** Id e data di aggiornamento di tutti i bandi in tabella. */
async function tutteLeRighe() {
  const out: { id: string; aggiornatoIl?: string }[] = [];
  let ExclusiveStartKey: Record<string, unknown> | undefined;
  do {
    const res = await db.send(new ScanCommand({ TableName: tables.concorsi, ProjectionExpression: "id, aggiornatoIl", ExclusiveStartKey }));
    out.push(...((res.Items ?? []) as typeof out));
    ExclusiveStartKey = res.LastEvaluatedKey;
  } while (ExclusiveStartKey);
  return out;
}

/** Cancella i bandi a blocchi da 25 (il massimo di BatchWrite), riprovando quelli rimasti indietro. */
async function cancella(ids: string[]) {
  for (let i = 0; i < ids.length; i += 25) {
    let pending = ids.slice(i, i + 25).map((id) => ({ DeleteRequest: { Key: { id } } }));
    while (pending.length) {
      const res = await db.send(new BatchWriteCommand({ RequestItems: { [tables.concorsi]: pending } }));
      pending = (res.UnprocessedItems?.[tables.concorsi] ?? []) as typeof pending;
    }
  }
}

/** Entrata del job: rilegge i chiusi; se il tempo non basta si rilancia da solo dalla pagina successiva. */
export const handler = async (event: Evento = {}, context?: Context) => {
  const inizio = event.inizio ?? new Date().toISOString();
  // Millisecondi che restano prima del timeout della Lambda.
  const tempoRimasto = () => context?.getRemainingTimeInMillis() ?? Infinity;

  const giro = await importaChiusi({ daPagina: event.daPagina ?? 0, finoA: inizioBandiScaduti(), maxPagine: Infinity, tempoRimasto });
  if (giro.prossimaPagina !== undefined) {
    // Non è finito: riparte da sola, in modo asincrono, dalla pagina dopo.
    await lambda.send(
      new InvokeCommand({
        FunctionName: context?.functionName ?? process.env.AWS_LAMBDA_FUNCTION_NAME,
        InvocationType: "Event",
        Payload: Buffer.from(JSON.stringify({ daPagina: giro.prossimaPagina, inizio } satisfies Evento)),
      }),
    );
    console.log(`Pulizia: ${giro.totale} chiusi risalvati, continua dalla pagina ${giro.prossimaPagina}`);
    return { continua: giro.prossimaPagina };
  }

  const righe = await tutteLeRighe();
  const via = daCancellare(righe, inizio);
  if (via.length > righe.length * MAX_QUOTA) {
    await avvisaAdmin(
      "Pulizia bandi fermata",
      `La pulizia di oggi cancellerebbe ${via.length} bandi su ${righe.length}: troppi, non ho cancellato nulla. Controlla se inPA ha cambiato qualcosa.`,
    );
    return { fermata: via.length, totale: righe.length };
  }
  await cancella(via.map((r) => r.id));
  console.log(`Pulizia: cancellati ${via.length} bandi non più su inPA, restano ${righe.length - via.length}`);
  await generaCacheBandi();
  return { cancellati: via.length, restano: righe.length - via.length };
};
