import { firmaValida, linkLettura, percorsoSicuro } from "@imieiconcorsi/core/disiscrizione";
import { PIANI } from "@imieiconcorsi/core/domain";
import { scadenzaDa } from "@imieiconcorsi/core/piani";
import { motivoRifiuto } from "@imieiconcorsi/core/sconti";
import { daTogliere } from "@imieiconcorsi/core/seguiti";
import { describe, expect, it } from "vitest";
import { scadenzaPremiata } from "../src/billing/inviti";
import { frequenzaEffettiva, SOGLIA_PAUSA_SETTIMANALE, SOGLIA_SETTIMANALE } from "../src/jobs/avvisi-logic";
import { daCancellare } from "../src/jobs/pulizia-bandi";
import { settimanaDi, usiDellaSettimana } from "../src/study/usi";

const GIORNO = 86_400_000;

describe("prezzi e durate", () => {
  it("listino Medium e Pro con il trimestre", () => {
    expect(PIANI.medium.prezzo).toEqual({ mensile: 9.99, trimestrale: 19.99, annuale: 39.99 });
    expect(PIANI.pro.prezzo).toEqual({ mensile: 14.99, trimestrale: 29.99, annuale: 69.99 });
  });
  it("il trimestre dura 90 giorni", () => {
    const da = new Date("2026-10-09T10:00:00Z");
    expect(Date.parse(scadenzaDa("trimestrale", da)) - da.getTime()).toBe(90 * GIORNO);
  });
  it("il Free ha 3 utilizzi delle banche dati a settimana, gli altri illimitati", () => {
    expect(PIANI.free.limiti.usiBancheDatiSettimana).toBe(3);
    expect(PIANI.medium.limiti.usiBancheDatiSettimana).toBeNull();
  });
});

describe("utilizzi settimanali delle banche dati", () => {
  it("la settimana parte dal lunedì", () => {
    expect(settimanaDi(new Date("2026-10-09T10:00:00Z"))).toBe("2026-10-05"); // venerdì
    expect(settimanaDi(new Date("2026-10-11T23:00:00Z"))).toBe("2026-10-05"); // domenica
    expect(settimanaDi(new Date("2026-10-12T00:30:00Z"))).toBe("2026-10-12"); // lunedì
  });
  it("a settimana nuova si riparte da zero", () => {
    const ora = new Date("2026-10-13T10:00:00Z");
    expect(usiDellaSettimana({ settimana: "2026-10-05", usi: 3, aperte: ["bd_1"] }, ora)).toEqual({ settimana: "2026-10-12", usi: 0, aperte: [] });
    expect(usiDellaSettimana({ settimana: "2026-10-12", usi: 2 }, ora).usi).toBe(2);
  });
});

describe("ritorno al Free: resta seguito l'ultimo concorso", () => {
  it("si tolgono tutti tranne il più recente, lo storico non conta", () => {
    const righe = [
      { userId: "u", concorsoId: "a", dal: "2026-09-01T00:00:00Z" },
      { userId: "u", concorsoId: "b", dal: "2026-10-05T00:00:00Z" },
      { userId: "u", concorsoId: "c", dal: "2026-08-01T00:00:00Z" },
      { userId: "u", concorsoId: "d", dal: "2026-10-08T00:00:00Z", rimossoIl: "2026-10-09T00:00:00Z" },
    ];
    expect(daTogliere(righe, 1).map((r) => r.concorsoId)).toEqual(["a", "c"]);
  });
});

describe("invita un amico", () => {
  const ora = new Date("2026-10-09T10:00:00Z");
  it("30 giorni da oggi, o dalla scadenza se è più avanti", () => {
    expect(scadenzaPremiata(undefined, ora)).toBe(new Date(ora.getTime() + 30 * GIORNO).toISOString());
    expect(scadenzaPremiata("2026-11-01T00:00:00.000Z", ora)).toBe("2026-12-01T00:00:00.000Z");
    expect(scadenzaPremiata("2026-01-01T00:00:00.000Z", ora)).toBe(new Date(ora.getTime() + 30 * GIORNO).toISOString());
  });
  it("un codice invito non vale come codice sconto", () => {
    const invito = { codice: "AMICO-K7MQ2XRT", tipo: "invito" as const, percentuale: 0, usi: 0, attivo: true, creatoIl: "", creatoDa: "" };
    expect(motivoRifiuto(invito, { piano: "medium" })).toMatch(/codice invito/);
  });
});

describe("avvisi solo a chi li legge", () => {
  it("giornaliero → lunedì → pausa, man mano che restano non aperti", () => {
    expect(frequenzaEffettiva("giornaliero", 0)).toBe("giornaliero");
    expect(frequenzaEffettiva("giornaliero", SOGLIA_SETTIMANALE)).toBe("settimanale");
    expect(frequenzaEffettiva("giornaliero", SOGLIA_SETTIMANALE + SOGLIA_PAUSA_SETTIMANALE)).toBe("pausa");
    expect(frequenzaEffettiva("settimanale", SOGLIA_PAUSA_SETTIMANALE - 1)).toBe("settimanale");
    expect(frequenzaEffettiva("settimanale", SOGLIA_PAUSA_SETTIMANALE)).toBe("pausa");
  });
  it("link di lettura firmati, diversi da quelli di disiscrizione", () => {
    const l = linkLettura("utente-1", "https://dev.imieiconcorsi.it", "segreto");
    const t = new URL(l.immagine).searchParams.get("t")!;
    expect(firmaValida("utente-1", t, "segreto", "aperto")).toBe(true);
    expect(firmaValida("utente-1", t, "segreto", "disiscrivi")).toBe(false);
    expect(new URL(l.clic("/app/concorsi/123")).searchParams.get("vai")).toBe("/app/concorsi/123");
  });
  it("il clic porta solo a pagine del sito", () => {
    expect(percorsoSicuro("/app/concorsi/123")).toBe("/app/concorsi/123");
    expect(percorsoSicuro("//evil.example")).toBe("/app");
    expect(percorsoSicuro("https://evil.example")).toBe("/app");
    expect(percorsoSicuro(undefined)).toBe("/app");
  });
});

describe("pulizia dei bandi tolti da inPA", () => {
  it("si cancella solo ciò che non è stato risalvato da più di 3 giorni prima del giro", () => {
    const inizio = "2026-10-11T03:00:00.000Z";
    const righe = [
      { id: "chiuso-ancora-su-inpa", aggiornatoIl: "2026-10-11T03:10:00.000Z" },
      { id: "aperto-di-ieri", aggiornatoIl: "2026-10-10T06:00:00.000Z" },
      { id: "sparito", aggiornatoIl: "2026-10-01T06:00:00.000Z" },
      { id: "senza-data" },
    ];
    expect(daCancellare(righe, inizio).map((r) => r.id)).toEqual(["sparito", "senza-data"]);
  });
});
