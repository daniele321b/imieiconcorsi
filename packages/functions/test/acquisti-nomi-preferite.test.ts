import { esitoAcquisto } from "@imieiconcorsi/core/acquisti";
import { conMaiuscola, conModificheAdmin, filtraConcorsi, filtriAttivi, nomeConcorso, nomiDistinti, ordinaConcorsi, scadenzaDiComodo, scadenzaVera, senzaModificheAdmin, tipoBando } from "@imieiconcorsi/core/concorsi";
import { PIANI, type Concorso } from "@imieiconcorsi/core/domain";
import { aggiornaProgresso, candidatePerSelezione, conPreferita, idDomanda, numeriAccesi } from "@imieiconcorsi/core/progressi";
import { describe, expect, it } from "vitest";

const ora = new Date("2026-10-10T10:00:00Z");
const GIORNO = 86_400_000;
const tra = (giorni: number) => new Date(ora.getTime() + giorni * GIORNO).toISOString();

describe("acquisto con un piano già attivo", () => {
  it("senza piano attivo parte da oggi", () => {
    expect(esitoAcquisto({ piano: "free" }, { piano: "pro", periodo: "trimestrale" }, ora)).toEqual({ consentito: true, tipo: "nuovo", scadenza: tra(90) });
    // Piano scaduto: come Free.
    expect(esitoAcquisto({ piano: "pro", scadenza: tra(-1) }, { piano: "pro", periodo: "mensile" }, ora)).toMatchObject({ tipo: "nuovo", scadenza: tra(30) });
  });

  it("stesso piano: i giorni comprati si aggiungono alla scadenza (Pro di un anno + trimestrale)", () => {
    const esito = esitoAcquisto({ piano: "pro", scadenza: tra(300), periodo: "annuale" }, { piano: "pro", periodo: "trimestrale" }, ora);
    expect(esito).toEqual({ consentito: true, tipo: "aggiunta", scadenza: tra(390) });
  });

  it("da Medium a Pro: i giorni Medium diventano giorni Pro in proporzione al prezzo", () => {
    const esito = esitoAcquisto({ piano: "medium", scadenza: tra(100), periodo: "annuale" }, { piano: "pro", periodo: "mensile" }, ora);
    const convertiti = Math.floor((100 * PIANI.medium.prezzo.annuale) / PIANI.pro.prezzo.annuale);
    expect(esito).toEqual({ consentito: true, tipo: "passaggio", scadenza: tra(convertiti + 30), giorniRimasti: 100, giorniConvertiti: convertiti });
    expect(convertiti).toBeLessThan(100); // il Pro costa di più: meno giorni, nessuna scorciatoia
  });

  it("da Pro a Medium mentre il Pro è attivo: non si può", () => {
    const esito = esitoAcquisto({ piano: "pro", scadenza: tra(200), periodo: "annuale" }, { piano: "medium", periodo: "trimestrale" }, ora);
    expect(esito.consentito).toBe(false);
    if (!esito.consentito) expect(esito.motivo).toMatch(/aggiungere tempo al Pro/);
  });

  it("piano dato dall'admin senza scadenza: lo stesso piano non si compra", () => {
    expect(esitoAcquisto({ piano: "medium", scadenza: null }, { piano: "medium", periodo: "mensile" }, ora).consentito).toBe(false);
    expect(esitoAcquisto({ piano: "medium", scadenza: null }, { piano: "pro", periodo: "mensile" }, ora)).toMatchObject({ tipo: "nuovo", scadenza: tra(30) });
  });
});

describe("nomi dei concorsi", () => {
  it("prima lettera maiuscola, anche dopo virgolette o numeri", () => {
    expect(conMaiuscola("  istruttore amministrativo")).toBe("Istruttore amministrativo");
    expect(conMaiuscola("«agente» di polizia")).toBe("«Agente» di polizia");
    expect(conMaiuscola("è indetto")).toBe("È indetto");
  });

  it("il nome ha l'anno, così i concorsi ricorrenti si distinguono", () => {
    expect(nomeConcorso({ titolo: "Concorso", figura: "agente di polizia di stato", pubblicatoIl: "2026-03-01T00:00:00Z" })).toBe("Agente di polizia di stato 2026");
    expect(nomeConcorso({ titolo: "Concorso", figura: "Agente di polizia di stato", pubblicatoIl: "2025-03-01T00:00:00Z" })).toBe("Agente di polizia di stato 2025");
    // Anno già nel titolo, o titolo che finisce con un numero.
    expect(nomeConcorso({ titolo: "Allievi agenti 2026", pubblicatoIl: "2026-03-01T00:00:00Z" })).toBe("Allievi agenti 2026");
    expect(nomeConcorso({ titolo: "Funzionari area 3", scadenza: "2026-12-01T00:00:00Z" })).toBe("Funzionari area 3 · 2026");
    expect(nomeConcorso({ titolo: "senza date" })).toBe("Senza date");
  });

  it("nelle liste, stesso ente e stesso nome: si aggiunge la data e, se serve, il codice", () => {
    const base = { ente: "Comune di Roma", titolo: "Istruttore", figura: undefined, scadenza: undefined };
    const nomi = nomiDistinti([
      { ...base, id: "aaaaaa111111", pubblicatoIl: "2026-03-01T10:00:00Z" },
      { ...base, id: "bbbbbb222222", pubblicatoIl: "2026-06-15T10:00:00Z" },
      { ...base, id: "cccccc333333", pubblicatoIl: "2026-06-15T10:00:00Z" },
      { ...base, id: "dddddd444444", ente: "Comune di Milano", pubblicatoIl: "2026-03-01T10:00:00Z" },
    ]);
    expect(nomi.get("aaaaaa111111")).toBe("Istruttore · 1 marzo 2026");
    expect(nomi.get("bbbbbb222222")).toBe("Istruttore · 15 giugno 2026 · cod. 222222");
    expect(nomi.get("cccccc333333")).toBe("Istruttore · 15 giugno 2026 · cod. 333333");
    expect(nomi.get("dddddd444444")).toBe("Istruttore 2026"); // altro ente: il nome con l'anno basta
  });
});

describe("domande preferite", () => {
  it("si salvano e si tolgono, e si ritrovano in ordine", () => {
    let p = conPreferita(undefined, 42, true);
    p = conPreferita(p, 7, true);
    p = conPreferita(p, 5977, true);
    expect(p.nPreferite).toBe(3);
    expect(numeriAccesi(p.preferite)).toEqual([7, 42, 5977]);
    p = conPreferita(p, 42, false);
    expect(numeriAccesi(p.preferite)).toEqual([7, 5977]);
    expect(idDomanda(7)).toBe("n00007");
  });

  it("una sessione sulle preferite usa solo quelle", () => {
    const domande = [1, 2, 3, 4].map((n) => ({ id: idDomanda(n) }));
    const progresso = { ...aggiornaProgresso(undefined, [{ numero: 1, giusta: true }]), ...conPreferita(undefined, 3, true) };
    expect(candidatePerSelezione(domande, progresso, "preferite")).toEqual({ prima: [{ id: "n00003" }], poi: [] });
  });
});

describe("ordinamenti della ricerca", () => {
  const adesso = new Date("2026-10-11T10:00:00Z");
  const bandi = [
    { id: "a", titolo: "Zootecnico", ente: "Comune di Bari", scadenza: "2026-11-01T00:00:00Z", pubblicatoIl: "2026-10-01T00:00:00Z", posti: 3 },
    { id: "b", titolo: "agente", ente: "Ministero", scadenza: "2026-12-01T00:00:00Z", pubblicatoIl: "2026-09-01T00:00:00Z", posti: 10 },
    { id: "c", titolo: "Bibliotecario", ente: "Ateneo", scadenza: "2026-09-01T00:00:00Z", pubblicatoIl: "2026-08-01T00:00:00Z" },
  ];
  const ids = (o: Parameters<typeof ordinaConcorsi>[1]) => ordinaConcorsi(bandi, o, adesso).map((c) => c.id);

  it("ogni ordinamento ha il suo opposto", () => {
    expect(ids("scadenza")).toEqual(["a", "b", "c"]); // aperti dal più vicino, poi i chiusi
    expect(ids("scadenza-lontana")).toEqual(["b", "a", "c"]);
    expect(ids("pubblicazione")).toEqual(["a", "b", "c"]);
    expect(ids("pubblicazione-vecchi")).toEqual(["c", "b", "a"]);
  });

  it("per nome del concorso (con la maiuscola), dalla A alla Z e al contrario", () => {
    expect(ids("nome-az")).toEqual(["b", "c", "a"]);
    expect(ids("nome-za")).toEqual(["a", "c", "b"]);
  });
});

describe("tipi di bando", () => {
  it.each([
    ["Concorso pubblico per esami per 10 istruttori amministrativi", "concorso"],
    ["Avviso di mobilità volontaria esterna per 2 agenti di polizia locale", "mobilita"],
    ["Selezione per assunzioni a tempo determinato di educatori", "tempo-determinato"],
    ["Avviso per il conferimento di incarico di collaborazione", "incarico"],
    ["Bando per 5 borse di studio e tirocini curriculari", "tirocinio"],
    ["Progressione verticale riservata al personale interno", "interno"],
  ])("%s → %s", (titolo, atteso) => {
    expect(tipoBando({ titolo })).toBe(atteso);
  });

  it("filtro per tipo: nessuno scelto = tutti", () => {
    const bandi = [
      { titolo: "Mobilità esterna", sedi: [] },
      { titolo: "Concorso per agenti", sedi: [] },
    ];
    expect(filtraConcorsi(bandi, { tipi: ["mobilita"] }).map((b) => b.titolo)).toEqual(["Mobilità esterna"]);
    expect(filtraConcorsi(bandi, {})).toHaveLength(2);
    expect(filtriAttivi({ tipi: [] })).toBe(0);
  });
});

describe("correzioni dell'admin ai bandi", () => {
  const inpa = { id: "x", titolo: "Concorso per agenti", ente: "Ministero", sedi: [], comparto: "altro", url: "", materie: ["logica"], materieStimate: true, bancaDatiPrevista: false, bancaDati: false, fonte: "inpa", aggiornatoIl: "" } as Concorso;

  it("si applicano, si ricordano i valori di inPA e si annullano", () => {
    const corretto = conModificheAdmin(inpa, { figura: "Allievi agenti", posti: 100 });
    expect(corretto).toMatchObject({ figura: "Allievi agenti", posti: 100, modificheAdmin: { figura: "Allievi agenti", posti: 100 }, originaliInpa: { figura: null, posti: null } });
    // Seconda correzione: gli originali restano quelli di inPA.
    const ancora = conModificheAdmin(corretto, { ...corretto.modificheAdmin, figura: "Allievi agenti PS" });
    expect(ancora.originaliInpa).toEqual({ figura: null, posti: null });
    const annullato = senzaModificheAdmin(ancora);
    expect(annullato.figura).toBeUndefined();
    expect(annullato.posti).toBeUndefined();
    expect(annullato.modificheAdmin).toBeUndefined();
    expect(annullato.titolo).toBe("Concorso per agenti");
  });

  it("l'import del mattino le riapplica sopra i dati freschi di inPA", () => {
    const fresco = { ...inpa, ente: "Ministero dell'Interno", scadenza: "2026-12-01T00:00:00Z" };
    const dopo = conModificheAdmin(fresco, { scadenza: "2026-12-15T00:00:00Z" }, true);
    expect(dopo.scadenza).toBe("2026-12-15T00:00:00Z");
    expect(dopo.ente).toBe("Ministero dell'Interno");
    expect(dopo.originaliInpa).toEqual({ scadenza: "2026-12-01T00:00:00Z" });
  });
});

describe("scadenze di comodo di inPA (bandi aperti fino a esaurimento)", () => {
  const ora = new Date("2026-10-12T10:00:00Z");
  it("2099 e 4999 non sono scadenze vere, il prossimo anno sì", () => {
    expect(scadenzaDiComodo("4999-12-31T00:00:00Z", ora)).toBe(true);
    expect(scadenzaDiComodo("2099-12-31T00:00:00Z", ora)).toBe(true);
    expect(scadenzaDiComodo("2027-06-30T00:00:00Z", ora)).toBe(false);
    expect(scadenzaVera("2099-12-31T00:00:00Z", ora)).toBeUndefined();
    expect(scadenzaVera(undefined, ora)).toBeUndefined();
  });

  it("il nome non prende l'anno dalla data di comodo", () => {
    expect(nomeConcorso({ titolo: "Rilevatore statistico", scadenza: "2099-12-31T00:00:00Z" })).toBe("Rilevatore statistico");
  });

  it("con «scadenza più lontana» vanno in fondo, come quelli senza scadenza", () => {
    const bandi = [
      { id: "a", titolo: "A", scadenza: "4999-12-31T00:00:00Z" },
      { id: "b", titolo: "B", scadenza: "2026-12-01T00:00:00Z" },
      { id: "c", titolo: "C", scadenza: "2026-11-01T00:00:00Z" },
    ];
    expect(ordinaConcorsi(bandi, "scadenza-lontana", ora).map((c) => c.id)).toEqual(["b", "c", "a"]);
    expect(ordinaConcorsi(bandi, "scadenza", ora).map((c) => c.id)).toEqual(["c", "b", "a"]);
  });
});
