import { Link } from "react-router";
import { LEGALE } from "../../lib/legale";
import { LegalePagina } from "./LegalePagina";
import { ComeContattarci, Titolare } from "./parti";

// Informativa ai sensi degli artt. 13 e 14 del Regolamento (UE) 2016/679 (GDPR).
// Descrive come funziona davvero l'app: se cambia il trattamento, va aggiornata
// insieme a VERSIONE_TERMINI (packages/core/src/domain.ts).

/** Pagina /privacy. */
export function Privacy() {
  return (
    <LegalePagina titolo="Informativa sulla privacy">
      <p>
        Questa informativa spiega quali dati personali tratta iMieiConcorsi ({LEGALE.sito}), perché, per quanto tempo e quali
        diritti hai. Raccogliamo il minimo indispensabile per farti studiare: il tuo nome e la tua email servono solo all'accesso
        e alle comunicazioni di servizio.
      </p>

      <h2>Titolare del trattamento</h2>
      <p>
        <Titolare />. Per qualsiasi richiesta sulla privacy scrivici <ComeContattarci />: rispondiamo entro 30 giorni.
      </p>

      <h2>Quali dati trattiamo</h2>
      <ul>
        <li>
          <strong>Dati dell'account:</strong> email, nome (facoltativo) e password, conservata da Amazon Cognito in forma non
          leggibile. Se accedi con Google o Facebook riceviamo da loro email, nome e un identificativo dell'account; non
          riceviamo la tua password né i tuoi contatti.
        </li>
        <li>
          <strong>Dati di studio:</strong> comparti di interesse, autovalutazione per materia, concorsi seguiti, risposte e
          punteggi delle sessioni. Sono collegati a un identificativo anonimo, non al tuo nome o alla tua email.
        </li>
        <li>
          <strong>Piano e pagamenti:</strong> piano attivo, periodo, data di scadenza e prova del consenso all'acquisto. I
          pagamenti passano da Stripe (anche quando scegli PayPal, Apple Pay o Google Pay): a Stripe comunichiamo l'importo, un
          codice d'ordine e la tua email per la ricevuta. Non vediamo e non conserviamo i dati della tua carta o del tuo conto.
        </li>
        <li>
          <strong>Ordini:</strong> per ogni acquisto un codice d'ordine, piano, periodo, importo, eventuale codice sconto,
          esito del pagamento, e la tua email e il tuo nome come intestatario dell'acquisto.
        </li>
        <li>
          <strong>Inviti:</strong> se ti iscrivi con il link di un amico, salviamo quale account ti ha invitato (identificativo
          anonimo), per dargli il premio quando compri un piano. Per lo stesso motivo lui vede quanti amici si sono iscritti e
          hanno comprato, non chi sono.
        </li>
        <li>
          <strong>Concorsi seguiti:</strong> teniamo lo storico dei concorsi che hai seguito (nome e giorno), che vedi nel profilo.
        </li>
        <li>
          <strong>Parere sull'app:</strong> se lo lasci dal profilo, il voto e il commento; ci arrivano anche per email.
        </li>
        <li>
          <strong>Progressi nelle banche dati:</strong> quali domande di ogni banca dati hai già fatto, quali hai sbagliato
          l'ultima volta e quali hai salvato tra le preferite, per proporti quelle nuove, da ripassare o preferite. Puoi azzerare
          fatte e sbagliate quando vuoi con "Ricomincia".
        </li>
        <li>
          <strong>Richieste di assistenza:</strong> se ci scrivi dalla pagina Assistenza, il tipo di richiesta, i messaggi
          scambiati e, se la richiesta nasce da lì, la domanda, la banca dati, il concorso o l'ordine a cui si riferisce. Ci
          arrivano anche per email; ti avvisiamo per email quando rispondiamo. Non scrivere password o dati della carta.
        </li>
        <li>
          <strong>Tutor AI (solo piano Pro):</strong> quando lo usi, le tue domande al tutor e la domanda di studio su cui chiedi
          vengono inviate al modello di intelligenza artificiale per avere la risposta, senza il tuo nome né la tua email. Non
          conserviamo le conversazioni: salviamo solo quante domande hai fatto al tutor nel mese e il consumo stimato, per i limiti
          di utilizzo. Il tutor risponde solo su argomenti di studio. Non scrivere dati personali nel tutor.
        </li>
        <li>
          <strong>Modulo contatti:</strong> se ci scrivi dalla pagina Contatti, nome, email, argomento e messaggio. Ci arrivano
          per email e li usiamo solo per risponderti; li conserviamo per il tempo necessario a gestire la richiesta e al massimo
          12 mesi. Per evitare invii automatici salviamo per 24 ore un'impronta cifrata del tuo indirizzo IP, non l'indirizzo.
        </li>
        <li>
          <strong>Accessi:</strong> data, ora e modo (email e password, oppure Google o Facebook) di ogni accesso al tuo
          account, per sicurezza e assistenza; si cancellano da soli dopo 12 mesi o subito se elimini l'account.
        </li>
        <li>
          <strong>Dati tecnici:</strong> log dei servizi (data e ora delle richieste, errori), conservati per 14 giorni per
          sicurezza e risoluzione dei problemi.
        </li>
      </ul>

      <h2>Perché li trattiamo e su quale base</h2>
      <ul>
        <li>
          Fornirti il servizio (account, studio, simulazioni, piano acquistato): esecuzione del contratto, art. 6.1.b GDPR.
        </li>
        <li>
          Email di servizio: codici di verifica, conferme d'acquisto, promemoria 3 giorni prima della scadenza del piano,
          avviso quando il piano finisce, avvisi sui nuovi bandi se li hai attivati nel profilo. Base: esecuzione del
          contratto; gli avvisi sui bandi si disattivano dal profilo o con il link "non ricevere più avvisi" in fondo a ogni
          email, senza dover accedere. Se un'email non viene consegnata o viene segnalata come spam, il nostro fornitore ci
          avvisa e smette di scrivere a quell'indirizzo.
        </li>
        <li>
          Avvisi solo a chi li legge: negli avvisi sui bandi un'immagine invisibile e i link ci dicono se l'email è stata
          aperta. Lo usiamo soltanto per contare gli avvisi non aperti di fila: dopo 7 si passa all'invio del lunedì, dopo
          altri 4 gli avvisi si sospendono finché non apri un'email o torni nell'app. Base: legittimo interesse a non mandare
          email inutili; puoi bloccare le immagini nel tuo programma di posta o disattivare gli avvisi dal profilo.
        </li>
        <li>
          Sicurezza e prevenzione degli abusi (per esempio non accettiamo indirizzi email temporanei): legittimo interesse,
          art. 6.1.f GDPR.
        </li>
        <li>Parere sull'app: tuo consenso, art. 6.1.a GDPR; puoi cancellarlo con l'account.</li>
        <li>Obblighi fiscali e contabili sui pagamenti: obbligo di legge, art. 6.1.c GDPR.</li>
      </ul>
      <p>Non facciamo profilazione a fini pubblicitari e non vendiamo né cediamo i tuoi dati.</p>

      <h2>Per quanto tempo</h2>
      <ul>
        <li>
          Dati dell'account e di studio, progressi e richieste di assistenza: finché l'account è attivo. Quando lo elimini
          vengono cancellati subito.
        </li>
        <li>
          Copie di sicurezza del database: si sovrascrivono da sole entro 35 giorni, quindi un dato cancellato sparisce anche da
          lì entro quel termine.
        </li>
        <li>
          Ordini e dati dei pagamenti, con email e nome dell'intestatario: 10 anni, come richiesto dalla legge per le scritture
          contabili (art. 2220 c.c.), anche dopo l'eliminazione dell'account. Non vengono usati per altro.
        </li>
        <li>Log tecnici: 14 giorni. Registro degli accessi: 12 mesi.</li>
      </ul>

      <h2>Dove sono e chi li tratta per noi</h2>
      <ul>
        <li>
          <strong>Amazon Web Services</strong> (Amazon Web Services EMEA SARL): ospita l'app, il database e l'invio delle email
          nella regione di Milano. È nostro responsabile del trattamento. La consegna del sito passa dalla rete CloudFront, che
          può servire le pagine da server fuori dall'Unione Europea. Il tutor AI usa Amazon Bedrock (modelli Claude di
          Anthropic) solo in regioni dell'Unione Europea; i testi inviati non vengono usati per addestrare i modelli.
        </li>
        <li>
          <strong>Google e Meta (Facebook)</strong>: solo se scegli di accedere con loro, per l'autenticazione. Trattano i dati
          secondo le proprie informative.
        </li>
        <li>
          <strong>Stripe</strong> (Stripe Payments Europe, Ltd., Irlanda): solo se acquisti un piano, per il pagamento e la
          ricevuta, secondo la propria informativa; con PayPal anche <strong>PayPal (Europe)</strong>, secondo la propria.
        </li>
      </ul>
      <p>
        Gli eventuali trasferimenti fuori dall'Unione Europea avvengono con le garanzie previste dal GDPR: decisione di
        adeguatezza (EU-US Data Privacy Framework) o clausole contrattuali standard della Commissione europea.
      </p>

      <h2>Cookie e memoria del browser</h2>
      <p>
        Non usiamo cookie di profilazione né strumenti di statistica di terze parti. Il sito salva nella memoria del browser
        solo quanto serve a tenerti collegato (i token di accesso), alcune tue preferenze e, durante una simulazione, le
        risposte già date. Sono strumenti tecnici: non richiedono consenso. L'elenco completo è nella pagina{" "}
        <Link to="/cookie">Cookie</Link>; le email che ti mandiamo sono descritte in <Link to="/email">Le nostre email</Link>.
      </p>
      <p>
        Nel piano Free, tra una domanda e l'altra, mostriamo annunci interni sui nostri piani: non usano cookie e non
        raccolgono dati.
      </p>

      <h2>I tuoi diritti</h2>
      <p>
        Puoi chiedere in qualsiasi momento di accedere ai tuoi dati, correggerli, cancellarli, limitarne il trattamento,
        opporti o riceverli in un formato leggibile (artt. 15–22 GDPR), scrivendoci <ComeContattarci />. Nome,
        interessi e avvisi li modifichi da solo dal profilo; l'account lo elimini dal profilo stesso (vedi{" "}
        <Link to="/eliminazione-dati">Eliminazione dei dati</Link>). Se ritieni che il trattamento violi il GDPR puoi fare
        reclamo al Garante per la protezione dei dati personali (
        <a href="https://www.garanteprivacy.it" target="_blank" rel="noreferrer">
          garanteprivacy.it
        </a>
        ).
      </p>

      <h2>Età</h2>
      <p>Il servizio è rivolto a persone maggiorenni, come i concorsi pubblici a cui prepara.</p>
    </LegalePagina>
  );
}
