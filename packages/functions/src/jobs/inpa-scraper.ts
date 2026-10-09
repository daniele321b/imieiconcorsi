import { BatchWriteCommand } from "@aws-sdk/lib-dynamodb";
import { batchGet, db, tables } from "@imieiconcorsi/core/db";
import type { Concorso } from "@imieiconcorsi/core/domain";
import { avvisaAdmin } from "@imieiconcorsi/core/email";
import { bandiAperti, toConcorso } from "./inpa";

const MAX_NELL_AVVISO = 50;

const dataBreve = (iso?: string) =>
  iso ? new Intl.DateTimeFormat("it-IT", { day: "2-digit", month: "2-digit", year: "numeric" }).format(new Date(iso)) : "—";

export async function importaBandi() {
  let totale = 0;
  const nuoviConBancaDati: Concorso[] = [];

  for await (const pagina of bandiAperti()) {
    const concorsi = pagina.map((b) => toConcorso(b));

    // Cosa c'è già: per riconoscere i bandi nuovi e non perdere i dati aggiunti dopo
    // l'import (es. banca dati ufficiale già importata).
    const esistenti = await batchGet<Pick<Concorso, "id" | "bancaDati" | "bancaDatiId" | "conclusoIl" | "primoImportoIl" | "pubblicatoIl">>(
      tables.concorsi,
      concorsi.map((c) => ({ id: c.id })),
      "id, bancaDati, bancaDatiId, conclusoIl, primoImportoIl, pubblicatoIl",
    );
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
      } else {
        c.primoImportoIl = adesso;
        if (c.bancaDatiPrevista) nuoviConBancaDati.push(c);
      }
    }

    for (let i = 0; i < concorsi.length; i += 25) {
      let pending = concorsi.slice(i, i + 25).map((Item) => ({ PutRequest: { Item } }));
      while (pending.length) {
        const res = await db.send(new BatchWriteCommand({ RequestItems: { [tables.concorsi]: pending } }));
        pending = (res.UnprocessedItems?.[tables.concorsi] ?? []) as typeof pending;
      }
    }
    totale += concorsi.length;
  }
  return { totale, nuoviConBancaDati };
}

/** L'admin lo sa per primo: controlla il bando e, quando esce, si importa la banca dati. */
async function avvisaBancheDati(nuovi: Concorso[]) {
  if (!nuovi.length) return;
  const righe = nuovi
    .slice(0, MAX_NELL_AVVISO)
    .map((c) => `- ${c.ente} — ${c.figura ?? c.titolo}\n  scade il ${dataBreve(c.scadenza)} · ${c.url}`);
  if (nuovi.length > MAX_NELL_AVVISO) righe.push(`… e altri ${nuovi.length - MAX_NELL_AVVISO}.`);
  await avvisaAdmin(
    `${nuovi.length} nuovi bandi con banca dati`,
    [`Oggi su inPA ci sono ${nuovi.length} bandi nuovi che citano una banca dati:`, "", ...righe].join("\n"),
  );
}

export const handler = async () => {
  const { totale, nuoviConBancaDati } = await importaBandi();
  console.log(`Importati ${totale} bandi aperti da inPA, ${nuoviConBancaDati.length} nuovi con banca dati`);
  // Allarme futuro: 0 bandi per 2 giorni = inPA ha cambiato struttura.
  if (totale === 0) {
    await avvisaAdmin("Scraper inPA: nessun bando trovato", "Lo scraper di stamattina non ha trovato bandi: controlla i log.");
    throw new Error("Nessun bando trovato su inPA");
  }
  await avvisaBancheDati(nuoviConBancaDati);
  return { totale, nuoviConBancaDati: nuoviConBancaDati.length };
};
