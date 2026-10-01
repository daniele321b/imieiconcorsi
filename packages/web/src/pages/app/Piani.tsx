import type { Periodo, PianoId } from "@imieiconcorsi/core/domain";
import { Check, Crown, Sparkles } from "lucide-react";
import { useState } from "react";
import { Alert, Badge, Button, PageHeader, Spinner, cx } from "../../components/ui";
import { api, useApi, type PianiApi } from "../../lib/api";
import { messaggioErrore, useAuth, useUtente } from "../../lib/auth";
import { data as dataLunga, euro } from "../../lib/format";

export function Piani() {
  const { utente } = useUtente();
  const { ricarica } = useAuth();
  const { data, loading, error, reload } = useApi<PianiApi>("/piani");
  const [periodo, setPeriodo] = useState<Periodo>(utente.periodo ?? "annuale");
  const [inCorso, setInCorso] = useState<PianoId>();
  const [esito, setEsito] = useState<{ tone: "success" | "error"; testo: string }>();

  async function scegli(piano: PianoId) {
    setInCorso(piano);
    setEsito(undefined);
    try {
      await api("/me/abbonamento", { method: "POST", body: { piano, periodo } });
      // Il piano è un gruppo Cognito: serve un token nuovo perché l'app lo veda.
      await ricarica({ rinnovaToken: true });
      await reload();
      setEsito({ tone: "success", testo: `Fatto! Ora hai il piano ${data?.piani.find((p) => p.id === piano)?.nome}.` });
    } catch (err) {
      setEsito({ tone: "error", testo: messaggioErrore(err) });
    } finally {
      setInCorso(undefined);
    }
  }

  if (loading) return <Spinner />;
  if (error || !data) return <Alert tone="error">{error?.message ?? "Piani non disponibili"}</Alert>;

  const medium = data.piani.find((p) => p.id === "medium")!;
  const sconto = Math.round((1 - medium.prezzo.annuale / (medium.prezzo.mensile * 12)) * 100);

  return (
    <div>
      <PageHeader
        title="Scegli il tuo piano"
        subtitle="Un solo pagamento per 30 o 365 giorni, senza rinnovo automatico. Ti avvisiamo 3 giorni prima della scadenza."
      />

      <div className="space-y-4">
        {utente.piano !== "free" && (
          <Alert tone="success">
            Hai il piano <strong>{data.piani.find((p) => p.id === utente.piano)?.nome}</strong>
            {data.scadenza ? <> fino al {dataLunga(data.scadenza)}.</> : <> senza scadenza.</>}
          </Alert>
        )}
        {data.modalita === "mock" && (
          <Alert tone="info">
            <strong>Beta:</strong> i pagamenti non sono ancora attivi. Il cambio di piano è immediato e gratuito, così puoi provare tutto.
          </Alert>
        )}
        {esito && (
          <Alert tone={esito.tone} onClose={() => setEsito(undefined)}>
            {esito.testo}
          </Alert>
        )}
      </div>

      <div className="mt-6 flex justify-center">
        <div className="inline-grid grid-cols-2 rounded-xl bg-white p-1 text-sm font-semibold ring-1 ring-slate-200" role="radiogroup">
          {(["mensile", "annuale"] as const).map((p) => (
            <button
              key={p}
              role="radio"
              aria-checked={periodo === p}
              onClick={() => setPeriodo(p)}
              className={cx("rounded-lg px-5 py-2 capitalize transition", periodo === p ? "bg-brand-600 text-white" : "text-slate-600")}
            >
              {p}
              {p === "annuale" && <span className={cx("ml-1.5 text-xs", periodo === p ? "text-accent-300" : "text-emerald-600")}>−{sconto}%</span>}
            </button>
          ))}
        </div>
      </div>

      <div className="mt-8 grid gap-6 lg:grid-cols-3">
        {data.piani.map((p) => {
          const attuale = utente.piano === p.id;
          const evidenziato = p.id === "medium";
          const prezzo = periodo === "mensile" ? p.prezzo.mensile : p.prezzo.annuale;
          return (
            <div
              key={p.id}
              className={cx(
                "relative flex flex-col rounded-3xl p-6 ring-1 sm:p-8",
                evidenziato ? "bg-brand-950 text-white shadow-2xl shadow-brand-900/30 ring-brand-800 lg:-translate-y-3" : "bg-white ring-slate-200",
              )}
            >
              {evidenziato && (
                <span className="absolute -top-3 left-1/2 -translate-x-1/2 rounded-full bg-accent-400 px-3 py-1 text-xs font-bold text-brand-950">
                  Il più scelto
                </span>
              )}
              <div className="flex items-center justify-between">
                <h2 className="flex items-center gap-2 text-xl font-extrabold">
                  {p.id === "pro" && <Sparkles className="size-5 text-fuchsia-500" />}
                  {p.id === "medium" && <Crown className="size-5 text-accent-300" />}
                  {p.nome}
                </h2>
                {attuale && <Badge tone={evidenziato ? "amber" : "brand"}>Il tuo piano</Badge>}
              </div>
              <p className={cx("mt-1 text-sm", evidenziato ? "text-brand-200" : "text-slate-500")}>{p.slogan}</p>

              <p className="mt-6">
                <span className="text-4xl font-extrabold tracking-tight">{prezzo ? euro(prezzo) : "Gratis"}</span>
                {prezzo > 0 && <span className={cx("text-sm", evidenziato ? "text-brand-200" : "text-slate-500")}> /{periodo === "mensile" ? "mese" : "anno"}</span>}
              </p>
              {prezzo > 0 && periodo === "annuale" && (
                <p className={cx("text-xs", evidenziato ? "text-brand-200" : "text-slate-500")}>pari a {euro(prezzo / 12)} al mese</p>
              )}

              <ul className="mt-6 flex-1 space-y-3 text-sm">
                {p.funzioni.map((f) => (
                  <li key={f} className="flex gap-2">
                    <Check className={cx("size-4 shrink-0", evidenziato ? "text-accent-300" : "text-brand-600")} /> {f}
                  </li>
                ))}
              </ul>

              <Button
                className="mt-8 w-full"
                size="lg"
                variant={evidenziato ? "accent" : attuale ? "secondary" : "primary"}
                disabled={attuale && (p.id === "free" || utente.periodo === periodo)}
                loading={inCorso === p.id}
                onClick={() => void scegli(p.id)}
              >
                {attuale && (p.id === "free" || utente.periodo === periodo)
                  ? "Piano attuale"
                  : attuale
                    ? `Passa all'abbonamento ${periodo}`
                    : p.id === "free"
                      ? "Torna a Free"
                      : `Scegli ${p.nome}`}
              </Button>
            </div>
          );
        })}
      </div>

      <p className="mt-8 text-center text-xs text-slate-400">Prezzi IVA inclusa. I prezzi definitivi saranno fissati al termine della beta.</p>
    </div>
  );
}
