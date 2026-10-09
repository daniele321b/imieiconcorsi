import { GetObjectCommand, ListObjectsV2Command, S3Client } from "@aws-sdk/client-s3";
import { BatchWriteCommand, QueryCommand } from "@aws-sdk/lib-dynamodb";
import { db, tables } from "@imieiconcorsi/core/db";
import { FileDomandeSchema } from "@imieiconcorsi/core/domande";
import { env } from "@imieiconcorsi/core/env";
import type { S3Event } from "aws-lambda";

// Importa la banca domande statica: un file JSON per materia (domande/<materia>.json nel
// bucket dei contenuti, caricato da Terraform da data/domande/). Il file è la fonte di
// verità: le domande che non ci sono più vengono tolte dalla tabella.

const s3 = new S3Client({});
const PREFISSO = "domande/";

async function scriviABlocchi(richieste: Record<string, unknown>[]) {
  for (let i = 0; i < richieste.length; i += 25) {
    let pending = richieste.slice(i, i + 25);
    while (pending.length) {
      const res = await db.send(new BatchWriteCommand({ RequestItems: { [tables.questions]: pending } }));
      pending = (res.UnprocessedItems?.[tables.questions] ?? []) as typeof pending;
    }
  }
}

async function idEsistenti(materia: string) {
  const ids: string[] = [];
  let start: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new QueryCommand({
        TableName: tables.questions,
        KeyConditionExpression: "materia = :m",
        ExpressionAttributeValues: { ":m": materia },
        ProjectionExpression: "id",
        ExclusiveStartKey: start,
      }),
    );
    ids.push(...(res.Items ?? []).map((i) => i.id as string));
    start = res.LastEvaluatedKey;
  } while (start);
  return ids;
}

export async function importaFile(bucket: string, key: string) {
  const materia = key.slice(PREFISSO.length).replace(/\.json$/, "");
  const obj = await s3.send(new GetObjectCommand({ Bucket: bucket, Key: key }));
  const domande = FileDomandeSchema.parse(JSON.parse(await obj.Body!.transformToString()));
  const fuoriPosto = domande.filter((d) => d.materia !== materia);
  if (fuoriPosto.length) throw new Error(`${key}: ${fuoriPosto.length} domande di un'altra materia`);

  const nelFile = new Set(domande.map((d) => d.id));
  const daTogliere = (await idEsistenti(materia)).filter((id) => !nelFile.has(id));

  await scriviABlocchi(domande.map((Item) => ({ PutRequest: { Item } })));
  await scriviABlocchi(daTogliere.map((id) => ({ DeleteRequest: { Key: { materia, id } } })));
  console.log(`${materia}: ${domande.length} domande, ${daTogliere.length} tolte`);
  return { materia, domande: domande.length, tolte: daTogliere.length };
}

/** Evento S3 (un file caricato) oppure invocazione a mano senza evento: reimporta tutto. */
export const handler = async (event?: Partial<S3Event>) => {
  const bucket = env("CONTENUTI_BUCKET");
  let keys = (event?.Records ?? [])
    .map((r) => decodeURIComponent(r.s3.object.key.replace(/\+/g, " ")))
    .filter((k) => k.startsWith(PREFISSO) && k.endsWith(".json"));

  if (!event?.Records) {
    const lista = await s3.send(new ListObjectsV2Command({ Bucket: bucket, Prefix: PREFISSO }));
    keys = (lista.Contents ?? []).map((o) => o.Key!).filter((k) => k.endsWith(".json"));
  }

  const risultati = [];
  for (const key of keys) risultati.push(await importaFile(bucket, key));
  return risultati;
};
