import { UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { db, tables } from "@imieiconcorsi/core/db";
import { firmaValida, LETTURA_AVVISI, percorsoSicuro, valoriLettura } from "@imieiconcorsi/core/disiscrizione";
import { avvisaAdmin } from "@imieiconcorsi/core/email";
import { env } from "@imieiconcorsi/core/env";
import type { APIGatewayProxyEventV2, APIGatewayProxyResultV2 } from "aws-lambda";
import { createHmac } from "node:crypto";
import { z } from "zod";

// Rotte SENZA login (authorization NONE nell'API Gateway): solo cose protette da firma.
//
// POST /pubblico/disiscrivi?u=<userId>&t=<firma>
//   - dalla pagina /disiscrivi del sito (u e t anche nel corpo JSON);
//   - dai provider di posta per la disiscrizione in un clic (RFC 8058: corpo
//     "List-Unsubscribe=One-Click", parametri nell'URL).
// GET /pubblico/aperto?u=&t=        immagine invisibile negli avvisi: la persona li legge
// GET /pubblico/clic?u=&t=&vai=/…   link degli avvisi: lettura registrata, poi la pagina del sito
// POST /pubblico/contatto            modulo della pagina /contatti: il messaggio arriva all'admin
//                                    (topic SNS, niente SES); al massimo 5 l'ora per indirizzo IP

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

// ── Modulo contatti ──────────────────────────────────────────────────────────

const Contatto = z.object({
  nome: z.string().trim().min(2, "Scrivi il tuo nome").max(100),
  email: z.email("Email non valida").max(200),
  argomento: z.enum(["informazioni", "account", "pagamenti", "privacy", "segnalazione", "altro"]),
  messaggio: z.string().trim().min(10, "Scrivi qualche parola in più").max(3000),
  /** Campo nascosto: lo compilano solo i programmi automatici */
  sito: z.string().max(0).optional(),
});

/** Messaggi accettati per indirizzo IP in un'ora. */
const CONTATTI_ORA = 5;

/**
 * Massimo CONTATTI_ORA messaggi l'ora per IP. Si salva solo un'impronta dell'IP (HMAC con il
 * segreto dei link), che si cancella da sola dopo un giorno (TTL "scade" della tabella contatori).
 */
async function entroIlLimite(event: APIGatewayProxyEventV2) {
  // Dietro CloudFront il primo indirizzo di x-forwarded-for è quello di chi scrive.
  const ip = event.headers["x-forwarded-for"]?.split(",")[0]?.trim() || event.requestContext.http.sourceIp;
  const impronta = createHmac("sha256", env("DISISCRIZIONE_SECRET")).update(ip).digest("hex").slice(0, 32);
  const ora = new Date().toISOString().slice(0, 13);
  try {
    await db.send(
      new UpdateCommand({
        TableName: tables.contatori,
        Key: { id: `contatto#${impronta}#${ora}` },
        UpdateExpression: "ADD n :uno SET scade = :scade",
        ConditionExpression: "attribute_not_exists(n) OR n < :max",
        ExpressionAttributeValues: { ":uno": 1, ":max": CONTATTI_ORA, ":scade": Math.floor(Date.now() / 1000) + 86_400 },
      }),
    );
    return true;
  } catch (err) {
    if (err instanceof Error && err.name === "ConditionalCheckFailedException") return false;
    throw err;
  }
}

async function contatto(event: APIGatewayProxyEventV2) {
  let dati: unknown;
  try {
    dati = JSON.parse(event.isBase64Encoded ? Buffer.from(event.body ?? "", "base64").toString() : (event.body ?? ""));
  } catch {
    return json(400, { error: "Richiesta non valida" });
  }
  const letto = Contatto.safeParse(dati);
  if (!letto.success) return json(400, { error: letto.error.issues[0]?.message ?? "Dati non validi" });
  // Campo nascosto compilato: è un programma. Risposta di successo, così non riprova.
  if (letto.data.sito) return json(200, { ok: true });
  if (!(await entroIlLimite(event))) return json(429, { error: "Hai già scritto più volte nell'ultima ora: riprova più tardi." });
  const { nome, email, argomento, messaggio } = letto.data;
  await avvisaAdmin(
    `Contatto dal sito (${argomento}): ${nome}`,
    [`Da: ${nome} <${email}>`, `Argomento: ${argomento}`, "", messaggio, "", "Rispondi direttamente a questo indirizzo email."].join("\n"),
  );
  return json(200, { ok: true });
}

export const handler = async (event: APIGatewayProxyEventV2): Promise<APIGatewayProxyResultV2> => {
  const q = event.queryStringParameters ?? {};
  if (event.routeKey === "POST /pubblico/contatto") {
    try {
      return await contatto(event);
    } catch (err) {
      console.error("Contatto non inviato", err);
      return json(500, { error: "Messaggio non inviato per un errore nostro: riprova tra poco." });
    }
  }
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
