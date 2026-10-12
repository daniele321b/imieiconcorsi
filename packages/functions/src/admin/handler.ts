import {
  AdminDisableUserCommand,
  AdminEnableUserCommand,
  AdminGetUserCommand,
  DescribeUserPoolCommand,
  ListUsersCommand,
  type UserType,
} from "@aws-sdk/client-cognito-identity-provider";
import { randomUUID } from "node:crypto";
import { CopyObjectCommand, DeleteObjectsCommand, GetObjectCommand, PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { BatchWriteCommand, DeleteCommand, GetCommand, PutCommand, QueryCommand, ScanCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { inviaEmail } from "@imieiconcorsi/core/email";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
import { eliminaAccount } from "@imieiconcorsi/core/account";
import { attributo, cognito, gruppiDi, userPoolId, utentiNelGruppo } from "@imieiconcorsi/core/cognito";
import { batchGet, db, tables } from "@imieiconcorsi/core/db";
import {
  COMPARTO_IDS,
  GRUPPI,
  MATERIA_IDS,
  pianoDaGruppi,
  PREFISSO_BANCA_DATI,
  TETTO_AI_MESE_USD,
  type BancaDati,
  type CodiceSconto,
  type Concorso,
  type Domanda,
  type ModificheConcorso,
  type Profilo,
  type Richiesta,
  concorsiDellaBanca,
  nomeConcorsoBreve,
  nomeTipoRichiesta,
} from "@imieiconcorsi/core/domain";
import { env } from "@imieiconcorsi/core/env";
import { emailPianoAttivato, emailTornatoFree } from "@imieiconcorsi/core/email-piani";
import { HttpError, notFound, richiediAdmin, service } from "@imieiconcorsi/core/http";
import { assegnaPiano } from "@imieiconcorsi/core/piani";
import { FORMATO_CODICE, generaCodice, normalizzaCodice } from "@imieiconcorsi/core/sconti";
import { conMaiuscola, conModificheAdmin, nomeConcorso, senzaModificheAdmin } from "@imieiconcorsi/core/concorsi";
import { rispostePerUtenti, type DomandaDelFile } from "../banche-dati/pubblica";
import type { Ordine } from "../billing/ordini";
import { z } from "zod";

// Pannello di controllo: solo per il gruppo Cognito "admin" (controllato in ogni route con
// richiediAdmin). Le pagine del sito sono /admin (Admin.tsx), /admin/banche-dati,
// /admin/pagamenti e /admin/richieste. Cosa si fa da qui:
// - riepilogo: utenti per piano, richieste aperte, spesa AI del mese;
// - utenti: ricerca per email, cambio di piano e scadenza, disattivazione dell'account;
// - codici sconto: creazione e disattivazione;
// - richieste di assistenza: elenco per stato e risposte (l'utente riceve un'email);
// - storico pagamenti: ordini con filtri e totali incassati;
// - banche dati ufficiali: caricamento del PDF, estrazione, pubblicazione, ritiro, eliminazione;
// - concorsi: "concluso" toglie un bando chiuso dalle liste.

/** Utenti per pagina nell'elenco del pannello. */
const PAGINA = 50;

/** Nuovo piano di un utente e, per i piani a pagamento, la scadenza. */
const CambioPiano = z.object({
  piano: z.enum(["free", "medium", "pro"]),
  /** Data di fine (YYYY-MM-DD o ISO). Assente o null = senza scadenza. */
  scadenza: z.string().datetime({ offset: true }).or(z.string().date()).nullable().optional(),
});

/** Account attivo (true) o disattivato: un account disattivato non può più accedere. */
const CambioStato = z.object({ abilitato: z.boolean() });

/** Nuovo codice sconto. */
const NuovoCodice = z.object({
  /** Vuoto = generato a caso (es. K7MQ-2XRT) */
  codice: z.string().max(40).optional(),
  percentuale: z.number().int().min(1).max(100),
  /** Vuoto = tutti i piani a pagamento */
  piani: z.array(z.enum(["medium", "pro"])).optional(),
  /** Ultimo giorno valido (YYYY-MM-DD) */
  validoFino: z.string().date().nullable().optional(),
  usiMassimi: z.number().int().min(1).nullable().optional(),
  nota: z.string().max(200).optional(),
});

/** Attiva o disattiva un codice sconto. */
const StatoCodice = z.object({ attivo: z.boolean() });

/** Risposta dell'assistenza a una richiesta e/o nuovo stato. */
const RispostaRichiesta = z
  .object({
    testo: z.string().trim().min(2).max(3000).optional(),
    stato: z.enum(["aperta", "in-lavorazione", "chiusa"]).optional(),
  })
  .refine((r) => r.testo || r.stato, "Scrivi una risposta o cambia lo stato");

/** Come è segnata la risposta giusta nel PDF (vedi banche-dati/parser.ts). */
const FORMATI = ["auto", "indicata", "segnata", "chiave", "prima", "risposta"] as const;
/** Ordine predefinito delle risposte agli utenti (ognuno può poi scegliere il suo). */
const ORDINI = ["mescolate", "pdf"] as const;
/** PDF più grande accettato: 200 MB. */
const MAX_PDF = 200 * 1024 * 1024;

/** Dati di una banca dati da caricare (il PDF lo carica poi il browser con un link firmato). */
const NuovaBanca = z.object({
  /** Facoltativo: senza concorso la banca dati sta solo nella sezione Banche dati */
  concorsoId: z.string().min(1).optional(),
  /** Altri concorsi da collegare (scelti dai suggeriti o cercati a mano) */
  concorsiIds: z.array(z.string().min(1).max(100)).max(50).optional(),
  /** Obbligatorio senza concorso; con il concorso, se manca, si prende il suo */
  comparto: z.enum(COMPARTO_IDS).optional(),
  anno: z.number().int().min(2000).max(2100).optional(),
  titolo: z.string().trim().min(3).max(200),
  materia: z.enum(MATERIA_IDS).optional(),
  formato: z.enum(FORMATI).default("auto"),
  ordineRisposte: z.enum(ORDINI).optional(),
  nomeFile: z.string().max(300),
  dimensione: z.number().int().min(1).max(MAX_PDF, "Il PDF supera i 200 MB"),
});

/** Correzioni a un bando (solo i campi da cambiare). */
const ModificaConcorso = z
  .object({
    figura: z.string().trim().min(3, "Il nome è troppo corto").max(200),
    titolo: z.string().trim().min(3).max(1000),
    ente: z.string().trim().min(2).max(300),
    scadenza: z.iso.datetime(),
    posti: z.number().int().min(0).max(100_000),
    sedi: z.array(z.string().trim().min(1).max(120)).max(50),
    comparto: z.enum(COMPARTO_IDS),
    materie: z.array(z.enum(MATERIA_IDS)).min(1, "Almeno una materia").max(20),
    descrizione: z.string().trim().max(10_000),
    bancaDatiPrevista: z.boolean(),
  })
  .partial()
  .strict();

/** Modifiche a una banca dati; cambiare il formato rifà l'estrazione. */
const ModificaBanca = z.object({
  titolo: z.string().trim().min(3).max(200).optional(),
  comparto: z.enum(COMPARTO_IDS).optional(),
  anno: z.number().int().min(2000).max(2100).nullable().optional(),
  materia: z.enum(MATERIA_IDS).nullable().optional(),
  formato: z.enum(FORMATI).optional(),
  ordineRisposte: z.enum(ORDINI).optional(),
});

const s3 = new S3Client({});
/** Dove sta il PDF di una banca dati nel bucket dei contenuti. */
const chiavePdf = (id: string) => `banche-dati/${id}.pdf`;

/** Una banca dati; 404 se non esiste. */
async function leggiBanca(id: string) {
  const res = await db.send(new GetCommand({ TableName: tables.bancheDati, Key: { id } }));
  if (!res.Item) throw notFound("Banca dati");
  return res.Item as BancaDati;
}

/** Rifà l'estrazione: il PDF si ricopia su se stesso e la notifica S3 fa ripartire la Lambda. */
async function rilanciaEstrazione(id: string) {
  await s3.send(
    new CopyObjectCommand({
      Bucket: env("CONTENUTI_BUCKET"),
      Key: chiavePdf(id),
      CopySource: `${env("CONTENUTI_BUCKET")}/${chiavePdf(id)}`,
      MetadataDirective: "REPLACE",
      ContentType: "application/pdf",
      Metadata: { estrazione: new Date().toISOString() },
    }),
  );
}

/** Membri dei gruppi medium/pro/admin, per username. */
async function gruppiPerUtente() {
  const mappa = new Map<string, string[]>();
  for (const gruppo of Object.values(GRUPPI)) {
    for await (const u of utentiNelGruppo(gruppo)) {
      mappa.set(u.Username!, [...(mappa.get(u.Username!) ?? []), gruppo]);
    }
  }
  return mappa;
}

/** Un utente Cognito con i suoi attributi; 404 se non esiste. */
async function utenteCognito(username: string) {
  try {
    return await cognito.send(new AdminGetUserCommand({ UserPoolId: userPoolId(), Username: username }));
  } catch (err) {
    if (err instanceof Error && err.name === "UserNotFoundException") throw notFound("Utente");
    throw err;
  }
}

const condizioneFallita = (err: unknown) => err instanceof Error && err.name === "ConditionalCheckFailedException";

/** Il concorso torna alle domande dei nostri libri, se usava proprio questa banca dati. */
async function scollegaConcorso(bancaId: string, concorsoId: string) {
  await db
    .send(
      new UpdateCommand({
        TableName: tables.concorsi,
        Key: { id: concorsoId },
        UpdateExpression: "SET bancaDati = :no REMOVE bancaDatiId",
        ConditionExpression: "bancaDatiId = :b",
        ExpressionAttributeValues: { ":no": false, ":b": bancaId },
      }),
    )
    .catch((err) => {
      if (!condizioneFallita(err)) throw err;
    });
}

/** Ritirando o eliminando la banca dati, tutti i suoi concorsi tornano alle nostre domande. */
async function scollegaTutti(banca: BancaDati) {
  for (const c of concorsiDellaBanca(banca)) await scollegaConcorso(banca.id, c.id);
}

/**
 * Il concorso usa la banca dati pubblicata: link alla consultazione e simulazioni con le domande
 * ufficiali. Non se ha già un'altra banca dati (restituisce false): va scollegata prima da quella.
 */
async function collegaConcorso(bancaId: string, concorsoId: string) {
  try {
    await db.send(
      new UpdateCommand({
        TableName: tables.concorsi,
        Key: { id: concorsoId },
        UpdateExpression: "SET bancaDati = :si, bancaDatiId = :b",
        ConditionExpression: "attribute_exists(id) AND (attribute_not_exists(bancaDatiId) OR bancaDatiId = :b)",
        ExpressionAttributeValues: { ":si": true, ":b": bancaId },
      }),
    );
    return true;
  } catch (err) {
    if (condizioneFallita(err)) return false;
    throw err;
  }
}

/**
 * Salva sulla banca dati la lista dei concorsi collegati (il primo resta anche in concorsoId).
 * `prima` = la banca come letta: se nel frattempo la lista è cambiata (un'altra modifica
 * contemporanea), non si sovrascrive e si chiede di riprovare.
 */
async function salvaConcorsiDellaBanca(prima: BancaDati, concorsi: { id: string; titolo: string }[]) {
  const condizione = prima.concorsi ? { ConditionExpression: "size(concorsi) = :n" } : { ConditionExpression: "attribute_not_exists(concorsi)" };
  const n = prima.concorsi ? { ":n": prima.concorsi.length } : {};
  try {
    await db.send(
      new UpdateCommand({
        TableName: tables.bancheDati,
        Key: { id: prima.id },
        ...condizione,
        ...(concorsi.length
          ? {
              UpdateExpression: "SET concorsi = :l, concorsoId = :p, concorsoTitolo = :t",
              ExpressionAttributeValues: { ":l": concorsi, ":p": concorsi[0]!.id, ":t": concorsi[0]!.titolo, ...n },
            }
          : { UpdateExpression: "SET concorsi = :l REMOVE concorsoId, concorsoTitolo", ExpressionAttributeValues: { ":l": [], ...n } }),
      }),
    );
  } catch (err) {
    if (condizioneFallita(err)) throw new HttpError(409, "La banca dati è cambiata nel frattempo: ricarica la pagina e riprova.");
    throw err;
  }
}

/** Come si ricorda un concorso collegato sulla banca dati: nome (con l'anno) ed ente. */
const voceConcorso = (c: Concorso) => ({ id: c.id, titolo: nomeConcorso(c), ente: conMaiuscola(c.ente) });

/** Concorsi da collegare: devono esistere e non avere già un'altra banca dati pubblicata. */
async function concorsiCollegabili(ids: string[], bancaId?: string) {
  const unici = [...new Set(ids)];
  const trovati = await batchGet<Concorso>(
    tables.concorsi,
    unici.map((id) => ({ id })),
    "id, ente, figura, titolo, comparto, bancaDatiId, pubblicatoIl, scadenza",
  );
  const perId = new Map(trovati.map((c) => [c.id, c]));
  const mancanti = unici.filter((id) => !perId.has(id));
  if (mancanti.length) throw new HttpError(404, `Concorso non trovato: ${mancanti.join(", ")}`);
  const occupati = trovati.filter((c) => c.bancaDatiId && c.bancaDatiId !== bancaId);
  if (occupati.length) {
    throw new HttpError(
      409,
      `Questi concorsi hanno già un'altra banca dati: ${occupati.map(nomeConcorsoBreve).join("; ")}. Scollegala prima da quella.`,
    );
  }
  return unici.map((id) => perId.get(id)!);
}

/** Cancella le domande pubblicate (materia bd#<id>), 25 alla volta. */
async function cancellaDomande(id: string) {
  let cancellate = 0;
  let ExclusiveStartKey: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new QueryCommand({
        TableName: tables.questions,
        KeyConditionExpression: "materia = :m",
        ExpressionAttributeValues: { ":m": `${PREFISSO_BANCA_DATI}${id}` },
        ProjectionExpression: "materia, id",
        ExclusiveStartKey,
      }),
    );
    const chiavi = (res.Items ?? []) as { materia: string; id: string }[];
    for (let i = 0; i < chiavi.length; i += 25) {
      let pending = chiavi.slice(i, i + 25).map((Key) => ({ DeleteRequest: { Key } }));
      while (pending.length) {
        const out = await db.send(new BatchWriteCommand({ RequestItems: { [tables.questions]: pending } }));
        pending = (out.UnprocessedItems?.[tables.questions] ?? []) as typeof pending;
      }
    }
    cancellate += chiavi.length;
    ExclusiveStartKey = res.LastEvaluatedKey;
  } while (ExclusiveStartKey);
  return cancellate;
}

/**
 * Le domande estratte entrano nella banca domande (materia bd#<id>) e il concorso la usa:
 * da qui le simulazioni Medium e Pro di quel concorso pescano le domande ufficiali.
 * Ripubblicare sovrascrive le stesse domande (id = numero nel PDF).
 */
async function pubblicaBanca(banca: BancaDati) {
  const file = await s3.send(new GetObjectCommand({ Bucket: env("CONTENUTI_BUCKET"), Key: `banche-dati/${banca.id}.json` }));
  const { domande } = JSON.parse(await file.Body!.transformToString()) as { domande: DomandaDelFile[] };
  if (banca.ordineRisposte === "pdf" && domande.some((d) => !d.pdf)) {
    throw new HttpError(409, "Questa banca dati è stata estratta prima che si salvasse l'ordine del PDF: rifai l'estrazione, poi pubblica.");
  }
  const materia = `${PREFISSO_BANCA_DATI}${banca.id}`;
  const items: (Domanda & { materiaDiStudio?: string })[] = domande.map((d) => ({
    materia: materia as Domanda["materia"],
    id: `n${String(d.numero).padStart(5, "0")}`,
    // La sezione del PDF (es. "Matematica") è più utile del titolo della banca dati.
    argomento: d.sezione ?? banca.titolo,
    livello: 3,
    testo: d.testo,
    ...rispostePerUtenti(d, banca.ordineRisposte),
    spiegazione: d.alternativeRicavate
      ? "Risposta indicata nella banca dati ufficiale del concorso. Il file ufficiale riporta solo la risposta esatta: le altre alternative sono risposte di domande simili della stessa banca dati."
      : "Risposta indicata nella banca dati ufficiale del concorso.",
    fonte: `${banca.titolo} (banca dati ufficiale)`,
    versione: "ufficiale",
    ...(banca.materia ? { materiaDiStudio: banca.materia } : {}),
  }));
  for (let i = 0; i < items.length; i += 25) {
    let pending = items.slice(i, i + 25).map((Item) => ({ PutRequest: { Item } }));
    while (pending.length) {
      const res = await db.send(new BatchWriteCommand({ RequestItems: { [tables.questions]: pending } }));
      pending = (res.UnprocessedItems?.[tables.questions] ?? []) as typeof pending;
    }
  }
  // Ogni concorso collegato usa la banca dati; chi ne ha già un'altra resta com'è (lo si dice all'admin).
  const occupati: string[] = [];
  for (const c of concorsiDellaBanca(banca)) {
    if (!(await collegaConcorso(banca.id, c.id))) occupati.push(c.titolo);
  }
  const ora = new Date().toISOString();
  await db.send(
    new UpdateCommand({
      TableName: tables.bancheDati,
      Key: { id: banca.id },
      UpdateExpression: "SET stato = :s, pubblicataIl = :o",
      ExpressionAttributeValues: { ":s": "pubblicata", ":o": ora },
    }),
  );
  return { domande: items.length, occupati };
}

/** Tutti gli ordini (tabella piccola: uno per acquisto). */
async function tuttiGliOrdini() {
  const out: Ordine[] = [];
  let ExclusiveStartKey: Record<string, unknown> | undefined;
  do {
    const res = await db.send(new ScanCommand({ TableName: tables.ordini, ExclusiveStartKey }));
    out.push(...((res.Items ?? []) as Ordine[]));
    ExclusiveStartKey = res.LastEvaluatedKey;
  } while (ExclusiveStartKey);
  return out;
}

/** Email degli utenti (da Cognito: nel database non c'è), poche richieste alla volta. */
async function emailDi(usernames: string[]) {
  const mappa = new Map<string, string | undefined>();
  const unici = [...new Set(usernames)];
  for (let i = 0; i < unici.length; i += 5) {
    await Promise.all(
      unici.slice(i, i + 5).map(async (u) => {
        try {
          const res = await cognito.send(new AdminGetUserCommand({ UserPoolId: userPoolId(), Username: u }));
          mappa.set(u, res.UserAttributes?.find((a) => a.Name === "email")?.Value);
        } catch {
          mappa.set(u, undefined); // utente eliminato: l'ordine resta per gli obblighi fiscali
        }
      }),
    );
  }
  return mappa;
}

/** Ordini per pagina nello storico pagamenti. */
const PAGINA_ORDINI = 50;

/** Scadenza scelta come giorno (YYYY-MM-DD): vale fino alla fine di quel giorno. */
const fineGiornata = (data: string) => (data.length === 10 ? `${data}T23:59:59.000Z` : new Date(data).toISOString());

export const handler = service({
  /** Numeri del pannello: utenti per piano, richieste aperte, spesa AI del mese. */
  "GET /admin/riepilogo": async (ctx) => {
    richiediAdmin(ctx);
    const mese = new Date().toISOString().slice(0, 7);
    const [pool, gruppi, spesaAi, aperte] = await Promise.all([
      cognito.send(new DescribeUserPoolCommand({ UserPoolId: userPoolId() })),
      gruppiPerUtente(),
      // Spesa AI del mese di tutta la piattaforma (la scrive il servizio AI, tabella contatori).
      db.send(new GetCommand({ TableName: tables.contatori, Key: { id: `ai#${mese}` } })),
      db.send(
        new QueryCommand({
          TableName: tables.richieste,
          IndexName: "perStato",
          KeyConditionExpression: "stato = :s",
          ExpressionAttributeValues: { ":s": "aperta" },
          Select: "COUNT",
        }),
      ),
    ]);
    const conta = (g: string) => [...gruppi.values()].filter((gs) => gs.includes(g)).length;
    return {
      utenti: pool.UserPool?.EstimatedNumberOfUsers ?? 0,
      medium: conta(GRUPPI.medium),
      pro: conta(GRUPPI.pro),
      admin: conta(GRUPPI.admin),
      richiesteAperte: aperte.Count ?? 0,
      ai: {
        spesaUsd: Number(spesaAi.Item?.spesaMicroUsd ?? 0) / 1e6,
        tettoUsd: Number(process.env.AI_TETTO_MENSILE_USD || TETTO_AI_MESE_USD),
        chiamate: Number(spesaAi.Item?.chiamate ?? 0),
      },
    };
  },

  /** ?cerca=inizio-email &pagina=<token della pagina successiva> */
  "GET /admin/utenti": async (ctx) => {
    richiediAdmin(ctx);
    const cerca = ctx.query.cerca?.trim().replace(/"/g, "");
    const [lista, gruppi] = await Promise.all([
      cognito.send(
        new ListUsersCommand({
          UserPoolId: userPoolId(),
          Limit: PAGINA,
          PaginationToken: ctx.query.pagina || undefined,
          Filter: cerca ? `email ^= "${cerca}"` : undefined,
        }),
      ),
      gruppiPerUtente(),
    ]);
    const utenti = lista.Users ?? [];
    const profili = await batchGet<Profilo>(
      tables.users,
      utenti.map((u) => ({ userId: attributo(u, "sub") })),
      "userId, scadenzaPiano, periodo, onboarded, feedback, ultimoAccessoIl, accessi",
    );
    const profiloDi = new Map(profili.map((p) => [p.userId, p]));

    return {
      utenti: utenti.map((u: UserType) => {
        const sub = attributo(u, "sub")!;
        const gs = gruppi.get(u.Username!) ?? [];
        const p = profiloDi.get(sub);
        return {
          username: u.Username!,
          email: attributo(u, "email"),
          nome: attributo(u, "name"),
          accesso: u.Username!.includes("_") ? u.Username!.split("_")[0] : "email",
          stato: u.UserStatus,
          abilitato: u.Enabled ?? true,
          creatoIl: u.UserCreateDate?.toISOString(),
          piano: pianoDaGruppi(gs.filter((g) => g !== GRUPPI.admin)),
          admin: gs.includes(GRUPPI.admin),
          scadenzaPiano: p?.scadenzaPiano,
          periodo: p?.periodo,
          onboarded: p?.onboarded ?? false,
          feedback: p?.feedback,
          ultimoAccessoIl: p?.ultimoAccessoIl,
          accessi: p?.accessi,
        };
      }),
      pagina: lista.PaginationToken,
    };
  },

  /** Gli ultimi 50 accessi di un utente (data e modo), dal più recente: li registra Cognito a ogni login. */
  "GET /admin/utenti/{username}/accessi": async (ctx) => {
    richiediAdmin(ctx);
    const user = await utenteCognito(ctx.params.username!);
    const sub = attributo({ Attributes: user.UserAttributes }, "sub");
    if (!sub) throw new HttpError(500, "Utente senza sub");
    const res = await db.send(
      new QueryCommand({
        TableName: tables.accessi,
        KeyConditionExpression: "userId = :u",
        ExpressionAttributeValues: { ":u": sub },
        ScanIndexForward: false,
        Limit: 50,
      }),
    );
    return { accessi: ((res.Items ?? []) as { il: string; metodo: string }[]).map((a) => ({ il: a.il.split("#")[0], metodo: a.metodo })) };
  },

  /** Cambia piano e scadenza a un utente (omaggi, assistenza); gli arriva un'email. */
  "PUT /admin/utenti/{username}/piano": async (ctx) => {
    richiediAdmin(ctx);
    const { piano, scadenza } = ctx.body(CambioPiano);
    const user = await utenteCognito(ctx.params.username!);
    const sub = user.UserAttributes?.find((a) => a.Name === "sub")?.Value;
    if (!sub) throw new HttpError(500, "Utente senza sub");
    const prima = pianoDaGruppi((await gruppiDi(user.Username!)).filter((g) => g !== GRUPPI.admin));
    const fine = piano === "free" || !scadenza ? null : fineGiornata(scadenza);
    await assegnaPiano({ userId: sub, username: user.Username!, piano, scadenza: fine });

    // Email solo quando cambia davvero il tipo di piano (Free ↔ a pagamento, Medium ↔ Pro).
    const email = user.UserAttributes?.find((a) => a.Name === "email")?.Value;
    const nome = user.UserAttributes?.find((a) => a.Name === "name")?.Value;
    if (email && piano !== prima) {
      if (piano === "free") await emailTornatoFree({ a: email, nome, pianoPrecedente: prima as "medium" | "pro", motivo: "admin" });
      else await emailPianoAttivato({ a: email, nome, piano, scadenza: fine });
    }
    return { ok: true };
  },

  /** Tutti i codici sconto, dal più recente. */
  "GET /admin/codici": async (ctx) => {
    richiediAdmin(ctx);
    const codici: CodiceSconto[] = [];
    let ExclusiveStartKey: Record<string, unknown> | undefined;
    do {
      const res = await db.send(new ScanCommand({ TableName: tables.codici, ExclusiveStartKey }));
      codici.push(...((res.Items ?? []) as CodiceSconto[]));
      ExclusiveStartKey = res.LastEvaluatedKey;
    } while (ExclusiveStartKey);
    // I codici "invita un amico" degli utenti stanno nella stessa tabella: qui solo gli sconti.
    return { codici: codici.filter((c) => c.tipo !== "invito").sort((a, b) => b.creatoIl.localeCompare(a.creatoIl)) };
  },

  /** Crea un codice sconto (scelto dall'admin o generato a caso). */
  "POST /admin/codici": async (ctx) => {
    richiediAdmin(ctx);
    const dati = ctx.body(NuovoCodice);
    const scelto = dati.codice?.trim() ? normalizzaCodice(dati.codice) : undefined;
    if (scelto && !FORMATO_CODICE.test(scelto)) throw new HttpError(400, "Il codice può avere da 4 a 24 lettere, numeri o trattini");

    // Un codice generato a caso che esiste già (rarissimo) si rigenera; uno scelto a mano no.
    for (let tentativo = 0; tentativo < 3; tentativo++) {
      const codice: CodiceSconto = {
        codice: scelto ?? generaCodice(),
        percentuale: dati.percentuale,
        ...(dati.piani?.length && dati.piani.length < 2 ? { piani: dati.piani } : {}),
        ...(dati.validoFino ? { validoFino: fineGiornata(dati.validoFino) } : {}),
        ...(dati.usiMassimi ? { usiMassimi: dati.usiMassimi } : {}),
        ...(dati.nota?.trim() ? { nota: dati.nota.trim() } : {}),
        usi: 0,
        attivo: true,
        creatoIl: new Date().toISOString(),
        creatoDa: ctx.email ?? ctx.username,
      };
      try {
        await db.send(new PutCommand({ TableName: tables.codici, Item: codice, ConditionExpression: "attribute_not_exists(codice)" }));
        return codice;
      } catch (err) {
        if (!(err instanceof Error && err.name === "ConditionalCheckFailedException")) throw err;
        if (scelto) throw new HttpError(409, `Il codice ${scelto} esiste già`);
      }
    }
    throw new HttpError(500, "Non riesco a generare un codice libero, riprova");
  },

  /** Attiva o disattiva un codice: disattivato smette subito di funzionare. */
  "PUT /admin/codici/{codice}": async (ctx) => {
    richiediAdmin(ctx);
    const { attivo } = ctx.body(StatoCodice);
    try {
      await db.send(
        new UpdateCommand({
          TableName: tables.codici,
          Key: { codice: ctx.params.codice },
          UpdateExpression: "SET attivo = :a",
          ConditionExpression: "attribute_exists(codice)",
          ExpressionAttributeValues: { ":a": attivo },
        }),
      );
    } catch (err) {
      if (err instanceof Error && err.name === "ConditionalCheckFailedException") throw notFound("Codice");
      throw err;
    }
    return { ok: true };
  },

  // ── Richieste di assistenza ────────────────────────────────────────────────

  /** Richieste per stato (indice perStato), dalla più recente. ?stato=aperta|in-lavorazione|chiusa */
  "GET /admin/richieste": async (ctx) => {
    richiediAdmin(ctx);
    const stato = ctx.query.stato ?? "aperta";
    const res = await db.send(
      new QueryCommand({
        TableName: tables.richieste,
        IndexName: "perStato",
        KeyConditionExpression: "stato = :s",
        ExpressionAttributeValues: { ":s": stato },
        ScanIndexForward: false,
        Limit: 100,
      }),
    );
    const richieste = (res.Items ?? []) as Richiesta[];
    const emails = await emailDi(richieste.map((r) => r.username));
    // Quante per stato, per i contatori del pannello.
    const conteggi = Object.fromEntries(
      await Promise.all(
        (["aperta", "in-lavorazione", "chiusa"] as const).map(async (s) => {
          const c = await db.send(
            new QueryCommand({
              TableName: tables.richieste,
              IndexName: "perStato",
              KeyConditionExpression: "stato = :s",
              ExpressionAttributeValues: { ":s": s },
              Select: "COUNT",
            }),
          );
          return [s, c.Count ?? 0];
        }),
      ),
    );
    return { conteggi, richieste: richieste.map(({ username, ...r }) => ({ ...r, email: emails.get(username) })) };
  },

  /** Risposta dell'assistenza e/o cambio di stato. Con una risposta, l'utente riceve un'email. */
  "POST /admin/richieste/{userId}/{id}": async (ctx) => {
    richiediAdmin(ctx);
    const { testo, stato } = ctx.body(RispostaRichiesta);
    const chiave = { userId: ctx.params.userId, id: ctx.params.id };
    const res = await db.send(new GetCommand({ TableName: tables.richieste, Key: chiave }));
    const r = res.Item as Richiesta | undefined;
    if (!r) throw notFound("Richiesta");

    const ora = new Date().toISOString();
    const set = ["aggiornataIl = :o"];
    const valori: Record<string, unknown> = { ":o": ora };
    if (testo) {
      set.push("messaggi = list_append(messaggi, :m)", "daLeggere = :si");
      valori[":m"] = [{ da: "assistenza", testo, il: ora }];
      valori[":si"] = true;
    }
    // Una risposta senza stato scelto mette la richiesta "in lavorazione" (se era aperta).
    const nuovoStato = stato ?? (testo && r.stato === "aperta" ? "in-lavorazione" : undefined);
    if (nuovoStato) {
      set.push("stato = :s");
      valori[":s"] = nuovoStato;
    }
    await db.send(new UpdateCommand({ TableName: tables.richieste, Key: chiave, UpdateExpression: `SET ${set.join(", ")}`, ExpressionAttributeValues: valori }));

    if (testo) {
      const email = (await emailDi([r.username])).get(r.username);
      if (email) {
        await inviaEmail({
          a: email,
          oggetto: `Risposta alla tua richiesta: ${nomeTipoRichiesta(r.tipo)}`,
          testo: [
            "Ciao,",
            "",
            "l'assistenza di iMieiConcorsi ha risposto alla tua richiesta:",
            "",
            testo,
            "",
            `Per rispondere o vedere la conversazione: ${process.env.SITE_URL ?? ""}/app/assistenza`,
            "",
            "Il team di iMieiConcorsi",
          ].join("\n"),
        }).catch((err) => console.error("Email di risposta alla richiesta non inviata", err));
      }
    }
    return { ok: true, stato: nuovoStato ?? r.stato };
  },

  // ── Storico pagamenti ──────────────────────────────────────────────────────

  /**
   * Ordini dal più recente. ?stato=pagato|in-attesa|scaduto|fallito &piano=medium|pro
   * &email=inizio dell'indirizzo &pagina=0,1,2… Con i totali incassati.
   */
  "GET /admin/ordini": async (ctx) => {
    richiediAdmin(ctx);
    const { stato, piano, email, pagina } = ctx.query;
    let ordini = (await tuttiGliOrdini()).sort((a, b) => b.creatoIl.localeCompare(a.creatoIl));

    const pagati = ordini.filter((o) => o.stato === "pagato");
    const mese = new Date().toISOString().slice(0, 7);
    const somma = (lista: Ordine[]) => Math.round(lista.reduce((n, o) => n + o.importo, 0) * 100) / 100;
    const totali = {
      ordini: ordini.length,
      pagati: pagati.length,
      incassato: somma(pagati),
      incassatoMese: somma(pagati.filter((o) => (o.pagatoIl ?? o.creatoIl).startsWith(mese))),
      perStato: Object.fromEntries(["pagato", "in-attesa", "scaduto", "fallito"].map((s) => [s, ordini.filter((o) => o.stato === s).length])),
    };

    if (stato) ordini = ordini.filter((o) => o.stato === stato);
    if (piano) ordini = ordini.filter((o) => o.piano === piano);
    if (email?.trim()) {
      // Da email a utenti Cognito (anche più account con la stessa email), poi i loro ordini.
      const res = await cognito.send(
        new ListUsersCommand({ UserPoolId: userPoolId(), Filter: `email ^= "${email.trim().replace(/"/g, "")}"`, Limit: 20 }),
      );
      const subs = new Set((res.Users ?? []).map((u) => attributo(u, "sub")));
      // Anche gli ordini di account eliminati, con l'email salvata sull'ordine.
      const q = email.trim().toLowerCase();
      ordini = ordini.filter((o) => subs.has(o.userId) || !!o.email?.toLowerCase().startsWith(q));
    }

    const n = Math.max(0, Number(pagina) || 0);
    const fetta = ordini.slice(n * PAGINA_ORDINI, (n + 1) * PAGINA_ORDINI);
    const emails = await emailDi(fetta.map((o) => o.username));
    return {
      totali,
      ordini: fetta.map((o) => ({
        id: o.id,
        // Email attuale da Cognito; se l'account non c'è più, quella salvata sull'ordine.
        email: emails.get(o.username) ?? (o.email || undefined),
        nome: o.nome || undefined,
        accountEliminato: !emails.get(o.username),
        ricevuta: o.ricevuta,
        piano: o.piano,
        periodo: o.periodo,
        prezzo: o.prezzo,
        importo: o.importo,
        codiceSconto: o.codiceSconto,
        percentualeSconto: o.percentualeSconto,
        stato: o.stato,
        creatoIl: o.creatoIl,
        pagatoIl: o.pagatoIl,
        scadenzaPiano: o.scadenzaPiano,
        stripeSessionId: o.stripeSessionId,
      })),
      trovati: ordini.length,
      prossima: (n + 1) * PAGINA_ORDINI < ordini.length ? n + 1 : null,
    };
  },

  // ── Banche dati ufficiali ──────────────────────────────────────────────────

  /** Tutte le banche dati, in ogni stato, dall'ultima caricata. */
  "GET /admin/banche-dati": async (ctx) => {
    richiediAdmin(ctx);
    const banche: BancaDati[] = [];
    let ExclusiveStartKey: Record<string, unknown> | undefined;
    do {
      const res = await db.send(new ScanCommand({ TableName: tables.bancheDati, ExclusiveStartKey }));
      banche.push(...((res.Items ?? []) as BancaDati[]));
      ExclusiveStartKey = res.LastEvaluatedKey;
    } while (ExclusiveStartKey);
    return { banche: banche.sort((a, b) => b.caricataIl.localeCompare(a.caricataIl)) };
  },

  /** Crea la banca dati e restituisce l'indirizzo (valido 15 minuti) per caricare il PDF su S3. */
  "POST /admin/banche-dati": async (ctx) => {
    richiediAdmin(ctx);
    const dati = ctx.body(NuovaBanca);
    // Concorsi collegati da subito: quello principale e gli altri scelti (suggeriti o cercati).
    const collegati = await concorsiCollegabili([...(dati.concorsoId ? [dati.concorsoId] : []), ...(dati.concorsiIds ?? [])]);
    const concorsi = collegati.map(voceConcorso);
    const comparto = dati.comparto ?? collegati[0]?.comparto;
    if (!comparto) throw new HttpError(400, "Indica il comparto o un concorso");

    const banca: BancaDati = {
      id: `bd_${randomUUID().replace(/-/g, "").slice(0, 16)}`,
      comparto,
      ...(dati.anno ? { anno: dati.anno } : {}),
      ...(concorsi.length ? { concorsi, concorsoId: concorsi[0]!.id, concorsoTitolo: concorsi[0]!.titolo } : {}),
      titolo: dati.titolo,
      ...(dati.materia ? { materia: dati.materia } : {}),
      formato: dati.formato,
      ...(dati.ordineRisposte === "pdf" ? { ordineRisposte: "pdf" as const } : {}),
      stato: "caricamento",
      nomeFile: dati.nomeFile,
      dimensione: dati.dimensione,
      caricataIl: new Date().toISOString(),
      caricataDa: ctx.email ?? ctx.username,
    };
    await db.send(new PutCommand({ TableName: tables.bancheDati, Item: banca }));
    const upload = await getSignedUrl(
      s3,
      new PutObjectCommand({ Bucket: env("CONTENUTI_BUCKET"), Key: chiavePdf(banca.id), ContentType: "application/pdf" }),
      { expiresIn: 900 },
    );
    return { banca, upload };
  },

  /**
   * Cambia titolo, materia, formato o ordine delle risposte. Cambiando il formato l'estrazione
   * riparte; cambiando l'ordine di una banca già pubblicata, le domande si ripubblicano.
   */
  "PUT /admin/banche-dati/{id}": async (ctx) => {
    richiediAdmin(ctx);
    const banca = await leggiBanca(ctx.params.id!);
    const { titolo, materia, formato, comparto, anno, ordineRisposte } = ctx.body(ModificaBanca);
    const set: string[] = [];
    const remove: string[] = [];
    const valori: Record<string, unknown> = {};
    if (titolo) (set.push("titolo = :t"), (valori[":t"] = titolo));
    if (comparto) (set.push("comparto = :c"), (valori[":c"] = comparto));
    if (anno) (set.push("anno = :a"), (valori[":a"] = anno));
    if (anno === null) remove.push("anno");
    if (materia) (set.push("materia = :m"), (valori[":m"] = materia));
    if (materia === null) remove.push("materia");
    const riestrai = !!formato && formato !== banca.formato && banca.stato !== "caricamento";
    if (formato) (set.push("formato = :f"), (valori[":f"] = formato));
    if (riestrai) (set.push("stato = :s"), (valori[":s"] = "estrazione"));
    const nuovoOrdine = !!ordineRisposte && ordineRisposte !== (banca.ordineRisposte ?? "mescolate");
    if (ordineRisposte) (set.push("ordineRisposte = :o"), (valori[":o"] = ordineRisposte));
    if (!set.length && !remove.length) return banca;
    // Prima si ripubblica con il nuovo ordine: se non si può (estrazione vecchia), non si salva nulla.
    if (nuovoOrdine && banca.stato === "pubblicata" && !riestrai) await pubblicaBanca({ ...banca, ordineRisposte });
    await db.send(
      new UpdateCommand({
        TableName: tables.bancheDati,
        Key: { id: banca.id },
        UpdateExpression: [set.length ? `SET ${set.join(", ")}` : "", remove.length ? `REMOVE ${remove.join(", ")}` : ""].join(" ").trim(),
        ...(Object.keys(valori).length ? { ExpressionAttributeValues: valori } : {}),
      }),
    );
    if (riestrai) await rilanciaEstrazione(banca.id);
    return leggiBanca(banca.id);
  },

  /** Rifà l'estrazione delle domande dal PDF. */
  "POST /admin/banche-dati/{id}/estrai": async (ctx) => {
    richiediAdmin(ctx);
    const banca = await leggiBanca(ctx.params.id!);
    await rilanciaEstrazione(banca.id);
    return { ok: true };
  },

  /** Pubblica le domande estratte: compaiono nella sezione Banche dati e nel concorso collegato. */
  "POST /admin/banche-dati/{id}/pubblica": async (ctx) => {
    richiediAdmin(ctx);
    const banca = await leggiBanca(ctx.params.id!);
    if (banca.stato !== "estratta" && banca.stato !== "pubblicata") throw new HttpError(409, "Prima serve un'estrazione riuscita");
    if (!banca.domande) throw new HttpError(409, "Nessuna domanda da pubblicare");
    return { ok: true, ...(await pubblicaBanca(banca)) };
  },

  /**
   * Collega un concorso (di solito aperto) alla banca dati, anche dopo il caricamento. Se la
   * banca è già pubblicata, il concorso mostra subito il link alla consultazione e le sue
   * simulazioni usano le domande ufficiali; altrimenti succede alla pubblicazione.
   */
  "POST /admin/banche-dati/{id}/concorsi": async (ctx) => {
    richiediAdmin(ctx);
    const { concorsoId } = ctx.body(z.object({ concorsoId: z.string().min(1).max(100) }));
    const banca = await leggiBanca(ctx.params.id!);
    const attuali = concorsiDellaBanca(banca);
    if (attuali.some((c) => c.id === concorsoId)) return banca;
    const [concorso] = await concorsiCollegabili([concorsoId], banca.id);
    // Prima la lista (se è cambiata nel frattempo non si tocca nulla), poi il concorso.
    const nuova = [...attuali, voceConcorso(concorso!)];
    await salvaConcorsiDellaBanca(banca, nuova);
    if (banca.stato === "pubblicata" && !(await collegaConcorso(banca.id, concorsoId))) {
      await salvaConcorsiDellaBanca({ ...banca, concorsi: nuova }, attuali).catch(() => {});
      throw new HttpError(409, "Il concorso ha già un'altra banca dati: scollegala prima da quella.");
    }
    return leggiBanca(banca.id);
  },

  /** Scollega un concorso: torna alle domande della nostra banca e perde il link alla banca dati. */
  "DELETE /admin/banche-dati/{id}/concorsi/{concorsoId}": async (ctx) => {
    richiediAdmin(ctx);
    const banca = await leggiBanca(ctx.params.id!);
    const concorsoId = ctx.params.concorsoId!;
    await salvaConcorsiDellaBanca(
      banca,
      concorsiDellaBanca(banca).filter((c) => c.id !== concorsoId),
    );
    await scollegaConcorso(banca.id, concorsoId);
    return leggiBanca(banca.id);
  },

  /** Il concorso torna alle domande dei nostri libri; la banca dati resta, ripubblicabile. */
  "POST /admin/banche-dati/{id}/ritira": async (ctx) => {
    richiediAdmin(ctx);
    const banca = await leggiBanca(ctx.params.id!);
    await scollegaTutti(banca);
    await db.send(
      new UpdateCommand({
        TableName: tables.bancheDati,
        Key: { id: banca.id },
        UpdateExpression: "SET stato = :s",
        ExpressionAttributeValues: { ":s": "estratta" },
      }),
    );
    return { ok: true };
  },

  /**
   * Elimina la banca dati per sempre: il concorso torna alle nostre domande, le domande
   * ufficiali e il PDF spariscono. Le sessioni già fatte restano nelle statistiche.
   */
  "DELETE /admin/banche-dati/{id}": async (ctx) => {
    richiediAdmin(ctx);
    const banca = await leggiBanca(ctx.params.id!);
    await scollegaTutti(banca);
    const domande = await cancellaDomande(banca.id);
    await s3.send(
      new DeleteObjectsCommand({
        Bucket: env("CONTENUTI_BUCKET"),
        Delete: { Objects: [{ Key: chiavePdf(banca.id) }, { Key: `banche-dati/${banca.id}.json` }], Quiet: true },
      }),
    );
    await db.send(new DeleteCommand({ TableName: tables.bancheDati, Key: { id: banca.id } }));
    console.log(`Banca dati ${banca.id} (${banca.titolo}) eliminata da ${ctx.email ?? ctx.username}: ${domande} domande`);
    return { ok: true, domande };
  },

  /**
   * Corregge un bando (nome, ente, scadenza, posti, sedi, comparto, materie, testo, banca dati
   * prevista). Si mandano solo i campi cambiati; restano anche dopo l'import del mattino da inPA.
   */
  "PUT /admin/concorsi/{id}": async (ctx) => {
    richiediAdmin(ctx);
    const nuove = ctx.body(ModificaConcorso) as ModificheConcorso;
    if (!Object.keys(nuove).length) throw new HttpError(400, "Nessuna modifica");
    // Materie scelte dall'admin: non sono più "stimate dal comparto".
    if (nuove.materie) nuove.materieStimate = false;
    const res = await db.send(new GetCommand({ TableName: tables.concorsi, Key: { id: ctx.params.id } }));
    if (!res.Item) throw notFound("Concorso");
    const prima = res.Item as Concorso;
    const dopo: Concorso = { ...conModificheAdmin(prima, { ...prima.modificheAdmin, ...nuove }), modificatoIl: new Date().toISOString() };
    await db.send(new PutCommand({ TableName: tables.concorsi, Item: dopo, ConditionExpression: "attribute_exists(id)" }));
    console.log(`Concorso ${prima.id} corretto da ${ctx.email ?? ctx.username}: ${Object.keys(nuove).join(", ")}`);
    return dopo;
  },

  /** Annulla le correzioni dell'admin: tornano i valori di inPA. */
  "DELETE /admin/concorsi/{id}/modifiche": async (ctx) => {
    richiediAdmin(ctx);
    const res = await db.send(new GetCommand({ TableName: tables.concorsi, Key: { id: ctx.params.id } }));
    if (!res.Item) throw notFound("Concorso");
    const dopo = senzaModificheAdmin(res.Item as Concorso);
    await db.send(new PutCommand({ TableName: tables.concorsi, Item: dopo, ConditionExpression: "attribute_exists(id)" }));
    return dopo;
  },

  /** Concorso finito: sparisce anche dai bandi scaduti (o ricompare, togliendo il segno). */
  "PUT /admin/concorsi/{id}/concluso": async (ctx) => {
    richiediAdmin(ctx);
    const { concluso } = ctx.body(z.object({ concluso: z.boolean() }));
    try {
      await db.send(
        new UpdateCommand({
          TableName: tables.concorsi,
          Key: { id: ctx.params.id },
          UpdateExpression: concluso ? "SET conclusoIl = :o" : "REMOVE conclusoIl",
          ConditionExpression: "attribute_exists(id)",
          ...(concluso ? { ExpressionAttributeValues: { ":o": new Date().toISOString() } } : {}),
        }),
      );
    } catch (err) {
      if (err instanceof Error && err.name === "ConditionalCheckFailedException") throw notFound("Concorso");
      throw err;
    }
    return { ok: true };
  },

  /** Disattiva o riattiva un account (non il proprio). */
  "PUT /admin/utenti/{username}/stato": async (ctx) => {
    richiediAdmin(ctx);
    const { abilitato } = ctx.body(CambioStato);
    const username = ctx.params.username!;
    if (username === ctx.username) throw new HttpError(400, "Non puoi disattivare il tuo account");
    const Command = abilitato ? AdminEnableUserCommand : AdminDisableUserCommand;
    await cognito.send(new Command({ UserPoolId: userPoolId(), Username: username }));
    return { ok: true };
  },

  /**
   * Elimina per sempre un utente: tutti i suoi dati e il login, come "Elimina account" del
   * profilo (core/account.ts). Restano solo gli ordini (obbligo contabile). Non il proprio.
   */
  "DELETE /admin/utenti/{username}": async (ctx) => {
    richiediAdmin(ctx);
    const username = ctx.params.username!;
    if (username === ctx.username) throw new HttpError(400, "Non puoi eliminare il tuo account da qui: usa il tuo profilo.");
    const user = await utenteCognito(username);
    const sub = attributo({ Attributes: user.UserAttributes }, "sub");
    if (!sub) throw new HttpError(500, "Utente senza sub");
    await eliminaAccount(sub, username, {
      email: attributo({ Attributes: user.UserAttributes }, "email"),
      nome: attributo({ Attributes: user.UserAttributes }, "name"),
    });
    console.log(`Utente ${sub} eliminato dall'admin ${ctx.email ?? ctx.username}`);
    return { ok: true };
  },
});
