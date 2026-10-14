import { describe, expect, it } from "vitest";
import { estraiDomandeColonne, intestazioni } from "../src/banche-dati/colonne";
import type { Elemento } from "../src/banche-dati/tabella";

// Tabella come nei PDF del Ministero della Giustizia (Polizia penitenziaria): intestazione
// Id | Livello | Quesito | Risp_esatta | Risp_errata_1-3, colonne a x 28, 58, 76, 348, 462, 576, 690.
const X = [28, 58, 76, 348, 462, 576, 690];
const TESTA = ["Id", "Livello", "Quesito", "Risp_esatta", "Risp_errata_1", "Risp_errata_2", "Risp_errata_3"];
const LARGHEZZA_TESTA = [8, 27, 33, 48, 58, 58, 58];
const X_TESTA = [28, 47, 194, 379, 488, 602, 716];

/** Una pagina: titolo, intestazione e righe [numero, livello, quesito, esatta, errate…] (ogni cella = righe di testo). */
function pagina(n: number, righe: [number, string[][]][], titolo = "CONCORSO PUBBLICO - BANCA DATI ARITMETICA"): Elemento[] {
  const el: Elemento[] = [{ pagina: n, testo: titolo, x: 74, y: 532, larghezza: 700, altezza: 10 }];
  TESTA.forEach((t, i) => el.push({ pagina: n, testo: t, x: X_TESTA[i]!, y: 501, larghezza: LARGHEZZA_TESTA[i]!, altezza: 10 }));
  let y = 470;
  for (const [numero, celle] of righe) {
    el.push({ pagina: n, testo: String(numero), x: X[0]!, y, larghezza: 5, altezza: 10 });
    el.push({ pagina: n, testo: "1", x: X[1]!, y, larghezza: 5, altezza: 10 });
    celle.forEach((righeCella, c) => righeCella.forEach((t, i) => el.push({ pagina: n, testo: t, x: X[c + 2]!, y: y - 13 * i, larghezza: t.length * 4, altezza: 10 })));
    y -= 45;
  }
  // Numero di pagina in fondo, da solo.
  el.push({ pagina: n, testo: String(n), x: 417, y: 26, larghezza: 6, altezza: 10 });
  return el;
}

describe("tabella quesito | esatta | errate", () => {
  it("riconosce l'intestazione con i ruoli delle colonne", () => {
    const [testa] = intestazioni(pagina(2, [])).values();
    expect(testa!.colonne.map((c) => c.ruolo)).toEqual(["numero", "livello", "domanda", "esatta", "errata", "errata", "errata"]);
  });

  it("legge domanda e risposte su più righe, con la sezione dal titolo, senza il numero di pagina", () => {
    const { domande, scartate } = estraiDomandeColonne(
      pagina(2, [
        [1, [["Dati due insiemi A e B, si dice", "intersezione:"], ["l'insieme degli elementi", "comuni"], ["l'unione"], ["la differenza"], ["il prodotto"]]],
        [2, [["L'insieme unione si scrive:"], ["A U B"], ["A ∩ B"], ["A + B"], ["B – A"]]],
      ]),
    );
    expect(scartate).toEqual([]);
    expect(domande).toHaveLength(2);
    expect(domande[0]!.testo).toBe("Dati due insiemi A e B, si dice intersezione:");
    expect(domande[0]!.pdf).toEqual({ opzioni: ["l'insieme degli elementi comuni", "l'unione", "la differenza", "il prodotto"], corretta: 0 });
    expect(domande[0]!.opzioni[domande[0]!.corretta]).toBe("l'insieme degli elementi comuni");
    expect(domande[1]!.pdf.opzioni.at(-1)).toBe("B – A");
    expect(domande[0]!.sezione).toBe("Aritmetica");
  });

  it("attacca gli esponenti (più piccoli e più in alto) alla loro base", () => {
    const el = pagina(2, [[5, [["Quanto vale (2a)"], ["8a"], ["6a"], ["2a"], ["4a"]]]]);
    const i = el.findIndex((e) => e.testo === "Quanto vale (2a)");
    const base = el[i]!;
    el.splice(i + 1, 0, { pagina: 2, testo: "3 ", x: base.x + base.larghezza, y: base.y + 5, larghezza: 5, altezza: 6.7 });
    const j = el.findIndex((e) => e.testo === "8a");
    el.splice(j + 1, 0, { pagina: 2, testo: "3", x: el[j]!.x + el[j]!.larghezza, y: el[j]!.y + 5, larghezza: 3, altezza: 6.7 });
    const [d] = estraiDomandeColonne(el).domande;
    expect(d!.testo).toBe("Quanto vale (2a)³");
    expect(d!.pdf.opzioni[0]).toBe("8a³");
  });

  it("divide un pezzo con domanda e risposta esatta insieme", () => {
    const el = pagina(2, [
      [26, [["Quale appartiene all'insieme N:"], ["0"], ["-5"], ["1,9"], ["3,15"]]],
      [27, [["Quale non appartiene all'insieme N:"], [], ["0"], ["105"], ["270"]]],
    ]);
    // La domanda finisce a x≈348 e la risposta "0,32" è nello stesso pezzo di testo.
    const i = el.findIndex((e) => e.testo.startsWith("Quale non"));
    el[i] = { ...el[i]!, testo: "Quale non appartiene all'insieme N: 0,32", larghezza: 290 };
    const [, d] = estraiDomandeColonne(el).domande;
    expect(d!.testo).toBe("Quale non appartiene all'insieme N:");
    expect(d!.pdf.opzioni).toEqual(["0,32", "0", "105", "270"]);
  });

  it("salta le copertine senza intestazione e scarta le risposte ripetute", () => {
    const copertina: Elemento[] = [{ pagina: 3, testo: "BANCA DATI", x: 330, y: 300, larghezza: 180, altezza: 36 }];
    const { domande, scartate } = estraiDomandeColonne([
      ...pagina(2, [[1, [["Quanto fa 2 + 2?"], ["4"], ["5"], ["3"], ["22"]]]]),
      ...copertina,
      ...pagina(4, [[1, [["Il capoluogo della Calabria è:"], ["Catanzaro"], ["Cosenza"], ["Crotone"], ["Cosenza"]]]], "CONCORSO ‐ BANCA DATI GEOGRAFIA"),
    ]);
    expect(domande.map((d) => d.pdf.opzioni)).toEqual([["4", "5", "3", "22"]]);
    expect(scartate).toEqual([{ numero: 1, motivo: "risposte ripetute" }]);
  });

  it("senza intestazione non legge nulla", () => {
    expect(estraiDomandeColonne([{ pagina: 1, testo: "1. Domanda A) uno B) due", x: 50, y: 500, larghezza: 100 }]).domande).toEqual([]);
  });
});
