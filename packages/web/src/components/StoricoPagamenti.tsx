import { periodo as durata, PIANI } from "@imieiconcorsi/core/domain";
import { LifeBuoy, Mail, Receipt } from "lucide-react";
import { useEffect, useState } from "react";
import { Link, useLocation } from "react-router";
import { api, useApi, type PagamentoApi } from "../lib/api";
import { messaggioErrore } from "../lib/auth";
import { data, euro } from "../lib/format";
import type { AperturaRichiesta } from "./Richieste";
import { Alert, Badge, Card, Espandibile, Spinner } from "./ui";

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
  const [invio, setInvio] = useState<string>();
  const [avviso, setAvviso] = useState<{ tone: "success" | "error"; testo: string }>();

  /** Rimanda la ricevuta di un ordine pagato all'email dell'account. */
  async function rimanda(id: string) {
    setInvio(id);
    setAvviso(undefined);
    try {
      const r = await api<{ email?: string }>(`/me/ordini/${id}/ricevuta`, { method: "POST" });
      setAvviso({ tone: "success", testo: `Ricevuta inviata${r.email ? ` a ${r.email}` : ""}: se non la vedi, guarda nello spam.` });
    } catch (err) {
      setAvviso({ tone: "error", testo: messaggioErrore(err) });
    } finally {
      setInvio(undefined);
    }
  }
  const { hash } = useLocation();

  // Arrivati da "I tuoi pagamenti" (pagina Piani): sezione aperta e si scende fin qui.
  const daLink = hash === "#pagamenti";
  useEffect(() => {
    if (daLink && !loading) document.getElementById("pagamenti")?.scrollIntoView({ behavior: "smooth" });
  }, [daLink, loading]);

  const ordini = risposta?.ordini ?? [];
  const pagati = ordini.filter((o) => o.stato === "pagato");
  const altri = ordini.length - pagati.length;
  const mostrati = tutti ? ordini : pagati;

  return (
    <Espandibile
      id="pagamenti"
      titolo="I tuoi pagamenti"
      icona={<Receipt className="size-5 text-brand-600" />}
      riassunto={loading ? undefined : pagati.length === 1 ? "1 pagamento" : `${pagati.length} pagamenti`}
      aperta={daLink}
    >
      <p className="text-sm text-slate-500">Dopo ogni pagamento ti mandiamo la ricevuta per email; qui puoi farla rimandare. Per la fattura o un problema, scrivici con "Aiuto".</p>

      {error && <Alert tone="error">{error.message}</Alert>}
      {avviso && (
        <Alert tone={avviso.tone} onClose={() => setAvviso(undefined)}>
          {avviso.testo}
        </Alert>
      )}
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
              <Card key={o.id} className="space-y-2 p-4">
                <div className="flex items-start justify-between gap-3">
                  <div className="min-w-0">
                    <p className="font-semibold text-slate-900">
                      {PIANI[o.piano].nome} · {durata(o.periodo).nome}
                    </p>
                    <p className="text-xs text-slate-500">{data(o.pagatoIl ?? o.creatoIl)}</p>
                  </div>
                  <div className="shrink-0 text-right">
                    <p className="font-bold text-slate-900">{euro(o.importo)}</p>
                    {o.codiceSconto && (
                      <p className="text-xs text-slate-500">
                        <s>{euro(o.prezzo)}</s> · {o.codiceSconto} −{o.percentualeSconto}%
                      </p>
                    )}
                  </div>
                </div>
                <p className="text-xs break-all text-slate-500">
                  {o.scadenzaPiano && o.stato === "pagato" && <>Valido fino al {data(o.scadenzaPiano)} · </>}
                  ordine <span className="font-mono">{o.id}</span>
                </p>
                <div className="flex flex-wrap items-center gap-x-4 gap-y-2">
                  <Badge tone={stato.tone}>{stato.nome}</Badge>
                  {o.stato === "pagato" && (
                    <button
                      onClick={() => void rimanda(o.id)}
                      disabled={!!invio}
                      className="inline-flex items-center gap-1 text-xs font-semibold text-slate-500 hover:text-brand-700 disabled:opacity-50"
                      title="Rimanda la ricevuta alla tua email"
                    >
                      <Mail className="size-3.5" /> {invio === o.id ? "Invio…" : "Rimanda la ricevuta"}
                    </button>
                  )}
                  <Link
                    to="/app/assistenza"
                    state={apertura}
                    className="inline-flex items-center gap-1 text-xs font-semibold text-slate-500 hover:text-brand-700"
                    title="Apri una richiesta di assistenza su questo ordine"
                  >
                    <LifeBuoy className="size-3.5" /> Aiuto
                  </Link>
                </div>
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
    </Espandibile>
  );
}
