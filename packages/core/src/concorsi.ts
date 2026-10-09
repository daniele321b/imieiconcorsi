// Ordinamento dei bandi nella ricerca: lo fa il sito sulla lista già scaricata.
import type { Concorso } from "./domain";

export const ORDINAMENTI = [
  { id: "scadenza", nome: "Scadenza più vicina" },
  { id: "pubblicazione", nome: "Usciti di recente" },
  { id: "piu-posti", nome: "Più posti" },
  { id: "meno-posti", nome: "Meno posti" },
] as const;
export type Ordinamento = (typeof ORDINAMENTI)[number]["id"];

type Ordinabile = Pick<Concorso, "scadenza" | "pubblicatoIl" | "posti">;

/**
 * Copia ordinata della lista. I bandi senza il dato usato per ordinare (data o posti
 * mancanti) vanno in fondo; a parità si tiene la scadenza più vicina.
 */
export function ordinaConcorsi<T extends Ordinabile>(concorsi: readonly T[], ordine: Ordinamento, ora = new Date()): T[] {
  const adesso = ora.toISOString();
  // Prima gli aperti (scadenza più vicina), poi quelli con le domande chiuse (chiusi da meno tempo).
  const perScadenza = (a: T, b: T) => {
    const chiusoA = !!a.scadenza && a.scadenza < adesso;
    const chiusoB = !!b.scadenza && b.scadenza < adesso;
    if (chiusoA !== chiusoB) return chiusoA ? 1 : -1;
    return chiusoA ? b.scadenza!.localeCompare(a.scadenza!) : (a.scadenza ?? "9999").localeCompare(b.scadenza ?? "9999");
  };
  const confronta: Record<Ordinamento, (a: T, b: T) => number> = {
    scadenza: perScadenza,
    pubblicazione: (a, b) => (b.pubblicatoIl ?? "").localeCompare(a.pubblicatoIl ?? "") || perScadenza(a, b),
    "piu-posti": (a, b) => (b.posti ?? 0) - (a.posti ?? 0) || perScadenza(a, b),
    // Senza numero di posti in fondo anche qui: non vuol dire "pochi posti".
    "meno-posti": (a, b) => (a.posti ?? Infinity) - (b.posti ?? Infinity) || perScadenza(a, b),
  };
  return [...concorsi].sort(confronta[ordine]);
}

// ── Filtri della ricerca ─────────────────────────────────────────────────────

export interface FiltriConcorsi {
  /** Scade entro N giorni da oggi */
  scadeEntroGiorni?: number;
  /** Pubblicato negli ultimi N giorni */
  pubblicatoDaGiorni?: number;
  postiMinimi?: number;
  /** Testo contenuto in una delle sedi (es. "Lombardia", "Roma") */
  sede?: string;
  /** Codice inPA: ESAMI, TITOLI, TITOLI_ESAMI… */
  procedura?: string;
  /** Solo bandi che citano una banca dati ufficiale */
  soloBancaDati?: boolean;
}

type Filtrabile = Pick<Concorso, "scadenza" | "pubblicatoIl" | "posti" | "sedi" | "tipoProcedura" | "bancaDatiPrevista" | "bancaDati">;

const GIORNO = 86_400_000;

export function filtraConcorsi<T extends Filtrabile>(concorsi: readonly T[], f: FiltriConcorsi, ora = new Date()): T[] {
  const sede = f.sede?.trim().toLowerCase();
  return concorsi.filter(
    (c) =>
      (!f.scadeEntroGiorni || (c.scadenza !== undefined && Date.parse(c.scadenza) - ora.getTime() <= f.scadeEntroGiorni * GIORNO)) &&
      (!f.pubblicatoDaGiorni || (c.pubblicatoIl !== undefined && ora.getTime() - Date.parse(c.pubblicatoIl) <= f.pubblicatoDaGiorni * GIORNO)) &&
      (!f.postiMinimi || (c.posti ?? 0) >= f.postiMinimi) &&
      (!sede || c.sedi.some((s) => s.toLowerCase().includes(sede))) &&
      (!f.procedura || c.tipoProcedura === f.procedura) &&
      (!f.soloBancaDati || c.bancaDatiPrevista || c.bancaDati),
  );
}

/** Quanti filtri sono attivi (per il pulsante "Filtri (2)"). */
export const filtriAttivi = (f: FiltriConcorsi) => Object.values(f).filter((v) => v !== undefined && v !== "" && v !== false).length;

// ── Bandi scaduti ────────────────────────────────────────────────────────────

/**
 * La scadenza è per inviare la domanda, non per prepararsi: un bando scaduto resta
 * consultabile e si può seguire per esercitarsi finché il concorso non è finito.
 * inPA non dice quando finisce: vale la scelta dell'admin ("concluso") o, al massimo,
 * MESI_DOPO_SCADENZA mesi dalla scadenza.
 */
export const MESI_DOPO_SCADENZA = 18;

export const inizioBandiScaduti = (ora = new Date()) => {
  const d = new Date(ora);
  d.setUTCMonth(d.getUTCMonth() - MESI_DOPO_SCADENZA);
  return d.toISOString();
};

export const scaduto = (c: Pick<Concorso, "scadenza">, ora = new Date()) => c.scadenza !== undefined && Date.parse(c.scadenza) < ora.getTime();
