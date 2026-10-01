import { describe, expect, it } from "vitest";
import { citaBancaDati, classificaComparto, toConcorso, type InpaBando } from "../src/jobs/inpa";

const bando = (ente: string, titolo = "Concorso per istruttore amministrativo"): InpaBando => ({
  id: "abc",
  titolo,
  entiRiferimento: [ente],
});

describe("classificaComparto", () => {
  it.each([
    ["Comune di Cavernago", "enti-locali"],
    ["Provincia di Teramo", "enti-locali"],
    ["Regione Umbria", "enti-locali"],
    ["Universita' degli studi di Ferrara", "universita"],
    ["Azienda Sanitaria Locale di Bari", "sanita"],
    ["INPS - Istituto Nazionale della Previdenza Sociale", "inps"],
    ["Ministero della Giustizia", "ministeri"],
    ["Ministero dell'Interno - Dipartimento della Pubblica Sicurezza", "forze-ordine"],
    ["Citta' Metropolitana di Firenze", "enti-locali"],
    ["Agenzia Regionale di Sanita della Toscana", "sanita"],
    ["Conservatorio di musica di Siena", "altro"],
  ])("%s → %s", (ente, comparto) => {
    expect(classificaComparto(bando(ente))).toBe(comparto);
  });

  it("non scambia un comune per un ente di ricerca per via del titolo", () => {
    expect(classificaComparto(bando("Comune di Morbegno", "Avviso di ricerca di personale"))).toBe("enti-locali");
  });
});

describe("toConcorso", () => {
  it("mappa i campi e marca le materie come stimate", () => {
    const c = toConcorso({
      ...bando("Comune di Gargnano"),
      descrizione: "<p>Prova <strong>scritta</strong>&nbsp;e orale</p>",
      dataScadenza: "2026-10-16T10:00:00Z",
      numPosti: 2,
    });
    expect(c).toMatchObject({
      comparto: "enti-locali",
      ente: "Comune di Gargnano",
      scadenza: "2026-10-16T10:00:00Z",
      posti: 2,
      descrizione: "Prova scritta e orale",
      materieStimate: true,
      url: "https://www.inpa.gov.it/bandi-e-avvisi/dettaglio-bando-avviso/?concorso_id=abc",
    });
  });
});

describe("citaBancaDati", () => {
  it.each([
    ["La prova si svolgerà sulla banca dati pubblicata sul sito", true],
    ["Le BANCHE DATI saranno rese disponibili", true],
    ["quesiti estratti dalla banca-dati", true],
    ["Prova scritta e orale", false],
  ])("%s → %s", (descrizione, atteso) => {
    expect(citaBancaDati({ ...bando("Comune di Pavia"), descrizione: `<p>${descrizione}</p>` })).toBe(atteso);
  });
});
