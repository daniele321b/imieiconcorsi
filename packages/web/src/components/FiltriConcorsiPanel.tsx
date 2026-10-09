import type { FiltriConcorsi } from "@imieiconcorsi/core/concorsi";
import { tipoProcedura } from "../lib/format";

const select =
  "mt-1 block h-10 w-full rounded-xl border-0 bg-white px-3 text-sm text-slate-900 ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500";

const num = (v: string) => (v ? Number(v) : undefined);

/** Pannello dei filtri della ricerca: scadenza, data di uscita, posti, sede, procedura, banca dati. */
export function FiltriConcorsiPanel({
  value,
  onChange,
  procedure,
}: {
  value: FiltriConcorsi;
  onChange: (f: FiltriConcorsi) => void;
  /** Tipi di procedura presenti nei bandi caricati */
  procedure: string[];
}) {
  const set = (parziale: Partial<FiltriConcorsi>) => onChange({ ...value, ...parziale });

  return (
    <div className="grid gap-3 rounded-2xl bg-white p-4 shadow-sm ring-1 ring-slate-200 sm:grid-cols-2 lg:grid-cols-3">
      <label className="text-xs font-semibold text-slate-500">
        Scadenza
        <select value={value.scadeEntroGiorni ?? ""} onChange={(e) => set({ scadeEntroGiorni: num(e.target.value) })} className={select}>
          <option value="">Qualsiasi</option>
          <option value="7">Entro 7 giorni</option>
          <option value="15">Entro 15 giorni</option>
          <option value="30">Entro 30 giorni</option>
          <option value="60">Entro 60 giorni</option>
        </select>
      </label>
      <label className="text-xs font-semibold text-slate-500">
        Uscito
        <select value={value.pubblicatoDaGiorni ?? ""} onChange={(e) => set({ pubblicatoDaGiorni: num(e.target.value) })} className={select}>
          <option value="">In qualsiasi data</option>
          <option value="1">Da ieri</option>
          <option value="7">Negli ultimi 7 giorni</option>
          <option value="30">Negli ultimi 30 giorni</option>
        </select>
      </label>
      <label className="text-xs font-semibold text-slate-500">
        Posti
        <select value={value.postiMinimi ?? ""} onChange={(e) => set({ postiMinimi: num(e.target.value) })} className={select}>
          <option value="">Qualsiasi numero</option>
          <option value="2">Almeno 2</option>
          <option value="5">Almeno 5</option>
          <option value="10">Almeno 10</option>
          <option value="50">Almeno 50</option>
        </select>
      </label>
      <label className="text-xs font-semibold text-slate-500">
        Sede
        <input
          value={value.sede ?? ""}
          onChange={(e) => set({ sede: e.target.value || undefined })}
          placeholder="es. Lombardia, Napoli"
          className={select}
        />
      </label>
      <label className="text-xs font-semibold text-slate-500">
        Tipo di selezione
        <select value={value.procedura ?? ""} onChange={(e) => set({ procedura: e.target.value || undefined })} className={select}>
          <option value="">Tutte</option>
          {procedure.map((p) => (
            <option key={p} value={p}>
              {tipoProcedura(p)}
            </option>
          ))}
        </select>
      </label>
      <label className="flex items-center gap-2 self-end pb-2 text-sm font-medium text-slate-700">
        <input
          type="checkbox"
          checked={!!value.soloBancaDati}
          onChange={(e) => set({ soloBancaDati: e.target.checked || undefined })}
          className="size-4 rounded border-slate-300 text-brand-600 focus:ring-brand-500"
        />
        Solo con banca dati ufficiale
      </label>
    </div>
  );
}
