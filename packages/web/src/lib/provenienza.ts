import { PARAMETRI_UTM, provenienzaDa, queryProvenienza } from "@imieiconcorsi/core/provenienza";

// Link dei social e degli annunci con i parametri UTM (https://…/?utm_source=instagram&…): la
// provenienza si ricorda nel browser fino all'iscrizione, al massimo 30 giorni, e parte con il primo
// GET /me (lib/auth.tsx), che la salva solo nel profilo appena creato. Vale il primo link aperto.
// Elencata nella pagina /cookie.

const CHIAVE = "provenienza";
const DURATA_MS = 30 * 24 * 60 * 60 * 1000;

/** Parametri UTM ricordati, se ci sono e non sono scaduti (gli scaduti si cancellano). */
function ricordati(): Record<string, unknown> | undefined {
  try {
    const salvati = localStorage.getItem(CHIAVE);
    if (!salvati) return undefined;
    const valori = JSON.parse(salvati) as Record<string, unknown>;
    if (typeof valori.il === "number" && Date.now() - valori.il < DURATA_MS) return valori;
    localStorage.removeItem(CHIAVE);
  } catch {}
  return undefined;
}

/** All'avvio: se l'indirizzo ha ?utm_source= e non c'è già una provenienza, la si tiene da parte. */
export function ricordaProvenienza() {
  try {
    if (ricordati()) return;
    const query = new URLSearchParams(window.location.search);
    const valori = Object.fromEntries(Object.keys(PARAMETRI_UTM).map((p) => [p, query.get(p) ?? undefined]));
    if (provenienzaDa(valori)) localStorage.setItem(CHIAVE, JSON.stringify({ ...valori, il: Date.now() }));
  } catch {}
}

/** Query string da aggiungere a GET /me ("?utm_source=…"), o "" se non c'è provenienza. */
export function parametriProvenienza() {
  const valori = ricordati();
  const provenienza = valori && provenienzaDa(valori);
  return provenienza ? queryProvenienza(provenienza) : "";
}

/** Dopo il primo GET /me riuscito: il server l'ha salvata (profilo nuovo) o ignorata (account già esistente). */
export function dimenticaProvenienza() {
  try {
    localStorage.removeItem(CHIAVE);
  } catch {}
}
