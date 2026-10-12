import type { Domanda, MateriaId } from "@imieiconcorsi/core/domain";
import { REGOLE_DEFAULT } from "@imieiconcorsi/core/domain";
import { describe, expect, it } from "vitest";
import { calcolaEsito, selezionaDomande } from "../src/study/logic";

const domanda = (materia: MateriaId, id: string, livello = 3, corretta = 0): Domanda => ({
  materia,
  id,
  livello,
  corretta,
  argomento: "x",
  testo: id,
  opzioni: ["a", "b", "c", "d"],
  spiegazione: "",
  fonte: "",
});

describe("selezionaDomande", () => {
  it("ripartisce le domande tra le materie", () => {
    const perMateria = new Map<MateriaId, Domanda[]>([
      ["storia", Array.from({ length: 10 }, (_, i) => domanda("storia", `s${i}`))],
      ["logica", Array.from({ length: 10 }, (_, i) => domanda("logica", `l${i}`))],
    ]);
    const scelte = selezionaDomande(perMateria, 6, {});
    expect(scelte).toHaveLength(6);
    expect(scelte.filter((d) => d.materia === "storia")).toHaveLength(3);
  });

  it("si ferma quando le domande finiscono", () => {
    const perMateria = new Map<MateriaId, Domanda[]>([["storia", [domanda("storia", "a"), domanda("storia", "b")]]]);
    expect(selezionaDomande(perMateria, 60, {})).toHaveLength(2);
  });

  it("preferisce il livello dell'utente", () => {
    const perMateria = new Map<MateriaId, Domanda[]>([
      ["storia", [1, 1, 1, 5, 5, 5].map((l, i) => domanda("storia", `d${i}`, l))],
    ]);
    const scelte = selezionaDomande(perMateria, 3, { storia: 5 }, () => 0);
    expect(scelte.every((d) => d.livello === 5)).toBe(true);
  });
});

describe("calcolaEsito", () => {
  const domande = [domanda("storia", "1"), domanda("storia", "2"), domanda("logica", "3"), domanda("logica", "4")];

  it("applica corrette, errate e omesse", () => {
    const esito = calcolaEsito(domande, [0, 1, null, 0], REGOLE_DEFAULT);
    expect(esito).toMatchObject({ corrette: 2, errate: 1, omesse: 1, punteggio: 1.75, massimo: 4, percentuale: 43.75, superata: false });
    expect(esito.perMateria).toEqual([
      { materia: "storia", corrette: 1, totale: 2 },
      { materia: "logica", corrette: 1, totale: 2 },
    ]);
  });

  it("supera la prova alla soglia", () => {
    expect(calcolaEsito(domande, [0, 0, 0, null], REGOLE_DEFAULT).superata).toBe(true);
  });

  it("non va sotto zero in percentuale", () => {
    expect(calcolaEsito(domande, [1, 1, 1, 1], REGOLE_DEFAULT).percentuale).toBe(0);
  });

  it("studio: giuste su risposte date, senza penalità (2 giuste su 10 = 20%, non 0%)", () => {
    const dieci = Array.from({ length: 10 }, (_, i) => domanda("logica", String(i)));
    const risposte = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1];
    expect(calcolaEsito(dieci, risposte, REGOLE_DEFAULT).percentuale).toBe(0); // simulazione: 2 − 8 × 0,25 = 0
    expect(calcolaEsito(dieci, risposte, REGOLE_DEFAULT, "studio").percentuale).toBe(20);
  });

  it("studio interrotto: le domande non fatte non contano", () => {
    const esito = calcolaEsito(domande, [0, 1, null, null], REGOLE_DEFAULT, "studio");
    expect(esito.percentuale).toBe(50);
    expect(esito.perMateria).toEqual([{ materia: "storia", corrette: 1, totale: 2 }]);
  });
});
