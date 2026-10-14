// Banche dati a tabella con tutte le risposte in colonna, come quelle del Ministero della
// Giustizia (concorsi di Polizia penitenziaria):
//
//   | Id | Livello | Quesito                    | Risp_esatta | Risp_errata_1 | Risp_errata_2 | Risp_errata_3 |
//   | 3  | 1       | L'insieme intersezione si… | A ∩ B       | A U B         | A + B         | B – A         |
//
// Le colonne si riconoscono dall'intestazione, ripetuta in cima a ogni pagina. Il titolo di
// ogni domanda e le risposte vanno a capo dentro la cella, quindi servono le posizioni nella
// pagina (come per tabella.ts). Tre cose dei PDF esportati da Excel:
//   - gli esponenti sono pezzi di testo più piccoli e più in alto: "4a" + "2" → "4a²";
//   - a volte la domanda e la risposta esatta arrivano in un pezzo solo ("…insieme N: 0,32"):
//     si divide dove inizia la colonna dopo;
//   - il numero di pagina in fondo non è una risposta dell'ultima riga.

import { mescolaStabile, pulisci, unisciCella, type DomandaEstratta, type Estrazione } from "./parser";
import type { Elemento } from "./tabella";

/** Cosa contiene una colonna. */
type Ruolo = "numero" | "livello" | "domanda" | "esatta" | "errata";

/** Testi dell'intestazione per ogni colonna ("Risp_esatta", "Risposta errata 2"…). */
const INTESTAZIONI: [Ruolo, RegExp][] = [
  ["numero", /^(?:id|n\.?|nr\.?|num(?:ero)?|progr(?:essivo)?)$/i],
  ["livello", /^(?:livello|difficolt[aà])$/i],
  ["domanda", /^(?:quesito|domanda|testo(?: della domanda)?)$/i],
  ["esatta", /^risp(?:osta)?[_\s.]*(?:esatta|corretta|giusta)$/i],
  ["errata", /^risp(?:osta)?[_\s.]*(?:errata|sbagliata)[_\s.]*\d*$/i],
];

const RE_NUMERO = /^\d{1,5}$/;
/** Titolo sopra la tabella: "… - BANCA DATI ARITMETICA" → sezione "Aritmetica". */
const RE_TITOLO = /(?:BANCA|Banca)\s+(?:DATI|dati)\s*[-–:]?\s*([A-ZÀ-Ú][A-ZÀ-Ú' ]{2,})$/;

const APICI: Record<string, string> = { "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "+": "⁺", "-": "⁻", "‐": "⁻", "–": "⁻", "(": "⁽", ")": "⁾", n: "ⁿ", x: "ˣ" };
const PEDICI: Record<string, string> = { "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉", "+": "₊", "-": "₋", "(": "₍", ")": "₎" };

/**
 * "12" → "¹²" (o "₁₂"); se un carattere non ha la versione piccola, "^(…)" / "_(…)". La
 * punteggiatura in coda resta normale ("2?" → "²?").
 */
function piccolo(testo: string, su: boolean): string {
  const [, t = "", coda = ""] = testo.match(/^\s*(.*?)([\s?.,:;!]*)$/) ?? [];
  const mappa = su ? APICI : PEDICI;
  const out = [...t].map((c) => mappa[c]);
  if (out.every(Boolean)) return out.join("") + coda;
  return `${su ? "^" : "_"}${t.length > 1 ? `(${t})` : t}${coda}`;
}

/** Il valore più frequente (a parità, il più piccolo). */
function moda(valori: number[]): number | undefined {
  const conta = new Map<number, number>();
  for (const v of valori) conta.set(v, (conta.get(v) ?? 0) + 1);
  return [...conta].sort((a, b) => b[1] - a[1] || a[0] - b[0])[0]?.[0];
}

/** Ruolo di un pezzo di testo dell'intestazione, se lo è. */
const ruoloDi = (testo: string) => INTESTAZIONI.find(([, re]) => re.test(testo.trim()))?.[0];

/** Intestazione di una pagina: y della riga e colonne (ruolo e centro), da sinistra. */
interface Intestazione {
  y: number;
  colonne: { ruolo: Ruolo; centro: number }[];
}

/** Le intestazioni di ogni pagina: una riga con almeno quesito, risposta esatta e una errata. */
export function intestazioni(elementi: Elemento[]): Map<number, Intestazione> {
  const out = new Map<number, Intestazione>();
  const candidati = elementi.filter((e) => ruoloDi(e.testo));
  for (const e of candidati) {
    if (out.has(e.pagina) || ruoloDi(e.testo) !== "domanda") continue;
    const riga = candidati.filter((c) => c.pagina === e.pagina && Math.abs(c.y - e.y) < 3).sort((a, b) => a.x - b.x);
    const colonne = riga.map((c) => ({ ruolo: ruoloDi(c.testo)!, centro: c.x + c.larghezza / 2 }));
    if (colonne.some((c) => c.ruolo === "esatta") && colonne.some((c) => c.ruolo === "errata")) out.set(e.pagina, { y: e.y, colonne });
  }
  return out;
}

/** Riga della tabella mentre la si legge: i pezzi di testo di ogni colonna. */
interface Riga {
  numero: number;
  sezione?: string;
  celle: { testo: string; y: number; fine: number }[][];
}

/** Dai pezzi di testo del PDF alle righe: numero e testo di ogni colonna. */
export function leggiColonne(elementi: Elemento[]) {
  const teste = intestazioni(elementi);
  const prima = teste.values().next().value as Intestazione | undefined;
  if (!prima) return { colonne: [] as Ruolo[], righe: [] as { numero: number; sezione?: string; celle: string[] }[] };
  const ruoli = prima.colonne.map((c) => c.ruolo);

  // Altezza normale del testo: i pezzi molto più bassi sono esponenti o pedici.
  const altezza = moda(elementi.filter((e) => e.altezza && e.testo.trim()).map((e) => Math.round(e.altezza! * 10) / 10)) ?? 0;
  const pezzi: Elemento[] = [];
  for (const e of elementi) {
    const testo = e.testo.replace(/ /g, " ").replace(/‐/g, "-");
    if (!testo.trim()) continue;
    const base = pezzi.at(-1);
    if (altezza && e.altezza && e.altezza < altezza * 0.8 && base && base.pagina === e.pagina && Math.abs(e.x - (base.x + base.larghezza)) < 2) {
      // Esponente (più in alto della base) o pedice (più in basso): si attacca alla base.
      base.testo += piccolo(testo, e.y > base.y);
      base.larghezza = e.x + e.larghezza - base.x;
      continue;
    }
    pezzi.push({ ...e, testo });
  }

  // Colonna di un pezzo, prima a occhio (prima colonna con il centro a destra del suo inizio),
  // poi con il bordo sinistro vero: l'inizio più frequente dei pezzi di quella colonna. Ogni
  // impaginazione ha i suoi bordi (nello stesso file le materie hanno colonne un po' diverse).
  const testaDi = (p: number) => teste.get(p) ?? prima;
  const impaginazione = (p: number) => testaDi(p).colonne.map((c) => Math.round(c.centro / 4)).join(",");
  const aOcchio = (e: Elemento) => {
    const i = testaDi(e.pagina).colonne.findIndex((c) => c.centro > e.x);
    return i < 0 ? ruoli.length - 1 : i;
  };
  const inizi = new Map<string, number[][]>();
  for (const e of pezzi) {
    const chiave = impaginazione(e.pagina);
    const perColonna = inizi.get(chiave) ?? ruoli.map(() => []);
    perColonna[aOcchio(e)]?.push(Math.round(e.x));
    inizi.set(chiave, perColonna);
  }
  const bordiDi = new Map([...inizi].map(([chiave, perColonna]) => [chiave, perColonna.map((xs) => moda(xs))]));
  /** Bordi sinistri delle colonne nella pagina p (il centro dell'intestazione se una colonna è vuota). */
  const bordi = (p: number) => (bordiDi.get(impaginazione(p)) ?? []).map((b, i) => b ?? testaDi(p).colonne[i]!.centro);
  const colonnaDi = (e: Elemento) => {
    let k = 0;
    bordi(e.pagina).forEach((b, i) => {
      if (b <= e.x + 3) k = i;
    });
    return k;
  };

  // Ultimo numero di riga di ogni pagina: sotto, staccato, c'è solo il numero di pagina.
  const ultimaRiga = new Map<number, number>();
  const perRiga = new Map<string, number>();
  for (const e of pezzi) {
    if (ruoli[colonnaDi(e)] === "numero" && RE_NUMERO.test(e.testo.trim())) ultimaRiga.set(e.pagina, Math.min(ultimaRiga.get(e.pagina) ?? Infinity, e.y));
    const chiave = `${e.pagina}|${Math.round(e.y)}`;
    perRiga.set(chiave, (perRiga.get(chiave) ?? 0) + 1);
  }
  /** Quanti pezzi ci sono sulla stessa riga della pagina (y entro 1-2 punti). */
  const sullaRiga = (e: Elemento) => [-1, 0, 1].reduce((n, d) => n + (perRiga.get(`${e.pagina}|${Math.round(e.y) + d}`) ?? 0), 0);
  const piePagina = (e: Elemento) => RE_NUMERO.test(e.testo.trim()) && e.y < (ultimaRiga.get(e.pagina) ?? -Infinity) - 20 && sullaRiga(e) === 1;
  // Se l'intestazione si ripete, le pagine senza (copertine delle materie) non fanno parte della tabella.
  const soloConIntestazione = teste.size > 1;

  const righe: Riga[] = [];
  let sezione: string | undefined;
  let iniziata = false;
  for (const e of pezzi) {
    const testa = teste.get(e.pagina);
    if (testa && e.y > testa.y - 3) {
      // Sopra la tabella: il titolo può dare la sezione; la riga dell'intestazione si salta.
      const titolo = e.y > testa.y + 3 ? pulisci(e.testo).match(RE_TITOLO) : null;
      if (titolo) sezione = titolo[1]!.charAt(0) + titolo[1]!.slice(1).toLowerCase().trim();
      iniziata = true;
      continue;
    }
    if (!iniziata || (soloConIntestazione && !testa) || piePagina(e)) continue;

    const confini = bordi(e.pagina);
    let k = colonnaDi(e);
    let testo = e.testo;
    let x = e.x;
    const fine = e.x + e.larghezza;
    // Pezzo che sconfina nelle colonne dopo (domanda e risposta esatta insieme): si divide
    // dove inizia la colonna dopo, allo spazio più vicino (meglio dopo ":", "?" o ".").
    while (k + 1 < confini.length && fine > confini[k + 1]! + 2) {
      const stima = Math.round((testo.length * (confini[k + 1]! - x)) / (fine - x));
      const spazi = [...testo.matchAll(/ /g)].map((m) => m.index!).filter((i) => Math.abs(i - stima) <= 6 && i > 0);
      if (!spazi.length) break;
      const punto = spazi.filter((i) => /[:?.]$/.test(testo.slice(0, i)));
      const taglio = (punto.length ? punto : spazi).sort((a, b) => Math.abs(a - stima) - Math.abs(b - stima))[0]!;
      aggiungi(righe, ruoli, k, testo.slice(0, taglio), e, x);
      x = confini[k + 1]!;
      testo = testo.slice(taglio + 1);
      k++;
    }
    if (ruoli[k] === "numero" && RE_NUMERO.test(testo.trim())) {
      righe.push({ numero: Number(testo.trim()), sezione, celle: ruoli.map(() => []) });
      continue;
    }
    aggiungi(righe, ruoli, k, testo, e, x);
  }
  return {
    colonne: ruoli,
    righe: righe.map((r) => ({ numero: r.numero, ...(r.sezione ? { sezione: r.sezione } : {}), celle: r.celle.map((c) => unisciCella(c.map((p) => p.testo))) })),
  };
}

/** Aggiunge un pezzo di testo alla cella k dell'ultima riga, attaccato se continua la stessa riga. */
function aggiungi(righe: Riga[], ruoli: Ruolo[], k: number, testo: string, e: Elemento, x: number) {
  const riga = righe.at(-1);
  if (!riga || ruoli[k] === "numero" || ruoli[k] === "livello" || !testo.trim()) return;
  const cella = riga.celle[k]!;
  const ultima = cella.at(-1);
  if (ultima && Math.abs(ultima.y - e.y) < 2 && x - ultima.fine < 1.5) {
    ultima.testo += testo;
    ultima.fine = e.x + e.larghezza;
  } else {
    cella.push({ testo, y: e.y, fine: e.x + e.larghezza });
  }
}

/** Dai pezzi di testo del PDF alle domande: tabella con risposta esatta ed errate in colonna. */
export function estraiDomandeColonne(elementi: Elemento[]): Estrazione {
  const risultato: Estrazione = { domande: [], scartate: [], formati: {} };
  const { colonne, righe } = leggiColonne(elementi);
  const iDomanda = colonne.indexOf("domanda");
  const iEsatta = colonne.indexOf("esatta");
  const iErrate = colonne.flatMap((r, i) => (r === "errata" ? [i] : []));
  const visti = new Set<string>();

  for (const r of righe) {
    // Mette la riga tra le scartate, con il motivo.
    const scarta = (motivo: string) => risultato.scartate.push({ numero: r.numero, motivo });
    const testo = r.celle[iDomanda] ?? "";
    const esatta = r.celle[iEsatta] ?? "";
    const errate = iErrate.map((i) => r.celle[i] ?? "").filter(Boolean);
    if (testo.length < 5) { scarta("testo della domanda mancante"); continue; }
    if (!esatta) { scarta("risposta esatta mancante"); continue; }
    if (!errate.length) { scarta("nessuna risposta errata"); continue; }
    const opzioni = [esatta, ...errate];
    if (new Set(opzioni.map((o) => o.toLowerCase())).size !== opzioni.length) { scarta("risposte ripetute"); continue; }
    const chiave = [testo, ...[...opzioni].sort()].join("|").toLowerCase();
    if (visti.has(chiave)) { scarta("domanda già presente (doppione)"); continue; }
    visti.add(chiave);

    const ordine = mescolaStabile(opzioni.map((_, i) => i), r.numero);
    const domanda: DomandaEstratta = {
      numero: r.numero,
      testo,
      opzioni: ordine.map((i) => opzioni[i]!),
      corretta: ordine.indexOf(0),
      ...(r.sezione ? { sezione: r.sezione } : {}),
      pdf: { opzioni, corretta: 0 },
    };
    risultato.domande.push(domanda);
    risultato.formati.colonne = (risultato.formati.colonne ?? 0) + 1;
  }
  return risultato;
}
