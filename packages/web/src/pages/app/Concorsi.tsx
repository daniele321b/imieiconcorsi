import {
  filtraConcorsi,
  filtriAttivi,
  ORDINAMENTI,
  ordinaConcorsi,
  type ConcorsoInLista,
  type FiltriConcorsi,
  type Ordinamento,
} from "@imieiconcorsi/core/concorsi";
import { COMPARTI, COMPARTO_IDS, type CompartoId } from "@imieiconcorsi/core/domain";
import { ArrowUpDown, Search, SearchX, SlidersHorizontal } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { ConcorsoCard } from "../../components/ConcorsoCard";
import { FiltriConcorsiPanel } from "../../components/FiltriConcorsiPanel";
import { Alert, Button, EmptyState, PageHeader, Spinner, UpgradeBanner, cx } from "../../components/ui";
import { api, ApiError, useApi, type ConcorsoApi } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { caricaBandi } from "../../lib/bandi";

// Ricerca dei bandi (/app/concorsi): lista dalla cache su CloudFront (lib/bandi.ts), filtri,
// ordinamento, ricerca per testo e "Segui". Si mostrano 30 bandi per volta.

/** Bandi mostrati per volta ("Mostra altri"). */
const PAGINA = 30;

/** Segui / smetti di seguire un concorso, con l'errore del limite del piano (usato anche nel dettaglio). */
export function useSegui(onCambio: (id: string, seguito: boolean) => void) {
  const [inCorso, setInCorso] = useState<string>();
  const [errore, setErrore] = useState<ApiError>();

  async function segui(c: { id: string; seguito: boolean }) {
    setInCorso(c.id);
    setErrore(undefined);
    try {
      await api(`/me/concorsi/${c.id}`, { method: c.seguito ? "DELETE" : "PUT" });
      onCambio(c.id, !c.seguito);
    } catch (err) {
      setErrore(err instanceof ApiError ? err : new ApiError(0, "Errore di rete"));
    } finally {
      setInCorso(undefined);
    }
  }
  return { segui, inCorso, errore, chiudiErrore: () => setErrore(undefined) };
}

/** Pagina /app/concorsi. */
export function Concorsi() {
  const [comparto, setComparto] = useState<CompartoId | "miei" | "tutti">("miei");
  const [testo, setTesto] = useState("");
  const [ordine, setOrdine] = useState<Ordinamento>("scadenza");
  const [filtri, setFiltri] = useState<FiltriConcorsi>({});
  const [pannello, setPannello] = useState(false);
  const [mostrati, setMostrati] = useState(PAGINA);

  const { utente } = useUtente();
  // Tutti i bandi, aperti e chiusi: le caselle Aperti/Chiusi nei filtri scelgono cosa vedere.
  const comparti = useMemo<readonly CompartoId[]>(
    () => (comparto === "tutti" ? COMPARTO_IDS : comparto === "miei" ? (utente.interessi.length ? utente.interessi : COMPARTO_IDS) : [comparto]),
    [comparto, utente.interessi],
  );
  const [bandi, setBandi] = useState<ConcorsoInLista[]>();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<ApiError>();
  useEffect(() => {
    let attuale = true;
    setLoading(true);
    setError(undefined);
    caricaBandi(comparti)
      .then((b) => attuale && setBandi(b))
      .catch(() => attuale && setError(new ApiError(0, "Non riesco a caricare i bandi: riprova tra poco.")))
      .finally(() => attuale && setLoading(false));
    return () => {
      attuale = false;
    };
  }, [comparti]);

  // Quali segui: dall'API (la lista in cache è uguale per tutti).
  const seguitiApi = useApi<{ concorsi: ConcorsoApi[] }>("/me/concorsi");
  const [seguiti, setSeguiti] = useState<Set<string>>(new Set());
  useEffect(() => {
    if (seguitiApi.data) setSeguiti(new Set(seguitiApi.data.concorsi.map((c) => c.id)));
  }, [seguitiApi.data]);
  const { segui, inCorso, errore, chiudiErrore } = useSegui((id, seguito) =>
    setSeguiti((s) => {
      const nuovi = new Set(s);
      if (seguito) nuovi.add(id);
      else nuovi.delete(id);
      return nuovi;
    }),
  );
  const data = useMemo(() => bandi && { concorsi: bandi.map((c) => ({ ...c, seguito: seguiti.has(c.id) })) }, [bandi, seguiti]);

  const filtrati = useMemo(() => {
    const q = testo.trim().toLowerCase();
    const trovati = q
      ? (data?.concorsi ?? []).filter((c) => [c.titolo, c.ente, c.figura, ...c.sedi].some((s) => s?.toLowerCase().includes(q)))
      : (data?.concorsi ?? []);
    return ordinaConcorsi(filtraConcorsi(trovati, filtri), ordine);
  }, [data, testo, ordine, filtri]);

  const procedure = useMemo(
    () => [...new Set((data?.concorsi ?? []).map((c) => c.tipoProcedura).filter((p): p is string => !!p))].sort(),
    [data],
  );
  const attivi = filtriAttivi(filtri);

  // "Tutti" cerca su ogni comparto, anche quelli che non segui.
  const chips: { id: CompartoId | "miei" | "tutti"; nome: string }[] = [
    { id: "miei", nome: "I miei interessi" },
    { id: "tutti", nome: "Tutti i bandi" },
    ...COMPARTI,
  ];

  return (
    <div>
      <PageHeader
        title="Concorsi"
        subtitle="I bandi di inPA, aperti e con le domande chiuse, aggiornati ogni mattina. Dai Filtri scegli se vedere solo gli aperti o solo i chiusi."
      />

      <div className="sticky top-16 z-20 -mx-4 space-y-3 bg-slate-50/90 px-4 py-3 backdrop-blur sm:-mx-6 sm:px-6">
        <div className="flex flex-col gap-3 sm:flex-row">
          <label className="relative block flex-1">
            <Search className="pointer-events-none absolute top-1/2 left-3.5 size-4 -translate-y-1/2 text-slate-400" />
            <input
              value={testo}
              onChange={(e) => {
                setTesto(e.target.value);
                setMostrati(PAGINA);
              }}
              placeholder="Cerca per ente, profilo o città…"
              className="h-12 w-full rounded-xl border-0 bg-white pr-4 pl-10 shadow-sm ring-1 ring-slate-200 focus:ring-2 focus:ring-brand-500 focus:outline-none"
            />
          </label>
          <label className="relative block sm:w-60">
            <span className="sr-only">Ordina per</span>
            <ArrowUpDown className="pointer-events-none absolute top-1/2 left-3.5 size-4 -translate-y-1/2 text-slate-400" />
            <select
              value={ordine}
              onChange={(e) => {
                setOrdine(e.target.value as Ordinamento);
                setMostrati(PAGINA);
              }}
              className="h-12 w-full appearance-none rounded-xl border-0 bg-white pr-4 pl-10 text-sm font-medium text-slate-700 shadow-sm ring-1 ring-slate-200 focus:ring-2 focus:ring-brand-500 focus:outline-none"
            >
              {ORDINAMENTI.map((o) => (
                <option key={o.id} value={o.id}>
                  Ordina: {o.nome.toLowerCase()}
                </option>
              ))}
            </select>
          </label>
          <Button
            variant={attivi ? "primary" : "secondary"}
            className="h-12 shrink-0"
            onClick={() => setPannello((p) => !p)}
            aria-expanded={pannello}
          >
            <SlidersHorizontal className="size-4" /> Filtri{attivi ? ` (${attivi})` : ""}
          </Button>
        </div>
        {pannello && (
          <div className="space-y-2">
            <FiltriConcorsiPanel
              value={filtri}
              procedure={procedure}
              onChange={(f) => {
                setFiltri(f);
                setMostrati(PAGINA);
              }}
            />
            {attivi > 0 && (
              <button onClick={() => setFiltri({})} className="text-sm font-semibold text-brand-600 hover:text-brand-700">
                Azzera i filtri
              </button>
            )}
          </div>
        )}
        <div className="-mx-1 flex gap-2 overflow-x-auto px-1 pb-1">
          {chips.map((c) => (
            <button
              key={c.id}
              onClick={() => {
                setComparto(c.id);
                setMostrati(PAGINA);
              }}
              className={cx(
                "shrink-0 rounded-full px-3.5 py-1.5 text-sm font-semibold transition",
                comparto === c.id ? "bg-brand-600 text-white" : "bg-white text-slate-600 ring-1 ring-slate-200 hover:ring-slate-300",
              )}
            >
              {c.nome}
            </button>
          ))}
        </div>
      </div>

      <div className="mt-4 space-y-4">
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
          <Spinner label="Carico i bandi…" />
        ) : filtrati.length ? (
          <>
            <p className="text-sm text-slate-500">
              {filtrati.length} {filtrati.length === 1 ? "bando" : "bandi"}
              {filtri.aperti === false ? " con le domande chiuse" : filtri.chiusi === false ? " aperti" : ""}, ordinati per{" "}
              {
                {
                  scadenza: "scadenza più vicina",
                  pubblicazione: "data di uscita, dai più recenti",
                  "piu-posti": "numero di posti, dai più numerosi",
                  "meno-posti": "numero di posti, dai meno numerosi",
                }[ordine]
              }
            </p>
            <div className="grid gap-4 md:grid-cols-2">
              {filtrati.slice(0, mostrati).map((c) => (
                <ConcorsoCard key={c.id} concorso={c} onSegui={(x) => void segui(x)} inCorso={inCorso === c.id} />
              ))}
            </div>
            {mostrati < filtrati.length && (
              <div className="flex justify-center pt-2">
                <Button variant="secondary" onClick={() => setMostrati((n) => n + PAGINA)}>
                  Mostra altri {Math.min(PAGINA, filtrati.length - mostrati)}
                </Button>
              </div>
            )}
          </>
        ) : (
          <EmptyState icon={<SearchX className="size-6" />} title="Nessun bando trovato">
            Prova a cambiare comparto o a cercare un'altra parola.
            {(filtri.aperti === false || filtri.chiusi === false) && (
              <>
                {" "}
                <button
                  onClick={() => setFiltri((f) => ({ ...f, aperti: undefined, chiusi: undefined }))}
                  className="font-semibold text-brand-600 hover:text-brand-700"
                >
                  Mostra aperti e chiusi
                </button>
                .
              </>
            )}
          </EmptyState>
        )}
      </div>
    </div>
  );
}
