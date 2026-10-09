import { MODI_RISPOSTE } from "@imieiconcorsi/core/risposte";
import { useId } from "react";
import { useOrdineRisposte } from "../lib/ordineRisposte";
import { cx } from "./ui";

/**
 * Selettore "Risposta giusta: mescolata / sempre per prima" per le banche dati ufficiali.
 * Vale per consultazione, studio e simulazioni, e resta salvato nel browser.
 */
export function OrdineRisposte({ scuro = false, onCambio }: { scuro?: boolean; onCambio?: () => void }) {
  const [modo, imposta] = useOrdineRisposte();
  const etichetta = useId();
  return (
    <div className="flex flex-wrap items-center gap-2 text-sm">
      <span id={etichetta} className={scuro ? "text-brand-200" : "text-slate-500"}>
        Risposta giusta
      </span>
      <div role="radiogroup" aria-labelledby={etichetta} className={cx("inline-grid grid-cols-2 rounded-lg p-0.5 text-xs font-semibold", scuro ? "bg-white/10" : "bg-slate-100")}>
        {MODI_RISPOSTE.map((m) => {
          const attivo = modo === m.id;
          return (
            <button
              key={m.id}
              role="radio"
              aria-checked={attivo}
              onClick={() => {
                if (attivo) return;
                imposta(m.id);
                onCambio?.();
              }}
              className={cx(
                "rounded-md px-2.5 py-1 transition",
                attivo ? (scuro ? "bg-white text-brand-900" : "bg-white text-brand-700 shadow-sm") : scuro ? "text-brand-100" : "text-slate-500",
              )}
            >
              {m.id === "prima" ? "Sempre per prima (A)" : "Mescolata"}
            </button>
          );
        })}
      </div>
    </div>
  );
}
