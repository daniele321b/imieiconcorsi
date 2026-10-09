import { nomeTipoRichiesta, type StatoRichiesta } from "@imieiconcorsi/core/domain";
import { ArrowLeft, ChevronDown, Inbox } from "lucide-react";
import { useState } from "react";
import { Link, Navigate } from "react-router";
import { ContestoBox, Conversazione, RispondiBox, STATI_RICHIESTA, StatoRichiestaBadge } from "../../components/Richieste";
import { Alert, Button, Card, EmptyState, PageHeader, Spinner, cx } from "../../components/ui";
import { api, useApi, type RichiestaAdmin } from "../../lib/api";
import { messaggioErrore, useUtente } from "../../lib/auth";
import { dataOra } from "../../lib/format";

// Pannello admin: richieste di assistenza degli utenti, divise per stato. Rispondendo, l'utente
// riceve un'email e la richiesta passa "in lavorazione" (se non si sceglie un altro stato).

interface RispostaRichieste {
  conteggi: Record<StatoRichiesta, number>;
  richieste: RichiestaAdmin[];
}

/** Pagina /admin/richieste: chi non è admin torna all'app. */
export function AdminRichieste() {
  const { utente } = useUtente();
  if (!utente.admin) return <Navigate to="/app" replace />;
  return <Richieste />;
}

/** Richieste di uno stato (aperte, in lavorazione, chiuse), con i conteggi. */
function Richieste() {
  const [stato, setStato] = useState<StatoRichiesta>("aperta");
  const { data, error, loading, reload } = useApi<RispostaRichieste>(`/admin/richieste?stato=${stato}`);
  const [aperta, setAperta] = useState<string>();

  return (
    <div className="space-y-6">
      <Link to="/admin" className="inline-flex items-center gap-1 text-sm font-semibold text-slate-500 hover:text-slate-800">
        <ArrowLeft className="size-4" /> Pannello di controllo
      </Link>
      <PageHeader title="Richieste degli utenti" subtitle="Rispondi qui: l'utente riceve un'email e trova la risposta nella pagina Assistenza." />

      <div className="flex flex-wrap gap-2">
        {STATI_RICHIESTA.map((s) => (
          <button
            key={s.id}
            onClick={() => setStato(s.id)}
            className={cx(
              "rounded-full px-3 py-1.5 text-sm font-semibold transition",
              stato === s.id ? "bg-brand-600 text-white" : "bg-white text-slate-600 ring-1 ring-slate-200 hover:ring-slate-300",
            )}
          >
            {s.nome} <span className="opacity-70">({data?.conteggi[s.id] ?? "…"})</span>
          </button>
        ))}
      </div>

      {error && <Alert tone="error">{error.message}</Alert>}

      {loading && !data ? (
        <Spinner label="Carico le richieste…" />
      ) : !data?.richieste.length ? (
        <EmptyState icon={<Inbox className="size-6" />} title="Nessuna richiesta">
          Non ci sono richieste in questo stato.
        </EmptyState>
      ) : (
        <div className="space-y-3">
          {data.richieste.map((r) => {
            const chiave = `${r.userId}/${r.id}`;
            const ultimo = r.messaggi.at(-1)!;
            return (
              <Card key={chiave} className="p-0">
                <button onClick={() => setAperta(aperta === chiave ? undefined : chiave)} className="flex w-full items-start gap-3 p-4 text-left">
                  <div className="min-w-0 flex-1">
                    <div className="flex flex-wrap items-center gap-2">
                      <span className="font-semibold text-slate-900">{nomeTipoRichiesta(r.tipo)}</span>
                      <StatoRichiestaBadge stato={r.stato} />
                      <span className="text-sm text-slate-500">{r.email ?? "account eliminato"}</span>
                    </div>
                    <p className="mt-1 truncate text-sm text-slate-500">
                      {ultimo.da === "assistenza" ? "Tu: " : ""}
                      {ultimo.testo}
                    </p>
                    <p className="mt-1 text-xs text-slate-400">
                      Aperta il {dataOra(r.creataIl)} · aggiornata il {dataOra(r.aggiornataIl)} · {r.messaggi.length} messaggi
                    </p>
                  </div>
                  <ChevronDown className={cx("mt-1 size-4 shrink-0 text-slate-400 transition", aperta === chiave && "rotate-180")} />
                </button>
                {aperta === chiave && (
                  <div className="space-y-4 border-t border-slate-100 p-4">
                    <ContestoBox contesto={r.contesto} />
                    <Conversazione messaggi={r.messaggi} io="assistenza" />
                    <RispostaAdmin richiesta={r} onFatto={() => void reload()} />
                  </div>
                )}
              </Card>
            );
          })}
          {loading && <Spinner />}
        </div>
      )}
    </div>
  );
}

/** Risposta dell'admin con il nuovo stato, o chiusura senza risposta. */
function RispostaAdmin({ richiesta, onFatto }: { richiesta: RichiestaAdmin; onFatto: () => void }) {
  // Stato dopo la risposta: vuoto = automatico (una richiesta aperta passa "in lavorazione").
  const [stato, setStato] = useState<StatoRichiesta | "">("");
  const [cambio, setCambio] = useState(false);
  const [errore, setErrore] = useState<string>();
  const percorso = `/admin/richieste/${encodeURIComponent(richiesta.userId)}/${richiesta.id}`;

  async function invia(body: { testo?: string; stato?: StatoRichiesta }) {
    setErrore(undefined);
    try {
      await api(percorso, { method: "POST", body });
      onFatto();
      return true;
    } catch (err) {
      setErrore(messaggioErrore(err));
      return false;
    }
  }

  async function soloStato(nuovo: StatoRichiesta) {
    setCambio(true);
    await invia({ stato: nuovo });
    setCambio(false);
  }

  return (
    <div className="space-y-2">
      {errore && <Alert tone="error">{errore}</Alert>}
      <RispondiBox
        placeholder="Risposta all'utente (gli arriva anche per email)…"
        invia={(testo) => invia({ testo, ...(stato ? { stato } : {}) })}
        extra={
          <>
            <label className="text-xs font-semibold text-slate-500">
              Poi{" "}
              <select
                value={stato}
                onChange={(e) => setStato(e.target.value as StatoRichiesta | "")}
                className="ml-1 h-8 rounded-lg border-0 bg-white px-2 text-sm ring-1 ring-slate-300"
              >
                <option value="">{richiesta.stato === "aperta" ? "in lavorazione" : "stato invariato"}</option>
                {STATI_RICHIESTA.filter((s) => s.id !== richiesta.stato).map((s) => (
                  <option key={s.id} value={s.id}>
                    {s.nome.toLowerCase()}
                  </option>
                ))}
              </select>
            </label>
            {richiesta.stato !== "chiusa" && (
              <Button size="sm" variant="secondary" loading={cambio} onClick={() => void soloStato("chiusa")}>
                Chiudi senza rispondere
              </Button>
            )}
          </>
        }
      />
    </div>
  );
}
