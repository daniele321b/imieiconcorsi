import { pianoDaGruppi } from "@imieiconcorsi/core/domain";
import { parseGruppi } from "@imieiconcorsi/core/http";
import { describe, expect, it } from "vitest";
import { azionePerAbbonato } from "../src/jobs/scadenze-logic";

// Test di gruppi Cognito → piano e delle azioni sugli abbonamenti in scadenza.

describe("parseGruppi", () => {
  it.each([
    ["[admin pro]", ["admin", "pro"]],
    ["[medium]", ["medium"]],
    ["pro,admin", ["pro", "admin"]],
    [["pro"], ["pro"]],
    [undefined, []],
    ["", []],
  ])("%j", (claim, attesi) => {
    expect(parseGruppi(claim)).toEqual(attesi);
  });
});

describe("pianoDaGruppi", () => {
  it.each([
    [[], "free"],
    [["medium"], "medium"],
    [["pro"], "pro"],
    [["medium", "pro"], "pro"],
    [["admin"], "pro"],
  ])("%j → %s", (gruppi, piano) => {
    expect(pianoDaGruppi(gruppi)).toBe(piano);
  });
});

describe("azionePerAbbonato", () => {
  const oggi = new Date("2026-10-10T05:00:00Z");
  // Data ISO a `giorni` giorni da oggi (negativi = nel passato).
  const tra = (giorni: number) => new Date(oggi.getTime() + giorni * 86_400_000).toISOString();

  it("senza scadenza non fa nulla (piano dato a mano dall'admin)", () => {
    expect(azionePerAbbonato(undefined, undefined, oggi)).toBe("nessuna");
  });
  it("scaduto → torna Free", () => {
    expect(azionePerAbbonato(tra(-1), undefined, oggi)).toBe("scaduto");
  });
  it("entro 3 giorni → promemoria", () => {
    expect(azionePerAbbonato(tra(2.5), undefined, oggi)).toBe("promemoria");
  });
  it("promemoria una volta sola per la stessa scadenza", () => {
    const s = tra(2);
    expect(azionePerAbbonato(s, s, oggi)).toBe("nessuna");
  });
  it("dopo un rinnovo il promemoria riparte", () => {
    expect(azionePerAbbonato(tra(2), tra(-28), oggi)).toBe("promemoria");
  });
  it("più di 3 giorni → nulla", () => {
    expect(azionePerAbbonato(tra(10), undefined, oggi)).toBe("nessuna");
  });
});
