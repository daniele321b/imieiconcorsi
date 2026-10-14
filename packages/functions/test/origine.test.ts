import { daCloudFront } from "@imieiconcorsi/core/http";
import { afterEach, describe, expect, it } from "vitest";

// Test del controllo che le richieste all'API arrivino da CloudFront (core/http.ts).

describe("solo richieste passate da CloudFront", () => {
  afterEach(() => {
    delete process.env.ORIGINE_SEGRETA;
  });

  it("senza segreto configurato non controlla nulla (prove in locale)", () => {
    expect(daCloudFront({})).toBe(true);
  });

  it("con il segreto: passa solo chi ha l'intestazione giusta", () => {
    process.env.ORIGINE_SEGRETA = "segreto-di-prova";
    expect(daCloudFront({ "x-origine-cloudfront": "segreto-di-prova" })).toBe(true);
    expect(daCloudFront({ "x-origine-cloudfront": "sbagliato" })).toBe(false);
    expect(daCloudFront({})).toBe(false);
    expect(daCloudFront(undefined)).toBe(false);
  });
});
