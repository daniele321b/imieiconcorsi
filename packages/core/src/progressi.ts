import type { ProgressoBanca, SelezioneBanca } from "./domain";

// Progressi nelle banche dati: mappe di bit delle domande fatte e sbagliate (vedi ProgressoBanca).
// Il numero di una domanda è quello del suo id: "n00042" → 42, e il bit 42 è il suo.

/** Numero della domanda dall'id nella tabella delle domande ("n00042" → 42). */
export const numeroDomanda = (id: string) => Number(id.slice(1));

/** true se il bit n della mappa è acceso (mappa assente = tutto spento). */
export function bitAcceso(bits: Uint8Array | undefined, n: number) {
  const byte = n >> 3;
  return !!bits && byte < bits.length && (bits[byte]! & (1 << (n & 7))) !== 0;
}

/** Copia di `bits` con il bit n acceso o spento (la mappa si allunga se serve). */
function conBit(bits: Uint8Array, n: number, acceso: boolean) {
  const byte = n >> 3;
  const out = new Uint8Array(Math.max(bits.length, byte + 1));
  out.set(bits);
  if (acceso) out[byte]! |= 1 << (n & 7);
  else out[byte]! &= ~(1 << (n & 7));
  return out;
}

/** Quanti bit accesi. */
export function contaBit(bits: Uint8Array | undefined) {
  let n = 0;
  for (const b of bits ?? []) {
    let x = b;
    while (x) {
      n += x & 1;
      x >>= 1;
    }
  }
  return n;
}

/** Esito di una domanda in una sessione consegnata (le domande lasciate in bianco non si passano). */
export interface EsitoDomanda {
  numero: number;
  giusta: boolean;
}

/** Nuove mappe dopo una sessione: la domanda è fatta; sbagliata se l'ultima risposta era sbagliata. */
export function aggiornaProgresso(prima: Pick<ProgressoBanca, "fatte" | "sbagliate"> | undefined, esiti: EsitoDomanda[]) {
  let fatte = prima?.fatte ?? new Uint8Array();
  let sbagliate = prima?.sbagliate ?? new Uint8Array();
  for (const e of esiti) {
    fatte = conBit(fatte, e.numero, true);
    sbagliate = conBit(sbagliate, e.numero, !e.giusta);
  }
  return { fatte, sbagliate, nFatte: contaBit(fatte), nSbagliate: contaBit(sbagliate) };
}

/**
 * Le domande da proporre per prime e quelle per completare il numero richiesto:
 * - nuove: prima quelle mai fatte; finite quelle, le già fatte;
 * - sbagliate: solo quelle sbagliate l'ultima volta;
 * - tutte: tutte allo stesso modo.
 */
export function candidatePerSelezione<T extends { id: string }>(
  domande: T[],
  progresso: Pick<ProgressoBanca, "fatte" | "sbagliate"> | undefined,
  selezione: SelezioneBanca,
): { prima: T[]; poi: T[] } {
  if (selezione === "tutte" || (!progresso && selezione === "nuove")) return { prima: domande, poi: [] };
  if (selezione === "sbagliate") return { prima: domande.filter((d) => bitAcceso(progresso?.sbagliate, numeroDomanda(d.id))), poi: [] };
  const fatta = (d: T) => bitAcceso(progresso?.fatte, numeroDomanda(d.id));
  return { prima: domande.filter((d) => !fatta(d)), poi: domande.filter(fatta) };
}
