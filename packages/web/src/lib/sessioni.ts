import { useState } from "react";
import { useNavigate } from "react-router";
import { api, ApiError, type NuovaSessione, type SessioneApi } from "./api";

/** Avvia una sessione di studio o una simulazione e apre la pagina della sessione. */
export function useAvviaSessione() {
  const navigate = useNavigate();
  const [inCorso, setInCorso] = useState<string>();
  const [errore, setErrore] = useState<ApiError>();

  async function avvia(input: NuovaSessione, chiave: string = input.tipo) {
    setInCorso(chiave);
    setErrore(undefined);
    try {
      const sessione = await api<SessioneApi>("/sessioni", { method: "POST", body: input });
      navigate(`/app/sessione/${sessione.id}`, { state: sessione });
    } catch (err) {
      setErrore(err instanceof ApiError ? err : new ApiError(0, "Errore di rete"));
    } finally {
      setInCorso(undefined);
    }
  }

  return { avvia, inCorso, errore, chiudiErrore: () => setErrore(undefined) };
}
