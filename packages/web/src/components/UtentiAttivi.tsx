import { Activity } from "lucide-react";
import { useEffect } from "react";
import { useApi } from "../lib/api";
import { dataOra } from "../lib/format";
import { Card, cx } from "./ui";

// Pannello admin: utenti attivi (GET /admin/attivita). Online = utenti diversi che hanno usato
// l'app negli ultimi 5 minuti; il resto sono utenti diversi nel periodo. Admin esclusi. Si
// aggiorna da solo ogni minuto.

interface Attivita {
  online: number;
  oggi: number;
  ieri: number;
  settimana: number;
  trentaGiorni: number;
  meseCorrente: number;
  meseScorso: number;
  serie: { giorno: string; utenti: number }[];
  aggiornatoIl: string;
}

const giornoBreve = new Intl.DateTimeFormat("it-IT", { day: "numeric", month: "short", timeZone: "UTC" });

/** Card del pannello admin con gli utenti attivi oggi, nel mese e giorno per giorno (si aggiorna ogni minuto). */
export function UtentiAttivi() {
  const { data, error, reload } = useApi<Attivita>("/admin/attivita");
  useEffect(() => {
    const t = setInterval(() => void reload(), 60_000);
    return () => clearInterval(t);
  }, [reload]);
  const massimo = Math.max(1, ...(data?.serie.map((g) => g.utenti) ?? [1]));

  return (
    <Card className="space-y-4">
      <div className="flex flex-wrap items-center gap-3">
        <Activity className="size-5 text-emerald-600" />
        <h2 className="text-lg font-bold text-slate-900">Utenti attivi</h2>
        <span className="ml-auto inline-flex items-center gap-2 rounded-full bg-emerald-50 px-3 py-1 text-sm font-semibold text-emerald-800 ring-1 ring-emerald-200">
          <span className="relative flex size-2">
            <span className="absolute inline-flex size-full animate-ping rounded-full bg-emerald-400 opacity-75" />
            <span className="relative inline-flex size-2 rounded-full bg-emerald-500" />
          </span>
          {data ? data.online : "…"} online ora
        </span>
      </div>
      {error && <p className="text-sm text-rose-600">{error.message}</p>}

      <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
        {[
          { nome: "Oggi", valore: data?.oggi },
          { nome: "Ieri", valore: data?.ieri },
          { nome: "Ultimi 7 giorni", valore: data?.settimana },
          { nome: "Ultimi 30 giorni", valore: data?.trentaGiorni },
          { nome: "Questo mese", valore: data?.meseCorrente },
          { nome: "Mese scorso", valore: data?.meseScorso },
        ].map((v) => (
          <div key={v.nome} className="rounded-xl bg-slate-50 p-3">
            <p className="text-2xl font-extrabold text-slate-900">{v.valore ?? "…"}</p>
            <p className="text-xs text-slate-500">{v.nome}</p>
          </div>
        ))}
      </div>

      {/* Utenti attivi giorno per giorno, ultimi 30 giorni. */}
      {data && (
        <div>
          <div className="flex h-24 items-end gap-0.5" role="img" aria-label="Utenti attivi al giorno negli ultimi 30 giorni">
            {data.serie.map((g, i) => (
              <div
                key={g.giorno}
                title={`${giornoBreve.format(new Date(`${g.giorno}T00:00:00Z`))}: ${g.utenti}`}
                className={cx("min-h-0.5 flex-1 rounded-t", i === data.serie.length - 1 ? "bg-emerald-500" : "bg-brand-300")}
                style={{ height: `${(g.utenti / massimo) * 100}%` }}
              />
            ))}
          </div>
          <div className="mt-1 flex justify-between text-[11px] text-slate-400">
            <span>{data.serie[0] && giornoBreve.format(new Date(`${data.serie[0].giorno}T00:00:00Z`))}</span>
            <span>oggi</span>
          </div>
        </div>
      )}

      <p className="text-xs text-slate-500">
        Persone diverse che hanno usato l'app (ogni azione con l'accesso fatto), admin esclusi; online = negli ultimi 5 minuti.
        Giorni in ora italiana. I conteggi partono dal giorno in cui è attivo questo registro.
        {data && ` Aggiornato alle ${dataOra(data.aggiornatoIl)}, si aggiorna da solo ogni minuto.`}
      </p>
    </Card>
  );
}
