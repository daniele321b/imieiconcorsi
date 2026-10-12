// Dal testo di una banca dati ufficiale (PDF già convertito in testo) alle domande.
//
// Formati riconosciuti, anche mescolati nello stesso file:
//   indicata  "Risposta esatta: B" (o corretta / giusta / soluzione) dentro la domanda
//   segnata   la risposta giusta ha un segno: "* B) …", "B) … *", "(X)", "[X]", "✓"
//   chiave    tabella delle soluzioni dopo un titolo come "Soluzioni" / "Risposte esatte":
//             "1 B  2 A  3-C  4) D …"
//   prima     "la risposta esatta è sempre la prima (A)": vale per tutte le domande
//   risposta  tabella "numero | domanda | risposta esatta", senza alternative (tabella.ts)
// "auto" li prova tutti; un formato scelto a mano forza quello.

/** Come è indicata la risposta giusta nel PDF (vedi sopra). */
export type Formato = "auto" | "indicata" | "segnata" | "chiave" | "prima" | "risposta";

/** Una domanda letta dal PDF, pronta da controllare e pubblicare. */
export interface DomandaEstratta {
  numero: number;
  testo: string;
  /** Mescolate, così la giusta non è sempre nella stessa posizione */
  opzioni: string[];
  corretta: number;
  /** Titolo della sezione del PDF in cui sta la domanda, es. "CULTURA GENERALE" */
  sezione?: string;
  /** Come nel PDF: per confrontare gli esempi con il file */
  pdf: { opzioni: string[]; corretta: number };
  /** Il PDF dava solo la risposta esatta: le altre sono ricavate (tabella.ts) */
  alternativeRicavate?: true;
}

/** Risultato dell'estrazione: domande valide, scartate con il motivo e conteggio per formato. */
export interface Estrazione {
  domande: DomandaEstratta[];
  scartate: { numero: number; motivo: string }[];
  /** Quante domande per ciascun modo di trovare la risposta giusta */
  formati: Partial<Record<Exclude<Formato, "auto">, number>>;
}

/** Lettere delle risposte, fino a 6 (A-F). */
const LETTERE = "ABCDEF";

/** Inizio di una domanda: "12. Testo…", "12) …", "Domanda n. 12: …". */
const RE_DOMANDA = /^(?:domanda\s*(?:n\.?\s*)?)?(\d{1,5})\s*[.)\]:–-]\s*(.*)$/i;
/** Una risposta: "B) …", "(b) …", "* B) …" (con l'asterisco = segnata come giusta). */
const RE_OPZIONE = /^(\*\s*)?[([]?([A-Fa-f])\s*[).\]:–-]\s*(.*)$/;
/** Riga "Risposta esatta: B" dentro la domanda. */
const RE_INDICATA = /^(?:risposta\s*(?:esatta|corretta|giusta)|soluzione|risp\.?\s*esatta)\s*[:.–-]?\s*\(?([A-Fa-f])\)?\b/i;
/** Segni che marcano la risposta giusta: asterisco, (X), [X], ✓. */
const RE_SEGNO = /(^\*\s*)|(\s*\*$)|\((?:x|X)\)|\[(?:x|X)\]|✓|✔/;
/**
 * Titolo della tabella delle soluzioni: una riga breve che inizia così. Non basta che
 * la parola compaia ("A) Garantire la soluzione delle controversie" è una risposta).
 */
const RE_TITOLO_CHIAVE =
  /^(?:tabella\s+(?:delle\s+)?|elenco\s+(?:delle\s+)?)?(?:soluzioni|risposte\s+(?:esatte|corrette|giuste)|chiave\s+(?:delle\s+)?risposte|correttore|griglia\s+(?:delle\s+)?risposte)\b[^.?]{0,40}$/i;

/** Una coppia numero-lettera nella tabella delle soluzioni: "12 B", "12) B", "12-B". */
const RE_COPPIA_CHIAVE = /\b(\d{1,5})\s*[.)\]:=–-]?\s*([A-F])\b/g;
/**
 * "La risposta esatta è sempre la prima", "… è la lettera A", "… è contrassegnata dalla
 * lettera “A”", "… corrisponde alla A": la giusta è sempre la A.
 */
const RE_SEMPRE_PRIMA =
  /rispost[ae]\s+(?:esatt|corrett|giust)[ae][^.]{0,60}?\s(?:è|e'|sono)\s+(?:sempre\s+)?(?:(?:contrassegnat|indicat|identificat|segnat)[ae]\s+(?:dalla|con\s+la)\s+|(?:corrispond\w*\s+)?(?:alla\s+)?)?(?:la\s+|le\s+)?(?:prima|lettera\s+["“”'‘’«]?a\b|["“”'‘’«(]?a["“”'’»)]?(?=[\s.,;:]|$))/i;
/** Righe da buttare: numeri di pagina, intestazioni ripetute. */
const RE_RUMORE = /^(?:pag(?:ina)?\.?\s*\d+(?:\s*(?:di|\/)\s*\d+)?|\d+\s*(?:di|\/)\s*\d+|\d{1,4})$/i;
/** Numero di pagina attaccato alla fine dell'ultima riga della pagina: "…velocità1 di 399". */
const RE_PAGINA_IN_CODA = /\s*\d{1,4}\s+di\s+\d{1,4}$/i;
/** …o all'inizio della riga dopo, su una pagina vuota: "84 di 399BANCA DATI". */
const RE_PAGINA_IN_TESTA = /^\d{1,4}\s+di\s+\d{1,4}(?=[A-ZÀ-Ú])/;
/** Tutto maiuscolo, senza numeri (es. "CULTURA GENERALE", "BANCA DATI", "MATEMATICA"). */
const maiuscolo = (r: string) => r.length >= 4 && !/[a-zà-ú0-9]/.test(r) && /[A-Z]{3}/.test(r);

/** Domanda mentre la si legge riga per riga, prima dei controlli. */
interface Grezza {
  numero: number;
  sezione?: string;
  testo: string[];
  opzioni: { testo: string[]; segnata: boolean }[];
  indicata?: number;
}

/** Spazi normali al posto di quelli speciali, niente spazi doppi. */
export const pulisci = (s: string) => s.replace(/ /g, " ").replace(/[ \t]+/g, " ").trim();
/** Righe spezzate dal PDF in un testo solo (riattacca le parole divise con il trattino). */
export const unisci = (parti: string[]) => pulisci(parti.join(" ").replace(/(\w)- (\w)/g, "$1$2"));

/** Mescola le opzioni in modo stabile (stesso PDF → stessa domanda), così la giusta non è sempre la A. */
export function mescolaStabile<T>(arr: T[], seme: number): T[] {
  const out = [...arr];
  let x = seme * 2654435761 || 1;
  for (let i = out.length - 1; i > 0; i--) {
    x = (x ^ (x << 13)) >>> 0;
    x = (x ^ (x >>> 17)) >>> 0;
    x = (x ^ (x << 5)) >>> 0;
    const j = x % (i + 1);
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

/** "CULTURA GENERALE" → "Cultura generale" */
const titoloSezione = (s: string) => s.charAt(0) + s.slice(1).toLowerCase();

/** Tabella delle soluzioni, se c'è: numero della domanda → indice della risposta giusta. */
function chiaveDelleRisposte(righe: string[]): Map<number, number> {
  const mappa = new Map<number, number>();
  const inizio = righe.findIndex((r) => RE_TITOLO_CHIAVE.test(r) && !RE_DOMANDA.test(r));
  if (inizio < 0) return mappa;
  for (const riga of righe.slice(inizio + 1)) {
    for (const m of riga.matchAll(RE_COPPIA_CHIAVE)) mappa.set(Number(m[1]), LETTERE.indexOf(m[2]));
  }
  return mappa;
}

/** Dal testo del PDF alle domande, con il formato indicato o provandoli tutti ("auto"). */
export function estraiDomande(testo: string, formato: Formato = "auto"): Estrazione {
  // Numeri di pagina attaccati a fine riga ("…velocità1 di 399") o all'intestazione ("84 di 399BANCA DATI").
  const grezzeRighe = testo.split(/\r?\n/).map((r) => {
    const p = pulisci(r);
    const senza = p.replace(RE_PAGINA_IN_CODA, "").replace(RE_PAGINA_IN_TESTA, "");
    return { r: senza, fineriga: senza !== p };
  });
  // Intestazioni ripetute in ogni pagina (es. "BANCA DATI"): si riconoscono perché tornano spesso.
  const conteggi = new Map<string, number>();
  for (const { r } of grezzeRighe) if (r) conteggi.set(r, (conteggi.get(r) ?? 0) + 1);
  const intestazione = (r: string) => maiuscolo(r) && (conteggi.get(r) ?? 0) >= 3;

  // Tolte le righe di servizio; si ricorda quali righe aprono una pagina (servono ai titoli di sezione).
  const righe: string[] = [];
  const inizioPagina = new Set<number>();
  let nuovaPagina = true;
  for (const { r, fineriga } of grezzeRighe) {
    if (!r || RE_RUMORE.test(r) || intestazione(r)) {
      if (r || fineriga) nuovaPagina = true;
      continue;
    }
    if (nuovaPagina) inizioPagina.add(righe.length);
    righe.push(r);
    nuovaPagina = fineriga;
  }
  const chiave = formato === "auto" || formato === "chiave" ? chiaveDelleRisposte(righe) : new Map<number, number>();
  const semprePrima = formato === "prima" || (formato === "auto" && RE_SEMPRE_PRIMA.test(righe.slice(0, 80).join(" ")));

  // La tabella delle soluzioni non va letta come domande.
  const fine = chiave.size ? righe.findIndex((r) => RE_TITOLO_CHIAVE.test(r) && !RE_DOMANDA.test(r)) : righe.length;
  const grezze: Grezza[] = [];
  let corrente: Grezza | undefined;
  let sezione: string | undefined;

  const daLeggere = righe.slice(0, fine);
  for (const [i, riga] of daLeggere.entries()) {
    // Titolo di sezione: maiuscolo, dopo una domanda completa e subito prima di una nuova.
    // Dà l'argomento alle domande che seguono. Le righe maiuscole dentro una domanda
    // (es. "T Q N I F" nelle serie di logica) restano testo.
    const prossima = daLeggere[i + 1];
    if (
      maiuscolo(riga) &&
      !RE_OPZIONE.test(riga) &&
      // A inizio pagina basta; a metà pagina potrebbe essere la fine di una risposta ("… persone LGBTQ").
      (inizioPagina.has(i) || (/\s/.test(riga) && riga.length >= 8 && !riga.startsWith("("))) &&
      (!corrente || corrente.opzioni.length >= 2) &&
      prossima !== undefined &&
      RE_DOMANDA.test(prossima)
    ) {
      sezione = riga;
      continue;
    }
    const ind = riga.match(RE_INDICATA);
    if (ind && corrente) {
      corrente.indicata = LETTERE.indexOf(ind[1].toUpperCase());
      continue;
    }
    const opz = riga.match(RE_OPZIONE);
    // Una lettera vale come opzione solo dentro una domanda e in ordine (A, B, C…): "E) " a inizio
    // di una frase del testo non deve aprire una risposta.
    if (opz && corrente && LETTERE.indexOf(opz[2].toUpperCase()) === corrente.opzioni.length) {
      corrente.opzioni.push({ testo: [opz[3]], segnata: !!opz[1] || RE_SEGNO.test(opz[3]) });
      continue;
    }
    const dom = riga.match(RE_DOMANDA);
    if (dom && (!corrente || corrente.opzioni.length >= 2 || Number(dom[1]) === corrente.numero + 1)) {
      corrente = { numero: Number(dom[1]), sezione, testo: [dom[2]], opzioni: [] };
      grezze.push(corrente);
      continue;
    }
    if (!corrente) continue;
    const ultima = corrente.opzioni.at(-1);
    if (ultima) {
      ultima.testo.push(riga);
      if (RE_SEGNO.test(riga)) ultima.segnata = true;
    } else {
      corrente.testo.push(riga);
    }
  }

  const risultato: Estrazione = { domande: [], scartate: [], formati: {} };
  const visti = new Set<string>();

  for (const g of grezze) {
    const testoDomanda = unisci(g.testo);
    const opzioni = g.opzioni.map((o) => unisci(o.testo).replace(RE_SEGNO, "").replace(/\s*\*\s*$/, "").trim());
    const scarta = (motivo: string) => risultato.scartate.push({ numero: g.numero, motivo });

    if (testoDomanda.length < 5) { scarta("testo della domanda mancante"); continue; }
    if (opzioni.length < 2) { scarta("meno di due risposte"); continue; }
    if (opzioni.some((o) => !o)) { scarta("una risposta è vuota"); continue; }
    if (new Set(opzioni.map((o) => o.toLowerCase())).size !== opzioni.length) { scarta("risposte ripetute"); continue; }

    const segnate = g.opzioni.flatMap((o, i) => (o.segnata ? [i] : []));
    let corretta: number | undefined;
    let come: Exclude<Formato, "auto"> | undefined;
    const prova = (f: Exclude<Formato, "auto">, valore: number | undefined) => {
      if (corretta === undefined && valore !== undefined && valore >= 0 && (formato === "auto" || formato === f)) {
        corretta = valore;
        come = f;
      }
    };
    prova("indicata", g.indicata);
    prova("segnata", segnate.length === 1 ? segnate[0] : undefined);
    prova("chiave", chiave.get(g.numero));
    if (semprePrima) prova("prima", 0);

    if (corretta === undefined || come === undefined) {
      scarta(segnate.length > 1 ? "più risposte segnate come giuste" : "risposta giusta non trovata");
      continue;
    }
    if (corretta >= opzioni.length) { scarta(`la risposta giusta (${LETTERE[corretta]}) non è tra quelle lette`); continue; }

    // Stesso testo con risposte diverse (es. "Quale non fa parte dello scheletro umano?") non è un doppione.
    const chiaveTesto = [testoDomanda, ...[...opzioni].sort()].join("|").toLowerCase();
    if (visti.has(chiaveTesto)) { scarta("domanda già presente (doppione)"); continue; }
    visti.add(chiaveTesto);

    const ordine = mescolaStabile(opzioni.map((_, i) => i), g.numero);
    risultato.domande.push({
      numero: g.numero,
      testo: testoDomanda,
      opzioni: ordine.map((i) => opzioni[i]),
      corretta: ordine.indexOf(corretta),
      ...(g.sezione ? { sezione: titoloSezione(g.sezione) } : {}),
      pdf: { opzioni, corretta },
    });
    risultato.formati[come] = (risultato.formati[come] ?? 0) + 1;
  }
  return risultato;
}
