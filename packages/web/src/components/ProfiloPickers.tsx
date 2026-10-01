import { COMPARTI, MATERIE, type CompartoId, type FrequenzaAvvisi, type MateriaId } from "@imieiconcorsi/core/domain";
import { Check } from "lucide-react";
import { IconaMateria } from "./brand";
import { Badge, cx } from "./ui";

export function InteressiPicker({ value, onChange }: { value: CompartoId[]; onChange: (v: CompartoId[]) => void }) {
  const toggle = (id: CompartoId) => onChange(value.includes(id) ? value.filter((v) => v !== id) : [...value, id]);
  return (
    <div className="grid gap-3 sm:grid-cols-2">
      {COMPARTI.map((c) => {
        const attivo = value.includes(c.id);
        return (
          <button
            key={c.id}
            type="button"
            onClick={() => toggle(c.id)}
            aria-pressed={attivo}
            className={cx(
              "relative rounded-2xl p-4 text-left ring-1 transition",
              attivo ? "bg-brand-50 ring-2 ring-brand-500" : "bg-white ring-slate-200 hover:ring-slate-300",
            )}
          >
            <div className="flex items-start justify-between gap-2">
              <p className="font-semibold text-slate-900">{c.nome}</p>
              <span
                className={cx(
                  "grid size-5 shrink-0 place-items-center rounded-full ring-1",
                  attivo ? "bg-brand-600 text-white ring-brand-600" : "ring-slate-300",
                )}
              >
                {attivo && <Check className="size-3.5" />}
              </span>
            </div>
            <p className="mt-1 text-sm text-slate-500">{c.descrizione}</p>
            {!c.contenuti && (
              <Badge tone="slate" className="mt-2">
                Solo avvisi per ora
              </Badge>
            )}
          </button>
        );
      })}
    </div>
  );
}

const LIVELLI = ["Base", "Elementare", "Medio", "Buono", "Ottimo"];

export function LivelliPicker({
  value,
  onChange,
}: {
  value: Partial<Record<MateriaId, number>>;
  onChange: (v: Partial<Record<MateriaId, number>>) => void;
}) {
  return (
    <div className="space-y-3">
      {MATERIE.map((m) => (
        <div key={m.id} className="flex flex-col gap-3 rounded-2xl bg-white p-4 ring-1 ring-slate-200 sm:flex-row sm:items-center">
          <div className="flex flex-1 items-center gap-3">
            <IconaMateria icona={m.icona} materia={m.id} />
            <div>
              <p className="font-semibold text-slate-900">{m.nome}</p>
              <p className="text-xs text-slate-500">{value[m.id] ? LIVELLI[value[m.id]! - 1] : "Non indicato"}</p>
            </div>
          </div>
          <div className="flex gap-1.5" role="radiogroup" aria-label={`Livello in ${m.nome}`}>
            {[1, 2, 3, 4, 5].map((n) => (
              <button
                key={n}
                type="button"
                role="radio"
                aria-checked={value[m.id] === n}
                aria-label={LIVELLI[n - 1]}
                onClick={() => onChange({ ...value, [m.id]: n })}
                className={cx(
                  "size-10 rounded-xl text-sm font-bold transition",
                  value[m.id] && n <= value[m.id]!
                    ? "bg-brand-600 text-white"
                    : "bg-slate-100 text-slate-500 hover:bg-slate-200",
                )}
              >
                {n}
              </button>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

const FREQUENZE: { id: FrequenzaAvvisi; titolo: string; testo: string }[] = [
  { id: "giornaliero", titolo: "Ogni giorno", testo: "Un'email al mattino quando escono nuovi bandi per te." },
  { id: "settimanale", titolo: "Ogni settimana", testo: "Un riepilogo il lunedì con tutti i bandi della settimana." },
  { id: "mai", titolo: "Nessun avviso", testo: "Controllerai tu i bandi nell'app." },
];

export function AvvisiPicker({ value, onChange }: { value: FrequenzaAvvisi; onChange: (v: FrequenzaAvvisi) => void }) {
  return (
    <div className="grid gap-3 sm:grid-cols-3" role="radiogroup">
      {FREQUENZE.map((f) => (
        <button
          key={f.id}
          type="button"
          role="radio"
          aria-checked={value === f.id}
          onClick={() => onChange(f.id)}
          className={cx(
            "rounded-2xl p-4 text-left ring-1 transition",
            value === f.id ? "bg-brand-50 ring-2 ring-brand-500" : "bg-white ring-slate-200 hover:ring-slate-300",
          )}
        >
          <p className="font-semibold text-slate-900">{f.titolo}</p>
          <p className="mt-1 text-sm text-slate-500">{f.testo}</p>
        </button>
      ))}
    </div>
  );
}
