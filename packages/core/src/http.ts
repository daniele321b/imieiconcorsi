import type { APIGatewayProxyEventV2WithJWTAuthorizer, APIGatewayProxyResultV2 } from "aws-lambda";
import { timingSafeEqual } from "node:crypto";
import { registraAttivita } from "./attivita";
import { ZodError, type ZodType } from "zod";
import { GRUPPI, PIANI, pianoDaGruppi, type Limiti, type PianoId } from "./domain";

// Base comune di tutte le API: ogni Lambda di servizio (profile, study, billing…) è creata con
// service() e una mappa di route. Qui si legge il token di Cognito (già verificato dall'API
// Gateway), si ricavano utente, piano e limiti, e si trasformano errori ed esiti in risposte JSON.

/** Evento dell'API Gateway HTTP con il token JWT già verificato dall'authorizer. */
export type Event = APIGatewayProxyEventV2WithJWTAuthorizer;

/**
 * Errore da mostrare all'utente: stato HTTP, messaggio in italiano e un codice facoltativo
 * che il sito usa per reagire (es. LIMITE_PIANO mostra l'invito a cambiare piano).
 */
export class HttpError extends Error {
  constructor(
    public status: number,
    message: string,
    public code?: string,
  ) {
    super(message);
  }
}

/** Errore 404 con un messaggio leggibile, es. notFound("Concorso"). */
export const notFound = (what = "Risorsa") => new HttpError(404, `${what} non trovata`);

/** Contesto di una richiesta, passato a ogni route: chi chiama, con quale piano, e i dati inviati. */
export interface Ctx {
  event: Event;
  /** sub di Cognito: id anonimo usato in tutte le tabelle */
  userId: string;
  /** cognito:username, per le operazioni admin su Cognito */
  username: string;
  email?: string;
  nome?: string;
  gruppi: string[];
  piano: PianoId;
  limiti: Limiti;
  admin: boolean;
  /** Parti variabili del percorso, es. {id} in "GET /concorsi/{id}" */
  params: Record<string, string | undefined>;
  /** Parametri dopo il "?" nell'indirizzo */
  query: Record<string, string | undefined>;
  /** Corpo JSON della richiesta, controllato con uno schema zod (errore 400 se non va bene) */
  body<T>(schema: ZodType<T>): T;
}

/** Una route dell'API: riceve il contesto della richiesta e restituisce il corpo JSON della risposta. */
type Route = (ctx: Ctx) => Promise<unknown>;

/**
 * Gruppi dal claim cognito:groups. L'authorizer JWT dell'API Gateway HTTP passa gli
 * array come stringa ("[admin pro]"); arrivano anche come array o separati da virgole.
 */
export function parseGruppi(claim: unknown): string[] {
  if (Array.isArray(claim)) return claim.map(String);
  if (typeof claim !== "string") return [];
  return claim
    .replace(/^\[|\]$/g, "")
    .split(/[\s,]+/)
    .map((g) => g.trim())
    .filter(Boolean);
}

/** Intestazione che CloudFront aggiunge a ogni chiamata all'API (modules/web, origine "api"). */
export const INTESTAZIONE_ORIGINE = "x-origine-cloudfront";

/**
 * La richiesta è passata da CloudFront? L'API Gateway ha anche un indirizzo pubblico diretto
 * (…execute-api…): chi lo usa salterebbe il WAF e i limiti per IP. CloudFront aggiunge
 * un'intestazione con un segreto (ORIGINE_SEGRETA, da Terraform) e qui la si controlla.
 * Senza segreto configurato (prove in locale) non si controlla nulla.
 */
export function daCloudFront(headers: Record<string, string | undefined> | undefined) {
  const atteso = process.env.ORIGINE_SEGRETA;
  if (!atteso) return true;
  const arrivato = headers?.[INTESTAZIONE_ORIGINE] ?? "";
  const a = Buffer.from(arrivato);
  const b = Buffer.from(atteso);
  return a.length === b.length && timingSafeEqual(a, b);
}

/**
 * Crea l'handler Lambda di un microservizio: una mappa "METODO /path" → funzione,
 * con le stesse chiavi delle route in infra/terraform (environments/<env>/main.tf).
 */
export function service(routes: Record<string, Route>) {
  return async (event: Event): Promise<APIGatewayProxyResultV2> => {
    if (!daCloudFront(event.headers)) return json(403, { error: "Accesso non consentito" });
    const route = routes[event.routeKey];
    if (!route) return json(404, { error: "Route non trovata" });

    const claims = event.requestContext.authorizer.jwt.claims;
    const gruppi = parseGruppi(claims["cognito:groups"]);
    const piano = pianoDaGruppi(gruppi);
    const ctx: Ctx = {
      event,
      userId: String(claims.sub),
      username: String(claims["cognito:username"] ?? claims.sub),
      email: claims.email as string | undefined,
      nome: claims.name as string | undefined,
      gruppi,
      piano,
      limiti: PIANI[piano].limiti,
      admin: gruppi.includes(GRUPPI.admin),
      params: event.pathParameters ?? {},
      query: event.queryStringParameters ?? {},
      body(schema) {
        const raw = event.body
          ? event.isBase64Encoded
            ? Buffer.from(event.body, "base64").toString()
            : event.body
          : "{}";
        return schema.parse(JSON.parse(raw));
      },
    };

    // Utente attivo (pannello admin → Utenti attivi): in parallelo alla risposta, senza farla aspettare.
    const attivita = ctx.admin || !claims.sub ? undefined : registraAttivita(ctx.userId);
    try {
      return json(200, (await route(ctx)) ?? { ok: true });
    } catch (err) {
      if (err instanceof HttpError) return json(err.status, { error: err.message, code: err.code });
      if (err instanceof ZodError) return json(400, { error: "Dati non validi", issues: err.issues });
      if (err instanceof SyntaxError) return json(400, { error: "JSON non valido" });
      console.error(err);
      return json(500, { error: "Errore interno" });
    } finally {
      // La Lambda si "congela" appena risponde: la scrittura va finita prima (non fallisce mai).
      await attivita;
    }
  };
}

/** Da chiamare in testa alle route del pannello di controllo. */
export function richiediAdmin(ctx: Ctx) {
  if (!ctx.admin) throw new HttpError(403, "Riservato agli amministratori", "SOLO_ADMIN");
}

/** Risposta HTTP con corpo JSON. */
function json(statusCode: number, body: unknown): APIGatewayProxyResultV2 {
  return {
    statusCode,
    // L'API passa da CloudFront: nessuna risposta va messa in cache.
    headers: { "content-type": "application/json", "cache-control": "no-store" },
    body: JSON.stringify(body),
  };
}
