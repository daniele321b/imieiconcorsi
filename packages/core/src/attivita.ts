import { PutCommand } from "@aws-sdk/lib-dynamodb";
import { createHmac } from "node:crypto";
import { db, tables } from "./db";

// Utenti attivi (pannello admin → Utenti attivi). Alla prima richiesta all'API di ogni minuto e
// di ogni giorno si scrive una riga nella tabella attivita: "m#2026-10-12T10:35" e "g#2026-10-12",
// con un'impronta anonima dell'utente (HMAC dell'id con un segreto), non l'id stesso.
//   online      = utenti diversi negli ultimi 5 minuti;
//   giornalieri = utenti diversi del giorno; settimanali e mensili = unione dei giorni.
// Si conta chi usa l'app (ogni chiamata con login), non chi ha solo il sito aperto in una scheda.
// Le richieste degli admin non contano.

/** Giorni e minuti per cui restano le righe (TTL "scade"). */
const GIORNI_RIGHE_GIORNO = 400;
const GIORNI_RIGHE_MINUTO = 2;

/** "2026-10-12" e "2026-10-12T10:35", in ora italiana (le giornate finiscono a mezzanotte di Roma). */
export function periodi(ora = new Date()) {
  const p = Object.fromEntries(
    new Intl.DateTimeFormat("en-CA", {
      timeZone: "Europe/Rome",
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
      hourCycle: "h23",
    })
      .formatToParts(ora)
      .map((x) => [x.type, x.value]),
  );
  const giorno = `${p.year}-${p.month}-${p.day}`;
  return { giorno, minuto: `${giorno}T${p.hour}:${p.minute}` };
}

/** Impronta anonima dell'utente: stessa persona = stessa impronta, ma non si risale all'id. */
export const impronta = (userId: string) =>
  createHmac("sha256", `attivita:${process.env.ORIGINE_SEGRETA ?? ""}`).update(userId).digest("hex").slice(0, 24);

/**
 * Periodi già segnati da questa Lambda (resta in memoria tra una richiesta e l'altra): così si
 * scrive una volta per minuto e per utente, non a ogni chiamata. Se la memoria cresce troppo
 * si svuota (al massimo si riscrive una riga che c'è già).
 */
const segnati = new Set<string>();

/** Segna l'utente come attivo adesso. Non fallisce mai: un errore qui non deve fermare l'API. */
export async function registraAttivita(userId: string, ora = new Date()) {
  if (!process.env.ATTIVITA_TABLE) return;
  try {
    const { giorno, minuto } = periodi(ora);
    const chi = impronta(userId);
    const secondi = Math.floor(ora.getTime() / 1000);
    const righe = [
      { periodo: `g#${giorno}`, scade: secondi + GIORNI_RIGHE_GIORNO * 86_400 },
      { periodo: `m#${minuto}`, scade: secondi + GIORNI_RIGHE_MINUTO * 86_400 },
    ].filter((r) => !segnati.has(`${r.periodo}|${chi}`));
    if (!righe.length) return;
    if (segnati.size > 50_000) segnati.clear();
    await Promise.all(
      righe.map((r) =>
        db
          .send(
            new PutCommand({
              TableName: tables.attivita,
              Item: { periodo: r.periodo, userId: chi, scade: r.scade },
              // Già segnato da un'altra Lambda: niente da fare.
              ConditionExpression: "attribute_not_exists(userId)",
            }),
          )
          .catch((err) => {
            if (!(err instanceof Error && err.name === "ConditionalCheckFailedException")) throw err;
          })
          .then(() => segnati.add(`${r.periodo}|${chi}`)),
      ),
    );
  } catch (err) {
    console.error("Attività non registrata", err);
  }
}

/** I giorni ("2026-10-12") da `giorno` all'indietro, `quanti` in tutto (il primo è `giorno`). */
export function giorniPrima(giorno: string, quanti: number): string[] {
  const base = Date.parse(`${giorno}T12:00:00Z`);
  return Array.from({ length: quanti }, (_, i) => new Date(base - i * 86_400_000).toISOString().slice(0, 10));
}

/**
 * Dai visitatori di ogni giorno (impronte) ai numeri del pannello: oggi, ieri, ultimi 7 e 30
 * giorni, mese in corso e mese scorso (utenti diversi), e la serie giorno per giorno.
 * `perGiorno` ha i giorni dal più recente (oggi) al più vecchio.
 */
export function riepilogoAttivita(perGiorno: { giorno: string; utenti: string[] }[]) {
  // Utenti diversi in un gruppo di giorni (chi torna più volte conta una volta).
  const unici = (giorni: typeof perGiorno) => new Set(giorni.flatMap((g) => g.utenti)).size;
  const oggi = perGiorno[0]?.giorno ?? "";
  const meseOra = oggi.slice(0, 7);
  const [a, m] = meseOra.split("-").map(Number) as [number, number];
  const meseScorso = m === 1 ? `${a - 1}-12` : `${a}-${String(m - 1).padStart(2, "0")}`;
  return {
    oggi: perGiorno[0]?.utenti.length ?? 0,
    ieri: perGiorno[1]?.utenti.length ?? 0,
    settimana: unici(perGiorno.slice(0, 7)),
    trentaGiorni: unici(perGiorno.slice(0, 30)),
    meseCorrente: unici(perGiorno.filter((g) => g.giorno.startsWith(meseOra))),
    meseScorso: unici(perGiorno.filter((g) => g.giorno.startsWith(meseScorso))),
    serie: perGiorno
      .slice(0, 30)
      .map((g) => ({ giorno: g.giorno, utenti: g.utenti.length }))
      .reverse(),
  };
}
