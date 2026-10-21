import { VERSIONE_TERMINI } from "@imieiconcorsi/core/domain";
import { config } from "./config";

// Dati di chi gestisce iMieiConcorsi, per le pagine pubbliche (Privacy, Termini, Chi siamo,
// Contatti…). Finché ragione sociale, sede e partita IVA sono vuote le pagine non parlano di
// società: dicono solo "iMieiConcorsi (imieiconcorsi.it)". Compilati, compaiono da soli in
// Privacy, Termini e Chi siamo.
// Prima di accettare pagamenti veri (Stripe live) questi dati servono per legge.

export const LEGALE = {
  /** Nome del servizio */
  nome: "iMieiConcorsi",
  sito: "imieiconcorsi.it",
  /** Società che gestisce il servizio: vuoti finché non è costituita */
  ragioneSociale: "",
  sede: "",
  partitaIva: "",
  /** Mittente di tutte le email dell'app (SES, ambiente shared) */
  mittente: "noreply@imieiconcorsi.it",
  versione: VERSIONE_TERMINI,
};

/**
 * Email di contatto dell'ambiente (info@ in prod, info-dev@ in dev), da config.json: la scrive
 * Terraform (app_config.emailContatti). La posta per questi indirizzi arriva all'admin
 * (modules/posta-in-arrivo). Vuota = si usa solo il modulo della pagina /contatti.
 */
export const emailContatti = (): string => config?.emailContatti ?? "";

/** true quando la società è costituita e i suoi dati sono compilati qui sopra. */
export const datiSocietari = !!(LEGALE.ragioneSociale && LEGALE.sede && LEGALE.partitaIva);
