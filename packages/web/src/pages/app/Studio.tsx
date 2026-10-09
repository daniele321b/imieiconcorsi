import { DOMANDE_STUDIO } from "@imieiconcorsi/core/domain";
import { BookOpenCheck, Lock } from "lucide-react";
import { useState } from "react";
import { IconaMateria } from "../../components/brand";
import { Alert, Button, Card, PageHeader, PremiumModal, Spinner, UpgradeBanner, cx } from "../../components/ui";
import { useApi, type MateriaApi } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { useAvviaSessione } from "../../lib/sessioni";

// Studio (/app/studio): scelta delle materie e del numero di domande per una sessione di
// studio, e simulazione libera sulle materie scelte.

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
