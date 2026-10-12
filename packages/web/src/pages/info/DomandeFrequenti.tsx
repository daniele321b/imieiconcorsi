import { COSTI_AI, GETTONI_AI_PRO, PIANI, SIMULAZIONE_MAX, USI_BANCHE_DATI_FREE } from "@imieiconcorsi/core/domain";
import { ChevronDown } from "lucide-react";
import type { ReactNode } from "react";
import { Link } from "react-router";
import { LegalePagina } from "../legale/LegalePagina";
import { ComeContattarci } from "../legale/parti";

// Pagina pubblica /domande-frequenti. Le risposte devono restare vere: i numeri vengono da
// core/domain.ts, il resto va aggiornato quando cambia il funzionamento dell'app.

/** Domande e risposte, raggruppate. */
const GRUPPI: { titolo: string; voci: { d: string; r: ReactNode }[] }[] = [
  {
    titolo: "Il servizio",
    voci: [
      {
        d: "Da dove arrivano i bandi?",
        r: (
          <>
            Dal portale pubblico inPA, che leggiamo ogni mattina. In ogni scheda c'è il link al bando ufficiale, che fa sempre
            fede: le informazioni possono contenere errori o non essere aggiornate.
          </>
        ),
      },
      {
        d: "Cosa sono le banche dati ufficiali?",
        r: (
          <>
            Per molti concorsi l'ente pubblica in anticipo l'elenco delle domande da cui sarà estratta la prova. Le carichiamo
            appena escono: puoi consultarle una per una, studiarle con la correzione subito e fare simulazioni. Con il Free hai{" "}
            {USI_BANCHE_DATI_FREE} utilizzi a settimana, con Medium e Pro sono illimitate.
          </>
        ),
      },
      {
        d: "Come funzionano le simulazioni?",
        r: (
          <>
            Come la prova vera: domande a tempo (un minuto a domanda), risposta giusta +1, sbagliata −0,25, non data 0. Con Medium
            e Pro scegli quante domande, fino a {SIMULAZIONE_MAX}.
          </>
        ),
      },
      {
        d: "Cos'è il tutor AI?",
        r: (
          <>
            Nel piano Pro un assistente con intelligenza artificiale ti spiega perché una risposta è giusta o sbagliata e prepara
            allenamenti sugli argomenti in cui sbagli. Hai {GETTONI_AI_PRO} crediti AI al mese: {COSTI_AI.tutor} per ogni domanda
            al tutor, {COSTI_AI.allenamento} per un allenamento. Le risposte possono contenere errori: verifica sempre sulle fonti
            ufficiali.
          </>
        ),
      },
    ],
  },
  {
    titolo: "Piani e pagamenti",
    voci: [
      {
        d: "Il piano si rinnova da solo?",
        r: (
          <>
            No. Ogni acquisto è un pagamento unico per 30 giorni, 90 giorni o un anno. Alla scadenza torni al {PIANI.free.nome}{" "}
            con tutti i progressi; ti avvisiamo per email 3 giorni prima. Vedi <Link to="/prezzi">Prezzi</Link>.
          </>
        ),
      },
      {
        d: "Come posso pagare?",
        r: <>Con carta, PayPal, Apple Pay o Google Pay, sulla pagina sicura di Stripe. Non vediamo i dati della tua carta.</>,
      },
      {
        d: "Posso avere un rimborso?",
        r: (
          <>
            L'accesso ai contenuti è immediato, quindi al momento dell'acquisto rinunci al recesso di 14 giorni; restano i
            rimborsi dovuti per legge, per esempio se il servizio non ti viene fornito. Dettagli nei{" "}
            <Link to="/termini">Termini e condizioni</Link>, punto 4.
          </>
        ),
      },
      {
        d: "Dove trovo la ricevuta?",
        r: <>Arriva per email dopo il pagamento; puoi farla rimandare da Profilo → I tuoi pagamenti.</>,
      },
    ],
  },
  {
    titolo: "Account, email e dati",
    voci: [
      {
        d: "Che email mi mandate?",
        r: (
          <>
            Solo email legate al tuo account (codici di accesso, ricevute, scadenza del piano, risposte dell'assistenza) e, se li
            attivi, gli avvisi sui nuovi bandi. Niente pubblicità. L'elenco completo è in{" "}
            <Link to="/email">Le nostre email</Link>.
          </>
        ),
      },
      {
        d: "Come smetto di ricevere gli avvisi sui bandi?",
        r: <>Dal profilo, oppure con il link "non ricevere più avvisi" in fondo a ogni avviso: basta un clic, senza accedere.</>,
      },
      {
        d: "Come elimino il mio account?",
        r: (
          <>
            Dal Profilo, in fondo alla pagina: la cancellazione è immediata. Tutti i passaggi sono in{" "}
            <Link to="/eliminazione-dati">Eliminazione dei dati</Link>.
          </>
        ),
      },
      {
        d: "Che dati raccogliete?",
        r: (
          <>
            Il minimo per farti studiare: email, nome facoltativo, i tuoi progressi e gli eventuali acquisti. Non vendiamo né
            cediamo i dati. Tutto è spiegato nell'<Link to="/privacy">Informativa sulla privacy</Link>.
          </>
        ),
      },
    ],
  },
];

/** Pagina /domande-frequenti. */
export function DomandeFrequenti() {
  return (
    <LegalePagina titolo="Domande frequenti" versione={false}>
      {GRUPPI.map((g) => (
        <section key={g.titolo}>
          <h2>{g.titolo}</h2>
          <div className="mt-3 divide-y divide-slate-100 rounded-2xl bg-white shadow-sm ring-1 ring-slate-200/70">
            {g.voci.map((v) => (
              <details key={v.d} className="group px-4 py-3">
                <summary className="flex cursor-pointer list-none items-center justify-between gap-3 font-semibold text-slate-900">
                  {v.d}
                  <ChevronDown className="size-4 shrink-0 text-slate-400 transition group-open:rotate-180" />
                </summary>
                <p className="mt-2 text-slate-600">{v.r}</p>
              </details>
            ))}
          </div>
        </section>
      ))}
      <h2>Non hai trovato la risposta?</h2>
      <p>
        Scrivici <ComeContattarci />.
      </p>
    </LegalePagina>
  );
}
