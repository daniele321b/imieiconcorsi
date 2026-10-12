import { COMPARTI, nomeMateria, type CompartoId, type MateriaId, type SelezioneBanca } from "@imieiconcorsi/core/domain";
import { ArrowLeft, BookOpenCheck, ChevronDown, Database, Eye, RotateCcw, Star, Timer } from "lucide-react";
import { useState } from "react";
import { Link } from "react-router";
import { NumeroAMano } from "../../components/NumeroDomande";
import { OrdineRisposte } from "../../components/OrdineRisposte";
import { Alert, Badge, Button, Card, EmptyState, PageHeader, ProgressBar, Spinner, UpgradeBanner, cx } from "../../components/ui";
import { api, useApi } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { useAvviaSessione } from "../../lib/sessioni";

interface BancaApi {
  id: string;
  titolo: string;
  comparto: CompartoId;
  anno?: number;
  materia?: MateriaId;
  domande: number;
  /** Concorsi collegati: la scheda li elenca con il link al bando */
  concorsi: { id: string; titolo: string; ente?: string }[];
  /** Domande già fatte e sbagliate l'ultima volta; assente = mai iniziata */
  progresso?: { fatte: number; sbagliate: number; preferite: number };
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
  const { utente } = useUtente();
  const usi = data?.usi;

  const perComparto = COMPARTI.map((c) => ({ ...c, banche: (data?.banche ?? []).filter((b) => b.comparto === c.id) })).filter((c) => c.banche.length);

  return (
    <div>
      <Link to="/app/studio" className="mb-4 inline-flex items-center gap-1 text-sm font-semibold text-slate-500 hover:text-slate-800">
        <ArrowLeft className="size-4" /> Studio
      </Link>
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
                    maxSimulazione={utente.limiti.domandePerSimulazione}
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
        <Link key={c.id} to={`/app/concorsi/${c.id}`} className="block break-words hover:text-brand-700">
          <span className="font-semibold text-slate-700">{c.titolo}</span>
          {c.ente && <span> · {c.ente}</span>}
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

/** Cosa fare con una banca dati, dopo averla aperta. */
type Modo = "studio" | "simulazione";

/**
 * Scheda di una banca dati: dati e progressi. Toccandola si aprono le tre scelte (Consulta,
 * Studia, Simulazione); scelto Studia o Simulazione si decide quali domande e quante, poi si parte.
 */
function SchedaBanca({
  banca,
  giaAperta,
  inCorso,
  maxSimulazione,
  onAvvia,
  onRicomincia,
}: {
  banca: BancaApi;
  /** Free: già consultata questa settimana, consultarla di nuovo non costa */
  giaAperta: boolean;
  inCorso?: string;
  /** Domande massime di una simulazione per il piano (il Pro ne sceglie a mano fino a 100) */
  maxSimulazione: number;
  onAvvia: (tipo: Modo, numero: number, selezione: SelezioneBanca) => void;
  onRicomincia: () => void;
}) {
  const [aperta, setAperta] = useState(false);
  const [modo, setModo] = useState<Modo>();
  const [studio, setStudio] = useState<number>(STUDIO[0]);
  // undefined: numero scritto a mano non (ancora) valido.
  const [simulazione, setSimulazione] = useState<number | undefined>(SIMULAZIONE[1]);
  const [selezione, setSelezione] = useState<SelezioneBanca>("nuove");
  const p = banca.progresso;
  // Finite le domande da ripassare (o tolte tutte le preferite), si torna alle nuove.
  const sel: SelezioneBanca = (selezione === "sbagliate" && !p?.sbagliate) || (selezione === "preferite" && !p?.preferite) ? "nuove" : selezione;
  const percentuale = p && banca.domande ? Math.round((p.fatte / banca.domande) * 100) : 0;
  const numero = modo === "studio" ? studio : simulazione;

  function scelta<T extends string | number>(opzioni: readonly { id: T; nome: string; disabled?: boolean }[], valore: T | undefined, set: (v: T) => void) {
    return (
      <div className="inline-flex flex-wrap gap-0.5 rounded-lg bg-slate-200/70 p-0.5 text-xs font-semibold">
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
  const riquadro = "flex flex-col items-center gap-1 rounded-xl px-2 py-3 text-center text-sm font-semibold ring-1 transition";

  return (
    <Card className="flex flex-col">
      <button
        type="button"
        onClick={() => {
          setAperta((a) => !a);
          setModo(undefined);
        }}
        aria-expanded={aperta}
        className="flex items-start gap-3 text-left"
      >
        <span className="grid size-10 shrink-0 place-items-center rounded-xl bg-brand-50 text-brand-600">
          <Database className="size-5" />
        </span>
        <span className="min-w-0 flex-1">
          <span className="block font-bold break-words text-slate-900">{banca.titolo}</span>
          <span className="mt-1 flex flex-wrap gap-1.5">
            {banca.anno && <Badge>{banca.anno}</Badge>}
            <Badge tone="brand">{banca.domande.toLocaleString("it-IT")} domande</Badge>
            {banca.materia && <Badge>{nomeMateria(banca.materia)}</Badge>}
          </span>
        </span>
        <ChevronDown className={cx("mt-1 size-5 shrink-0 text-slate-400 transition", aperta && "rotate-180")} />
      </button>
      {banca.concorsi.length > 0 && (
        <div className="pl-13">
          <ConcorsiCollegati concorsi={banca.concorsi} />
        </div>
      )}

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
              {p.preferite > 0 && (
                <>
                  {" · "}
                  <Link to={`/app/banche-dati/${banca.id}?preferite=1`} className="inline-flex items-center gap-0.5 font-semibold text-amber-700 hover:underline">
                    <Star className="size-3 fill-amber-400 text-amber-500" /> {p.preferite} preferite
                  </Link>
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

      {!aperta ? (
        <button
          type="button"
          onClick={() => setAperta(true)}
          className="mt-4 rounded-xl bg-brand-50 py-2.5 text-sm font-semibold text-brand-700 transition hover:bg-brand-100"
        >
          Consulta, studia o fai una simulazione
        </button>
      ) : (
        <div className="mt-4 animate-fade-up space-y-3 border-t border-slate-100 pt-4">
          <div className="grid grid-cols-3 gap-2">
            <Link to={`/app/banche-dati/${banca.id}`} className={cx(riquadro, "text-slate-700 ring-slate-200 hover:bg-slate-50")}>
              <Eye className="size-5 text-brand-600" /> Consulta
              <span className="text-[11px] font-normal text-slate-500">{giaAperta ? "Già aperta questa settimana" : "Una per una, con la risposta"}</span>
            </Link>
            {(
              [
                { id: "studio", nome: "Studia", Icon: BookOpenCheck, sotto: "Correzione subito" },
                { id: "simulazione", nome: "Simulazione", Icon: Timer, sotto: "A tempo, come la prova" },
              ] as const
            ).map((m) => (
              <button
                key={m.id}
                type="button"
                aria-pressed={modo === m.id}
                onClick={() => setModo(modo === m.id ? undefined : m.id)}
                className={cx(riquadro, modo === m.id ? "bg-brand-600 text-white ring-brand-600" : "text-slate-700 ring-slate-200 hover:bg-slate-50")}
              >
                <m.Icon className={cx("size-5", modo === m.id ? "text-white" : "text-brand-600")} /> {m.nome}
                <span className={cx("text-[11px] font-normal", modo === m.id ? "text-brand-100" : "text-slate-500")}>{m.sotto}</span>
              </button>
            ))}
          </div>

          {modo && (
            <div className="animate-fade-up space-y-3 rounded-xl bg-slate-50 p-3">
              {p && (
                <div className="space-y-1.5">
                  <p className="text-xs font-semibold text-slate-500">Quali domande</p>
                  {scelta<SelezioneBanca>(
                    [
                      { id: "nuove", nome: "Nuove" },
                      { id: "sbagliate", nome: `Da ripassare (${p.sbagliate})`, disabled: !p.sbagliate },
                      { id: "preferite", nome: `Preferite (${p.preferite})`, disabled: !p.preferite },
                      { id: "tutte", nome: "Tutte" },
                    ],
                    sel,
                    setSelezione,
                  )}
                </div>
              )}
              <div className="space-y-1.5">
                <p className="text-xs font-semibold text-slate-500">Quante domande</p>
                <div className="flex flex-wrap items-center gap-x-3 gap-y-2">
                  {modo === "studio" ? scelta(numeri(STUDIO), studio, setStudio) : scelta(numeri(SIMULAZIONE), simulazione, setSimulazione)}
                  {modo === "simulazione" && maxSimulazione > Math.max(...SIMULAZIONE) && (
                    <NumeroAMano valore={simulazione} onChange={setSimulazione} max={maxSimulazione} fissi={SIMULAZIONE} />
                  )}
                </div>
              </div>
              <Button
                className="w-full"
                disabled={!numero}
                loading={inCorso === `${banca.id}-${modo}`}
                onClick={() => numero && onAvvia(modo, numero, sel)}
              >
                {modo === "studio" ? (
                  <>
                    <BookOpenCheck className="size-4" /> Inizia lo studio
                  </>
                ) : (
                  <>
                    <Timer className="size-4" /> Inizia la simulazione
                  </>
                )}
              </Button>
            </div>
          )}
        </div>
      )}
    </Card>
  );
}
