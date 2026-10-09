import { QueryCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { db, tables } from "./db";

// Concorsi seguiti (tabella follows). Smettere di seguire non cancella la riga: resta lo
// storico (nome del concorso e giorno in cui lo si è seguito), visibile nel profilo.

/** Una riga della tabella follows: un concorso seguito (o seguito in passato) da un utente. */
export interface Seguito {
  userId: string;
  concorsoId: string;
  /** Ultima volta che l'utente l'ha seguito (ISO) */
  dal: string;
  /** "Ente — figura": resta anche se il bando sparisce da inPA */
  titolo?: string;
  /** Presente = non lo segue più (storico) */
  rimossoIl?: string;
  /** Tolto in automatico al ritorno al piano Free */
  rimossoPerPiano?: boolean;
}

/** Tutte le righe dell'utente, seguiti attivi e storico. */
export async function righeSeguiti(userId: string) {
  const out: Seguito[] = [];
  let ExclusiveStartKey: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new QueryCommand({
        TableName: tables.follows,
        KeyConditionExpression: "userId = :u",
        ExpressionAttributeValues: { ":u": userId },
        ExclusiveStartKey,
      }),
    );
    out.push(...((res.Items ?? []) as Seguito[]));
    ExclusiveStartKey = res.LastEvaluatedKey;
  } while (ExclusiveStartKey);
  return out;
}

/** Solo i concorsi seguiti adesso (senza lo storico). */
export const attivi = (righe: Seguito[]) => righe.filter((r) => !r.rimossoIl);

/** Quali concorsi smettere di seguire per tenerne `quanti`: si tengono i più recenti. */
export function daTogliere(righe: Seguito[], quanti: number) {
  return attivi(righe)
    .sort((a, b) => b.dal.localeCompare(a.dal))
    .slice(quanti);
}

/** Smette di seguire (la riga resta nello storico). */
export async function smettiDiSeguire(userId: string, concorsoId: string, perPiano = false) {
  await db
    .send(
      new UpdateCommand({
        TableName: tables.follows,
        Key: { userId, concorsoId },
        UpdateExpression: perPiano ? "SET rimossoIl = :o, rimossoPerPiano = :si" : "SET rimossoIl = :o",
        ConditionExpression: "attribute_exists(userId) AND attribute_not_exists(rimossoIl)",
        ExpressionAttributeValues: { ":o": new Date().toISOString(), ...(perPiano ? { ":si": true } : {}) },
      }),
    )
    .catch((err) => {
      if (!(err instanceof Error && err.name === "ConditionalCheckFailedException")) throw err;
    });
}

/** Ritorno al Free: resta seguito solo il concorso seguito per ultimo. */
export async function riduciSeguiti(userId: string, quanti: number) {
  const togliere = daTogliere(await righeSeguiti(userId), quanti);
  for (const r of togliere) await smettiDiSeguire(userId, r.concorsoId, true);
  return togliere.length;
}
