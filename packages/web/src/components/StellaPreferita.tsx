import { Star } from "lucide-react";
import { useEffect, useState } from "react";
import { api } from "../lib/api";
import { cx } from "./ui";

/**
 * Stella "preferita" su una domanda di una banca dati ufficiale: la salva per ritrovarla dopo
 * (consultazione → "Solo preferite", sessioni sulle preferite). Si accende subito e torna come
 * prima se il server non risponde. `onCambio` riceve il nuovo stato e quante preferite ci sono.
 */
export function StellaPreferita({
  bancaId,
  numero,
  preferita,
  onCambio,
  conTesto = false,
  className,
}: {
  bancaId: string;
  /** Numero della domanda nella banca dati */
  numero: number;
  preferita: boolean;
  onCambio?: (preferita: boolean, quante: number) => void;
  /** Mostra anche la scritta ("Salva" / "Salvata") accanto alla stella */
  conTesto?: boolean;
  className?: string;
}) {
  const [attiva, setAttiva] = useState(preferita);
  const [inCorso, setInCorso] = useState(false);
  const [errore, setErrore] = useState(false);
  useEffect(() => setAttiva(preferita), [preferita, numero]);

  async function cambia() {
    const nuovo = !attiva;
    setAttiva(nuovo);
    setInCorso(true);
    setErrore(false);
    try {
      const r = await api<{ preferite: number }>(`/me/progressi/${encodeURIComponent(bancaId)}/preferite/${numero}`, {
        method: "PUT",
        body: { preferita: nuovo },
      });
      onCambio?.(nuovo, r.preferite);
    } catch {
      setAttiva(!nuovo);
      setErrore(true);
    } finally {
      setInCorso(false);
    }
  }

  return (
    <button
      type="button"
      onClick={() => void cambia()}
      disabled={inCorso}
      aria-pressed={attiva}
      aria-label={attiva ? "Togli dalle preferite" : "Salva tra le preferite"}
      title={errore ? "Non salvata: riprova" : attiva ? "Togli dalle preferite" : "Salva tra le preferite, per ritrovarla dopo"}
      className={cx(
        "inline-flex items-center gap-1.5 rounded-lg text-xs font-semibold transition",
        conTesto ? "px-2 py-1 ring-1" : "p-1.5",
        attiva ? "text-amber-700 ring-amber-200" : "text-slate-400 ring-slate-200 hover:text-amber-600",
        errore && "text-rose-600",
        className,
      )}
    >
      <Star className={cx("size-5", attiva && "fill-amber-400 text-amber-500")} />
      {conTesto && (attiva ? "Salvata" : "Salva")}
    </button>
  );
}
