import { nomeTipoRichiesta, TIPI_RICHIESTA, type TipoRichiesta } from "@imieiconcorsi/core/domain";
import { ChevronDown, LifeBuoy, Plus } from "lucide-react";
import { useState } from "react";
import { useLocation, useNavigate } from "react-router";
import {
  areaTesto,
  ContestoBox,
  Conversazione,
  RispondiBox,
  StatoRichiestaBadge,
  type AperturaRichiesta,
} from "../../components/Richieste";
import { Alert, Badge, Button, Card, EmptyState, PageHeader, Spinner, cx } from "../../components/ui";
import { api, useApi, type ContestoRichiesta, type RichiestaApi } from "../../lib/api";
import { messaggioErrore, useUtente } from "../../lib/auth";
import { dataOra } from "../../lib/format";

// Assistenza: l'utente registrato scrive alla piattaforma (banca dati da aggiungere, domanda
// sbagliata, problemi di accesso o di pagamento…) e legge le risposte. Si arriva qui anche dal
// link "Segnala un errore" sotto le domande, con tipo e contesto già compilati.

/** Traccia di testo da completare per un tipo di richiesta. */
const modello = (tipo: TipoRichiesta): string => TIPI_RICHIESTA.find((t) => t.id === tipo)?.modello ?? "";

/** Pagina /app/assistenza. */
export function Assistenza() {
  const location = useLocation();
  const navigate = useNavigate();
  const apertura = location.state as AperturaRichiesta | null;
  const { utente, setUtente } = useUtente();
  const { data, error, loading, setData } = useApi<{ richieste: RichiestaApi[] }>("/me/richieste");
  const [nuova, setNuova] = useState(!!apertura);
  const [aperta, setAperta] = useState<string>();

  const richieste = data?.richieste ?? [];

  function aggiorna(id: string, modifica: (r: RichiestaApi) => RichiestaApi) {
    setData((d) => d && { richieste: d.richieste.map((r) => (r.id === id ? modifica(r) : r)) });
  }

  /** Aprendo una richiesta con una risposta nuova, la si segna come letta (e cala il pallino nel menu). */
  function apri(r: RichiestaApi) {
    setAperta(aperta === r.id ? undefined : r.id);
    if (!r.daLeggere) return;
    aggiorna(r.id, (x) => ({ ...x, daLeggere: undefined }));
    setUtente({ ...utente, richiesteDaLeggere: Math.max(0, (utente.richiesteDaLeggere ?? 1) - 1) });
    void api(`/me/richieste/${r.id}/letta`, { method: "PUT" }).catch(() => {});
  }

  function creata(r: RichiestaApi) {
    setData((d) => ({ richieste: [r, ...(d?.richieste ?? [])] }));
    setNuova(false);
    setAperta(r.id);
    // Tolto lo stato del link: ricaricando la pagina il modulo non si riapre.
    navigate(location.pathname, { replace: true, state: null });
  }

  return (
    <div className="mx-auto max-w-3xl space-y-6">
      <PageHeader
        title="Assistenza"
        subtitle="Chiedi una banca dati, segnala una domanda sbagliata o un problema: ti rispondiamo qui e ti avvisiamo per email."
        actions={
          !nuova && (
            <Button onClick={() => setNuova(true)}>
              <Plus className="size-4" /> Nuova richiesta
            </Button>
          )
        }
      />

      {nuova && (
        <NuovaRichiestaForm
          tipoIniziale={apertura?.tipo}
          contesto={apertura?.contesto}
          onCreata={creata}
          onAnnulla={() => {
            setNuova(false);
            navigate(location.pathname, { replace: true, state: null });
          }}
        />
      )}

      {error && <Alert tone="error">{error.message}</Alert>}

      {loading ? (
        <Spinner label="Carico le tue richieste…" />
      ) : !richieste.length ? (
        !nuova && (
          <EmptyState icon={<LifeBuoy className="size-6" />} title="Nessuna richiesta">
            Quando ci scrivi, qui trovi la conversazione con l'assistenza.
          </EmptyState>
        )
      ) : (
        <section className="space-y-3">
          <h2 className="text-lg font-bold">Le tue richieste</h2>
          {richieste.map((r) => {
            const ultimo = r.messaggi.at(-1)!;
            return (
              <Card key={r.id} className="p-0">
                <button onClick={() => apri(r)} className="flex w-full items-start gap-3 p-4 text-left">
                  <div className="min-w-0 flex-1">
                    <div className="flex flex-wrap items-center gap-2">
                      <span className="font-semibold text-slate-900">{nomeTipoRichiesta(r.tipo)}</span>
                      <StatoRichiestaBadge stato={r.stato} />
                      {r.daLeggere && <Badge tone="green">Nuova risposta</Badge>}
                    </div>
                    <p className="mt-1 truncate text-sm text-slate-500">
                      {ultimo.da === "assistenza" ? "Assistenza: " : ""}
                      {ultimo.testo}
                    </p>
                    <p className="mt-1 text-xs text-slate-400">Aggiornata il {dataOra(r.aggiornataIl)}</p>
                  </div>
                  <ChevronDown className={cx("mt-1 size-4 shrink-0 text-slate-400 transition", aperta === r.id && "rotate-180")} />
                </button>
                {aperta === r.id && (
                  <div className="space-y-4 border-t border-slate-100 p-4">
                    <ContestoBox contesto={r.contesto} />
                    <Conversazione messaggi={r.messaggi} io="utente" />
                    <RispostaUtente richiesta={r} onInviato={(m) => aggiorna(r.id, (x) => ({ ...x, ...m }))} />
                  </div>
                )}
              </Card>
            );
          })}
        </section>
      )}
    </div>
  );
}

/** Casella per aggiungere un messaggio a una richiesta (una chiusa si riapre). */
function RispostaUtente({ richiesta, onInviato }: { richiesta: RichiestaApi; onInviato: (r: Partial<RichiestaApi>) => void }) {
  const [errore, setErrore] = useState<string>();

  async function invia(testo: string) {
    setErrore(undefined);
    try {
      await api(`/me/richieste/${richiesta.id}/messaggi`, { method: "POST", body: { testo } });
      const il = new Date().toISOString();
      // Una richiesta chiusa si riapre con il nuovo messaggio (come fa il server).
      onInviato({
        messaggi: [...richiesta.messaggi, { da: "utente", testo, il }],
        stato: richiesta.stato === "chiusa" ? "aperta" : richiesta.stato,
        aggiornataIl: il,
      });
      return true;
    } catch (err) {
      setErrore(messaggioErrore(err));
      return false;
    }
  }

  return (
    <div className="space-y-2">
      {errore && <Alert tone="error">{errore}</Alert>}
      <RispondiBox
        invia={invia}
        placeholder={richiesta.stato === "chiusa" ? "La richiesta è chiusa: scrivendo la riapri." : "Aggiungi un messaggio…"}
      />
    </div>
  );
}

/** Modulo di una nuova richiesta: tipo, traccia da completare, contesto allegato. */
function NuovaRichiestaForm({
  tipoIniziale,
  contesto,
  onCreata,
  onAnnulla,
}: {
  tipoIniziale?: TipoRichiesta;
  contesto?: ContestoRichiesta;
  onCreata: (r: RichiestaApi) => void;
  onAnnulla: () => void;
}) {
  const [tipo, setTipo] = useState<TipoRichiesta | undefined>(tipoIniziale);
  const [testo, setTesto] = useState(tipoIniziale ? modello(tipoIniziale) : "");
  const [invio, setInvio] = useState(false);
  const [errore, setErrore] = useState<string>();

  /** Cambiando tipo, il testo diventa la traccia del nuovo tipo, se non è già stato scritto altro. */
  function scegli(nuovo: TipoRichiesta) {
    if (!testo.trim() || (tipo && testo === modello(tipo))) setTesto(modello(nuovo));
    setTipo(nuovo);
  }

  async function invia() {
    if (!tipo) return;
    setInvio(true);
    setErrore(undefined);
    try {
      onCreata(await api<RichiestaApi>("/me/richieste", { method: "POST", body: { tipo, testo: testo.trim(), contesto } }));
    } catch (err) {
      setErrore(messaggioErrore(err));
    } finally {
      setInvio(false);
    }
  }

  // Il testo conta solo se l'utente ha scritto qualcosa oltre la traccia.
  const scritto = !!tipo && testo.trim().length >= 10 && testo !== modello(tipo);

  return (
    <Card className="animate-fade-up space-y-4">
      <div>
        <h2 className="font-bold text-slate-900">Di cosa hai bisogno?</h2>
        <div className="mt-3 flex flex-wrap gap-2">
          {TIPI_RICHIESTA.map((t) => (
            <button
              key={t.id}
              onClick={() => scegli(t.id)}
              className={cx(
                "rounded-full px-3 py-1.5 text-sm font-semibold transition",
                tipo === t.id ? "bg-brand-600 text-white" : "bg-white text-slate-600 ring-1 ring-slate-200 hover:ring-slate-300",
              )}
            >
              {t.nome}
            </button>
          ))}
        </div>
      </div>

      {tipo && (
        <>
          <ContestoBox contesto={contesto} />
          <label className="block">
            <span className="mb-1.5 block text-sm font-medium text-slate-700">Il tuo messaggio</span>
            <textarea
              value={testo}
              onChange={(e) => setTesto(e.target.value)}
              rows={7}
              maxLength={3000}
              autoFocus
              placeholder="Raccontaci cosa ti serve…"
              className={areaTesto}
            />
            <span className="mt-1 block text-xs text-slate-500">Completa le righe della traccia: ci aiutano a risponderti prima. Non scrivere password o dati della carta.</span>
          </label>
        </>
      )}

      {errore && <Alert tone="error">{errore}</Alert>}

      <div className="flex justify-end gap-2">
        <Button variant="ghost" onClick={onAnnulla}>
          Annulla
        </Button>
        <Button loading={invio} disabled={!scritto} onClick={() => void invia()}>
          Invia la richiesta
        </Button>
      </div>
    </Card>
  );
}
