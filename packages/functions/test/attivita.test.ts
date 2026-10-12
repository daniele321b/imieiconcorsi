import { giorniPrima, impronta, periodi, riepilogoAttivita } from "@imieiconcorsi/core/attivita";
import { describe, expect, it } from "vitest";

describe("utenti attivi", () => {
  it("giorni e minuti in ora italiana", () => {
    // 23:30 UTC del 12 ottobre = 01:30 del 13 a Roma (ora legale).
    expect(periodi(new Date("2026-10-12T23:30:00Z"))).toEqual({ giorno: "2026-10-13", minuto: "2026-10-13T01:30" });
    // Inverno: UTC+1.
    expect(periodi(new Date("2026-12-31T23:15:00Z"))).toEqual({ giorno: "2027-01-01", minuto: "2027-01-01T00:15" });
  });

  it("giorni all'indietro, anche a cavallo dei mesi e del cambio d'ora", () => {
    expect(giorniPrima("2026-11-02", 4)).toEqual(["2026-11-02", "2026-11-01", "2026-10-31", "2026-10-30"]);
    expect(giorniPrima("2026-03-30", 3)).toEqual(["2026-03-30", "2026-03-29", "2026-03-28"]);
  });

  it("impronta stabile e diversa per utenti diversi", () => {
    expect(impronta("abc")).toBe(impronta("abc"));
    expect(impronta("abc")).not.toBe(impronta("abd"));
    expect(impronta("abc")).not.toContain("abc");
  });

  it("settimanali e mensili contano le persone una volta sola", () => {
    const giorni = giorniPrima("2026-11-03", 40).map((giorno, i) => ({
      giorno,
      utenti: i === 0 ? ["a", "b"] : i === 1 ? ["a"] : i === 5 ? ["c"] : i === 10 ? ["d"] : i === 35 ? ["e"] : [],
    }));
    const r = riepilogoAttivita(giorni);
    expect(r.oggi).toBe(2);
    expect(r.ieri).toBe(1);
    expect(r.settimana).toBe(3); // a, b, c
    expect(r.trentaGiorni).toBe(4); // + d
    expect(r.meseCorrente).toBe(2); // 1-3 novembre: a, b
    expect(r.meseScorso).toBe(2); // ottobre: c (29/10) e d (24/10); e è di settembre
    expect(r.serie).toHaveLength(30);
    expect(r.serie.at(-1)).toEqual({ giorno: "2026-11-03", utenti: 2 });
  });
});
