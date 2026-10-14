// Banche dati a tabella senza intestazione, con le risposte in colonna e la lettera della giusta
// nell'ultima, come quelle della Guardia di Finanza (avanzamenti interni, "Materiale testologico"):
//
//   | TSUYB00000077 | I procuratori europei delegati: | a) non sono… | b) sono… | c) … | d) … | c |
//
// Le colonne si riconoscono dalle risposte: i pezzi che iniziano con "a)", "b)"… stanno sempre
// alla stessa x. A sinistra il codice della domanda (lettere e cifre) e il testo, a destra la
// lettera della risposta giusta. Le celle sono allineate in alto: la riga inizia con il codice e
// quello che nella pagina sta sopra il primo codice è il titolo ("VIETATA LA PUBBLICAZIONE…").

import { mescolaStabile, unisciCella, type DomandaEstratta, type Estrazione } from "./parser";
import type { Elemento } from "./tabella";

/** Codice della domanda: "TSUYB00000076", "GDTTA0000366" o solo il numero. */
const RE_CODICE = /^[A-Z]{0,8}\d{1,12}$/;
/** Inizio di una risposta: "a) …". */
const RE_OPZIONE = /^([a-f])\)\s*/i;
/** Cella della risposta giusta: una lettera sola. */
const RE_LETTERA = /^[a-f]$/i;

/** Il valore più frequente (a parità, il più piccolo), con quante volte compare. */
function moda(valori: number[]): [number, number] | undefined {
  const conta = new Map<number, number>();
  for (const v of valori) conta.set(v, (conta.get(v) ?? 0) + 1);
  return [...conta].sort((a, b) => b[1] - a[1] || a[0] - b[0])[0];
}

/**
 * Le colonne della tabella (bordo sinistro di codice, domanda, risposte a-d, lettera giusta),
 * oppure undefined se il PDF non è fatto così: servono almeno le colonne "a)" e "b)" ripetute e
 * quella della lettera.
 */
export function colonneLettere(elementi: Elemento[]) {
  const pezzi = elementi.filter((e) => e.testo.trim());
  const lettere: string[] = [];
  const xRisposte: number[] = [];
  for (const l of "abcdef") {
    const m = moda(pezzi.filter((e) => e.testo.trim().toLowerCase().startsWith(`${l})`)).map((e) => Math.round(e.x)));
    if (!m || m[1] < 5 || (xRisposte.length && m[0] <= xRisposte.at(-1)! + 20)) break;
    lettere.push(l);
    xRisposte.push(m[0]);
  }
  if (lettere.length < 2) return undefined;
  const xLettera = moda(pezzi.filter((e) => RE_LETTERA.test(e.testo.trim()) && e.x > xRisposte.at(-1)! + 20).map((e) => Math.round(e.x)));
  const codici = pezzi.filter((e) => RE_CODICE.test(e.testo.trim()) && e.x < xRisposte[0]! - 60);
  const xCodice = moda(codici.map((e) => Math.round(e.x)));
  if (!xLettera || xLettera[1] < 5 || !xCodice || xCodice[1] < 3) return undefined;
  // La domanda: l'inizio più frequente tra i codici e la colonna "a)".
  const xDomanda = moda(pezzi.filter((e) => e.x > xCodice[0] + 20 && e.x < xRisposte[0]! - 5).map((e) => Math.round(e.x)));
  if (!xDomanda) return undefined;
  return { lettere, bordi: [xCodice[0], xDomanda[0], ...xRisposte, xLettera[0]] };
}

/** Dai pezzi di testo del PDF alle domande: tabella codice | domanda | a)-d) | lettera giusta. */
export function estraiDomandeLettere(elementi: Elemento[]): Estrazione {
  const risultato: Estrazione = { domande: [], scartate: [], formati: {} };
  const col = colonneLettere(elementi);
  if (!col) return risultato;
  const { lettere, bordi } = col;
  const iLettera = bordi.length - 1;
  /** Colonna di un pezzo: l'ultima con il bordo sinistro prima del suo inizio (codici allineati a destra: la prima). */
  const colonnaDi = (x: number) => {
    let k = 0;
    bordi.forEach((b, i) => {
      if (b <= x + 3) k = i;
    });
    return k;
  };

  // Primo codice di ogni pagina: quello che sta sopra è il titolo della pagina.
  const inCima = new Map<number, number>();
  for (const e of elementi) {
    if (colonnaDi(e.x) === 0 && RE_CODICE.test(e.testo.trim())) inCima.set(e.pagina, Math.max(inCima.get(e.pagina) ?? -Infinity, e.y));
  }

  type Parte = { testo: string; y: number; fine: number };
  const righe: { codice: string; celle: Parte[][] }[] = [];
  for (const e of elementi) {
    const testo = e.testo.replace(/ /g, " ");
    if (!testo.trim() || e.y > (inCima.get(e.pagina) ?? Infinity) + 2) continue;
    const k = colonnaDi(e.x);
    if (k === 0 && RE_CODICE.test(testo.trim())) {
      righe.push({ codice: testo.trim(), celle: bordi.map(() => []) });
      continue;
    }
    const cella = righe.at(-1)?.celle[k];
    if (!cella || k === 0) continue;
    const ultima = cella.at(-1);
    // Sulla stessa riga e attaccato al pezzo prima ("è" + ":"): senza spazio.
    if (ultima && Math.abs(ultima.y - e.y) < 2 && e.x - ultima.fine < 1.5) {
      ultima.testo += testo;
      ultima.fine = e.x + e.larghezza;
    } else {
      cella.push({ testo, y: e.y, fine: e.x + e.larghezza });
    }
  }

  const visti = new Set<string>();
  for (const r of righe) {
    const numero = Number(r.codice.replace(/\D/g, ""));
    // Mette la riga tra le scartate, con il motivo.
    const scarta = (motivo: string) => risultato.scartate.push({ numero, motivo });
    const celle = r.celle.map((c) => unisciCella(c.map((p) => p.testo)));
    const testo = celle[1] ?? "";
    // Le risposte senza "a) ": la lettera la dà la colonna.
    const risposte = lettere.map((l, i) => ({ l, testo: celle[i + 2]!.replace(RE_OPZIONE, "").trim() })).filter((o) => o.testo);
    const giusta = celle[iLettera]!.trim().toLowerCase();
    if (testo.length < 5) { scarta("testo della domanda mancante"); continue; }
    if (risposte.length < 2) { scarta("meno di due risposte"); continue; }
    if (!RE_LETTERA.test(giusta)) { scarta("lettera della risposta giusta mancante"); continue; }
    const corretta = risposte.findIndex((o) => o.l === giusta);
    if (corretta < 0) { scarta(`la risposta giusta (${giusta}) non è tra quelle lette`); continue; }
    const opzioni = risposte.map((o) => o.testo);
    if (new Set(opzioni.map((o) => o.toLowerCase())).size !== opzioni.length) { scarta("risposte ripetute"); continue; }
    const chiave = [testo, ...[...opzioni].sort()].join("|").toLowerCase();
    if (visti.has(chiave)) { scarta("domanda già presente (doppione)"); continue; }
    visti.add(chiave);

    const ordine = mescolaStabile(opzioni.map((_, i) => i), numero);
    const domanda: DomandaEstratta = {
      numero,
      testo,
      opzioni: ordine.map((i) => opzioni[i]!),
      corretta: ordine.indexOf(corretta),
      pdf: { opzioni, corretta },
    };
    risultato.domande.push(domanda);
    risultato.formati.lettera = (risultato.formati.lettera ?? 0) + 1;
  }
  return risultato;
}
