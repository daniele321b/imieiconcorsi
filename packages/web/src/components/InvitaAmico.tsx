import { Check, Copy, Gift, Send } from "lucide-react";
import { type FormEvent, useState } from "react";
import { api, useApi } from "../lib/api";
import { messaggioErrore } from "../lib/auth";
import { Alert, Button, Card } from "./ui";

// Card "Invita un amico" del profilo: link d'invito da copiare e campo per il codice di chi ci ha invitato.

interface InvitoApi {
  codice: string;
  link: string;
  iscritti: number;
  premi: number;
  giorniPerPremio: number;
  puoiInserire: boolean;
  invitato: boolean;
}

/** Profilo: il proprio codice da dare agli amici e, prima del primo acquisto, il codice di chi ci ha invitato. */
export function InvitaAmico() {
  const { data, error, reload } = useApi<InvitoApi>("/me/invito");
  const [copiato, setCopiato] = useState(false);
  const [codiceAmico, setCodiceAmico] = useState("");
  const [inCorso, setInCorso] = useState(false);
  const [esito, setEsito] = useState<{ tone: "success" | "error"; testo: string }>();

  // Copia il link d'invito negli appunti e lo segnala per due secondi.
  async function copia() {
    if (!data) return;
    try {
      await navigator.clipboard.writeText(data.link);
      setCopiato(true);
      setTimeout(() => setCopiato(false), 2000);
    } catch {}
  }

  // Registra il codice dell'amico che ci ha invitato.
  async function inserisci(e: FormEvent) {
    e.preventDefault();
    setInCorso(true);
    setEsito(undefined);
    try {
      await api("/me/invito", { method: "POST", body: { codice: codiceAmico } });
      setEsito({ tone: "success", testo: "Fatto: quando comprerai un piano, il tuo amico riceverà un mese gratis." });
      setCodiceAmico("");
      await reload();
    } catch (err) {
      setEsito({ tone: "error", testo: messaggioErrore(err) });
    } finally {
      setInCorso(false);
    }
  }

  if (error || !data) return null;
  const messaggio = encodeURIComponent(`Mi sto preparando ai concorsi pubblici con iMieiConcorsi: provalo anche tu ${data.link}`);

  return (
    <Card className="space-y-4">
      <div className="flex items-start gap-3">
        <span className="grid size-10 shrink-0 place-items-center rounded-xl bg-amber-100 text-amber-700">
          <Gift className="size-5" />
        </span>
        <div>
          <h2 className="font-bold text-slate-900">Invita un amico, prendi un mese gratis</h2>
          <p className="text-sm text-slate-500">
            Quando un amico si iscrive con il tuo link e compra un piano, ricevi {data.giorniPerPremio} giorni gratis: Medium se sei Free,
            altrimenti il tuo piano si allunga.
          </p>
        </div>
      </div>

      <div className="flex flex-col gap-2 sm:flex-row sm:items-center">
        <code className="flex-1 truncate rounded-xl bg-slate-50 px-3 py-2.5 text-sm text-slate-700 ring-1 ring-slate-200">{data.link}</code>
        <div className="flex gap-2">
          <Button variant="secondary" onClick={() => void copia()}>
            {copiato ? <Check className="size-4" /> : <Copy className="size-4" />} {copiato ? "Copiato" : "Copia"}
          </Button>
          <a
            href={`https://wa.me/?text=${messaggio}`}
            target="_blank"
            rel="noreferrer"
            className="inline-flex h-10 items-center gap-2 rounded-xl bg-emerald-600 px-4 text-sm font-semibold text-white hover:bg-emerald-700"
          >
            <Send className="size-4" /> WhatsApp
          </a>
        </div>
      </div>
      <p className="text-xs text-slate-500">
        Il tuo codice: <strong className="font-mono">{data.codice}</strong> · amici iscritti: {data.iscritti} · hanno comprato: {data.premi}
      </p>

      {data.puoiInserire && (
        <form onSubmit={inserisci} className="flex flex-col gap-2 border-t border-slate-100 pt-4 sm:flex-row sm:items-center">
          <label htmlFor="codice-amico" className="text-sm text-slate-600 sm:w-56">
            Ti ha invitato un amico?
          </label>
          <input
            id="codice-amico"
            value={codiceAmico}
            onChange={(e) => setCodiceAmico(e.target.value.toUpperCase())}
            placeholder="AMICO-…"
            className="h-10 flex-1 rounded-xl border-0 bg-white px-3 font-mono uppercase ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500 focus:outline-none"
          />
          <Button type="submit" variant="secondary" disabled={!codiceAmico.trim()} loading={inCorso}>
            Inserisci
          </Button>
        </form>
      )}
      {data.invitato && !data.puoiInserire && <p className="text-xs text-slate-500">Sei stato invitato da un amico: grazie!</p>}
      {esito && (
        <Alert tone={esito.tone} onClose={() => setEsito(undefined)}>
          {esito.testo}
        </Alert>
      )}
    </Card>
  );
}
