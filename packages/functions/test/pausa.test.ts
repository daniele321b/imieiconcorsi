import { chiudiPausa, tempoSessione } from "@imieiconcorsi/core/domain";
import { describe, expect, it } from "vitest";

// Pausa delle simulazioni (POST /sessioni/{id}/pausa): alla ripresa la scadenza si sposta in
// avanti della pausa; il tempo impiegato non conta le pause.

/** Minuti in millisecondi. */
const minuti = (n: number) => n * 60_000;
/** L'istante a `min` minuti dall'inizio della prova (19/10/2026 alle 10:00 UTC). */
const alle = (min: number) => new Date(Date.parse("2026-10-19T10:00:00Z") + minuti(min));

describe("pausa della simulazione", () => {
  it("riprendere sposta la scadenza e somma la pausa", () => {
    // 30 minuti a disposizione, pausa dal minuto 10 al minuto 25.
    const s = { scadeIl: alle(30).toISOString(), inPausaDal: alle(10).toISOString() };
    expect(chiudiPausa(s, alle(25))).toEqual({ scadeIl: alle(45).toISOString(), pausaMs: minuti(15) });
    // Seconda pausa: si somma alla prima.
    expect(chiudiPausa({ scadeIl: alle(45).toISOString(), inPausaDal: alle(40).toISOString(), pausaMs: minuti(15) }, alle(42))).toEqual({
      scadeIl: alle(47).toISOString(),
      pausaMs: minuti(17),
    });
  });

  it("senza pausa in corso non cambia nulla", () => {
    expect(chiudiPausa({ scadeIl: alle(30).toISOString(), pausaMs: minuti(5) }, alle(20))).toEqual({
      scadeIl: alle(30).toISOString(),
      pausaMs: minuti(5),
    });
  });

  it("tempo impiegato e a disposizione senza le pause", () => {
    // 30 minuti di prova, 15 di pausa (scadenza spostata al minuto 45), consegna al minuto 40.
    const s = { creataIl: alle(0).toISOString(), scadeIl: alle(45).toISOString(), pausaMs: minuti(15), consegnataIl: alle(40).toISOString() };
    expect(tempoSessione(s)).toEqual({ impiegatoMs: minuti(25), disponibileMs: minuti(30) });
    // Consegna dopo la scadenza (browser chiuso): al massimo tutto il tempo.
    expect(tempoSessione({ ...s, consegnataIl: alle(60).toISOString() }).impiegatoMs).toBe(minuti(30));
    // Studio: niente scadenza né pause.
    expect(tempoSessione({ creataIl: alle(0).toISOString(), consegnataIl: alle(12).toISOString() })).toEqual({
      impiegatoMs: minuti(12),
      disponibileMs: undefined,
    });
  });
});
