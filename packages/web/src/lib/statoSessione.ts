import { useEffect, useState, type Dispatch, type SetStateAction } from "react";

// Stato di una pagina che sopravvive quando si apre un'altra pagina e si torna indietro (es. i
// filtri della ricerca dei bandi dopo aver aperto un bando). Resta in sessionStorage: vale per la
// scheda del browser e si azzera chiudendola.

/** Come useState, ma il valore si salva in sessionStorage sotto `chiave` e si ritrova al ritorno. */
export function useStatoSessione<T>(chiave: string, iniziale: T): [T, Dispatch<SetStateAction<T>>] {
  const [valore, setValore] = useState<T>(() => {
    try {
      const salvato = sessionStorage.getItem(chiave);
      return salvato === null ? iniziale : (JSON.parse(salvato) as T);
    } catch {
      return iniziale;
    }
  });
  useEffect(() => {
    try {
      sessionStorage.setItem(chiave, JSON.stringify(valore));
    } catch {}
  }, [chiave, valore]);
  return [valore, setValore];
}
