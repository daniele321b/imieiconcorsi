import { feedbackModificabileDal, GIORNI_TRA_FEEDBACK } from "@imieiconcorsi/core/domain";
import { MessageSquareHeart, Star } from "lucide-react";
import { useState } from "react";
import { api } from "../lib/api";
import { messaggioErrore, useAuth, useUtente } from "../lib/auth";
import { data } from "../lib/format";
import { Alert, Button, cx } from "./ui";

/** Parere sull'app nel profilo: voto da 1 a 5 e commento, modificabile ogni 15 giorni. */
export function FeedbackApp() {
  const { utente } = useUtente();
  const { ricarica } = useAuth();
  const [voto, setVoto] = useState(utente.feedback?.voto ?? 0);
  const [testo, setTesto] = useState(utente.feedback?.testo ?? "");
  const [invio, setInvio] = useState(false);
  const [esito, setEsito] = useState<{ tone: "success" | "error"; testo: string }>();
  const bloccatoFino = feedbackModificabileDal(utente.feedback);

  async function invia() {
    setInvio(true);
    setEsito(undefined);
    try {
      await api("/me/feedback", { method: "PUT", body: { voto, testo: testo.trim() || undefined } });
      await ricarica();
      setEsito({ tone: "success", testo: "Grazie! Il tuo parere ci aiuta a migliorare l'app." });
    } catch (err) {
      setEsito({ tone: "error", testo: messaggioErrore(err) });
    } finally {
      setInvio(false);
    }
  }

  return (
    <section className="space-y-3">
      <h2 className="flex items-center gap-2 text-lg font-bold">
        <MessageSquareHeart className="size-5 text-brand-600" /> Il tuo parere sull'app
      </h2>
      <p className="text-sm text-slate-500">
        Puoi cambiarlo una volta ogni {GIORNI_TRA_FEEDBACK} giorni
        {bloccatoFino ? <>: di nuovo dal {data(bloccatoFino)}.</> : "."}
      </p>
      <div className="flex gap-1" role="radiogroup" aria-label="Voto da 1 a 5">
        {[1, 2, 3, 4, 5].map((n) => (
          <button
            key={n}
            role="radio"
            aria-checked={voto === n}
            aria-label={`${n} su 5`}
            disabled={!!bloccatoFino}
            onClick={() => setVoto(n)}
            className="p-1 disabled:cursor-not-allowed"
          >
            <Star className={cx("size-7", n <= voto ? "fill-accent-400 text-accent-400" : "text-slate-300")} />
          </button>
        ))}
      </div>
      <textarea
        value={testo}
        onChange={(e) => setTesto(e.target.value)}
        disabled={!!bloccatoFino}
        maxLength={1000}
        rows={3}
        placeholder="Cosa ti piace, cosa manca, cosa miglioreresti?"
        className="block w-full max-w-2xl rounded-xl border-0 bg-white px-3.5 py-2.5 text-sm text-slate-900 ring-1 ring-slate-300 placeholder:text-slate-400 focus:ring-2 focus:ring-brand-500 focus:outline-none disabled:bg-slate-50 disabled:text-slate-500"
      />
      {esito && (
        <Alert tone={esito.tone} onClose={() => setEsito(undefined)}>
          {esito.testo}
        </Alert>
      )}
      {!bloccatoFino && (
        <Button variant="secondary" disabled={!voto} loading={invio} onClick={() => void invia()}>
          {utente.feedback ? "Aggiorna il parere" : "Invia il parere"}
        </Button>
      )}
    </section>
  );
}
