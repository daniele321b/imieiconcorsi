import type { CompartoId, Concorso, MateriaId } from "@imieiconcorsi/core/domain";

// API JSON pubblica usata dal portale inPA stesso. Una chiamata al giorno, sequenziale.
const SEARCH_URL = "https://portale.inpa.gov.it/concorsi-smart/api/concorso-public-area/search-better";
const DETTAGLIO_URL = "https://www.inpa.gov.it/bandi-e-avvisi/dettaglio-bando-avviso/?concorso_id=";
const PAGE_SIZE = 100;
const PAUSA_MS = 500;

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

export async function* bandiAperti(fetchFn: typeof fetch = fetch): AsyncGenerator<InpaBando[]> {
  for (let page = 0; ; page++) {
    const res = await fetchFn(`${SEARCH_URL}?page=${page}&size=${PAGE_SIZE}`, {
      method: "POST",
      headers: { "content-type": "application/json", "user-agent": "iMieiConcorsi/0.1 (aggiornamento giornaliero)" },
      body: JSON.stringify({ text: "", status: ["OPEN"] }),
    });
    if (!res.ok) throw new Error(`inPA ha risposto ${res.status} alla pagina ${page}`);
    const data = (await res.json()) as InpaPage;
    yield data.content;
    if (data.last || !data.content.length) return;
    await new Promise((r) => setTimeout(r, PAUSA_MS));
  }
}

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
  "enti-locali": ["diritto-amministrativo", "diritto-costituzionale", "informatica", "logica"],
  "forze-ordine": ["italiano", "storia", "diritto-costituzionale", "logica", "informatica"],
  inps: ["diritto-amministrativo", "diritto-costituzionale", "informatica", "logica"],
  ministeri: ["diritto-amministrativo", "diritto-costituzionale", "informatica", "logica"],
  sanita: ["diritto-amministrativo", "diritto-costituzionale", "informatica"],
  universita: ["diritto-amministrativo", "informatica", "logica"],
  altro: ["diritto-amministrativo", "diritto-costituzionale", "logica"],
};

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

export function toConcorso(b: InpaBando, now = new Date()): Concorso {
  const comparto = classificaComparto(b);
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
    materie: MATERIE_TIPICHE[comparto],
    materieStimate: true,
    bancaDatiPrevista: citaBancaDati(b),
    bancaDati: false,
    fonte: "inpa",
    aggiornatoIl: now.toISOString(),
  };
}
