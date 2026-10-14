// Banche dati a tabella con la sola risposta esatta, come quelle di Carabinieri e Forze armate
// ("In questo file trovi solo la domanda con la relativa risposta esatta"):
//
//   | 1 | Sinonimo di aborrire                 | detestare        |
//   | 2 | Completa la serie: Milano, Torino…   | Napoli           |
//
// Dal solo testo non si capisce dove finisce la domanda e inizia la risposta ("Sinonimo di
// aborrire detestare"): servono le posizioni nella pagina. Le colonne si trovano da sole (le x
// più frequenti), "Materia : …" sopra la tabella diventa la sezione.
//
// Gli utenti però si allenano a scelta multipla: le alternative sbagliate si ricavano dalle
// risposte di domande dello stesso tipo nella stessa banca dati (stessa sezione, stesso inizio
// della domanda, stessa forma della risposta). Senza AI e sempre uguali per lo stesso file.
// Si scartano, con il motivo, le domande in cui così si sbaglierebbe: quelle al negativo ("Non
// ha nulla a che fare con…": una risposta presa a caso sarebbe anch'essa giusta) e quelle che
// citano alternative che il file non riporta.

import { mescolaStabile, pulisci, unisci, type DomandaEstratta, type Estrazione } from "./parser";

/** Un pezzo di testo del PDF con la sua posizione (punti PDF, y dal basso). */
export interface Elemento {
  pagina: number;
  testo: string;
  x: number;
  y: number;
  larghezza: number;
  /** Altezza del testo: gli esponenti sono più bassi del resto (colonne.ts) */
  altezza?: number;
}

/** Una riga della tabella: numero, domanda e risposta esatta. */
export interface RigaTabella {
  numero: number;
  domanda: string;
  risposta: string;
  sezione?: string;
}

/** Quante alternative sbagliate cercare (4 risposte in tutto, come nei quiz d'esame). */
const ALTERNATIVE = 3;

const RE_NUMERO = /^\d{1,5}$/;
/** Titolo di sezione sopra la tabella: "Materia : Capacità verbale". */
const RE_SEZIONE = /^(?:materia|argomento|sezione)\s*[:–-]\s*(.+)$/i;

/** Il valore più frequente (a parità, il più piccolo), con quante volte compare. */
function moda(valori: number[]): [number, number] | undefined {
  const conta = new Map<number, number>();
  for (const v of valori) conta.set(v, (conta.get(v) ?? 0) + 1);
  return [...conta].sort((a, b) => b[1] - a[1] || a[0] - b[0])[0];
}

/**
 * Le colonne della tabella: x dei numeri, della domanda e della risposta. undefined se non
 * c'è una tabella così (almeno 5 righe numerate e due colonne di testo).
 */
export function colonne(elementi: Elemento[]) {
  const numeri = moda(elementi.filter((e) => RE_NUMERO.test(e.testo.trim())).map((e) => Math.round(e.x)));
  if (!numeri || numeri[1] < 5) return undefined;
  const xNumero = numeri[0];
  // Inizio dei pezzi di testo: le due x più frequenti a destra dei numeri, ben distanti.
  const conta = new Map<number, number>();
  for (const e of elementi) {
    const x = Math.round(e.x);
    if (e.testo.trim() && x > xNumero + 10) conta.set(x, (conta.get(x) ?? 0) + 1);
  }
  const frequenti = [...conta].filter(([, n]) => n >= 5).sort((a, b) => b[1] - a[1]);
  const [prima] = frequenti;
  const seconda = frequenti.find(([x]) => prima && Math.abs(x - prima[0]) >= 40);
  if (!prima || !seconda) return undefined;
  return { xNumero, xDomanda: Math.min(prima[0], seconda[0]), xRisposta: Math.max(prima[0], seconda[0]) };
}

/**
 * Dai pezzi di testo (nell'ordine del PDF: numero, righe della domanda, righe della risposta)
 * alle righe della tabella. Quello che c'è prima della prima riga numerata (copertina) si salta.
 */
export function leggiTabella(elementi: Elemento[]): RigaTabella[] {
  const col = colonne(elementi);
  if (!col) return [];
  type Parte = { testo: string; y: number; fine: number; pagina: number };
  const righe: { numero: number; sezione?: string; domanda: Parte[]; risposta: Parte[] }[] = [];
  let sezione: string | undefined;

  for (const e of elementi) {
    const testo = e.testo.replace(/ /g, " ");
    if (!testo.trim()) continue;
    const titolo = testo.trim().match(RE_SEZIONE);
    if (titolo) {
      sezione = pulisci(titolo[1]!);
      continue;
    }
    if (RE_NUMERO.test(testo.trim()) && Math.abs(e.x - col.xNumero) <= 4) {
      righe.push({ numero: Number(testo.trim()), sezione, domanda: [], risposta: [] });
      continue;
    }
    const riga = righe.at(-1);
    if (!riga || e.x < col.xDomanda - 4) continue;
    const parti = e.x < col.xRisposta - 3 ? riga.domanda : riga.risposta;
    const ultima = parti.at(-1);
    // Sulla stessa riga e attaccato al pezzo prima ("vera" + "?"): senza spazio.
    if (ultima && ultima.pagina === e.pagina && Math.abs(ultima.y - e.y) < 2 && e.x - ultima.fine < 1.5) {
      ultima.testo += testo;
      ultima.fine = e.x + e.larghezza;
    } else {
      parti.push({ testo, y: e.y, fine: e.x + e.larghezza, pagina: e.pagina });
    }
  }
  return righe.map((r) => ({
    numero: r.numero,
    domanda: unisci(r.domanda.map((p) => p.testo)),
    risposta: unisci(r.risposta.map((p) => p.testo)),
    ...(r.sezione ? { sezione: r.sezione } : {}),
  }));
}

// ── Alternative ricavate ─────────────────────────────────────────────────────

/** Minuscolo, senza accenti e punteggiatura: per confrontare risposte e inizi di domanda. */
const normale = (s: string) =>
  s
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9<>=/;]+/g, " ")
    .trim();

/** Le prime n parole della domanda, senza numeri: domande "dello stesso tipo". */
const famiglia = (domanda: string, n: number) =>
  normale(domanda)
    .replace(/[0-9<>=/;]+/g, " ")
    .split(/\s+/)
    .filter(Boolean)
    .slice(0, n)
    .join(" ");

/**
 * Struttura della parte dopo il "?" (solo simboli e incognite): "Renzo : I Promessi sposi = X : Y"
 * → ":=X:Y" (coppia libera), "Assegnare : X = commuovere : Y" → ":X=:Y". Tiene insieme le
 * proporzioni dello stesso tipo.
 */
const struttura = (domanda: string) =>
  domanda
    .slice(domanda.lastIndexOf("?") + 1)
    .replace(/\b(?![XY]\b)[^\s:=]+/g, "")
    .replace(/\s+/g, "");

/** Forma della risposta: le alternative devono avere la stessa, o si riconoscono a colpo d'occhio. */
export function forma(r: string): string {
  if (/^X\s*=.*;\s*Y\s*=/i.test(r)) return "xy";
  if (/^X\s*=/i.test(r)) return "x";
  if (/\s\/\s/.test(r)) return "coppia";
  if (/^-?\d+(?:[.,]\d+)?\s*%?$/.test(r)) return "numero";
  if (/^[A-Z]$/.test(r)) return "lettera";
  const parole = r.split(/\s+/).length;
  // Maiuscolo (es. "FRASCA") a parte: si confonde con le parole minuscole.
  const maiuscola = r === r.toUpperCase() && /[A-Z]/.test(r) ? "-maiuscola" : "";
  return (parole === 1 ? "parola" : parole <= 3 ? "breve" : "frase") + maiuscola;
}

/** Coppie vero/falso: l'unica alternativa sensata è l'altra. */
const OPPOSTI: Record<string, string> = { vera: "Falsa", falsa: "Vera", vero: "Falso", falso: "Vero", si: "No", sì: "No", no: "Sì" };

/** Lettere dell'alfabeto italiano, per le serie di lettere ("L, I, H, G, ?"). */
const ALFABETO = "ABCDEFGHILMNOPQRSTUVZ";

/**
 * "Se A<B, B>C, D>B, quale delle seguenti affermazioni è sicuramente vera?": le alternative
 * si calcolano dalle relazioni date, scegliendo solo affermazioni che NON sono sicuramente vere
 * (o sicuramente false, se la domanda chiede la falsa). undefined se la domanda non è così.
 */
export function alternativeRelazioni(domanda: string, risposta: string, seme: number): string[] | undefined {
  const m = domanda.match(/^(.*?)\bquale delle seguenti affermazioni [eè] sicuramente (vera|falsa)/i);
  if (!m || !/^[A-Z]\s*[<>]\s*[A-Z]$/.test(risposta)) return undefined;
  // a > b per ogni relazione data: "A<B" vuol dire B > A.
  const maggioreDi = new Map<string, Set<string>>();
  const lettere = new Set<string>();
  for (const [, a, op, b] of m[1]!.matchAll(/\b([A-Z])\s*([<>])\s*([A-Z])\b/g)) {
    const [alto, basso] = op === ">" ? [a!, b!] : [b!, a!];
    lettere.add(a!).add(b!);
    maggioreDi.set(alto, (maggioreDi.get(alto) ?? new Set()).add(basso));
  }
  // Sicuramente a > b: c'è una catena a > … > b.
  const sopra = (a: string, b: string, visti = new Set<string>()): boolean =>
    [...(maggioreDi.get(a) ?? [])].some((c) => c === b || (!visti.has(c) && (visti.add(c), sopra(c, b, visti))));
  // Vero o falso per una relazione "A > B", undefined se non si deduce dalle relazioni lette.
  const vale = (s: string) => {
    const [, a, op, b] = s.match(/^([A-Z])\s*([<>])\s*([A-Z])$/)!;
    const [alto, basso] = op === ">" ? [a!, b!] : [b!, a!];
    return sopra(alto, basso) ? true : sopra(basso, alto) ? false : undefined;
  };
  const chiedeVera = m[2]!.toLowerCase() === "vera";
  // La risposta del file deve tornare con le relazioni lette, o non ci si fida del calcolo.
  if (vale(risposta.replace(/\s/g, "")) !== chiedeVera) return undefined;
  const tutte = [...lettere].flatMap((a) => [...lettere].filter((b) => b !== a).flatMap((b) => [`${a}<${b}`, `${a}>${b}`]));
  const buone = tutte.filter((s) => s !== risposta.replace(/\s/g, "") && vale(s) !== chiedeVera);
  return mescolaStabile(buone, seme).slice(0, ALTERNATIVE);
}

/** Numeri vicini alla risposta (stesso formato): in un calcolo sono sicuramente sbagliati. */
function numeriVicini(r: string, seme: number): string[] {
  const virgola = r.includes(",");
  const percento = r.trim().endsWith("%");
  const n = Number(r.replace("%", "").replace(",", ".").trim());
  const decimali = (r.replace("%", "").trim().split(/[.,]/)[1] ?? "").length;
  const passo = decimali ? 10 ** -decimali : 1;
  const vicini = [n - passo, n + passo, n + 2 * passo, n - 2 * passo].filter((v) => n < 0 || v >= 0);
  return mescolaStabile(vicini, seme)
    .slice(0, ALTERNATIVE)
    .map((v) => {
      const s = v.toFixed(decimali);
      return (virgola ? s.replace(".", ",") : s) + (percento ? "%" : "");
    });
}

/** Lettere vicine nell'alfabeto italiano, per le serie. */
function lettereVicine(r: string, seme: number): string[] {
  const i = ALFABETO.indexOf(r);
  if (i < 0) return [];
  const vicine = [i - 2, i - 1, i + 1, i + 2].filter((j) => j >= 0 && j < ALFABETO.length).map((j) => ALFABETO[j]!);
  return mescolaStabile(vicine, seme).slice(0, ALTERNATIVE);
}

/** "X = Geppetto; Y = Pinocchio" → ["Geppetto", "Pinocchio"]; "cucire / latta" → ["cucire", "latta"]. */
function partiCoppia(r: string, f: string): [string, string] | undefined {
  const m = f === "xy" ? r.match(/^X\s*=\s*(.+?);\s*Y\s*=\s*(.+)$/i) : f === "coppia" ? r.match(/^(.+?)\s+\/\s+(.+)$/) : null;
  return m && !m[2]!.includes(" / ") ? [m[1]!.trim(), m[2]!.trim()] : undefined;
}
/** Ricompone una coppia nella forma del file ("X = a; Y = b" oppure "a / b"). */
const componiCoppia = ([a, b]: [string, string], f: string) => (f === "xy" ? `X = ${a}; Y = ${b}` : `${a} / ${b}`);

/**
 * Alternative per le risposte a coppie. Un'altra coppia del file può essere giusta anche lei:
 * in "Renzo : I Promessi sposi = X : Y" va bene ogni personaggio con la sua opera, quindi
 * "Mirandolina; La Locandiera" non può fare da alternativa. Si incrociano le coppie: la X giusta
 * con la Y di un'altra, una X di un'altra con la Y giusta, due di altre. Nessuna combinazione
 * presente nel file (sarebbe una coppia vera).
 */
function alternativeCoppie(giusta: [string, string], altre: [string, string][], vere: Set<string>, f: string, seme: number): string[] {
  const gia = new Set([normale(componiCoppia(giusta, f))]);
  // Coppia accettabile come alternativa: parti diverse, non vera, non già usata.
  const buona = (c: [string, string]) => {
    const n = normale(componiCoppia(c, f));
    return normale(c[0]) !== normale(c[1]) && !vere.has(n) && !gia.has(n);
  };
  const mescolate = mescolaStabile(altre, seme);
  const tentativi: [string, string][][] = [
    mescolate.map((o) => [giusta[0], o[1]]),
    mescolate.map((o) => [o[0], giusta[1]]),
    mescolate.flatMap((o, i) => mescolate.slice(i + 1).map((p): [string, string] => [o[0], p[1]])),
  ];
  const out: string[] = [];
  // Una per tipo, finché ce ne sono, poi si riempie.
  for (let giro = 0; out.length < ALTERNATIVE && giro < 3; giro++) {
    for (const lista of tentativi) {
      if (out.length >= ALTERNATIVE) break;
      const c = lista.find(buona);
      if (!c) continue;
      gia.add(normale(componiCoppia(c, f)));
      out.push(componiCoppia(c, f));
    }
  }
  return out;
}

/** Perché una domanda non si può trasformare in scelta multipla, se non si può. */
export function motivoScarto(domanda: string): string | undefined {
  // "Non ha nulla a che fare con la parola alba": un'altra risposta presa a caso (es. "lama")
  // non ha nulla a che fare con "alba" neanche lei, quindi sarebbe giusta anche quella.
  if (/^\s*(?:non ha nulla a che (?:fare|vedere)|non (?:è )?attinente|non appartiene|non fa parte|non c'entra)/i.test(domanda)) {
    return "domanda al negativo: le alternative prese da altre risposte sarebbero giuste anche loro";
  }
  // "Quale delle seguenti parole non ha lo stesso significato delle altre?" e basta: le parole mancano.
  const dopo = domanda.slice(domanda.lastIndexOf("?") + 1).trim();
  if (/\b(?:delle|tra le|fra le|tra i|fra i)\s+seguenti\s+(?:parole|termini|numeri|lettere|coppie)\b|delle altre\s*\?/i.test(domanda) && !dopo && !domanda.includes(":")) {
    return "il file non riporta le alternative tra cui scegliere";
  }
  if (/\b(?:figura|immagine|grafico|disegno)\b/i.test(domanda)) return "domanda con una figura che il file non contiene";
  return undefined;
}

/**
 * Dalle righe della tabella alle domande a scelta multipla. Per ogni domanda le alternative
 * sono, in ordine di preferenza: calcolate (vero/falso, relazioni, numeri, lettere), poi risposte
 * di domande con lo stesso inizio (3 parole, poi 2) e la stessa forma, poi della stessa forma
 * nella sezione, infine in tutto il file. Tra le candidate, prima quelle di lunghezza simile.
 */
export function domandeDallaTabella(righe: RigaTabella[]): Estrazione {
  const risultato: Estrazione = { domande: [], scartate: [], formati: {} };
  const valide: RigaTabella[] = [];
  const visti = new Set<string>();
  for (const r of righe) {
    // Mette la riga tra le scartate, con il motivo.
    const scarta = (motivo: string) => risultato.scartate.push({ numero: r.numero, motivo });
    if (r.domanda.length < 3) { scarta("testo della domanda mancante"); continue; }
    if (!r.risposta) { scarta("risposta esatta mancante"); continue; }
    const motivo = motivoScarto(r.domanda);
    if (motivo) { scarta(motivo); continue; }
    const chiave = normale(`${r.domanda}|${r.risposta}`);
    if (visti.has(chiave)) { scarta("domanda già presente (doppione)"); continue; }
    visti.add(chiave);
    valide.push(r);
  }

  // Indici delle risposte: per famiglia di domanda + forma, per sezione + forma, per forma.
  const indice = new Map<string, string[]>();
  // Aggiunge una risposta all'indice sotto la chiave `k`.
  const aggiungi = (k: string, risposta: string) => {
    const lista = indice.get(k);
    if (lista) lista.push(risposta);
    else indice.set(k, [risposta]);
  };
  for (const r of valide) {
    const f = forma(r.risposta);
    aggiungi(`st|${r.sezione}|${famiglia(r.domanda, 3)}|${struttura(r.domanda)}|${f}`, r.risposta);
    aggiungi(`f3|${r.sezione}|${famiglia(r.domanda, 3)}|${f}`, r.risposta);
    aggiungi(`f2|${r.sezione}|${famiglia(r.domanda, 2)}|${f}`, r.risposta);
    aggiungi(`s|${r.sezione}|${f}`, r.risposta);
    aggiungi(`t|${f}`, r.risposta);
  }

  // Tutte le coppie del file (per non usarne una vera come alternativa).
  const vere = new Set(valide.filter((r) => partiCoppia(r.risposta, forma(r.risposta))).map((r) => normale(r.risposta)));
  // Chiavi dell'indice per una riga, dalla più specifica alla più generica.
  const chiavi = (r: RigaTabella, f: string) => [`st|${r.sezione}|${famiglia(r.domanda, 3)}|${struttura(r.domanda)}|${f}`, `f3|${r.sezione}|${famiglia(r.domanda, 3)}|${f}`, `f2|${r.sezione}|${famiglia(r.domanda, 2)}|${f}`, `s|${r.sezione}|${f}`, `t|${f}`];

  for (const r of valide) {
    const f = forma(r.risposta);
    const giusta = normale(r.risposta);
    const coppia = partiCoppia(r.risposta, f);
    let alternative: string[] = [];
    const opposta = OPPOSTI[r.risposta.trim().toLowerCase()];
    if (opposta) alternative = [opposta];
    else if (f === "numero") alternative = numeriVicini(r.risposta, r.numero);
    else if (f === "lettera") alternative = lettereVicine(r.risposta, r.numero);
    else if (coppia) {
      // Le coppie delle domande più simili (stesso inizio), poi della sezione.
      const altre = new Map<string, [string, string]>();
      for (const k of chiavi(r, f)) {
        for (const c of indice.get(k) ?? []) {
          const parti = partiCoppia(c, f);
          if (parti && normale(c) !== giusta && altre.size < 16) altre.set(normale(c), parti);
        }
        if (altre.size >= 6) break;
      }
      // Prima le coppie che somigliano alla giusta: nomi propri con nomi propri ("Geppetto;
      // Pinocchio" con "Eva; Genesi"), parole comuni con parole comuni.
      const maiuscola = (t: string) => /^[A-ZÀ-Ú]/.test(t);
      // Quanto una coppia somiglia a quella giusta (nomi propri al posto di nomi propri): 0, 1 o 2.
      const somiglia = (c: [string, string]) => Number(maiuscola(c[0]) === maiuscola(coppia[0])) + Number(maiuscola(c[1]) === maiuscola(coppia[1]));
      const ordinate = [...altre.values()].sort((a, b) => somiglia(b) - somiglia(a));
      const migliori = ordinate.filter((c) => somiglia(c) === somiglia(ordinate[0]!));
      alternative = alternativeCoppie(coppia, migliori.length >= 2 ? migliori : ordinate, vere, f, r.numero);
    } else alternative = alternativeRelazioni(r.domanda, r.risposta, r.numero) ?? [];

    if (!alternative.length) {
      const scelte = new Map<string, string>();
      const domandaNormale = ` ${normale(r.domanda)} `;
      for (const k of chiavi(r, f)) {
        if (scelte.size >= ALTERNATIVE) break;
        const candidate = [...new Set(indice.get(k) ?? [])].filter((c) => {
          const n = normale(c);
          // Non la giusta, non già scelta, non una parola della domanda stessa.
          return n && n !== giusta && !scelte.has(n) && !domandaNormale.includes(` ${n} `);
        });
        // Prima quelle di lunghezza simile alla giusta, poi a caso (ma sempre uguale) tra le vicine.
        const vicine = candidate.sort((a, b) => Math.abs(a.length - r.risposta.length) - Math.abs(b.length - r.risposta.length) || a.localeCompare(b)).slice(0, 12);
        for (const c of mescolaStabile(vicine, r.numero)) {
          if (scelte.size >= ALTERNATIVE) break;
          scelte.set(normale(c), c);
        }
      }
      alternative = [...scelte.values()];
    }
    if (!alternative.length) {
      risultato.scartate.push({ numero: r.numero, motivo: "nessuna alternativa ricavabile dalle altre risposte" });
      continue;
    }

    const opzioni = [r.risposta, ...alternative];
    const ordine = mescolaStabile(opzioni.map((_, i) => i), r.numero);
    const domanda: DomandaEstratta = {
      numero: r.numero,
      testo: r.domanda,
      opzioni: ordine.map((i) => opzioni[i]!),
      corretta: ordine.indexOf(0),
      ...(r.sezione ? { sezione: r.sezione } : {}),
      // "Come nel PDF": la risposta del file per prima, poi le alternative ricavate.
      pdf: { opzioni, corretta: 0 },
      alternativeRicavate: true,
    };
    risultato.domande.push(domanda);
    risultato.formati.risposta = (risultato.formati.risposta ?? 0) + 1;
  }
  return risultato;
}

/** Dai pezzi di testo del PDF alle domande: tabella con la sola risposta esatta. */
export const estraiDomandeRisposta = (elementi: Elemento[]) => domandeDallaTabella(leggiTabella(elementi));
