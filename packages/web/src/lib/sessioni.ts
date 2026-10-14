import { useState } from "react";
import { useNavigate } from "react-router";
import { api, ApiError, type NuovaSessione, type SessioneApi } from "./api";
import { leggiOrdineRisposte } from "./ordineRisposte";

/** Avvia una sessione di studio o una simulazione e apre la pagina della sessione. */
export function useAvviaSessione() {
  const navigate = useNavigate();
  const [inCorso, setInCorso] = useState<string>();
  const [errore, setErrore] = useState<ApiError>();

  // Crea la sessione sul server e la apre; `chiave` indica quale pulsante è in attesa.
  async function avvia(input: NuovaSessione, chiave: string = input.tipo) {
    setInCorso(chiave);
    setErrore(undefined);
    try {
      // Le risposte delle banche dati nell'ordine scelto dall'utente (senza banca dati non conta).
      const sessione = await api<SessioneApi>("/sessioni", { method: "POST", body: { ordineRisposte: leggiOrdineRisposte(), ...input } });
      navigate(`/app/sessione/${sessione.id}`, { state: sessione });
    } catch (err) {
      setErrore(err instanceof ApiError ? err : new ApiError(0, "Errore di rete"));
    } finally {
      setInCorso(undefined);
    }
  }

  return { avvia, inCorso, errore, chiudiErrore: () => setErrore(undefined) };
}
