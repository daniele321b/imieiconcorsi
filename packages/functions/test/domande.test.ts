import { DomandaSchema } from "@imieiconcorsi/core/domande";
import { readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";

// Controlli sulla banca domande statica prima di ogni deploy (scripts/deploy.sh test).
const CARTELLA = join(__dirname, "../../../data/domande");
const file = readdirSync(CARTELLA).filter((f) => f.endsWith(".json"));
const normalizza = (t: string) => t.toLowerCase().replace(/[^a-zà-ù0-9]+/g, " ").trim();

describe.each(file)("data/domande/%s", (nome) => {
  const materia = nome.replace(/\.json$/, "");
  const domande = JSON.parse(readFileSync(join(CARTELLA, nome), "utf8")) as unknown[];

  it("ogni domanda rispetta lo schema", () => {
    for (const [i, d] of domande.entries()) {
      const res = DomandaSchema.safeParse(d);
      expect(res.success, `domanda ${i}: ${res.error?.issues.map((x) => `${x.path.join(".")} ${x.message}`).join("; ")}`).toBe(true);
    }
  });

  it("tutte della materia del file", () => {
    expect(domande.every((d) => (d as { materia: string }).materia === materia)).toBe(true);
  });

  it("id unici", () => {
    const ids = domande.map((d) => (d as { id: string }).id);
    expect(ids.length).toBe(new Set(ids).size);
  });

  it("nessuna domanda ripetuta (stesso testo e stesse opzioni)", () => {
    const testi = domande.map((d) => {
      const { testo, opzioni } = d as { testo: string; opzioni: string[] };
      return [normalizza(testo), ...opzioni.map(normalizza).sort()].join(" | ");
    });
    const doppie = testi.filter((t, i) => testi.indexOf(t) !== i);
    expect(doppie).toEqual([]);
  });
});
