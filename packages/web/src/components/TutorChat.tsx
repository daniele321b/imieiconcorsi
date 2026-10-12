import type { MateriaId } from "@imieiconcorsi/core/domain";
import { ArrowUp, Sparkles } from "lucide-react";
import { type FormEvent, Fragment, type ReactNode, useEffect, useRef, useState } from "react";
import { api, ApiError, toneErroreAi, type DomandaTutor, type GettoniAi, type MessaggioTutor } from "../lib/api";
import { Alert, UpgradeBanner, cx } from "./ui";

/** Grassetto (**così**) dentro una riga. */
function inline(testo: string) {
  return testo.split(/(\*\*[^*]+\*\*)/g).map((p, i) =>
    p.startsWith("**") && p.endsWith("**") ? (
      <strong key={i} className="font-semibold text-slate-900">
        {p.slice(2, -2)}
      </strong>
    ) : (
      <Fragment key={i}>{p}</Fragment>
    ),
  );
}

/** Il tutor scrive testo semplice: paragrafi, elenchi con "- " e grassetto. */
export function TestoTutor({ testo }: { testo: string }) {
  const blocchi: ReactNode[] = [];
  let elenco: string[] = [];
  const chiudiElenco = () => {
    if (!elenco.length) return;
    blocchi.push(
      <ul key={blocchi.length} className="list-disc space-y-1 pl-5">
        {elenco.map((r, i) => (
          <li key={i}>{inline(r)}</li>
        ))}
      </ul>,
    );
    elenco = [];
  };
  for (const riga of testo.split("\n")) {
    const voce = riga.match(/^\s*[-*•]\s+(.*)$/);
    if (voce) elenco.push(voce[1]);
    else {
      chiudiElenco();
      if (riga.trim()) blocchi.push(<p key={blocchi.length}>{inline(riga.replace(/^#+\s*/, ""))}</p>);
    }
  }
  chiudiElenco();
  return <div className="space-y-2">{blocchi}</div>;
}

/**
 * Chat con il tutor AI (piano Pro). Con `domanda` il tutor conosce la domanda, la risposta
 * giusta e quella data; senza, si parla di una materia o di qualsiasi argomento d'esame.
 */
export function TutorChat({
  domanda,
  materia,
  suggerimenti = [],
  onGettoni,
  className,
}: {
  domanda?: DomandaTutor;
  materia?: MateriaId;
  /** Domande pronte da un clic, es. "Perché la mia risposta è sbagliata?" */
  suggerimenti?: string[];
  onGettoni?: (g: GettoniAi) => void;
  className?: string;
}) {
  const [messaggi, setMessaggi] = useState<MessaggioTutor[]>([]);
  const [testo, setTesto] = useState("");
  const [inCorso, setInCorso] = useState(false);
  const [errore, setErrore] = useState<ApiError>();
  const [gettoni, setGettoni] = useState<GettoniAi>();
  const fondo = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (messaggi.length) fondo.current?.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }, [messaggi.length, inCorso]);

  async function invia(domandaStudente: string) {
    const pulita = domandaStudente.trim();
    if (!pulita || inCorso) return;
    const nuovi = [...messaggi, { ruolo: "studente" as const, testo: pulita }];
    setMessaggi(nuovi);
    setTesto("");
    setInCorso(true);
    setErrore(undefined);
    try {
      const r = await api<{ risposta: string; fuoriTema?: boolean; gettoni: GettoniAi }>("/ai/tutor", {
        method: "POST",
        body: { domanda, materia, messaggi: nuovi },
      });
      if (r.fuoriTema) {
        // Domanda fuori tema: non resta nella conversazione (non la si rimanda al modello), solo l'avviso.
        setMessaggi(messaggi);
        setErrore(new ApiError(200, r.risposta, "FUORI_TEMA"));
      } else {
        setMessaggi([...nuovi, { ruolo: "tutor", testo: r.risposta }]);
      }
      setGettoni(r.gettoni);
      onGettoni?.(r.gettoni);
    } catch (err) {
      // La domanda torna nel campo: si può riprovare senza riscriverla.
      setMessaggi(messaggi);
      setTesto(pulita);
      setErrore(err instanceof ApiError ? err : new ApiError(0, "Errore di rete"));
    } finally {
      setInCorso(false);
    }
  }

  const onSubmit = (e: FormEvent) => {
    e.preventDefault();
    void invia(testo);
  };

  return (
    <div className={cx("overflow-hidden rounded-2xl bg-white ring-1 ring-brand-100", className)}>
      <div className="flex items-center gap-2 bg-gradient-to-r from-brand-950 to-brand-700 px-4 py-2.5 text-white">
        <Sparkles className="size-4 text-accent-300" />
        <p className="text-sm font-bold">Tutor AI</p>
        <p className="ml-auto text-xs text-brand-100">
          {gettoni ? `ancora ${gettoni.restanti} crediti AI questo mese` : ""}
        </p>
      </div>

      <div className="max-h-[28rem] space-y-3 overflow-y-auto p-4 text-sm leading-relaxed text-slate-700">
        {!messaggi.length && (
          <p className="text-slate-500">
            {domanda
              ? "Chiedimi perché la risposta giusta è quella, o fatti spiegare l'argomento con un esempio."
              : "Chiedimi di spiegarti un argomento, una norma o un esercizio: rispondo come un insegnante."}
          </p>
        )}
        {messaggi.map((m, i) =>
          m.ruolo === "studente" ? (
            <div key={i} className="ml-auto w-fit max-w-[85%] rounded-2xl rounded-br-md bg-brand-600 px-3.5 py-2 text-white">
              {m.testo}
            </div>
          ) : (
            <div key={i} className="max-w-[92%] animate-fade-up rounded-2xl rounded-bl-md bg-slate-50 px-3.5 py-2.5 ring-1 ring-slate-100">
              <TestoTutor testo={m.testo} />
            </div>
          ),
        )}
        {inCorso && (
          <div className="flex w-fit items-center gap-1 rounded-2xl rounded-bl-md bg-slate-50 px-4 py-3 ring-1 ring-slate-100" aria-label="Il tutor sta scrivendo">
            {[0, 150, 300].map((d) => (
              <span key={d} className="size-1.5 animate-bounce rounded-full bg-brand-400" style={{ animationDelay: `${d}ms` }} />
            ))}
          </div>
        )}
        <div ref={fondo} />
      </div>

      {errore && (
        <div className="px-4 pb-3">
          {errore.code === "LIMITE_PIANO" ? (
            <UpgradeBanner message={errore.message} />
          ) : (
            <Alert tone={toneErroreAi(errore)} onClose={() => setErrore(undefined)}>
              {errore.message}
            </Alert>
          )}
        </div>
      )}

      {!messaggi.length && suggerimenti.length > 0 && (
        <div className="flex flex-wrap gap-2 px-4 pb-3">
          {suggerimenti.map((s) => (
            <button
              key={s}
              disabled={inCorso}
              onClick={() => void invia(s)}
              className="rounded-full bg-brand-50 px-3 py-1.5 text-xs font-semibold text-brand-700 ring-1 ring-brand-100 transition hover:bg-brand-100"
            >
              {s}
            </button>
          ))}
        </div>
      )}

      <form onSubmit={onSubmit} className="flex items-end gap-2 border-t border-slate-100 p-3">
        <textarea
          value={testo}
          onChange={(e) => setTesto(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              void invia(testo);
            }
          }}
          rows={1}
          maxLength={1200}
          placeholder="Scrivi la tua domanda…"
          aria-label="Domanda per il tutor"
          className="max-h-32 min-h-10 flex-1 resize-none rounded-xl border-0 bg-slate-50 px-3 py-2.5 text-sm ring-1 ring-slate-200 focus:ring-2 focus:ring-brand-500 focus:outline-none"
        />
        <button
          type="submit"
          disabled={!testo.trim() || inCorso}
          aria-label="Invia"
          className="grid size-10 shrink-0 place-items-center rounded-xl bg-brand-600 text-white transition hover:bg-brand-700 disabled:opacity-40"
        >
          <ArrowUp className="size-4" />
        </button>
      </form>
      <p className="px-4 pb-3 text-[11px] text-slate-400">
        Il tutor AI può sbagliare: per norme, date e numeri controlla sempre la fonte. Non scrivere dati personali.
      </p>
    </div>
  );
}
