import { BatchWriteCommand, DeleteCommand, QueryCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { eliminaUtenteCognito } from "./cognito";
import { db, tables } from "./db";

// Eliminazione di un account con tutti i suoi dati: la usano l'utente stesso (DELETE /me,
// servizio profile) e l'admin (DELETE /admin/utenti/{username}). Restano solo gli ordini,
// conservati 10 anni per obbligo contabile, con email e nome di chi ha pagato (vedi Informativa).

/** Tutte le righe di un utente in una tabella con chiave composta (userId + sortKey), 25 alla volta. */
async function eliminaRighe(table: string, sortKey: string, userId: string) {
  let start: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new QueryCommand({
        TableName: table,
        KeyConditionExpression: "userId = :u",
        ExpressionAttributeValues: { ":u": userId },
        ProjectionExpression: `userId, ${sortKey}`,
        ExclusiveStartKey: start,
      }),
    );
    const chiavi = res.Items ?? [];
    for (let i = 0; i < chiavi.length; i += 25) {
      let pending = chiavi.slice(i, i + 25).map((Key) => ({ DeleteRequest: { Key } }));
      while (pending.length) {
        const out = await db.send(new BatchWriteCommand({ RequestItems: { [table]: pending } }));
        pending = (out.UnprocessedItems?.[table] ?? []) as typeof pending;
      }
    }
    start = res.LastEvaluatedKey;
  } while (start);
}

/**
 * Gli ordini restano 10 anni: prima di cancellare l'utente Cognito ci si scrive email e nome
 * (per quelli fatti prima che si salvassero all'acquisto), così l'admin li ritrova nello storico.
 */
async function firmaOrdini(userId: string, persona: { email?: string; nome?: string }) {
  if (!persona.email && !persona.nome) return;
  let start: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new QueryCommand({
        TableName: tables.ordini,
        IndexName: "perUtente",
        KeyConditionExpression: "userId = :u",
        ExpressionAttributeValues: { ":u": userId },
        ProjectionExpression: "id",
        ExclusiveStartKey: start,
      }),
    );
    for (const { id } of (res.Items ?? []) as { id: string }[]) {
      await db.send(
        new UpdateCommand({
          TableName: tables.ordini,
          Key: { id },
          UpdateExpression: "SET email = if_not_exists(email, :e), nome = if_not_exists(nome, :n), accountEliminatoIl = :o",
          ExpressionAttributeValues: { ":e": persona.email ?? "", ":n": persona.nome ?? "", ":o": new Date().toISOString() },
        }),
      );
    }
    start = res.LastEvaluatedKey;
  } while (start);
}

/**
 * Cancella l'account: sessioni, concorsi seguiti, richieste di assistenza, progressi nelle
 * banche dati, profilo e per ultimo l'utente Cognito (email, nome, login). Non si annulla.
 */
export async function eliminaAccount(userId: string, username: string, persona: { email?: string; nome?: string } = {}) {
  await firmaOrdini(userId, persona);
  await eliminaRighe(tables.attempts, "id", userId);
  await eliminaRighe(tables.follows, "concorsoId", userId);
  await eliminaRighe(tables.richieste, "id", userId);
  await eliminaRighe(tables.progressi, "bancaId", userId);
  await eliminaRighe(tables.accessi, "il", userId);
  await db.send(new DeleteCommand({ TableName: tables.users, Key: { userId } }));
  await eliminaUtenteCognito(username);
}
