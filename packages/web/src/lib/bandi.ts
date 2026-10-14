import { scaduto, type ConcorsoInLista } from "@imieiconcorsi/core/concorsi";
import { COMPARTO_IDS, type CompartoId } from "@imieiconcorsi/core/domain";
import { useEffect, useState } from "react";
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

/** Giorni in cui un bando da caricare è "nuovo". */
export const GIORNI_NUOVO = 7;

/** Nel browser dell'admin: i bandi da caricare già visti nell'elenco (il pallino rosso li esclude). */
const CHIAVE_VISTI = "admin:bandi-da-caricare-visti";
const EVENTO_VISTI = "bandi-da-caricare-visti";

/** Id dei bandi da caricare già visti dall'admin (salvati nel browser). */
function bandiVisti(): Set<string> {
  try {
    return new Set(JSON.parse(localStorage.getItem(CHIAVE_VISTI) ?? "[]") as string[]);
  } catch {
    return new Set();
  }
}

/** L'admin ha aperto l'elenco: questi bandi non contano più nel pallino rosso. */
export function segnaBandiVisti(ids: string[]) {
  try {
    const visti = bandiVisti();
    ids.forEach((id) => visti.add(id));
    // Si tengono solo gli ultimi 2.000 (i bandi vecchi escono comunque dall'elenco).
    localStorage.setItem(CHIAVE_VISTI, JSON.stringify([...visti].slice(-2000)));
  } catch {}
  window.dispatchEvent(new Event(EVENTO_VISTI));
}

/**
 * Solo per l'admin: bandi aperti che citano una banca dati non ancora caricata. `tutti` e
 * `nuovi` (usciti negli ultimi GIORNI_NUOVO giorni) per il cruscotto; `daVedere` = nuovi non
 * ancora visti nell'elenco, per il pallino rosso (si azzera aprendo l'elenco).
 * La lista dei bandi si scarica una volta per sessione.
 */
export function useBandiDaCaricare(attivo: boolean) {
  const [nuovi, setNuovi] = useState<string[]>();
  const [tutti, setTutti] = useState(0);
  const [visti, setVisti] = useState(bandiVisti);
  useEffect(() => {
    if (!attivo) return;
    caricaBandi(COMPARTO_IDS)
      .then((bandi) => {
        const attesa = bandi.filter((c) => c.bancaDatiPrevista && !c.bancaDati && !scaduto(c));
        const da = Date.now() - GIORNI_NUOVO * 86_400_000;
        setTutti(attesa.length);
        setNuovi(attesa.filter((c) => c.pubblicatoIl && Date.parse(c.pubblicatoIl) > da).map((c) => c.id));
      })
      .catch(() => setNuovi(undefined));
    // Rilegge i visti quando un'altra parte del sito li cambia.
    const aggiorna = () => setVisti(bandiVisti());
    window.addEventListener(EVENTO_VISTI, aggiorna);
    return () => window.removeEventListener(EVENTO_VISTI, aggiorna);
  }, [attivo]);
  if (!nuovi) return undefined;
  return { tutti, nuovi: nuovi.length, daVedere: nuovi.filter((id) => !visti.has(id)).length };
}
