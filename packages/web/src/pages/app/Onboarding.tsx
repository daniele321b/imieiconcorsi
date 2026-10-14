import type { CompartoId, FrequenzaAvvisi, MateriaId } from "@imieiconcorsi/core/domain";
import { ArrowLeft, ArrowRight } from "lucide-react";
import { useState } from "react";
import { Link, useNavigate } from "react-router";
import { Logo } from "../../components/brand";
import { AvvisiPicker, InteressiPicker, LivelliPicker } from "../../components/ProfiloPickers";
import { Alert, Button, Field, cx } from "../../components/ui";
import { api } from "../../lib/api";
import { messaggioErrore, useAuth, useUtente } from "../../lib/auth";

// Primo accesso (/app/onboarding): tre passi (comparti, livelli, avvisi) e accettazione di
// Termini e Informativa. Finché non è completato, l'app riporta qui.

/** Titolo e sottotitolo di ogni passo. */
const PASSI = [
  { titolo: "Quali concorsi ti interessano?", sotto: "Scegli uno o più comparti: ti avviseremo solo per questi." },
  { titolo: "Come te la cavi nelle materie?", sotto: "Una stima veloce da 1 a 5. Serve a partire dalle domande giuste per te." },
  { titolo: "Quando vuoi gli avvisi?", sotto: "Puoi cambiarlo quando vuoi dal profilo." },
];

/** Pagina /app/onboarding. */
export function Onboarding() {
  const { utente } = useUtente();
  const { ricarica } = useAuth();
  const navigate = useNavigate();
  const [passo, setPasso] = useState(0);
  const [nome, setNome] = useState(utente.nome ?? "");
  const [interessi, setInteressi] = useState<CompartoId[]>(utente.interessi);
  const [livelli, setLivelli] = useState<Partial<Record<MateriaId, number>>>(utente.livelli);
  const [avvisi, setAvvisi] = useState<FrequenzaAvvisi>(utente.avvisi);
  const [accetto, setAccetto] = useState(false);
  const [salvataggio, setSalvataggio] = useState(false);
  const [errore, setErrore] = useState<string>();

  const puoiAvanzare = passo !== 0 || interessi.length > 0;

  // Salva le scelte del primo accesso (con l'accettazione dei termini) ed entra nell'app.
  async function concludi() {
    setSalvataggio(true);
    setErrore(undefined);
    try {
      await api("/me/profilo", { method: "PUT", body: { nome: nome || undefined, interessi, livelli, avvisi, accettaTermini: true } });
      await ricarica({ rinnovaToken: true });
      navigate("/app", { replace: true });
    } catch (err) {
      setErrore(messaggioErrore(err));
    } finally {
      setSalvataggio(false);
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-brand-50 to-slate-50">
      <div className="mx-auto max-w-3xl px-4 py-8 sm:px-6">
        <Logo />

        <div className="mt-8 flex gap-2" aria-label={`Passo ${passo + 1} di ${PASSI.length}`}>
          {PASSI.map((_, i) => (
            <div key={i} className={cx("h-1.5 flex-1 rounded-full transition", i <= passo ? "bg-brand-600" : "bg-brand-100")} />
          ))}
        </div>

        <div key={passo} className="mt-8 animate-fade-up">
          <p className="text-sm font-semibold text-brand-600">
            Passo {passo + 1} di {PASSI.length}
          </p>
          <h1 className="mt-1 text-2xl font-extrabold tracking-tight text-slate-900 sm:text-3xl">{PASSI[passo].titolo}</h1>
          <p className="mt-1 text-slate-500">{PASSI[passo].sotto}</p>

          <div className="mt-6">
            {passo === 0 && <InteressiPicker value={interessi} onChange={setInteressi} />}
            {passo === 1 && <LivelliPicker value={livelli} onChange={setLivelli} />}
            {passo === 2 && (
              <div className="space-y-6">
                <AvvisiPicker value={avvisi} onChange={setAvvisi} />
                <Field label="Come vuoi che ti chiamiamo? (facoltativo)" name="nome" value={nome} onChange={(e) => setNome(e.target.value)} />
                <label className="flex items-start gap-2.5 rounded-2xl bg-white p-4 text-sm text-slate-600 ring-1 ring-slate-200">
                  <input
                    type="checkbox"
                    checked={accetto}
                    onChange={(e) => setAccetto(e.target.checked)}
                    className="mt-0.5 size-4 rounded border-slate-300 text-brand-600 focus:ring-brand-500"
                  />
                  <span>
                    Accetto i{" "}
                    <Link to="/termini" target="_blank" className="font-semibold text-brand-600 underline">
                      Termini e condizioni
                    </Link>{" "}
                    e ho letto l'
                    <Link to="/privacy" target="_blank" className="font-semibold text-brand-600 underline">
                      Informativa privacy
                    </Link>
                    .
                  </span>
                </label>
              </div>
            )}
          </div>
        </div>

        {errore && (
          <div className="mt-6">
            <Alert tone="error">{errore}</Alert>
          </div>
        )}

        <div className="mt-8 flex items-center justify-between">
          <Button variant="ghost" onClick={() => setPasso((p) => p - 1)} className={cx(passo === 0 && "invisible")}>
            <ArrowLeft className="size-4" /> Indietro
          </Button>
          {passo < PASSI.length - 1 ? (
            <Button size="lg" disabled={!puoiAvanzare} onClick={() => setPasso((p) => p + 1)}>
              Avanti <ArrowRight className="size-4" />
            </Button>
          ) : (
            <Button size="lg" loading={salvataggio} disabled={!accetto} onClick={() => void concludi()}>
              Inizia a prepararti <ArrowRight className="size-4" />
            </Button>
          )}
        </div>
      </div>
    </div>
  );
}
