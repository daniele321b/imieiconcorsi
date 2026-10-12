import { Link } from "react-router";
import { LEGALE } from "../../lib/legale";
import { LegalePagina } from "../legale/LegalePagina";
import { ComeContattarci } from "../legale/parti";

// Pagina pubblica /email: tutte le email che l'app manda, quando, e come smettere di
// riceverle. Deve restare allineata al codice: core/email-piani.ts, billing/ordini.ts,
// billing/inviti.ts, jobs/scadenze.ts, jobs/avvisi.ts, admin/handler.ts (risposte), Cognito.
// AWS la guarda quando valuta l'uscita di SES dalla sandbox.

/** Le email, nell'ordine in cui di solito si ricevono. */
const EMAIL: { nome: string; quando: string; frequenza: string; stop: string }[] = [
  {
    nome: "Codice di verifica",
    quando: "Quando ti registri con email e password o chiedi di reimpostare la password.",
    frequenza: "Solo quando lo chiedi tu",
    stop: "Necessaria per l'accesso",
  },
  {
    nome: "Ricevuta dell'acquisto",
    quando: "Dopo ogni pagamento di un piano, con importo, periodo e scadenza.",
    frequenza: "Una per acquisto",
    stop: "Necessaria (documento dell'acquisto)",
  },
  {
    nome: "Piano attivato",
    quando: "Quando ti attiviamo un piano a pagamento (per esempio un omaggio o dopo una richiesta di assistenza).",
    frequenza: "Una per attivazione",
    stop: "Necessaria (riguarda il tuo account)",
  },
  {
    nome: "Giorni gratis per un invito",
    quando: "Quando un amico che hai invitato compra un piano e ricevi i giorni in regalo.",
    frequenza: "Una per premio",
    stop: "Necessaria (riguarda il tuo account)",
  },
  {
    nome: "Promemoria di scadenza",
    quando: "3 giorni prima della scadenza di un piano a pagamento.",
    frequenza: "Una per piano",
    stop: "Necessaria (riguarda il tuo account)",
  },
  {
    nome: "Piano scaduto",
    quando: "Quando il piano a pagamento finisce e l'account torna al Free.",
    frequenza: "Una per piano",
    stop: "Necessaria (riguarda il tuo account)",
  },
  {
    nome: "Risposta dell'assistenza",
    quando: "Quando rispondiamo a una tua richiesta di assistenza.",
    frequenza: "Una per risposta",
    stop: "Necessaria (l'hai chiesta tu)",
  },
  {
    nome: "Nuovi bandi per te",
    quando: "Solo se li attivi nel profilo: i bandi usciti nei comparti che hai scelto.",
    frequenza: "Al massimo una al giorno, oppure una a settimana (lunedì)",
    stop: "Dal profilo o con un clic sul link in fondo all'email, senza accedere",
  },
];

/** Pagina /email. */
export function LeNostreEmail() {
  return (
    <LegalePagina titolo="Le nostre email" sotto="Cosa ti scriviamo, quando e come smettere di riceverlo." versione={false}>
      <p>
        Scriviamo solo alle persone che si sono registrate su {LEGALE.sito} con il proprio indirizzo, e solo per cose che
        riguardano il loro account o che hanno chiesto. <strong>Non mandiamo pubblicità né newsletter</strong>, non compriamo e
        non usiamo elenchi di indirizzi di altri, non cediamo il tuo indirizzo a nessuno.
      </p>
      <p>
        Le email partono da <strong>{LEGALE.mittente}</strong> (iMieiConcorsi). I codici di verifica dell'accesso possono arrivare
        da un indirizzo del servizio di autenticazione che usiamo (Amazon Cognito).
      </p>

      <h2>Tutte le email</h2>
      <div className="not-prose space-y-2">
        {EMAIL.map((e) => (
          <div key={e.nome} className="rounded-2xl bg-white p-4 text-sm shadow-sm ring-1 ring-slate-200/70">
            <p className="font-semibold text-slate-900">{e.nome}</p>
            <p className="mt-1 text-slate-600">{e.quando}</p>
            <dl className="mt-2 grid gap-x-4 gap-y-1 text-xs sm:grid-cols-2">
              <div>
                <dt className="inline font-semibold text-slate-500">Quante: </dt>
                <dd className="inline text-slate-700">{e.frequenza}</dd>
              </div>
              <div>
                <dt className="inline font-semibold text-slate-500">Per smettere: </dt>
                <dd className="inline text-slate-700">{e.stop}</dd>
              </div>
            </dl>
          </div>
        ))}
      </div>

      <h2>Gli avvisi sui nuovi bandi</h2>
      <ul>
        <li>Sono spenti finché non li attivi tu dal profilo, scegliendo i comparti e la frequenza.</li>
        <li>
          Ogni avviso dice perché lo ricevi e ha in fondo il link "non ricevere più avvisi": un clic e confermi, senza accedere.
          I programmi di posta come Gmail mostrano anche il pulsante "Annulla iscrizione", che funziona allo stesso modo.
        </li>
        <li>
          Li mandiamo solo a chi li legge: dopo 7 avvisi giornalieri non aperti di fila passiamo a uno a settimana, e dopo altri 4
          non aperti li sospendiamo finché non torni nell'app o apri un'email.
        </li>
      </ul>

      <h2>Indirizzi che non funzionano</h2>
      <p>
        Se un'email torna indietro perché l'indirizzo non esiste, o se qualcuno la segnala come spam, smettiamo subito di
        scrivere a quell'indirizzo e lo controlliamo noi. Se pensi di non ricevere più le nostre email per questo, scrivici{" "}
        <ComeContattarci />.
      </p>

      <h2>Non ti aspettavi una nostra email?</h2>
      <p>
        Può succedere se qualcuno ha usato il tuo indirizzo per registrarsi. Scrivici <ComeContattarci /> e lo rimuoviamo; per
        gli avvisi puoi anche usare il link in fondo all'email. Come trattiamo i dati è spiegato nell'
        <Link to="/privacy">Informativa sulla privacy</Link>.
      </p>
    </LegalePagina>
  );
}
