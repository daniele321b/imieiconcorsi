import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";
import { GetCommand, QueryCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { batchGet, db, getProfilo, tables } from "@imieiconcorsi/core/db";
import {
  AI_AL_MINUTO,
  COSTI_AI,
  DOMANDE_ALLENAMENTO_AI,
  TETTO_AI_MESE_USD,
  TETTO_AI_UTENTE_USD,
  type Domanda,
  type MateriaId,
  type Sessione,
} from "@imieiconcorsi/core/domain";
import { avvisaAdmin } from "@imieiconcorsi/core/email";
import { env } from "@imieiconcorsi/core/env";
import { HttpError, service, type Ctx } from "@imieiconcorsi/core/http";
import { randomUUID } from "node:crypto";
import {
  campione,
  domandeValide,
  eFuoriTema,
  gettoniUsati,
  meseCorrente,
  MESSAGGIO_FUORI_TEMA,
  messaggiTutor,
  minutoCorrente,
  promptAllenamento,
  puntiDeboli,
  RichiestaAllenamento,
  RichiestaTutor,
  rinnovoGettoni,
  risposteDellaMateria,
  SISTEMA_AUTORE,
  SISTEMA_TUTOR,
  sogliaSuperata,
  spesaMicroUsd,
  STRUMENTO_DOMANDE,
  type UsoToken,
} from "./logic";

// Funzioni AI del piano Pro: tutor e allenamenti con domande generate.
// Claude su Amazon Bedrock (profilo d'inferenza EU: i dati restano in Europa), pagato a
// token sulla bolletta AWS. Le protezioni contro spese indesiderate, in ordine:
// 1. gettoni: GETTONI_AI_PRO al mese per utente, scalati prima della chiamata;
// 2. tetto di spesa per utente: token contati sul profilo, stop oltre AI_TETTO_UTENTE_USD al mese;
// 3. ritmo: al massimo AI_AL_MINUTO richieste al minuto per utente;
// 4. tetto della piattaforma: spesa del mese di tutti (tabella contatori), stop oltre
//    AI_TETTO_MENSILE_USD con email all'admin all'80% e al 100%;
// 5. tema: il tutor risponde solo sullo studio, altrimenti dà il segnale FUORI_TEMA (gettone restituito);
// 6. token massimi per risposta e messaggi della chat tagliati (MAX_TOKEN_*, MAX_MESSAGGI).

const client = new AnthropicBedrock({ awsRegion: process.env.AWS_REGION, timeout: 25_000, maxRetries: 1 });
/** es. eu.anthropic.claude-haiku-4-5-20251001-v1:0 (variabile ai_model in Terraform) */
const modello = () => env("AI_MODEL");

const MAX_TOKEN_TUTOR = 800;
const MAX_TOKEN_ALLENAMENTO = 3000;
/** Sessioni consegnate da cui si cercano gli errori per l'allenamento. */
const SESSIONI_RECENTI = 30;
/** Domande date al modello come materiale per scrivere quelle nuove. */
const MATERIALE = 8;

/** Data in italiano, es. "1 novembre". */
const dataIt = (iso: string) => new Intl.DateTimeFormat("it-IT", { day: "numeric", month: "long" }).format(new Date(iso));

/** Errore 429 quando l'utente ha finito i crediti AI del mese. */
const gettoniFiniti = (ctx: Ctx) =>
  new HttpError(
    429,
    `Hai usato tutti i ${ctx.limiti.gettoniAi} crediti AI di questo mese: ripartono il ${dataIt(rinnovoGettoni())}.`,
    "GETTONI_FINITI",
  );

/** Errore 429 quando la piattaforma ha raggiunto il tetto di spesa AI del mese. */
const spesaFinita = () =>
  new HttpError(
    429,
    `Hai raggiunto il limite di utilizzo del tutor AI per questo mese: torna disponibile il ${dataIt(rinnovoGettoni())}.`,
    "GETTONI_FINITI",
  );

/** Tetti di spesa in milionesimi di dollaro: da Terraform, altrimenti i valori di riserva del dominio. */
const tettoUtente = () => Number(process.env.AI_TETTO_UTENTE_USD || TETTO_AI_UTENTE_USD) * 1e6;
const tettoMese = () => Number(process.env.AI_TETTO_MENSILE_USD || TETTO_AI_MESE_USD) * 1e6;
/** Riga della tabella contatori con la spesa AI di un mese. */
const chiaveContatore = (mese: string) => `ai#${mese}`;

/** Il tutor AI è solo per chi ha il piano Pro (o admin): altrimenti 403. */
function richiediAi(ctx: Ctx) {
  if (!ctx.limiti.ai) throw new HttpError(403, "Il tutor AI è incluso nel piano Pro.", "LIMITE_PIANO");
}

/** La scrittura condizionata non è andata (la condizione era falsa). */
const condizioneFallita = (err: unknown) => err instanceof Error && err.name === "ConditionalCheckFailedException";

/**
 * Spesa AI del mese di tutta la piattaforma (tabella contatori). Si rilegge al massimo ogni
 * 30 secondi: la Lambda resta accesa tra una richiesta e l'altra e la tiene in memoria.
 */
let spesaPiattaforma: { mese: string; micro: number; lettaIl: number } | undefined;

/** Tetto mensile della piattaforma raggiunto: l'AI va in pausa per tutti fino al mese dopo. */
async function controllaTettoPiattaforma() {
  const mese = meseCorrente();
  if (!spesaPiattaforma || spesaPiattaforma.mese !== mese || Date.now() - spesaPiattaforma.lettaIl > 30_000) {
    const res = await db.send(new GetCommand({ TableName: tables.contatori, Key: { id: chiaveContatore(mese) } }));
    spesaPiattaforma = { mese, micro: Number(res.Item?.spesaMicroUsd ?? 0), lettaIl: Date.now() };
  }
  if (spesaPiattaforma.micro >= tettoMese()) {
    throw new HttpError(503, "Il tutor AI è in pausa per qualche tempo: riprova più tardi. Questa domanda non ti è stata conteggiata.", "AI_IN_PAUSA");
  }
}

/** Al massimo AI_AL_MINUTO richieste al minuto per utente (contro script e clic a raffica). */
async function controllaRitmo(ctx: Ctx) {
  const minuto = minutoCorrente();
  try {
    // Stesso minuto: si conta, se c'è posto.
    await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: ctx.userId },
        UpdateExpression: "SET aiNelMinuto = aiNelMinuto + :uno",
        ConditionExpression: "aiMinuto = :min AND aiNelMinuto < :max",
        ExpressionAttributeValues: { ":uno": 1, ":min": minuto, ":max": AI_AL_MINUTO },
      }),
    );
    return;
  } catch (err) {
    if (!condizioneFallita(err)) throw err;
  }
  try {
    // Minuto nuovo: si riparte da uno.
    await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: ctx.userId },
        UpdateExpression: "SET aiMinuto = :min, aiNelMinuto = :uno",
        ConditionExpression: "attribute_exists(userId) AND (attribute_not_exists(aiMinuto) OR aiMinuto <> :min)",
        ExpressionAttributeValues: { ":uno": 1, ":min": minuto },
      }),
    );
  } catch (err) {
    if (condizioneFallita(err)) throw new HttpError(429, "Stai facendo molte domande di fila: aspetta qualche secondo e riprova.", "TROPPO_VELOCE");
    throw err;
  }
}

/** Scala `costo` gettoni dal mese corrente; errore se non bastano o se l'utente ha raggiunto il tetto di spesa. */
async function riservaGettoni(ctx: Ctx, costo: number) {
  const mese = meseCorrente();
  const massimo = ctx.limiti.gettoniAi;
  if (costo > massimo) throw gettoniFiniti(ctx);
  try {
    // Stesso mese: si aggiunge, se c'è posto e la spesa del mese è sotto il tetto.
    await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: ctx.userId },
        UpdateExpression: "SET ai.usati = ai.usati + :c",
        ConditionExpression: "ai.mese = :m AND ai.usati <= :soglia AND (attribute_not_exists(ai.spesaMicroUsd) OR ai.spesaMicroUsd < :tetto)",
        ExpressionAttributeValues: { ":c": costo, ":m": mese, ":soglia": massimo - costo, ":tetto": tettoUtente() },
      }),
    );
    return;
  } catch (err) {
    if (!condizioneFallita(err)) throw err;
  }
  try {
    // Primo uso del mese (o di sempre): si riparte da zero.
    await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: ctx.userId },
        UpdateExpression: "SET ai = :ai",
        ConditionExpression: "attribute_exists(userId) AND (attribute_not_exists(ai) OR ai.mese <> :m)",
        ExpressionAttributeValues: { ":ai": { mese, usati: costo, tokenIngresso: 0, tokenUscita: 0, spesaMicroUsd: 0 }, ":m": mese },
      }),
    );
  } catch (err) {
    if (!condizioneFallita(err)) throw err;
    // Stesso mese e niente posto: per i gettoni finiti o per il tetto di spesa?
    const ai = (await getProfilo(ctx.userId))?.ai;
    throw ai?.mese === mese && (ai.spesaMicroUsd ?? 0) >= tettoUtente() ? spesaFinita() : gettoniFiniti(ctx);
  }
}

/** Ridà i crediti scalati per una richiesta AI non riuscita (solo nello stesso mese). */
async function restituisciGettoni(ctx: Ctx, costo: number) {
  await db
    .send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: ctx.userId },
        UpdateExpression: "SET ai.usati = ai.usati - :c",
        ConditionExpression: "ai.mese = :m AND ai.usati >= :c",
        ExpressionAttributeValues: { ":c": costo, ":m": meseCorrente() },
      }),
    )
    .catch((err) => console.error("Gettoni non restituiti", err));
}

/**
 * Token e spesa di una chiamata: sul profilo dell'utente (tetto per utente) e sul contatore
 * della piattaforma (tetto mensile). Superato l'80% o il 100% del tetto mensile, l'admin
 * riceve un'email (una volta per soglia: il contatore si aggiorna in modo atomico).
 */
async function registraConsumo(ctx: Ctx, uso: UsoToken) {
  const mese = meseCorrente();
  const spesa = spesaMicroUsd(uso);
  const valori = { ":i": uso.input_tokens, ":o": uso.output_tokens, ":s": spesa };
  const utente = db
    .send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: ctx.userId },
        UpdateExpression:
          "SET ai.tokenIngresso = if_not_exists(ai.tokenIngresso, :zero) + :i, ai.tokenUscita = if_not_exists(ai.tokenUscita, :zero) + :o, ai.spesaMicroUsd = if_not_exists(ai.spesaMicroUsd, :zero) + :s",
        ConditionExpression: "ai.mese = :m",
        ExpressionAttributeValues: { ...valori, ":zero": 0, ":m": mese },
      }),
    )
    .catch((err) => console.error("Consumo AI dell'utente non registrato", err));

  const piattaforma = db
    .send(
      new UpdateCommand({
        TableName: tables.contatori,
        Key: { id: chiaveContatore(mese) },
        UpdateExpression: "ADD tokenIngresso :i, tokenUscita :o, spesaMicroUsd :s, chiamate :uno",
        ExpressionAttributeValues: { ...valori, ":uno": 1 },
        ReturnValues: "UPDATED_NEW",
      }),
    )
    .then(async (res) => {
      const dopo = Number(res.Attributes?.spesaMicroUsd ?? 0);
      if (spesaPiattaforma?.mese === mese) spesaPiattaforma.micro = dopo;
      const soglia = sogliaSuperata(dopo - spesa, dopo, tettoMese());
      if (!soglia) return;
      // Milionesimi di dollaro in testo, es. "12.50 $".
      const usd = (n: number) => `${(n / 1e6).toFixed(2)} $`;
      await avvisaAdmin(
        soglia >= 1 ? "Tutor AI in pausa: raggiunto il tetto di spesa del mese" : "Tutor AI: spesa del mese all'80% del tetto",
        [
          `Spesa AI stimata nel mese ${mese}: ${usd(dopo)} su un tetto di ${usd(tettoMese())}.`,
          soglia >= 1
            ? "Il tutor e gli allenamenti AI sono in pausa per tutti fino al mese prossimo."
            : "Al 100% il tutor e gli allenamenti AI vanno in pausa per tutti fino al mese prossimo.",
          "Per alzare il tetto: variabile ai_tetto_mensile_usd in terraform.tfvars, poi scripts/deploy.sh infra.",
        ].join("\n"),
      );
    })
    .catch((err) => console.error("Consumo AI della piattaforma non registrato", err));

  await Promise.all([utente, piattaforma]);
}

/** Cosa restituisce la chiamata al modello: il risultato (assente = non valido) e i token usati. */
interface EsitoChiamata<T> {
  risultato?: T;
  uso: UsoToken;
  /** Richiesta fuori tema: niente risultato, il gettone torna indietro */
  fuoriTema?: boolean;
}

/**
 * Chiamata al modello con tutti i controlli: tetto della piattaforma, richieste al minuto,
 * gettoni e tetto di spesa dell'utente. I gettoni si scalano prima (così due richieste insieme
 * non sforano) e tornano indietro se la chiamata fallisce, se la risposta non è valida o se la
 * richiesta è fuori tema. I token consumati si contano sempre.
 */
async function chiamaAi<T>(ctx: Ctx, costo: number, chiamata: () => Promise<EsitoChiamata<T>>): Promise<{ risultato: T } | { fuoriTema: true }> {
  await controllaTettoPiattaforma();
  await controllaRitmo(ctx);
  await riservaGettoni(ctx, costo);
  let esito: EsitoChiamata<T>;
  try {
    esito = await chiamata();
  } catch (err) {
    await restituisciGettoni(ctx, costo);
    if (err instanceof HttpError) throw err;
    // Niente contenuti nei log: solo il tipo di errore.
    console.error("Chiamata AI non riuscita", err instanceof AnthropicBedrock.APIError ? `${err.status} ${err.name}` : err);
    throw new HttpError(503, "Il tutor AI non risponde in questo momento: riprova tra poco. Questa domanda non ti è stata conteggiata.", "AI_NON_DISPONIBILE");
  }
  await registraConsumo(ctx, esito.uso);
  if (esito.fuoriTema) {
    await restituisciGettoni(ctx, costo);
    return { fuoriTema: true };
  }
  if (esito.risultato === undefined) {
    await restituisciGettoni(ctx, costo);
    throw new HttpError(503, "Il tutor AI non ha dato una risposta valida: riprova. Questa domanda non ti è stata conteggiata.", "AI_NON_DISPONIBILE");
  }
  return { risultato: esito.risultato };
}

/** Crediti AI del mese: totali, usati, restanti e data del rinnovo. */
async function statoGettoni(ctx: Ctx) {
  const profilo = await getProfilo(ctx.userId);
  const usati = gettoniUsati(profilo?.ai);
  return { totale: ctx.limiti.gettoniAi, usati, restanti: Math.max(0, ctx.limiti.gettoniAi - usati), rinnovoIl: rinnovoGettoni() };
}

/** Ultime sessioni consegnate dell'utente, per i suggerimenti del tutor. */
async function sessioniConsegnate(userId: string, quante: number) {
  const res = await db.send(
    new QueryCommand({
      TableName: tables.attempts,
      KeyConditionExpression: "userId = :u",
      ExpressionAttributeValues: { ":u": userId },
      ScanIndexForward: false,
      Limit: quante,
    }),
  );
  return ((res.Items ?? []) as Sessione[]).filter((s) => s.stato === "consegnata" && s.esito);
}

/** Materiale per l'allenamento: prima le domande sbagliate di recente, poi altre della stessa materia. */
async function materiale(userId: string, materia: MateriaId) {
  const sessioni = await sessioniConsegnate(userId, SESSIONI_RECENTI);
  const risposte = risposteDellaMateria(sessioni, materia).slice(0, 100);
  const viste = await batchGet<Domanda>(tables.questions, risposte.map(({ materia, id }) => ({ materia, id })));
  const perChiave = new Map(viste.map((d) => [d.id, d]));
  const sbagliate = risposte
    .filter((r) => {
      const d = perChiave.get(r.id);
      return d && r.risposta !== d.corretta;
    })
    .map((r) => perChiave.get(r.id)!)
    .slice(0, MATERIALE);
  if (sbagliate.length >= MATERIALE) return sbagliate;

  // Pochi errori: si completa con domande della banca, meglio se degli stessi argomenti.
  const res = await db.send(
    new QueryCommand({
      TableName: tables.questions,
      KeyConditionExpression: "materia = :m",
      ExpressionAttributeValues: { ":m": materia },
      Limit: 300,
    }),
  );
  const giaPrese = new Set(sbagliate.map((d) => d.id));
  const argomenti = new Set(sbagliate.map((d) => d.argomento));
  const altre = ((res.Items ?? []) as Domanda[]).filter((d) => !giaPrese.has(d.id));
  const stessiArgomenti = altre.filter((d) => argomenti.has(d.argomento));
  const resto = altre.filter((d) => !argomenti.has(d.argomento));
  const mancano = MATERIALE - sbagliate.length;
  const scelte = campione(stessiArgomenti, mancano);
  return [...sbagliate, ...scelte, ...campione(resto, mancano - scelte.length)];
}

export const handler = service({
  /** Gettoni del mese e materie più deboli (per proporre l'allenamento). */
  "GET /ai/stato": async (ctx) => {
    const [gettoni, sessioni] = await Promise.all([statoGettoni(ctx), sessioniConsegnate(ctx.userId, 200)]);
    return { attivo: ctx.limiti.ai, gettoni, puntiDeboli: puntiDeboli(sessioni), costi: COSTI_AI };
  },

  /** Risposta del tutor alla conversazione; fuori tema = avviso, gettone restituito. */
  "POST /ai/tutor": async (ctx) => {
    richiediAi(ctx);
    const input = ctx.body(RichiestaTutor);
    const esito = await chiamaAi(ctx, COSTI_AI.tutor, async () => {
      const msg = await client.messages.create({
        model: modello(),
        max_tokens: MAX_TOKEN_TUTOR,
        system: SISTEMA_TUTOR,
        messages: messaggiTutor(input),
      });
      const testo = msg.content
        .flatMap((b) => (b.type === "text" ? [b.text] : []))
        .join("\n")
        .trim();
      const fuoriTema = eFuoriTema(testo);
      console.log(`Tutor: ${msg.usage.input_tokens} token in, ${msg.usage.output_tokens} out${fuoriTema ? ", fuori tema" : ""}${testo ? "" : `, vuota (${msg.stop_reason})`}`);
      return { risultato: testo || undefined, uso: msg.usage, fuoriTema };
    });
    return "fuoriTema" in esito
      ? { risposta: MESSAGGIO_FUORI_TEMA, fuoriTema: true, gettoni: await statoGettoni(ctx) }
      : { risposta: esito.risultato, gettoni: await statoGettoni(ctx) };
  },

  /** Domande nuove sui punti deboli. Non si salvano: si fanno nella pagina e basta. */
  "POST /ai/allenamento": async (ctx) => {
    richiediAi(ctx);
    const input = ctx.body(RichiestaAllenamento);
    let materia = input.materia;
    if (!materia) {
      const deboli = puntiDeboli(await sessioniConsegnate(ctx.userId, 200));
      materia = deboli[0]?.materia;
      if (!materia) throw new HttpError(400, "Scegli una materia: non hai ancora abbastanza risposte per capire i tuoi punti deboli.");
    }
    const base = await materiale(ctx.userId, materia);
    if (!base.length) throw new HttpError(409, "Non ci sono ancora domande in questa materia", "NESSUNA_DOMANDA");

    const esito = await chiamaAi(ctx, COSTI_AI.allenamento, async () => {
      const msg = await client.messages.create({
        model: modello(),
        max_tokens: MAX_TOKEN_ALLENAMENTO,
        system: SISTEMA_AUTORE,
        tools: [STRUMENTO_DOMANDE],
        tool_choice: { type: "auto" },
        messages: [{ role: "user", content: promptAllenamento(materia, base, DOMANDE_ALLENAMENTO_AI) }],
      });
      const uso = msg.content.find((b) => b.type === "tool_use");
      const valide = uso ? domandeValide(uso.input) : [];
      console.log(`Allenamento: ${msg.usage.input_tokens} token in, ${msg.usage.output_tokens} out, ${valide.length} domande valide (${msg.stop_reason})`);
      return { risultato: valide.length ? valide : undefined, uso: msg.usage };
    });
    // L'allenamento non ha testo libero dell'utente: non può essere fuori tema.
    const domande = "risultato" in esito ? esito.risultato : [];
    return {
      materia,
      domande: domande.map((d) => ({ id: randomUUID(), materia, ...d })),
      gettoni: await statoGettoni(ctx),
    };
  },
});
