import { conMaiuscola, nomeConcorso, scadenzaVera } from "@imieiconcorsi/core/concorsi";
import { MATERIE, nomeComparto } from "@imieiconcorsi/core/domain";
import { ArrowLeft, Bookmark, BookmarkCheck, BookOpenCheck, CalendarClock, Database, ExternalLink, Eye, Info, MapPin, ShieldCheck, Timer, Users } from "lucide-react";
import { useState } from "react";
import { ModificaBando } from "../../components/ModificaBando";
import { NumeroAMano } from "../../components/NumeroDomande";
import { Link, useParams } from "react-router";
import { IconaMateria } from "../../components/brand";
import { OrdineRisposte } from "../../components/OrdineRisposte";
import { Alert, Badge, Button, ButtonLink, Card, Spinner, UpgradeBanner, cx } from "../../components/ui";
import { api, ApiError, useApi, type ConcorsoApi } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { data, giorniA, scadenzaTesto, tipoProcedura } from "../../lib/format";
import { useAvviaSessione } from "../../lib/sessioni";
import { useSegui } from "./Concorsi";

// Dettaglio di un bando (/app/concorsi/:id): scadenza, posti, sedi, materie, link a inPA,
// Segui, studio e simulazione sulle materie del bando o sulla sua banca dati ufficiale.
// Per l'admin: "Segna come concluso".

/** Domande della simulazione tra cui scegliere. */
const LUNGHEZZE = [30, 50, 60];
/** Domande di una sessione di studio sulla banca dati. */
const STUDIO_BANCA = [10, 20, 30];

/** Da dove prendere le domande della simulazione: banca dati ufficiale o materie del bando. */
type Fonte = "banca" | "materie";

/** Pagina /app/concorsi/:id. */
export function ConcorsoDettaglio() {
  const { id } = useParams();
  const { utente } = useUtente();
  const { data: concorso, loading, error, setData } = useApi<ConcorsoApi>(`/concorsi/${id}`);
  const { segui, inCorso: seguiInCorso, errore: erroreSegui, chiudiErrore: chiudiSegui } = useSegui((_, seguito) =>
    setData((c) => c && { ...c, seguito }),
  );
  const { avvia, inCorso, errore, chiudiErrore } = useAvviaSessione();
  // undefined: numero scritto a mano non (ancora) valido.
  const [lunghezza, setLunghezza] = useState<number | undefined>(60);
  // Con la banca dati ufficiale i piani a pagamento scelgono da dove pescare le domande.
  const [fonte, setFonte] = useState<Fonte>("banca");
  const [studioBanca, setStudioBanca] = useState(STUDIO_BANCA[0]);

  if (loading) return <Spinner />;
  if (error || !concorso) return <Alert tone="error">{error?.message ?? "Concorso non trovato"}</Alert>;

  const giorni = giorniA(concorso.scadenza);
  const materie = MATERIE.filter((m) => concorso.materie.includes(m.id));
  const erroreMostrato = errore ?? erroreSegui;
  // Medium e Pro senza limiti; il Free con i suoi utilizzi settimanali (li controlla il server).
  const usiLimitati = utente.limiti.usiBancheDatiSettimana;
  const conBanca = !!concorso.bancaDatiId;
  const usaBanca = conBanca && fonte === "banca";

  return (
    <div className="space-y-6">
      <Link to="/app/concorsi" className="inline-flex items-center gap-1 text-sm font-semibold text-slate-500 hover:text-slate-800">
        <ArrowLeft className="size-4" /> Tutti i concorsi
      </Link>

      <header className="rounded-3xl bg-white p-6 shadow-sm ring-1 ring-slate-200/70 sm:p-8">
        <p className="text-sm font-semibold tracking-wide break-words text-brand-600 uppercase">{conMaiuscola(concorso.ente)}</p>
        <h1 className="mt-2 text-2xl font-extrabold tracking-tight break-words text-slate-900 sm:text-3xl">{nomeConcorso(concorso)}</h1>
        {concorso.figura && <p className="mt-2 break-words text-slate-500">{conMaiuscola(concorso.titolo)}</p>}
        <p className="mt-1 text-xs text-slate-400">
          Codice inPA <span className="font-mono">{concorso.id}</span>
          {concorso.pubblicatoIl && ` · pubblicato il ${data(concorso.pubblicatoIl)}`}
        </p>
        {giorni !== undefined && giorni < 0 && (
          <p className="mt-3 rounded-xl bg-amber-50 px-3 py-2 text-sm text-amber-900 ring-1 ring-amber-200">
            {concorso.conclusoIl
              ? "Concorso concluso."
              : `Le domande di partecipazione si sono chiuse il ${data(concorso.scadenza)}: se le hai inviate, continua pure a prepararti con studio e simulazioni.`}
          </p>
        )}

        <div className="mt-5 flex flex-wrap gap-2">
          <Badge tone={giorni !== undefined && giorni <= 7 ? "red" : "brand"}>
            <CalendarClock className="size-3" /> {scadenzaTesto(concorso.scadenza)}
            {scadenzaVera(concorso.scadenza) && ` · ${data(concorso.scadenza)}`}
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
        </div>

        {/* Solo admin: correzione di nome e dati del bando (restano anche dopo l'import da inPA). */}
        {utente.admin && <ModificaBando concorso={concorso} onSalvato={(c) => setData((x) => x && { ...c, seguito: x.seguito, bancaDatiTitolo: x.bancaDatiTitolo, bancaDatiDomande: x.bancaDatiDomande })} />}

        {/* Solo admin, solo bandi con le domande chiuse: quando il concorso è davvero finito
            (graduatoria uscita) lo si toglie anche dalla ricerca dei bandi chiusi. */}
        {utente.admin && giorni !== undefined && giorni < 0 && (
          <SegnaConcluso
            id={concorso.id}
            concluso={!!concorso.conclusoIl}
            onCambio={(conclusoIl) => setData((c) => c && { ...c, conclusoIl })}
          />
        )}
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
          {conBanca && (
            // Su telefono tutto in colonna: titolo e testo a tutta larghezza, poi i comandi.
            <Card className="space-y-4 p-4 ring-brand-200 sm:p-5">
              <div className="flex items-start gap-3">
                <span className="grid size-11 shrink-0 place-items-center rounded-xl bg-brand-50 text-brand-600">
                  <Database className="size-5" />
                </span>
                <div className="min-w-0 flex-1">
                  <p className="font-semibold">Banca dati ufficiale</p>
                  {concorso.bancaDatiTitolo && (
                    <p className="text-sm break-words text-slate-700">
                      {concorso.bancaDatiTitolo}
                      {!!concorso.bancaDatiDomande && <span className="text-slate-500"> · {concorso.bancaDatiDomande.toLocaleString("it-IT")} domande</span>}
                    </p>
                  )}
                  <p className="mt-1 text-xs text-slate-500">
                    Le domande pubblicate dall'ente, con la risposta giusta subito.
                    {usiLimitati !== null && ` Piano Free: ${usiLimitati} utilizzi a settimana.`}
                  </p>
                </div>
              </div>
              <OrdineRisposte />
              <div className="flex flex-wrap items-center justify-between gap-3">
                <ButtonLink to={`/app/banche-dati/${concorso.bancaDatiId}`} size="sm" variant="secondary">
                  <Eye className="size-4" /> Consulta domanda per domanda
                </ButtonLink>
                <div className="flex items-center gap-2">
                  <div className="inline-grid grid-cols-3 rounded-lg bg-slate-100 p-0.5 text-xs font-semibold">
                    {STUDIO_BANCA.map((n) => (
                      <button
                        key={n}
                        onClick={() => setStudioBanca(n)}
                        className={cx("rounded-md px-2.5 py-1 transition", studioBanca === n ? "bg-white text-brand-700 shadow-sm" : "text-slate-500")}
                      >
                        {n}
                      </button>
                    ))}
                  </div>
                  <Button
                    size="sm"
                    loading={inCorso === "banca-studio"}
                    onClick={() => void avvia({ tipo: "studio", bancaDatiId: concorso.bancaDatiId, concorsoId: concorso.id, numero: studioBanca }, "banca-studio")}
                  >
                    <BookOpenCheck className="size-4" /> Studia
                  </Button>
                </div>
              </div>
            </Card>
          )}

          {/* Banca dati prevista dal bando ma non ancora caricata: la frase del bando da cui lo capiamo. */}
          {!conBanca && concorso.bancaDatiPrevista && (
            <Card className="space-y-1 p-4 text-sm">
              <p className="flex items-center gap-2 font-semibold text-slate-900">
                <Database className="size-4 text-brand-600" /> Il bando prevede una banca dati di domande
              </p>
              {concorso.bancaDatiFrase && <p className="break-words text-slate-600 italic">«{concorso.bancaDatiFrase}»</p>}
              <p className="text-xs text-slate-500">
                Appena l'ente la pubblica la carichiamo qui. Lo deduciamo dal testo del bando su inPA: in caso di dubbio fa fede il bando.
              </p>
            </Card>
          )}

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
          {/* Un solo riquadro con una riga per materia: da telefono un riquadro per materia occupava troppo. */}
          <div className="divide-y divide-slate-100 rounded-2xl bg-white shadow-sm ring-1 ring-slate-200/70">
            {materie.map((m) => (
              <div key={m.id} className="flex items-center gap-3 px-4 py-2.5">
                <IconaMateria icona={m.icona} materia={m.id} piccola />
                <div className="min-w-0 flex-1">
                  <p className="text-sm font-semibold break-words text-slate-900">{m.nome}</p>
                  <p className="text-xs text-slate-500">Il tuo livello: {utente.livelli[m.id] ?? "—"}/5</p>
                </div>
                <Button
                  size="sm"
                  variant="ghost"
                  className="shrink-0 text-brand-600"
                  loading={inCorso === m.id}
                  onClick={() => void avvia({ tipo: "studio", materie: [m.id], concorsoId: concorso.id }, m.id)}
                >
                  Studia
                </Button>
              </div>
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
              {usaBanca
                ? "Domande della banca dati ufficiale del concorso, un minuto a domanda."
                : "Domande su tutte le materie del bando, un minuto a domanda."}{" "}
              Risposta giusta +1, sbagliata −0,25, non data 0.
            </p>
            {conBanca && (
              <div className="mt-4" role="radiogroup" aria-label="Da dove prendere le domande">
                <p className="text-xs font-semibold text-brand-200">Domande da</p>
                <div className="mt-1 grid grid-cols-2 gap-1 rounded-xl bg-white/10 p-1 text-xs font-semibold">
                  {(
                    [
                      ["banca", "Banca dati ufficiale"],
                      ["materie", "Materie del bando"],
                    ] as const
                  ).map(([id, nome]) => (
                    <button
                      key={id}
                      role="radio"
                      aria-checked={fonte === id}
                      onClick={() => setFonte(id)}
                      className={cx("rounded-lg px-2 py-1.5 transition", fonte === id ? "bg-white text-brand-900" : "text-brand-100 hover:bg-white/10")}
                    >
                      {nome}
                    </button>
                  ))}
                </div>
                {fonte === "banca" && (
                  <div className="mt-3">
                    <OrdineRisposte scuro />
                  </div>
                )}
                {usiLimitati !== null && fonte === "banca" && (
                  <p className="mt-2 text-xs text-brand-200">
                    Piano Free: {usiLimitati} utilizzi delle banche dati a settimana.{" "}
                    <Link to="/app/piani" className="font-semibold text-white underline">
                      Illimitati con Medium
                    </Link>
                  </p>
                )}
              </div>
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
            {/* Pro: quante domande vuole, fino a 100 (es. la prova vera ne ha 80). */}
            {utente.limiti.domandePerSimulazione > Math.max(...LUNGHEZZE) && (
              <div className="mt-3">
                <NumeroAMano valore={lunghezza} onChange={setLunghezza} max={utente.limiti.domandePerSimulazione} fissi={LUNGHEZZE} scuro />
              </div>
            )}
            <Button
              variant="accent"
              size="lg"
              className="mt-4 w-full"
              disabled={!lunghezza}
              loading={inCorso === "simulazione"}
              onClick={() =>
                void avvia({
                  tipo: "simulazione",
                  concorsoId: concorso.id,
                  numero: lunghezza,
                  // Banca dati scelta: esplicita (vale anche per il Free); materie esplicite = niente banca dati.
                  ...(usaBanca ? { bancaDatiId: concorso.bancaDatiId } : conBanca ? { materie: concorso.materie } : {}),
                })
              }
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
  // Segna il concorso come concluso, o lo riapre.
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
    <div className="mt-6 space-y-2 rounded-2xl bg-amber-50/60 p-4 text-sm ring-1 ring-amber-200">
      <p className="flex items-center gap-2 font-semibold text-amber-900">
        <ShieldCheck className="size-4" /> Solo per te (admin)
      </p>
      <p className="text-amber-900/80">
        {concluso
          ? "Questo concorso è segnato come concluso: non compare più tra i bandi chiusi della ricerca. Riaprilo se è stato un errore."
          : "Le domande sono chiuse ma il bando resta nella ricerca, perché chi l'ha fatta continua a prepararsi. Quando il concorso è davvero finito (graduatoria pubblicata), segnalo come concluso: sparisce dalla ricerca per tutti."}
      </p>
      <div className="flex flex-wrap items-center gap-2">
        <Button variant="secondary" size="sm" loading={inCorso} onClick={() => void cambia()}>
          {concluso ? "Riapri il concorso" : "Segna come concluso"}
        </Button>
        {errore && <span className="text-rose-600">{errore}</span>}
      </div>
    </div>
  );
}
