import { periodo as durata, PIANI, type PianoId, type Periodo } from "./domain";

// Cosa succede al piano in corso quando si compra un piano a pagamento. Senza AWS: la usano il
// sito (pagina Piani, per spiegarlo prima di pagare) e billing (all'acquisto e al pagamento).
//
// - Nessun piano attivo (Free o scaduto): il piano parte adesso per i giorni comprati.
// - Stesso piano già attivo: i giorni comprati si AGGIUNGONO alla scadenza attuale
//   (es. Pro di un anno + trimestrale = la scadenza si sposta di 90 giorni).
// - Medium attivo → Pro: i giorni Medium rimasti diventano giorni Pro in proporzione al prezzo
//   (niente si perde e non conviene comprare Medium per avere Pro a meno), più quelli comprati.
// - Pro attivo → Medium: non si può (si perderebbe il Pro); si aggiunge tempo al Pro, o si
//   compra Medium alla scadenza.

const GIORNO = 86_400_000;

/** Il piano dell'utente adesso: scadenza null o assente = senza scadenza (dato dall'admin). */
export interface PianoAttuale {
  piano: PianoId;
  scadenza?: string | null;
  /** Durata dell'ultimo acquisto: serve a convertire i giorni Medium in Pro */
  periodo?: Periodo;
}

/** Esito del controllo prima di un acquisto: non consentito (con il motivo) oppure che tipo di acquisto è e la nuova scadenza. */
export type EsitoAcquisto =
  | { consentito: false; motivo: string }
  | {
      consentito: true;
      /** nuovo = parte adesso; aggiunta = si allunga il piano attuale; passaggio = Medium → Pro */
      tipo: "nuovo" | "aggiunta" | "passaggio";
      /** Nuova scadenza (ISO) */
      scadenza: string;
      /** Solo passaggio: giorni Medium rimasti e giorni Pro in cui diventano */
      giorniRimasti?: number;
      giorniConvertiti?: number;
    };

/** Data in italiano per i messaggi, es. "10 ottobre 2026". */
const dataIt = (iso: string) => new Intl.DateTimeFormat("it-IT", { day: "numeric", month: "long", year: "numeric", timeZone: "Europe/Rome" }).format(new Date(iso));

/** Esito dell'acquisto di `nuovo` per chi ha `attuale`, calcolato all'istante `ora`. */
export function esitoAcquisto(attuale: PianoAttuale, nuovo: { piano: "medium" | "pro"; periodo: Periodo }, ora = new Date()): EsitoAcquisto {
  const giorni = durata(nuovo.periodo).giorni;
  const adesso = ora.getTime();
  const fine = attuale.scadenza ? Date.parse(attuale.scadenza) : undefined;
  const senzaScadenza = attuale.piano !== "free" && !attuale.scadenza;
  const attivo = attuale.piano !== "free" && (senzaScadenza || (fine !== undefined && fine > adesso));
  // Data ISO a `giorniInPiu` giorni da `base`.
  const da = (base: number, giorniInPiu: number) => new Date(base + giorniInPiu * GIORNO).toISOString();
  // Nome del piano da mostrare all'utente.
  const nome = (p: PianoId) => PIANI[p].nome;

  if (!attivo) return { consentito: true, tipo: "nuovo", scadenza: da(adesso, giorni) };

  if (attuale.piano === "pro" && nuovo.piano === "medium") {
    return {
      consentito: false,
      motivo: senzaScadenza
        ? `Hai già il piano ${nome("pro")}, che comprende tutto il ${nome("medium")}.`
        : `Hai il piano ${nome("pro")} fino al ${dataIt(attuale.scadenza!)}: puoi aggiungere tempo al ${nome("pro")}, oppure acquistare il ${nome("medium")} dopo la scadenza.`,
    };
  }
  if (attuale.piano === nuovo.piano) {
    if (senzaScadenza) return { consentito: false, motivo: `Hai già il piano ${nome(nuovo.piano)} senza scadenza: non serve acquistarlo.` };
    return { consentito: true, tipo: "aggiunta", scadenza: da(fine!, giorni) };
  }
  // Medium → Pro. Un Medium senza scadenza (dato dall'admin) non ha giorni da convertire.
  if (senzaScadenza) return { consentito: true, tipo: "nuovo", scadenza: da(adesso, giorni) };
  const giorniRimasti = Math.ceil((fine! - adesso) / GIORNO);
  const p = attuale.periodo ?? nuovo.periodo;
  const giorniConvertiti = Math.floor((giorniRimasti * PIANI.medium.prezzo[p]) / PIANI.pro.prezzo[p]);
  return { consentito: true, tipo: "passaggio", scadenza: da(adesso, giorniConvertiti + giorni), giorniRimasti, giorniConvertiti };
}
