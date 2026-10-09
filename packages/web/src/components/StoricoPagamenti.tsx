import { periodo as durata, PIANI } from "@imieiconcorsi/core/domain";
import { LifeBuoy, Receipt } from "lucide-react";
import { useEffect, useRef, useState } from "react";
import { Link, useLocation } from "react-router";
import { useApi, type PagamentoApi } from "../lib/api";
import { data, euro } from "../lib/format";
import type { AperturaRichiesta } from "./Richieste";
import { Alert, Badge, Card, Spinner } from "./ui";

// Profilo → "I tuoi pagamenti": gli acquisti dell'utente (GET /me/ordini), dal più recente.
// Si vedono quelli pagati; i tentativi non completati (pagina di pagamento chiusa, pagamento
// rifiutato) si aprono a parte. La ricevuta la manda Stripe per email.

const STATI: Record<PagamentoApi["stato"], { nome: string; tone: "green" | "amber" | "slate" | "red" }> = {
  pagato: { nome: "Pagato", tone: "green" },
  "in-attesa": { nome: "In attesa", tone: "amber" },
  scaduto: { nome: "Non completato", tone: "slate" },
  fallito: { nome: "Non riuscito", tone: "red" },
};

/** Storico dei pagamenti dell'utente, con il link all'assistenza per ogni ordine. */
export function StoricoPagamenti() {
  const { data: risposta, loading, error } = useApi<{ ordini: PagamentoApi[] }>("/me/ordini");
  const [tutti, setTutti] = useState(false);
  const { hash } = useLocation();
  const sezione = useRef<HTMLElement>(null);

  // Arrivati da "I tuoi pagamenti" (pagina Piani): si scende fin qui quando la lista è pronta.
  useEffect(() => {
    if (hash === "#pagamenti" && !loading) sezione.current?.scrollIntoView({ behavior: "smooth" });
  }, [hash, loading]);

  const ordini = risposta?.ordini ?? [];
  const pagati = ordini.filter((o) => o.stato === "pagato");
  const altri = ordini.length - pagati.length;
  const mostrati = tutti ? ordini : pagati;

  return (
    <section id="pagamenti" ref={sezione} className="scroll-mt-24 space-y-3">
      <h2 className="flex items-center gap-2 text-lg font-bold">
        <Receipt className="size-5 text-brand-600" /> I tuoi pagamenti
      </h2>
      <p className="text-sm text-slate-500">La ricevuta di ogni pagamento te la manda Stripe per email. Per la fattura o un problema, scrivici dall'ordine.</p>

      {error && <Alert tone="error">{error.message}</Alert>}
      {loading ? (
        <Spinner label="Carico i pagamenti…" />
      ) : !mostrati.length ? (
        <p className="text-sm text-slate-500">{ordini.length ? "Nessun pagamento completato." : "Non hai ancora fatto acquisti."}</p>
      ) : (
        <div className="space-y-2">
          {mostrati.map((o) => {
            const stato = STATI[o.stato];
            const apertura: AperturaRichiesta = { tipo: "pagamento", contesto: { ordineId: o.id } };
            return (
              <Card key={o.id} className="flex flex-wrap items-center gap-x-4 gap-y-2 p-4">
                <div className="min-w-0 flex-1">
                  <p className="font-semibold text-slate-900">
                    {PIANI[o.piano].nome} · {durata(o.periodo).nome}
                  </p>
                  <p className="text-xs text-slate-500">
                    {data(o.pagatoIl ?? o.creatoIl)}
                    {o.scadenzaPiano && o.stato === "pagato" && ` · valido fino al ${data(o.scadenzaPiano)}`} · ordine{" "}
                    <span className="font-mono">{o.id}</span>
                  </p>
                </div>
                <div className="text-right">
                  <p className="font-bold text-slate-900">{euro(o.importo)}</p>
                  {o.codiceSconto && (
                    <p className="text-xs text-slate-500">
                      <s>{euro(o.prezzo)}</s> · {o.codiceSconto} −{o.percentualeSconto}%
                    </p>
                  )}
                </div>
                <Badge tone={stato.tone}>{stato.nome}</Badge>
                <Link
                  to="/app/assistenza"
                  state={apertura}
                  className="inline-flex items-center gap-1 text-xs font-semibold text-slate-400 hover:text-brand-700"
                  title="Apri una richiesta di assistenza su questo ordine"
                >
                  <LifeBuoy className="size-3.5" /> Aiuto
                </Link>
              </Card>
            );
          })}
        </div>
      )}

      {altri > 0 && (
        <button onClick={() => setTutti((t) => !t)} className="text-sm font-semibold text-brand-600 hover:text-brand-700">
          {tutti ? "Mostra solo i pagamenti completati" : `Mostra anche i tentativi non completati (${altri})`}
        </button>
      )}
    </section>
  );
}
