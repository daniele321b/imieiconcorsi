import { api } from "./api";

// Link "invita un amico": https://…/?invito=AMICO-XXXX. Il codice si ricorda nel browser
// finché l'amico non ha un account, poi si manda una volta al server.

const CHIAVE = "invito";

/** All'avvio: se l'indirizzo ha ?invito=, lo si tiene da parte. */
export function ricordaInvito() {
  try {
    const codice = new URLSearchParams(window.location.search).get("invito");
    if (codice && /^[A-Za-z0-9-]{4,24}$/.test(codice)) localStorage.setItem(CHIAVE, codice.toUpperCase());
  } catch {}
}

/** Dopo l'accesso: manda il codice ricordato. Va bene anche se non vale più (es. account già usato). */
export async function inviaInvitoRicordato() {
  let codice: string | null = null;
  try {
    codice = localStorage.getItem(CHIAVE);
  } catch {}
  if (!codice) return;
  try {
    await api("/me/invito", { method: "POST", body: { codice } });
  } catch {
    // Codice non valido, proprio, o già un acquisto fatto: non si riprova.
  }
  try {
    localStorage.removeItem(CHIAVE);
  } catch {}
}
