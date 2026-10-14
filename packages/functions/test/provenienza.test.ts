import { provenienzaDa, pulisciValore, queryProvenienza, riepilogoProvenienza, SENZA_FONTE } from "@imieiconcorsi/core/provenienza";
import { describe, expect, it } from "vitest";

// Test della provenienza degli iscritti dai link UTM (core/provenienza.ts).

describe("provenienza degli iscritti", () => {
  it("ripulisce i valori UTM", () => {
    expect(pulisciValore(" Instagram ")).toBe("instagram");
    expect(pulisciValore("Lancio Ottobre")).toBe("lancio_ottobre");
    expect(pulisciValore("<script>alert(1)</script>")).toBe("scriptalert1script");
    expect(pulisciValore("x".repeat(60))).toHaveLength(40);
    expect(pulisciValore("")).toBeUndefined();
    expect(pulisciValore("!!!")).toBeUndefined();
    expect(pulisciValore(42)).toBeUndefined();
  });

  it("serve utm_source; tiene solo i quattro parametri UTM", () => {
    expect(provenienzaDa({ utm_medium: "social" })).toBeUndefined();
    expect(provenienzaDa({ utm_source: "TikTok", utm_campaign: "Bio", fbclid: "abc123", altro: "x" })).toEqual({
      fonte: "tiktok",
      campagna: "bio",
    });
    expect(
      provenienzaDa({ utm_source: "facebook", utm_medium: "paid", utm_campaign: "lancio", utm_content: "annuncio-a" }),
    ).toEqual({ fonte: "facebook", mezzo: "paid", campagna: "lancio", contenuto: "annuncio-a" });
  });

  it("andata e ritorno tra provenienza e query string di GET /me", () => {
    const p = { fonte: "instagram", mezzo: "social", campagna: "bio" };
    const query = queryProvenienza(p);
    expect(query).toBe("?utm_source=instagram&utm_medium=social&utm_campaign=bio");
    expect(provenienzaDa(Object.fromEntries(new URLSearchParams(query)))).toEqual(p);
  });

  it("conta gli iscritti per fonte negli ultimi 7 e 30 giorni e in tutto", () => {
    const ora = new Date("2026-10-13T12:00:00Z");
    // Data ISO di `giorni` giorni fa.
    const fa = (giorni: number) => new Date(ora.getTime() - giorni * 864e5).toISOString();
    const { totali, righe } = riepilogoProvenienza(
      [
        { createdAt: fa(1), provenienza: { fonte: "instagram", campagna: "bio" } },
        { createdAt: fa(10), provenienza: { fonte: "instagram", campagna: "bio" } },
        { createdAt: fa(2), provenienza: { fonte: "tiktok" } },
        { createdAt: fa(60), provenienza: { fonte: "instagram", campagna: "bio" } },
        { createdAt: fa(3) },
        { createdAt: fa(100) },
      ],
      ora,
    );
    expect(totali).toEqual({ ultimi7: 3, ultimi30: 4, totale: 6 });
    expect(righe).toEqual([
      { fonte: "instagram", mezzo: undefined, campagna: "bio", contenuto: undefined, ultimi7: 1, ultimi30: 2, totale: 3 },
      { fonte: SENZA_FONTE, mezzo: undefined, campagna: undefined, contenuto: undefined, ultimi7: 1, ultimi30: 1, totale: 2 },
      { fonte: "tiktok", mezzo: undefined, campagna: undefined, contenuto: undefined, ultimi7: 1, ultimi30: 1, totale: 1 },
    ]);
  });
});
