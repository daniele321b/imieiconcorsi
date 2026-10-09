import type { CompartoId, Concorso, MateriaId } from "@imieiconcorsi/core/domain";

// Accesso a inPA (il portale dei concorsi pubblici) e conversione dei suoi bandi nei nostri
// Concorso: comparto dedotto da ente e settore, materie lette dal testo (o stimate per comparto),
// segnale "cita una banca dati". Lo usano lo scraper del mattino e la pulizia della domenica.
//
// API JSON pubblica usata dal portale inPA stesso. Una chiamata al giorno, sequenziale.
const SEARCH_URL = "https://portale.inpa.gov.it/concorsi-smart/api/concorso-public-area/search-better";
const DETTAGLIO_URL = "https://www.inpa.gov.it/bandi-e-avvisi/dettaglio-bando-avviso/?concorso_id=";
/** Bandi per pagina (il massimo che inPA accetta senza rallentare). */
const PAGE_SIZE = 100;
/** Pausa tra una pagina e l'altra, per non pesare sul portale. */
const PAUSA_MS = 500;

/** Un bando come lo restituisce inPA (solo i campi che usiamo). */
export interface InpaBando {
  id: string;
  titolo: string;
  descrizioneBreve?: string | null;
  descrizione?: string | null;
  figuraRicercata?: string | null;
  dataPubblicazione?: string | null;
  dataScadenza?: string | null;
  tipoProcedura?: string | null;
  numPosti?: number | null;
  sedi?: string[] | null;
  settori?: string[] | null;
  categorie?: string[] | null;
  entiRiferimento?: string[] | null;
}

interface InpaPage {
  content: InpaBando[];
  last: boolean;
  totalElements: number;
}

/** OPEN = domande aperte; CLOSED = scadute (inPA le dà più o meno dalla scadenza più recente). */
export type StatoInpa = "OPEN" | "CLOSED";

/** Una pagina di risultati di inPA. */
export async function cercaPagina(stato: StatoInpa, page: number, fetchFn: typeof fetch = fetch): Promise<InpaPage> {
  const res = await fetchFn(`${SEARCH_URL}?page=${page}&size=${PAGE_SIZE}`, {
    method: "POST",
    headers: { "content-type": "application/json", "user-agent": "iMieiConcorsi/0.1 (aggiornamento giornaliero)" },
    body: JSON.stringify({ text: "", status: [stato] }),
  });
  if (!res.ok) throw new Error(`inPA ha risposto ${res.status} alla pagina ${page} (${stato})`);
  return (await res.json()) as InpaPage;
}

/** Attesa tra due chiamate. */
export const pausa = () => new Promise((r) => setTimeout(r, PAUSA_MS));

/** Pagine di bandi a partire da `daPagina`, una chiamata ogni PAUSA_MS. */
export async function* bandi(stato: StatoInpa, daPagina = 0, fetchFn: typeof fetch = fetch): AsyncGenerator<{ pagina: number; bandi: InpaBando[]; ultima: boolean }> {
  for (let page = daPagina; ; page++) {
    const data = await cercaPagina(stato, page, fetchFn);
    const ultima = data.last || !data.content.length;
    yield { pagina: page, bandi: data.content, ultima };
    if (ultima) return;
    await pausa();
  }
}

/** Tutti i bandi con le domande aperte, una pagina alla volta. */
export async function* bandiAperti(fetchFn: typeof fetch = fetch): AsyncGenerator<InpaBando[]> {
  for await (const p of bandi("OPEN", 0, fetchFn)) yield p.bandi;
}

/**
 * La pagina di chiusi è tutta più vecchia di `limite`? L'ordine di inPA è solo
 * approssimativo, quindi conta la scadenza più recente della pagina.
 */
export function paginaPiuVecchiaDi(pagina: InpaBando[], limite: string) {
  const scadenze = pagina.map((b) => b.dataScadenza).filter((d): d is string => !!d);
  return scadenze.length > 0 && scadenze.every((d) => d < limite);
}

/** Comparto di un bando dalle parole di ente, settore e titolo: vince la prima regola che corrisponde. */
const REGOLE_COMPARTO: [CompartoId, RegExp][] = [
  ["forze-ordine", /polizia di stato|polizia penitenziaria|carabinieri|guardia di finanza|vigili del fuoco|esercito|marina militare|aeronautica|ministero della difesa|ministero dell'interno/i],
  ["inps", /\binps\b|\binail\b|previdenza/i],
  ["sanita", /sanit[aà]|\basl\b|\basst\b|\basp\b|\bausl\b|\bats\b|ospedal|salute/i],
  ["universita", /universit|politecnico|ricerca|\bcnr\b|istituto nazionale/i],
  ["ministeri", /ministero|agenzia|autorit|presidenza del consiglio|corte dei conti|avvocatura/i],
  ["enti-locali", /comune|provincia|regione|unione|citt[aà]'? metropolitana|comunit[aà]'? montana|consorzio/i],
];

/** Decide sul nome dell'ente; il titolo serve solo se l'ente non basta (parole come "ricerca" lo renderebbero ambiguo). */
export function classificaComparto(b: InpaBando): CompartoId {
  const match = (testo: string) => REGOLE_COMPARTO.find(([, re]) => re.test(testo))?.[0];
  return match((b.entiRiferimento ?? []).join(" ")) ?? match(b.titolo) ?? "altro";
}

/**
 * Stima delle materie in base al comparto, finché l'estrazione dal PDF del bando (settimana 2)
 * non le legge davvero. Per questo il concorso resta marcato `materieStimate: true`.
 */
const MATERIE_TIPICHE: Record<CompartoId, MateriaId[]> = {
  "enti-locali": ["diritto-amministrativo", "diritto-costituzionale", "contabilita-pubblica", "informatica", "inglese", "logica"],
  "forze-ordine": [
    "italiano", "storia", "geografia", "diritto-costituzionale", "diritto-penale",
    "logica", "matematica", "informatica", "inglese",
  ],
  inps: ["diritto-amministrativo", "diritto-costituzionale", "diritto-lavoro", "contabilita-pubblica", "informatica", "inglese", "logica"],
  ministeri: ["diritto-amministrativo", "diritto-costituzionale", "contabilita-pubblica", "informatica", "inglese", "logica"],
  sanita: ["diritto-amministrativo", "diritto-costituzionale", "diritto-lavoro", "informatica", "inglese"],
  universita: ["diritto-amministrativo", "diritto-lavoro", "informatica", "inglese", "logica"],
  altro: ["diritto-amministrativo", "diritto-costituzionale", "informatica", "inglese", "logica"],
};

/**
 * Materie citate nel testo del bando ("prove su: diritto amministrativo, lingua inglese…").
 * Parole chiave volutamente specifiche: meglio una materia in meno che una sbagliata.
 */
const PAROLE_MATERIA: [MateriaId, RegExp][] = [
  ["diritto-amministrativo", /diritto amministrativ|procedimento amministrativ|ordinamento degli enti locali|\btuel\b|l(egge|\.)\s*(n\.\s*)?241/i],
  ["diritto-costituzionale", /diritto costituzional|costituzione della repubblica|diritto pubblico/i],
  ["contabilita-pubblica", /contabilit[aà] (pubblica|di stato|degli enti)|ordinamento finanziario e contabile|bilancio degli enti|armonizzazione contabile/i],
  ["diritto-lavoro", /diritto del lavoro|lavoro (alle dipendenze delle )?pubblic|pubblico impiego|previdenz/i],
  ["diritto-penale", /diritto penale|procedura penale|reati contro la pubblica amministrazione/i],
  ["italiano", /lingua italiana|grammatica italiana|comprensione (del|di un) testo/i],
  ["storia", /\bstoria (d'italia|contemporanea|moderna)|cultura generale/i],
  ["geografia", /\bgeografia\b/i],
  ["logica", /\blogic|ragionamento (logico|verbale|numerico)|(psico)?attitudinal/i],
  ["matematica", /\bmatematic|\baritmetic/i],
  ["informatica", /informatic|competenze digitali|strumenti digitali/i],
  ["inglese", /lingua inglese|\binglese\b/i],
];

/** Materie citate nel testo del bando (es. "diritto amministrativo", "lingua inglese"). */
export function materieDalTesto(testo: string): MateriaId[] {
  return PAROLE_MATERIA.filter(([, re]) => re.test(testo)).map(([m]) => m);
}

/** Testo senza tag HTML e spazi doppi. */
const testoSemplice = (html?: string | null) =>
  html
    ?.replace(/<[^>]+>/g, " ")
    .replace(/&nbsp;/g, " ")
    .replace(/\s+/g, " ")
    .trim();

/** Il bando cita una banca dati ("banca dati", "banche dati", "banca-dati")? */
const BANCA_DATI = /banc(a|he)[\s-]*dati/i;
export const citaBancaDati = (b: InpaBando) =>
  BANCA_DATI.test([b.titolo, b.descrizioneBreve, testoSemplice(b.descrizione)].filter(Boolean).join(" "));

/** Da un bando di inPA al nostro Concorso (comparto, materie, link al dettaglio). */
export function toConcorso(b: InpaBando, now = new Date()): Concorso {
  const comparto = classificaComparto(b);
  // Con almeno due materie trovate nel bando ci fidiamo del testo; altrimenti stima per comparto.
  const lette = materieDalTesto([b.titolo, b.descrizioneBreve, testoSemplice(b.descrizione)].filter(Boolean).join(" "));
  const dalBando = lette.length >= 2;
  return {
    id: b.id,
    titolo: b.titolo.trim(),
    ente: b.entiRiferimento?.[0]?.trim() ?? "Ente non indicato",
    sedi: b.sedi ?? [],
    comparto,
    // Senza scadenza il concorso non entra nell'indice per comparto (che ordina per scadenza).
    scadenza: b.dataScadenza ?? undefined,
    pubblicatoIl: b.dataPubblicazione ?? undefined,
    tipoProcedura: b.tipoProcedura ?? undefined,
    posti: b.numPosti ?? undefined,
    figura: b.figuraRicercata?.trim() || undefined,
    descrizione: testoSemplice(b.descrizione)?.slice(0, 4000) || b.descrizioneBreve || undefined,
    url: DETTAGLIO_URL + b.id,
    materie: dalBando ? lette : MATERIE_TIPICHE[comparto],
    materieStimate: !dalBando,
    bancaDatiPrevista: citaBancaDati(b),
    bancaDati: false,
    fonte: "inpa",
    aggiornatoIl: now.toISOString(),
  };
}
