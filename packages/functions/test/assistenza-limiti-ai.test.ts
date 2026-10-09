import { PREZZI_AI_USD, TETTO_AI_UTENTE_USD } from "@imieiconcorsi/core/domain";
import { describe, expect, it } from "vitest";
import { eFuoriTema, FUORI_TEMA, minutoCorrente, SISTEMA_TUTOR, sogliaSuperata, spesaMicroUsd } from "../src/ai/logic";
import { limiteRichieste } from "../src/richieste/handler";

describe("limiti dell'AI", () => {
  it("la spesa si stima in milionesimi di dollaro dai token", () => {
    // 1 milione di token in ingresso costa PREZZI_AI_USD.ingresso dollari.
    expect(spesaMicroUsd({ input_tokens: 1_000_000, output_tokens: 0 })).toBe(PREZZI_AI_USD.ingresso * 1e6);
    // Una risposta tipica del tutor: frazioni di centesimo, arrotondate per eccesso.
    const tipica = spesaMicroUsd({ input_tokens: 1500, output_tokens: 400 });
    expect(tipica).toBe(Math.ceil(1500 * PREZZI_AI_USD.ingresso + 400 * PREZZI_AI_USD.uscita));
    expect(tipica).toBeLessThan(10_000); // meno di un centesimo
  });

  it("anche al massimo dei token, il tetto per utente vale centinaia di risposte", () => {
    // Chat al limite: ~8 messaggi lunghi + domanda (~5.000 token) e 800 token di risposta.
    const peggiore = spesaMicroUsd({ input_tokens: 5000, output_tokens: 800 });
    expect((TETTO_AI_UTENTE_USD * 1e6) / peggiore).toBeGreaterThan(250);
  });

  it("l'admin è avvisato una volta all'80% e una al 100% del tetto mensile", () => {
    const tetto = 50e6;
    expect(sogliaSuperata(39e6, 39.5e6, tetto)).toBeUndefined();
    expect(sogliaSuperata(39.9e6, 40.1e6, tetto)).toBe(0.8);
    expect(sogliaSuperata(40.1e6, 41e6, tetto)).toBeUndefined();
    expect(sogliaSuperata(49.9e6, 50e6, tetto)).toBe(1);
    // Un salto che le supera entrambe: conta la più alta.
    expect(sogliaSuperata(39e6, 51e6, tetto)).toBe(1);
    expect(sogliaSuperata(51e6, 52e6, tetto)).toBeUndefined();
  });

  it("riconosce il segnale fuori tema anche con testo intorno", () => {
    expect(eFuoriTema(FUORI_TEMA)).toBe(true);
    expect(eFuoriTema(`  ${FUORI_TEMA}\n`)).toBe(true);
    expect(eFuoriTema(`Mi dispiace. ${FUORI_TEMA}`)).toBe(true);
    expect(eFuoriTema("La risposta giusta è la B perché la legge 241/1990…")).toBe(false);
  });

  it("le istruzioni del tutor contengono il segnale e l'ambito", () => {
    expect(SISTEMA_TUTOR).toContain(FUORI_TEMA);
    expect(SISTEMA_TUTOR).toMatch(/concorsi pubblici/);
  });

  it("il minuto per il limite di ritmo è in UTC", () => {
    expect(minutoCorrente(new Date("2026-10-09T10:15:42.123Z"))).toBe("2026-10-09T10:15");
  });
});

describe("richieste di assistenza", () => {
  const ora = new Date("2026-10-09T10:00:00Z");
  const r = (stato: "aperta" | "in-lavorazione" | "chiusa", creataIl = "2026-10-01T10:00:00Z") => ({ stato, creataIl });

  it("si può scrivere se non si è al limite", () => {
    expect(limiteRichieste([], ora)).toBeUndefined();
    expect(limiteRichieste([r("aperta"), r("chiusa"), r("chiusa")], ora)).toBeUndefined();
  });

  it("al massimo 5 richieste non chiuse insieme", () => {
    const aperte = [r("aperta"), r("aperta"), r("in-lavorazione"), r("in-lavorazione"), r("aperta")];
    expect(limiteRichieste(aperte, ora)).toMatch(/5 richieste aperte/);
    expect(limiteRichieste([...aperte.slice(0, 4), r("chiusa")], ora)).toBeUndefined();
  });

  it("al massimo 10 richieste nuove al giorno", () => {
    const oggi = Array.from({ length: 10 }, () => r("chiusa", "2026-10-09T08:00:00Z"));
    expect(limiteRichieste(oggi, ora)).toMatch(/domani/);
    expect(limiteRichieste(oggi.slice(1), ora)).toBeUndefined();
  });
});
