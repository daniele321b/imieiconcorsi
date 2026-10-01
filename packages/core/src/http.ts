import type { APIGatewayProxyEventV2WithJWTAuthorizer, APIGatewayProxyResultV2 } from "aws-lambda";
import { ZodError, type ZodType } from "zod";
import { GRUPPI, PIANI, pianoDaGruppi, type Limiti, type PianoId } from "./domain";

export type Event = APIGatewayProxyEventV2WithJWTAuthorizer;

export class HttpError extends Error {
  constructor(
    public status: number,
    message: string,
    public code?: string,
  ) {
    super(message);
  }
}

export const notFound = (what = "Risorsa") => new HttpError(404, `${what} non trovata`);

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
  params: Record<string, string | undefined>;
  query: Record<string, string | undefined>;
  body<T>(schema: ZodType<T>): T;
}

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

/**
 * Crea l'handler Lambda di un microservizio: una mappa "METODO /path" → funzione,
 * con le stesse chiavi delle route in infra/terraform (environments/<env>/main.tf).
 */
export function service(routes: Record<string, Route>) {
  return async (event: Event): Promise<APIGatewayProxyResultV2> => {
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

    try {
      return json(200, (await route(ctx)) ?? { ok: true });
    } catch (err) {
      if (err instanceof HttpError) return json(err.status, { error: err.message, code: err.code });
      if (err instanceof ZodError) return json(400, { error: "Dati non validi", issues: err.issues });
      if (err instanceof SyntaxError) return json(400, { error: "JSON non valido" });
      console.error(err);
      return json(500, { error: "Errore interno" });
    }
  };
}

/** Da chiamare in testa alle route del pannello di controllo. */
export function richiediAdmin(ctx: Ctx) {
  if (!ctx.admin) throw new HttpError(403, "Riservato agli amministratori", "SOLO_ADMIN");
}

function json(statusCode: number, body: unknown): APIGatewayProxyResultV2 {
  return {
    statusCode,
    // L'API passa da CloudFront: nessuna risposta va messa in cache.
    headers: { "content-type": "application/json", "cache-control": "no-store" },
    body: JSON.stringify(body),
  };
}
