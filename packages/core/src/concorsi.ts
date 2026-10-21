// Ordinamento dei bandi nella ricerca: lo fa il sito sulla lista già scaricata.
import type { CampoModificabile, CompartoId, Concorso, ModificheConcorso } from "./domain";

/** Ordinamenti tra cui scegliere nella ricerca dei bandi. */
export const ORDINAMENTI = [
  { id: "scadenza", nome: "Scadenza più vicina" },
  { id: "scadenza-lontana", nome: "Scadenza più lontana" },
  { id: "pubblicazione", nome: "Usciti di recente" },
  { id: "pubblicazione-vecchi", nome: "Usciti da più tempo" },
  { id: "piu-posti", nome: "Più posti" },
  { id: "meno-posti", nome: "Meno posti" },
  { id: "nome-az", nome: "Nome dalla A alla Z" },
  { id: "nome-za", nome: "Nome dalla Z alla A" },
] as const;
/** Id di un ordinamento della ricerca dei bandi (scadenza, posti, nome…). */
export type Ordinamento = (typeof ORDINAMENTI)[number]["id"];

/** I campi di un bando che servono a ordinarlo (vanno bene anche i bandi della lista in cache). */
type Ordinabile = Pick<Concorso, "scadenza" | "pubblicatoIl" | "posti"> & Partial<Pick<Concorso, "titolo" | "figura">>;

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
  // Prima gli aperti (scadenza più lontana), poi i chiusi (chiusi da più tempo).
  const perScadenzaLontana = (a: T, b: T) => {
    const chiusoA = !!a.scadenza && a.scadenza < adesso;
    const chiusoB = !!b.scadenza && b.scadenza < adesso;
    if (chiusoA !== chiusoB) return chiusoA ? 1 : -1;
    // Senza scadenza (o con una di comodo) in fondo anche qui.
    const veraA = scadenzaVera(a.scadenza);
    const veraB = scadenzaVera(b.scadenza);
    if (!veraA || !veraB) return veraA ? -1 : veraB ? 1 : 0;
    return chiusoA ? veraA.localeCompare(veraB) : veraB.localeCompare(veraA);
  };
  // Nome con cui si ordina un bando: figura, o titolo se manca.
  const nome = (c: T) => conMaiuscola(c.figura || c.titolo || "");
  // Confronto alfabetico italiano, senza badare a maiuscole e accenti.
  const alfabetico = (x: string, y: string) => x.localeCompare(y, "it", { sensitivity: "base" });
  const confronta: Record<Ordinamento, (a: T, b: T) => number> = {
    scadenza: perScadenza,
    "scadenza-lontana": perScadenzaLontana,
    // Senza data di pubblicazione in fondo, come per "usciti di recente".
    "pubblicazione-vecchi": (a, b) =>
      (a.pubblicatoIl ?? "9999").localeCompare(b.pubblicatoIl ?? "9999") || perScadenza(a, b),
    "nome-az": (a, b) => alfabetico(nome(a), nome(b)) || perScadenza(a, b),
    "nome-za": (a, b) => alfabetico(nome(b), nome(a)) || perScadenza(a, b),
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
// ── Tipi di bando ────────────────────────────────────────────────────────────
// inPA pubblica anche mobilità, selezioni a tempo determinato, incarichi, tirocini e procedure
// interne: il tipo si riconosce dal titolo (e dalla figura). Il primo che corrisponde vince.

export const TIPI_BANDO = [
  { id: "tirocinio", nome: "Tirocini e borse", re: /tirocin|borse? di studio|\bstage\b|dottorat|assegn[oi] di ricerca|praticantato|servizio civile/i },
  { id: "mobilita", nome: "Mobilità", re: /mobilit[aà]/i },
  { id: "interno", nome: "Interni e progressioni", re: /progression|riservat[oa] al personale|concorso interno|selezione interna/i },
  { id: "incarico", nome: "Incarichi e collaborazioni", re: /incaric|collaborazion|consulen|co\.?co\.?co|libero.professional|lavoro autonomo/i },
  { id: "tempo-determinato", nome: "Tempo determinato", re: /tempo determinato|\ba termine\b|supplenz|stagional/i },
  { id: "concorso", nome: "Concorsi", re: /./ },
] as const;
/** Id di un tipo di bando (concorso, mobilità, avviso…), riconosciuto dal titolo con TIPI_BANDO. */
export type TipoBando = (typeof TIPI_BANDO)[number]["id"];

/** Tipo di un bando dal titolo e dalla figura cercata. */
export const tipoBando = (c: Pick<Concorso, "titolo" | "figura">): TipoBando =>
  TIPI_BANDO.find((t) => t.re.test(`${c.titolo} ${c.figura ?? ""}`))!.id;

// ── Correzioni dell'admin ────────────────────────────────────────────────────

/**
 * Il bando con le correzioni dell'admin applicate. Si ricordano i valori di partenza (di inPA)
 * dei campi corretti, per poterli rimettere: quelli già ricordati restano, salvo `aggiornaOriginali`
 * (l'import del mattino, che porta i valori freschi di inPA).
 */
export function conModificheAdmin(c: Concorso, modifiche: ModificheConcorso, aggiornaOriginali = false): Concorso {
  const chiavi = Object.keys(modifiche) as CampoModificabile[];
  if (!chiavi.length) return c;
  const originali: Partial<Record<CampoModificabile, unknown>> = aggiornaOriginali ? {} : { ...c.originaliInpa };
  for (const k of chiavi) if (!(k in originali)) originali[k] = c[k] ?? null;
  return { ...c, ...modifiche, modificheAdmin: modifiche, originaliInpa: originali };
}

/** Il bando senza le correzioni dell'admin: tornano i valori di inPA. */
export function senzaModificheAdmin(c: Concorso): Concorso {
  const { modificheAdmin: _m, originaliInpa, modificatoIl: _i, ...resto } = c;
  const out: Record<string, unknown> = { ...resto };
  for (const [k, v] of Object.entries(originaliInpa ?? {})) {
    if (v === null) delete out[k];
    else out[k] = v;
  }
  return out as unknown as Concorso;
}

/** Filtri della ricerca dei bandi (pannello Filtri e scelta Tutti/Aperti/Chiusi): assente = nessun filtro. */
export interface FiltriConcorsi {
  /** Solo questi tipi di bando (assente o vuoto = tutti) */
  tipi?: TipoBando[];
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

/** I campi di un bando che servono ai filtri. */
type Filtrabile = Pick<Concorso, "scadenza" | "pubblicatoIl" | "posti" | "sedi" | "tipoProcedura" | "bancaDatiPrevista" | "bancaDati" | "titolo" | "figura">;

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
      (!f.tipi?.length || f.tipi.includes(tipoBando(c))) &&
      (!f.soloBancaDati || c.bancaDatiPrevista || c.bancaDati),
  );
}

/** Quanti filtri sono attivi (per il pulsante "Filtri (2)"): una casella Aperti/Chiusi tolta conta. */
export const filtriAttivi = (f: FiltriConcorsi) =>
  Object.entries(f).filter(([k, v]) =>
    k === "aperti" || k === "chiusi" ? v === false : v !== undefined && v !== "" && v !== false && !(Array.isArray(v) && !v.length),
  ).length;

// ── Bandi scaduti ────────────────────────────────────────────────────────────

/**
 * La scadenza è per inviare la domanda, non per prepararsi: un bando scaduto resta
 * consultabile e si può seguire per esercitarsi finché il concorso non è finito.
 * inPA non dice quando finisce: vale la scelta dell'admin ("concluso") o, al massimo,
 * MESI_DOPO_SCADENZA mesi dalla scadenza.
 */
export const MESI_DOPO_SCADENZA = 24;

/** Data più vecchia di scadenza per cui un bando chiuso resta nelle liste. */
export const inizioBandiScaduti = (ora = new Date()) => {
  const d = new Date(ora);
  d.setUTCMonth(d.getUTCMonth() - MESI_DOPO_SCADENZA);
  return d.toISOString();
};

/** true se il termine per inviare la domanda è passato. */
export const scaduto = (c: Pick<Concorso, "scadenza">, ora = new Date()) => c.scadenza !== undefined && Date.parse(c.scadenza) < ora.getTime();

// ── Scadenze di comodo ───────────────────────────────────────────────────────
// Per i bandi aperti "fino a esaurimento" (avvisi sempre aperti, rilevatori, elenchi) inPA mette
// una scadenza di comodo lontanissima (2099, 4999…): mostrarla darebbe "Scade tra 1.085.978
// giorni". Nel database resta com'è (serve all'indice ordinato per scadenza), ma ovunque si
// mostri vale "senza scadenza".

/** Oltre questi anni da oggi una scadenza è di comodo. */
const ANNI_SCADENZA_VERA = 5;

/** La scadenza è una data di comodo di inPA (bando aperto senza termine)? */
export const scadenzaDiComodo = (iso?: string, ora = new Date()) =>
  !!iso && Date.parse(iso) - ora.getTime() > ANNI_SCADENZA_VERA * 365 * GIORNO;

/** La scadenza da mostrare e da usare nei conti: undefined se manca o è di comodo. */
export const scadenzaVera = (iso?: string, ora = new Date()) => (iso && !scadenzaDiComodo(iso, ora) ? iso : undefined);

// ── Nomi dei concorsi ────────────────────────────────────────────────────────

/** Prima lettera maiuscola (il resto com'è): inPA ha anche titoli come "istruttore amministrativo". */
export const conMaiuscola = (testo: string) => testo.trim().replace(/\p{L}/u, (lettera) => lettera.toLocaleUpperCase("it-IT"));

/** Anno del bando: di pubblicazione o, se manca, della scadenza. */
export function annoBando(c: Pick<Concorso, "pubblicatoIl" | "scadenza">) {
  const data = c.pubblicatoIl ?? scadenzaVera(c.scadenza);
  return data ? new Date(data).getUTCFullYear() : undefined;
}

/**
 * Nome da mostrare: la figura cercata (o il titolo) con la maiuscola e l'anno, perché i
 * concorsi che si ripetono (es. "Agente di Polizia di Stato") si distinguano: "… 2026", "… 2025".
 */
export function nomeConcorso(c: Pick<Concorso, "titolo" | "figura" | "pubblicatoIl" | "scadenza">) {
  const base = conMaiuscola(c.figura || c.titolo);
  const anno = annoBando(c);
  if (!anno || base.includes(String(anno))) return base;
  // "… 150 posti 2026" si leggerebbe male: dopo un numero l'anno va staccato.
  return /\d$/.test(base) ? `${base} · ${anno}` : `${base} ${anno}`;
}

const dataNome = new Intl.DateTimeFormat("it-IT", { day: "numeric", month: "long", year: "numeric", timeZone: "Europe/Rome" });

/**
 * Nomi per una lista: se lo stesso ente ha due bandi con lo stesso nome (stesso anno), si
 * aggiunge la data di pubblicazione e, se non basta, un pezzo del codice inPA.
 */
export function nomiDistinti<T extends Pick<Concorso, "id" | "ente" | "titolo" | "figura" | "pubblicatoIl" | "scadenza">>(lista: readonly T[]) {
  const nomi = new Map(lista.map((c) => [c.id, nomeConcorso(c)]));
  // Stesso ente e stesso nome: bandi che l'utente non saprebbe distinguere.
  const chiave = (c: T) => `${c.ente.toLowerCase()}|${nomi.get(c.id)}`;
  // Bandi che condividono la chiave con almeno un altro.
  const doppi = (perChiave: (c: T) => string) => {
    const conta = new Map<string, number>();
    for (const c of lista) conta.set(perChiave(c), (conta.get(perChiave(c)) ?? 0) + 1);
    return lista.filter((c) => conta.get(perChiave(c))! > 1);
  };
  for (const c of doppi(chiave)) {
    const data = c.pubblicatoIl ?? scadenzaVera(c.scadenza);
    if (data) nomi.set(c.id, `${conMaiuscola(c.figura || c.titolo)} · ${dataNome.format(new Date(data))}`);
  }
  for (const c of doppi(chiave)) nomi.set(c.id, `${nomi.get(c.id)} · cod. ${c.id.slice(-6)}`);
  return nomi;
}

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

/** I campi di un bando che servono a proporlo per una banca dati (somiglianza di titolo, comparto, anno). */
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
