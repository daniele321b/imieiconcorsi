import { useEffect, useState } from "react";
import { Link, useSearchParams } from "react-router";
import { config } from "../lib/config";
import { LegalePagina } from "./legale/LegalePagina";

// Pagina aperta dal link "non ricevere più avvisi" nelle email: funziona senza login.
// Si conferma con un pulsante, così i programmi che aprono i link delle email da soli
// (antivirus, anteprime) non disiscrivono nessuno per sbaglio.

/** Momenti della pagina: prima della conferma, invio, fatto, errore (link non valido). */
type Stato = "da-confermare" | "in-corso" | "fatto" | "errore";

/** Pagina /disiscrivi?u=…&t=… */
export function Disiscrivi() {
  const [params] = useSearchParams();
  const u = params.get("u");
  const t = params.get("t");
  const [stato, setStato] = useState<Stato>("da-confermare");
  const [errore, setErrore] = useState<string>();

  useEffect(() => {
    if (!u || !t) {
      setStato("errore");
      setErrore("Link incompleto: apri quello che trovi in fondo all'email degli avvisi.");
    }
  }, [u, t]);

  // Conferma la disiscrizione dagli avvisi via email con la firma del link.
  async function conferma() {
    setStato("in-corso");
    try {
      const res = await fetch(`${config.apiUrl}/pubblico/disiscrivi`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ u, t }),
      });
      if (!res.ok) throw new Error(((await res.json().catch(() => ({}))) as { error?: string }).error ?? "Non riuscito");
      setStato("fatto");
    } catch (err) {
      setStato("errore");
      setErrore(err instanceof Error ? err.message : "Non riuscito, riprova.");
    }
  }

  return (
    <LegalePagina titolo="Avvisi sui nuovi bandi">
      {stato === "fatto" ? (
        <>
          <p>
            <strong>Fatto.</strong> Non riceverai più le email con i nuovi bandi. Le altre email del tuo account (per esempio
            la conferma di un acquisto) restano attive.
          </p>
          <p>
            Puoi riattivare gli avvisi quando vuoi dal tuo <Link to="/app/profilo">profilo</Link>.
          </p>
        </>
      ) : stato === "errore" ? (
        <p>{errore}</p>
      ) : (
        <>
          <p>Vuoi smettere di ricevere le email con i nuovi bandi dei comparti che segui?</p>
          <p>
            <button
              onClick={() => void conferma()}
              disabled={stato === "in-corso"}
              className="rounded-xl bg-brand-600 px-5 py-2.5 font-semibold text-white hover:bg-brand-700 disabled:opacity-60"
            >
              {stato === "in-corso" ? "Un attimo…" : "Sì, non inviarmi più gli avvisi"}
            </button>
          </p>
        </>
      )}
    </LegalePagina>
  );
}
