import { AdminGetUserCommand } from "@aws-sdk/client-cognito-identity-provider";
import { GetCommand, PutCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { cognito, userPoolId } from "@imieiconcorsi/core/cognito";
import { db, tables } from "@imieiconcorsi/core/db";
import { PIANI, VERSIONE_TERMINI, type Periodo } from "@imieiconcorsi/core/domain";
import { inviaEmail } from "@imieiconcorsi/core/email";
import { dataIt } from "@imieiconcorsi/core/email-piani";
import { assegnaPiano, scadenzaDa } from "@imieiconcorsi/core/piani";

// Ordini dei piani a pagamento (tabella ordini). Niente dati personali: email e nome stanno
// in Cognito e si leggono al momento della conferma. Il piano si attiva solo da qui.

export type StatoOrdine = "in-attesa" | "pagato" | "scaduto" | "fallito";

export interface Ordine {
  /** Codice anonimo, anche su Stripe (client_reference_id) */
  id: string;
  userId: string;
  username: string;
  piano: "medium" | "pro";
  periodo: Periodo;
  /** Prezzo di listino e importo pagato, in euro */
  prezzo: number;
  importo: number;
  codiceSconto?: string;
  percentualeSconto?: number;
  stato: StatoOrdine;
  stripeSessionId?: string;
  /** Consenso all'esecuzione immediata con rinuncia al recesso, dato prima del pagamento */
  consenso: { rinunciaRecesso: true; versioneTermini: string; il: string };
  creatoIl: string;
  aggiornatoIl: string;
  pagatoIl?: string;
  scadenzaPiano?: string;
}

const euro = (n: number) => n.toLocaleString("it-IT", { style: "currency", currency: "EUR" });

export async function salvaOrdine(o: Ordine) {
  await db.send(new PutCommand({ TableName: tables.ordini, Item: o }));
}

export async function leggiOrdine(id: string) {
  const res = await db.send(new GetCommand({ TableName: tables.ordini, Key: { id } }));
  return res.Item as Ordine | undefined;
}

/** Chiude un ordine non pagato (sessione scaduta o pagamento fallito), solo se era in attesa. */
export async function chiudiOrdine(id: string, stato: "scaduto" | "fallito") {
  try {
    await db.send(
      new UpdateCommand({
        TableName: tables.ordini,
        Key: { id },
        UpdateExpression: "SET stato = :s, aggiornatoIl = :ora",
        ConditionExpression: "stato = :attesa",
        ExpressionAttributeValues: { ":s": stato, ":attesa": "in-attesa", ":ora": new Date().toISOString() },
      }),
    );
  } catch (err) {
    if (!(err instanceof Error && err.name === "ConditionalCheckFailedException")) throw err;
  }
}

/**
 * Pagamento confermato: attiva il piano UNA volta sola, anche se arrivano insieme il webhook
 * di Stripe e la pagina di ritorno (il passaggio "in-attesa" → "pagato" è condizionato).
 * Restituisce l'ordine aggiornato.
 */
export async function completaOrdine(id: string): Promise<Ordine | undefined> {
  const ora = new Date().toISOString();
  let ordine: Ordine;
  try {
    const res = await db.send(
      new UpdateCommand({
        TableName: tables.ordini,
        Key: { id },
        UpdateExpression: "SET stato = :pagato, pagatoIl = :ora, aggiornatoIl = :ora",
        ConditionExpression: "stato = :attesa OR stato = :scaduto",
        ExpressionAttributeValues: { ":pagato": "pagato", ":attesa": "in-attesa", ":scaduto": "scaduto", ":ora": ora },
        ReturnValues: "ALL_NEW",
      }),
    );
    ordine = res.Attributes as Ordine;
  } catch (err) {
    // Già completato (o mai esistito): niente da fare.
    if (err instanceof Error && err.name === "ConditionalCheckFailedException") return leggiOrdine(id);
    throw err;
  }

  const scadenza = scadenzaDa(ordine.periodo);
  await assegnaPiano({ userId: ordine.userId, username: ordine.username, piano: ordine.piano, periodo: ordine.periodo, scadenza });

  // Prova del consenso + codice sconto usato (vale una volta per utente).
  await db.send(
    new UpdateCommand({
      TableName: tables.users,
      Key: { userId: ordine.userId },
      UpdateExpression: ordine.codiceSconto
        ? "SET ultimoAcquisto = :a, codiciUsati = list_append(if_not_exists(codiciUsati, :vuota), :c)"
        : "SET ultimoAcquisto = :a",
      ExpressionAttributeValues: {
        ":a": {
          piano: ordine.piano,
          periodo: ordine.periodo,
          il: ora,
          rinunciaRecesso: true,
          versioneTermini: ordine.consenso.versioneTermini,
          importo: ordine.importo,
          ordine: ordine.id,
          ...(ordine.codiceSconto ? { codiceSconto: ordine.codiceSconto } : {}),
        },
        ...(ordine.codiceSconto ? { ":vuota": [], ":c": [ordine.codiceSconto] } : {}),
      },
    }),
  );
  await db.send(
    new UpdateCommand({
      TableName: tables.ordini,
      Key: { id },
      UpdateExpression: "SET scadenzaPiano = :s",
      ExpressionAttributeValues: { ":s": scadenza },
    }),
  );

  if (ordine.codiceSconto) {
    // Il pagamento c'è già stato: se nel frattempo il codice si è esaurito, il piano resta valido.
    await db
      .send(
        new UpdateCommand({
          TableName: tables.codici,
          Key: { codice: ordine.codiceSconto },
          UpdateExpression: "SET usi = usi + :uno",
          ExpressionAttributeValues: { ":uno": 1 },
        }),
      )
      .catch((err) => console.error(`Uso del codice ${ordine.codiceSconto} non conteggiato`, err));
  }

  await inviaConferma(ordine, scadenza);
  return { ...ordine, scadenzaPiano: scadenza };
}

/**
 * Conferma dell'acquisto su supporto durevole (art. 51, c. 7, Codice del consumo): riepilogo e
 * consenso all'esecuzione immediata con rinuncia al recesso. Se l'email non parte l'acquisto
 * resta valido: l'errore finisce nei log.
 */
export async function inviaConferma(o: Ordine, scadenza: string) {
  try {
    const utente = await cognito.send(new AdminGetUserCommand({ UserPoolId: userPoolId(), Username: o.username }));
    const email = utente.UserAttributes?.find((a) => a.Name === "email")?.Value;
    if (!email) return;
    const p = PIANI[o.piano];
    await inviaEmail({
      a: email,
      oggetto: `Conferma acquisto: piano ${p.nome} ${o.periodo}`,
      testo: [
        "Grazie per il tuo acquisto su iMieiConcorsi.",
        "",
        `Ordine: ${o.id}`,
        `Piano: ${p.nome} (${o.periodo})`,
        o.codiceSconto
          ? `Importo: ${euro(o.importo)} IVA inclusa (prezzo ${euro(o.prezzo)}, sconto del ${o.percentualeSconto}% con il codice ${o.codiceSconto})`
          : `Importo: ${euro(o.importo)} IVA inclusa`,
        `Valido fino al: ${dataIt(scadenza)}`,
        "",
        "Pagamento unico: il piano NON si rinnova automaticamente. Ti avviseremo 3 giorni prima della scadenza.",
        "",
        "Hai chiesto di accedere subito ai contenuti del piano e hai preso atto che, per questo, perdi il diritto",
        "di recesso (art. 59, comma 1, lettera o, D.Lgs. 206/2005). Il pagamento non è rimborsabile, salvo i casi",
        `previsti dalla legge. Termini e condizioni, versione ${VERSIONE_TERMINI}: ${process.env.SITE_URL ?? ""}/termini`,
        "",
        "Il team di iMieiConcorsi",
      ].join("\n"),
    });
  } catch (err) {
    console.error("Email di conferma acquisto non inviata", err);
  }
}
