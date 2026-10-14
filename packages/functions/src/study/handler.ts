import { DeleteCommand, GetCommand, PutCommand, QueryCommand, ScanCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { batchGet, db, getProfilo, tables } from "@imieiconcorsi/core/db";
import {
  MATERIA_IDS,
  MATERIE,
  PREFISSO_BANCA_DATI,
  REGOLE_DEFAULT,
  SELEZIONI_BANCA,
  DOMANDE_MIN,
  SIMULAZIONE_MAX,
  SIMULAZIONE_STANDARD,
  concorsiDellaBanca,
  type BancaDati,
  type Concorso,
  type Domanda,
  type MateriaId,
  type ProgressoBanca,
  type Sessione,
} from "@imieiconcorsi/core/domain";
import { HttpError, notFound, service } from "@imieiconcorsi/core/http";
import {
  aggiornaProgresso,
  bitAcceso,
  candidatePerSelezione,
  conPreferita,
  idDomanda,
  numeriAccesi,
  numeroDomanda,
  type EsitoDomanda,
} from "@imieiconcorsi/core/progressi";
import { dispongiRisposte } from "@imieiconcorsi/core/risposte";
import { sortableId, timePrefix } from "@imieiconcorsi/core/ids";
import { z } from "zod";
import { calcolaEsito, mescola, pubblica, selezionaDomande } from "./logic";
import { consumaUso, statoUsi } from "./usi";

// Servizio "study": sessioni di studio e simulazioni, banche dati ufficiali (elenco,
// consultazione domanda per domanda, progressi), statistiche. Il punteggio si calcola qui alla
// consegna, mai nel browser. La scelta delle domande e il calcolo stanno in logic.ts (provati
// dai test); gli utilizzi settimanali del piano Free in usi.ts.

/** Minuti concessi per domanda nelle simulazioni (60 domande → 60 minuti). */
const MINUTI_PER_DOMANDA = 1;

/** Cosa chiede il sito per avviare una sessione. */
const NuovaSessione = z.object({
  tipo: z.enum(["studio", "simulazione"]),
  materie: z.array(z.enum(MATERIA_IDS)).min(1).optional(),
  concorsoId: z.string().optional(),
  /** Sessione sulle domande di una banca dati ufficiale */
  bancaDatiId: z.string().optional(),
  /** Banca dati: la giusta sempre per prima o mescolate (scelta dell'utente; assente = quella dell'admin) */
  ordineRisposte: z.enum(["prima", "mescolate"]).optional(),
  /** Banca dati: prima le domande mai fatte (predefinito), solo le sbagliate, o tutte */
  selezione: z.enum(SELEZIONI_BANCA).optional(),
  numero: z.number().int().min(DOMANDE_MIN).max(SIMULAZIONE_MAX).optional(),
});

/** Banche dati pubblicate, per la sezione Banche dati (poche righe: basta uno Scan). */
async function bancheDatiPubblicate() {
  const out: BancaDati[] = [];
  let ExclusiveStartKey: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new ScanCommand({
        TableName: tables.bancheDati,
        FilterExpression: "stato = :p",
        ExpressionAttributeValues: { ":p": "pubblicata" },
        ExclusiveStartKey,
      }),
    );
    out.push(...((res.Items ?? []) as BancaDati[]));
    ExclusiveStartKey = res.LastEvaluatedKey;
  } while (ExclusiveStartKey);
  return out;
}

/** Risposte date, nell'ordine delle domande (null = non risposta). */
const Consegna = z.object({
  risposte: z.array(z.number().int().min(0).max(9).nullable()).max(SIMULAZIONE_MAX),
});

/** Domande di una materia della banca statica, o di una banca dati ufficiale (bd#<id>). */
async function domandeDiMateria(materia: MateriaId | string) {
  const items: Domanda[] = [];
  let start: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new QueryCommand({
        TableName: tables.questions,
        KeyConditionExpression: "materia = :m",
        ExpressionAttributeValues: { ":m": materia },
        ExclusiveStartKey: start,
      }),
    );
    items.push(...((res.Items ?? []) as Domanda[]));
    start = res.LastEvaluatedKey;
  } while (start);
  return items;
}

/** Una sessione dell'utente; 404 se non esiste. */
async function getSessione(userId: string, id: string) {
  const res = await db.send(new GetCommand({ TableName: tables.attempts, Key: { userId, id } }));
  if (!res.Item) throw notFound("Sessione");
  return res.Item as Sessione;
}

/**
 * Le domande nell'ordine in cui sono state proposte; per le banche dati, con le risposte
 * nell'ordine scelto dall'utente. Lo stesso ordine vale per la vista e per il punteggio.
 */
async function domandeDellaSessione(s: Sessione) {
  const trovate = await batchGet<Domanda>(tables.questions, s.domande);
  const byKey = new Map(trovate.map((d) => [`${d.materia}/${d.id}`, d]));
  const ordine = s.bancaDati?.ordine;
  return s.domande
    .map((k) => byKey.get(`${k.materia}/${k.id}`))
    .filter((d): d is Domanda => !!d)
    .map((d) => (ordine && d.materia.startsWith(PREFISSO_BANCA_DATI) ? dispongiRisposte(d, ordine, `${d.materia}/${d.id}`) : d));
}

// ── Progressi nelle banche dati ──────────────────────────────────────────────

/** Progressi dell'utente in una banca; quelli di un'estrazione precedente non valgono più. */
async function progressoDi(userId: string, banca: Pick<BancaDati, "id" | "estrattaIl">) {
  const res = await db.send(new GetCommand({ TableName: tables.progressi, Key: { userId, bancaId: banca.id } }));
  const p = res.Item as ProgressoBanca | undefined;
  return p && p.estrattaIl === banca.estrattaIl ? p : undefined;
}

/** Progressi dell'utente in tutte le banche: righe piccole, senza le mappe di bit. */
async function progressiDellUtente(userId: string) {
  const res = await db.send(
    new QueryCommand({
      TableName: tables.progressi,
      KeyConditionExpression: "userId = :u",
      ExpressionAttributeValues: { ":u": userId },
      ProjectionExpression: "bancaId, nFatte, nSbagliate, nPreferite, estrattaIl",
    }),
  );
  return new Map(
    ((res.Items ?? []) as Pick<ProgressoBanca, "bancaId" | "nFatte" | "nSbagliate" | "nPreferite" | "estrattaIl">[]).map((p) => [p.bancaId, p]),
  );
}

/** La scrittura condizionata non è andata (la condizione era falsa). */
const condizioneFallita = (err: unknown) => err instanceof Error && err.name === "ConditionalCheckFailedException";

/** I campi della riga dei progressi che una modifica può cambiare. */
type CampiProgresso = Partial<Pick<ProgressoBanca, "fatte" | "sbagliate" | "nFatte" | "nSbagliate" | "preferite" | "nPreferite">>;

/**
 * Modifica la riga dei progressi di un utente in una banca dati: si legge, si cambia con
 * `cambia` (che riceve la riga attuale, o niente) e si riscrive con il numero di revisione;
 * se nel frattempo un'altra scrittura l'ha cambiata, si riprova (fino a 3 volte).
 * I campi che `cambia` non tocca restano com'erano (es. le preferite alla consegna).
 */
async function modificaProgresso(userId: string, bancaId: string, cambia: (base: ProgressoBanca | undefined) => CampiProgresso) {
  const banca = await db.send(new GetCommand({ TableName: tables.bancheDati, Key: { id: bancaId }, ProjectionExpression: "estrattaIl" }));
  const estrattaIl = banca.Item?.estrattaIl as string | undefined;
  for (let tentativo = 0; tentativo < 3; tentativo++) {
    const res = await db.send(new GetCommand({ TableName: tables.progressi, Key: { userId, bancaId } }));
    const prima = res.Item as ProgressoBanca | undefined;
    // Banca estratta di nuovo dall'admin: i numeri possono essere cambiati, si riparte da zero.
    const base = prima && prima.estrattaIl === estrattaIl ? prima : undefined;
    const vuota = new Uint8Array();
    const riga: ProgressoBanca = {
      userId,
      bancaId,
      fatte: base?.fatte ?? vuota,
      sbagliate: base?.sbagliate ?? vuota,
      nFatte: base?.nFatte ?? 0,
      nSbagliate: base?.nSbagliate ?? 0,
      ...(base?.preferite ? { preferite: base.preferite, nPreferite: base.nPreferite ?? 0 } : {}),
      ...cambia(base),
      estrattaIl,
      rev: (prima?.rev ?? 0) + 1,
      aggiornatoIl: new Date().toISOString(),
    };
    try {
      await db.send(
        new PutCommand({
          TableName: tables.progressi,
          Item: riga,
          ConditionExpression: prima ? "#rev = :rev" : "attribute_not_exists(userId)",
          ...(prima ? { ExpressionAttributeNames: { "#rev": "rev" }, ExpressionAttributeValues: { ":rev": prima.rev } } : {}),
        }),
      );
      return riga;
    } catch (err) {
      if (!condizioneFallita(err)) throw err;
    }
  }
  throw new Error("Progressi non salvati: troppe scritture contemporanee");
}

/** Segna le domande di una sessione consegnata come fatte (e sbagliate o no). */
async function salvaProgresso(userId: string, bancaId: string, esiti: EsitoDomanda[]) {
  if (!esiti.length) return;
  await modificaProgresso(userId, bancaId, (base) => aggiornaProgresso(base, esiti));
}

/** Ordine delle risposte di una banca dati: quello scelto dall'utente, altrimenti quello dell'admin. */
const ordineDi = (banca: BancaDati | undefined, scelto: "prima" | "mescolate" | undefined) =>
  scelto ?? (banca?.ordineRisposte === "pdf" ? "prima" : "mescolate");

/** Simulazioni (non da banca dati) iniziate da lunedì: il Free ne ha una a settimana. */
async function simulazioniDellaSettimana(userId: string) {
  const lunedi = new Date();
  lunedi.setUTCHours(0, 0, 0, 0);
  lunedi.setUTCDate(lunedi.getUTCDate() - ((lunedi.getUTCDay() + 6) % 7));
  const res = await db.send(
    new QueryCommand({
      TableName: tables.attempts,
      KeyConditionExpression: "userId = :u AND id >= :da",
      // Le simulazioni sulle banche dati hanno il loro limite (utilizzi): qui non contano.
      FilterExpression: "tipo = :t AND attribute_not_exists(bancaDati)",
      ExpressionAttributeValues: { ":u": userId, ":da": timePrefix(lunedi), ":t": "simulazione" },
      Select: "COUNT",
    }),
  );
  return res.Count ?? 0;
}

/** Cosa restituire al client: le soluzioni solo se è studio o se la prova è consegnata. */
async function vista(s: Sessione) {
  const domande = await domandeDellaSessione(s);
  const conSoluzioni = s.tipo === "studio" || s.stato === "consegnata";
  const { userId, ...resto } = s;
  return { ...resto, domande: await conPreferite(s, conSoluzioni ? domande : domande.map(pubblica)) };
}

/** Sessioni su una banca dati: ogni domanda dice se è tra le preferite (la stella accesa). */
async function conPreferite<T extends { materia: string; id: string }>(s: Sessione, domande: T[]): Promise<(T & { preferita?: boolean })[]> {
  if (!s.bancaDati) return domande;
  const banca = await db.send(new GetCommand({ TableName: tables.bancheDati, Key: { id: s.bancaDati.id }, ProjectionExpression: "id, estrattaIl" }));
  const progresso = await progressoDi(s.userId, { id: s.bancaDati.id, estrattaIl: banca.Item?.estrattaIl as string | undefined });
  const materia = `${PREFISSO_BANCA_DATI}${s.bancaDati.id}`;
  return domande.map((d) => (d.materia === materia ? { ...d, preferita: bitAcceso(progresso?.preferite, numeroDomanda(d.id)) } : d));
}

export const handler = service({
  /** Materie della banca statica con il numero di domande e il livello dichiarato dall'utente. */
  "GET /materie": async ({ userId }) => {
    const profilo = await getProfilo(userId);
    const conteggi = await Promise.all(
      MATERIE.map((m) =>
        db.send(
          new QueryCommand({
            TableName: tables.questions,
            KeyConditionExpression: "materia = :m",
            ExpressionAttributeValues: { ":m": m.id },
            Select: "COUNT",
          }),
        ),
      ),
    );
    // La versione della banca è la stessa per tutte le domande: basta leggerne una.
    const una = await db.send(
      new QueryCommand({
        TableName: tables.questions,
        KeyConditionExpression: "materia = :m",
        ExpressionAttributeValues: { ":m": MATERIE[0].id },
        ProjectionExpression: "versione",
        Limit: 1,
      }),
    );
    return {
      materie: MATERIE.map((m, i) => ({ ...m, domande: conteggi[i].Count ?? 0, livello: profilo?.livelli[m.id] })),
      versione: (una.Items?.[0]?.versione as string | undefined) ?? "v1",
    };
  },

  /** Catalogo per comparto, per tutti; il piano Free ha USI_BANCHE_DATI_FREE utilizzi a settimana (usi). */
  "GET /banche-dati": async (ctx) => {
    const [banche, usi, progressi] = await Promise.all([bancheDatiPubblicate(), statoUsi(ctx), progressiDellUtente(ctx.userId)]);
    return {
      usi,
      banche: banche
        .map((b) => {
          const p = progressi.get(b.id);
          return {
            b,
            progresso: p && p.estrattaIl === b.estrattaIl ? { fatte: p.nFatte, sbagliate: p.nSbagliate, preferite: p.nPreferite ?? 0 } : undefined,
          };
        })
        .map(({ b, progresso }) => ({
          id: b.id,
          titolo: b.titolo,
          comparto: b.comparto ?? "altro",
          anno: b.anno,
          materia: b.materia,
          domande: b.domande ?? 0,
          concorsoId: b.concorsoId,
          concorsoTitolo: b.concorsoTitolo,
          /** Tutti i concorsi collegati (la scheda li elenca con il link) */
          concorsi: concorsiDellaBanca(b),
          /** Domande già fatte e sbagliate l'ultima volta (assente = mai iniziata) */
          progresso,
        }))
        .sort((a, b) => (b.anno ?? 0) - (a.anno ?? 0) || a.titolo.localeCompare(b.titolo)),
    };
  },

  /**
   * Consultazione domanda per domanda, con la risposta giusta. ?da=<numero> va avanti,
   * ?fino=<numero> torna indietro; 20 domande per volta. ?ordine=prima|mescolate come le
   * risposte (la chiave è la stessa delle sessioni: stessa domanda, stesso ordine). Nel piano Free la prima
   * consultazione della settimana di questa banca dati costa un utilizzo.
   */
  "GET /banche-dati/{id}/domande": async (ctx) => {
    const res = await db.send(new GetCommand({ TableName: tables.bancheDati, Key: { id: ctx.params.id } }));
    const banca = res.Item as BancaDati | undefined;
    if (!banca || banca.stato !== "pubblicata") throw notFound("Banca dati");
    await consumaUso(ctx, banca.id);

    const PAGINA = 20;
    const indietro = ctx.query.fino !== undefined;
    const numero = Math.max(1, Number(indietro ? ctx.query.fino : (ctx.query.da ?? 1)) || 1);
    const materia = `${PREFISSO_BANCA_DATI}${banca.id}`;
    const progresso = await progressoDi(ctx.userId, banca);
    let trovate: Domanda[];
    let altre: boolean;
    if (ctx.query.preferite === "1") {
      // Solo le preferite: i loro numeri dalla mappa di bit, 20 per volta, poi le domande.
      const tutte = numeriAccesi(progresso?.preferite);
      const verso = indietro ? tutte.filter((n) => n <= numero).reverse() : tutte.filter((n) => n >= numero);
      const scelti = verso.slice(0, PAGINA);
      altre = verso.length > PAGINA;
      trovate = await batchGet<Domanda>(tables.questions, scelti.map((n) => ({ materia, id: idDomanda(n) })));
    } else {
      const out = await db.send(
        new QueryCommand({
          TableName: tables.questions,
          KeyConditionExpression: `materia = :m AND id ${indietro ? "<=" : ">="} :k`,
          ExpressionAttributeValues: { ":m": materia, ":k": idDomanda(numero) },
          ScanIndexForward: !indietro,
          Limit: PAGINA,
        }),
      );
      trovate = (out.Items ?? []) as Domanda[];
      altre = !!out.LastEvaluatedKey;
    }
    const q = ctx.query.ordine;
    const ordine = ordineDi(banca, q === "prima" || q === "mescolate" ? q : undefined);
    const domande = trovate
      .map((d) => dispongiRisposte(d, ordine, `${d.materia}/${d.id}`))
      .map(({ id, argomento, testo, opzioni, corretta }) => {
        const numero = numeroDomanda(id);
        // Già fatta in una sessione, e se l'ultima volta era sbagliata.
        return {
          numero,
          argomento,
          testo,
          opzioni,
          corretta,
          fatta: bitAcceso(progresso?.fatte, numero),
          sbagliata: bitAcceso(progresso?.sbagliate, numero),
          preferita: bitAcceso(progresso?.preferite, numero),
        };
      })
      .sort((a, b) => a.numero - b.numero);
    return {
      banca: {
        id: banca.id,
        titolo: banca.titolo,
        domande: banca.domande ?? 0,
        indiceSezioni: banca.indiceSezioni ?? [],
        mescolate: ordine === "mescolate",
        /** Il file ufficiale dava solo la risposta esatta: le alternative sono ricavate */
        alternativeRicavate: !!banca.alternativeRicavate,
        ordine,
      },
      domande,
      // C'è altro in quella direzione?
      altre,
      progresso: progresso ? { fatte: progresso.nFatte, sbagliate: progresso.nSbagliate, preferite: progresso.nPreferite ?? 0 } : undefined,
      usi: await statoUsi(ctx),
    };
  },

  /**
   * Avvia una sessione: su materie, sul concorso (le sue materie o la sua banca dati) o su
   * una banca dati scelta. Controlla i limiti del piano e salva le chiavi delle domande scelte.
   */
  "POST /sessioni": async (ctx) => {
    const input = ctx.body(NuovaSessione);
    const profilo = await getProfilo(ctx.userId);
    if (!profilo) throw new HttpError(409, "Profilo non ancora creato");
    const { limiti } = ctx;

    let materie = input.materie;
    /** Domande ufficiali: banca dati scelta dalla sezione Banche dati, o quella del concorso. */
    let bancaDati: string | undefined;
    let infoBanca: Sessione["bancaDati"];
    /** Banca della sessione, per scegliere le domande in base ai progressi */
    let bancaScelta: BancaDati | undefined;
    if (input.bancaDatiId) {
      const res = await db.send(new GetCommand({ TableName: tables.bancheDati, Key: { id: input.bancaDatiId } }));
      const banca = res.Item as BancaDati | undefined;
      if (!banca || banca.stato !== "pubblicata") throw notFound("Banca dati");

      bancaDati = `${PREFISSO_BANCA_DATI}${banca.id}`;
      const ordine = ordineDi(banca, input.ordineRisposte);
      infoBanca = { id: banca.id, titolo: banca.titolo, mescolate: ordine === "mescolate", ordine };
      materie ??= banca.materia ? [banca.materia] : [];
      bancaScelta = banca;
    }
    if (input.concorsoId) {
      const res = await db.send(new GetCommand({ TableName: tables.concorsi, Key: { id: input.concorsoId } }));
      if (!res.Item) throw notFound("Concorso");
      const concorso = res.Item as Concorso;
      materie ??= concorso.materie;
      if (!bancaDati && input.tipo === "simulazione" && limiti.bancheDati && concorso.bancaDatiId && !input.materie) {
        const res = await db.send(new GetCommand({ TableName: tables.bancheDati, Key: { id: concorso.bancaDatiId } }));
        const banca = res.Item as BancaDati | undefined;
        bancaDati = `${PREFISSO_BANCA_DATI}${concorso.bancaDatiId}`;
        const ordine = ordineDi(banca, input.ordineRisposte);
        infoBanca = { id: concorso.bancaDatiId, titolo: banca?.titolo ?? "Banca dati ufficiale", mescolate: ordine === "mescolate", ordine };
        bancaScelta = banca;
      }
    }
    if (!materie?.length && !bancaDati) throw new HttpError(400, "Indica le materie, un concorso o una banca dati");

    let numero: number;
    // Le sessioni sulle banche dati scelte dall'utente hanno il loro limite (utilizzi), non quello delle simulazioni.
    if (input.tipo === "simulazione") {
      if (limiti.simulazioniSettimana !== null && !input.bancaDatiId) {
        const fatte = await simulazioniDellaSettimana(ctx.userId);
        if (fatte >= limiti.simulazioniSettimana) {
          throw new HttpError(
            403,
            "Hai già usato la simulazione gratuita di questa settimana. Con Medium sono illimitate.",
            "LIMITE_PIANO",
          );
        }
      }
      numero = input.numero ?? SIMULAZIONE_STANDARD;
      // Oltre 60 domande si sceglie a mano, con Medium e Pro (fino a 100).
      if (numero > limiti.domandePerSimulazione) {
        throw new HttpError(
          403,
          `Nel piano Free le simulazioni arrivano a ${limiti.domandePerSimulazione} domande. Con Medium e Pro scegli tu quante, fino a ${SIMULAZIONE_MAX}.`,
          "LIMITE_PIANO",
        );
      }
    } else {
      numero = Math.min(input.numero ?? 10, limiti.domandePerSessioneStudio);
    }

    // Piano Free: un utilizzo dei USI_BANCHE_DATI_FREE settimanali, dopo gli altri controlli.
    if (input.bancaDatiId) await consumaUso(ctx);

    let domande: Domanda[];
    if (bancaDati) {
      // Banca dati: prima le domande scelte dalla selezione (di solito le mai fatte), poi le altre.
      const [tutte, progresso] = await Promise.all([domandeDiMateria(bancaDati), bancaScelta ? progressoDi(ctx.userId, bancaScelta) : undefined]);
      const selezione = input.selezione ?? "nuove";
      const { prima, poi } = candidatePerSelezione(tutte, progresso, selezione);
      if (selezione === "sbagliate" && !prima.length) {
        throw new HttpError(409, "Non hai domande sbagliate da ripassare in questa banca dati: ottimo!", "NESSUNA_DOMANDA");
      }
      if (selezione === "preferite" && !prima.length) {
        throw new HttpError(409, "Non hai ancora domande preferite in questa banca dati: salvale con la stella.", "NESSUNA_DOMANDA");
      }
      const chiave = bancaDati as MateriaId;
      const scelte = selezionaDomande(new Map([[chiave, prima]]), numero, profilo.livelli);
      domande = scelte.length < numero && poi.length ? mescola([...scelte, ...selezionaDomande(new Map([[chiave, poi]]), numero - scelte.length, profilo.livelli)]) : scelte;
    } else {
      const fonti = materie ?? [];
      const perMateria = new Map(await Promise.all(fonti.map(async (m) => [m, await domandeDiMateria(m)] as const)));
      domande = selezionaDomande(perMateria, numero, profilo.livelli);
    }
    if (!domande.length) throw new HttpError(409, "Non ci sono ancora domande per queste materie", "NESSUNA_DOMANDA");

    const now = new Date();
    const sessione: Sessione = {
      userId: ctx.userId,
      id: sortableId(now),
      tipo: input.tipo,
      concorsoId: input.concorsoId,
      materie: materie ?? [],
      ...(infoBanca ? { bancaDati: infoBanca } : {}),
      domande: domande.map(({ materia, id }) => ({ materia, id })),
      stato: "in-corso",
      regole: REGOLE_DEFAULT,
      creataIl: now.toISOString(),
      scadeIl:
        input.tipo === "simulazione"
          ? new Date(now.getTime() + domande.length * MINUTI_PER_DOMANDA * 60_000).toISOString()
          : undefined,
    };
    await db.send(new PutCommand({ TableName: tables.attempts, Item: sessione }));
    return vista(sessione);
  },

  /** Una sessione (anche per riprenderla): soluzioni solo se è studio o già consegnata. */
  "GET /sessioni/{id}": async ({ userId, params }) => vista(await getSessione(userId, params.id!)),

  /** Consegna: calcola il punteggio, chiude la sessione e aggiorna i progressi della banca dati. */
  "POST /sessioni/{id}/consegna": async (ctx) => {
    const { risposte } = ctx.body(Consegna);
    const sessione = await getSessione(ctx.userId, ctx.params.id!);
    if (sessione.stato === "consegnata") throw new HttpError(409, "Sessione già consegnata");

    // Il timer è lato client: allo scadere il browser consegna da solo.
    const now = new Date();
    const domande = await domandeDellaSessione(sessione);
    const esito = calcolaEsito(domande, risposte, sessione.regole, sessione.tipo);
    const aggiornata: Sessione = { ...sessione, stato: "consegnata", consegnataIl: now.toISOString(), risposte, esito };

    await db.send(
      new UpdateCommand({
        TableName: tables.attempts,
        Key: { userId: ctx.userId, id: sessione.id },
        UpdateExpression: "SET stato = :s, consegnataIl = :c, risposte = :r, esito = :e",
        ConditionExpression: "stato = :inCorso",
        ExpressionAttributeValues: {
          ":s": "consegnata",
          ":c": aggiornata.consegnataIl,
          ":r": risposte,
          ":e": esito,
          ":inCorso": "in-corso",
        },
      }),
    );
    // Banca dati: le domande risposte diventano "fatte" (e "sbagliate" se l'ultima risposta era sbagliata).
    if (sessione.bancaDati) {
      const materia = `${PREFISSO_BANCA_DATI}${sessione.bancaDati.id}`;
      const esiti = domande.flatMap((d, i) =>
        d.materia === materia && risposte[i] != null ? [{ numero: numeroDomanda(d.id), giusta: risposte[i] === d.corretta }] : [],
      );
      // La consegna è già salvata: un problema qui non deve farla fallire.
      await salvaProgresso(ctx.userId, sessione.bancaDati.id, esiti).catch((err) => console.error("Progressi della banca dati non salvati", err));
    }
    const { userId, ...resto } = aggiornata;
    return { ...resto, domande: await conPreferite(sessione, domande) };
  },

  /** Salva (o toglie) una domanda della banca dati tra le preferite, per ritrovarla dopo. */
  "PUT /me/progressi/{bancaId}/preferite/{numero}": async (ctx) => {
    const { preferita } = ctx.body(z.object({ preferita: z.boolean() }));
    const numero = Number(ctx.params.numero);
    if (!Number.isInteger(numero) || numero < 1 || numero > 99_999) throw new HttpError(400, "Numero di domanda non valido");
    const banca = await db.send(new GetCommand({ TableName: tables.bancheDati, Key: { id: ctx.params.bancaId }, ProjectionExpression: "id, stato" }));
    if (banca.Item?.stato !== "pubblicata") throw notFound("Banca dati");
    const riga = await modificaProgresso(ctx.userId, ctx.params.bancaId!, (base) => conPreferita(base, numero, preferita));
    return { preferita, preferite: riga.nPreferite ?? 0 };
  },

  /** Ricomincia da capo una banca dati: si dimenticano le domande fatte e sbagliate (le preferite restano). */
  "DELETE /me/progressi/{bancaId}": async (ctx) => {
    const chiave = { userId: ctx.userId, bancaId: ctx.params.bancaId };
    const res = await db.send(new GetCommand({ TableName: tables.progressi, Key: chiave, ProjectionExpression: "nPreferite" }));
    if (res.Item?.nPreferite) {
      // Ci sono preferite: si azzerano solo fatte e sbagliate.
      const vuota = new Uint8Array();
      await modificaProgresso(ctx.userId, ctx.params.bancaId!, () => ({ fatte: vuota, sbagliate: vuota, nFatte: 0, nSbagliate: 0 }));
    } else {
      await db.send(new DeleteCommand({ TableName: tables.progressi, Key: chiave }));
    }
    return { ok: true };
  },

  /** Statistiche della dashboard: risposte per materia, andamento delle simulazioni, ultime sessioni. */
  "GET /me/statistiche": async ({ userId }) => {
    const res = await db.send(
      new QueryCommand({
        TableName: tables.attempts,
        KeyConditionExpression: "userId = :u",
        ExpressionAttributeValues: { ":u": userId },
        ScanIndexForward: false,
        Limit: 200,
      }),
    );
    const sessioni = ((res.Items ?? []) as Sessione[]).filter((s) => s.stato === "consegnata" && s.esito);

    // Le domande delle banche dati hanno materia "bd#<id>": vanno a parte, con il titolo della banca.
    const materie = new Map<MateriaId, { corrette: number; totale: number }>();
    const banche = new Map<string, { titolo: string; corrette: number; totale: number }>();
    for (const s of sessioni) {
      for (const m of s.esito!.perMateria) {
        if (m.materia.startsWith(PREFISSO_BANCA_DATI)) {
          const bancaId = m.materia.slice(PREFISSO_BANCA_DATI.length);
          const acc = banche.get(bancaId) ?? { titolo: s.bancaDati?.titolo ?? "Banca dati ufficiale", corrette: 0, totale: 0 };
          acc.corrette += m.corrette;
          acc.totale += m.totale;
          banche.set(bancaId, acc);
          continue;
        }
        const acc = materie.get(m.materia) ?? { corrette: 0, totale: 0 };
        acc.corrette += m.corrette;
        acc.totale += m.totale;
        materie.set(m.materia, acc);
      }
    }
    // Percentuale di risposte giuste, arrotondata (0 senza risposte).
    const percentuale = (v: { corrette: number; totale: number }) => (v.totale ? Math.round((v.corrette / v.totale) * 100) : 0);

    return {
      domandeRisposte: [...materie.values(), ...banche.values()].reduce((n, m) => n + m.totale, 0),
      /** Risposte giuste in tutte le sessioni (materie e banche dati) */
      risposteCorrette: [...materie.values(), ...banche.values()].reduce((n, m) => n + m.corrette, 0),
      perMateria: [...materie].filter(([, v]) => v.totale > 0).map(([materia, v]) => ({ materia, ...v, percentuale: percentuale(v) })),
      perBancaDati: [...banche].filter(([, v]) => v.totale > 0).map(([bancaId, v]) => ({ bancaId, ...v, percentuale: percentuale(v) })),
      simulazioni: sessioni
        .filter((s) => s.tipo === "simulazione")
        .slice(0, 20)
        .reverse()
        .map((s) => ({ id: s.id, data: s.consegnataIl!, percentuale: s.esito!.percentuale, superata: s.esito!.superata })),
      recenti: sessioni.slice(0, 5).map((s) => ({
        id: s.id,
        tipo: s.tipo,
        materie: s.materie,
        bancaDati: s.bancaDati?.titolo,
        concorsoId: s.concorsoId,
        data: s.consegnataIl!,
        percentuale: s.esito!.percentuale,
        // Tempo impiegato (le simulazioni hanno un limite; lo studio no).
        durataMs: Date.parse(s.consegnataIl!) - Date.parse(s.creataIl),
      })),
    };
  },
});
