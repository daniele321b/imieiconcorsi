import type { Provenienza } from "./domain";

// Provenienza degli iscritti (pannello admin → Provenienza iscritti). I link dei social e degli
// annunci portano i parametri UTM (?utm_source=instagram&utm_medium=social&utm_campaign=bio): il
// sito li ricorda fino all'iscrizione (web lib/provenienza.ts) e il primo GET /me li salva nel
// profilo appena creato, una volta sola. Si tengono solo questi quattro parametri, ripuliti:
// niente identificativi di clic (fbclid, ttclid, gclid) né altro dell'indirizzo.

/** Parametro dell'indirizzo → campo della provenienza. */
export const PARAMETRI_UTM = {
  utm_source: "fonte",
  utm_medium: "mezzo",
  utm_campaign: "campagna",
  utm_content: "contenuto",
} as const satisfies Record<string, keyof Provenienza>;

/** Lunghezza massima di ogni valore. */
const MAX = 40;

/** Etichetta di chi si è iscritto senza un link con utm_source (o prima che esistesse). */
export const SENZA_FONTE = "diretto";

/** Un valore UTM ripulito: minuscolo, spazi in "_", solo lettere, cifre, ".", "-" e "_". Vuoto → undefined. */
export function pulisciValore(valore: unknown): string | undefined {
  if (typeof valore !== "string") return undefined;
  const pulito = valore
    .trim()
    .toLowerCase()
    .replace(/\s+/g, "_")
    .replace(/[^a-z0-9._-]/g, "")
    .slice(0, MAX);
  return pulito || undefined;
}

/** Provenienza dai parametri UTM (query string o valori salvati); senza utm_source non c'è. */
export function provenienzaDa(parametri: Record<string, unknown>): Provenienza | undefined {
  const fonte = pulisciValore(parametri.utm_source);
  if (!fonte) return undefined;
  const provenienza: Provenienza = { fonte };
  for (const [parametro, campo] of Object.entries(PARAMETRI_UTM)) {
    if (campo === "fonte") continue;
    const valore = pulisciValore(parametri[parametro]);
    if (valore) provenienza[campo] = valore;
  }
  return provenienza;
}

/** Query string con i parametri UTM di una provenienza ("?utm_source=…"), per GET /me. */
export function queryProvenienza(provenienza: Provenienza): string {
  const query = new URLSearchParams();
  for (const [parametro, campo] of Object.entries(PARAMETRI_UTM)) {
    const valore = provenienza[campo];
    if (valore) query.set(parametro, valore);
  }
  return `?${query}`;
}

/** Una riga del riepilogo: iscritti con la stessa fonte, mezzo, campagna e contenuto. */
export interface RigaProvenienza {
  fonte: string;
  mezzo?: string;
  campagna?: string;
  contenuto?: string;
  ultimi7: number;
  ultimi30: number;
  totale: number;
}

/**
 * Iscritti per provenienza negli ultimi 7 e 30 giorni e in tutto (dalla data di creazione del
 * profilo). Chi non ha provenienza finisce sotto SENZA_FONTE. Righe dalla più numerosa nei 30 giorni.
 */
export function riepilogoProvenienza(profili: { createdAt?: string; provenienza?: Provenienza }[], ora = new Date()) {
  const righe = new Map<string, RigaProvenienza>();
  const totali = { ultimi7: 0, ultimi30: 0, totale: 0 };
  for (const profilo of profili) {
    const { fonte, mezzo, campagna, contenuto } = profilo.provenienza ?? { fonte: SENZA_FONTE };
    const chiave = [fonte, mezzo, campagna, contenuto].map((v) => v ?? "").join("|");
    const riga = righe.get(chiave) ?? { fonte, mezzo, campagna, contenuto, ultimi7: 0, ultimi30: 0, totale: 0 };
    const giorni = profilo.createdAt ? (ora.getTime() - Date.parse(profilo.createdAt)) / 864e5 : Infinity;
    for (const conto of [riga, totali]) {
      conto.totale++;
      if (giorni <= 30) conto.ultimi30++;
      if (giorni <= 7) conto.ultimi7++;
    }
    righe.set(chiave, riga);
  }
  const ordinate = [...righe.values()].sort(
    (a, b) => b.ultimi30 - a.ultimi30 || b.totale - a.totale || a.fonte.localeCompare(b.fonte),
  );
  return { totali, righe: ordinate };
}
