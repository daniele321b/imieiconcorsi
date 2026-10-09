import { filtraConcorsi, ordinaConcorsi } from "@imieiconcorsi/core/concorsi";
import { PIANI, type CodiceSconto } from "@imieiconcorsi/core/domain";
import { emailConsentita } from "@imieiconcorsi/core/registrazione";
import { FORMATO_CODICE, generaCodice, motivoRifiuto, normalizzaCodice, prezzoScontato } from "@imieiconcorsi/core/sconti";
import { describe, expect, it } from "vitest";

describe("ordinaConcorsi", () => {
  const bandi = [
    { id: "a", scadenza: "2026-11-10", pubblicatoIl: "2026-09-01", posti: 3 },
    { id: "b", scadenza: "2026-10-20", pubblicatoIl: "2026-10-01" },
    { id: "c", scadenza: "2026-12-01", posti: 40 },
    { id: "d", scadenza: "2026-10-15", pubblicatoIl: "2026-10-05", posti: 3 },
  ];
  const ids = (l: { id: string }[]) => l.map((c) => c.id);
  // Data fissa: con la data di oggi il test cambierebbe esito quando i bandi di prova scadono.
  const oggi = new Date("2026-10-01T00:00:00Z");

  it("per scadenza: la più vicina prima", () => {
    expect(ids(ordinaConcorsi(bandi, "scadenza", oggi))).toEqual(["d", "b", "a", "c"]);
  });
  it("per data di uscita: i più recenti prima, senza data in fondo", () => {
    expect(ids(ordinaConcorsi(bandi, "pubblicazione", oggi))).toEqual(["d", "b", "a", "c"]);
  });
  it("per posti: i più numerosi prima, a parità la scadenza più vicina, senza posti in fondo", () => {
    expect(ids(ordinaConcorsi(bandi, "piu-posti", oggi))).toEqual(["c", "d", "a", "b"]);
  });
  it("per meno posti: i meno numerosi prima, senza posti in fondo", () => {
    expect(ids(ordinaConcorsi(bandi, "meno-posti", oggi))).toEqual(["d", "a", "c", "b"]);
  });
  it("non modifica la lista originale", () => {
    ordinaConcorsi(bandi, "piu-posti", oggi);
    expect(ids(bandi)).toEqual(["a", "b", "c", "d"]);
  });
});

describe("codici sconto", () => {
  const base: CodiceSconto = { codice: "BENVENUTO20", percentuale: 20, usi: 0, attivo: true, creatoIl: "2026-10-01", creatoDa: "admin" };
  const oggi = new Date("2026-10-07T10:00:00Z");

  it("normalizza e genera codici nel formato giusto", () => {
    expect(normalizzaCodice(" benvenuto 20 ")).toBe("BENVENUTO20");
    for (let i = 0; i < 20; i++) expect(generaCodice()).toMatch(FORMATO_CODICE);
  });

  it("calcola il prezzo scontato al centesimo", () => {
    expect(prezzoScontato(9.99, 20)).toBe(7.99);
    expect(prezzoScontato(79.99, 50)).toBe(40);
    expect(prezzoScontato(19.99, 100)).toBe(0);
  });

  it.each([
    ["valido", base, "medium", [], null],
    ["inesistente", undefined, "medium", [], "Codice sconto non valido."],
    ["disattivato", { ...base, attivo: false }, "medium", [], "Codice sconto non valido."],
    ["scaduto", { ...base, validoFino: "2026-10-06T23:59:59.000Z" }, "medium", [], "Questo codice sconto è scaduto."],
    ["esaurito", { ...base, usiMassimi: 5, usi: 5 }, "medium", [], "Questo codice sconto è esaurito."],
    ["piano free", base, "free", [], "Il codice sconto vale solo sui piani a pagamento."],
    ["solo pro", { ...base, piani: ["pro"] as ("medium" | "pro")[] }, "medium", [], "Questo codice vale solo per il piano Pro."],
    ["già usato", base, "pro", ["BENVENUTO20"], "Hai già usato questo codice sconto."],
  ] as const)("%s", (_, codice, piano, usati, atteso) => {
    expect(motivoRifiuto(codice, { piano, codiciUsati: [...usati], oggi })).toBe(atteso);
  });
});

describe("email consentite in registrazione", () => {
  it.each([
    ["mario.rossi@gmail.com", true],
    ["Mario@HOTMAIL.IT", true],
    ["a@libero.it", true],
    ["a@icloud.com", true],
    ["a@mailinator.com", false],
    ["a@10minutemail.com", false],
    ["a@comune.roma.it", false],
  ])("%s → %s", (email, atteso) => {
    expect(emailConsentita(email)).toBe(atteso);
  });
});

describe("piani", () => {
  it("pubblicità solo nel Free", () => {
    expect(PIANI.free.limiti.pubblicita).toBe(true);
    expect(PIANI.medium.limiti.pubblicita).toBe(false);
    expect(PIANI.pro.limiti.pubblicita).toBe(false);
  });
});

describe("filtraConcorsi", () => {
  const ora = new Date("2026-10-10T10:00:00Z");
  const bandi = [
    { id: "a", scadenza: "2026-10-14T10:00:00Z", pubblicatoIl: "2026-10-08T08:00:00Z", posti: 1, sedi: ["Milano (MI)"], tipoProcedura: "ESAMI", bancaDatiPrevista: true, bancaDati: false },
    { id: "b", scadenza: "2026-11-30T10:00:00Z", pubblicatoIl: "2026-09-01T08:00:00Z", posti: 12, sedi: ["Roma"], tipoProcedura: "TITOLI_ESAMI", bancaDatiPrevista: false, bancaDati: false },
    { id: "c", scadenza: "2026-10-25T10:00:00Z", sedi: [], bancaDatiPrevista: false, bancaDati: false },
  ];
  const ids = (l: { id: string }[]) => l.map((c) => c.id);

  it.each([
    ["nessun filtro", {}, ["a", "b", "c"]],
    ["scade entro 7 giorni", { scadeEntroGiorni: 7 }, ["a"]],
    ["scade entro 30 giorni", { scadeEntroGiorni: 30 }, ["a", "c"]],
    ["pubblicati negli ultimi 7 giorni", { pubblicatoDaGiorni: 7 }, ["a"]],
    ["almeno 5 posti", { postiMinimi: 5 }, ["b"]],
    ["sede", { sede: "milano" }, ["a"]],
    ["procedura", { procedura: "TITOLI_ESAMI" }, ["b"]],
    ["con banca dati", { soloBancaDati: true }, ["a"]],
  ] as const)("%s", (_, filtri, attesi) => {
    expect(ids(filtraConcorsi(bandi, filtri, ora))).toEqual(attesi);
  });
});

describe("ordinaConcorsi con i bandi scaduti", () => {
  it("prima gli aperti per scadenza, poi gli scaduti dal più recente", () => {
    const ora = new Date("2026-10-10T10:00:00Z");
    const bandi = [
      { id: "scaduto-vecchio", scadenza: "2026-05-01" },
      { id: "aperto-lontano", scadenza: "2026-12-01" },
      { id: "scaduto-recente", scadenza: "2026-10-01" },
      { id: "aperto-vicino", scadenza: "2026-10-15" },
    ];
    expect(ordinaConcorsi(bandi, "scadenza", ora).map((b) => b.id)).toEqual(["aperto-vicino", "aperto-lontano", "scaduto-recente", "scaduto-vecchio"]);
  });
});
