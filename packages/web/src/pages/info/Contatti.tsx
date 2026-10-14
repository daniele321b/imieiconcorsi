import { CheckCircle2, LifeBuoy, Send, ShieldCheck, Trash2 } from "lucide-react";
import { useState } from "react";
import { Link } from "react-router";
import { Button } from "../../components/ui";
import { useAuth } from "../../lib/auth";
import { config } from "../../lib/config";
import { LEGALE } from "../../lib/legale";
import { LegalePagina } from "../legale/LegalePagina";

// Pagina pubblica /contatti: modulo che funziona senza account (POST /pubblico/contatto, il
// messaggio arriva all'admin per email) e scorciatoie per assistenza, privacy ed eliminazione.

const ARGOMENTI = [
  { id: "informazioni", nome: "Informazioni sul servizio" },
  { id: "account", nome: "Accesso e account" },
  { id: "pagamenti", nome: "Pagamenti e ricevute" },
  { id: "privacy", nome: "Privacy e dati personali" },
  { id: "segnalazione", nome: "Segnalare un errore" },
  { id: "altro", nome: "Altro" },
] as const;

const campo =
  "mt-1 block w-full rounded-xl border-0 bg-white px-3 py-2.5 text-sm text-slate-900 ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500 focus:outline-none";

/** Pagina /contatti. */
export function Contatti() {
  const { stato } = useAuth();
  const [dati, setDati] = useState({ nome: "", email: "", argomento: "informazioni", messaggio: "", sito: "" });
  const [invio, setInvio] = useState(false);
  const [inviato, setInviato] = useState(false);
  const [errore, setErrore] = useState<string>();
  // Cambia solo i campi indicati del modulo.
  const set = (parziale: Partial<typeof dati>) => setDati((d) => ({ ...d, ...parziale }));

  // Invia il modulo contatti.
  async function invia(e: React.FormEvent) {
    e.preventDefault();
    setInvio(true);
    setErrore(undefined);
    try {
      const res = await fetch(`${config.apiUrl}/pubblico/contatto`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ ...dati, sito: dati.sito || undefined }),
      });
      if (!res.ok) throw new Error(((await res.json().catch(() => ({}))) as { error?: string }).error ?? "Messaggio non inviato");
      setInviato(true);
    } catch (err) {
      setErrore(err instanceof Error ? err.message : "Messaggio non inviato: riprova.");
    } finally {
      setInvio(false);
    }
  }

  return (
    <LegalePagina titolo="Contatti" sotto="Scrivici per qualsiasi domanda: rispondiamo all'email che indichi, di solito entro 2 giorni lavorativi." versione={false}>
      <div className="grid gap-3 sm:grid-cols-3">
        {[
          {
            Icon: LifeBuoy,
            titolo: "Hai un account?",
            testo: "Dalla pagina Assistenza dell'app trovi le risposte anche lì, insieme alla storia della richiesta.",
            to: stato === "autenticato" ? "/app/assistenza" : "/",
            link: stato === "autenticato" ? "Vai all'Assistenza" : "Accedi",
          },
          { Icon: ShieldCheck, titolo: "Privacy", testo: "Come trattiamo i dati e come esercitare i tuoi diritti.", to: "/privacy", link: "Informativa" },
          { Icon: Trash2, titolo: "Eliminare l'account", testo: "Si fa dal profilo, in un minuto.", to: "/eliminazione-dati", link: "Come fare" },
        ].map((b) => (
          <div key={b.titolo} className="rounded-2xl bg-white p-4 text-sm shadow-sm ring-1 ring-slate-200/70">
            <b.Icon className="size-5 text-brand-600" />
            <p className="mt-2 font-semibold text-slate-900">{b.titolo}</p>
            <p className="mt-1 text-slate-600">{b.testo}</p>
            <Link to={b.to} className="mt-2 inline-block">
              {b.link}
            </Link>
          </div>
        ))}
      </div>

      <h2>Scrivici</h2>
      {LEGALE.email && (
        <p>
          Puoi scrivere anche a <strong>{LEGALE.email}</strong>.
        </p>
      )}
      {inviato ? (
        <div className="flex gap-3 rounded-2xl bg-emerald-50 p-4 text-emerald-900 ring-1 ring-emerald-200">
          <CheckCircle2 className="mt-0.5 size-5 shrink-0" />
          <p>
            <strong className="text-emerald-900">Messaggio inviato, grazie!</strong> Ti rispondiamo all'indirizzo {dati.email}.
          </p>
        </div>
      ) : (
        <form onSubmit={(e) => void invia(e)} className="space-y-3 rounded-2xl bg-white p-5 shadow-sm ring-1 ring-slate-200/70">
          <div className="grid gap-3 sm:grid-cols-2">
            <label className="block text-sm">
              <span className="font-medium text-slate-700">Nome</span>
              <input required minLength={2} maxLength={100} autoComplete="name" className={campo} value={dati.nome} onChange={(e) => set({ nome: e.target.value })} />
            </label>
            <label className="block text-sm">
              <span className="font-medium text-slate-700">Email</span>
              <input required type="email" maxLength={200} autoComplete="email" className={campo} value={dati.email} onChange={(e) => set({ email: e.target.value })} />
            </label>
          </div>
          <label className="block text-sm">
            <span className="font-medium text-slate-700">Argomento</span>
            <select className={campo} value={dati.argomento} onChange={(e) => set({ argomento: e.target.value })}>
              {ARGOMENTI.map((a) => (
                <option key={a.id} value={a.id}>
                  {a.nome}
                </option>
              ))}
            </select>
          </label>
          <label className="block text-sm">
            <span className="font-medium text-slate-700">Messaggio</span>
            <textarea required minLength={10} maxLength={3000} rows={6} className={campo} value={dati.messaggio} onChange={(e) => set({ messaggio: e.target.value })} />
          </label>
          {/* Trappola per i programmi automatici: invisibile alle persone. */}
          <input
            type="text"
            name="sito"
            tabIndex={-1}
            autoComplete="off"
            aria-hidden
            className="absolute -left-[9999px] h-0 w-0 opacity-0"
            value={dati.sito}
            onChange={(e) => set({ sito: e.target.value })}
          />
          <p className="text-xs text-slate-500">
            Usiamo nome, email e messaggio solo per risponderti, come spiegato nell'<Link to="/privacy">Informativa sulla privacy</Link>.
            Non scrivere password o dati della carta.
          </p>
          {errore && <p className="text-sm text-rose-600">{errore}</p>}
          <Button type="submit" loading={invio}>
            <Send className="size-4" /> Invia il messaggio
          </Button>
        </form>
      )}
    </LegalePagina>
  );
}
