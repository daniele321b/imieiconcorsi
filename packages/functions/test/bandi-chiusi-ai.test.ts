import { filtraConcorsi, filtriAttivi } from "@imieiconcorsi/core/concorsi";
import { PIANI } from "@imieiconcorsi/core/domain";
import { describe, expect, it } from "vitest";
import {
  contestoDomanda,
  domandeValide,
  gettoniUsati,
  meseCorrente,
  messaggiTutor,
  MAX_MESSAGGI,
  puntiDeboli,
  rinnovoGettoni,
  risposteDellaMateria,
} from "../src/ai/logic";
import { paginaPiuVecchiaDi } from "../src/jobs/inpa";

const ids = (l: { id: string }[]) => l.map((c) => c.id);

describe("filtro Aperti / Chiusi", () => {
  const ora = new Date("2026-10-10T10:00:00Z");
  const base = { sedi: [], bancaDatiPrevista: false, bancaDati: false };
  const bandi = [
    { ...base, id: "aperto", scadenza: "2026-10-14T10:00:00Z" },
    { ...base, id: "chiuso", scadenza: "2026-09-01T10:00:00Z" },
    { ...base, id: "chiuso-ieri", scadenza: "2026-10-09T10:00:00Z" },
  ];

  it("all'inizio si vedono tutti", () => {
    expect(ids(filtraConcorsi(bandi, {}, ora))).toEqual(["aperto", "chiuso", "chiuso-ieri"]);
  });
  it("togliendo Aperti restano i chiusi", () => {
    expect(ids(filtraConcorsi(bandi, { aperti: false }, ora))).toEqual(["chiuso", "chiuso-ieri"]);
  });
  it("togliendo Chiusi restano gli aperti", () => {
    expect(ids(filtraConcorsi(bandi, { chiusi: false }, ora))).toEqual(["aperto"]);
  });
  it("'scade entro' non conta i bandi già chiusi", () => {
    expect(ids(filtraConcorsi(bandi, { scadeEntroGiorni: 7 }, ora))).toEqual(["aperto"]);
  });
  it("una casella tolta conta tra i filtri attivi", () => {
    expect(filtriAttivi({})).toBe(0);
    expect(filtriAttivi({ aperti: true, chiusi: true })).toBe(0);
    expect(filtriAttivi({ chiusi: false, postiMinimi: 5 })).toBe(2);
  });
});

describe("storico dei bandi chiusi", () => {
  it("si ferma quando tutta la pagina è più vecchia del limite", () => {
    const pagina = (...scadenze: (string | null)[]) => scadenze.map((d, i) => ({ id: String(i), titolo: "x", dataScadenza: d }));
    expect(paginaPiuVecchiaDi(pagina("2025-01-02", "2025-01-05"), "2025-04-01")).toBe(true);
    // L'ordine di inPA è approssimativo: basta un bando recente per continuare.
    expect(paginaPiuVecchiaDi(pagina("2025-01-02", "2025-06-05"), "2025-04-01")).toBe(false);
    expect(paginaPiuVecchiaDi(pagina(null), "2025-04-01")).toBe(false);
  });
});

describe("gettoni AI", () => {
  const ora = new Date("2026-10-31T23:30:00Z");
  it("contano solo nel mese corrente e si rinnovano il primo del mese", () => {
    expect(meseCorrente(ora)).toBe("2026-10");
    expect(gettoniUsati({ mese: "2026-10", usati: 12 }, ora)).toBe(12);
    expect(gettoniUsati({ mese: "2026-09", usati: 280 }, ora)).toBe(0);
    expect(gettoniUsati(undefined, ora)).toBe(0);
    expect(rinnovoGettoni(ora)).toBe("2026-11-01T00:00:00.000Z");
    expect(rinnovoGettoni(new Date("2026-12-15T00:00:00Z"))).toBe("2027-01-01T00:00:00.000Z");
  });
  it("solo il piano Pro ne ha", () => {
    expect(PIANI.free.limiti.gettoniAi).toBe(0);
    expect(PIANI.medium.limiti.gettoniAi).toBe(0);
    expect(PIANI.pro.limiti.gettoniAi).toBeGreaterThan(0);
  });
});

describe("punti deboli", () => {
  const esito = (perMateria: { materia: string; corrette: number; totale: number }[]) => ({
    esito: { corrette: 0, errate: 0, omesse: 0, punteggio: 0, massimo: 0, percentuale: 0, superata: false, perMateria },
  });

  it("ordina dalla percentuale più bassa, ignora banche dati e materie con poche risposte", () => {
    const deboli = puntiDeboli([
      esito([
        { materia: "logica", corrette: 2, totale: 10 },
        { materia: "storia", corrette: 9, totale: 10 },
        { materia: "inglese", corrette: 0, totale: 2 },
        { materia: "bd#bd_123", corrette: 0, totale: 50 },
      ]),
      esito([{ materia: "storia", corrette: 1, totale: 10 }]),
    ] as never);
    expect(deboli).toEqual([
      { materia: "logica", percentuale: 20, risposte: 10 },
      { materia: "storia", percentuale: 50, risposte: 20 },
    ]);
  });

  it("raccoglie le risposte di una materia una volta sola, dalla sessione più recente", () => {
    const sessioni = [
      { domande: [{ materia: "logica", id: "q1" }, { materia: "storia", id: "s1" }], risposte: [2, 0] },
      { domande: [{ materia: "logica", id: "q1" }, { materia: "logica", id: "q2" }], risposte: [1, null] },
    ];
    expect(risposteDellaMateria(sessioni as never, "logica")).toEqual([
      { materia: "logica", id: "q1", risposta: 2 },
      { materia: "logica", id: "q2", risposta: null },
    ]);
  });
});

describe("domande generate dall'AI", () => {
  const buona = { argomento: "Logica", testo: "Quale numero completa la serie 2, 4, 8, ?", opzioni: ["10", "12", "16", "14"], corretta: 2, spiegazione: "Ogni numero è il doppio del precedente." };

  it("tiene solo quelle con 4 risposte distinte e una giusta valida", () => {
    const valide = domandeValide({
      domande: [
        buona,
        { ...buona, opzioni: ["a", "b", "c"] },
        { ...buona, opzioni: ["16", "16", "12", "10"] },
        { ...buona, corretta: 4 },
        { ...buona, spiegazione: "" },
      ],
    });
    expect(valide).toEqual([buona]);
  });
  it("non si rompe con un input strano", () => {
    expect(domandeValide(undefined)).toEqual([]);
    expect(domandeValide({ domande: "nulla" })).toEqual([]);
  });
});

describe("messaggi per il tutor", () => {
  const domanda = { materia: "logica", testo: "2+2?", opzioni: ["3", "4"], corretta: 1, risposta: 0, spiegazione: "Somma." };

  it("mette la domanda, la risposta giusta e quella data nel primo messaggio", () => {
    expect(contestoDomanda(domanda)).toContain("Risposta giusta: B.");
    expect(contestoDomanda(domanda)).toContain("Io ho risposto A.");
    const m = messaggiTutor({ domanda, messaggi: [{ ruolo: "studente", testo: "Perché?" }] });
    expect(m).toHaveLength(1);
    expect(m[0].role).toBe("user");
    expect(m[0].content).toMatch(/^Sto studiando questa domanda[\s\S]*Perché\?$/);
  });

  it("tiene solo gli ultimi messaggi, iniziando sempre dallo studente", () => {
    const messaggi = Array.from({ length: 13 }, (_, i) => ({ ruolo: i % 2 ? ("tutor" as const) : ("studente" as const), testo: `m${i}` }));
    const m = messaggiTutor({ messaggi });
    expect(m.length).toBeLessThanOrEqual(MAX_MESSAGGI);
    expect(m[0].role).toBe("user");
    expect(m.at(-1)).toEqual({ role: "user", content: "m12" });
  });
});
