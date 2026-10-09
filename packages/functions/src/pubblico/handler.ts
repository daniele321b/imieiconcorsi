import { UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { db, tables } from "@imieiconcorsi/core/db";
import { firmaValida } from "@imieiconcorsi/core/disiscrizione";
import type { APIGatewayProxyEventV2, APIGatewayProxyResultV2 } from "aws-lambda";

// Rotte SENZA login (authorization NONE nell'API Gateway): solo cose protette da firma.
//
// POST /pubblico/disiscrivi?u=<userId>&t=<firma>
//   - dalla pagina /disiscrivi del sito (u e t anche nel corpo JSON);
//   - dai provider di posta per la disiscrizione in un clic (RFC 8058: corpo
//     "List-Unsubscribe=One-Click", parametri nell'URL).

const json = (statusCode: number, body: unknown): APIGatewayProxyResultV2 => ({
  statusCode,
  headers: { "content-type": "application/json", "cache-control": "no-store" },
  body: JSON.stringify(body),
});

function parametri(event: APIGatewayProxyEventV2) {
  let u = event.queryStringParameters?.u;
  let t = event.queryStringParameters?.t;
  if ((!u || !t) && event.body) {
    const testo = event.isBase64Encoded ? Buffer.from(event.body, "base64").toString() : event.body;
    try {
      const dati = JSON.parse(testo) as { u?: unknown; t?: unknown };
      if (typeof dati.u === "string") u = dati.u;
      if (typeof dati.t === "string") t = dati.t;
    } catch {}
  }
  return { u, t };
}

export const handler = async (event: APIGatewayProxyEventV2): Promise<APIGatewayProxyResultV2> => {
  if (event.routeKey !== "POST /pubblico/disiscrivi") return json(404, { error: "Route non trovata" });

  const { u, t } = parametri(event);
  if (!u || !t || u.length > 100 || t.length > 100 || !firmaValida(u, t)) {
    return json(400, { error: "Link non valido: apri quello dell'email più recente." });
  }
  try {
    await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: u },
        UpdateExpression: "SET avvisi = :mai, updatedAt = :ora",
        ConditionExpression: "attribute_exists(userId)",
        ExpressionAttributeValues: { ":mai": "mai", ":ora": new Date().toISOString() },
      }),
    );
  } catch (err) {
    // Account già eliminato: per chi clicca il risultato è lo stesso.
    if (!(err instanceof Error && err.name === "ConditionalCheckFailedException")) {
      console.error("Disiscrizione non riuscita", err);
      return json(500, { error: "Errore interno, riprova tra poco." });
    }
  }
  return json(200, { ok: true });
};
