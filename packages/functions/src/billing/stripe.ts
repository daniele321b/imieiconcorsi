import { createHmac, timingSafeEqual } from "node:crypto";
import { env } from "@imieiconcorsi/core/env";

// Stripe Checkout con chiamate dirette all'API REST (niente SDK: due chiamate in tutto).
// Documentazione: https://docs.stripe.com/api/checkout/sessions

const API = "https://api.stripe.com/v1";

/** Importo minimo che Stripe accetta in euro. */
export const MINIMO_STRIPE = 0.5;

/** I campi che usiamo di una sessione di Stripe Checkout (la pagina di pagamento). */
export interface SessioneStripe {
  id: string;
  url: string | null;
  /** "open" | "complete" | "expired" */
  status: string;
  /** "paid" | "unpaid" | "no_payment_required" */
  payment_status: string;
  client_reference_id: string | null;
}

/** Parametri annidati nel formato che vuole Stripe: line_items[0][price_data][currency]=eur */
export function formEncode(obj: Record<string, unknown>, prefisso = ""): string[] {
  return Object.entries(obj).flatMap(([k, v]) => {
    const chiave = prefisso ? `${prefisso}[${k}]` : k;
    if (v === undefined || v === null) return [];
    if (typeof v === "object") return formEncode(v as Record<string, unknown>, chiave);
    return [`${encodeURIComponent(chiave)}=${encodeURIComponent(String(v))}`];
  });
}

/** Chiamata all'API di Stripe con la chiave segreta; con `idempotenza` Stripe non la ripete due volte. */
async function chiama<T>(metodo: "GET" | "POST", percorso: string, parametri?: Record<string, unknown>, idempotenza?: string): Promise<T> {
  const res = await fetch(`${API}${percorso}`, {
    method: metodo,
    headers: {
      authorization: `Bearer ${env("STRIPE_SECRET_KEY")}`,
      ...(parametri ? { "content-type": "application/x-www-form-urlencoded" } : {}),
      ...(idempotenza ? { "idempotency-key": idempotenza } : {}),
    },
    body: parametri ? formEncode(parametri).join("&") : undefined,
  });
  const dati = (await res.json()) as T & { error?: { message?: string } };
  if (!res.ok) throw new Error(`Stripe ${res.status}: ${dati.error?.message ?? "errore"}`);
  return dati;
}

/** Crea la pagina di pagamento per un ordine; l'utente ci viene mandato dal sito. */
export function creaSessione(args: {
  ordineId: string;
  email?: string;
  descrizione: string;
  centesimi: number;
  ritorno: string;
  annullato: string;
}) {
  return chiama<SessioneStripe>(
    "POST",
    "/checkout/sessions",
    {
      mode: "payment",
      locale: "it",
      client_reference_id: args.ordineId,
      customer_email: args.email,
      success_url: args.ritorno,
      cancel_url: args.annullato,
      // La sessione resta aperta un'ora; poi l'ordine scade (evento checkout.session.expired).
      expires_at: Math.floor(Date.now() / 1000) + 3600,
      line_items: {
        0: { quantity: 1, price_data: { currency: "eur", unit_amount: args.centesimi, product_data: { name: args.descrizione } } },
      },
      // Nella dashboard Stripe ogni pagamento dice da quale app arriva.
      metadata: { app: "imieiconcorsi", ordine: args.ordineId },
      payment_intent_data: { description: `iMieiConcorsi — ${args.descrizione}`, metadata: { app: "imieiconcorsi", ordine: args.ordineId } },
    },
    // Lo stesso ordine non crea mai due sessioni.
    `imieiconcorsi-${args.ordineId}`,
  );
}

/** Stato attuale di una sessione di pagamento (per la pagina di ritorno, se il webhook tarda). */
export const leggiSessione = (id: string) => chiama<SessioneStripe>("GET", `/checkout/sessions/${encodeURIComponent(id)}`);

/**
 * Firma dei webhook Stripe: header "Stripe-Signature: t=<secondi>,v1=<hmac>[,v1=…]",
 * HMAC-SHA256 di "<t>.<corpo grezzo>" con il segreto whsec_…; tolleranza 5 minuti.
 * https://docs.stripe.com/webhooks#verify-manually
 */
export function firmaWebhookValida(corpo: string, header: string | undefined, segreto: string, ora = Date.now()) {
  if (!header) return false;
  const parti = header.split(",").map((p) => p.split("=", 2) as [string, string]);
  const t = Number(parti.find(([k]) => k === "t")?.[1]);
  if (!Number.isFinite(t) || Math.abs(ora / 1000 - t) > 300) return false;
  const attesa = Buffer.from(createHmac("sha256", segreto).update(`${t}.${corpo}`).digest("hex"));
  return parti
    .filter(([k]) => k === "v1")
    .some(([, v]) => {
      const ricevuta = Buffer.from(v ?? "");
      return ricevuta.length === attesa.length && timingSafeEqual(ricevuta, attesa);
    });
}
