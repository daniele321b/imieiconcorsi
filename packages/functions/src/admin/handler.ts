import {
  AdminDisableUserCommand,
  AdminEnableUserCommand,
  AdminGetUserCommand,
  DescribeUserPoolCommand,
  ListUsersCommand,
  type UserType,
} from "@aws-sdk/client-cognito-identity-provider";
import { randomUUID } from "node:crypto";
import { CopyObjectCommand, GetObjectCommand, PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { BatchWriteCommand, GetCommand, PutCommand, ScanCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
import { attributo, cognito, gruppiDi, userPoolId, utentiNelGruppo } from "@imieiconcorsi/core/cognito";
import { batchGet, db, tables } from "@imieiconcorsi/core/db";
import {
  COMPARTO_IDS,
  GRUPPI,
  MATERIA_IDS,
  pianoDaGruppi,
  PREFISSO_BANCA_DATI,
  type BancaDati,
  type CodiceSconto,
  type Concorso,
  type Domanda,
  type Profilo,
} from "@imieiconcorsi/core/domain";
import { env } from "@imieiconcorsi/core/env";
import { emailPianoAttivato, emailTornatoFree } from "@imieiconcorsi/core/email-piani";
import { HttpError, notFound, richiediAdmin, service } from "@imieiconcorsi/core/http";
import { assegnaPiano } from "@imieiconcorsi/core/piani";
import { FORMATO_CODICE, generaCodice, normalizzaCodice } from "@imieiconcorsi/core/sconti";
import { z } from "zod";

// Pannello di controllo: solo per il gruppo Cognito "admin" (controllato in ogni route).

const PAGINA = 50;

const CambioPiano = z.object({
  piano: z.enum(["free", "medium", "pro"]),
  /** Data di fine (YYYY-MM-DD o ISO). Assente o null = senza scadenza. */
  scadenza: z.string().datetime({ offset: true }).or(z.string().date()).nullable().optional(),
});

const CambioStato = z.object({ abilitato: z.boolean() });

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

const StatoCodice = z.object({ attivo: z.boolean() });

const FORMATI = ["auto", "indicata", "segnata", "chiave", "prima"] as const;
const MAX_PDF = 200 * 1024 * 1024;

const NuovaBanca = z.object({
  /** Facoltativo: senza concorso la banca dati sta solo nella sezione Banche dati */
  concorsoId: z.string().min(1).optional(),
  /** Obbligatorio senza concorso; con il concorso, se manca, si prende il suo */
  comparto: z.enum(COMPARTO_IDS).optional(),
  anno: z.number().int().min(2000).max(2100).optional(),
  titolo: z.string().trim().min(3).max(200),
  materia: z.enum(MATERIA_IDS).optional(),
  formato: z.enum(FORMATI).default("auto"),
  nomeFile: z.string().max(300),
  dimensione: z.number().int().min(1).max(MAX_PDF, "Il PDF supera i 200 MB"),
});

const ModificaBanca = z.object({
  titolo: z.string().trim().min(3).max(200).optional(),
  comparto: z.enum(COMPARTO_IDS).optional(),
  anno: z.number().int().min(2000).max(2100).nullable().optional(),
  materia: z.enum(MATERIA_IDS).nullable().optional(),
  formato: z.enum(FORMATI).optional(),
});

const s3 = new S3Client({});
const chiavePdf = (id: string) => `banche-dati/${id}.pdf`;

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

async function utenteCognito(username: string) {
  try {
    return await cognito.send(new AdminGetUserCommand({ UserPoolId: userPoolId(), Username: username }));
  } catch (err) {
    if (err instanceof Error && err.name === "UserNotFoundException") throw notFound("Utente");
    throw err;
  }
}

const fineGiornata = (data: string) => (data.length === 10 ? `${data}T23:59:59.000Z` : new Date(data).toISOString());

export const handler = service({
  "GET /admin/riepilogo": async (ctx) => {
    richiediAdmin(ctx);
    const [pool, gruppi] = await Promise.all([
      cognito.send(new DescribeUserPoolCommand({ UserPoolId: userPoolId() })),
      gruppiPerUtente(),
    ]);
    const conta = (g: string) => [...gruppi.values()].filter((gs) => gs.includes(g)).length;
    return {
      utenti: pool.UserPool?.EstimatedNumberOfUsers ?? 0,
      medium: conta(GRUPPI.medium),
      pro: conta(GRUPPI.pro),
      admin: conta(GRUPPI.admin),
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
      "userId, scadenzaPiano, periodo, onboarded, feedback",
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
        };
      }),
      pagina: lista.PaginationToken,
    };
  },

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

  "GET /admin/codici": async (ctx) => {
    richiediAdmin(ctx);
    const codici: CodiceSconto[] = [];
    let ExclusiveStartKey: Record<string, unknown> | undefined;
    do {
      const res = await db.send(new ScanCommand({ TableName: tables.codici, ExclusiveStartKey }));
      codici.push(...((res.Items ?? []) as CodiceSconto[]));
      ExclusiveStartKey = res.LastEvaluatedKey;
    } while (ExclusiveStartKey);
    return { codici: codici.sort((a, b) => b.creatoIl.localeCompare(a.creatoIl)) };
  },

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

  // ── Banche dati ufficiali ──────────────────────────────────────────────────

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
    let concorso: Concorso | undefined;
    if (dati.concorsoId) {
      concorso = (await db.send(new GetCommand({ TableName: tables.concorsi, Key: { id: dati.concorsoId } }))).Item as Concorso | undefined;
      if (!concorso) throw notFound("Concorso");
    }
    const comparto = dati.comparto ?? concorso?.comparto;
    if (!comparto) throw new HttpError(400, "Indica il comparto o un concorso");

    const banca: BancaDati = {
      id: `bd_${randomUUID().replace(/-/g, "").slice(0, 16)}`,
      comparto,
      ...(dati.anno ? { anno: dati.anno } : {}),
      ...(concorso ? { concorsoId: concorso.id, concorsoTitolo: `${concorso.ente} — ${concorso.figura ?? concorso.titolo}` } : {}),
      titolo: dati.titolo,
      ...(dati.materia ? { materia: dati.materia } : {}),
      formato: dati.formato,
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

  /** Cambia titolo, materia o formato; cambiando il formato l'estrazione riparte. */
  "PUT /admin/banche-dati/{id}": async (ctx) => {
    richiediAdmin(ctx);
    const banca = await leggiBanca(ctx.params.id!);
    const { titolo, materia, formato, comparto, anno } = ctx.body(ModificaBanca);
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
    if (!set.length && !remove.length) return banca;
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

  "POST /admin/banche-dati/{id}/estrai": async (ctx) => {
    richiediAdmin(ctx);
    const banca = await leggiBanca(ctx.params.id!);
    await rilanciaEstrazione(banca.id);
    return { ok: true };
  },

  /**
   * Le domande estratte entrano nella banca domande (materia bd#<id>) e il concorso la usa:
   * da qui le simulazioni Medium e Pro di quel concorso pescano le domande ufficiali.
   */
  "POST /admin/banche-dati/{id}/pubblica": async (ctx) => {
    richiediAdmin(ctx);
    const banca = await leggiBanca(ctx.params.id!);
    if (banca.stato !== "estratta" && banca.stato !== "pubblicata") throw new HttpError(409, "Prima serve un'estrazione riuscita");
    if (!banca.domande) throw new HttpError(409, "Nessuna domanda da pubblicare");

    const file = await s3.send(new GetObjectCommand({ Bucket: env("CONTENUTI_BUCKET"), Key: `banche-dati/${banca.id}.json` }));
    const { domande } = JSON.parse(await file.Body!.transformToString()) as {
      domande: { numero: number; testo: string; opzioni: string[]; corretta: number }[];
    };
    const materia = `${PREFISSO_BANCA_DATI}${banca.id}`;
    const items: (Domanda & { materiaDiStudio?: string })[] = domande.map((d) => ({
      materia: materia as Domanda["materia"],
      id: `n${String(d.numero).padStart(5, "0")}`,
      argomento: banca.titolo,
      livello: 3,
      testo: d.testo,
      opzioni: d.opzioni,
      corretta: d.corretta,
      spiegazione: "Risposta indicata nella banca dati ufficiale del concorso.",
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
    if (banca.concorsoId) {
      await db.send(
        new UpdateCommand({
          TableName: tables.concorsi,
          Key: { id: banca.concorsoId },
          UpdateExpression: "SET bancaDati = :si, bancaDatiId = :b",
          ExpressionAttributeValues: { ":si": true, ":b": banca.id },
        }),
      );
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
    return { ok: true, domande: items.length };
  },

  /** Il concorso torna alle domande dei nostri libri; la banca dati resta, ripubblicabile. */
  "POST /admin/banche-dati/{id}/ritira": async (ctx) => {
    richiediAdmin(ctx);
    const banca = await leggiBanca(ctx.params.id!);
    if (banca.concorsoId) {
      await db
        .send(
          new UpdateCommand({
            TableName: tables.concorsi,
            Key: { id: banca.concorsoId },
            UpdateExpression: "SET bancaDati = :no REMOVE bancaDatiId",
            ConditionExpression: "bancaDatiId = :b",
            ExpressionAttributeValues: { ":no": false, ":b": banca.id },
          }),
        )
        .catch((err) => {
          if (!(err instanceof Error && err.name === "ConditionalCheckFailedException")) throw err;
        });
    }
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

  "PUT /admin/utenti/{username}/stato": async (ctx) => {
    richiediAdmin(ctx);
    const { abilitato } = ctx.body(CambioStato);
    const username = ctx.params.username!;
    if (username === ctx.username) throw new HttpError(400, "Non puoi disattivare il tuo account");
    const Command = abilitato ? AdminEnableUserCommand : AdminDisableUserCommand;
    await cognito.send(new Command({ UserPoolId: userPoolId(), Username: username }));
    return { ok: true };
  },
});
