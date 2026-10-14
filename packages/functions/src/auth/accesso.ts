import { PutCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { db, tables } from "@imieiconcorsi/core/db";
import type { PreTokenGenerationTriggerEvent } from "aws-lambda";
import { randomBytes } from "node:crypto";

// Trigger Cognito "pre token generation": parte a ogni rilascio di token. Si registrano solo i
// login veri (non i rinnovi automatici dei token ogni ora): una riga nella tabella accessi, che
// si cancella da sola dopo 12 mesi, e l'ultimo accesso sul profilo. Il pannello admin li mostra.
// Non deve MAI bloccare il login: qualunque errore finisce nei log e il token parte comunque.

/** Giorni di conservazione degli accessi (TTL della tabella). */
const GIORNI = 365;

/** Login con email e password (SRP dal sito) o dal login ospitato di Cognito (Google, Facebook). */
const METODI: Record<string, string> = {
  TokenGeneration_Authentication: "email e password",
  TokenGeneration_NewPasswordChallenge: "email e password",
  TokenGeneration_HostedAuth: "Google o Facebook",
};

/** Registra il login (accesso e ultimo accesso sul profilo) e restituisce sempre l'evento, anche se fallisce. */
export const handler = async (event: PreTokenGenerationTriggerEvent) => {
  const metodo = METODI[event.triggerSource];
  const userId = event.request.userAttributes.sub;
  if (!metodo || !userId) return event;
  try {
    const ora = new Date();
    await Promise.all([
      db.send(
        new PutCommand({
          TableName: tables.accessi,
          // Chiave ordinabile per data, unica anche per due accessi nello stesso millisecondo.
          Item: { userId, il: `${ora.toISOString()}#${randomBytes(2).toString("hex")}`, metodo, scade: Math.floor(ora.getTime() / 1000) + GIORNI * 86_400 },
        }),
      ),
      db
        .send(
          new UpdateCommand({
            TableName: tables.users,
            Key: { userId },
            UpdateExpression: "SET ultimoAccessoIl = :o, accessi = if_not_exists(accessi, :zero) + :uno",
            // Al primissimo login il profilo non esiste ancora (nasce con GET /me): niente.
            ConditionExpression: "attribute_exists(userId)",
            ExpressionAttributeValues: { ":o": ora.toISOString(), ":zero": 0, ":uno": 1 },
          }),
        )
        .catch((err) => {
          if (!(err instanceof Error && err.name === "ConditionalCheckFailedException")) throw err;
        }),
    ]);
  } catch (err) {
    console.error("Accesso non registrato", err);
  }
  return event;
};
