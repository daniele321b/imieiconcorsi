import { PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { QueryCommand } from "@aws-sdk/lib-dynamodb";
import { CAMPI_LISTA, inizioBandiScaduti, type ConcorsoInLista } from "@imieiconcorsi/core/concorsi";
import { db, tables } from "@imieiconcorsi/core/db";
import { COMPARTO_IDS, type CompartoId } from "@imieiconcorsi/core/domain";
import { env } from "@imieiconcorsi/core/env";
import { gzipSync } from "node:zlib";

// Lista dei bandi in cache: dopo ogni import si scrive un file per comparto nel bucket del
// sito, servito da CloudFront sotto /dati/bandi/. La ricerca dell'app legge questi file
// invece di interrogare DynamoDB a ogni visita.
//
//   dati/bandi/indice.json               mai in cache: dice qual è la versione corrente
//   dati/bandi/<versione>/<comparto>.json  gzip, in cache per sempre (una versione non cambia)
//
// Le versioni vecchie le cancella una regola di scadenza del bucket (modules/web).

const s3 = new S3Client({});

/** Il file indice.json: versione corrente e, per comparto, il file da scaricare. */
export interface IndiceBandi {
  versione: string;
  generatoIl: string;
  comparti: Record<CompartoId, { file: string; bandi: number }>;
}

/** Bandi aperti e chiusi da meno di MESI_DOPO_SCADENZA mesi, non conclusi, di un comparto. */
async function bandiDelComparto(comparto: CompartoId) {
  const out: ConcorsoInLista[] = [];
  const nomi = Object.fromEntries(CAMPI_LISTA.map((c, i) => [`#c${i}`, c]));
  let ExclusiveStartKey: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new QueryCommand({
        TableName: tables.concorsi,
        IndexName: "byComparto",
        KeyConditionExpression: "comparto = :c AND scadenza >= :da",
        FilterExpression: "attribute_not_exists(conclusoIl)",
        ProjectionExpression: Object.keys(nomi).join(", "),
        ExpressionAttributeNames: nomi,
        ExpressionAttributeValues: { ":c": comparto, ":da": inizioBandiScaduti() },
        ExclusiveStartKey,
      }),
    );
    out.push(...((res.Items ?? []) as ConcorsoInLista[]));
    ExclusiveStartKey = res.LastEvaluatedKey;
  } while (ExclusiveStartKey);
  return out;
}

/** Scrive una nuova versione dei file per comparto e poi l'indice che la rende attiva. */
export async function generaCacheBandi(ora = new Date()) {
  const bucket = env("WEB_BUCKET");
  const versione = ora.toISOString().replace(/[-:]/g, "").slice(0, 13); // es. 20261009T0612
  const comparti = {} as IndiceBandi["comparti"];

  for (const comparto of COMPARTO_IDS) {
    const bandi = await bandiDelComparto(comparto);
    const file = `dati/bandi/${versione}/${comparto}.json`;
    await s3.send(
      new PutObjectCommand({
        Bucket: bucket,
        Key: file,
        Body: gzipSync(JSON.stringify(bandi)),
        ContentType: "application/json",
        ContentEncoding: "gzip",
        CacheControl: "public, max-age=31536000, immutable",
      }),
    );
    comparti[comparto] = { file: `/${file}`, bandi: bandi.length };
  }

  const indice: IndiceBandi = { versione, generatoIl: ora.toISOString(), comparti };
  await s3.send(
    new PutObjectCommand({
      Bucket: bucket,
      Key: "dati/bandi/indice.json",
      Body: JSON.stringify(indice),
      ContentType: "application/json",
      CacheControl: "no-cache",
    }),
  );
  const totale = Object.values(comparti).reduce((n, c) => n + c.bandi, 0);
  console.log(`Cache bandi ${versione}: ${totale} bandi in ${COMPARTO_IDS.length} file`);
  return { versione, totale };
}
