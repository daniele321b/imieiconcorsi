import { PERIODI, PIANI, type PianoId } from "@imieiconcorsi/core/domain";
import { Check } from "lucide-react";
import { Link } from "react-router";
import { cx } from "../../components/ui";
import { useAuth } from "../../lib/auth";
import { euro } from "../../lib/format";
import { LegalePagina } from "../legale/LegalePagina";

// Pagina pubblica /prezzi: piani e prezzi visibili anche senza account (dentro l'app la
// scelta e l'acquisto stanno in /app/piani). I dati vengono da PIANI in core/domain.ts.

const ORDINE: PianoId[] = ["free", "medium", "pro"];

/** Pagina /prezzi. */
export function Prezzi() {
  const { stato } = useAuth();
  const dentro = stato === "autenticato";
  return (
    <LegalePagina titolo="Prezzi" sotto="Si parte gratis. Quando serve, un piano per il tempo che ti occorre: pagamento unico, nessun rinnovo automatico." versione={false}>
      <div className="not-prose grid gap-4 md:grid-cols-3">
        {ORDINE.map((id) => {
          const p = PIANI[id];
          return (
            <div key={id} className={cx("flex flex-col rounded-2xl bg-white p-5 shadow-sm ring-1", id === "pro" ? "ring-2 ring-brand-500" : "ring-slate-200")}>
              <p className="text-lg font-bold text-slate-900">{p.nome}</p>
              <p className="text-sm text-slate-500">{p.slogan}</p>
              {id === "free" ? (
                <p className="mt-3 text-3xl font-extrabold text-slate-900">Gratis</p>
              ) : (
                <dl className="mt-3 space-y-1 text-sm">
                  {PERIODI.map((per) => (
                    <div key={per.id} className="flex items-baseline justify-between gap-2">
                      <dt className="text-slate-500">{per.nome}</dt>
                      <dd className="text-lg font-extrabold text-slate-900">{euro(p.prezzo[per.id])}</dd>
                    </div>
                  ))}
                </dl>
              )}
              <ul className="mt-4 flex-1 list-none! space-y-1.5 pl-0! text-sm text-slate-700">
                {p.funzioni.map((f) => (
                  <li key={f} className="flex gap-2">
                    <Check className="mt-0.5 size-4 shrink-0 text-emerald-600" /> {f}
                  </li>
                ))}
              </ul>
            </div>
          );
        })}
      </div>

      <div className="mt-6 text-center">
        <Link
          to={dentro ? "/app/piani" : "/"}
          className="inline-flex h-11 items-center rounded-xl bg-brand-600 px-6 text-sm font-semibold text-white no-underline hover:bg-brand-700"
          style={{ textDecoration: "none", color: "white" }}
        >
          {dentro ? "Scegli il tuo piano" : "Inizia gratis"}
        </Link>
      </div>

      <h2>Come funziona il pagamento</h2>
      <ul>
        <li>
          <strong>Pagamento unico</strong> per 30 giorni, 90 giorni o un anno. Alla scadenza il piano non si rinnova: torni al
          Free, con tutti i tuoi progressi, e ti avvisiamo per email 3 giorni prima.
        </li>
        <li>Prezzi in euro, IVA inclusa ove dovuta. Il prezzo applicato è quello mostrato al momento dell'acquisto.</li>
        <li>
          Paghi sulla pagina sicura di Stripe con carta, PayPal, Apple Pay o Google Pay: non vediamo i dati della tua carta. La
          ricevuta arriva per email.
        </li>
        <li>
          Se ricompri lo stesso piano i giorni si sommano alla scadenza; passando da Medium a Pro i giorni rimasti vengono
          convertiti.
        </li>
        <li>
          L'accesso ai contenuti è immediato: per questo, con il tuo consenso al momento dell'acquisto, non si applica il diritto
          di recesso di 14 giorni. I dettagli, anche sui rimborsi dovuti per legge, sono nei{" "}
          <Link to="/termini">Termini e condizioni</Link> (punti 3 e 4).
        </li>
      </ul>
    </LegalePagina>
  );
}
