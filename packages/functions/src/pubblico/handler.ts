import { UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { db, tables } from "@imieiconcorsi/core/db";
import { firmaValida, LETTURA_AVVISI, percorsoSicuro, valoriLettura } from "@imieiconcorsi/core/disiscrizione";
import type { APIGatewayProxyEventV2, APIGatewayProxyResultV2 } from "aws-lambda";

// Rotte SENZA login (authorization NONE nell'API Gateway): solo cose protette da firma.
//
// POST /pubblico/disiscrivi?u=<userId>&t=<firma>
//   - dalla pagina /disiscrivi del sito (u e t anche nel corpo JSON);
//   - dai provider di posta per la disiscrizione in un clic (RFC 8058: corpo
//     "List-Unsubscribe=One-Click", parametri nell'URL).
// GET /pubblico/aperto?u=&t=        immagine invisibile negli avvisi: la persona li legge
// GET /pubblico/clic?u=&t=&vai=/…   link degli avvisi: lettura registrata, poi la pagina del sito

/** Risposta JSON senza cache. */
const json = (statusCode: number, body: unknown): APIGatewayProxyResultV2 => ({
  statusCode,
  headers: { "content-type": "application/json", "cache-control": "no-store" },
  body: JSON.stringify(body),
});

/** Id utente (u) e firma (t): dall'indirizzo o, dalla pagina del sito, dal corpo JSON. */
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

/** GIF trasparente 1x1. */
const PIXEL = "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7";

/** Avvisi letti: il contatore dei non aperti torna a zero. Firma sbagliata = niente, senza errori. */
async function registraLettura(u: string | undefined, t: string | undefined) {
  if (!u || !t || u.length > 100 || t.length > 100 || !firmaValida(u, t, undefined, "aperto")) return;
  await db
    .send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: u },
        UpdateExpression: LETTURA_AVVISI,
        ConditionExpression: "attribute_exists(userId)",
        ExpressionAttributeValues: valoriLettura(),
      }),
    )
    .catch((err) => {
      if (!(err instanceof Error && err.name === "ConditionalCheckFailedException")) console.error("Lettura avviso non registrata", err);
    });
}

export const handler = async (event: APIGatewayProxyEventV2): Promise<APIGatewayProxyResultV2> => {
  const q = event.queryStringParameters ?? {};
  if (event.routeKey === "GET /pubblico/aperto") {
    await registraLettura(q.u, q.t);
    return {
      statusCode: 200,
      headers: { "content-type": "image/gif", "cache-control": "no-store" },
      body: PIXEL,
      isBase64Encoded: true,
    };
  }
  if (event.routeKey === "GET /pubblico/clic") {
    await registraLettura(q.u, q.t);
    return { statusCode: 302, headers: { location: percorsoSicuro(q.vai), "cache-control": "no-store" } };
  }
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
