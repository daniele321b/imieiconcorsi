import { VERSIONE_TERMINI } from "@imieiconcorsi/core/domain";

// Dati del titolare per Informativa privacy e Termini. DA COMPLETARE prima del lancio:
// finché restano tra parentesi quadre, le pagine mostrano l'avviso "bozza".
export const LEGALE = {
  titolare: "[Nome e cognome o ragione sociale]",
  indirizzo: "[Indirizzo completo]",
  partitaIva: "[Partita IVA o codice fiscale]",
  email: "[email di contatto, es. privacy@imieiconcorsi.it]",
  sito: "imieiconcorsi.it",
  versione: VERSIONE_TERMINI,
};

/** true finché qualche dato è ancora tra parentesi quadre: le pagine legali mostrano "bozza". */
export const legaleInBozza = Object.values(LEGALE).some((v) => v.startsWith("["));
