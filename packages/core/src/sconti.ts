// Regole dei codici sconto, senza dipendenze AWS: le usano billing, admin e il sito.
import type { CodiceSconto, PianoId } from "./domain";

/** Codice inserito dall'utente → forma salvata (maiuscole, senza spazi). */
export const normalizzaCodice = (codice: string) => codice.trim().toUpperCase().replace(/\s+/g, "");

/** Forma valida di un codice scelto dall'admin: 4-24 tra lettere maiuscole, numeri e trattino. */
export const FORMATO_CODICE = /^[A-Z0-9-]{4,24}$/;

/** Alfabeto senza caratteri ambigui (0/O, 1/I/L). */
const ALFABETO = "ABCDEFGHJKMNPQRSTUVWXYZ23456789";

/** Codice casuale leggibile, es. "K7MQ-2XRT". */
export function generaCodice(casuale: () => number = Math.random) {
  // Quattro caratteri a caso dall'alfabeto senza simboli ambigui.
  const pezzo = () => Array.from({ length: 4 }, () => ALFABETO[Math.floor(casuale() * ALFABETO.length)]).join("");
  return `${pezzo()}-${pezzo()}`;
}

/** Prezzo dopo lo sconto, arrotondato al centesimo (calcolo in centesimi: niente errori di virgola mobile). */
export const prezzoScontato = (prezzo: number, percentuale: number) =>
  Math.round((Math.round(prezzo * 100) * (100 - percentuale)) / 100) / 100;

/**
 * Motivo per cui il codice non vale per questo acquisto, oppure null se vale.
 * I messaggi finiscono così come sono all'utente.
 */
export function motivoRifiuto(
  c: CodiceSconto | undefined,
  { piano, codiciUsati = [], oggi = new Date() }: { piano: PianoId; codiciUsati?: string[]; oggi?: Date },
): string | null {
  if (c?.tipo === "invito") return "Questo è un codice invito di un amico: inseriscilo nel profilo, sezione Invita un amico.";
  if (!c || !c.attivo) return "Codice sconto non valido.";
  if (c.validoFino && Date.parse(c.validoFino) < oggi.getTime()) return "Questo codice sconto è scaduto.";
  if (c.usiMassimi !== undefined && c.usi >= c.usiMassimi) return "Questo codice sconto è esaurito.";
  if (piano === "free") return "Il codice sconto vale solo sui piani a pagamento.";
  if (c.piani?.length && !c.piani.includes(piano)) {
    return `Questo codice vale solo per il piano ${c.piani.map((p) => (p === "pro" ? "Pro" : "Medium")).join(" o ")}.`;
  }
  if (codiciUsati.includes(c.codice)) return "Hai già usato questo codice sconto.";
  return null;
}
