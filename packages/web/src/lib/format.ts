// Formattazione all'italiana di date, importi e durate, usata in tutte le pagine.
import { scadenzaDiComodo } from "@imieiconcorsi/core/concorsi";

const dataFmt = new Intl.DateTimeFormat("it-IT", { day: "numeric", month: "long", year: "numeric" });
const dataBreveFmt = new Intl.DateTimeFormat("it-IT", { day: "numeric", month: "short" });
const dataOraFmt = new Intl.DateTimeFormat("it-IT", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
const euroFmt = new Intl.NumberFormat("it-IT", { style: "currency", currency: "EUR" });

/** "9 ottobre 2026" ("—" se manca). */
export const data = (iso?: string) => (iso ? dataFmt.format(new Date(iso)) : "—");
/** "9 ott". */
export const dataBreve = (iso?: string) => (iso ? dataBreveFmt.format(new Date(iso)) : "—");
/** "9 ott, 14:30". */
export const dataOra = (iso?: string) => (iso ? dataOraFmt.format(new Date(iso)) : "—");
/** "9,99 €". */
export const euro = (n: number) => euroFmt.format(n);

/** Giorni da oggi alla data (negativi se è passata; undefined se manca). */
export function giorniA(iso?: string) {
  // Scadenze di comodo di inPA (2099, 4999…): il bando non ha un termine.
  if (!iso || scadenzaDiComodo(iso)) return undefined;
  return Math.ceil((new Date(iso).getTime() - Date.now()) / 86_400_000);
}

/** Scadenza di un bando a parole: "Scade tra 5 giorni", "Scade oggi", "Domande chiuse". */
export function scadenzaTesto(iso?: string) {
  if (scadenzaDiComodo(iso)) return "Senza scadenza";
  const g = giorniA(iso);
  if (g === undefined) return "Scadenza non indicata";
  // Scaduto il termine per la domanda: il bando resta, ci si può ancora esercitare.
  if (g < 0) return "Domande chiuse";
  if (g === 0) return "Scade oggi";
  if (g === 1) return "Scade domani";
  return `Scade tra ${g} giorni`;
}

/** Nomi leggibili dei tipi di procedura di inPA. */
const PROCEDURE: Record<string, string> = {
  ESAMI: "Esami",
  TITOLI: "Titoli",
  TITOLI_ESAMI: "Titoli ed esami",
  COLLOQUIO: "Colloquio",
  TITOLI_COLLOQUIO: "Titoli e colloquio",
};
/** Tipo di procedura leggibile ("TITOLI_ESAMI" → "Titoli ed esami"). */
export const tipoProcedura = (t?: string) => (t ? (PROCEDURE[t] ?? t.replace(/_/g, " ").toLowerCase()) : undefined);

/** Durata come cronometro: "04:05" o "1:04:05". */
export function durata(ms: number) {
  const s = Math.max(0, Math.floor(ms / 1000));
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = s % 60;
  const mm = String(m).padStart(2, "0");
  const ss = String(sec).padStart(2, "0");
  return h ? `${h}:${mm}:${ss}` : `${mm}:${ss}`;
}
