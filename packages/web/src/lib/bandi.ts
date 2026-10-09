import type { ConcorsoInLista } from "@imieiconcorsi/core/concorsi";
import type { CompartoId } from "@imieiconcorsi/core/domain";
import { api } from "./api";

// Lista dei bandi: file statici generati ogni mattina (S3 + CloudFront, /dati/bandi/),
// senza passare dall'API. Se mancano (prima generazione non ancora fatta) si usa l'API.

/** Il file indice.json: la versione corrente e, per comparto, il file da scaricare. */
interface IndiceBandi {
  versione: string;
  generatoIl: string;
  comparti: Partial<Record<CompartoId, { file: string; bandi: number }>>;
}

/** Un file per versione non cambia mai: si scarica una volta per sessione. */
const fileCaricati = new Map<string, Promise<ConcorsoInLista[]>>();

/** Scarica un file JSON statico. */
async function json<T>(percorso: string): Promise<T> {
  const res = await fetch(percorso, { headers: { accept: "application/json" } });
  if (!res.ok) throw new Error(`${percorso}: ${res.status}`);
  return (await res.json()) as T;
}

/** Bandi dei comparti indicati, dai file in cache (o dall'API se i file non ci sono ancora). */
export async function caricaBandi(comparti: readonly CompartoId[]): Promise<ConcorsoInLista[]> {
  try {
    const indice = await json<IndiceBandi>("/dati/bandi/indice.json");
    const liste = await Promise.all(
      comparti.map((c) => {
        const file = indice.comparti[c]?.file;
        if (!file) return Promise.resolve<ConcorsoInLista[]>([]);
        if (!fileCaricati.has(file)) {
          const p = json<ConcorsoInLista[]>(file);
          p.catch(() => fileCaricati.delete(file));
          fileCaricati.set(file, p);
        }
        return fileCaricati.get(file)!;
      }),
    );
    return liste.flat();
  } catch {
    const qs = new URLSearchParams({ comparto: comparti.length === 1 ? comparti[0] : "tutti", scaduti: "1" });
    const { concorsi } = await api<{ concorsi: ConcorsoInLista[] }>(`/concorsi?${qs}`);
    return comparti.length === 1 ? concorsi : concorsi.filter((c) => comparti.includes(c.comparto));
  }
}
