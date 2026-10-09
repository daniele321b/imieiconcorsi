import { COMPARTI, nomeMateria, type CompartoId, type MateriaId } from "@imieiconcorsi/core/domain";
import { BookOpenCheck, Database, Lock, Timer } from "lucide-react";
import { useState } from "react";
import { Link } from "react-router";
import { Alert, Badge, Button, Card, EmptyState, PageHeader, PremiumModal, Spinner, UpgradeBanner, cx } from "../../components/ui";
import { useApi } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { useAvviaSessione } from "../../lib/sessioni";

interface BancaApi {
  id: string;
  titolo: string;
  comparto: CompartoId;
  anno?: number;
  materia?: MateriaId;
  domande: number;
  concorsoId?: string;
  concorsoTitolo?: string;
}

const STUDIO = [10, 20, 30] as const;
const SIMULAZIONE = [30, 60] as const;

// Banche dati ufficiali per comparto, anche slegate dai concorsi (es. "Polizia di Stato 2026").
// Si vedono tutte; esercitarsi richiede Medium o Pro.
export function BancheDati() {
  const { utente } = useUtente();
  const { data, loading, error } = useApi<{ banche: BancaApi[] }>("/banche-dati");
  const { avvia, inCorso, errore, chiudiErrore } = useAvviaSessione();
  const [premium, setPremium] = useState(false);
  const accesso = utente.limiti.bancheDati;

  const perComparto = COMPARTI.map((c) => ({ ...c, banche: (data?.banche ?? []).filter((b) => b.comparto === c.id) })).filter((c) => c.banche.length);

  return (
    <div>
      <PageHeader
        title="Banche dati ufficiali"
        subtitle="Le domande pubblicate dagli enti per le prove dei concorsi, divise per comparto. Studia con la correzione subito o fai una simulazione a tempo."
      />

      <div className="space-y-4">
        {!accesso && (
          <UpgradeBanner message="Le banche dati ufficiali sono incluse nei piani Medium e Pro: qui sotto vedi quelle disponibili." />
        )}
        {errore &&
          (errore.code === "LIMITE_PIANO" ? (
            <UpgradeBanner message={errore.message} onClose={chiudiErrore} />
          ) : (
            <Alert tone="error" onClose={chiudiErrore}>
              {errore.message}
            </Alert>
          ))}
        {error && <Alert tone="error">{error.message}</Alert>}
      </div>

      {premium && (
        <PremiumModal titolo="Banche dati ufficiali" onClose={() => setPremium(false)}>
          Con <strong>Medium</strong> e <strong>Pro</strong> ti eserciti sulle domande ufficiali pubblicate dagli enti: sessioni di
          studio con la risposta giusta subito e simulazioni a tempo, per tutte le banche dati disponibili.
        </PremiumModal>
      )}

      {loading ? (
        <Spinner />
      ) : !perComparto.length ? (
        <EmptyState icon={<Database className="size-6" />} title="Nessuna banca dati ancora">
          Le pubblichiamo appena gli enti le rendono disponibili: ti avvisiamo noi.
        </EmptyState>
      ) : (
        <div className="mt-6 space-y-8">
          {perComparto.map((c) => (
            <section key={c.id}>
              <h2 className="mb-3 text-lg font-bold text-slate-900">{c.nome}</h2>
              <div className="grid gap-4 md:grid-cols-2">
                {c.banche.map((b) => (
                  <SchedaBanca
                    key={b.id}
                    banca={b}
                    bloccata={!accesso}
                    inCorso={inCorso}
                    onBloccata={() => setPremium(true)}
                    onAvvia={(tipo, numero) => void avvia({ tipo, bancaDatiId: b.id, numero }, `${b.id}-${tipo}`)}
                  />
                ))}
              </div>
            </section>
          ))}
        </div>
      )}
    </div>
  );
}

function SchedaBanca({
  banca,
  bloccata,
  inCorso,
  onBloccata,
  onAvvia,
}: {
  banca: BancaApi;
  bloccata: boolean;
  inCorso?: string;
  onBloccata: () => void;
  onAvvia: (tipo: "studio" | "simulazione", numero: number) => void;
}) {
  const [studio, setStudio] = useState<number>(STUDIO[0]);
  const [simulazione, setSimulazione] = useState<number>(SIMULAZIONE[1]);

  const scelta = (opzioni: readonly number[], valore: number, set: (n: number) => void) => (
    <div className="inline-grid rounded-lg bg-slate-100 p-0.5 text-xs font-semibold" style={{ gridTemplateColumns: `repeat(${opzioni.length}, 1fr)` }}>
      {opzioni.map((n) => (
        <button
          key={n}
          onClick={() => set(n)}
          className={cx("rounded-md px-2.5 py-1 transition", valore === n ? "bg-white text-brand-700 shadow-sm" : "text-slate-500")}
        >
          {n}
        </button>
      ))}
    </div>
  );

  return (
    <Card className="flex flex-col">
      <div className="flex items-start gap-3">
        <span className="grid size-10 shrink-0 place-items-center rounded-xl bg-brand-50 text-brand-600">
          {bloccata ? <Lock className="size-5" /> : <Database className="size-5" />}
        </span>
        <div className="min-w-0 flex-1">
          <p className="font-bold text-slate-900">{banca.titolo}</p>
          <div className="mt-1 flex flex-wrap gap-1.5">
            {banca.anno && <Badge>{banca.anno}</Badge>}
            <Badge tone="brand">{banca.domande.toLocaleString("it-IT")} domande</Badge>
            {banca.materia && <Badge>{nomeMateria(banca.materia)}</Badge>}
          </div>
          {banca.concorsoId && (
            <Link to={`/app/concorsi/${banca.concorsoId}`} className="mt-1 block truncate text-xs text-slate-500 hover:text-brand-700">
              Concorso: {banca.concorsoTitolo}
            </Link>
          )}
        </div>
      </div>

      <div className="mt-4 space-y-2 border-t border-slate-100 pt-4">
        <div className="flex items-center justify-between gap-2">
          {scelta(STUDIO, studio, setStudio)}
          <Button
            size="sm"
            variant="secondary"
            loading={inCorso === `${banca.id}-studio`}
            onClick={() => (bloccata ? onBloccata() : onAvvia("studio", studio))}
          >
            <BookOpenCheck className="size-4" /> Studia
          </Button>
        </div>
        <div className="flex items-center justify-between gap-2">
          {scelta(SIMULAZIONE, simulazione, setSimulazione)}
          <Button size="sm" loading={inCorso === `${banca.id}-simulazione`} onClick={() => (bloccata ? onBloccata() : onAvvia("simulazione", simulazione))}>
            <Timer className="size-4" /> Simulazione
          </Button>
        </div>
      </div>
    </Card>
  );
}
