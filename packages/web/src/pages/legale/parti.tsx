import { Link } from "react-router";
import { datiSocietari, LEGALE } from "../../lib/legale";

// Pezzi di testo comuni alle pagine pubbliche: chi gestisce il servizio e come contattarlo.

/** "iMieiConcorsi (imieiconcorsi.it), …": con i dati della società quando c'è. */
export function Titolare() {
  return datiSocietari ? (
    <>
      {LEGALE.ragioneSociale}, con sede in {LEGALE.sede}, P. IVA {LEGALE.partitaIva}, che gestisce {LEGALE.nome} ({LEGALE.sito})
    </>
  ) : (
    <>
      {LEGALE.nome} ({LEGALE.sito}), progetto in fase di avvio: i dati della società che gestirà il servizio (ragione sociale,
      sede e partita IVA) saranno pubblicati in questa pagina appena costituita
    </>
  );
}

/** Come scriverci: l'email se c'è, sempre il modulo della pagina Contatti. */
export function ComeContattarci() {
  return LEGALE.email ? (
    <>
      all'indirizzo <strong>{LEGALE.email}</strong> o con il modulo della pagina <Link to="/contatti">Contatti</Link>
    </>
  ) : (
    <>
      con il modulo della pagina <Link to="/contatti">Contatti</Link> (o dalla pagina Assistenza, se hai un account)
    </>
  );
}
