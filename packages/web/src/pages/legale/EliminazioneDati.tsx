import { Link } from "react-router";
import { LegalePagina } from "./LegalePagina";
import { ComeContattarci } from "./parti";

// Istruzioni per l'eliminazione dei dati: richieste anche da Meta (Facebook Login) e Google.

/** Pagina /eliminazione-dati (pubblica: la chiedono anche Meta e Google). */
export function EliminazioneDati() {
  return (
    <LegalePagina titolo="Eliminazione dei dati">
      <p>Puoi eliminare il tuo account e i dati collegati in qualsiasi momento, anche se ti sei registrato con Google o Facebook.</p>

      <h2>Dal sito, in un minuto</h2>
      <ul>
        <li>Accedi e apri il tuo <strong>Profilo</strong>.</li>
        <li>
          In fondo alla pagina premi <strong>Elimina account</strong> e conferma scrivendo <strong>ELIMINA</strong>.
        </li>
      </ul>

      <h2>Cosa viene cancellato</h2>
      <ul>
        <li>Email, nome e accesso, compreso il collegamento con Google o Facebook.</li>
        <li>Profilo di studio: interessi, livelli, concorsi seguiti, sessioni, risposte, statistiche e progressi nelle banche dati.</li>
        <li>Richieste di assistenza e i loro messaggi.</li>
        <li>Piano attivo: l'eventuale periodo residuo non viene rimborsato.</li>
      </ul>
      <p>
        La cancellazione è immediata. Dalle copie di sicurezza del database i dati spariscono entro 35 giorni. Restano solo i
        dati dei pagamenti (ordini, con l'email e il nome dell'intestatario), conservati per 10 anni per obbligo di legge, come spiegato nell'
        <Link to="/privacy">Informativa sulla privacy</Link>.
      </p>

      <h2>Se non riesci ad accedere</h2>
      <p>
        Scrivici <ComeContattarci />, indicando l'indirizzo email del tuo account e chiedendo l'eliminazione: per sicurezza
        ti chiederemo conferma da quell'indirizzo. Rispondiamo entro 30 giorni.
      </p>

      <h2>Se usavi Facebook o Google</h2>
      <p>
        Dopo aver eliminato l'account puoi anche togliere iMieiConcorsi dalle app collegate: su Facebook in Impostazioni e privacy
        → Impostazioni → App e siti web; su Google in Account Google → Sicurezza → Connessioni a terze parti.
      </p>
    </LegalePagina>
  );
}
