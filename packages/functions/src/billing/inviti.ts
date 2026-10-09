import { AdminGetUserCommand } from "@aws-sdk/client-cognito-identity-provider";
import { GetCommand, PutCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { cognito, gruppiDi, userPoolId } from "@imieiconcorsi/core/cognito";
import { db, getProfilo, tables } from "@imieiconcorsi/core/db";
import {
  GIORNI_PREMIO_INVITO,
  GRUPPI,
  MAX_PREMI_INVITO_ANNO,
  PIANI,
  pianoDaGruppi,
  type CodiceInvito,
  type Profilo,
} from "@imieiconcorsi/core/domain";
import { inviaEmail } from "@imieiconcorsi/core/email";
import { dataIt } from "@imieiconcorsi/core/email-piani";
import { HttpError } from "@imieiconcorsi/core/http";
import { assegnaPiano } from "@imieiconcorsi/core/piani";
import { generaCodice, normalizzaCodice } from "@imieiconcorsi/core/sconti";

// "Invita un amico": ogni utente ha un codice (tabella codici, tipo invito). L'amico lo
// inserisce prima del suo primo acquisto; quando compra un piano, chi l'ha invitato riceve
// GIORNI_PREMIO_INVITO giorni gratis (Medium se era Free, altrimenti il suo piano si allunga).

const fallita = (err: unknown) => err instanceof Error && err.name === "ConditionalCheckFailedException";
const GIORNO = 86_400_000;

/** Un codice d'invito (undefined se non esiste o se è un codice sconto). */
async function leggiInvito(codice: string) {
  const res = await db.send(new GetCommand({ TableName: tables.codici, Key: { codice } }));
  const c = res.Item as CodiceInvito | undefined;
  return c?.tipo === "invito" ? c : undefined;
}

/** Il codice dell'utente, creato al primo bisogno (es. AMICO-K7MQ2XRT). */
export async function codiceDi(userId: string): Promise<CodiceInvito> {
  const profilo = await getProfilo(userId);
  if (profilo?.codiceInvito) {
    const c = await leggiInvito(profilo.codiceInvito);
    if (c) return c;
  }
  for (let tentativo = 0; tentativo < 5; tentativo++) {
    const c: CodiceInvito = {
      codice: `AMICO-${generaCodice().replace("-", "")}`,
      tipo: "invito",
      proprietario: userId,
      iscritti: 0,
      premi: 0,
      creatoIl: new Date().toISOString(),
    };
    try {
      await db.send(new PutCommand({ TableName: tables.codici, Item: c, ConditionExpression: "attribute_not_exists(codice)" }));
    } catch (err) {
      if (fallita(err)) continue;
      throw err;
    }
    try {
      await db.send(
        new UpdateCommand({
          TableName: tables.users,
          Key: { userId },
          UpdateExpression: "SET codiceInvito = :c",
          ConditionExpression: "attribute_exists(userId) AND attribute_not_exists(codiceInvito)",
          ExpressionAttributeValues: { ":c": c.codice },
        }),
      );
      return c;
    } catch (err) {
      // Due richieste insieme: vale il codice salvato per primo.
      if (fallita(err)) return codiceDi(userId);
      throw err;
    }
  }
  throw new HttpError(500, "Non riesco a creare il codice invito, riprova");
}

/** L'amico inserisce il codice: vale una volta, prima del suo primo acquisto, mai il proprio. */
export async function usaCodiceInvito(userId: string, inserito: string) {
  const c = await leggiInvito(normalizzaCodice(inserito));
  if (!c) throw new HttpError(400, "Codice invito non valido.", "CODICE_NON_VALIDO");
  if (c.proprietario === userId) throw new HttpError(400, "Questo è il tuo codice: va dato a un amico.", "CODICE_NON_VALIDO");
  try {
    await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId },
        UpdateExpression: "SET invitatoDa = :p",
        ConditionExpression: "attribute_exists(userId) AND attribute_not_exists(invitatoDa) AND attribute_not_exists(ultimoAcquisto)",
        ExpressionAttributeValues: { ":p": c.proprietario },
      }),
    );
  } catch (err) {
    if (fallita(err)) throw new HttpError(409, "Il codice invito si può inserire una sola volta, prima del primo acquisto.");
    throw err;
  }
  await db.send(
    new UpdateCommand({
      TableName: tables.codici,
      Key: { codice: c.codice },
      UpdateExpression: "SET iscritti = iscritti + :uno",
      ExpressionAttributeValues: { ":uno": 1 },
    }),
  );
}

/** Nuova scadenza: GIORNI_PREMIO_INVITO giorni in più, da oggi o dalla scadenza se è più avanti. */
export function scadenzaPremiata(scadenza: string | undefined, ora = new Date()) {
  const base = Math.max(ora.getTime(), scadenza ? Date.parse(scadenza) : 0);
  return new Date(base + GIORNI_PREMIO_INVITO * GIORNO).toISOString();
}

/**
 * Primo acquisto di un utente invitato: premio a chi l'ha invitato, una volta sola (il
 * segno invitoPremiato è condizionato). Errori nei log: l'acquisto resta valido comunque.
 */
export async function premiaChiHaInvitato(userId: string) {
  const amico = await getProfilo(userId);
  if (!amico?.invitatoDa || amico.invitoPremiato) return;
  try {
    await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId },
        UpdateExpression: "SET invitoPremiato = :o",
        ConditionExpression: "attribute_exists(invitatoDa) AND attribute_not_exists(invitoPremiato)",
        ExpressionAttributeValues: { ":o": new Date().toISOString() },
      }),
    );
  } catch (err) {
    if (fallita(err)) return;
    throw err;
  }

  const chi = await getProfilo(amico.invitatoDa);
  if (!chi?.username) return;
  const anno = String(new Date().getUTCFullYear());
  const premiAnno = chi.premiInvito?.anno === anno ? chi.premiInvito.n : 0;
  if (premiAnno >= MAX_PREMI_INVITO_ANNO) {
    console.log(`Invito: ${chi.userId} ha già ${premiAnno} premi quest'anno`);
    return;
  }

  const gruppi = await gruppiDi(chi.username);
  const piano = pianoDaGruppi(gruppi.filter((g) => g !== GRUPPI.admin));
  let pianoFinale = piano;
  let scadenza: string | undefined;
  if (gruppi.includes(GRUPPI.admin)) {
    // L'admin ha già tutto: si conta il premio, senza cambiare nulla.
  } else if (piano === "free") {
    pianoFinale = "medium";
    scadenza = scadenzaPremiata(undefined);
    await assegnaPiano({ userId: chi.userId, username: chi.username, piano: "medium", periodo: "mensile", scadenza });
  } else if (chi.scadenzaPiano) {
    scadenza = scadenzaPremiata(chi.scadenzaPiano);
    await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: chi.userId },
        UpdateExpression: "SET scadenzaPiano = :s REMOVE promemoriaInviatoPer",
        ExpressionAttributeValues: { ":s": scadenza },
      }),
    );
  }

  await db.send(
    new UpdateCommand({
      TableName: tables.users,
      Key: { userId: chi.userId },
      UpdateExpression: "SET premiInvito = :p",
      ExpressionAttributeValues: { ":p": { anno, n: premiAnno + 1 } },
    }),
  );
  if (chi.codiceInvito) {
    await db.send(
      new UpdateCommand({
        TableName: tables.codici,
        Key: { codice: chi.codiceInvito },
        UpdateExpression: "SET premi = premi + :uno",
        ExpressionAttributeValues: { ":uno": 1 },
      }),
    );
  }
  if (scadenza) await emailPremio(chi, pianoFinale, scadenza);
}

/** Email a chi ha invitato: il premio è arrivato, con il piano e la nuova scadenza. */
async function emailPremio(chi: Profilo, piano: "medium" | "pro" | "free", scadenza: string) {
  try {
    const u = await cognito.send(new AdminGetUserCommand({ UserPoolId: userPoolId(), Username: chi.username }));
    const attr = (n: string) => u.UserAttributes?.find((a) => a.Name === n)?.Value;
    const email = attr("email");
    if (!email) return;
    const nome = attr("name");
    await inviaEmail({
      a: email,
      oggetto: `Hai ${GIORNI_PREMIO_INVITO} giorni gratis: il tuo amico si è abbonato`,
      testo: [
        `Ciao${nome ? ` ${nome}` : ""},`,
        "",
        `un amico che hai invitato ha appena comprato un piano su iMieiConcorsi: grazie!`,
        `Come promesso, hai ${GIORNI_PREMIO_INVITO} giorni gratis: il tuo piano ${PIANI[piano].nome} vale fino al ${dataIt(scadenza)}.`,
        "",
        `Invita altri amici dal tuo profilo: ${process.env.SITE_URL ?? ""}/app/profilo`,
        "",
        "Il team di iMieiConcorsi",
      ].join("\n"),
    });
  } catch (err) {
    console.error("Email del premio invito non inviata", err);
  }
}
