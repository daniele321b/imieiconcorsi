import { Megaphone } from "lucide-react";
import { useApi, type AdminProvenienza } from "../lib/api";
import { dataOra } from "../lib/format";
import { Card, cx } from "./ui";

// Pannello admin: da dove arrivano gli iscritti (GET /admin/provenienza). Conta i profili creati
// arrivando da un link con i parametri UTM (social, annunci); gli altri sono "diretto".

const COLONNE = ["Fonte", "Mezzo", "Campagna", "Contenuto", "7 giorni", "30 giorni", "Totale"];

/** Card del pannello admin con gli iscritti per fonte, mezzo, campagna e contenuto. */
export function ProvenienzaIscritti() {
  const { data, error } = useApi<AdminProvenienza>("/admin/provenienza");

  return (
    <Card className="space-y-4">
      <div className="flex flex-wrap items-center gap-3">
        <Megaphone className="size-5 text-fuchsia-600" />
        <h2 className="text-lg font-bold text-slate-900">Provenienza iscritti</h2>
        {data && (
          <span className="ml-auto text-sm text-slate-500">
            Nuovi iscritti: <strong className="text-slate-900">{data.totali.ultimi7}</strong> in 7 giorni ·{" "}
            <strong className="text-slate-900">{data.totali.ultimi30}</strong> in 30 · {data.totali.totale} in tutto
          </span>
        )}
      </div>
      {error && <p className="text-sm text-rose-600">{error.message}</p>}

      {data && (
        <div className="overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead>
              <tr className="border-b border-slate-200 text-xs text-slate-500">
                {COLONNE.map((c, i) => (
                  <th key={c} className={cx("py-2 pr-4 font-semibold whitespace-nowrap", i >= 4 && "text-right")}>
                    {c}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.righe.map((r) => (
                <tr key={[r.fonte, r.mezzo, r.campagna, r.contenuto].join("|")} className="border-b border-slate-100 last:border-0">
                  <td className="py-2 pr-4 font-semibold text-slate-900">{r.fonte}</td>
                  <td className="py-2 pr-4 text-slate-600">{r.mezzo ?? "—"}</td>
                  <td className="py-2 pr-4 text-slate-600">{r.campagna ?? "—"}</td>
                  <td className="py-2 pr-4 text-slate-600">{r.contenuto ?? "—"}</td>
                  <td className="py-2 pr-4 text-right tabular-nums text-slate-900">{r.ultimi7}</td>
                  <td className="py-2 pr-4 text-right tabular-nums text-slate-900">{r.ultimi30}</td>
                  <td className="py-2 text-right tabular-nums text-slate-900">{r.totale}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <p className="text-xs text-slate-500">
        Dai parametri UTM del primo link aperto prima di iscriversi (es. ?utm_source=instagram&utm_campaign=bio). «diretto» =
        iscritti senza link UTM, compresi quelli arrivati prima che la provenienza venisse registrata. Chi elimina l'account
        esce dal conteggio.
        {data && ` Aggiornato alle ${dataOra(data.aggiornatoIl)}.`}
      </p>
    </Card>
  );
}
