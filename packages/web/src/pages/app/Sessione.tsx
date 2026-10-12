import { DOMANDE_TRA_ANNUNCI, nomeMateria, PREFISSO_BANCA_DATI } from "@imieiconcorsi/core/domain";
import { numeroDomanda } from "@imieiconcorsi/core/progressi";
import { ArrowLeft, ArrowRight, CheckCircle2, ChevronDown, Flag, RotateCcw, Timer, Trophy, X, XCircle } from "lucide-react";
import { useCallback, useEffect, useRef, useState } from "react";
import { Link, useLocation, useNavigate, useParams } from "react-router";
import { Pubblicita } from "../../components/Pubblicita";
import { ChiediAlTutor } from "../../components/ChiediAlTutor";
import { SegnalaErrore } from "../../components/Richieste";
import { StellaPreferita } from "../../components/StellaPreferita";
import { Alert, Badge, Button, ButtonLink, Card, ProgressBar, Spinner, cx } from "../../components/ui";
import { api, ApiError, haSoluzione, useApi, type ContestoRichiesta, type SessioneApi } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { durata } from "../../lib/format";

// Pagina di una sessione (/app/sessione/:id): studio con correzione subito, simulazione a tempo
// e, dopo la consegna, i risultati con la revisione delle risposte. Il punteggio lo calcola il
// server (POST /sessioni/{id}/consegna); qui si raccolgono solo le risposte.

/** Risposte date, nell'ordine delle domande (null = non risposta). */
type Risposte = (number | null)[];

/** Stella "preferita" sulle domande delle banche dati ufficiali (le altre non ce l'hanno). */
function StellaSessione({ sessione, domanda }: { sessione: SessioneApi; domanda: SessioneApi["domande"][number] }) {
  if (!sessione.bancaDati || domanda.materia !== `${PREFISSO_BANCA_DATI}${sessione.bancaDati.id}`) return null;
  return <StellaPreferita conTesto bancaId={sessione.bancaDati.id} numero={numeroDomanda(domanda.id)} preferita={!!domanda.preferita} />;
}

/** Per "Segnala un errore": quale domanda, e di quale banca dati o concorso. */
function contestoDomanda(sessione: SessioneApi, d: { materia: string; id: string; testo: string }): ContestoRichiesta {
  return {
    domanda: { materia: d.materia, id: d.id, testo: d.testo.slice(0, 1500) },
    ...(sessione.bancaDati ? { bancaDatiId: sessione.bancaDati.id } : {}),
    ...(sessione.concorsoId ? { concorsoId: sessione.concorsoId } : {}),
  };
}

/** Le domande ufficiali hanno le risposte in ordine diverso dal PDF: lo si dice, o sembra un errore. */
function NotaOrdineRisposte({ sessione }: { sessione: SessioneApi }) {
  if (!sessione.bancaDati?.mescolate) return null;
  return (
    <p className="mb-4 rounded-xl bg-slate-100 px-3 py-2 text-xs text-slate-600">
      Le risposte sono in ordine diverso dal PDF ufficiale: così impari la risposta giusta e non la sua lettera.
    </p>
  );
}

/** Pagina /app/sessione/:id: carica la sessione e mostra studio, simulazione o risultati. */
export function SessionePage() {
  const { id } = useParams();
  // key: passando da una sessione all'altra lo stato riparte da zero.
  return <Sessione key={id} id={id!} />;
}

/** La sessione: dati arrivati dalla pagina precedente o richiesti al server. */
function Sessione({ id }: { id: string }) {
  const { state } = useLocation();
  const appenaCreata = (state as SessioneApi | null)?.id === id ? (state as SessioneApi) : undefined;
  // Se arriviamo dalla creazione abbiamo già i dati; altrimenti (ricarica, link) li chiediamo al server.
  const remota = useApi<SessioneApi>(appenaCreata ? null : `/sessioni/${id}`);
  const [sessione, setSessione] = useState<SessioneApi | undefined>(appenaCreata);

  useEffect(() => {
    if (remota.data) setSessione(remota.data);
  }, [remota.data]);

  if (remota.loading) return <Spinner />;
  if (remota.error) return <Alert tone="error">{remota.error.message}</Alert>;
  if (!sessione) return <Spinner />;

  if (sessione.stato === "consegnata") return <Risultati sessione={sessione} />;
  return sessione.tipo === "studio" ? (
    <StudioRunner sessione={sessione} onConsegnata={setSessione} />
  ) : (
    <SimulazioneRunner sessione={sessione} onConsegnata={setSessione} />
  );
}

/** Consegna delle risposte al server, che calcola il punteggio. */
function useConsegna(sessione: SessioneApi, onConsegnata: (s: SessioneApi) => void) {
  const [inCorso, setInCorso] = useState(false);
  const [errore, setErrore] = useState<string>();
  const consegna = useCallback(
    async (risposte: Risposte) => {
      setInCorso(true);
      setErrore(undefined);
      try {
        onConsegnata(await api<SessioneApi>(`/sessioni/${sessione.id}/consegna`, { method: "POST", body: { risposte } }));
        try {
          localStorage.removeItem(chiaveBozza(sessione.id));
        } catch {}
      } catch (err) {
        setErrore(err instanceof ApiError ? err.message : "Consegna non riuscita: riprova.");
      } finally {
        setInCorso(false);
      }
    },
    [sessione.id, onConsegnata],
  );
  return { consegna, inCorso, errore };
}

// ── Cronometro ───────────────────────────────────────────────────────────────

/** Millisecondi trascorsi da `inizio`, aggiornati ogni secondo. */
function useTrascorso(inizio: string) {
  const [ora, setOra] = useState(() => Date.now());
  useEffect(() => {
    const t = setInterval(() => setOra(Date.now()), 1000);
    return () => clearInterval(t);
  }, []);
  return Math.max(0, ora - Date.parse(inizio));
}

/**
 * Cronometro della prova d'esame: tempo rimasto in grande, tempo trascorso, barra del tempo e
 * ritmo (risposte date rispetto al tempo passato: con un minuto a domanda si vede subito se si
 * è indietro). Rosso e lampeggiante negli ultimi 5 minuti.
 */
function CronometroProva({ inizio, fine, date, totale }: { inizio: string; fine: string; date: number; totale: number }) {
  const trascorso = useTrascorso(inizio);
  const durataTotale = Date.parse(fine) - Date.parse(inizio);
  const rimanente = Math.max(0, durataTotale - trascorso);
  const quota = Math.min(1, trascorso / durataTotale);
  const pocoTempo = rimanente < 5 * 60_000;
  // Domande che "dovresti" aver fatto a questo punto, con il tempo diviso in parti uguali.
  const attese = Math.floor(quota * totale);
  const ritmo = date >= attese ? "in linea" : `${attese - date} ${attese - date === 1 ? "domanda" : "domande"} indietro`;
  return (
    <div className="flex flex-col items-end gap-1">
      <span
        className={cx(
          "inline-flex items-center gap-1.5 rounded-full px-3 py-1 font-mono text-base font-bold tabular-nums",
          pocoTempo ? "animate-pulse bg-rose-100 text-rose-700" : "bg-brand-950 text-white",
        )}
        role="timer"
        aria-label={`Tempo rimasto ${durata(rimanente)}`}
      >
        <Timer className="size-4" /> {durata(rimanente)}
      </span>
      <span className="text-[11px] font-medium text-slate-500 tabular-nums">
        trascorsi {durata(trascorso)} · ritmo {ritmo}
      </span>
      <span className="block h-1 w-28 overflow-hidden rounded-full bg-slate-200" aria-hidden>
        <span className={cx("block h-full rounded-full", pocoTempo ? "bg-rose-500" : "bg-brand-500")} style={{ width: `${quota * 100}%` }} />
      </span>
    </div>
  );
}

/** Cronometro dello studio: solo il tempo trascorso, senza limite. */
function CronometroStudio({ inizio }: { inizio: string }) {
  const trascorso = useTrascorso(inizio);
  return (
    <span className="inline-flex items-center gap-1 font-mono text-xs font-semibold text-slate-500 tabular-nums" role="timer" aria-label={`Tempo trascorso ${durata(trascorso)}`}>
      <Timer className="size-3.5" /> {durata(trascorso)}
    </span>
  );
}

// ── Studio: una domanda alla volta con correzione immediata ──────────────────

/** Studio: una domanda alla volta, con la risposta giusta e la spiegazione subito dopo. */
function StudioRunner({ sessione, onConsegnata }: { sessione: SessioneApi; onConsegnata: (s: SessioneApi) => void }) {
  const { utente } = useUtente();
  const [indice, setIndice] = useState(0);
  const [risposte, setRisposte] = useState<Risposte>(() => sessione.domande.map(() => null));
  const [annuncio, setAnnuncio] = useState(false);
  const { consegna, inCorso, errore } = useConsegna(sessione, onConsegnata);
  const [interrompi, setInterrompi] = useState(false);
  const [uscita, setUscita] = useState(false);
  const navigate = useNavigate();
  const { key } = useLocation();

  /**
   * Interrompi ed esci: le risposte date finora si consegnano (contano nei progressi e nelle
   * statistiche, le domande non fatte no), poi si torna alla pagina di prima.
   */
  async function esci() {
    setUscita(true);
    try {
      if (risposte.some((r) => r !== null)) {
        await api(`/sessioni/${sessione.id}/consegna`, { method: "POST", body: { risposte } });
      }
    } catch {
      // Anche se il salvataggio non riesce si esce: la sessione resta "in corso" e basta.
    }
    // Pagina aperta direttamente (nessuna pagina prima nell'app): si va allo studio.
    if (key === "default") navigate("/app/studio", { replace: true });
    else navigate(-1);
  }

  // Piano Free: un annuncio dopo ogni 5 domande (mai prima del risultato finale).
  const avanti = () => {
    // L'annuncio solo andando verso domande nuove, non ripassando quelle già fatte.
    if (utente.limiti.pubblicita && (indice + 1) % DOMANDE_TRA_ANNUNCI === 0 && risposte[indice + 1] === null) setAnnuncio(true);
    else setIndice((i) => i + 1);
  };

  const domanda = sessione.domande[indice];
  const scelta = risposte[indice];
  const rivelata = scelta !== null;
  const ultima = indice === sessione.domande.length - 1;
  const giuste = risposte.filter((r, i) => {
    const d = sessione.domande[i];
    return r !== null && haSoluzione(d) && r === d.corretta;
  }).length;

  return (
    <div className="mx-auto max-w-2xl">
      <div className="mb-6 flex items-center justify-between gap-4">
        <div>
          <p className="text-sm font-semibold text-brand-600">{sessione.bancaDati?.titolo ?? sessione.materie.map(nomeMateria).join(", ")}</p>
          <p className="flex items-center gap-3 text-sm text-slate-500">
            Domanda {indice + 1} di {sessione.domande.length} <CronometroStudio inizio={sessione.creataIl} />
          </p>
        </div>
        <div className="flex shrink-0 items-center gap-2">
          <Badge tone="green">
            <CheckCircle2 className="size-3" /> {giuste} giuste
          </Badge>
          <Button variant="secondary" size="sm" onClick={() => setInterrompi(true)} aria-label="Interrompi e esci">
            <X className="size-4" /> Esci
          </Button>
        </div>
      </div>
      {interrompi && (
        <Card className="mb-6 space-y-3 ring-amber-300">
          <p className="font-semibold text-slate-900">Vuoi interrompere lo studio?</p>
          <p className="text-sm text-slate-600">
            {risposte.some((r) => r !== null)
              ? `Le ${risposte.filter((r) => r !== null).length} risposte date finora restano nei tuoi progressi e nelle statistiche; le domande che non hai fatto non contano.`
              : "Non hai ancora risposto a nessuna domanda: non viene salvato nulla."}
          </p>
          <div className="flex flex-wrap gap-2">
            <Button variant="secondary" size="sm" disabled={uscita} onClick={() => setInterrompi(false)}>
              Continua a studiare
            </Button>
            <Button size="sm" loading={uscita} onClick={() => void esci()}>
              Interrompi ed esci
            </Button>
          </div>
        </Card>
      )}
      <ProgressBar value={((indice + (rivelata ? 1 : 0)) / sessione.domande.length) * 100} className="mb-6" />
      <NotaOrdineRisposte sessione={sessione} />

      {annuncio ? (
        <Pubblicita
          onContinua={() => {
            setAnnuncio(false);
            setIndice((i) => i + 1);
          }}
        />
      ) : (
      <Card key={indice} className="animate-fade-up p-6 sm:p-8">
        <p className="text-xs font-semibold tracking-wide text-slate-400 uppercase">{domanda.argomento}</p>
        <h2 className="mt-2 text-xl font-bold text-slate-900">{domanda.testo}</h2>

        <div className="mt-6 grid gap-3">
          {domanda.opzioni.map((opzione, i) => {
            const corretta = haSoluzione(domanda) && i === domanda.corretta;
            const sbagliata = rivelata && i === scelta && !corretta;
            return (
              <button
                key={i}
                disabled={rivelata}
                onClick={() => setRisposte((r) => r.map((v, j) => (j === indice ? i : v)))}
                className={cx(
                  "flex items-center gap-3 rounded-xl p-4 text-left font-medium ring-1 transition",
                  !rivelata && "ring-slate-200 hover:bg-brand-50 hover:ring-brand-300",
                  rivelata && corretta && "bg-emerald-50 text-emerald-900 ring-2 ring-emerald-500",
                  sbagliata && "bg-rose-50 text-rose-900 ring-2 ring-rose-400",
                  rivelata && !corretta && !sbagliata && "opacity-50 ring-slate-200",
                )}
              >
                <span className="grid size-7 shrink-0 place-items-center rounded-lg bg-slate-100 text-sm font-bold text-slate-600">
                  {String.fromCharCode(65 + i)}
                </span>
                <span className="flex-1">{opzione}</span>
                {rivelata && corretta && <CheckCircle2 className="size-5 text-emerald-600" />}
                {sbagliata && <XCircle className="size-5 text-rose-500" />}
              </button>
            );
          })}
        </div>

        {rivelata && haSoluzione(domanda) && (
          <div className="mt-6 animate-fade-up rounded-xl bg-slate-50 p-4 text-sm">
            <p className="font-semibold text-slate-900">{scelta === domanda.corretta ? "Esatto!" : "Non proprio."}</p>
            <p className="mt-1 text-slate-600">{domanda.spiegazione}</p>
            <ChiediAlTutor domanda={domanda} risposta={scelta} />
            <div className="mt-3 flex flex-wrap items-center gap-3">
              <StellaSessione sessione={sessione} domanda={domanda} />
              <SegnalaErrore contesto={contestoDomanda(sessione, domanda)} />
            </div>
          </div>
        )}
      </Card>
      )}

      {errore && (
        <div className="mt-4">
          <Alert tone="error">{errore}</Alert>
        </div>
      )}

      {/* Precedente: si rivede una domanda già fatta, con la risposta data (non si cambia). */}
      <div className={cx("mt-6 flex items-center justify-between gap-3", annuncio && "hidden")}>
        <Button size="lg" variant="secondary" disabled={indice === 0} onClick={() => setIndice((i) => i - 1)}>
          <ArrowLeft className="size-4" /> Precedente
        </Button>
        {ultima ? (
          <Button size="lg" disabled={!rivelata} loading={inCorso} onClick={() => void consegna(risposte)}>
            Vedi il risultato <ArrowRight className="size-4" />
          </Button>
        ) : (
          <Button size="lg" disabled={!rivelata} onClick={avanti}>
            Prossima domanda <ArrowRight className="size-4" />
          </Button>
        )}
      </div>
    </div>
  );
}

// ── Simulazione: timer, navigazione libera, consegna finale ──────────────────

const chiaveBozza = (id: string) => `simulazione:${id}`;

/** Risposte della simulazione salvate nel browser: ricaricando la pagina non si perdono. */
function leggiBozza(id: string, n: number): Risposte {
  try {
    const salvate = JSON.parse(localStorage.getItem(chiaveBozza(id)) ?? "null");
    if (Array.isArray(salvate) && salvate.length === n) return salvate;
  } catch {}
  return Array.from({ length: n }, () => null);
}

/** Simulazione: timer, salto tra le domande, consegna (automatica allo scadere del tempo). */
function SimulazioneRunner({ sessione, onConsegnata }: { sessione: SessioneApi; onConsegnata: (s: SessioneApi) => void }) {
  const [indice, setIndice] = useState(0);
  const [risposte, setRisposte] = useState<Risposte>(() => leggiBozza(sessione.id, sessione.domande.length));
  const [rimanente, setRimanente] = useState(() => Date.parse(sessione.scadeIl!) - Date.now());
  const [conferma, setConferma] = useState(false);
  const { consegna, inCorso, errore } = useConsegna(sessione, onConsegnata);
  const consegnata = useRef(false);

  // Bozza nel browser: una ricarica della pagina non fa perdere le risposte.
  useEffect(() => {
    try {
      localStorage.setItem(chiaveBozza(sessione.id), JSON.stringify(risposte));
    } catch {}
  }, [sessione.id, risposte]);

  useEffect(() => {
    const t = setInterval(() => setRimanente(Date.parse(sessione.scadeIl!) - Date.now()), 1000);
    return () => clearInterval(t);
  }, [sessione.scadeIl]);

  // Tempo scaduto: consegna automatica, una volta sola.
  useEffect(() => {
    if (rimanente <= 0 && !consegnata.current) {
      consegnata.current = true;
      void consegna(risposte);
    }
  }, [rimanente, risposte, consegna]);

  const domanda = sessione.domande[indice];
  const date = risposte.filter((r) => r !== null).length;

  return (
    <div className="grid gap-6 lg:grid-cols-[1fr_18rem]">
      <div>
        <div className="sticky top-16 z-10 -mx-4 mb-4 flex items-center justify-between gap-4 bg-slate-50/90 px-4 py-3 backdrop-blur sm:-mx-6 sm:px-6 lg:static lg:mx-0 lg:bg-transparent lg:p-0">
          <p className="text-sm font-semibold text-slate-600">
            Domanda {indice + 1}/{sessione.domande.length} · {nomeMateria(domanda.materia)}
          </p>
          <CronometroProva inizio={sessione.creataIl} fine={sessione.scadeIl!} date={date} totale={sessione.domande.length} />
        </div>

        <NotaOrdineRisposte sessione={sessione} />
        <Card key={indice} className="animate-fade-up p-6 sm:p-8">
          <h2 className="text-xl font-bold text-slate-900">{domanda.testo}</h2>
          <div className="mt-6 grid gap-3" role="radiogroup">
            {domanda.opzioni.map((opzione, i) => (
              <button
                key={i}
                role="radio"
                aria-checked={risposte[indice] === i}
                onClick={() => setRisposte((r) => r.map((v, j) => (j === indice ? (v === i ? null : i) : v)))}
                className={cx(
                  "flex items-center gap-3 rounded-xl p-4 text-left font-medium ring-1 transition",
                  risposte[indice] === i ? "bg-brand-50 text-brand-900 ring-2 ring-brand-500" : "ring-slate-200 hover:bg-slate-50",
                )}
              >
                <span
                  className={cx(
                    "grid size-7 shrink-0 place-items-center rounded-lg text-sm font-bold",
                    risposte[indice] === i ? "bg-brand-600 text-white" : "bg-slate-100 text-slate-600",
                  )}
                >
                  {String.fromCharCode(65 + i)}
                </span>
                {opzione}
              </button>
            ))}
          </div>
          <p className="mt-4 text-xs text-slate-400">Clicca di nuovo una risposta per lasciarla in bianco.</p>
        </Card>

        <div className="mt-6 flex justify-between">
          <Button variant="secondary" disabled={indice === 0} onClick={() => setIndice((i) => i - 1)}>
            Precedente
          </Button>
          <Button disabled={indice === sessione.domande.length - 1} onClick={() => setIndice((i) => i + 1)}>
            Successiva <ArrowRight className="size-4" />
          </Button>
        </div>
      </div>

      <aside className="space-y-4">
        <Card>
          <p className="text-sm font-semibold text-slate-900">
            {date} di {sessione.domande.length} risposte date
          </p>
          <div className="mt-3 grid grid-cols-8 gap-1.5 lg:grid-cols-6">
            {risposte.map((r, i) => (
              <button
                key={i}
                onClick={() => setIndice(i)}
                aria-label={`Vai alla domanda ${i + 1}`}
                className={cx(
                  "aspect-square rounded-md text-xs font-bold transition",
                  i === indice && "ring-2 ring-brand-500 ring-offset-1",
                  r !== null ? "bg-brand-600 text-white" : "bg-slate-100 text-slate-500 hover:bg-slate-200",
                )}
              >
                {i + 1}
              </button>
            ))}
          </div>
        </Card>

        {errore && <Alert tone="error">{errore}</Alert>}

        {conferma ? (
          <Card className="ring-amber-300">
            <p className="text-sm font-semibold">Vuoi consegnare?</p>
            {date < sessione.domande.length && (
              <p className="mt-1 text-sm text-slate-500">{sessione.domande.length - date} domande restano senza risposta.</p>
            )}
            <div className="mt-3 flex gap-2">
              <Button variant="secondary" size="sm" onClick={() => setConferma(false)}>
                Annulla
              </Button>
              <Button size="sm" loading={inCorso} onClick={() => void consegna(risposte)}>
                Consegna
              </Button>
            </div>
          </Card>
        ) : (
          <Button variant="accent" size="lg" className="w-full" onClick={() => setConferma(true)}>
            <Flag className="size-4" /> Consegna la prova
          </Button>
        )}
      </aside>
    </div>
  );
}

// ── Risultati ────────────────────────────────────────────────────────────────

/** Risultati: punteggio, esito, risultati per materia e revisione domanda per domanda. */
function Risultati({ sessione }: { sessione: SessioneApi }) {
  const esito = sessione.esito!;
  const [aperta, setAperta] = useState<number | null>(null);
  const simulazione = sessione.tipo === "simulazione";

  return (
    <div className="mx-auto max-w-3xl space-y-6">
      <Card
        className={cx(
          "overflow-hidden p-0 text-center",
          simulazione && (esito.superata ? "ring-emerald-200" : "ring-rose-200"),
        )}
      >
        <div
          className={cx(
            "px-6 py-8",
            simulazione
              ? esito.superata
                ? "bg-gradient-to-br from-emerald-500 to-teal-600 text-white"
                : "bg-gradient-to-br from-slate-700 to-slate-900 text-white"
              : "bg-gradient-to-br from-brand-600 to-fuchsia-600 text-white",
          )}
        >
          <Trophy className="mx-auto size-8 text-accent-300" />
          <p className="mt-3 text-sm font-semibold opacity-80">
            {simulazione ? (esito.superata ? "Prova superata" : "Prova non superata") : "Sessione completata"}
          </p>
          <p className="mt-1 text-5xl font-extrabold tracking-tight">{esito.percentuale}%</p>
          {!simulazione && (
            <p className="mt-1 text-sm opacity-80">
              {esito.corrette} giuste su {esito.corrette + esito.errate} risposte
              {esito.omesse > 0 && ` · ${esito.omesse} domande non fatte`}
            </p>
          )}
          {simulazione && (
            <p className="mt-1 text-sm opacity-80">
              Punteggio {esito.punteggio.toLocaleString("it-IT")} su {esito.massimo} · soglia {Math.round(sessione.regole.soglia * 100)}%
            </p>
          )}
          {simulazione && sessione.consegnataIl && sessione.scadeIl && (
            <p className="mt-1 inline-flex items-center gap-1 text-sm opacity-80">
              <Timer className="size-4" /> Tempo impiegato{" "}
              {durata(Math.min(Date.parse(sessione.consegnataIl), Date.parse(sessione.scadeIl)) - Date.parse(sessione.creataIl))} su{" "}
              {durata(Date.parse(sessione.scadeIl) - Date.parse(sessione.creataIl))}
            </p>
          )}
          {!simulazione && sessione.consegnataIl && (
            <p className="mt-1 inline-flex items-center gap-1 text-sm opacity-80">
              <Timer className="size-4" /> Tempo impiegato {durata(Date.parse(sessione.consegnataIl) - Date.parse(sessione.creataIl))}
            </p>
          )}
        </div>
        <div className="grid grid-cols-3 divide-x divide-slate-100">
          {[
            { label: "Giuste", valore: esito.corrette, cls: "text-emerald-600" },
            { label: "Sbagliate", valore: esito.errate, cls: "text-rose-600" },
            { label: "Non date", valore: esito.omesse, cls: "text-slate-500" },
          ].map((x) => (
            <div key={x.label} className="py-4">
              <p className={cx("text-2xl font-extrabold", x.cls)}>{x.valore}</p>
              <p className="text-xs font-medium text-slate-500">{x.label}</p>
            </div>
          ))}
        </div>
      </Card>

      {esito.perMateria.length > 1 && (
        <Card>
          <p className="mb-4 font-semibold">Per materia</p>
          <ul className="space-y-3">
            {esito.perMateria.map((m) => {
              const p = Math.round((m.corrette / m.totale) * 100);
              return (
                <li key={m.materia}>
                  <div className="flex justify-between text-sm">
                    <span className="font-medium">{nomeMateria(m.materia)}</span>
                    <span className="text-slate-500">
                      {m.corrette}/{m.totale}
                    </span>
                  </div>
                  <ProgressBar value={p} tone={p >= 70 ? "green" : p >= 50 ? "amber" : "red"} className="mt-1" />
                </li>
              );
            })}
          </ul>
        </Card>
      )}

      <div className="flex flex-wrap justify-center gap-3">
        <ButtonLink to="/app" variant="secondary">
          Torna alla dashboard
        </ButtonLink>
        <ButtonLink to={sessione.concorsoId ? `/app/concorsi/${sessione.concorsoId}` : "/app/studio"}>
          <RotateCcw className="size-4" /> Nuova sessione
        </ButtonLink>
      </div>

      <section>
        <h2 className="mb-3 text-lg font-bold">Rivedi le risposte</h2>
        <NotaOrdineRisposte sessione={sessione} />
        <div className="space-y-2">
          {sessione.domande.map((d, i) => {
            if (!haSoluzione(d)) return null;
            const r = sessione.risposte?.[i] ?? null;
            const ok = r === d.corretta;
            return (
              <Card key={`${d.materia}/${d.id}`} className="p-0">
                <button onClick={() => setAperta(aperta === i ? null : i)} className="flex w-full items-start gap-3 p-4 text-left">
                  {r === null ? (
                    <span className="mt-0.5 size-5 shrink-0 rounded-full border-2 border-slate-300" />
                  ) : ok ? (
                    <CheckCircle2 className="mt-0.5 size-5 shrink-0 text-emerald-500" />
                  ) : (
                    <XCircle className="mt-0.5 size-5 shrink-0 text-rose-500" />
                  )}
                  <span className="flex-1 text-sm font-medium">
                    {i + 1}. {d.testo}
                  </span>
                  <ChevronDown className={cx("size-4 shrink-0 text-slate-400 transition", aperta === i && "rotate-180")} />
                </button>
                {aperta === i && (
                  <div className="space-y-2 border-t border-slate-100 px-4 py-3 text-sm">
                    {r !== null && !ok && (
                      <p className="text-rose-700">
                        <span className="font-semibold">La tua risposta:</span> {d.opzioni[r]}
                      </p>
                    )}
                    <p className="text-emerald-700">
                      <span className="font-semibold">Risposta giusta:</span> {d.opzioni[d.corretta]}
                    </p>
                    <p className="text-slate-600">{d.spiegazione}</p>
                    <ChiediAlTutor domanda={d} risposta={r} />
                    <div className="flex flex-wrap items-center gap-3">
                      <StellaSessione sessione={sessione} domanda={d} />
                      <SegnalaErrore contesto={contestoDomanda(sessione, d)} />
                    </div>
                  </div>
                )}
              </Card>
            );
          })}
        </div>
      </section>

      <p className="text-center text-sm">
        <Link to="/app" className="font-semibold text-brand-600">
          Torna alla dashboard
        </Link>
      </p>
    </div>
  );
}
