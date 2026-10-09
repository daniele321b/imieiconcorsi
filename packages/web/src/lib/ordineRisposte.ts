import type { ModoRisposte } from "@imieiconcorsi/core/domain";
import { useSyncExternalStore } from "react";

// Come vedere le risposte delle banche dati: scelta dell'utente, ricordata nel browser e
// condivisa da tutte le pagine (lista, concorso, consultazione, sessioni).

/** Chiave nel localStorage del browser. */
const CHIAVE = "banche-dati:ordine-risposte";
const PREDEFINITO: ModoRisposte = "mescolate";
const ascoltatori = new Set<() => void>();

/** La scelta salvata (mescolate se non c'è o se il browser blocca il localStorage). */
export function leggiOrdineRisposte(): ModoRisposte {
  try {
    const v = localStorage.getItem(CHIAVE);
    return v === "prima" || v === "mescolate" ? v : PREDEFINITO;
  } catch {
    return PREDEFINITO;
  }
}

/** Salva la scelta e avvisa le pagine aperte. */
export function impostaOrdineRisposte(modo: ModoRisposte) {
  try {
    localStorage.setItem(CHIAVE, modo);
  } catch {}
  ascoltatori.forEach((a) => a());
}

/** La scelta corrente per i componenti React, aggiornata quando cambia; restituisce [modo, imposta]. */
export function useOrdineRisposte() {
  const modo = useSyncExternalStore(
    (a) => {
      ascoltatori.add(a);
      return () => ascoltatori.delete(a);
    },
    leggiOrdineRisposte,
    () => PREDEFINITO,
  );
  return [modo, impostaOrdineRisposte] as const;
}
