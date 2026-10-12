import type { BancaDati } from "@imieiconcorsi/core/domain";

// Pubblicazione di una banca dati estratta: dal file JSON dell'estrazione alle domande che
// vedono gli utenti (tabella questions, materia "bd#<id>"). La usa il pannello admin.

/** Una domanda come la salva l'estrazione in banche-dati/<id>.json. */
export interface DomandaDelFile {
  numero: number;
  testo: string;
  /** Mescolate (vedi parser) */
  opzioni: string[];
  corretta: number;
  sezione?: string;
  /** Ordine del PDF; manca nei file estratti prima del 9 ottobre 2026 */
  pdf?: { opzioni: string[]; corretta: number };
  /** Il PDF dava solo la risposta esatta: le altre sono ricavate da domande simili */
  alternativeRicavate?: boolean;
}

/** Le risposte che vedranno gli utenti, secondo la scelta dell'admin per questa banca dati. */
export function rispostePerUtenti(d: DomandaDelFile, ordine: BancaDati["ordineRisposte"]) {
  // Alternative ricavate: "come nel PDF" vorrebbe dire la giusta sempre per prima. Mescolate.
  if (ordine === "pdf" && !d.alternativeRicavate) {
    if (!d.pdf) throw new Error("Estrazione senza l'ordine del PDF");
    return { opzioni: d.pdf.opzioni, corretta: d.pdf.corretta };
  }
  return { opzioni: d.opzioni, corretta: d.corretta };
}
