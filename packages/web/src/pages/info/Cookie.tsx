import { Link } from "react-router";
import { LegalePagina } from "../legale/LegalePagina";
import { ComeContattarci } from "../legale/parti";

// Pagina pubblica /cookie: cosa salva il sito nel browser. Deve restare allineata alle chiavi
// usate nel codice (lib/ordineRisposte.ts, lib/invito.ts, lib/bandi.ts, pages/app/Sessione.tsx,
// pages/app/BancaDatiConsulta.tsx, pages/AuthCallback.tsx) e ad Amplify (token di accesso).
// Se un giorno arrivano statistiche o pubblicità di terzi serve il banner del consenso.

const VOCI: { nome: string; cosa: string; durata: string }[] = [
  {
    nome: "Accesso (Amazon Cognito)",
    cosa: "I token che ti tengono collegato al tuo account, così non devi rifare l'accesso a ogni visita.",
    durata: "Finché non esci; si rinnovano da soli fino a 30 giorni",
  },
  {
    nome: "Risposte della simulazione",
    cosa: "Le risposte già date durante una simulazione, per non perderle se ricarichi la pagina.",
    durata: "Fino alla consegna della simulazione",
  },
  {
    nome: "Preferenze di studio",
    cosa: "Come vuoi vedere la risposta giusta nelle banche dati (mescolata o sempre per prima) e se mostrarla subito.",
    durata: "Finché non la cambi",
  },
  {
    nome: "Codice invito",
    cosa: "Il codice dell'amico che ti ha invitato, se apri il suo link, fino a quando completi l'iscrizione.",
    durata: "Fino all'iscrizione",
  },
  {
    nome: "Accesso con Google o Facebook",
    cosa: "Un segno temporaneo per completare l'accesso social al primo collegamento.",
    durata: "Fino alla chiusura della scheda",
  },
];

/** Pagina /cookie. */
export function Cookie() {
  return (
    <LegalePagina titolo="Cookie e memoria del browser">
      <p>
        <strong>Non usiamo cookie di profilazione, di pubblicità o di statistica</strong>, né nostri né di terze parti. Per
        questo non ti chiediamo il consenso con un banner.
      </p>
      <p>
        Il sito salva nel tuo browser (memoria locale, simile ai cookie tecnici) solo quello che serve a farlo funzionare. Sono
        strumenti tecnici, che la legge permette senza consenso:
      </p>
      <div className="not-prose space-y-2">
        {VOCI.map((v) => (
          <div key={v.nome} className="rounded-2xl bg-white p-4 text-sm shadow-sm ring-1 ring-slate-200/70">
            <p className="font-semibold text-slate-900">{v.nome}</p>
            <p className="mt-1 text-slate-600">{v.cosa}</p>
            <p className="mt-1 text-xs text-slate-500">Quanto resta: {v.durata}</p>
          </div>
        ))}
      </div>

      <h2>Pagine di altri servizi</h2>
      <p>
        Quando accedi con Google o Facebook, o quando paghi sulla pagina di Stripe, sei sui loro siti, che usano i propri
        cookie secondo le loro informative. Noi non leggiamo quei cookie.
      </p>

      <h2>Come cancellarli</h2>
      <p>
        Uscendo dall'account si cancellano i token di accesso. Puoi cancellare tutto dalle impostazioni del browser (dati dei
        siti per {"imieiconcorsi.it"}): dovrai solo rifare l'accesso. Il resto è spiegato nell'
        <Link to="/privacy">Informativa sulla privacy</Link>; per domande scrivici <ComeContattarci />.
      </p>
    </LegalePagina>
  );
}
