import { DOMANDE_MIN } from "@imieiconcorsi/core/domain";
import { useEffect, useState } from "react";
import { cx } from "./ui";

/**
 * Numero di domande scritto a mano (solo Pro, fino a `max`), accanto alle scelte fisse. Si
 * accende quando il numero scelto non è tra quelle. Casella vuota o numero fuori dai limiti:
 * `onChange(undefined)`, così la pagina non fa partire la sessione con un numero a metà
 * (scrivendo "150" si passa da "15").
 */
export function NumeroAMano({
  valore,
  onChange,
  max,
  fissi,
  scuro = false,
}: {
  valore: number | undefined;
  onChange: (n: number | undefined) => void;
  max: number;
  /** Le scelte già presenti come pulsanti */
  fissi: readonly number[];
  /** Su sfondo scuro (riquadro della simulazione nella pagina del concorso) */
  scuro?: boolean;
}) {
  const attivo = valore === undefined || !fissi.includes(valore);
  const [testo, setTesto] = useState(attivo ? String(valore) : "");
  // Scelto un pulsante (o scritto un numero che c'è già come pulsante): la casella si svuota.
  useEffect(() => {
    if (!attivo) setTesto("");
  }, [attivo]);
  const n = Number(testo);
  const fuori = testo !== "" && (!Number.isInteger(n) || n < DOMANDE_MIN || n > max);

  return (
    <label className={cx("flex items-center gap-2 text-xs font-semibold", scuro ? "text-brand-100" : "text-slate-500")}>
      Altro numero
      <input
        type="number"
        inputMode="numeric"
        min={DOMANDE_MIN}
        max={max}
        value={testo}
        placeholder={`${DOMANDE_MIN}-${max}`}
        onChange={(e) => {
          setTesto(e.target.value);
          const v = Number(e.target.value);
          onChange(e.target.value !== "" && Number.isInteger(v) && v >= DOMANDE_MIN && v <= max ? v : undefined);
        }}
        aria-invalid={fuori}
        className={cx(
          "h-8 w-20 rounded-lg border-0 px-2 text-sm font-bold tabular-nums ring-1 focus:ring-2 focus:outline-none",
          scuro ? "bg-white/10 text-white ring-white/20 placeholder:text-brand-200 focus:ring-white" : "bg-white text-slate-900 ring-slate-300 focus:ring-brand-500",
          attivo && !fuori && (scuro ? "bg-white !text-brand-900" : "ring-2 ring-brand-500"),
          fuori && "ring-2 !ring-rose-400",
        )}
      />
      {fuori && <span className={scuro ? "text-rose-200" : "text-rose-600"}>da {DOMANDE_MIN} a {max}</span>}
    </label>
  );
}
