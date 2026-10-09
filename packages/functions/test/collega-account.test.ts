import { describe, expect, it } from "vitest";
import { decidi, providerDaUsername } from "../src/auth/collega-account";

describe("providerDaUsername", () => {
  it.each([
    ["facebook_10229", { nome: "Facebook", id: "10229" }],
    ["Google_1122_33", { nome: "Google", id: "1122_33" }],
    ["3f2a9c1e-5b7d", undefined],
    ["apple_1", undefined],
  ])("%s", (username, atteso) => {
    expect(providerDaUsername(username)).toEqual(atteso);
  });
});

describe("decidi", () => {
  it("social con account email confermato → collega", () => {
    expect(decidi("PreSignUp_ExternalProvider", [{ username: "uuid-1", stato: "CONFIRMED" }])).toEqual({
      azione: "collega",
      destinazione: "uuid-1",
    });
  });
  it("social con account email mai confermato → nuovo utente (niente collegamento)", () => {
    expect(decidi("PreSignUp_ExternalProvider", [{ username: "uuid-1", stato: "UNCONFIRMED" }])).toEqual({ azione: "procedi" });
  });
  it("primo accesso social → procedi", () => {
    expect(decidi("PreSignUp_ExternalProvider", [])).toEqual({ azione: "procedi" });
  });
  it("registrazione email quando c'è già Facebook → rifiuta indicando Facebook", () => {
    const d = decidi("PreSignUp_SignUp", [{ username: "facebook_1", stato: "EXTERNAL_PROVIDER" }]);
    expect(d).toEqual({ azione: "rifiuta", messaggio: "Esiste già un account con questa email: accedi con Facebook." });
  });
  it("registrazione email nuova → procedi", () => {
    expect(decidi("PreSignUp_SignUp", [])).toEqual({ azione: "procedi" });
  });
});
