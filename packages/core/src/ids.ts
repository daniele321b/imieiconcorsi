import { randomBytes } from "node:crypto";

const TS_LEN = 9;

/** Id ordinabile per data: timestamp base36 a lunghezza fissa + suffisso casuale. */
export function sortableId(date = new Date()) {
  return timePrefix(date) + randomBytes(4).toString("hex");
}

/** Prefisso da usare come limite inferiore in una query su id ordinabili. */
export function timePrefix(date: Date) {
  return date.getTime().toString(36).padStart(TS_LEN, "0");
}
