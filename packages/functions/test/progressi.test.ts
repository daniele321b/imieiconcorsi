import { aggiornaProgresso, bitAcceso, candidatePerSelezione, contaBit, numeroDomanda } from "@imieiconcorsi/core/progressi";
import { describe, expect, it } from "vitest";

const id = (n: number) => `n${String(n).padStart(5, "0")}`;
const domande = (quante: number) => Array.from({ length: quante }, (_, i) => ({ id: id(i + 1) }));

describe("progressi nelle banche dati", () => {
  it("il numero della domanda viene dal suo id", () => {
    expect(numeroDomanda("n00042")).toBe(42);
    expect(numeroDomanda(id(5977))).toBe(5977);
  });

  it("una sessione segna le domande fatte e quelle sbagliate", () => {
    const p = aggiornaProgresso(undefined, [
      { numero: 1, giusta: true },
      { numero: 9, giusta: false },
      { numero: 5977, giusta: true },
    ]);
    expect(p.nFatte).toBe(3);
    expect(p.nSbagliate).toBe(1);
    expect(bitAcceso(p.fatte, 9)).toBe(true);
    expect(bitAcceso(p.sbagliate, 9)).toBe(true);
    expect(bitAcceso(p.sbagliate, 1)).toBe(false);
    expect(bitAcceso(p.fatte, 2)).toBe(false);
    // 6.000 domande stanno in meno di 1 KB.
    expect(p.fatte.length).toBeLessThan(1000);
  });

  it("rifatta giusta, una domanda non è più da ripassare (ma resta fatta)", () => {
    const prima = aggiornaProgresso(undefined, [{ numero: 9, giusta: false }]);
    const dopo = aggiornaProgresso(prima, [{ numero: 9, giusta: true }, { numero: 10, giusta: false }]);
    expect(bitAcceso(dopo.fatte, 9)).toBe(true);
    expect(bitAcceso(dopo.sbagliate, 9)).toBe(false);
    expect(dopo.nFatte).toBe(2);
    expect(dopo.nSbagliate).toBe(1);
    // La mappa di prima non cambia (si lavora su copie).
    expect(bitAcceso(prima.sbagliate, 9)).toBe(true);
  });

  it("conta i bit accesi", () => {
    expect(contaBit(undefined)).toBe(0);
    expect(contaBit(new Uint8Array([0b1011, 0xff]))).toBe(11);
  });

  it("nuove: prima le mai fatte, poi le altre per completare", () => {
    const tutte = domande(10);
    const p = aggiornaProgresso(undefined, [1, 2, 3].map((numero) => ({ numero, giusta: true })));
    const { prima, poi } = candidatePerSelezione(tutte, p, "nuove");
    expect(prima.map((d) => numeroDomanda(d.id))).toEqual([4, 5, 6, 7, 8, 9, 10]);
    expect(poi.map((d) => numeroDomanda(d.id))).toEqual([1, 2, 3]);
  });

  it("senza progressi sono tutte nuove", () => {
    expect(candidatePerSelezione(domande(4), undefined, "nuove")).toEqual({ prima: domande(4), poi: [] });
  });

  it("da ripassare: solo le sbagliate l'ultima volta", () => {
    const p = aggiornaProgresso(undefined, [
      { numero: 2, giusta: false },
      { numero: 5, giusta: true },
      { numero: 7, giusta: false },
    ]);
    const { prima, poi } = candidatePerSelezione(domande(10), p, "sbagliate");
    expect(prima.map((d) => numeroDomanda(d.id))).toEqual([2, 7]);
    expect(poi).toEqual([]);
    expect(candidatePerSelezione(domande(10), undefined, "sbagliate").prima).toEqual([]);
  });

  it("tutte: nessuna preferenza", () => {
    const p = aggiornaProgresso(undefined, [{ numero: 1, giusta: false }]);
    expect(candidatePerSelezione(domande(3), p, "tutte")).toEqual({ prima: domande(3), poi: [] });
  });
});
