import { CheckCircle2, Clock, XCircle } from "lucide-react";
import { useEffect, useRef, useState } from "react";
import { Link, useSearchParams } from "react-router";
import type { AperturaRichiesta } from "../../components/Richieste";
import { Alert, ButtonLink, Card, Spinner } from "../../components/ui";
import { api, ApiError, type OrdineApi } from "../../lib/api";
import { useAuth } from "../../lib/auth";
import { data as dataLunga, euro } from "../../lib/format";

/** Ogni quanto richiedere l'esito e per quanto (la conferma di Stripe arriva di solito in pochi secondi). */
const OGNI_MS = 2000;
const MASSIMO_MS = 90_000;

// Pagina di ritorno da Stripe: /app/pagamento?ordine=ord_…[&annullato=1]
export function Pagamento() {
  const [params] = useSearchParams();
  const id = params.get("ordine");
  const annullato = params.has("annullato");
  const { ricarica } = useAuth();
  const [ordine, setOrdine] = useState<OrdineApi>();
  const [errore, setErrore] = useState<string>();
  const [scaduto, setScaduto] = useState(false);
  const inizio = useRef(Date.now());

  useEffect(() => {
    if (!id) return;
    let fermo = false;
    let timer: ReturnType<typeof setTimeout>;

    async function controlla() {
      try {
        const o = await api<OrdineApi>(`/me/ordini/${encodeURIComponent(id!)}`);
        if (fermo) return;
        setOrdine(o);
        if (o.stato === "pagato") {
          // Il piano è un gruppo Cognito: serve un token nuovo perché l'app lo veda.
          await ricarica({ rinnovaToken: true });
          return;
        }
        if (o.stato !== "in-attesa" || annullato) return;
      } catch (err) {
        if (fermo) return;
        setErrore(err instanceof ApiError ? err.message : "Errore di rete");
        return;
      }
      if (Date.now() - inizio.current > MASSIMO_MS) setScaduto(true);
      else timer = setTimeout(() => void controlla(), OGNI_MS);
    }

    void controlla();
    return () => {
      fermo = true;
      clearTimeout(timer);
    };
  }, [id, annullato, ricarica]);

  if (!id) return <Alert tone="error">Ordine non indicato.</Alert>;
  if (errore) return <Alert tone="error">{errore}</Alert>;
  if (!ordine) return <Spinner label="Controllo il pagamento…" />;

  const nomePiano = ordine.piano === "pro" ? "Pro" : "Medium";

  return (
    <div className="mx-auto max-w-lg">
      <Card className="p-8 text-center">
        {ordine.stato === "pagato" ? (
          <>
            <CheckCircle2 className="mx-auto size-12 text-emerald-500" />
            <h1 className="mt-4 text-2xl font-extrabold">Pagamento riuscito</h1>
            <p className="mt-2 text-slate-600">
              Il piano <strong>{nomePiano}</strong> è attivo
              {ordine.scadenzaPiano && <> fino al {dataLunga(ordine.scadenzaPiano)}</>}. Ti abbiamo mandato l'email di conferma.
            </p>
            <p className="mt-1 text-sm text-slate-500">Importo: {euro(ordine.importo)}</p>
            <ButtonLink to="/app" className="mt-6">
              Inizia a studiare
            </ButtonLink>
          </>
        ) : annullato && ordine.stato === "in-attesa" ? (
          <>
            <XCircle className="mx-auto size-12 text-slate-400" />
            <h1 className="mt-4 text-2xl font-extrabold">Pagamento annullato</h1>
            <p className="mt-2 text-slate-600">Non è stato addebitato nulla e il tuo piano non è cambiato.</p>
            <ButtonLink to="/app/piani" variant="secondary" className="mt-6">
              Torna ai piani
            </ButtonLink>
          </>
        ) : ordine.stato === "in-attesa" ? (
          <>
            <Clock className="mx-auto size-12 text-brand-500" />
            <h1 className="mt-4 text-2xl font-extrabold">Stiamo ricevendo la conferma…</h1>
            <p className="mt-2 text-slate-600">
              {scaduto
                ? "La conferma del pagamento non è ancora arrivata. Se hai pagato, il piano si attiva da solo appena arriva: ricarica la pagina tra qualche minuto."
                : "Di solito bastano pochi secondi. Non chiudere la pagina."}
            </p>
            {!scaduto && <Spinner label="" />}
          </>
        ) : (
          <>
            <XCircle className="mx-auto size-12 text-rose-500" />
            <h1 className="mt-4 text-2xl font-extrabold">{ordine.stato === "scaduto" ? "Pagamento scaduto" : "Pagamento non riuscito"}</h1>
            <p className="mt-2 text-slate-600">Non è stato addebitato nulla. Puoi riprovare quando vuoi.</p>
            <ButtonLink to="/app/piani" variant="secondary" className="mt-6">
              Torna ai piani
            </ButtonLink>
          </>
        )}
      </Card>
      <p className="mt-4 text-center text-xs text-slate-400">
        Ordine {ordine.id} · <Link to="/termini">Termini</Link> ·{" "}
        <Link to="/app/assistenza" state={{ tipo: "pagamento", contesto: { ordineId: ordine.id } } satisfies AperturaRichiesta}>
          Problemi con il pagamento?
        </Link>
      </p>
    </div>
  );
}
