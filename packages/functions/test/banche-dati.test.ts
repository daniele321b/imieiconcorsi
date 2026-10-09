import { describe, expect, it } from "vitest";
import { estraiDomande } from "../src/banche-dati/parser";

const giusta = (d: { opzioni: string[]; corretta: number }) => d.opzioni[d.corretta];

describe("estrazione delle domande dalle banche dati", () => {
  it("risposta indicata dentro la domanda, con testo su più righe e numeri di pagina", () => {
    const testo = [
      "1. Ai sensi della Costituzione, il Presidente della Repubblica",
      "è eletto per:",
      "A) cinque anni",
      "B) sette anni",
      "C) nove anni",
      "Risposta esatta: B",
      "Pagina 1 di 30",
      "2) Quale organo approva il bilancio dello Stato?",
      "a) Il Governo",
      "b) Il Parlamento",
      "c) La Corte dei conti",
      "Risposta corretta: b",
    ].join("\n");
    const { domande, scartate, formati } = estraiDomande(testo);
    expect(scartate).toEqual([]);
    expect(domande.map((d) => d.testo)).toEqual([
      "Ai sensi della Costituzione, il Presidente della Repubblica è eletto per:",
      "Quale organo approva il bilancio dello Stato?",
    ]);
    expect(domande.map(giusta)).toEqual(["sette anni", "Il Parlamento"]);
    expect(formati).toEqual({ indicata: 2 });
  });

  it("risposta segnata con asterisco o (X)", () => {
    const testo = [
      "10. Capitale d'Italia?", "A) Milano", "B) Roma *", "C) Napoli",
      "11. Quanti sono i giorni di una settimana?", "A) 5", "* B) 7", "C) 6",
      "12. Quante sono le regioni italiane?", "A) 20 (X)", "B) 18", "C) 22",
    ].join("\n");
    const { domande, scartate } = estraiDomande(testo);
    expect(domande.map(giusta)).toEqual(["Roma", "7", "20"]);
    expect(scartate).toEqual([]);
  });

  it("tabella delle soluzioni in fondo, che non viene letta come domande", () => {
    const testo = [
      "1. Domanda numero uno?",
      "A) uno",
      "B) due",
      "C) tre",
      "2. Domanda numero due?",
      "A) alfa",
      "B) beta",
      "C) gamma",
      "SOLUZIONI",
      "1 C   2-A",
    ].join("\n");
    const { domande, formati } = estraiDomande(testo);
    expect(domande.map(giusta)).toEqual(["tre", "alfa"]);
    expect(formati).toEqual({ chiave: 2 });
  });

  it("'la risposta esatta è sempre la prima': mescola le opzioni ma tiene la giusta", () => {
    const testo = [
      "Avvertenza: la risposta esatta è sempre la prima.",
      ...Array.from({ length: 8 }, (_, i) => [`${i + 1}. Domanda di prova numero ${i + 1}?`, "A) giusta", "B) sbagliata uno", "C) sbagliata due", "D) sbagliata tre"]).flat(),
    ].join("\n");
    const { domande } = estraiDomande(testo);
    expect(domande).toHaveLength(8);
    expect(domande.every((d) => giusta(d) === "giusta")).toBe(true);
    // Non sempre in prima posizione dopo il rimescolamento.
    expect(new Set(domande.map((d) => d.corretta)).size).toBeGreaterThan(1);
  });

  it("senza modo di sapere la giusta scarta e dice perché; il formato forzato vince", () => {
    const testo = ["5. Domanda senza indicazioni?", "A) primo", "B) secondo", "6. Doppia segnata?", "A) uno *", "B) due *"].join("\n");
    expect(estraiDomande(testo).scartate).toEqual([
      { numero: 5, motivo: "risposta giusta non trovata" },
      { numero: 6, motivo: "più risposte segnate come giuste" },
    ]);
    expect(estraiDomande(testo, "prima").domande.map(giusta)).toEqual(["primo", "uno"]);
  });

  it("scarta i doppioni", () => {
    const testo = ["1. Stessa domanda?", "A) x", "B) y", "Risposta esatta: A", "2. Stessa domanda?", "A) x", "B) y", "Risposta esatta: A"].join("\n");
    const { domande, scartate } = estraiDomande(testo);
    expect(domande).toHaveLength(1);
    expect(scartate).toEqual([{ numero: 2, motivo: "domanda già presente (doppione)" }]);
  });
});
