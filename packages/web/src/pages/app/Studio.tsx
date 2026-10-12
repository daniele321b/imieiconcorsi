import { DOMANDE_STUDIO } from "@imieiconcorsi/core/domain";
import { BookOpenCheck, ChevronRight, Database, Lock } from "lucide-react";
import { Link } from "react-router";
import { useState } from "react";
import { IconaMateria } from "../../components/brand";
import { Alert, Button, Card, PageHeader, PremiumModal, Spinner, UpgradeBanner, cx } from "../../components/ui";
import { useApi, type MateriaApi } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { useAvviaSessione } from "../../lib/sessioni";

// Studio (/app/studio): riquadro d'ingresso alle banche dati ufficiali, scelta delle materie e del
// numero di domande per una sessione di studio, e simulazione libera sulle materie scelte.

/** Pagina /app/studio. */
export function Studio() {
  const { utente } = useUtente();
  const { data, loading, error } = useApi<{ materie: MateriaApi[]; versione?: string }>("/materie");
  const { avvia, inCorso, errore, chiudiErrore } = useAvviaSessione();
  const massimo = utente.limiti.domandePerSessioneStudio;
  const [numero, setNumero] = useState<number>(DOMANDE_STUDIO[0]);
  const [premium, setPremium] = useState(false);

  return (
    <div>
      <PageHeader title="Studio" subtitle="Scegli una materia: la spiegazione arriva subito dopo ogni risposta." />

      {/* Le banche dati ufficiali stanno qui dentro (non più nel menu): si entra toccando il riquadro. */}
      <Link
        to="/app/banche-dati"
        className="mb-6 flex items-center gap-4 rounded-2xl bg-gradient-to-r from-brand-950 via-brand-800 to-brand-600 p-5 text-white shadow-sm transition hover:shadow-md"
      >
        <span className="grid size-12 shrink-0 place-items-center rounded-xl bg-white/10 text-accent-300">
          <Database className="size-6" />
        </span>
        <span className="min-w-0 flex-1">
          <span className="block text-lg font-bold">Banche dati ufficiali</span>
          <span className="block text-sm text-brand-100">
            Le domande pubblicate dagli enti per i concorsi: consultale, studiale o fai una simulazione.
          </span>
        </span>
        <ChevronRight className="size-5 shrink-0 text-brand-200" />
      </Link>

      <h2 className="mb-3 text-lg font-bold text-slate-900">Le materie</h2>

      <div className="mb-6 flex flex-wrap items-center gap-3">
        <span className="text-sm font-semibold text-slate-600">Domande per sessione</span>
        <div className="inline-grid grid-cols-3 rounded-xl bg-white p-1 text-sm font-semibold ring-1 ring-slate-200" role="radiogroup">
          {DOMANDE_STUDIO.map((n) => {
            const bloccato = n > massimo;
            return (
              <button
                key={n}
                role="radio"
                aria-checked={numero === n}
                onClick={() => (bloccato ? setPremium(true) : setNumero(n))}
                className={cx(
                  "inline-flex items-center justify-center gap-1 rounded-lg px-4 py-1.5 transition",
                  numero === n ? "bg-brand-600 text-white" : bloccato ? "text-slate-400" : "text-slate-600 hover:bg-slate-50",
                )}
              >
                {bloccato && <Lock className="size-3" />} {n}
              </button>
            );
          })}
        </div>
      </div>

      {premium && (
        <PremiumModal titolo="Sessioni da 20 o 30 domande" onClose={() => setPremium(false)}>
          Con il piano Free ogni sessione di studio ha 10 domande. Con <strong>Medium</strong> e <strong>Pro</strong> scegli tu
          quante farne (10, 20 o 30), senza pubblicità e con le banche dati ufficiali dei tuoi concorsi.
        </PremiumModal>
      )}

      <div className="space-y-4">
        {errore &&
          (errore.code === "LIMITE_PIANO" ? (
            <UpgradeBanner message={errore.message} onClose={chiudiErrore} />
          ) : (
            <Alert tone="error" onClose={chiudiErrore}>
              {errore.message}
            </Alert>
          ))}
        {error && <Alert tone="error">{error.message}</Alert>}

        {loading ? (
          <Spinner />
        ) : (
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {data?.materie.map((m) => (
              <Card key={m.id} className="flex flex-col">
                <div className="flex items-center gap-3">
                  <IconaMateria icona={m.icona} materia={m.id} className="size-12" />
                  <div>
                    <p className="font-bold text-slate-900">{m.nome}</p>
                    <p className="text-sm text-slate-500">{m.domande} domande disponibili</p>
                  </div>
                </div>
                <div className="mt-4 flex items-center gap-1.5" aria-label={`Il tuo livello: ${m.livello ?? "non indicato"}`}>
                  {[1, 2, 3, 4, 5].map((n) => (
                    <span key={n} className={cx("h-1.5 flex-1 rounded-full", m.livello && n <= m.livello ? "bg-brand-500" : "bg-slate-100")} />
                  ))}
                </div>
                <p className="mt-1 text-xs text-slate-500">Il tuo livello {m.livello ? `${m.livello}/5` : "non indicato"}</p>
                <Button
                  className="mt-5"
                  disabled={!m.domande}
                  loading={inCorso === m.id}
                  onClick={() => void avvia({ tipo: "studio", materie: [m.id], numero: Math.min(numero, massimo) }, m.id)}
                >
                  <BookOpenCheck className="size-4" /> {m.domande ? "Inizia" : "In arrivo"}
                </Button>
              </Card>
            ))}
          </div>
        )}
      </div>

      <p className="mx-auto mt-10 max-w-3xl text-center text-xs leading-relaxed text-slate-400">
        Le domande sono scritte dalla redazione a partire da libri di testo e fonti online: MatematicaC3 e Matematica Dolce
        (CC BY / CC BY-SA), appunti di L. Ghio (CC BY-SA), voci di Wikipedia (CC BY-SA 4.0), dati ISTAT (CC BY 4.0) e testi di
        legge ufficiali su Normattiva.{data?.versione && <> Banca domande {data.versione}.</>}
      </p>
    </div>
  );
}
