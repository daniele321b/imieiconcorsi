import { randomBytes } from "node:crypto";

// Id ordinabili per data (sessioni, richieste, ordini): in DynamoDB le righe di un utente
// escono già dalla più vecchia alla più recente (o al contrario), senza indici in più.

/** Cifre del timestamp in base 36: bastano fino all'anno 5188. */
const TS_LEN = 9;

/** Id ordinabile per data: timestamp base36 a lunghezza fissa + suffisso casuale. */
export function sortableId(date = new Date()) {
  return timePrefix(date) + randomBytes(4).toString("hex");
}

/** Prefisso da usare come limite inferiore in una query su id ordinabili. */
export function timePrefix(date: Date) {
  return date.getTime().toString(36).padStart(TS_LEN, "0");
}
