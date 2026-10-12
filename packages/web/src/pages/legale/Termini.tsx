import { GIORNI_PREMIO_INVITO, MAX_PREMI_INVITO_ANNO, PIANI } from "@imieiconcorsi/core/domain";
import { Link } from "react-router";
import { euro } from "../../lib/format";
import { LEGALE } from "../../lib/legale";
import { LegalePagina } from "./LegalePagina";
import { ComeContattarci, Titolare } from "./parti";

// Termini e condizioni. I punti su pagamento unico, nessun rinnovo e recesso devono
// restare allineati al flusso di acquisto (pagina Piani e servizio billing).

/** Pagina /termini. */
export function Termini() {
  return (
    <LegalePagina titolo="Termini e condizioni">
      <p>
        Questi termini regolano l'uso di iMieiConcorsi ({LEGALE.sito}). Il servizio è fornito da: <Titolare />. Puoi
        scriverci <ComeContattarci />. Registrandoti li accetti, insieme all'<Link to="/privacy">Informativa sulla privacy</Link>.
      </p>

      <h2>1. Il servizio</h2>
      <p>
        iMieiConcorsi aiuta a prepararsi ai concorsi pubblici: segnala i bandi pubblicati su inPA, propone domande di studio e
        simulazioni d'esame e, nei piani a pagamento, le banche dati ufficiali dei concorsi quando l'ente le pubblica. È uno
        strumento di studio: non garantisce il superamento di alcun concorso. Le informazioni sui
        bandi provengono da fonti pubbliche e possono contenere errori o non essere aggiornate: fa fede sempre il bando
        ufficiale pubblicato dall'ente.
      </p>

      <h2>2. Account</h2>
      <ul>
        <li>Il servizio è riservato ai maggiorenni.</li>
        <li>Ogni persona può avere un solo account. Credenziali e accesso sono personali e non vanno condivisi.</li>
        <li>
          Per registrarti con email e password serve un indirizzo di un provider di posta diffuso (Gmail, Outlook, Libero…);
          gli indirizzi temporanei non sono accettati. Puoi sempre accedere con Google o Facebook.
        </li>
        <li>
          Possiamo sospendere o chiudere un account in caso di uso abusivo, ad esempio la copia sistematica dei contenuti o
          tentativi di accesso non autorizzato.
        </li>
        <li>Puoi eliminare l'account quando vuoi dal tuo profilo.</li>
      </ul>

      <h2>3. Piani e prezzi</h2>
      <ul>
        <li>Il piano {PIANI.free.nome} è gratuito e mostra un annuncio ogni 5 domande di studio; i piani a pagamento sono senza pubblicità.</li>
        <li>
          I piani {PIANI.medium.nome} e {PIANI.pro.nome} sono a pagamento, per 30 giorni, 90 giorni o 365 giorni. Prezzi
          attuali, IVA inclusa ove dovuta: {PIANI.medium.nome} {euro(PIANI.medium.prezzo.mensile)} per 30 giorni,{" "}
          {euro(PIANI.medium.prezzo.trimestrale)} per 90 giorni, {euro(PIANI.medium.prezzo.annuale)} per un anno;{" "}
          {PIANI.pro.nome} {euro(PIANI.pro.prezzo.mensile)} per 30 giorni, {euro(PIANI.pro.prezzo.trimestrale)} per 90 giorni,{" "}
          {euro(PIANI.pro.prezzo.annuale)} per un anno. Il prezzo applicato è quello mostrato al momento dell'acquisto.
        </li>
        <li>
          <strong>Invita un amico.</strong> Ogni utente ha un codice personale. Se un amico lo inserisce prima del suo primo
          acquisto e poi compra un piano, chi l'ha invitato riceve {GIORNI_PREMIO_INVITO} giorni gratis: piano {PIANI.medium.nome} se
          ha il piano {PIANI.free.nome}, altrimenti il suo piano si allunga. Al massimo {MAX_PREMI_INVITO_ANNO} premi l'anno; i premi
          non si convertono in denaro. Gli inviti a sé stessi o con account creati apposta non danno diritto al premio.
        </li>
        <li>
          <strong>Pagamento unico, nessun rinnovo automatico.</strong> Ogni acquisto è un pagamento singolo per il periodo
          scelto. Alla scadenza il piano non si rinnova e l'account torna Free, conservando i progressi. Ti avvisiamo per email 3
          giorni prima della scadenza; per continuare basta un nuovo acquisto.
        </li>
        <li>
          <strong>Acquisti con un piano attivo.</strong> Se acquisti di nuovo lo stesso piano, i giorni acquistati si aggiungono
          alla scadenza attuale (es. un anno di {PIANI.pro.nome} più 90 giorni: la scadenza si sposta di 90 giorni). Se passi da{" "}
          {PIANI.medium.nome} a {PIANI.pro.nome}, i giorni {PIANI.medium.nome} che ti restano diventano giorni {PIANI.pro.nome} in
          proporzione ai prezzi di listino, in aggiunta a quelli acquistati; la pagina Piani te lo mostra prima del pagamento.
          Mentre hai il piano {PIANI.pro.nome} non puoi acquistare il {PIANI.medium.nome}: puoi farlo dopo la scadenza. Il periodo
          residuo non viene rimborsato in denaro.
        </li>
        <li>
          Possiamo offrire codici sconto: ognuno vale una sola volta per account, sui piani e fino alla data indicati, e
          riduce il prezzo del solo acquisto in cui viene usato.
        </li>
        <li>
          <strong>Pagamento:</strong> avviene sulla pagina sicura di Stripe, con carta, PayPal, Apple Pay o Google Pay. Il piano
          si attiva appena Stripe conferma il pagamento; se il pagamento non va a buon fine non ti viene addebitato nulla e il
          piano non cambia. Ti inviamo per email la ricevuta dell'acquisto (puoi farla rimandare da Profilo → I tuoi pagamenti);
          per la fattura scrivici <ComeContattarci />, indicando il codice dell'ordine.
        </li>
      </ul>

      <h2>4. Diritto di recesso e rimborsi</h2>
      <p>
        I piani a pagamento danno accesso immediato a contenuti digitali. Al momento dell'acquisto ti chiediamo di confermare
        espressamente che vuoi l'accesso immediato e che, per questo, <strong>perdi il diritto di recesso</strong> di 14 giorni
        (art. 59, comma 1, lettera o, del Codice del consumo, D.Lgs. 206/2005). Riceverai conferma dell'acquisto e del consenso
        su un supporto durevole.
      </p>
      <p>
        Di conseguenza <strong>i pagamenti non sono rimborsabili</strong>, salvo i casi in cui il rimborso è dovuto per legge:
        ad esempio se il servizio acquistato non ti viene fornito per cause a noi imputabili. Restano fermi tutti i diritti che
        la legge riconosce al consumatore e che non possono essere esclusi da un contratto.
      </p>

      <h2>5. Contenuti</h2>
      <ul>
        <li>
          Le domande sono scritte da noi a partire da libri di testo e da fonti online (voci di Wikipedia, dati ISTAT, testi
          normativi ufficiali) con licenza che ne consente l'uso.
          Per ogni domanda teniamo traccia della fonte precisa. Possono esserci errori: se ne trovi uno, segnalacelo.
        </li>
        <li>
          Le banche dati ufficiali, quando disponibili, sono riportate come pubblicate dall'ente (nei piani Medium e Pro): fa
          fede la versione ufficiale. L'estrazione delle domande dal PDF dell'ente è automatica e può contenere errori.
        </li>
        <li>
          Le funzioni di intelligenza artificiale del piano {PIANI.pro.nome} producono risposte generate automaticamente: sono
          un aiuto allo studio e possono contenere errori, da verificare sulle fonti ufficiali. Rispondono solo su argomenti di
          studio per i concorsi e hanno limiti di utilizzo: un numero massimo di crediti AI al mese, un numero massimo di richieste al minuto e un
          tetto di consumo mensile per account, per un uso corretto e sostenibile del servizio. Se si raggiunge un limite, le
          funzioni AI tornano disponibili il mese successivo (o dopo pochi secondi, per il limite al minuto).
        </li>
        <li>
          Se trovi una domanda o una risposta sbagliata, puoi segnalarla dalla pagina Assistenza o dal link "Segnala un errore"
          sotto la domanda.
        </li>
        <li>
          Testi, domande, spiegazioni e software di iMieiConcorsi sono protetti. Puoi usarli per il tuo studio personale; non
          puoi copiarli, estrarli in modo sistematico o ridistribuirli.
        </li>
      </ul>

      <h2>6. Comunicazioni e feedback</h2>
      <ul>
        <li>
          Ti scriviamo per email per le comunicazioni sul tuo account e sul piano (conferme d'acquisto, scadenze). Gli avvisi
          sui nuovi bandi arrivano solo se li attivi nel profilo e si disattivano dal profilo o con il link in fondo a ogni
          email. Non mandiamo pubblicità per email. L'elenco completo è in <Link to="/email">Le nostre email</Link>.
        </li>
        <li>
          Se ci lasci un parere sull'app dal profilo, possiamo usarlo per migliorare il servizio. Non lo pubblichiamo con il
          tuo nome senza chiederti il permesso.
        </li>
      </ul>

      <h2>7. Disponibilità e responsabilità</h2>
      <p>
        Facciamo il possibile perché il servizio sia sempre disponibile, ma possono esserci interruzioni per manutenzione o
        problemi tecnici. Nei limiti consentiti dalla legge non rispondiamo dei danni indiretti derivanti dall'uso del servizio,
        né delle decisioni prese sulla base delle informazioni sui bandi.
      </p>

      <h2>8. Modifiche</h2>
      <p>
        Possiamo aggiornare questi termini. Le modifiche importanti te le comunichiamo prima che entrino in vigore; i piani già
        acquistati restano regolati dai termini in vigore al momento dell'acquisto.
      </p>

      <h2>9. Reclami e legge applicabile</h2>
      <p>
        Per qualsiasi problema scrivici <ComeContattarci />: rispondiamo entro 15 giorni. Si applica la legge
        italiana. Se sei un consumatore puoi rivolgerti anche a un organismo di risoluzione alternativa delle controversie
        (ADR, artt. 141 e seguenti del Codice del consumo); per le controversie è competente il foro del tuo luogo di residenza
        o domicilio.
      </p>
    </LegalePagina>
  );
}
