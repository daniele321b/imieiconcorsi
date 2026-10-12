import { VERSIONE_TERMINI } from "@imieiconcorsi/core/domain";

// Dati di chi gestisce iMieiConcorsi, per le pagine pubbliche (Privacy, Termini, Chi siamo,
// Contatti…). Per ora il servizio è un progetto in avvio con il nome iMieiConcorsi: la società
// che lo gestirà non è ancora costituita. Appena c'è, compila ragione sociale, sede e partita
// IVA: le pagine li mostrano da sole al posto della frase "in fase di costituzione".
// Prima di accettare pagamenti veri (Stripe live) questi dati servono per legge.

export const LEGALE = {
  /** Nome del servizio */
  nome: "iMieiConcorsi",
  sito: "imieiconcorsi.it",
  /** Società che gestisce il servizio: vuoti finché non è costituita */
  ragioneSociale: "",
  sede: "",
  partitaIva: "",
  /** Email di contatto; vuota = si usa il modulo della pagina /contatti */
  email: "",
  /** Mittente di tutte le email dell'app (SES, ambiente shared) */
  mittente: "noreply@imieiconcorsi.it",
  versione: VERSIONE_TERMINI,
};

/** true quando la società è costituita e i suoi dati sono compilati qui sopra. */
export const datiSocietari = !!(LEGALE.ragioneSociale && LEGALE.sede && LEGALE.partitaIva);
