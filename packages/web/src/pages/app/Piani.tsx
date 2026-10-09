import { PREZZI_DI_PROVA, type Periodo, type PianoId } from "@imieiconcorsi/core/domain";
import { prezzoScontato } from "@imieiconcorsi/core/sconti";
import { Check, Crown, Sparkles, Tag, X } from "lucide-react";
import { useState } from "react";
import { Link, Navigate } from "react-router";
import { Alert, Badge, Button, PageHeader, Spinner, cx } from "../../components/ui";
import { api, useApi, type CodiceScontoApi, type PianiApi } from "../../lib/api";
import { messaggioErrore, useAuth, useUtente } from "../../lib/auth";
import { data as dataLunga, euro } from "../../lib/format";

export function Piani() {
  const { utente } = useUtente();
  // L'admin ha già tutto: niente piani da comprare.
  if (utente.admin) return <Navigate to="/app" replace />;
  return <SceltaPiano />;
}

function SceltaPiano() {
  const { utente } = useUtente();
  const { ricarica } = useAuth();
  const { data, loading, error, reload } = useApi<PianiApi>("/piani");
  const [periodo, setPeriodo] = useState<Periodo>("mensile");
  const [inCorso, setInCorso] = useState<PianoId>();
  const [rinunciaRecesso, setRinunciaRecesso] = useState(false);
  const [esito, setEsito] = useState<{ tone: "success" | "error"; testo: string }>();
  const [codice, setCodice] = useState("");
  const [sconto, setSconto] = useState<CodiceScontoApi>();
  const [verifica, setVerifica] = useState<{ inCorso: boolean; errore?: string }>({ inCorso: false });

  const scontoSu = (piano: PianoId) => (sconto && piano !== "free" && sconto.piani.includes(piano) ? sconto : undefined);

  async function applicaCodice() {
    setVerifica({ inCorso: true });
    try {
      setSconto(await api<CodiceScontoApi>("/me/codice-sconto", { method: "POST", body: { codice } }));
      setVerifica({ inCorso: false });
    } catch (err) {
      setSconto(undefined);
      setVerifica({ inCorso: false, errore: messaggioErrore(err) });
    }
  }

  async function scegli(piano: PianoId) {
    setInCorso(piano);
    setEsito(undefined);
    try {
      const res = await api<{ pagamento?: string }>("/me/abbonamento", {
        method: "POST",
        body: {
          piano,
          periodo,
          ...(piano !== "free" ? { rinunciaRecesso: true } : {}),
          ...(scontoSu(piano) ? { codice: sconto!.codice } : {}),
        },
      });
      // Con Stripe si va alla sua pagina di pagamento; si torna su /app/pagamento.
      if (res.pagamento) {
        window.location.assign(res.pagamento);
        return;
      }
      setRinunciaRecesso(false);
      setSconto(undefined);
      setCodice("");
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
  const scontoAnnuale = Math.round((1 - medium.prezzo.annuale / (medium.prezzo.mensile * 12)) * 100);

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
        {data.modalita === "stripe" && PREZZI_DI_PROVA && (
          <Alert tone="info">
            <strong>Prezzi di prova:</strong> ogni piano costa 0,50 € per provare i pagamenti con Stripe (in modalità test non
            viene addebitato nulla: usa la carta 4242 4242 4242 4242).
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
              {p === "annuale" && scontoAnnuale > 0 && !PREZZI_DI_PROVA && <span className={cx("ml-1.5 text-xs", periodo === p ? "text-accent-300" : "text-emerald-600")}>−{scontoAnnuale}%</span>}
            </button>
          ))}
        </div>
      </div>

      <div className="mx-auto mt-6 max-w-2xl rounded-2xl bg-white p-4 ring-1 ring-slate-200">
        {sconto ? (
          <div className="flex items-center justify-between gap-3 text-sm">
            <p className="flex items-center gap-2 text-emerald-700">
              <Tag className="size-4" />
              Codice <strong>{sconto.codice}</strong>: sconto del {sconto.percentuale}%
              {sconto.piani.length < 2 && <> sul piano {sconto.piani[0] === "pro" ? "Pro" : "Medium"}</>}
            </p>
            <button onClick={() => setSconto(undefined)} className="text-slate-400 hover:text-slate-700" aria-label="Rimuovi il codice">
              <X className="size-4" />
            </button>
          </div>
        ) : null}
        {sconto && (
          <p className="mt-2 text-xs text-amber-700">
            Il codice si usa con il prossimo acquisto e poi non vale più per il tuo account. Rimuovilo se vuoi tenerlo per dopo.
          </p>
        )}
        {!sconto && (
          <form
            className="flex flex-col gap-2 sm:flex-row sm:items-center"
            onSubmit={(e) => {
              e.preventDefault();
              void applicaCodice();
            }}
          >
            <label className="flex flex-1 items-center gap-2 text-sm text-slate-600">
              <Tag className="size-4 shrink-0 text-slate-400" />
              <span className="sr-only">Codice sconto</span>
              <input
                value={codice}
                onChange={(e) => setCodice(e.target.value.toUpperCase())}
                placeholder="Hai un codice sconto?"
                className="h-10 w-full rounded-xl border-0 bg-white px-3 font-mono uppercase ring-1 ring-slate-300 placeholder:font-sans placeholder:normal-case focus:ring-2 focus:ring-brand-500 focus:outline-none"
              />
            </label>
            <Button type="submit" variant="secondary" disabled={!codice.trim()} loading={verifica.inCorso}>
              Applica
            </Button>
          </form>
        )}
        {!sconto && <p className="mt-2 text-xs text-slate-500">Ogni codice sconto vale una sola volta per account.</p>}
        {verifica.errore && <p className="mt-2 text-sm text-rose-600">{verifica.errore}</p>}
      </div>

      <label className="mx-auto mt-4 flex max-w-2xl items-start gap-3 rounded-2xl bg-white p-4 text-sm text-slate-600 ring-1 ring-slate-200">
        <input
          type="checkbox"
          checked={rinunciaRecesso}
          onChange={(e) => setRinunciaRecesso(e.target.checked)}
          className="mt-0.5 size-4 shrink-0 rounded border-slate-300 text-brand-600 focus:ring-brand-500"
        />
        <span>
          Voglio accedere subito al piano e prendo atto che, per questo, <strong>perdo il diritto di recesso</strong> (art. 59,
          lett. o, Codice del consumo). Il pagamento è unico, <strong>non si rinnova</strong> e{" "}
          <strong>non è rimborsabile</strong>, come previsto dai{" "}
          <Link to="/termini" target="_blank" className="font-semibold text-brand-600 underline">
            Termini
          </Link>
          .
        </span>
      </label>

      <div className="mt-8 grid gap-6 lg:grid-cols-3">
        {data.piani.map((p) => {
          const attuale = utente.piano === p.id;
          const evidenziato = p.id === "medium";
          const pieno = periodo === "mensile" ? p.prezzo.mensile : p.prezzo.annuale;
          const scontoPiano = scontoSu(p.id);
          const prezzo = scontoPiano ? prezzoScontato(pieno, scontoPiano.percentuale) : pieno;
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
                {scontoPiano && (
                  <span className={cx("mr-2 text-lg line-through", evidenziato ? "text-brand-300" : "text-slate-400")}>{euro(pieno)}</span>
                )}
                <span className="text-4xl font-extrabold tracking-tight">{prezzo ? euro(prezzo) : p.id === "free" ? "Gratis" : euro(0)}</span>
                {pieno > 0 && <span className={cx("text-sm", evidenziato ? "text-brand-200" : "text-slate-500")}> /{periodo === "mensile" ? "mese" : "anno"}</span>}
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
                disabled={(attuale && (p.id === "free" || utente.periodo === periodo)) || (p.id !== "free" && !rinunciaRecesso)}
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
