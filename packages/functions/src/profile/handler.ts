import { PutCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { aggiornaNome } from "@imieiconcorsi/core/cognito";
import { db, getProfilo, tables } from "@imieiconcorsi/core/db";
import { COMPARTO_IDS, MATERIA_IDS, type Profilo, type Utente } from "@imieiconcorsi/core/domain";
import { type Ctx, service } from "@imieiconcorsi/core/http";
import { z } from "zod";

const ProfiloInput = z.object({
  nome: z.string().trim().max(80).optional(),
  interessi: z.array(z.enum(COMPARTO_IDS)).min(1, "Scegli almeno un comparto"),
  livelli: z.partialRecord(z.enum(MATERIA_IDS), z.number().int().min(1).max(5)),
  avvisi: z.enum(["giornaliero", "settimanale", "mai"]),
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

  "PUT /me/profilo": async (ctx) => {
    const input = ctx.body(ProfiloInput);
    // Il nome è un dato personale: va su Cognito, non nel database.
    if (input.nome && input.nome !== ctx.nome) await aggiornaNome(ctx.username, input.nome);

    const res = await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: ctx.userId },
        UpdateExpression: "SET interessi = :i, livelli = :l, avvisi = :a, onboarded = :t, updatedAt = :u",
        ConditionExpression: "attribute_exists(userId)",
        ExpressionAttributeValues: {
          ":i": input.interessi,
          ":l": input.livelli,
          ":a": input.avvisi,
          ":t": true,
          ":u": new Date().toISOString(),
        },
        ReturnValues: "ALL_NEW",
      }),
    );
    return utente(ctx, res.Attributes as Profilo, input.nome || ctx.nome);
  },
});
