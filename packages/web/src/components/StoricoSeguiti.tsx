import { ChevronDown, History } from "lucide-react";
import { useState } from "react";
import { Link } from "react-router";
import { api } from "../lib/api";
import { data } from "../lib/format";
import { cx } from "./ui";

interface VoceStorico {
  concorsoId: string;
  titolo: string;
  dal: string;
  seguito: boolean;
}

/** Storico dei concorsi seguiti: chiuso finché non lo apri, poi solo nome e giorno. */
export function StoricoSeguiti() {
  const [aperto, setAperto] = useState(false);
  const [voci, setVoci] = useState<VoceStorico[]>();
  const [errore, setErrore] = useState<string>();

  async function apri() {
    setAperto((a) => !a);
    if (voci) return;
    try {
      setVoci((await api<{ storico: VoceStorico[] }>("/me/storico-concorsi")).storico);
    } catch {
      setErrore("Storico non disponibile, riprova più tardi.");
    }
  }

  return (
    <section className="rounded-2xl bg-white ring-1 ring-slate-200">
      <button onClick={() => void apri()} aria-expanded={aperto} className="flex w-full items-center gap-2 p-4 text-left text-sm font-semibold text-slate-700">
        <History className="size-4 text-slate-400" />
        Storico dei concorsi seguiti
        <ChevronDown className={cx("ml-auto size-4 text-slate-400 transition", aperto && "rotate-180")} />
      </button>
      {aperto && (
        <div className="border-t border-slate-100 px-4 py-3 text-sm">
          {errore ? (
            <p className="text-rose-600">{errore}</p>
          ) : !voci ? (
            <p className="text-slate-400">Carico…</p>
          ) : !voci.length ? (
            <p className="text-slate-500">Non hai ancora seguito nessun concorso.</p>
          ) : (
            <ul className="max-h-72 divide-y divide-slate-100 overflow-y-auto">
              {voci.map((v) => (
                <li key={v.concorsoId} className="flex items-baseline justify-between gap-3 py-2">
                  <Link to={`/app/concorsi/${v.concorsoId}`} className="min-w-0 truncate text-slate-800 hover:text-brand-700">
                    {v.titolo}
                  </Link>
                  <span className="shrink-0 text-xs text-slate-500">{data(v.dal)}</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </section>
  );
}
