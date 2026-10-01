/** Giorni di preavviso per l'email "il tuo piano sta per scadere". */
export const GIORNI_PREAVVISO = 3;

export type Azione = "nessuna" | "promemoria" | "scaduto";

/**
 * Cosa fare oggi per un abbonato: senza scadenza (piano dato a mano dall'admin) nulla;
 * scaduto → torna Free; entro 3 giorni → promemoria, una volta sola per quella scadenza.
 */
export function azionePerAbbonato(
  scadenza: string | undefined,
  promemoriaInviatoPer: string | undefined,
  oggi = new Date(),
): Azione {
  if (!scadenza) return "nessuna";
  const mancano = Date.parse(scadenza) - oggi.getTime();
  if (mancano <= 0) return "scaduto";
  if (mancano <= GIORNI_PREAVVISO * 86_400_000 && promemoriaInviatoPer !== scadenza) return "promemoria";
  return "nessuna";
}
