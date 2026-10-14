import { describe, expect, it } from "vitest";
import { estraiDomande } from "../src/banche-dati/parser";
import { rispostePerUtenti } from "../src/banche-dati/pubblica";
import { dispongiRisposte } from "@imieiconcorsi/core/risposte";

// Test dell'estrazione delle domande dai PDF delle banche dati e dell'ordine delle risposte mostrate.

/** Testo della risposta giusta di una domanda estratta. */
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

describe("banca dati Polizia di Stato 2026 (righe vere del PDF)", () => {
  // Il PDF dice in legenda che la giusta è la A, ha "BANCA DATI" in cima a ogni pagina e il
  // numero di pagina attaccato all'ultima riga.
  const pagina = (n: number, righe: string[]) => ["BANCA DATI", ...righe.slice(0, -1), `${righe.at(-1)}${n} di 399`];
  const testo = [
    "LEGENDA",
    "- La risposta esatta è contrassegnata dalla lettera “A”",
    ...pagina(1, [
      "CULTURA GENERALE",
      "1. Il simbolo chimico del Magnesio?", "A) Mg", "B) k", "C) Pb", "D) Se", "E) St",
      "7. Indicare tra i seguenti cosa non fa parte dello", "scheletro umano.", "A) Lingua", "B) Rotula", "C) Carpo",
      "15. Indicare tra i seguenti cosa non fa parte dello", "scheletro umano.", "A) Estensore ulnare del carpo", "B) Falangi", "C) Femore",
      "16. L’attrito volvente si genera:", "A) quando un oggetto rotola su un altro", "B) quando due oggetti strisciano",
      "C) quando due oggetti corrono sulla stessa parallela ed", "alla stessa velocità",
    ]),
    ...pagina(2, [
      "391. A causa della pandemia un evento si tratta:", "A) del World Economic Forum (WEF)",
      "B) del primo concorso di bellezza riservato alle persone", "LGBTQ",
      "392. Cerere è un pianeta di che tipo:", "A) nano", "B) gigante",
      "393. Garantire la pace tra gli Stati vuol dire:", "A) Garantire pacificamente la soluzione delle", "controversie", "B) Fare la guerra",
    ]),
    "84 di 399BANCA DATI",
    "STORIA",
    "1338. In Cile il generale Pinochet terminò il suo mandato nel…", "A) 1990", "B) 1975",
    "5115. Individuare la lettera che completa la serie: ?", "T Q N I F", "A) Z", "B) X",
  ].join("\n");
  const { domande, scartate, formati } = estraiDomande(testo);
  // Domanda estratta con il numero `n`.
  const d = (n: number) => domande.find((x) => x.numero === n)!;

  it("riconosce la legenda: la giusta è sempre la A", () => {
    expect(scartate).toEqual([]);
    expect(formati).toEqual({ prima: domande.length });
    expect(domande.every((x) => x.pdf.corretta === 0 && giusta(x) === x.pdf.opzioni[0])).toBe(true);
  });
  it("toglie numeri di pagina e intestazioni dalle risposte", () => {
    expect(d(16).pdf.opzioni.at(-1)).toBe("quando due oggetti corrono sulla stessa parallela ed alla stessa velocità");
    expect(d(391).pdf.opzioni.at(-1)).toBe("del primo concorso di bellezza riservato alle persone LGBTQ");
  });
  it("una parola come 'soluzione' in una risposta non apre la tabella delle soluzioni", () => {
    expect(d(393).pdf.opzioni[0]).toBe("Garantire pacificamente la soluzione delle controversie");
    expect(d(1338)).toBeDefined();
  });
  it("legge le sezioni come argomento, senza mangiare le righe maiuscole delle domande", () => {
    expect([d(1).sezione, d(391).sezione, d(1338).sezione]).toEqual(["Cultura generale", "Cultura generale", "Storia"]);
    expect(d(5115).testo).toBe("Individuare la lettera che completa la serie: ? T Q N I F");
  });
  it("stesso testo con risposte diverse non è un doppione", () => {
    expect(d(7)).toBeDefined();
    expect(d(15)).toBeDefined();
  });
});

describe("ordine delle risposte agli utenti", () => {
  const testo = [
    "La risposta esatta è contrassegnata dalla lettera “A”",
    "1. Il simbolo chimico del Magnesio?", "A) Mg", "B) k", "C) Pb", "D) Se", "E) St",
    "2. Quante sono le vertebre lombari nell'uomo ?", "A) 5", "B) 4", "C) 7", "D) 3", "E) 2",
    "3. Il tricheco è possibile trovarlo:", "A) in ambiente polare", "B) nella savana", "C) nella foresta tropicale",
    "D) nella prateria", "E) nella tundra",
  ].join("\n");
  const { domande } = estraiDomande(testo);

  it("come nel PDF: la giusta resta la A", () => {
    expect(domande.map((d) => rispostePerUtenti(d, "pdf").corretta)).toEqual([0, 0, 0]);
  });
  it("mescolate: cambia la lettera, non la risposta giusta", () => {
    const mescolate = domande.map((d) => rispostePerUtenti(d, undefined));
    expect(mescolate.map(giusta)).toEqual(["Mg", "5", "in ambiente polare"]);
    expect(mescolate.some((m) => m.corretta !== 0)).toBe(true);
  });
  it("un file estratto senza l'ordine del PDF non si pubblica come nel PDF", () => {
    const { pdf, ...vecchia } = domande[0];
    expect(() => rispostePerUtenti(vecchia, "pdf")).toThrow();
  });
});

describe("risposte scelte dall'utente: giusta sempre per prima o mescolate", () => {
  const d = { opzioni: ["3", "5", "4", "2", "7"], corretta: 1 };

  it("sempre per prima: la giusta va in A, le altre restano in ordine", () => {
    expect(dispongiRisposte(d, "prima", "bd#x/n00002")).toEqual({ opzioni: ["5", "3", "4", "2", "7"], corretta: 0 });
  });
  it("mescolate: stesso ordine per la stessa domanda, la giusta resta la stessa", () => {
    const a = dispongiRisposte(d, "mescolate", "bd#x/n00002");
    expect(dispongiRisposte(d, "mescolate", "bd#x/n00002")).toEqual(a);
    expect(a.opzioni.at(a.corretta)).toBe("5");
    expect([...a.opzioni].sort()).toEqual([...d.opzioni].sort());
  });
  it("mescolate: domande diverse hanno ordini diversi (la giusta non sta sempre nello stesso posto)", () => {
    const posti = new Set(Array.from({ length: 30 }, (_, i) => dispongiRisposte({ opzioni: ["a", "b", "c", "d", "e"], corretta: 0 }, "mescolate", `bd#x/n${i}`).corretta));
    expect(posti.size).toBeGreaterThan(2);
  });
});
