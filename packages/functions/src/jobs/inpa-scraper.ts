import { BatchWriteCommand } from "@aws-sdk/lib-dynamodb";
import { conModificheAdmin, inizioBandiScaduti, nomeConcorso } from "@imieiconcorsi/core/concorsi";
import { batchGet, db, tables } from "@imieiconcorsi/core/db";
import type { Concorso } from "@imieiconcorsi/core/domain";
import { avvisaAdmin } from "@imieiconcorsi/core/email";
import type { Context } from "aws-lambda";
import { generaCacheBandi } from "./cache-bandi";
import { bandi, bandiAperti, paginaPiuVecchiaDi, toConcorso, type InpaBando } from "./inpa";

// Job del mattino (06:00, EventBridge Scheduler): importa da inPA tutti i bandi aperti e i
// chiusi degli ultimi giorni nella tabella concorsi, avvisa l'admin dei bandi nuovi che citano
// una banca dati e rifà la lista dei bandi in cache (S3 + CloudFront) che legge la ricerca.
// Lanciato a mano con { storico } importa i chiusi degli ultimi 24 mesi (scripts/deploy.sh storico-bandi).
// L'accesso all'API di inPA sta in inpa.ts.

/** Bandi elencati al massimo nell'email all'admin. */
const MAX_NELL_AVVISO = 50;
/** Ogni mattina si ripassano i chiusi degli ultimi giorni (bandi mai visti aperti, rettifiche). */
const GIORNI_CHIUSI_RECENTI = 7;
/** Pagine di chiusi lette al massimo ogni mattina. */
const MAX_PAGINE_CHIUSI_RECENTI = 20;
/** Storico: si smette di leggere pagine quando alla Lambda resta meno di così. */
const MARGINE_MS = 90_000;

const dataBreve = (iso?: string) =>
  iso ? new Intl.DateTimeFormat("it-IT", { day: "2-digit", month: "2-digit", year: "numeric" }).format(new Date(iso)) : "—";

/**
 * Salva una pagina di bandi senza perdere i dati aggiunti dopo l'import (banca dati
 * collegata, concluso, correzioni dell'admin). Restituisce i bandi aperti mai visti prima che
 * citano una banca dati.
 */
export async function salva(pagina: InpaBando[], chiusi: boolean) {
  let concorsi = pagina.map((b) => toConcorso(b));
  const nuoviConBancaDati: Concorso[] = [];

  const esistenti = await batchGet<
    Pick<Concorso, "id" | "bancaDati" | "bancaDatiId" | "conclusoIl" | "primoImportoIl" | "pubblicatoIl" | "modificheAdmin" | "modificatoIl">
  >(tables.concorsi, concorsi.map((c) => ({ id: c.id })), "id, bancaDati, bancaDatiId, conclusoIl, primoImportoIl, pubblicatoIl, modificheAdmin, modificatoIl");
  const giaVisti = new Map(esistenti.map((e) => [e.id, e]));
  const adesso = new Date().toISOString();
  for (const c of concorsi) {
    const prima = giaVisti.get(c.id);
    if (prima) {
      c.bancaDati = prima.bancaDati ?? false;
      if (prima.bancaDatiId) c.bancaDatiId = prima.bancaDatiId;
      if (prima.conclusoIl) c.conclusoIl = prima.conclusoIl;
      // Bandi importati prima di questo campo: contano dalla pubblicazione, così non sembrano tutti nuovi.
      c.primoImportoIl = prima.primoImportoIl ?? prima.pubblicatoIl ?? "1970-01-01T00:00:00.000Z";
      if (prima.modificatoIl) c.modificatoIl = prima.modificatoIl;
    } else if (chiusi) {
      // Un bando già chiuso non è una novità da segnalare a nessuno.
      c.primoImportoIl = c.pubblicatoIl ?? "1970-01-01T00:00:00.000Z";
    } else {
      c.primoImportoIl = adesso;
      if (c.bancaDatiPrevista) nuoviConBancaDati.push(c);
    }
  }

  // Correzioni dell'admin (nome, scadenza…) di nuovo sopra i dati freschi di inPA, che restano
  // come originali per poterle annullare.
  concorsi = concorsi.map((c) => {
    const modifiche = giaVisti.get(c.id)?.modificheAdmin;
    return modifiche ? conModificheAdmin(c, modifiche, true) : c;
  });

  for (let i = 0; i < concorsi.length; i += 25) {
    let pending = concorsi.slice(i, i + 25).map((Item) => ({ PutRequest: { Item } }));
    while (pending.length) {
      const res = await db.send(new BatchWriteCommand({ RequestItems: { [tables.concorsi]: pending } }));
      pending = (res.UnprocessedItems?.[tables.concorsi] ?? []) as typeof pending;
    }
  }
  return nuoviConBancaDati;
}

/** Tutti i bandi aperti, pagina per pagina. */
export async function importaBandi() {
  let totale = 0;
  const nuoviConBancaDati: Concorso[] = [];
  for await (const pagina of bandiAperti()) {
    nuoviConBancaDati.push(...(await salva(pagina, false)));
    totale += pagina.length;
  }
  return { totale, nuoviConBancaDati };
}

/**
 * Bandi chiusi da `daPagina` finché le scadenze arrivano a `finoA` o finisce il tempo.
 * prossimaPagina = da dove riprendere (assente = finito).
 */
export async function importaChiusi(input: { daPagina: number; finoA: string; maxPagine: number; tempoRimasto: () => number }) {
  let totale = 0;
  let pagine = 0;
  for await (const p of bandi("CLOSED", input.daPagina)) {
    await salva(p.bandi, true);
    totale += p.bandi.length;
    pagine++;
    if (p.ultima || paginaPiuVecchiaDi(p.bandi, input.finoA)) return { totale };
    if (pagine >= input.maxPagine || input.tempoRimasto() < MARGINE_MS) return { totale, prossimaPagina: p.pagina + 1 };
  }
  return { totale };
}

/** L'admin lo sa per primo: controlla il bando e, quando esce, si importa la banca dati. */
async function avvisaBancheDati(nuovi: Concorso[]) {
  if (!nuovi.length) return;
  const righe = nuovi
    .slice(0, MAX_NELL_AVVISO)
    .map((c) => `- ${nomeConcorso(c)} — ${c.ente}\n  scade il ${dataBreve(c.scadenza)} · ${c.url}`);
  if (nuovi.length > MAX_NELL_AVVISO) righe.push(`… e altri ${nuovi.length - MAX_NELL_AVVISO}.`);
  await avvisaAdmin(
    `${nuovi.length} nuovi bandi con banca dati`,
    [
      `Oggi su inPA ci sono ${nuovi.length} bandi nuovi che citano una banca dati:`,
      "",
      ...righe,
      "",
      "Quando l'ente pubblica la banca dati, caricala dal pannello: i bandi in attesa sono in",
      `${process.env.SITE_URL ?? ""}/admin/banche-dati#da-caricare`,
    ].join("\n"),
  );
}

/**
 * Ogni mattina: tutti i bandi aperti e i chiusi degli ultimi giorni.
 * Con { storico: { daPagina } } (scripts/deploy.sh storico-bandi): i chiusi degli ultimi
 * MESI_DOPO_SCADENZA mesi, a blocchi; la risposta dice da che pagina continuare.
 */
export const handler = async (event: { storico?: { daPagina?: number } } = {}, context?: Context) => {
  const tempoRimasto = () => context?.getRemainingTimeInMillis() ?? Infinity;

  if (event.storico) {
    const r = await importaChiusi({ daPagina: event.storico.daPagina ?? 0, finoA: inizioBandiScaduti(), maxPagine: Infinity, tempoRimasto });
    console.log(`Storico: importati ${r.totale} bandi chiusi, prossima pagina ${r.prossimaPagina ?? "nessuna (finito)"}`);
    if (r.prossimaPagina === undefined) await generaCacheBandi();
    return { chiusi: r.totale, prossimaPagina: r.prossimaPagina ?? null };
  }

  const { totale, nuoviConBancaDati } = await importaBandi();
  console.log(`Importati ${totale} bandi aperti da inPA, ${nuoviConBancaDati.length} nuovi con banca dati`);
  // Allarme futuro: 0 bandi per 2 giorni = inPA ha cambiato struttura.
  if (totale === 0) {
    await avvisaAdmin("Scraper inPA: nessun bando trovato", "Lo scraper di stamattina non ha trovato bandi: controlla i log.");
    throw new Error("Nessun bando trovato su inPA");
  }
  await avvisaBancheDati(nuoviConBancaDati);

  const limite = new Date(Date.now() - GIORNI_CHIUSI_RECENTI * 86_400_000).toISOString();
  const chiusi = await importaChiusi({ daPagina: 0, finoA: limite, maxPagine: MAX_PAGINE_CHIUSI_RECENTI, tempoRimasto });
  console.log(`Aggiornati ${chiusi.totale} bandi chiusi negli ultimi ${GIORNI_CHIUSI_RECENTI} giorni`);
  // La lista che legge l'app (S3 + CloudFront): rifatta dopo ogni import.
  await generaCacheBandi();
  return { totale, nuoviConBancaDati: nuoviConBancaDati.length, chiusi: chiusi.totale };
};
