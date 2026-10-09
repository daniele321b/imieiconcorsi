import { createHmac } from "node:crypto";
import { PIANI, PREZZI_DI_PROVA } from "@imieiconcorsi/core/domain";
import { describe, expect, it } from "vitest";
import { firmaWebhookValida, formEncode, MINIMO_STRIPE } from "../src/billing/stripe";

describe("firma dei webhook Stripe", () => {
  const segreto = "whsec_prova";
  const corpo = '{"type":"checkout.session.completed"}';
  const ora = Date.parse("2026-10-09T10:00:00Z");
  const t = Math.floor(ora / 1000);
  const v1 = createHmac("sha256", segreto).update(`${t}.${corpo}`).digest("hex");

  it("accetta la firma giusta, anche tra più v1", () => {
    expect(firmaWebhookValida(corpo, `t=${t},v1=${v1}`, segreto, ora)).toBe(true);
    expect(firmaWebhookValida(corpo, `t=${t},v1=sbagliata,v1=${v1}`, segreto, ora)).toBe(true);
  });

  it("rifiuta corpo modificato, segreto sbagliato, firma vecchia o mancante", () => {
    expect(firmaWebhookValida(corpo + " ", `t=${t},v1=${v1}`, segreto, ora)).toBe(false);
    expect(firmaWebhookValida(corpo, `t=${t},v1=${v1}`, "whsec_altro", ora)).toBe(false);
    expect(firmaWebhookValida(corpo, `t=${t},v1=${v1}`, segreto, ora + 10 * 60_000)).toBe(false);
    expect(firmaWebhookValida(corpo, undefined, segreto, ora)).toBe(false);
  });
});

describe("parametri per Stripe", () => {
  it("codifica gli oggetti annidati come vuole l'API", () => {
    expect(formEncode({ mode: "payment", line_items: { 0: { quantity: 1, price_data: { currency: "eur" } } }, vuoto: undefined })).toEqual([
      "mode=payment",
      "line_items%5B0%5D%5Bquantity%5D=1",
      "line_items%5B0%5D%5Bprice_data%5D%5Bcurrency%5D=eur",
    ]);
  });
});

describe("prezzi", () => {
  it("con i prezzi di prova nessun piano scende sotto il minimo di Stripe", () => {
    for (const p of [PIANI.medium, PIANI.pro]) {
      expect(p.prezzo.mensile).toBeGreaterThanOrEqual(MINIMO_STRIPE);
      expect(p.prezzo.annuale).toBeGreaterThanOrEqual(MINIMO_STRIPE);
      if (PREZZI_DI_PROVA) expect(p.prezzo).toEqual({ mensile: 0.5, annuale: 0.5 });
    }
  });
});
