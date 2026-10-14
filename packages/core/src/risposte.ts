// Ordine delle risposte delle banche dati ufficiali, scelto dall'utente entrando in una banca
// dati: "prima" = la giusta sempre per prima (A), "mescolate" = ordine casuale ma fisso per
// ogni domanda (stessa domanda, stesso ordine, ogni volta). Senza dipendenze AWS: lo usano
// il servizio studio (sessioni e punteggio) e il sito (consultazione).
import type { ModoRisposte } from "./domain";

/** Le due scelte, con il nome da mostrare nel sito. */
export const MODI_RISPOSTE: { id: ModoRisposte; nome: string }[] = [
  { id: "mescolate", nome: "Mescolate" },
  { id: "prima", nome: "Giusta sempre per prima" },
];

/** Numero stabile da un testo (FNV-1a), per mescolare sempre allo stesso modo. */
function seme(testo: string) {
  let h = 0x811c9dc5;
  for (let i = 0; i < testo.length; i++) {
    h ^= testo.charCodeAt(i);
    h = Math.imul(h, 0x01000193) >>> 0;
  }
  return h || 1;
}

/** Permutazione di 0..n-1 sempre uguale per la stessa chiave (xorshift dal seme della chiave). */
function mescolaStabile(n: number, chiave: string) {
  const out = Array.from({ length: n }, (_, i) => i);
  let x = seme(chiave);
  for (let i = n - 1; i > 0; i--) {
    x = (x ^ (x << 13)) >>> 0;
    x = (x ^ (x >>> 17)) >>> 0;
    x = (x ^ (x << 5)) >>> 0;
    const j = x % (i + 1);
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

/**
 * La domanda con le risposte nell'ordine scelto. `chiave` identifica la domanda (es. il suo
 * id): con "mescolate" la stessa chiave dà sempre lo stesso ordine.
 */
export function dispongiRisposte<T extends { opzioni: string[]; corretta: number }>(d: T, modo: ModoRisposte, chiave: string): T {
  const altre = d.opzioni.map((_, i) => i).filter((i) => i !== d.corretta);
  const ordine = modo === "prima" ? [d.corretta, ...altre] : mescolaStabile(d.opzioni.length, chiave);
  return { ...d, opzioni: ordine.map((i) => d.opzioni[i]), corretta: ordine.indexOf(d.corretta) };
}
