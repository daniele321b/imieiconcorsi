import { periodo as durata, PIANI, type Periodo } from "@imieiconcorsi/core/domain";
import { ArrowLeft, Copy, Receipt, Search } from "lucide-react";
import { useEffect, useState } from "react";
import { Link, Navigate } from "react-router";
import { Alert, Badge, Button, Card, PageHeader, Spinner } from "../../components/ui";
import { copiaTesto } from "../../lib/appunti";
import { api, ApiError } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { data, dataBreve, euro } from "../../lib/format";

// Pannello admin: storico dei pagamenti (tabella ordini), con i totali incassati.

type Stato = "pagato" | "in-attesa" | "scaduto" | "fallito";

interface OrdineAdmin {
  id: string;
  email?: string;
  piano: "medium" | "pro";
  periodo: Periodo;
  prezzo: number;
  importo: number;
  codiceSconto?: string;
  percentualeSconto?: number;
  stato: Stato;
  creatoIl: string;
  pagatoIl?: string;
  scadenzaPiano?: string;
  stripeSessionId?: string;
}

interface RispostaOrdini {
  totali: { ordini: number; pagati: number; incassato: number; incassatoMese: number; perStato: Record<Stato, number> };
  ordini: OrdineAdmin[];
  trovati: number;
  prossima: number | null;
}

const STATI: { id: Stato; nome: string; tone: "green" | "amber" | "slate" | "red" }[] = [
  { id: "pagato", nome: "Pagato", tone: "green" },
  { id: "in-attesa", nome: "In attesa", tone: "amber" },
  { id: "scaduto", nome: "Non completato", tone: "slate" },
  { id: "fallito", nome: "Fallito", tone: "red" },
];

const campo = "h-10 rounded-xl border-0 bg-white px-3 text-sm ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500";

/** Pagina /admin/pagamenti: chi non è admin torna all'app. */
export function AdminPagamenti() {
  const { utente } = useUtente();
  if (!utente.admin) return <Navigate to="/app" replace />;
  return <Storico />;
}

/** Totali, filtri e tabella degli ordini, 50 per volta. */
function Storico() {
  const [stato, setStato] = useState<Stato | "">("pagato");
  const [piano, setPiano] = useState("");
  const [cerca, setCerca] = useState("");
  const [email, setEmail] = useState("");
  const [risposta, setRisposta] = useState<RispostaOrdini>();
  const [ordini, setOrdini] = useState<OrdineAdmin[]>([]);
  const [caricamento, setCaricamento] = useState(true);
  const [errore, setErrore] = useState<string>();

  // Ricerca per inizio dell'email, con una piccola attesa mentre si scrive.
  useEffect(() => {
    const t = setTimeout(() => setEmail(cerca.trim()), 400);
    return () => clearTimeout(t);
  }, [cerca]);

  async function carica(pagina = 0) {
    setCaricamento(true);
    setErrore(undefined);
    try {
      const qs = new URLSearchParams({ pagina: String(pagina) });
      if (stato) qs.set("stato", stato);
      if (piano) qs.set("piano", piano);
      if (email) qs.set("email", email);
      const r = await api<RispostaOrdini>(`/admin/ordini?${qs}`);
      setRisposta(r);
      setOrdini((prima) => (pagina ? [...prima, ...r.ordini] : r.ordini));
    } catch (err) {
      setErrore(err instanceof ApiError ? err.message : "Errore di rete");
    } finally {
      setCaricamento(false);
    }
  }

  useEffect(() => {
    void carica();
  }, [stato, piano, email]);

  const t = risposta?.totali;

  return (
    <div className="space-y-6">
      <Link to="/admin" className="inline-flex items-center gap-1 text-sm font-semibold text-slate-500 hover:text-slate-800">
        <ArrowLeft className="size-4" /> Pannello di controllo
      </Link>
      <PageHeader title="Storico pagamenti" subtitle="Ogni tentativo di acquisto è un ordine: pagato, in attesa del pagamento, non completato o fallito." />

      {t && (
        <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
          {[
            { label: "Incassato questo mese", valore: euro(t.incassatoMese) },
            { label: "Incassato in totale", valore: euro(t.incassato) },
            { label: "Ordini pagati", valore: String(t.pagati) },
            { label: "Ordini non pagati", valore: String(t.ordini - t.pagati) },
          ].map((c) => (
            <Card key={c.label}>
              <Receipt className="size-5 text-brand-600" />
              <p className="mt-2 text-2xl font-extrabold">{c.valore}</p>
              <p className="text-sm text-slate-500">{c.label}</p>
            </Card>
          ))}
        </div>
      )}

      <div className="flex flex-wrap items-end gap-3">
        <label className="text-xs font-semibold text-slate-500">
          Stato
          <select value={stato} onChange={(e) => setStato(e.target.value as Stato | "")} className={`mt-1 block ${campo}`}>
            <option value="">Tutti</option>
            {STATI.map((s) => (
              <option key={s.id} value={s.id}>
                {s.nome} ({t?.perStato[s.id] ?? "…"})
              </option>
            ))}
          </select>
        </label>
        <label className="text-xs font-semibold text-slate-500">
          Piano
          <select value={piano} onChange={(e) => setPiano(e.target.value)} className={`mt-1 block ${campo}`}>
            <option value="">Tutti</option>
            <option value="medium">{PIANI.medium.nome}</option>
            <option value="pro">{PIANI.pro.nome}</option>
          </select>
        </label>
        <label className="relative block min-w-64 flex-1 text-xs font-semibold text-slate-500">
          Email
          <Search className="pointer-events-none absolute bottom-3 left-3 size-4 text-slate-400" />
          <input value={cerca} onChange={(e) => setCerca(e.target.value)} placeholder="inizio dell'indirizzo" className={`mt-1 block w-full pl-9 ${campo}`} />
        </label>
      </div>

      {errore && <Alert tone="error">{errore}</Alert>}

      <div className="overflow-x-auto rounded-2xl bg-white ring-1 ring-slate-200">
        <table className="w-full text-left text-sm">
          <thead className="border-b border-slate-100 text-xs text-slate-500">
            <tr>
              <th className="px-4 py-3 font-semibold">Data</th>
              <th className="px-4 py-3 font-semibold">Utente</th>
              <th className="px-4 py-3 font-semibold">Piano</th>
              <th className="px-4 py-3 font-semibold">Importo</th>
              <th className="px-4 py-3 font-semibold">Stato</th>
              <th className="px-4 py-3 font-semibold">Valido fino al</th>
              <th className="px-4 py-3 font-semibold">Ordine</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {ordini.map((o) => {
              const s = STATI.find((x) => x.id === o.stato)!;
              return (
                <tr key={o.id}>
                  <td className="px-4 py-3 whitespace-nowrap">{dataBreve(o.pagatoIl ?? o.creatoIl)}</td>
                  <td className="px-4 py-3">{o.email ?? <span className="text-slate-400">account eliminato</span>}</td>
                  <td className="px-4 py-3 whitespace-nowrap">
                    {PIANI[o.piano].nome} · {durata(o.periodo).nome}
                  </td>
                  <td className="px-4 py-3 whitespace-nowrap">
                    <strong>{euro(o.importo)}</strong>
                    {o.codiceSconto && (
                      <span className="block text-xs text-slate-500">
                        <s>{euro(o.prezzo)}</s> · {o.codiceSconto} −{o.percentualeSconto}%
                      </span>
                    )}
                  </td>
                  <td className="px-4 py-3">
                    <Badge tone={s.tone}>{s.nome}</Badge>
                  </td>
                  <td className="px-4 py-3 whitespace-nowrap">{o.scadenzaPiano ? data(o.scadenzaPiano) : "—"}</td>
                  <td className="px-4 py-3">
                    <button
                      onClick={() => void copiaTesto(o.stripeSessionId ? `${o.id} · Stripe ${o.stripeSessionId}` : o.id)}
                      className="inline-flex items-center gap-1 font-mono text-xs text-slate-500 hover:text-brand-700"
                      title="Copia il codice dell'ordine (e della sessione Stripe)"
                    >
                      {o.id.slice(0, 12)}… <Copy className="size-3" />
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
        {caricamento ? (
          <Spinner label="Carico gli ordini…" />
        ) : (
          !ordini.length && <p className="py-10 text-center text-sm text-slate-500">Nessun ordine con questi filtri.</p>
        )}
      </div>

      {risposta?.prossima !== null && risposta?.prossima !== undefined && !caricamento && (
        <div className="flex justify-center">
          <Button variant="secondary" onClick={() => void carica(risposta.prossima!)}>
            Carica altri ({risposta.trovati - ordini.length})
          </Button>
        </div>
      )}
    </div>
  );
}
