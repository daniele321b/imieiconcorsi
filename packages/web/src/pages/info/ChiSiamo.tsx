import { Link } from "react-router";
import { datiSocietari } from "../../lib/legale";
import { LegalePagina } from "../legale/LegalePagina";
import { ComeContattarci, Titolare } from "../legale/parti";

// Pagina pubblica /chi-siamo: cos'è iMieiConcorsi, chi lo gestisce, da dove vengono bandi e
// domande, come si sostiene. La guardano anche Stripe e AWS quando valutano il servizio.

/** Pagina /chi-siamo. */
export function ChiSiamo() {
  return (
    <LegalePagina titolo="Chi siamo" sotto="Un'app per prepararsi ai concorsi pubblici italiani, dal bando alla prova." versione={false}>
      <h2>Cosa facciamo</h2>
      <p>
        iMieiConcorsi aiuta chi vuole entrare nella pubblica amministrazione a trovare i bandi giusti e a prepararsi bene.
        Ogni mattina leggiamo i nuovi bandi pubblicati sul portale inPA e avvisiamo chi li ha chiesti; per ogni concorso
        proponiamo lo studio delle materie d'esame, simulazioni a tempo con le regole della prova e, quando l'ente le pubblica,
        le banche dati ufficiali di domande. Nel piano Pro c'è anche un tutor con intelligenza artificiale che spiega errori e
        argomenti.
      </p>

      <h2>Chi c'è dietro</h2>
      <p>
        iMieiConcorsi è un progetto indipendente nato in Italia nel 2026 ed è in fase di avvio: lo stiamo facendo crescere
        insieme ai primi utenti, ascoltando i loro pareri.{datiSocietari && <> Gestore del servizio: <Titolare />.</>}
      </p>

      <h2>Indipendenti dagli enti</h2>
      <p>
        Non siamo affiliati al Dipartimento della Funzione Pubblica, al portale inPA né ad alcun ente che bandisce concorsi. Le
        informazioni sui bandi vengono da fonti pubbliche e possono contenere errori o non essere aggiornate: fa fede sempre il
        bando ufficiale, che colleghiamo in ogni scheda.
      </p>

      <h2>Da dove vengono le domande</h2>
      <ul>
        <li>
          Le domande di studio le scriviamo noi, a partire da libri di testo e da fonti con licenza che ne consente l'uso
          (testi normativi ufficiali, dati ISTAT, voci di Wikipedia). Per ognuna teniamo traccia della fonte.
        </li>
        <li>
          Le banche dati ufficiali sono riportate come pubblicate dall'ente per il concorso. Se trovi un errore, puoi segnalarlo
          sotto ogni domanda.
        </li>
      </ul>

      <h2>Come ci sosteniamo</h2>
      <p>
        Con i piani a pagamento Medium e Pro, senza abbonamenti che si rinnovano da soli (vedi <Link to="/prezzi">Prezzi</Link>).
        Il piano Free è gratuito e mostra solo annunci dei nostri piani. Non vendiamo né cediamo i dati di nessuno e non mandiamo
        pubblicità per email.
      </p>

      <h2>Scrivici</h2>
      <p>
        Per domande, proposte o problemi scrivici <ComeContattarci />.
      </p>
    </LegalePagina>
  );
}
