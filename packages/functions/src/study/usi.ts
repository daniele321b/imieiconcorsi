import { UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { db, getProfilo, tables } from "@imieiconcorsi/core/db";
import { HttpError, type Ctx } from "@imieiconcorsi/core/http";

// Utilizzi delle banche dati ufficiali nel piano Free (USI_BANCHE_DATI_FREE a settimana).
// Un utilizzo = una sessione di studio o simulazione su una banca dati, oppure la prima
// consultazione di una banca dati nella settimana (poi sfogliarla di nuovo non costa).
// Contatore sul profilo: usiBancheDati = { settimana, usi, aperte: [id banca] }.

/** Lunedì della settimana in corso (UTC), YYYY-MM-DD: a settimana nuova si riparte. */
export function settimanaDi(ora = new Date()) {
  const d = new Date(Date.UTC(ora.getUTCFullYear(), ora.getUTCMonth(), ora.getUTCDate()));
  d.setUTCDate(d.getUTCDate() - ((d.getUTCDay() + 6) % 7));
  return d.toISOString().slice(0, 10);
}

/** Contatore sul profilo: settimana (lunedì), utilizzi fatti, banche già aperte in consultazione. */
export interface UsiBancheDati {
  settimana: string;
  usi: number;
  aperte?: string[];
}

/** Il contatore di questa settimana: se è di una settimana passata, riparte da zero. */
export const usiDellaSettimana = (u: UsiBancheDati | undefined, ora = new Date()) =>
  u?.settimana === settimanaDi(ora) ? u : { settimana: settimanaDi(ora), usi: 0, aperte: [] };

/** Quanti utilizzi restano questa settimana; null = illimitati. */
export async function statoUsi(ctx: Ctx) {
  const limite = ctx.limiti.usiBancheDatiSettimana;
  if (limite === null) return null;
  const profilo = await getProfilo(ctx.userId);
  const u = usiDellaSettimana(profilo?.usiBancheDati);
  return { limite, usati: u.usi, restanti: Math.max(0, limite - u.usi), aperte: u.aperte ?? [] };
}

const fallita = (err: unknown) => err instanceof Error && err.name === "ConditionalCheckFailedException";

/** Errore mostrato quando gli utilizzi gratuiti della settimana sono finiti. */
const limiteRaggiunto = (limite: number) =>
  new HttpError(
    403,
    `Hai usato i ${limite} utilizzi gratuiti delle banche dati di questa settimana: ripartono lunedì. Con Medium e Pro sono illimitati.`,
    "LIMITE_PIANO",
  );

/**
 * Scala un utilizzo (piano Free). Con `bancaDaSfogliare` la consultazione costa solo la prima
 * volta nella settimana. Gli aggiornamenti sono condizionati: due richieste insieme non sforano.
 */
export async function consumaUso(ctx: Ctx, bancaDaSfogliare?: string) {
  const limite = ctx.limiti.usiBancheDatiSettimana;
  if (limite === null) return;
  const settimana = settimanaDi();

  if (bancaDaSfogliare) {
    const profilo = await getProfilo(ctx.userId);
    const u = usiDellaSettimana(profilo?.usiBancheDati);
    if (u.aperte?.includes(bancaDaSfogliare)) return;
  }
  const aperte = bancaDaSfogliare ? [bancaDaSfogliare] : [];

  try {
    // Stessa settimana: un utilizzo in più, se ce n'è ancora.
    await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: ctx.userId },
        UpdateExpression: "SET usiBancheDati.usi = usiBancheDati.usi + :uno, usiBancheDati.aperte = list_append(if_not_exists(usiBancheDati.aperte, :vuota), :aperte)",
        ConditionExpression: "usiBancheDati.settimana = :w AND usiBancheDati.usi < :max",
        ExpressionAttributeValues: { ":uno": 1, ":vuota": [], ":aperte": aperte, ":w": settimana, ":max": limite },
      }),
    );
    return;
  } catch (err) {
    if (!fallita(err)) throw err;
  }
  try {
    // Prima volta nella settimana.
    await db.send(
      new UpdateCommand({
        TableName: tables.users,
        Key: { userId: ctx.userId },
        UpdateExpression: "SET usiBancheDati = :u",
        ConditionExpression: "attribute_exists(userId) AND (attribute_not_exists(usiBancheDati) OR usiBancheDati.settimana <> :w)",
        ExpressionAttributeValues: { ":u": { settimana, usi: 1, aperte }, ":w": settimana },
      }),
    );
  } catch (err) {
    if (fallita(err)) throw limiteRaggiunto(limite);
    throw err;
  }
}
