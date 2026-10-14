import { TIPI_RICHIESTA, type StatoRichiesta, type TipoRichiesta } from "@imieiconcorsi/core/domain";
import { ArrowLeft, CheckCircle2, Flag, Send } from "lucide-react";
import { type ReactNode, useState } from "react";
import { Link } from "react-router";
import { api, ApiError, type ContestoRichiesta, type RichiestaApi } from "../lib/api";
import { dataOra } from "../lib/format";
import { Badge, Button, cx } from "./ui";

// Pezzi comuni dell'assistenza: la usano la pagina dell'utente (/app/assistenza) e il
// pannello admin (/admin/richieste).

/** Cosa si passa alla pagina Assistenza con lo stato del link (niente dati nell'indirizzo). */
export interface AperturaRichiesta {
  tipo: TipoRichiesta;
  contesto?: ContestoRichiesta;
}

/** I tre stati con nome e colore dell'etichetta. */
export const STATI_RICHIESTA: { id: StatoRichiesta; nome: string; tone: "amber" | "brand" | "slate" }[] = [
  { id: "aperta", nome: "Aperta", tone: "amber" },
  { id: "in-lavorazione", nome: "In lavorazione", tone: "brand" },
  { id: "chiusa", nome: "Chiusa", tone: "slate" },
];

/** Etichetta colorata dello stato di una richiesta. */
export function StatoRichiestaBadge({ stato }: { stato: StatoRichiesta }) {
  const s = STATI_RICHIESTA.find((x) => x.id === stato)!;
  return <Badge tone={s.tone}>{s.nome}</Badge>;
}

/** Traccia del messaggio per una domanda sbagliata (la stessa della pagina Assistenza). */
const TRACCIA_ERRORE = TIPI_RICHIESTA.find((t) => t.id === "domanda-errata")!.modello;

/**
 * "Segnala un errore" sotto una domanda: si apre qui, sotto la domanda, senza cambiare pagina
 * (in una sessione di studio si perderebbe il punto). Inviata la segnalazione, "Torna alla
 * domanda" chiude il riquadro e si riprende da dove si era; la risposta arriva in Assistenza.
 */
export function SegnalaErrore({ contesto, className }: { contesto: ContestoRichiesta; className?: string }) {
  const [aperta, setAperta] = useState(false);
  const [testo, setTesto] = useState<string>(TRACCIA_ERRORE);
  const [invio, setInvio] = useState(false);
  const [inviata, setInviata] = useState(false);
  const [errore, setErrore] = useState<string>();
  // Chiude il modulo e lo riporta allo stato iniziale.
  const torna = () => {
    setAperta(false);
    setInviata(false);
    setErrore(undefined);
    setTesto(TRACCIA_ERRORE);
  };

  // Invia la segnalazione di una domanda errata, con il contesto della domanda.
  async function invia() {
    setInvio(true);
    setErrore(undefined);
    try {
      await api("/me/richieste", { method: "POST", body: { tipo: "domanda-errata", testo: testo.trim(), contesto } });
      setInviata(true);
    } catch (err) {
      setErrore(err instanceof ApiError ? err.message : "Invio non riuscito: riprova.");
    } finally {
      setInvio(false);
    }
  }

  if (!aperta) {
    return (
      <button
        type="button"
        onClick={() => setAperta(true)}
        className={cx("inline-flex items-center gap-1.5 text-xs font-semibold text-slate-400 hover:text-rose-600", className)}
      >
        <Flag className="size-3.5" /> Segnala un errore
      </button>
    );
  }
  // Il testo conta solo se si è scritto qualcosa oltre la traccia.
  const scritto = testo.trim().length >= 10 && testo !== TRACCIA_ERRORE;
  return (
    <div className="mt-3 w-full basis-full animate-fade-up space-y-3 rounded-xl bg-white p-4 text-sm ring-1 ring-rose-200">
      {inviata ? (
        <>
          <p className="flex items-center gap-2 font-semibold text-emerald-700">
            <CheckCircle2 className="size-4" /> Segnalazione inviata, grazie!
          </p>
          <p className="text-slate-600">
            La controlliamo e ti rispondiamo in{" "}
            <Link to="/app/assistenza" className="font-semibold text-brand-600 hover:underline">
              Assistenza
            </Link>
            , con un'email quando c'è la risposta.
          </p>
          <Button size="sm" onClick={torna}>
            <ArrowLeft className="size-4" /> Torna alla domanda
          </Button>
        </>
      ) : (
        <>
          <p className="flex items-center gap-2 font-semibold text-slate-900">
            <Flag className="size-4 text-rose-500" /> Cosa non va in questa domanda?
          </p>
          <textarea value={testo} onChange={(e) => setTesto(e.target.value)} rows={4} maxLength={3000} autoFocus className={areaTesto} />
          {errore && <p className="text-rose-600">{errore}</p>}
          <div className="flex flex-wrap gap-2">
            <Button size="sm" variant="secondary" disabled={invio} onClick={torna}>
              <ArrowLeft className="size-4" /> Torna alla domanda
            </Button>
            <Button size="sm" disabled={!scritto} loading={invio} onClick={() => void invia()}>
              <Send className="size-4" /> Invia segnalazione
            </Button>
          </div>
        </>
      )}
    </div>
  );
}

/** Da dove nasce la richiesta: domanda, concorso, banca dati, ordine. */
export function ContestoBox({ contesto }: { contesto?: ContestoRichiesta }) {
  if (!contesto || !Object.keys(contesto).length) return null;
  return (
    <div className="space-y-1 rounded-xl bg-slate-50 p-3 text-xs text-slate-600">
      {contesto.domanda && (
        <p>
          <span className="font-semibold text-slate-800">Domanda:</span> {contesto.domanda.testo}
        </p>
      )}
      {contesto.bancaDatiId && (
        <p>
          <span className="font-semibold text-slate-800">Banca dati:</span>{" "}
          <Link to={`/app/banche-dati/${contesto.bancaDatiId}`} className="text-brand-600 hover:underline">
            apri
          </Link>
          {contesto.domanda && ` (domanda ${contesto.domanda.id})`}
        </p>
      )}
      {contesto.concorsoId && (
        <p>
          <span className="font-semibold text-slate-800">Concorso:</span>{" "}
          <Link to={`/app/concorsi/${contesto.concorsoId}`} className="text-brand-600 hover:underline">
            apri il bando
          </Link>
        </p>
      )}
      {contesto.ordineId && (
        <p>
          <span className="font-semibold text-slate-800">Ordine:</span> <span className="font-mono">{contesto.ordineId}</span>
        </p>
      )}
    </div>
  );
}

/**
 * I messaggi di una richiesta, come una chat: a destra quelli di chi guarda (`io`),
 * a sinistra quelli dell'altra parte.
 */
export function Conversazione({ messaggi, io }: { messaggi: RichiestaApi["messaggi"]; io: "utente" | "assistenza" }) {
  return (
    <ol className="space-y-3">
      {messaggi.map((m, i) => {
        const mio = m.da === io;
        return (
          <li key={i} className={cx("flex flex-col", mio ? "items-end" : "items-start")}>
            <div
              className={cx(
                "max-w-[85%] rounded-2xl px-4 py-2.5 text-sm whitespace-pre-wrap",
                mio ? "rounded-br-md bg-brand-600 text-white" : "rounded-bl-md bg-slate-100 text-slate-800",
              )}
            >
              {m.testo}
            </div>
            <span className="mt-1 text-[11px] text-slate-400">
              {m.da === "assistenza" ? "Assistenza" : io === "assistenza" ? "Utente" : "Tu"} · {dataOra(m.il)}
            </span>
          </li>
        );
      })}
    </ol>
  );
}

/** Stile delle caselle di testo dell'assistenza. */
export const areaTesto =
  "block w-full rounded-xl border-0 bg-white px-3.5 py-2.5 text-sm text-slate-900 ring-1 ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-brand-500 focus:outline-none";

/** Casella per rispondere in una conversazione. `invia` restituisce false se l'invio non è riuscito. */
export function RispondiBox({
  invia,
  placeholder = "Scrivi un messaggio…",
  extra,
}: {
  invia: (testo: string) => Promise<boolean>;
  placeholder?: string;
  /** Altri comandi accanto al pulsante (es. lo stato nel pannello admin) */
  extra?: ReactNode;
}) {
  const [testo, setTesto] = useState("");
  const [invio, setInvio] = useState(false);

  // Invia il messaggio e svuota il campo se è andato.
  async function onInvia() {
    setInvio(true);
    if (await invia(testo.trim())) setTesto("");
    setInvio(false);
  }

  return (
    <div className="space-y-2">
      <textarea value={testo} onChange={(e) => setTesto(e.target.value)} rows={3} maxLength={3000} placeholder={placeholder} className={areaTesto} />
      <div className="flex flex-wrap items-center justify-end gap-2">
        {extra}
        <Button size="sm" loading={invio} disabled={testo.trim().length < 2} onClick={() => void onInvia()}>
          <Send className="size-3.5" /> Invia
        </Button>
      </div>
    </div>
  );
}
