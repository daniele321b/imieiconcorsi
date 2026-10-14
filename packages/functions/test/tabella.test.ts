import { describe, expect, it } from "vitest";
import { alternativeRelazioni, domandeDallaTabella, leggiTabella, motivoScarto, type Elemento, type RigaTabella } from "../src/banche-dati/tabella";

// Tabella come nei PDF "solo risposta esatta": numero a x=10, domanda a x=94, risposta a x=473.
function pagina(righe: [number, string[], string[]][], sezione?: string): Elemento[] {
  const el: Elemento[] = [];
  let y = 560;
  if (sezione) el.push({ pagina: 1, testo: `Materia : ${sezione}`, x: 337, y: 572, larghezza: 160 });
  for (const [n, domanda, risposta] of righe) {
    el.push({ pagina: 1, testo: String(n), x: 10, y: y - 6, larghezza: 6 });
    domanda.forEach((t, i) => el.push({ pagina: 1, testo: t, x: 94, y: y - 12 * i, larghezza: t.length * 5 }));
    risposta.forEach((t, i) => el.push({ pagina: 1, testo: t, x: 473, y: y - 12 * i, larghezza: t.length * 5 }));
    y -= 40;
  }
  return el;
}

describe("tabella domanda | risposta esatta", () => {
  it("separa domanda e risposta anche su più righe, con la sezione", () => {
    const el = pagina(
      [
        [1, ["Sinonimo di aborrire"], ["detestare"]],
        [2, ["Non si può escludere che, se Luca non avesse", "risposto male, l'esame sarebbe stato superato."], ["È possibile che l'esame sarebbe", "stato superato"]],
        [3, ["Contrario di corto"], ["lungo"]],
        [4, ["Sinonimo di elenco"], ["lista"]],
        [5, ["Sinonimo di diniego"], ["rifiuto"]],
      ],
      "Capacità verbale",
    );
    // "vera" + "?" attaccati sulla stessa riga: senza spazio.
    // (nel PDF i pezzi arrivano nell'ordine della riga: subito dopo la domanda 1)
    el.splice(3, 0, { pagina: 1, testo: "?", x: 94 + 20 * 5, y: 560, larghezza: 5 });
    const righe = leggiTabella(el);
    expect(righe).toHaveLength(5);
    expect(righe[0]).toEqual({ numero: 1, domanda: "Sinonimo di aborrire?", risposta: "detestare", sezione: "Capacità verbale" });
    expect(righe[1]!.risposta).toBe("È possibile che l'esame sarebbe stato superato");
  });

  it("senza tabella non legge nulla", () => {
    expect(leggiTabella([{ pagina: 1, testo: "1. Domanda A) uno B) due", x: 50, y: 500, larghezza: 100 }])).toEqual([]);
  });
});

describe("alternative ricavate", () => {
  // Riga di tabella di prova nella sezione Logica.
  const riga = (numero: number, domanda: string, risposta: string): RigaTabella => ({ numero, domanda, risposta, sezione: "Logica" });

  it("dalle risposte di domande dello stesso tipo, mai la giusta", () => {
    const { domande } = domandeDallaTabella([
      riga(1, "Sinonimo di aborrire", "detestare"),
      riga(2, "Sinonimo di abrogare", "invalidare"),
      riga(3, "Sinonimo di adamantino", "puro"),
      riga(4, "Sinonimo di assiduo", "costante"),
      riga(5, "Contrario di corto", "lungo"),
    ]);
    const d = domande[0]!;
    expect(d.alternativeRicavate).toBe(true);
    expect(d.opzioni[d.corretta]).toBe("detestare");
    expect(d.opzioni).toHaveLength(4);
    expect(d.pdf.opzioni.slice(1).every((o) => ["invalidare", "puro", "costante"].includes(o))).toBe(true);
  });

  it("coppie: incrociate, mai un'altra coppia vera del file", () => {
    // Testo di una proporzione "a : b = X : Y".
    const testo = (a: string, b: string) => `Quali tra i termini proposti completano correttamente la seguente proporzione? ${a} : ${b} = X : Y`;
    const { domande } = domandeDallaTabella([
      riga(1, testo("Renzo", "I Promessi sposi"), "X = Geppetto; Y = Pinocchio"),
      riga(2, testo("Achille", "Iliade"), "X = Beatrice; Y = Divina Commedia"),
      riga(3, testo("Telemaco", "Odissea"), "X = Eva; Y = Genesi"),
      riga(4, testo("Lavinia", "Eneide"), "X = Mirandolina; Y = La Locandiera"),
    ]);
    const vere = ["X = Beatrice; Y = Divina Commedia", "X = Eva; Y = Genesi", "X = Mirandolina; Y = La Locandiera"];
    const altre = domande[0]!.pdf.opzioni.slice(1);
    expect(altre).toHaveLength(3);
    expect(altre.some((o) => vere.includes(o))).toBe(false);
    expect(altre).toContainEqual(expect.stringMatching(/^X = Geppetto; Y = (?!Pinocchio)/));
  });

  it("relazioni: alternative che non sono sicuramente vere (o false)", () => {
    // A<B, B>C, D>B: D>A è sicura; B>A o D>C lo sarebbero anche, quindi non vanno.
    const vere = alternativeRelazioni("Se A<B, B>C, D>B, quale delle seguenti affermazioni è sicuramente vera?", "D>A", 7)!;
    expect(vere).toHaveLength(3);
    expect(vere).not.toContain("B>A");
    expect(vere).not.toContain("D>C");
    const false_ = alternativeRelazioni("Se B<C, D>B, A<B, quale delle seguenti affermazioni è sicuramente falsa?", "C<A", 7)!;
    expect(false_).not.toContain("A>C");
    expect(false_).not.toContain("B<A");
  });

  it("vero/falso, numeri e lettere", () => {
    const { domande } = domandeDallaTabella([
      riga(1, "Se due proposizioni sono entrambe «vere», qual è il risultato della congiunzione?", "Vera"),
      riga(2, "Quanto fa 12 per 3?", "36"),
      riga(3, "L, I, H, G, ?", "F"),
    ]);
    expect(domande[0]!.pdf.opzioni).toEqual(["Vera", "Falsa"]);
    expect(domande[1]!.pdf.opzioni.slice(1).every((o) => /^\d+$/.test(o) && Math.abs(Number(o) - 36) <= 2)).toBe(true);
    expect(domande[2]!.pdf.opzioni.slice(1)).not.toContain("F");
  });

  it("scarta le domande al negativo e quelle senza le alternative", () => {
    expect(motivoScarto("Non ha nulla a che fare con la parola alba")).toMatch(/negativo/);
    expect(motivoScarto("Non attinente alla parola salmo")).toMatch(/negativo/);
    expect(motivoScarto("Quale delle seguenti parole non ha lo stesso significato delle altre?")).toMatch(/alternative/);
    expect(motivoScarto("Non si può escludere che, se Luca non avesse risposto male, l'esame sarebbe stato superato.")).toBeUndefined();
    expect(motivoScarto("Quale tra i termini proposti completa correttamente la seguente proporzione? Arno : fiume = Everest : X")).toBeUndefined();
  });
});
