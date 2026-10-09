import type { Domanda, DomandaPubblica, Esito, MateriaId, Regole } from "@imieiconcorsi/core/domain";

// Parte pura del servizio studio (senza AWS, provata dai test): scelta delle domande di una
// sessione, mescolamento, versione senza soluzioni e calcolo del punteggio.

/**
 * Sceglie `numero` domande ripartite il più possibile in modo uniforme tra le materie.
 * Dentro ogni materia preferisce quelle vicine al livello dichiarato dall'utente.
 */
export function selezionaDomande(
  perMateria: Map<MateriaId, Domanda[]>,
  numero: number,
  livelli: Partial<Record<MateriaId, number>>,
  random: () => number = Math.random,
): Domanda[] {
  const code = [...perMateria].map(([materia, domande]) => {
    const livello = livelli[materia] ?? 3;
    // Rumore casuale perché due sessioni consecutive non siano identiche.
    return domande
      .map((d) => ({ d, peso: Math.abs(d.livello - livello) + random() * 2 }))
      .sort((a, b) => a.peso - b.peso)
      .map((x) => x.d);
  });

  const scelte: Domanda[] = [];
  // Una domanda per materia a giro finché si raggiunge il numero o finiscono le domande.
  while (scelte.length < numero && code.some((c) => c.length)) {
    for (const coda of code) {
      const d = coda.shift();
      if (d) scelte.push(d);
      if (scelte.length === numero) break;
    }
  }
  return mescola(scelte, random);
}

/** Copia della lista in ordine casuale (Fisher-Yates). */
export function mescola<T>(items: T[], random: () => number = Math.random): T[] {
  const out = [...items];
  for (let i = out.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

/** La domanda senza soluzione, spiegazione e fonte: è quella che vede chi fa una simulazione. */
export const pubblica = ({ corretta, spiegazione, fonte, ...d }: Domanda): DomandaPubblica => d;

/** Punteggio di una sessione consegnata: giuste, sbagliate, non date, percentuale e per materia. */
export function calcolaEsito(domande: Domanda[], risposte: (number | null)[], regole: Regole): Esito {
  let corrette = 0;
  let errate = 0;
  let omesse = 0;
  const perMateria = new Map<MateriaId, { corrette: number; totale: number }>();

  domande.forEach((d, i) => {
    const r = risposte[i] ?? null;
    const m = perMateria.get(d.materia) ?? { corrette: 0, totale: 0 };
    m.totale++;
    if (r === null) omesse++;
    else if (r === d.corretta) {
      corrette++;
      m.corrette++;
    } else errate++;
    perMateria.set(d.materia, m);
  });

  const massimo = domande.length * regole.corretta;
  const punteggio = round2(corrette * regole.corretta + errate * regole.errata + omesse * regole.omessa);
  const percentuale = massimo ? round2((Math.max(punteggio, 0) / massimo) * 100) : 0;

  return {
    corrette,
    errate,
    omesse,
    punteggio,
    massimo,
    percentuale,
    superata: massimo > 0 && punteggio >= massimo * regole.soglia,
    perMateria: [...perMateria].map(([materia, v]) => ({ materia, ...v })),
  };
}

const round2 = (n: number) => Math.round(n * 100) / 100;
