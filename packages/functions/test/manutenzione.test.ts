import { readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";

// Funzioni CloudFront del sito (infra/terraform/modules/web/functions): manutenzione.js in cima a
// spa.js e api-prefix.js, come le unisce Terraform. Si eseguono con una KeyValueStore finta.
const CARTELLA = join(__dirname, "../../../infra/terraform/modules/web/functions");

type Richiesta = { uri: string; querystring?: Record<string, { value: string }>; cookies?: Record<string, { value: string }> };
type Risposta = { statusCode?: number; headers?: Record<string, { value: string }>; body?: { data: string }; cookies?: Record<string, { value: string }>; uri?: string };

/** Il handler di una funzione, con le chiavi date nella KeyValueStore (chiave assente = errore, come CloudFront). */
function funzione(nome: "spa.js" | "api-prefix.js", chiavi: Record<string, string>) {
  const codice = `${readFileSync(join(CARTELLA, "manutenzione.js"), "utf8")}\n${readFileSync(join(CARTELLA, nome), "utf8")}`
    .replace("import cf from 'cloudfront';", "")
    .concat("\nreturn handler;");
  const cf = {
    kvs: () => ({
      get: async (k: string) => {
        if (!(k in chiavi)) throw new Error("chiave assente");
        return chiavi[k];
      },
    }),
  };
  const handler = new Function("cf", codice)(cf) as (e: { request: Richiesta }) => Promise<Risposta>;
  return (request: Richiesta) => handler({ request: { querystring: {}, cookies: {}, ...request } });
}

describe("manutenzione del sito (CloudFront)", () => {
  it("spenta (chiave assente o 'no'): il sito e l'API funzionano come prima", async () => {
    expect(await funzione("spa.js", {})({ uri: "/app/concorsi/123" })).toMatchObject({ uri: "/index.html" });
    expect(await funzione("spa.js", { attiva: "no" })({ uri: "/assets/x.js" })).toMatchObject({ uri: "/assets/x.js" });
    expect(await funzione("api-prefix.js", {})({ uri: "/api/me" })).toMatchObject({ uri: "/me" });
  });

  it("accesa: pagina 503 con il messaggio (senza HTML), JSON 503 per API e dati", async () => {
    const chiavi = { attiva: "si", messaggio: "Torniamo alle <18:00>" };
    const pagina = await funzione("spa.js", chiavi)({ uri: "/app/studio" });
    expect(pagina.statusCode).toBe(503);
    expect(pagina.headers!["retry-after"]!.value).toBe("1800");
    expect(pagina.body!.data).toContain("Siamo in manutenzione");
    expect(pagina.body!.data).toContain("Torniamo alle &lt;18:00&gt;");

    const api = await funzione("api-prefix.js", chiavi)({ uri: "/api/me" });
    expect(api.statusCode).toBe(503);
    expect(JSON.parse(api.body!.data)).toEqual({ error: "Torniamo alle <18:00>", code: "MANUTENZIONE" });
    // I dati JSON del sito (lista dei bandi, config) rispondono come l'API.
    const dati = await funzione("spa.js", chiavi)({ uri: "/dati/bandi/enti-locali.json" });
    expect(JSON.parse(dati.body!.data).code).toBe("MANUTENZIONE");
  });

  it("senza messaggio usa quello predefinito", async () => {
    const pagina = await funzione("spa.js", { attiva: "si" })({ uri: "/" });
    expect(pagina.body!.data).toContain("Torniamo il prima possibile");
  });

  it("link con il codice di accesso: cookie e poi sito normale; codice sbagliato no", async () => {
    const chiavi = { attiva: "si", accesso: "abc123" };
    const entra = await funzione("spa.js", chiavi)({ uri: "/app", querystring: { accesso: { value: "abc123" } } });
    expect(entra.statusCode).toBe(302);
    expect(entra.headers!.location!.value).toBe("/app");
    expect(entra.cookies!.imc_accesso_manutenzione!.value).toBe("abc123");

    const conCookie = { cookies: { imc_accesso_manutenzione: { value: "abc123" } } };
    expect(await funzione("spa.js", chiavi)({ uri: "/app", ...conCookie })).toMatchObject({ uri: "/index.html" });
    expect(await funzione("api-prefix.js", chiavi)({ uri: "/api/me", ...conCookie })).toMatchObject({ uri: "/me" });
    expect((await funzione("spa.js", chiavi)({ uri: "/app", querystring: { accesso: { value: "sbagliato" } } })).statusCode).toBe(503);
  });

  it("?manutenzione=anteprima mostra la pagina anche a manutenzione spenta", async () => {
    const pagina = await funzione("spa.js", {})({ uri: "/", querystring: { manutenzione: { value: "anteprima" } } });
    expect(pagina.statusCode).toBe(503);
    expect(pagina.body!.data).toContain("Siamo in manutenzione");
  });
});
