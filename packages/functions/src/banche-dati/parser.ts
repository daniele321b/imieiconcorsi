// Dal testo di una banca dati ufficiale (PDF già convertito in testo) alle domande.
//
// Formati riconosciuti, anche mescolati nello stesso file:
//   indicata  "Risposta esatta: B" (o corretta / giusta / soluzione) dentro la domanda
//   segnata   la risposta giusta ha un segno: "* B) …", "B) … *", "(X)", "[X]", "✓"
//   chiave    tabella delle soluzioni dopo un titolo come "Soluzioni" / "Risposte esatte":
//             "1 B  2 A  3-C  4) D …"
//   prima     "la risposta esatta è sempre la prima (A)": vale per tutte le domande
// "auto" li prova tutti; un formato scelto a mano forza quello.

export type Formato = "auto" | "indicata" | "segnata" | "chiave" | "prima";

export interface DomandaEstratta {
  numero: number;
  testo: string;
  opzioni: string[];
  corretta: number;
}

export interface Estrazione {
  domande: DomandaEstratta[];
  scartate: { numero: number; motivo: string }[];
  /** Quante domande per ciascun modo di trovare la risposta giusta */
  formati: Partial<Record<Exclude<Formato, "auto">, number>>;
}

const LETTERE = "ABCDEF";

const RE_DOMANDA = /^(?:domanda\s*(?:n\.?\s*)?)?(\d{1,5})\s*[.)\]:–-]\s*(.*)$/i;
const RE_OPZIONE = /^(\*\s*)?[([]?([A-Fa-f])\s*[).\]:–-]\s*(.*)$/;
const RE_INDICATA = /^(?:risposta\s*(?:esatta|corretta|giusta)|soluzione|risp\.?\s*esatta)\s*[:.–-]?\s*\(?([A-Fa-f])\)?\b/i;
const RE_SEGNO = /(^\*\s*)|(\s*\*$)|\((?:x|X)\)|\[(?:x|X)\]|✓|✔/;
const RE_TITOLO_CHIAVE = /soluzion|risposte\s+(?:esatte|corrette|giuste)|chiave\s+(?:delle\s+)?rispost|correttore|griglia\s+(?:delle\s+)?rispost/i;
const RE_COPPIA_CHIAVE = /\b(\d{1,5})\s*[.)\]:=–-]?\s*([A-F])\b/g;
const RE_SEMPRE_PRIMA = /rispost[ae]\s+(?:esatt|corrett|giust)[ae][^.]{0,40}?\s(?:è|e'|sono)\s+(?:sempre\s+)?(?:la\s+|le\s+)?(?:prima|lettera\s+a|\(?a\)?)\b/i;
/** Righe da buttare: numeri di pagina, intestazioni ripetute. */
const RE_RUMORE = /^(?:pag(?:ina)?\.?\s*\d+(?:\s*(?:di|\/)\s*\d+)?|\d+\s*(?:di|\/)\s*\d+|\d{1,4})$/i;

interface Grezza {
  numero: number;
  testo: string[];
  opzioni: { testo: string[]; segnata: boolean }[];
  indicata?: number;
}

const pulisci = (s: string) => s.replace(/ /g, " ").replace(/[ \t]+/g, " ").trim();
const unisci = (parti: string[]) => pulisci(parti.join(" ").replace(/(\w)- (\w)/g, "$1$2"));

/** Mescola le opzioni in modo stabile (stesso PDF → stessa domanda), così la giusta non è sempre la A. */
function mescolaStabile<T>(arr: T[], seme: number): T[] {
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

function chiaveDelleRisposte(righe: string[]): Map<number, number> {
  const mappa = new Map<number, number>();
  const inizio = righe.findIndex((r) => RE_TITOLO_CHIAVE.test(r) && !RE_DOMANDA.test(r));
  if (inizio < 0) return mappa;
  for (const riga of righe.slice(inizio + 1)) {
    for (const m of riga.matchAll(RE_COPPIA_CHIAVE)) mappa.set(Number(m[1]), LETTERE.indexOf(m[2]));
  }
  return mappa;
}

export function estraiDomande(testo: string, formato: Formato = "auto"): Estrazione {
  const righe = testo.split(/\r?\n/).map(pulisci).filter((r) => r && !RE_RUMORE.test(r));
  const chiave = formato === "auto" || formato === "chiave" ? chiaveDelleRisposte(righe) : new Map<number, number>();
  const semprePrima = formato === "prima" || (formato === "auto" && RE_SEMPRE_PRIMA.test(righe.slice(0, 80).join(" ")));

  // La tabella delle soluzioni non va letta come domande.
  const fine = chiave.size ? righe.findIndex((r) => RE_TITOLO_CHIAVE.test(r) && !RE_DOMANDA.test(r)) : righe.length;
  const grezze: Grezza[] = [];
  let corrente: Grezza | undefined;

  for (const riga of righe.slice(0, fine)) {
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
      corrente = { numero: Number(dom[1]), testo: [dom[2]], opzioni: [] };
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

    const chiaveTesto = testoDomanda.toLowerCase();
    if (visti.has(chiaveTesto)) { scarta("domanda già presente (doppione)"); continue; }
    visti.add(chiaveTesto);

    const ordine = mescolaStabile(opzioni.map((_, i) => i), g.numero);
    risultato.domande.push({ numero: g.numero, testo: testoDomanda, opzioni: ordine.map((i) => opzioni[i]), corretta: ordine.indexOf(corretta) });
    risultato.formati[come] = (risultato.formati[come] ?? 0) + 1;
  }
  return risultato;
}
