import { describe, expect, it } from "vitest";
import { estraiDomandeLettere } from "../src/banche-dati/lettere";
import { unisciCella } from "../src/banche-dati/parser";
import type { Elemento } from "../src/banche-dati/tabella";

// Tabella come nei PDF della Guardia di Finanza: codice (allineato a destra) a x≈36-41, domanda
// a 115, risposte a) b) c) d) a 327 / 448 / 569 / 690, lettera giusta a 813. Celle allineate in alto.
const X = [115, 327, 448, 569, 690, 813];

/** Pagine con il titolo in cima e le righe [codice, domanda, a, b, c, d, lettera] (ogni cella = righe di testo). */
function pdf(righe: [string, string[], string[], string[], string[], string[], string][], perPagina = 5): Elemento[] {
  const el: Elemento[] = [];
  righe.forEach(([codice, ...celle], i) => {
    const pagina = Math.floor(i / perPagina) + 1;
    if (i % perPagina === 0) el.push({ pagina, testo: "VIETATA LA PUBBLICAZIONE, LA RIPRODUZIONE E LA DIVULGAZIONE.", x: 172, y: 548, larghezza: 496 });
    const y = 523 - (i % perPagina) * 90;
    el.push({ pagina, testo: codice, x: 110 - codice.length * 5.5, y, larghezza: codice.length * 5.5 });
    celle.forEach((cella, c) => {
      const righeCella = typeof cella === "string" ? [cella] : cella;
      righeCella.forEach((t, j) => el.push({ pagina, testo: t, x: X[c]!, y: y - 13 * j, larghezza: t.length * 4.5 }));
    });
  });
  return el;
}

/** Riga semplice: domanda, quattro risposte e la lettera giusta. */
const riga = (n: number, domanda: string, risposte: string[], giusta: string): [string, string[], string[], string[], string[], string[], string] => [
  `TSUYB${String(n).padStart(8, "0")}`,
  [domanda],
  [`a) ${risposte[0]}`],
  [`b) ${risposte[1]}`],
  [`c) ${risposte[2]}`],
  [`d) ${risposte[3]}`],
  giusta,
];

describe("tabella codice | domanda | a)-d) | lettera giusta", () => {
  const righe = [
    riga(76, "La responsabilità ex D.Lgs. 231/2001 è", ["Penale.", "Amministrativa.", "Civile.", "Tributaria."], "b"),
    riga(77, "Il FEAMPA è entrato in vigore il:", ["14 luglio 2021", "1 gennaio 2020", "30 giugno 2022", "1 marzo 2019"], "a"),
    riga(78, "Quale divisione in sillabe è esatta?", ["Au- to- re- vo- lez- za", "A- u- to- re- vo- lez- za", "Au- to- re- vo- le- zza", "A- u- to- re- vo- le- zza"], "a"),
    riga(79, "Le procure regionali hanno sede:", ["in ogni capoluogo di Regione", "in ogni Provincia", "solo a Roma", "nessuna risposta è corretta"], "a"),
    riga(80, "Il livello centrale della Procura europea è costituito:", ["da 15 Camere Permanenti", "dalla Corte di Cassazione", "da 15 procuratori", "da un coordinatore"], "a"),
    riga(8, "La PAC è finanziata tramite:", ["il F.E.A.M.P.", "il F.E.P.", "il FE.A.GA. e il F.E.A.S.R.", "il F.P.A.C."], "c"),
  ];

  it("legge codice, domanda, risposte senza la lettera e la giusta dalla colonna", () => {
    const { domande, scartate, formati } = estraiDomandeLettere(pdf(righe));
    expect(scartate).toEqual([]);
    expect(formati).toEqual({ lettera: 6 });
    const d = domande[0]!;
    expect(d.numero).toBe(76);
    expect(d.testo).toBe("La responsabilità ex D.Lgs. 231/2001 è");
    expect(d.pdf).toEqual({ opzioni: ["Penale.", "Amministrativa.", "Civile.", "Tributaria."], corretta: 1 });
    expect(d.opzioni[d.corretta]).toBe("Amministrativa.");
    // Il titolo della seconda pagina non finisce nell'ultima risposta della prima.
    expect(domande[4]!.pdf.opzioni[3]).toBe("da un coordinatore");
    expect(domande[5]).toMatchObject({ numero: 8, pdf: { corretta: 2 } });
  });

  it("tiene i trattini dentro la riga (sillabe) e quelli a fine riga", () => {
    const { domande } = estraiDomandeLettere(pdf(righe));
    expect(domande[2]!.pdf.opzioni[0]).toBe("Au- to- re- vo- lez- za");
    expect(unisciCella(["poteri di polizia economico-", "finanziaria"])).toBe("poteri di polizia economico-finanziaria");
    expect(unisciCella(["Il trattato di", "Schengen"])).toBe("Il trattato di Schengen");
  });

  it("scarta le righe senza lettera giusta valida", () => {
    const senza = [...righe.slice(0, 5), riga(81, "Domanda senza soluzione:", ["uno", "due", "tre", "quattro"], "")];
    const { domande, scartate } = estraiDomandeLettere(pdf(senza));
    expect(domande).toHaveLength(5);
    expect(scartate).toEqual([{ numero: 81, motivo: "lettera della risposta giusta mancante" }]);
  });

  it("senza colonne a) b) ripetute non legge nulla", () => {
    expect(estraiDomandeLettere([{ pagina: 1, testo: "1. Domanda A) uno B) due", x: 50, y: 500, larghezza: 100 }]).domande).toEqual([]);
  });
});
