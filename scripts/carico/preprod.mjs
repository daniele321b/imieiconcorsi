// Preparazione di preprod per i test di carico (docs/TEST-DI-CARICO.md). Lo lancia
// scripts/deploy.sh carico …, che passa i nomi giusti: non serve chiamarlo a mano.
//
//   node scripts/carico/preprod.mjs utenti N           crea N utenti di prova (o li completa)
//   node scripts/carico/preprod.mjs elimina-utenti     cancella gli utenti di prova da Cognito
//   node scripts/carico/preprod.mjs copia-banche       copia le banche dati pubblicate da dev (o prod)
//
// Variabili: REGION, USER_POOL_ID, PASSWORD (utenti); TABELLE_DA e TABELLE_A, JSON
// { banche, questions } con i nomi delle tabelle di origine e di preprod (copia-banche).
//
// Gli utenti di prova hanno email success+caricoNNNN@simulator.amazonses.com: il simulatore di
// SES accetta tutto senza consegnare niente, quindi le email che partono durante il test non
// arrivano a nessuno e non toccano la reputazione del dominio. Uno su tre è nel piano Medium
// (gruppo Cognito "medium"), come ci si aspetta tra gli iscritti: k6 legge il piano dal token.

import {
  AdminAddUserToGroupCommand,
  AdminCreateUserCommand,
  AdminDeleteUserCommand,
  AdminSetUserPasswordCommand,
  CognitoIdentityProviderClient,
  ListUsersCommand,
} from "@aws-sdk/client-cognito-identity-provider";
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { BatchWriteCommand, DynamoDBDocumentClient, PutCommand, QueryCommand, ScanCommand } from "@aws-sdk/lib-dynamodb";

const REGION = process.env.REGION ?? "eu-south-1";
const cognito = new CognitoIdentityProviderClient({ region: REGION, maxAttempts: 8 });
const db = DynamoDBDocumentClient.from(new DynamoDBClient({ region: REGION, maxAttempts: 8 }));

/** Email dell'utente di prova numero n (1, 2, …): la stessa regola usata da k6 (scenari.js). */
export const emailUtente = (n) => `success+carico${String(n).padStart(4, "0")}@simulator.amazonses.com`;
/** Uno su tre nel piano Medium: 3, 6, 9… (k6 lo legge comunque dal token). */
const medium = (n) => n % 3 === 0;
/** Prefisso delle email di prova, per trovarle con ListUsers. */
const PREFISSO = "success+carico";

/** Valore obbligatorio da una variabile d'ambiente. */
function env(nome) {
  const v = process.env[nome];
  if (!v) throw new Error(`manca la variabile ${nome}`);
  return v;
}

/** Esegue lavoro(x) per ogni elemento, al massimo `insieme` alla volta (i limiti di Cognito sono bassi). */
async function aGruppi(elementi, insieme, lavoro) {
  let i = 0;
  let fatti = 0;
  const avanzamento = setInterval(() => process.stdout.write(`\r  ${fatti}/${elementi.length}`), 1000);
  try {
    await Promise.all(
      Array.from({ length: insieme }, async () => {
        while (i < elementi.length) {
          const x = elementi[i++];
          await lavoro(x);
          fatti++;
        }
      }),
    );
  } finally {
    clearInterval(avanzamento);
    process.stdout.write(`\r  ${fatti}/${elementi.length}\n`);
  }
}

/** Crea (o sistema, se c'è già) l'utente di prova n: email verificata, password definitiva, piano. */
async function creaUtente(pool, password, n) {
  const email = emailUtente(n);
  try {
    await cognito.send(
      new AdminCreateUserCommand({
        UserPoolId: pool,
        Username: email,
        // Nessuna email di benvenuto: l'utente nasce già pronto.
        MessageAction: "SUPPRESS",
        UserAttributes: [
          { Name: "email", Value: email },
          { Name: "email_verified", Value: "true" },
        ],
      }),
    );
  } catch (err) {
    if (err.name !== "UsernameExistsException") throw err;
  }
  // Password definitiva: altrimenti al primo login Cognito chiederebbe di cambiarla.
  await cognito.send(new AdminSetUserPasswordCommand({ UserPoolId: pool, Username: email, Password: password, Permanent: true }));
  if (medium(n)) await cognito.send(new AdminAddUserToGroupCommand({ UserPoolId: pool, Username: email, GroupName: "medium" }));
}

/** utenti N: crea gli utenti di prova da 1 a N. Rilanciarlo è sicuro (completa quelli che mancano). */
async function utenti(n) {
  if (!Number.isInteger(n) || n < 1 || n > 5000) throw new Error("numero di utenti tra 1 e 5000");
  const pool = env("USER_POOL_ID");
  const password = env("PASSWORD");
  console.log(`  ${n} utenti di prova nel pool ${pool} (${Math.ceil(n / 3)} nel piano Medium)`);
  // 5 alla volta: ogni utente sono 2-3 chiamate, e Cognito ne accetta qualche decina al secondo.
  await aGruppi(
    Array.from({ length: n }, (_, i) => i + 1),
    5,
    (i) => creaUtente(pool, password, i),
  );
}

/** Tutti gli username degli utenti di prova (email che inizia con success+carico). */
async function utentiDiProva(pool) {
  const out = [];
  let PaginationToken;
  do {
    const res = await cognito.send(new ListUsersCommand({ UserPoolId: pool, Filter: `email ^= "${PREFISSO}"`, PaginationToken }));
    out.push(...(res.Users ?? []).map((u) => u.Username));
    PaginationToken = res.PaginationToken;
  } while (PaginationToken);
  return out;
}

/**
 * elimina-utenti: toglie gli utenti di prova da Cognito. Le loro righe nelle tabelle restano: si
 * cancellano con l'ambiente (destroy). Serve solo per rifare il test con utenti "nuovi".
 */
async function eliminaUtenti() {
  const pool = env("USER_POOL_ID");
  const nomi = await utentiDiProva(pool);
  console.log(`  ${nomi.length} utenti di prova da eliminare`);
  await aGruppi(nomi, 5, (u) => cognito.send(new AdminDeleteUserCommand({ UserPoolId: pool, Username: u })));
}

/**
 * copia-banche: le banche dati pubblicate dell'ambiente di origine (di solito dev) e le loro
 * domande (partizione "bd#<id>" della tabella questions) vanno nelle tabelle di preprod. Così il
 * test usa anche le sessioni sulle banche dati ufficiali. L'origine si legge e basta.
 */
async function copiaBanche() {
  const da = JSON.parse(env("TABELLE_DA"));
  const a = JSON.parse(env("TABELLE_A"));
  const banche = [];
  let ExclusiveStartKey;
  do {
    const res = await db.send(
      new ScanCommand({ TableName: da.banche, FilterExpression: "stato = :p", ExpressionAttributeValues: { ":p": "pubblicata" }, ExclusiveStartKey }),
    );
    banche.push(...(res.Items ?? []));
    ExclusiveStartKey = res.LastEvaluatedKey;
  } while (ExclusiveStartKey);
  if (!banche.length) {
    console.log(`  nessuna banca dati pubblicata in ${da.banche}: niente da copiare`);
    return;
  }
  for (const banca of banche) {
    const domande = [];
    let start;
    do {
      const res = await db.send(
        new QueryCommand({ TableName: da.questions, KeyConditionExpression: "materia = :m", ExpressionAttributeValues: { ":m": `bd#${banca.id}` }, ExclusiveStartKey: start }),
      );
      domande.push(...(res.Items ?? []));
      start = res.LastEvaluatedKey;
    } while (start);
    // Prima le domande, poi la banca: una banca senza domande non deve mai comparire pubblicata.
    for (let i = 0; i < domande.length; i += 25) await scriviTutte(a.questions, domande.slice(i, i + 25));
    await db.send(new PutCommand({ TableName: a.banche, Item: banca }));
    console.log(`  ${banca.titolo ?? banca.id}: ${domande.length} domande`);
  }
}

/** BatchWrite di al massimo 25 righe, riprovando quelle che DynamoDB rimanda indietro. */
async function scriviTutte(tabella, righe) {
  let richieste = righe.map((Item) => ({ PutRequest: { Item } }));
  for (let tentativo = 0; richieste.length; tentativo++) {
    if (tentativo > 8) throw new Error(`${tabella}: scrittura non riuscita`);
    if (tentativo) await new Promise((r) => setTimeout(r, 200 * 2 ** tentativo));
    const res = await db.send(new BatchWriteCommand({ RequestItems: { [tabella]: richieste } }));
    richieste = res.UnprocessedItems?.[tabella] ?? [];
  }
}

const [comando, arg] = process.argv.slice(2);
const comandi = {
  utenti: () => utenti(Number(arg)),
  "elimina-utenti": eliminaUtenti,
  "copia-banche": copiaBanche,
};
if (!comandi[comando]) {
  console.error("uso: node scripts/carico/preprod.mjs utenti N | elimina-utenti | copia-banche");
  process.exit(2);
}
comandi[comando]().catch((err) => {
  console.error(`\nERRORE: ${err.name ?? ""} ${err.message}`);
  process.exit(1);
});
