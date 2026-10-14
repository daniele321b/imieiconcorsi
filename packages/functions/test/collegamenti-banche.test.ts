import { concorsiSuggeriti, paroleChiave } from "@imieiconcorsi/core/concorsi";
import { concorsiDellaBanca, nomeConcorsoBreve, type CompartoId } from "@imieiconcorsi/core/domain";
import { describe, expect, it } from "vitest";

// Test dei concorsi suggeriti da collegare a una banca dati.

const ora = new Date("2026-10-09T10:00:00Z");

/** Bando di prova: comparto forze dell'ordine e scadenza a fine novembre se non indicati. */
const bando = (id: string, ente: string, titolo: string, extra: Partial<{ figura: string; comparto: CompartoId; scadenza: string; bancaDatiPrevista: boolean; bancaDati: boolean }> = {}) => ({
  id,
  ente,
  titolo,
  figura: extra.figura,
  comparto: extra.comparto ?? ("forze-ordine" as CompartoId),
  scadenza: extra.scadenza ?? "2026-11-30T23:59:00Z",
  bancaDatiPrevista: extra.bancaDatiPrevista ?? true,
  bancaDati: extra.bancaDati ?? false,
});

describe("concorsi da collegare a una banca dati", () => {
  it("parole chiave: niente parole generiche, numeri o accenti", () => {
    expect([...paroleChiave("Banca dati Polizia di Stato 2026 — prova preselettiva")]).toEqual(["polizia", "stato"]);
    expect(paroleChiave("Città metropolitana di Roma").has("citta")).toBe(true);
  });

  it("propone i bandi aperti simili, dal più somigliante, e segna quelli molto simili", () => {
    const bandi = [
      bando("1", "Ministero dell'Interno", "Concorso per 1000 allievi agenti della Polizia di Stato"),
      bando("2", "Comune di Milano", "Istruttore amministrativo", { comparto: "enti-locali", bancaDatiPrevista: false }),
      bando("3", "Ministero dell'Interno", "Commissari della Polizia di Stato", { bancaDatiPrevista: false }),
      bando("4", "Polizia penitenziaria", "Agenti", { bancaDatiPrevista: false }),
    ];
    const s = concorsiSuggeriti({ titolo: "Banca dati Polizia di Stato 2026", comparto: "forze-ordine", anno: 2026 }, bandi, { ora });
    expect(s.map((x) => x.concorso.id)).toEqual(["1", "3", "4"]);
    expect(s[0]!.forte).toBe(true); // due parole in comune e il bando cita una banca dati
    expect(s[1]!.forte).toBe(false); // somiglia ma non cita una banca dati
  });

  it("esclude i chiusi, quelli già collegati e quelli con un'altra banca dati", () => {
    const bandi = [
      bando("chiuso", "Polizia di Stato", "Agenti", { scadenza: "2026-09-01T00:00:00Z" }),
      bando("collegato", "Polizia di Stato", "Agenti"),
      bando("occupato", "Polizia di Stato", "Agenti", { bancaDati: true }),
      bando("libero", "Polizia di Stato", "Agenti"),
    ];
    const s = concorsiSuggeriti({ titolo: "Polizia di Stato" }, bandi, { ora, esclusi: new Set(["collegato"]) });
    expect(s.map((x) => x.concorso.id)).toEqual(["libero"]);
  });

  it("senza parole significative nel titolo non propone nulla", () => {
    expect(concorsiSuggeriti({ titolo: "Banca dati 2026" }, [bando("1", "Polizia di Stato", "Agenti")], { ora })).toEqual([]);
  });

  it("lista dei concorsi collegati, anche per le banche salvate con un concorso solo", () => {
    expect(concorsiDellaBanca({ concorsoId: "c1", concorsoTitolo: "Ente — Figura" })).toEqual([{ id: "c1", titolo: "Ente — Figura" }]);
    expect(concorsiDellaBanca({})).toEqual([]);
    const lista = [{ id: "a", titolo: "A" }, { id: "b", titolo: "B" }];
    expect(concorsiDellaBanca({ concorsi: lista, concorsoId: "a" })).toBe(lista);
    expect(nomeConcorsoBreve({ ente: "Comune di Roma", figura: "Vigile urbano", titolo: "Concorso" })).toBe("Comune di Roma — Vigile urbano");
  });
});
