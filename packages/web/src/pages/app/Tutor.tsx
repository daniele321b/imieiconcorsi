import { COSTI_AI, DOMANDE_ALLENAMENTO_AI, GETTONI_AI_PRO, MATERIE, nomeMateria, type MateriaId } from "@imieiconcorsi/core/domain";
import { ArrowRight, CheckCircle2, Coins, Lock, MessageCircleQuestion, RotateCcw, Sparkles, Target, XCircle } from "lucide-react";
import { useState } from "react";
import { TutorChat } from "../../components/TutorChat";
import { Alert, Badge, Button, ButtonLink, Card, PageHeader, ProgressBar, Spinner, UpgradeBanner, cx } from "../../components/ui";
import { api, ApiError, toneErroreAi, useApi, type AiStato, type DomandaAllenamento, type GettoniAi } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { data } from "../../lib/format";

// Tutor AI del piano Pro: allenamento con domande nuove sui punti deboli e chat libera.
// Ogni azione costa gettoni (COSTI_AI); il mese dopo si rinnovano.

/** Pagina /app/tutor: per i piani senza AI, la presentazione del piano Pro. */
export function Tutor() {
  const { utente } = useUtente();
  if (!utente.limiti.ai) return <TutorBloccato />;
  return <TutorPro />;
}

/** Tutor per il piano Pro: gettoni, allenamento e chat libera. */
function TutorPro() {
  const { data: stato, loading, error, setData } = useApi<AiStato>("/ai/stato");
  const aggiornaGettoni = (gettoni: GettoniAi) => setData((s) => s && { ...s, gettoni });
  const [materiaChat, setMateriaChat] = useState<MateriaId | "">("");

  if (loading) return <Spinner />;
  if (error || !stato) return <Alert tone="error">{error?.message ?? "Tutor non disponibile"}</Alert>;

  const { gettoni } = stato;

  return (
    <div className="space-y-8">
      <PageHeader
        title="Tutor AI"
        subtitle="Domande nuove sui tuoi errori e un insegnante sempre disponibile per spiegarti norme, esercizi e argomenti."
      />

      <Card className="flex flex-wrap items-center gap-4">
        <span className="grid size-11 shrink-0 place-items-center rounded-2xl bg-amber-100 text-amber-700">
          <Coins className="size-5" />
        </span>
        <div className="min-w-48 flex-1">
          <div className="flex items-baseline justify-between gap-2">
            <p className="font-bold text-slate-900">
              {gettoni.restanti} gettoni su {gettoni.totale}
            </p>
            <p className="text-xs text-slate-500">si rinnovano il {data(gettoni.rinnovoIl)}</p>
          </div>
          <ProgressBar
            value={(gettoni.restanti / Math.max(1, gettoni.totale)) * 100}
            tone={gettoni.restanti < gettoni.totale * 0.15 ? "amber" : "brand"}
            className="mt-2"
          />
          <p className="mt-1.5 text-xs text-slate-500">
            Risposta del tutor: {stato.costi.tutor} gettone · Allenamento da {DOMANDE_ALLENAMENTO_AI} domande: {stato.costi.allenamento} gettoni
          </p>
        </div>
      </Card>

      <Allenamento puntiDeboli={stato.puntiDeboli} onGettoni={aggiornaGettoni} />

      <section>
        <div className="mb-3 flex flex-wrap items-end justify-between gap-3">
          <div>
            <h2 className="flex items-center gap-2 text-lg font-bold text-slate-900">
              <MessageCircleQuestion className="size-5 text-brand-600" /> Chiedi al tutor
            </h2>
            <p className="text-sm text-slate-500">Un argomento che non ti torna, una norma da capire, un esercizio di logica.</p>
          </div>
          <label className="text-xs font-semibold text-slate-500">
            Materia
            <select
              value={materiaChat}
              onChange={(e) => setMateriaChat(e.target.value as MateriaId | "")}
              className="mt-1 block h-10 rounded-xl border-0 bg-white px-3 text-sm text-slate-900 ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500"
            >
              <option value="">Qualsiasi</option>
              {MATERIE.map((m) => (
                <option key={m.id} value={m.id}>
                  {m.nome}
                </option>
              ))}
            </select>
          </label>
        </div>
        <TutorChat
          // Cambiando materia la conversazione riparte.
          key={materiaChat}
          materia={materiaChat || undefined}
          onGettoni={aggiornaGettoni}
          suggerimenti={[
            "Differenza tra annullabilità e nullità di un atto",
            "Come funziona il bilancio di un comune?",
            "Spiegami le proporzioni con un esempio",
          ]}
        />
      </section>
    </div>
  );
}

/** Allenamento: genera domande nuove sulla materia scelta (o la più debole) e le corregge subito. */
function Allenamento({ puntiDeboli, onGettoni }: { puntiDeboli: AiStato["puntiDeboli"]; onGettoni: (g: GettoniAi) => void }) {
  const [materia, setMateria] = useState<MateriaId | undefined>(puntiDeboli[0]?.materia);
  const [domande, setDomande] = useState<DomandaAllenamento[]>();
  const [inCorso, setInCorso] = useState(false);
  const [errore, setErrore] = useState<ApiError>();

  async function genera() {
    setInCorso(true);
    setErrore(undefined);
    try {
      const r = await api<{ materia: MateriaId; domande: DomandaAllenamento[]; gettoni: GettoniAi }>("/ai/allenamento", {
        method: "POST",
        body: { materia },
      });
      setMateria(r.materia);
      setDomande(r.domande);
      onGettoni(r.gettoni);
    } catch (err) {
      setErrore(err instanceof ApiError ? err : new ApiError(0, "Errore di rete"));
    } finally {
      setInCorso(false);
    }
  }

  const deboli = new Map(puntiDeboli.map((p) => [p.materia, p]));

  return (
    <section>
      <h2 className="flex items-center gap-2 text-lg font-bold text-slate-900">
        <Target className="size-5 text-brand-600" /> Allenamento sui punti deboli
      </h2>
      <p className="mb-3 text-sm text-slate-500">
        Il tutor guarda le domande che hai sbagliato e ne scrive {DOMANDE_ALLENAMENTO_AI} nuove sugli stessi argomenti, ogni volta diverse.
      </p>

      {domande ? (
        <QuizAi key={domande[0]?.id} domande={domande} onGettoni={onGettoni} onAltre={() => void genera()} generando={inCorso} />
      ) : (
        <Card className="space-y-4">
          {puntiDeboli.length > 0 ? (
            <p className="text-sm text-slate-600">
              Dalle tue sessioni, le materie dove sbagli di più sono in cima: parti da lì.
            </p>
          ) : (
            <p className="text-sm text-slate-600">
              Fai qualche sessione di studio o una simulazione e il tutor capirà dove sbagli. Intanto scegli una materia.
            </p>
          )}
          <div className="flex flex-wrap gap-2">
            {[...puntiDeboli.map((p) => p.materia), ...MATERIE.map((m) => m.id).filter((id) => !deboli.has(id))].map((id) => {
              const p = deboli.get(id);
              return (
                <button
                  key={id}
                  onClick={() => setMateria(id)}
                  className={cx(
                    "inline-flex items-center gap-1.5 rounded-full px-3 py-1.5 text-sm font-semibold transition",
                    materia === id ? "bg-brand-600 text-white" : "bg-white text-slate-600 ring-1 ring-slate-200 hover:ring-slate-300",
                  )}
                >
                  {nomeMateria(id)}
                  {p && (
                    <span className={cx("rounded-full px-1.5 text-xs", materia === id ? "bg-white/20" : p.percentuale < 60 ? "bg-rose-50 text-rose-700" : "bg-slate-100")}>
                      {p.percentuale}%
                    </span>
                  )}
                </button>
              );
            })}
          </div>
          {errore && (errore.code === "LIMITE_PIANO" ? <UpgradeBanner message={errore.message} /> : <Alert tone={toneErroreAi(errore)}>{errore.message}</Alert>)}
          <Button size="lg" disabled={!materia} loading={inCorso} onClick={() => void genera()}>
            <Sparkles className="size-4" /> Genera {DOMANDE_ALLENAMENTO_AI} domande · {COSTI_AI.allenamento} gettoni
          </Button>
          {inCorso && <p className="text-xs text-slate-500">Il tutor sta scrivendo le domande: ci vogliono una decina di secondi.</p>}
        </Card>
      )}
    </section>
  );
}

/** Una domanda alla volta, con la correzione subito e il tutor per farsi spiegare. */
function QuizAi({
  domande,
  onGettoni,
  onAltre,
  generando,
}: {
  domande: DomandaAllenamento[];
  onGettoni: (g: GettoniAi) => void;
  onAltre: () => void;
  generando: boolean;
}) {
  const [indice, setIndice] = useState(0);
  const [risposte, setRisposte] = useState<(number | null)[]>(() => domande.map(() => null));
  const [tutor, setTutor] = useState(false);
  const finito = indice >= domande.length;
  const giuste = risposte.filter((r, i) => r === domande[i]?.corretta).length;

  if (finito) {
    return (
      <Card className="text-center">
        <p className="text-sm font-semibold text-brand-600">Allenamento finito</p>
        <p className="mt-1 text-4xl font-extrabold text-slate-900">
          {giuste}/{domande.length}
        </p>
        <p className="mt-1 text-sm text-slate-500">{nomeMateria(domande[0].materia)}</p>
        <div className="mt-5 flex flex-wrap justify-center gap-3">
          <Button variant="secondary" onClick={() => (setIndice(0), setRisposte(domande.map(() => null)))}>
            <RotateCcw className="size-4" /> Rifai queste
          </Button>
          <Button loading={generando} onClick={onAltre}>
            <Sparkles className="size-4" /> Altre {DOMANDE_ALLENAMENTO_AI} domande · {COSTI_AI.allenamento} gettoni
          </Button>
        </div>
      </Card>
    );
  }

  const d = domande[indice];
  const scelta = risposte[indice];
  const rivelata = scelta !== null;

  return (
    <div className="space-y-3">
      <Card key={d.id} className="animate-fade-up p-6 sm:p-8">
        <div className="flex items-center justify-between gap-3">
          <p className="text-xs font-semibold tracking-wide text-slate-400 uppercase">{d.argomento}</p>
          <Badge tone="brand">
            <Sparkles className="size-3" /> {indice + 1}/{domande.length}
          </Badge>
        </div>
        <h3 className="mt-2 text-xl font-bold text-slate-900">{d.testo}</h3>
        <div className="mt-6 grid gap-3">
          {d.opzioni.map((o, i) => {
            const corretta = i === d.corretta;
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
                <span className="flex-1">{o}</span>
                {rivelata && corretta && <CheckCircle2 className="size-5 text-emerald-600" />}
                {sbagliata && <XCircle className="size-5 text-rose-500" />}
              </button>
            );
          })}
        </div>
        {rivelata && (
          <div className="mt-6 animate-fade-up rounded-xl bg-slate-50 p-4 text-sm">
            <p className="font-semibold text-slate-900">{scelta === d.corretta ? "Esatto!" : "Non proprio."}</p>
            <p className="mt-1 text-slate-600">{d.spiegazione}</p>
            {!tutor && (
              <button onClick={() => setTutor(true)} className="mt-3 inline-flex items-center gap-1.5 text-sm font-semibold text-brand-600 hover:text-brand-700">
                <Sparkles className="size-4" /> Chiedi al tutor
              </button>
            )}
          </div>
        )}
      </Card>

      {rivelata && tutor && (
        <TutorChat
          key={d.id}
          domanda={{ ...d, risposta: scelta }}
          onGettoni={onGettoni}
          suggerimenti={scelta === d.corretta ? ["Spiegamelo meglio con un esempio"] : ["Perché la mia risposta è sbagliata?", "Dammi un trucco per ricordarlo"]}
        />
      )}

      <p className="text-xs text-slate-400">Domande scritte dall'AI a partire dalla nostra banca: possono contenere imprecisioni.</p>

      <div className="flex justify-end">
        <Button
          size="lg"
          disabled={!rivelata}
          onClick={() => {
            setTutor(false);
            setIndice((i) => i + 1);
          }}
        >
          {indice === domande.length - 1 ? "Vedi il risultato" : "Prossima domanda"} <ArrowRight className="size-4" />
        </Button>
      </div>
    </div>
  );
}

/** Free e Medium: cosa fa il tutor, con l'invito al piano Pro. */
function TutorBloccato() {
  return (
    <div className="space-y-6">
      <PageHeader title="Tutor AI" subtitle="Il tuo insegnante personale per i concorsi, incluso nel piano Pro." />
      <div className="overflow-hidden rounded-3xl bg-gradient-to-br from-brand-950 via-brand-900 to-brand-700 p-6 text-white shadow-xl sm:p-10">
        <Badge tone="amber">
          <Lock className="size-3" /> Piano Pro
        </Badge>
        <h2 className="mt-4 max-w-xl text-2xl font-extrabold tracking-tight sm:text-3xl">Smetti di ripetere gli stessi errori.</h2>
        <div className="mt-6 grid gap-4 sm:grid-cols-3">
          {[
            { Icon: Target, titolo: "Allenamenti mirati", testo: `${DOMANDE_ALLENAMENTO_AI} domande nuove scritte sulle domande che sbagli, ogni volta diverse.` },
            { Icon: MessageCircleQuestion, titolo: "Spiegazioni su misura", testo: "Hai sbagliato? Il tutor ti spiega perché e ti dà un trucco per ricordarlo." },
            { Icon: Coins, titolo: `${GETTONI_AI_PRO} gettoni al mese`, testo: `1 per ogni risposta del tutor, ${COSTI_AI.allenamento} per ogni allenamento.` },
          ].map(({ Icon, titolo, testo }) => (
            <div key={titolo} className="rounded-2xl bg-white/10 p-4 ring-1 ring-white/10">
              <Icon className="size-5 text-accent-300" />
              <p className="mt-2 font-bold">{titolo}</p>
              <p className="mt-1 text-sm text-brand-100">{testo}</p>
            </div>
          ))}
        </div>
        <ButtonLink to="/app/piani" variant="accent" size="lg" className="mt-8">
          <Sparkles className="size-4" /> Passa a Pro
        </ButtonLink>
      </div>
    </div>
  );
}
