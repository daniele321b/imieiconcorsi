// Ordinamento dei bandi nella ricerca: lo fa il sito sulla lista già scaricata.
import type { CompartoId, Concorso } from "./domain";

/** Ordinamenti tra cui scegliere nella ricerca dei bandi. */
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

/** I campi di un bando nelle liste (file in cache e ricerca): niente descrizione. */
export type ConcorsoInLista = Pick<
  Concorso,
  | "id"
  | "titolo"
  | "ente"
  | "sedi"
  | "comparto"
  | "scadenza"
  | "pubblicatoIl"
  | "tipoProcedura"
  | "posti"
  | "figura"
  | "bancaDatiPrevista"
  | "bancaDati"
  | "bancaDatiId"
>;
/** Gli stessi campi come elenco, per leggerli da DynamoDB e scriverli nel file in cache. */
export const CAMPI_LISTA = [
  "id", "titolo", "ente", "sedi", "comparto", "scadenza", "pubblicatoIl", "tipoProcedura", "posti", "figura", "bancaDatiPrevista", "bancaDati",
  "bancaDatiId",
] as const satisfies readonly (keyof ConcorsoInLista)[];

/** Filtri della ricerca (pannello "Filtri" del sito); un campo assente = filtro spento. */
export interface FiltriConcorsi {
  /** false = nasconde i bandi con le domande ancora aperte (assente = li mostra) */
  aperti?: boolean;
  /** false = nasconde i bandi con le domande chiuse (assente = li mostra) */
  chiusi?: boolean;
  /** Scade entro N giorni da oggi (solo bandi ancora aperti) */
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

/** Bandi che rispettano tutti i filtri attivi. */
export function filtraConcorsi<T extends Filtrabile>(concorsi: readonly T[], f: FiltriConcorsi, ora = new Date()): T[] {
  const sede = f.sede?.trim().toLowerCase();
  return concorsi.filter(
    (c) =>
      (f.aperti !== false || scaduto(c, ora)) &&
      (f.chiusi !== false || !scaduto(c, ora)) &&
      (!f.scadeEntroGiorni ||
        (c.scadenza !== undefined && !scaduto(c, ora) && Date.parse(c.scadenza) - ora.getTime() <= f.scadeEntroGiorni * GIORNO)) &&
      (!f.pubblicatoDaGiorni || (c.pubblicatoIl !== undefined && ora.getTime() - Date.parse(c.pubblicatoIl) <= f.pubblicatoDaGiorni * GIORNO)) &&
      (!f.postiMinimi || (c.posti ?? 0) >= f.postiMinimi) &&
      (!sede || c.sedi.some((s) => s.toLowerCase().includes(sede))) &&
      (!f.procedura || c.tipoProcedura === f.procedura) &&
      (!f.soloBancaDati || c.bancaDatiPrevista || c.bancaDati),
  );
}

/** Quanti filtri sono attivi (per il pulsante "Filtri (2)"): una casella Aperti/Chiusi tolta conta. */
export const filtriAttivi = (f: FiltriConcorsi) =>
  Object.entries(f).filter(([k, v]) => (k === "aperti" || k === "chiusi" ? v === false : v !== undefined && v !== "" && v !== false)).length;

// ── Bandi scaduti ────────────────────────────────────────────────────────────

/**
 * La scadenza è per inviare la domanda, non per prepararsi: un bando scaduto resta
 * consultabile e si può seguire per esercitarsi finché il concorso non è finito.
 * inPA non dice quando finisce: vale la scelta dell'admin ("concluso") o, al massimo,
 * MESI_DOPO_SCADENZA mesi dalla scadenza.
 */
export const MESI_DOPO_SCADENZA = 18;

/** Data più vecchia di scadenza per cui un bando chiuso resta nelle liste. */
export const inizioBandiScaduti = (ora = new Date()) => {
  const d = new Date(ora);
  d.setUTCMonth(d.getUTCMonth() - MESI_DOPO_SCADENZA);
  return d.toISOString();
};

/** true se il termine per inviare la domanda è passato. */
export const scaduto = (c: Pick<Concorso, "scadenza">, ora = new Date()) => c.scadenza !== undefined && Date.parse(c.scadenza) < ora.getTime();

// ── Concorsi da collegare a una banca dati ───────────────────────────────────

/** Parole che non dicono nulla su quale concorso sia (compaiono ovunque). */
const PAROLE_VUOTE = new Set([
  "banca", "banche", "dati", "concorso", "concorsi", "pubblico", "pubblica", "pubblici", "bando", "avviso", "selezione",
  "prova", "prove", "preselettiva", "preselezione", "quiz", "quesiti", "test", "ufficiale", "ufficiali", "esame", "esami",
  "della", "delle", "dello", "degli", "nella", "nelle", "anno", "anni", "posti", "posto", "tempo", "indeterminato",
  "determinato", "pieno", "parziale", "unità", "unita", "profilo", "categoria", "area", "titoli", "copertura",
]);

/** Parole significative di un testo: minuscole, senza accenti, almeno 4 lettere, niente numeri. */
export function paroleChiave(testo: string) {
  return new Set(
    testo
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .split(/[^a-z0-9]+/)
      .filter((p) => p.length >= 4 && !/^\d+$/.test(p) && !PAROLE_VUOTE.has(p)),
  );
}

type Collegabile = Pick<Concorso, "id" | "titolo" | "ente" | "figura" | "comparto" | "scadenza" | "bancaDatiPrevista" | "bancaDati">;

/** Un concorso proposto per una banca dati: punti di somiglianza e se la proposta è forte. */
export interface Suggerimento<T> {
  concorso: T;
  punti: number;
  /** Almeno due parole in comune e il bando cita una banca dati: quasi certamente è lui */
  forte: boolean;
}

/**
 * Concorsi aperti da proporre per una banca dati, dal più somigliante: parole in comune tra il
 * titolo della banca e ente/titolo/figura del bando, più un punto se il bando cita una banca
 * dati, se è dello stesso comparto e se nomina l'anno della banca. Esclusi i chiusi, quelli già
 * collegati (`esclusi`) e quelli che hanno già un'altra banca dati pubblicata.
 */
export function concorsiSuggeriti<T extends Collegabile>(
  banca: { titolo: string; comparto?: CompartoId; anno?: number },
  bandi: readonly T[],
  opzioni: { esclusi?: ReadonlySet<string>; ora?: Date; massimo?: number } = {},
): Suggerimento<T>[] {
  const parole = paroleChiave(banca.titolo);
  if (!parole.size) return [];
  const ora = opzioni.ora ?? new Date();
  const out: Suggerimento<T>[] = [];
  for (const c of bandi) {
    if (opzioni.esclusi?.has(c.id) || c.bancaDati || !c.scadenza || scaduto(c, ora)) continue;
    const delBando = paroleChiave(`${c.ente} ${c.titolo} ${c.figura ?? ""}`);
    const comuni = [...parole].filter((p) => delBando.has(p)).length;
    if (!comuni) continue;
    const punti =
      comuni +
      (c.bancaDatiPrevista ? 1 : 0) +
      (banca.comparto && c.comparto === banca.comparto ? 1 : 0) +
      (banca.anno && `${c.titolo} ${c.figura ?? ""}`.includes(String(banca.anno)) ? 1 : 0);
    out.push({ concorso: c, punti, forte: comuni >= 2 && c.bancaDatiPrevista });
  }
  return out
    .sort((a, b) => b.punti - a.punti || (a.concorso.scadenza ?? "").localeCompare(b.concorso.scadenza ?? ""))
    .slice(0, opzioni.massimo ?? 10);
}
