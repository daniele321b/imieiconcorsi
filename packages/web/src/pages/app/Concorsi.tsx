import { COMPARTI, type CompartoId } from "@imieiconcorsi/core/domain";
import { Search, SearchX } from "lucide-react";
import { useMemo, useState } from "react";
import { ConcorsoCard } from "../../components/ConcorsoCard";
import { Alert, Button, EmptyState, PageHeader, Spinner, UpgradeBanner, cx } from "../../components/ui";
import { api, ApiError, useApi, type ConcorsoApi } from "../../lib/api";
import { useUtente } from "../../lib/auth";

const PAGINA = 30;

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

export function Concorsi() {
  const { utente } = useUtente();
  const [comparto, setComparto] = useState<CompartoId | "miei">("miei");
  const [testo, setTesto] = useState("");
  const [mostrati, setMostrati] = useState(PAGINA);

  const { data, loading, error, setData } = useApi<{ concorsi: ConcorsoApi[] }>(
    comparto === "miei" ? "/concorsi" : `/concorsi?comparto=${comparto}`,
  );
  const { segui, inCorso, errore, chiudiErrore } = useSegui((id, seguito) =>
    setData((d) => d && { concorsi: d.concorsi.map((c) => (c.id === id ? { ...c, seguito } : c)) }),
  );

  const filtrati = useMemo(() => {
    const q = testo.trim().toLowerCase();
    if (!q) return data?.concorsi ?? [];
    return (data?.concorsi ?? []).filter((c) =>
      [c.titolo, c.ente, c.figura, ...c.sedi].some((s) => s?.toLowerCase().includes(q)),
    );
  }, [data, testo]);

  const chips: { id: CompartoId | "miei"; nome: string }[] = [
    { id: "miei", nome: "I miei interessi" },
    ...COMPARTI.filter((c) => c.id !== "altro" || utente.interessi.includes("altro")),
  ];

  return (
    <div>
      <PageHeader title="Concorsi aperti" subtitle="Tutti i bandi di inPA con la scadenza ancora aperta, aggiornati ogni mattina." />

      <div className="sticky top-16 z-20 -mx-4 space-y-3 bg-slate-50/90 px-4 py-3 backdrop-blur sm:-mx-6 sm:px-6">
        <label className="relative block">
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
              {filtrati.length} {filtrati.length === 1 ? "bando" : "bandi"}, in ordine di scadenza
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
          </EmptyState>
        )}
      </div>
    </div>
  );
}
