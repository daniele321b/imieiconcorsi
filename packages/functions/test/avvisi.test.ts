import { feedbackModificabileDal } from "@imieiconcorsi/core/domain";
import { describe, expect, it } from "vitest";
import { bandiNuovi, deveAvvisare } from "../src/jobs/avvisi-logic";

// 2026-10-12 è un lunedì; le 7:00 italiane sono le 5:00 UTC.
const lunedi = new Date("2026-10-12T05:00:00Z");
const martedi = new Date("2026-10-13T05:00:00Z");

describe("deveAvvisare", () => {
  it.each([
    ["giornaliero, mai avvisato", "giornaliero", undefined, martedi, true],
    ["giornaliero, avvisato ieri", "giornaliero", "2026-10-12T05:00:00Z", martedi, true],
    ["giornaliero, già avvisato oggi", "giornaliero", "2026-10-13T04:59:00Z", martedi, false],
    ["settimanale di lunedì", "settimanale", "2026-10-05T05:00:00Z", lunedi, true],
    ["settimanale di martedì", "settimanale", undefined, martedi, false],
    ["mai", "mai", undefined, lunedi, false],
  ] as const)("%s", (_, frequenza, ultimo, ora, atteso) => {
    expect(deveAvvisare(frequenza, ultimo, ora)).toBe(atteso);
  });
});

describe("bandi nuovi", () => {
  const bandi = [
    // Visto dall'app solo oggi ma pubblicato settimane fa: non è "nuovo".
    { id: "vecchio-scoperto-ora", pubblicatoIl: "2026-09-20T08:00:00Z", primoImportoIl: "2026-10-13T04:00:00Z", scadenza: "2026-11-01" },
    { id: "ieri-b", pubblicatoIl: "2026-10-12T15:00:00Z", scadenza: "2026-11-20" },
    { id: "ieri-a", pubblicatoIl: "2026-10-12T00:00:00Z", scadenza: "2026-10-30" },
    { id: "oggi", pubblicatoIl: "2026-10-13T03:00:00Z", scadenza: "2026-10-25" },
    { id: "senza-data", primoImportoIl: "2026-10-12T04:30:00Z", scadenza: "2026-12-01" },
    { id: "settimana-scorsa", pubblicatoIl: "2026-10-07T09:00:00Z", scadenza: "2026-12-05" },
  ];
  // Solo gli id, per confrontare l'ordine.
  const ids = (l: { id: string }[]) => l.map((b) => b.id);

  it("giornaliero: solo quelli pubblicati ieri, il più vicino alla scadenza prima", () => {
    expect(ids(bandiNuovi(bandi, "giornaliero", martedi))).toEqual(["ieri-a", "ieri-b", "senza-data"]);
  });

  it("settimanale: gli ultimi 7 giorni, oggi escluso", () => {
    expect(ids(bandiNuovi(bandi, "settimanale", martedi))).toEqual(["ieri-a", "ieri-b", "senza-data", "settimana-scorsa"]);
  });
});

describe("feedback", () => {
  const ora = new Date("2026-10-20T10:00:00Z");
  it("si modifica dopo 15 giorni", () => {
    expect(feedbackModificabileDal(undefined, ora)).toBeNull();
    expect(feedbackModificabileDal({ voto: 4, il: "2026-10-01T10:00:00Z" }, ora)).toBeNull();
    expect(feedbackModificabileDal({ voto: 4, il: "2026-10-10T10:00:00Z" }, ora)).toBe("2026-10-25T10:00:00.000Z");
  });
});

describe("link di disiscrizione", () => {
  it("la firma vale solo per il suo utente e il suo segreto", async () => {
    const { firmaDisiscrizione, firmaValida } = await import("@imieiconcorsi/core/disiscrizione");
    const t = firmaDisiscrizione("utente-1", "segreto");
    expect(firmaValida("utente-1", t, "segreto")).toBe(true);
    expect(firmaValida("utente-2", t, "segreto")).toBe(false);
    expect(firmaValida("utente-1", t, "altro-segreto")).toBe(false);
    expect(firmaValida("utente-1", "corto", "segreto")).toBe(false);
  });
});
