import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { BatchGetCommand, type BatchGetCommandOutput, DynamoDBDocumentClient, GetCommand } from "@aws-sdk/lib-dynamodb";
import type { Profilo } from "./domain";
import { env } from "./env";

/** Nomi delle tabelle, passati da Terraform come variabili d'ambiente di ogni Lambda. */
export const tables = {
  get users() {
    return env("USERS_TABLE");
  },
  get concorsi() {
    return env("CONCORSI_TABLE");
  },
  get follows() {
    return env("FOLLOWS_TABLE");
  },
  get questions() {
    return env("QUESTIONS_TABLE");
  },
  get attempts() {
    return env("ATTEMPTS_TABLE");
  },
  get codici() {
    return env("CODICI_TABLE");
  },
  get ordini() {
    return env("ORDINI_TABLE");
  },
  get bancheDati() {
    return env("BANCHE_DATI_TABLE");
  },
  get richieste() {
    return env("RICHIESTE_TABLE");
  },
  get progressi() {
    return env("PROGRESSI_TABLE");
  },
  get contatori() {
    return env("CONTATORI_TABLE");
  },
  get accessi() {
    return env("ACCESSI_TABLE");
  },
};

/** Client DynamoDB che lavora con oggetti JavaScript normali (i campi undefined non si salvano). */
export const db = DynamoDBDocumentClient.from(new DynamoDBClient({}), {
  marshallOptions: { removeUndefinedValues: true },
});

/** BatchGet con gestione del limite di 100 chiavi e delle chiavi non elaborate. */
export async function batchGet<T>(
  table: string,
  keys: Record<string, unknown>[],
  projection?: string,
): Promise<T[]> {
  const out: T[] = [];
  for (let i = 0; i < keys.length; i += 100) {
    let pending: Record<string, unknown>[] | undefined = keys.slice(i, i + 100);
    while (pending?.length) {
      const res: BatchGetCommandOutput = await db.send(new BatchGetCommand({ RequestItems: { [table]: { Keys: pending, ProjectionExpression: projection } } }));
      out.push(...((res.Responses?.[table] ?? []) as T[]));
      pending = res.UnprocessedKeys?.[table]?.Keys;
    }
  }
  return out;
}

/** Profilo di studio dell'utente (tabella users). Il piano NON sta qui: è nei gruppi Cognito. */
export async function getProfilo(userId: string): Promise<Profilo | undefined> {
  const res = await db.send(new GetCommand({ TableName: tables.users, Key: { userId } }));
  return res.Item as Profilo | undefined;
}
