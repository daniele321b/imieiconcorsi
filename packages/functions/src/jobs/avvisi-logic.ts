import type { Concorso, FrequenzaAvvisi } from "@imieiconcorsi/core/domain";

const GIORNO = 86_400_000;

/** Data (YYYY-MM-DD) e giorno della settimana in ora italiana. */
function giornoARoma(d: Date) {
  const parti = new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/Rome", year: "numeric", month: "2-digit", day: "2-digit", weekday: "short" })
    .formatToParts(d)
    .reduce<Record<string, string>>((acc, p) => ({ ...acc, [p.type]: p.value }), {});
  return { data: `${parti.year}-${parti.month}-${parti.day}`, lunedi: parti.weekday === "Mon" };
}

/**
 * Oggi va mandato l'avviso? Giornaliero: una volta al giorno. Settimanale: il lunedì.
 * Mai due volte nello stesso giorno (il job si può rilanciare a mano).
 */
export function deveAvvisare(frequenza: FrequenzaAvvisi | undefined, ultimoAvvisoIl: string | undefined, ora = new Date()) {
  if (!frequenza || frequenza === "mai") return false;
  const oggi = giornoARoma(ora);
  if (ultimoAvvisoIl && giornoARoma(new Date(ultimoAvvisoIl)).data === oggi.data) return false;
  return frequenza === "giornaliero" || oggi.lunedi;
}

/**
 * Bandi usciti su inPA ieri (avviso giornaliero) o negli ultimi 7 giorni (settimanale),
 * per data di pubblicazione in ora italiana; quelli di oggi arrivano domani. Senza data di
 * pubblicazione conta il giorno in cui l'app ha visto il bando. Il più vicino alla scadenza prima.
 */
export function bandiNuovi<T extends Pick<Concorso, "primoImportoIl" | "pubblicatoIl" | "scadenza">>(
  concorsi: T[],
  frequenza: Exclude<FrequenzaAvvisi, "mai">,
  ora = new Date(),
) {
  const giorni = new Set(
    Array.from({ length: frequenza === "settimanale" ? 7 : 1 }, (_, i) => giornoARoma(new Date(ora.getTime() - (i + 1) * GIORNO)).data),
  );
  return concorsi
    .filter((c) => {
      const uscito = c.pubblicatoIl ?? c.primoImportoIl;
      return uscito !== undefined && giorni.has(giornoARoma(new Date(uscito)).data);
    })
    .sort((a, b) => (a.scadenza ?? "").localeCompare(b.scadenza ?? ""));
}
