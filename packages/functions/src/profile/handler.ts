import { BatchWriteCommand, DeleteCommand, PutCommand, QueryCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { aggiornaNome, eliminaUtenteCognito } from "@imieiconcorsi/core/cognito";
import { db, getProfilo, tables } from "@imieiconcorsi/core/db";
import {
  COMPARTO_IDS,
  feedbackModificabileDal,
  GIORNI_TRA_FEEDBACK,
  MATERIA_IDS,
  VERSIONE_TERMINI,
  type Profilo,
  type Utente,
} from "@imieiconcorsi/core/domain";
import { avvisaAdmin } from "@imieiconcorsi/core/email";
import { dataIt } from "@imieiconcorsi/core/email-piani";
import { type Ctx, HttpError, service } from "@imieiconcorsi/core/http";
import { z } from "zod";

const ProfiloInput = z.object({
  nome: z.string().trim().max(80).optional(),
  interessi: z.array(z.enum(COMPARTO_IDS)).min(1, "Scegli almeno un comparto"),
  livelli: z.partialRecord(z.enum(MATERIA_IDS), z.number().int().min(1).max(5)),
  avvisi: z.enum(["giornaliero", "settimanale", "mai"]),
  /** Spuntato nell'onboarding: Termini e Informativa nella versione corrente */
  accettaTermini: z.literal(true).optional(),
});

const FeedbackInput = z.object({
  voto: z.number().int().min(1).max(5),
  testo: z.string().trim().max(1000).optional(),
});

/** Profilo di studio + identità e piano dal token (email, nome e gruppi stanno solo in Cognito). */
const utente = (ctx: Ctx, profilo: Profilo, nome = ctx.nome): Utente => ({
  ...profilo,
  email: ctx.email,
  nome,
  piano: ctx.piano,
  admin: ctx.admin,
  limiti: ctx.limiti,
});

/** Tutte le righe di un utente in una tabella con chiave composta (userId + sortKey). */
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

export const handler = service({
  // Il profilo nasce al primo accesso, qualunque sia il metodo di login.
  "GET /me": async (ctx) => {
    let profilo = await getProfilo(ctx.userId);
    if (!profilo) {
      const now = new Date().toISOString();
      profilo = {
        userId: ctx.userId,
        username: ctx.username,
        onboarded: false,
        interessi: [],
        livelli: {},
        avvisi: "settimanale",
        createdAt: now,
        updatedAt: now,
      } satisfies Profilo;
      await db
        .send(
          new PutCommand({
            TableName: tables.users,
            Item: profilo,
            ConditionExpression: "attribute_not_exists(userId)",
          }),
        )
        .catch((err) => {
          // Due richieste parallele al primo accesso: va bene, il profilo esiste già.
          if (err.name !== "ConditionalCheckFailedException") throw err;
        });
    }
    return utente(ctx, profilo);
  },

  /** Parere sull'app: una modifica ogni 15 giorni, e l'admin riceve un'email. */
  "PUT /me/feedback": async (ctx) => {
    const { voto, testo } = ctx.body(FeedbackInput);
    const profilo = await getProfilo(ctx.userId);
    const dal = feedbackModificabileDal(profilo?.feedback);
    if (dal) throw new HttpError(429, `Puoi modificare il tuo parere una volta ogni ${GIORNI_TRA_FEEDBACK} giorni: di nuovo dal ${dataIt(dal)}.`);

    const feedback = { voto, ...(testo ? { testo } : {}), il: new Date().toISOString() };
    await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: ctx.userId },
        UpdateExpression: "SET feedback = :f",
        ConditionExpression: "attribute_exists(userId)",
        ExpressionAttributeValues: { ":f": feedback },
      }),
    );
    try {
      await avvisaAdmin(
        `Feedback ${"★".repeat(voto)}${"☆".repeat(5 - voto)}`,
        [`Voto: ${voto}/5 (piano ${ctx.piano})`, "", testo || "(nessun commento)", "", `Utente: ${ctx.email ?? ctx.username}`].join("\n"),
      );
    } catch (err) {
      console.error("Avviso feedback all'admin non inviato", err);
    }
    return feedback;
  },

  "PUT /me/profilo": async (ctx) => {
    const input = ctx.body(ProfiloInput);
    // Il nome è un dato personale: va su Cognito, non nel database.
    if (input.nome && input.nome !== ctx.nome) await aggiornaNome(ctx.username, input.nome);

    const now = new Date().toISOString();
    const res = await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: ctx.userId },
        UpdateExpression:
          "SET interessi = :i, livelli = :l, avvisi = :a, onboarded = :t, updatedAt = :u" +
          (input.accettaTermini ? ", terminiAccettati = :termini" : ""),
        ConditionExpression: "attribute_exists(userId)",
        ExpressionAttributeValues: {
          ":i": input.interessi,
          ":l": input.livelli,
          ":a": input.avvisi,
          ":t": true,
          ":u": now,
          ...(input.accettaTermini ? { ":termini": { versione: VERSIONE_TERMINI, il: now } } : {}),
        },
        ReturnValues: "ALL_NEW",
      }),
    );
    return utente(ctx, res.Attributes as Profilo, input.nome || ctx.nome);
  },

  /**
   * Eliminazione dell'account (diritto alla cancellazione, richiesta anche da Facebook):
   * dati di studio, concorsi seguiti, profilo e infine l'utente Cognito con email e nome.
   * I dati dei pagamenti restano solo sulla piattaforma di pagamento, per obblighi fiscali.
   */
  "DELETE /me": async (ctx) => {
    await eliminaRighe(tables.attempts, "id", ctx.userId);
    await eliminaRighe(tables.follows, "concorsoId", ctx.userId);
    await db.send(new DeleteCommand({ TableName: tables.users, Key: { userId: ctx.userId } }));
    await eliminaUtenteCognito(ctx.username);
    console.log(`Account eliminato: ${ctx.userId}`);
    return { ok: true };
  },
});
