import { Link } from "react-router";
import { datiSocietari, LEGALE } from "../../lib/legale";

// Pezzi di testo comuni alle pagine pubbliche: chi gestisce il servizio e come contattarlo.

/** Chi gestisce il servizio: i dati societari se compilati in lib/legale.ts, altrimenti solo il nome del servizio. */
export function Titolare() {
  return datiSocietari ? (
    <>
      {LEGALE.ragioneSociale}, con sede in {LEGALE.sede}, P. IVA {LEGALE.partitaIva}, che gestisce {LEGALE.nome} ({LEGALE.sito})
    </>
  ) : (
    <>
      {LEGALE.nome} ({LEGALE.sito})
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
