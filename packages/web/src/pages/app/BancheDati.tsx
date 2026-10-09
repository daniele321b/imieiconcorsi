import { COMPARTI, nomeMateria, type CompartoId, type MateriaId, type SelezioneBanca } from "@imieiconcorsi/core/domain";
import { BookOpenCheck, Database, Eye, RotateCcw, Timer } from "lucide-react";
import { useState } from "react";
import { Link } from "react-router";
import { OrdineRisposte } from "../../components/OrdineRisposte";
import { Alert, Badge, Button, ButtonLink, Card, EmptyState, PageHeader, ProgressBar, Spinner, UpgradeBanner, cx } from "../../components/ui";
import { api, useApi } from "../../lib/api";
import { useAvviaSessione } from "../../lib/sessioni";

interface BancaApi {
  id: string;
  titolo: string;
  comparto: CompartoId;
  anno?: number;
  materia?: MateriaId;
  domande: number;
  /** Concorsi collegati: la scheda li elenca con il link al bando */
  concorsi: { id: string; titolo: string }[];
  /** Domande già fatte e sbagliate l'ultima volta; assente = mai iniziata */
  progresso?: { fatte: number; sbagliate: number };
}

/** Utilizzi del piano Free nella settimana; null = illimitati. */
export interface UsiApi {
  limite: number;
  usati: number;
  restanti: number;
  aperte: string[];
}

/** Domande per una sessione di studio e per una simulazione, tra cui scegliere. */
const STUDIO = [10, 20, 30] as const;
const SIMULAZIONE = [30, 60] as const;

// Banche dati ufficiali per comparto, anche slegate dai concorsi (es. "Polizia di Stato 2026").
// Medium e Pro senza limiti; il Free ha USI_BANCHE_DATI_FREE utilizzi a settimana.
export function BancheDati() {
  const { data, loading, error, reload } = useApi<{ banche: BancaApi[]; usi: UsiApi | null }>("/banche-dati");
  const { avvia, inCorso, errore, chiudiErrore } = useAvviaSessione();
  const usi = data?.usi;

  const perComparto = COMPARTI.map((c) => ({ ...c, banche: (data?.banche ?? []).filter((b) => b.comparto === c.id) })).filter((c) => c.banche.length);

  return (
    <div>
      <PageHeader
        title="Banche dati ufficiali"
        subtitle="Le domande pubblicate dagli enti per le prove dei concorsi, divise per comparto. Consultale una per una, studia con la correzione subito o fai una simulazione a tempo."
      />

      <div className="space-y-4">
        <div className="rounded-2xl bg-white p-4 ring-1 ring-slate-200">
          <OrdineRisposte />
          <p className="mt-2 text-xs text-slate-500">
            Molti PDF ufficiali mettono la risposta giusta sempre in A: mescolata impari la risposta, non la lettera. Vale per
            consultazione, studio e simulazioni.
          </p>
        </div>
        {usi && (
          <Alert tone={usi.restanti ? "info" : "error"}>
            Piano Free: {usi.restanti === 1 ? "ti resta 1 utilizzo" : `ti restano ${usi.restanti} utilizzi`} su {usi.limite}{" "}
            questa settimana (ripartono lunedì). Un utilizzo = una sessione, oppure la prima consultazione di una banca dati
            nella settimana. Con Medium e Pro sono illimitati.
          </Alert>
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
                    giaAperta={!!usi?.aperte.includes(b.id)}
                    inCorso={inCorso}
                    onAvvia={(tipo, numero, selezione) => void avvia({ tipo, bancaDatiId: b.id, numero, selezione }, `${b.id}-${tipo}`).then(() => reload())}
                    onRicomincia={() => void api(`/me/progressi/${b.id}`, { method: "DELETE" }).then(() => reload())}
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

/** Concorsi per cui vale la banca dati: i primi due, gli altri si aprono con "e altri N". */
function ConcorsiCollegati({ concorsi }: { concorsi: BancaApi["concorsi"] }) {
  const [tutti, setTutti] = useState(false);
  const mostrati = tutti ? concorsi : concorsi.slice(0, 2);
  return (
    <div className="mt-1 space-y-0.5 text-xs text-slate-500">
      <p className="font-semibold">{concorsi.length === 1 ? "Concorso" : `Vale per ${concorsi.length} concorsi`}:</p>
      {mostrati.map((c) => (
        <Link key={c.id} to={`/app/concorsi/${c.id}`} className="block truncate hover:text-brand-700">
          {c.titolo}
        </Link>
      ))}
      {concorsi.length > 2 && (
        <button onClick={() => setTutti((t) => !t)} className="font-semibold text-brand-600 hover:text-brand-700">
          {tutti ? "Mostra meno" : `e altri ${concorsi.length - 2}`}
        </button>
      )}
    </div>
  );
}

/** Scheda di una banca dati: dati, progressi, consultazione, studio e simulazione. */
function SchedaBanca({
  banca,
  giaAperta,
  inCorso,
  onAvvia,
  onRicomincia,
}: {
  banca: BancaApi;
  /** Free: già consultata questa settimana, consultarla di nuovo non costa */
  giaAperta: boolean;
  inCorso?: string;
  onAvvia: (tipo: "studio" | "simulazione", numero: number, selezione: SelezioneBanca) => void;
  onRicomincia: () => void;
}) {
  const [studio, setStudio] = useState<number>(STUDIO[0]);
  const [simulazione, setSimulazione] = useState<number>(SIMULAZIONE[1]);
  const [selezione, setSelezione] = useState<SelezioneBanca>("nuove");
  const p = banca.progresso;
  // Finite le domande da ripassare, si torna alle nuove.
  const sel: SelezioneBanca = selezione === "sbagliate" && !p?.sbagliate ? "nuove" : selezione;
  const percentuale = p && banca.domande ? Math.round((p.fatte / banca.domande) * 100) : 0;

  function scelta<T extends string | number>(opzioni: readonly { id: T; nome: string; disabled?: boolean }[], valore: T, set: (v: T) => void) {
    return (
      <div className="inline-grid rounded-lg bg-slate-100 p-0.5 text-xs font-semibold" style={{ gridTemplateColumns: `repeat(${opzioni.length}, auto)` }}>
        {opzioni.map((o) => (
          <button
            key={o.id}
            onClick={() => set(o.id)}
            disabled={o.disabled}
            className={cx(
              "rounded-md px-2.5 py-1 transition disabled:opacity-40",
              valore === o.id ? "bg-white text-brand-700 shadow-sm" : "text-slate-500",
            )}
          >
            {o.nome}
          </button>
        ))}
      </div>
    );
  }
  const numeri = (n: readonly number[]) => n.map((x) => ({ id: x, nome: String(x) }));

  return (
    <Card className="flex flex-col">
      <div className="flex items-start gap-3">
        <span className="grid size-10 shrink-0 place-items-center rounded-xl bg-brand-50 text-brand-600">
          <Database className="size-5" />
        </span>
        <div className="min-w-0 flex-1">
          <p className="font-bold text-slate-900">{banca.titolo}</p>
          <div className="mt-1 flex flex-wrap gap-1.5">
            {banca.anno && <Badge>{banca.anno}</Badge>}
            <Badge tone="brand">{banca.domande.toLocaleString("it-IT")} domande</Badge>
            {banca.materia && <Badge>{nomeMateria(banca.materia)}</Badge>}
          </div>
          {banca.concorsi.length > 0 && <ConcorsiCollegati concorsi={banca.concorsi} />}
        </div>
      </div>

      {/* Domande già fatte nelle sessioni (studio e simulazioni) su questa banca dati. */}
      {p && (
        <div className="mt-4">
          <ProgressBar value={percentuale} tone="green" />
          <div className="mt-1.5 flex flex-wrap items-center justify-between gap-x-3 gap-y-1 text-xs text-slate-500">
            <span>
              <strong className="text-slate-700">{p.fatte.toLocaleString("it-IT")}</strong> di {banca.domande.toLocaleString("it-IT")} fatte ({percentuale}%)
              {p.sbagliate > 0 && (
                <>
                  {" · "}
                  <strong className="text-rose-600">{p.sbagliate.toLocaleString("it-IT")}</strong> da ripassare
                </>
              )}
            </span>
            <button
              onClick={() => window.confirm("Ricominciare da capo? Si azzerano le domande fatte e quelle da ripassare di questa banca dati.") && onRicomincia()}
              className="inline-flex items-center gap-1 font-semibold hover:text-slate-800"
            >
              <RotateCcw className="size-3" /> Ricomincia
            </button>
          </div>
        </div>
      )}

      <div className="mt-4 space-y-2 border-t border-slate-100 pt-4">
        {p && (
          <div className="flex items-center justify-between gap-2">
            <p className="text-xs text-slate-500">Quali domande</p>
            {scelta<SelezioneBanca>(
              [
                { id: "nuove", nome: "Nuove" },
                { id: "sbagliate", nome: `Da ripassare (${p.sbagliate})`, disabled: !p.sbagliate },
                { id: "tutte", nome: "Tutte" },
              ],
              sel,
              setSelezione,
            )}
          </div>
        )}
        <div className="flex items-center justify-between gap-2">
          <p className="text-xs text-slate-500">{giaAperta ? "Già aperta questa settimana" : "Domanda per domanda, con la risposta"}</p>
          <ButtonLink to={`/app/banche-dati/${banca.id}`} size="sm" variant="ghost">
            <Eye className="size-4" /> Consulta
          </ButtonLink>
        </div>
        <div className="flex items-center justify-between gap-2">
          {scelta(numeri(STUDIO), studio, setStudio)}
          <Button
            size="sm"
            variant="secondary"
            loading={inCorso === `${banca.id}-studio`}
            onClick={() => onAvvia("studio", studio, sel)}
          >
            <BookOpenCheck className="size-4" /> Studia
          </Button>
        </div>
        <div className="flex items-center justify-between gap-2">
          {scelta(numeri(SIMULAZIONE), simulazione, setSimulazione)}
          <Button size="sm" loading={inCorso === `${banca.id}-simulazione`} onClick={() => onAvvia("simulazione", simulazione, sel)}>
            <Timer className="size-4" /> Simulazione
          </Button>
        </div>
      </div>
    </Card>
  );
}
