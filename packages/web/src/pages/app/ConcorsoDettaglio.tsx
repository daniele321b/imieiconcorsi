import { MATERIE, nomeComparto } from "@imieiconcorsi/core/domain";
import { ArrowLeft, Bookmark, BookmarkCheck, CalendarClock, ExternalLink, Info, MapPin, Timer, Users } from "lucide-react";
import { useState } from "react";
import { Link, useParams } from "react-router";
import { IconaMateria } from "../../components/brand";
import { Alert, Badge, Button, Card, Spinner, UpgradeBanner, cx } from "../../components/ui";
import { api, ApiError, useApi, type ConcorsoApi } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { data, giorniA, scadenzaTesto, tipoProcedura } from "../../lib/format";
import { useAvviaSessione } from "../../lib/sessioni";
import { useSegui } from "./Concorsi";

const LUNGHEZZE = [30, 50, 60];

export function ConcorsoDettaglio() {
  const { id } = useParams();
  const { utente } = useUtente();
  const { data: concorso, loading, error, setData } = useApi<ConcorsoApi>(`/concorsi/${id}`);
  const { segui, inCorso: seguiInCorso, errore: erroreSegui, chiudiErrore: chiudiSegui } = useSegui((_, seguito) =>
    setData((c) => c && { ...c, seguito }),
  );
  const { avvia, inCorso, errore, chiudiErrore } = useAvviaSessione();
  const [lunghezza, setLunghezza] = useState(60);

  if (loading) return <Spinner />;
  if (error || !concorso) return <Alert tone="error">{error?.message ?? "Concorso non trovato"}</Alert>;

  const giorni = giorniA(concorso.scadenza);
  const materie = MATERIE.filter((m) => concorso.materie.includes(m.id));
  const erroreMostrato = errore ?? erroreSegui;

  return (
    <div className="space-y-6">
      <Link to="/app/concorsi" className="inline-flex items-center gap-1 text-sm font-semibold text-slate-500 hover:text-slate-800">
        <ArrowLeft className="size-4" /> Tutti i concorsi
      </Link>

      <header className="rounded-3xl bg-white p-6 shadow-sm ring-1 ring-slate-200/70 sm:p-8">
        <p className="text-sm font-semibold tracking-wide text-brand-600 uppercase">{concorso.ente}</p>
        <h1 className="mt-2 text-2xl font-extrabold tracking-tight text-slate-900 sm:text-3xl">{concorso.figura ?? concorso.titolo}</h1>
        {concorso.figura && <p className="mt-2 text-slate-500">{concorso.titolo}</p>}
        {giorni !== undefined && giorni < 0 && (
          <p className="mt-3 rounded-xl bg-amber-50 px-3 py-2 text-sm text-amber-900 ring-1 ring-amber-200">
            {concorso.conclusoIl
              ? "Concorso concluso."
              : `Le domande di partecipazione si sono chiuse il ${data(concorso.scadenza)}: se le hai inviate, continua pure a prepararti con studio e simulazioni.`}
          </p>
        )}

        <div className="mt-5 flex flex-wrap gap-2">
          <Badge tone={giorni !== undefined && giorni <= 7 ? "red" : "brand"}>
            <CalendarClock className="size-3" /> {scadenzaTesto(concorso.scadenza)} · {data(concorso.scadenza)}
          </Badge>
          <Badge>{nomeComparto(concorso.comparto)}</Badge>
          {tipoProcedura(concorso.tipoProcedura) && <Badge>{tipoProcedura(concorso.tipoProcedura)}</Badge>}
          {concorso.sedi.length > 0 && (
            <Badge>
              <MapPin className="size-3" /> {concorso.sedi.join(", ")}
            </Badge>
          )}
          {concorso.posti ? (
            <Badge>
              <Users className="size-3" /> {concorso.posti} {concorso.posti === 1 ? "posto" : "posti"}
            </Badge>
          ) : null}
        </div>

        <div className="mt-6 flex flex-wrap gap-3">
          <Button variant={concorso.seguito ? "secondary" : "primary"} loading={seguiInCorso === concorso.id} onClick={() => void segui(concorso)}>
            {concorso.seguito ? <BookmarkCheck className="size-4" /> : <Bookmark className="size-4" />}
            {concorso.seguito ? "Lo stai seguendo" : "Segui questo concorso"}
          </Button>
          <a
            href={concorso.url}
            target="_blank"
            rel="noreferrer"
            className="inline-flex h-10 items-center gap-2 rounded-xl px-4 text-sm font-semibold text-slate-700 ring-1 ring-slate-200 hover:bg-slate-50"
          >
            Bando su inPA <ExternalLink className="size-4" />
          </a>
          {utente.admin && giorni !== undefined && giorni < 0 && (
            <SegnaConcluso
              id={concorso.id}
              concluso={!!concorso.conclusoIl}
              onCambio={(conclusoIl) => setData((c) => c && { ...c, conclusoIl })}
            />
          )}
        </div>
      </header>

      {erroreMostrato &&
        (erroreMostrato.code === "LIMITE_PIANO" ? (
          <UpgradeBanner
            message={erroreMostrato.message}
            onClose={() => {
              chiudiErrore();
              chiudiSegui();
            }}
          />
        ) : (
          <Alert
            tone="error"
            onClose={() => {
              chiudiErrore();
              chiudiSegui();
            }}
          >
            {erroreMostrato.message}
          </Alert>
        ))}

      <div className="grid gap-6 lg:grid-cols-[1.4fr_1fr]">
        <section className="space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-bold text-slate-900">Materie d'esame</h2>
            {concorso.materieStimate && <Badge tone="amber">Stimate dal comparto</Badge>}
          </div>
          {concorso.materieStimate && (
            <p className="flex gap-2 text-sm text-slate-500">
              <Info className="mt-0.5 size-4 shrink-0" />
              Le materie sono dedotte dal tipo di ente. Presto le leggeremo direttamente dal bando.
            </p>
          )}
          <div className="grid gap-3">
            {materie.map((m) => (
              <Card key={m.id} className="flex items-center gap-4 p-4">
                <IconaMateria icona={m.icona} materia={m.id} />
                <div className="flex-1">
                  <p className="font-semibold">{m.nome}</p>
                  <p className="text-xs text-slate-500">Il tuo livello: {utente.livelli[m.id] ?? "—"}/5</p>
                </div>
                <Button
                  size="sm"
                  variant="secondary"
                  loading={inCorso === m.id}
                  onClick={() => void avvia({ tipo: "studio", materie: [m.id], concorsoId: concorso.id }, m.id)}
                >
                  Studia
                </Button>
              </Card>
            ))}
          </div>

          {concorso.descrizione && (
            <Card>
              <p className="mb-2 font-semibold">Dal bando</p>
              <p className="text-sm leading-relaxed whitespace-pre-line text-slate-600">{concorso.descrizione}</p>
            </Card>
          )}
        </section>

        <aside>
          <Card className="sticky top-24 bg-gradient-to-br from-brand-950 to-brand-800 text-white ring-0">
            <Timer className="size-6 text-accent-300" />
            <h2 className="mt-3 text-lg font-bold">Simulazione d'esame</h2>
            <p className="mt-1 text-sm text-brand-100">
              {concorso.bancaDati && utente.limiti.bancheDati
                ? "Domande della banca dati ufficiale del concorso, un minuto a domanda."
                : "Domande su tutte le materie del bando, un minuto a domanda."}{" "}
              Risposta giusta +1, sbagliata −0,25, non data 0.
            </p>
            {concorso.bancaDati && (
              <p className="mt-3 rounded-xl bg-white/10 px-3 py-2 text-xs text-brand-100">
                {utente.limiti.bancheDati ? (
                  <>Banca dati ufficiale disponibile: la simulazione usa le domande ufficiali.</>
                ) : (
                  <>
                    È uscita la banca dati ufficiale: con <Link to="/app/piani" className="font-semibold text-white underline">Medium o Pro</Link> la
                    simulazione usa le domande ufficiali.
                  </>
                )}
              </p>
            )}
            <div className="mt-5 grid grid-cols-3 gap-2" role="radiogroup" aria-label="Numero di domande">
              {LUNGHEZZE.map((n) => (
                <button
                  key={n}
                  role="radio"
                  aria-checked={lunghezza === n}
                  onClick={() => setLunghezza(n)}
                  className={cx(
                    "rounded-xl py-2.5 text-sm font-bold transition",
                    lunghezza === n ? "bg-white text-brand-900" : "bg-white/10 text-white hover:bg-white/20",
                  )}
                >
                  {n} domande
                </button>
              ))}
            </div>
            <Button
              variant="accent"
              size="lg"
              className="mt-4 w-full"
              loading={inCorso === "simulazione"}
              onClick={() => void avvia({ tipo: "simulazione", concorsoId: concorso.id, numero: lunghezza })}
            >
              Inizia la simulazione
            </Button>
            {utente.limiti.simulazioniSettimana !== null && (
              <p className="mt-3 text-center text-xs text-brand-200">
                Piano Free: {utente.limiti.simulazioniSettimana} simulazione a settimana
              </p>
            )}
          </Card>
        </aside>
      </div>
    </div>
  );
}

/** Admin: il concorso è finito e non compare più nemmeno tra i bandi con le domande chiuse. */
function SegnaConcluso({ id, concluso, onCambio }: { id: string; concluso: boolean; onCambio: (conclusoIl?: string) => void }) {
  const [inCorso, setInCorso] = useState(false);
  const [errore, setErrore] = useState<string>();
  async function cambia() {
    setInCorso(true);
    setErrore(undefined);
    try {
      await api(`/admin/concorsi/${encodeURIComponent(id)}/concluso`, { method: "PUT", body: { concluso: !concluso } });
      onCambio(concluso ? undefined : new Date().toISOString());
    } catch (err) {
      setErrore(err instanceof ApiError ? err.message : "Errore di rete");
    } finally {
      setInCorso(false);
    }
  }
  return (
    <span className="inline-flex items-center gap-2">
      <Button variant="ghost" loading={inCorso} onClick={() => void cambia()}>
        {concluso ? "Admin: riapri il concorso" : "Admin: segna come concluso"}
      </Button>
      {errore && <span className="text-sm text-rose-600">{errore}</span>}
    </span>
  );
}
