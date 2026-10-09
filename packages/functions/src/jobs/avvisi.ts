import { AdminGetUserCommand } from "@aws-sdk/client-cognito-identity-provider";
import { QueryCommand, ScanCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { cognito, userPoolId } from "@imieiconcorsi/core/cognito";
import { db, tables } from "@imieiconcorsi/core/db";
import { linkDisiscrizione } from "@imieiconcorsi/core/disiscrizione";
import { COMPARTO_IDS, type CompartoId, type Concorso, type Profilo } from "@imieiconcorsi/core/domain";
import { inviaEmail } from "@imieiconcorsi/core/email";
import { dataIt } from "@imieiconcorsi/core/email-piani";
import { env } from "@imieiconcorsi/core/env";
import { bandiNuovi, deveAvvisare } from "./avvisi-logic";

// Ogni mattina alle 7, dopo l'import dei bandi: a chi ha scelto gli avvisi arrivano i bandi
// dei suoi comparti usciti su inPA ieri (ogni giorno) o nell'ultima settimana (il lunedì).

const MAX_NELL_EMAIL = 20;

type Iscritto = Pick<Profilo, "userId" | "username" | "avvisi" | "interessi" | "onboarded" | "ultimoAvvisoIl">;

async function iscritti() {
  const out: Iscritto[] = [];
  let ExclusiveStartKey: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new ScanCommand({
        TableName: tables.users,
        ProjectionExpression: "userId, username, avvisi, interessi, onboarded, ultimoAvvisoIl",
        ExclusiveStartKey,
      }),
    );
    out.push(...((res.Items ?? []) as Iscritto[]));
    ExclusiveStartKey = res.LastEvaluatedKey;
  } while (ExclusiveStartKey);
  return out;
}

/** Bandi aperti di un comparto, letti una volta sola per tutti gli utenti. */
function bandiPerComparto() {
  const cache = new Map<CompartoId, Promise<Concorso[]>>();
  return (comparto: CompartoId) => {
    if (!cache.has(comparto)) {
      cache.set(
        comparto,
        db
          .send(
            new QueryCommand({
              TableName: tables.concorsi,
              IndexName: "byComparto",
              KeyConditionExpression: "comparto = :c AND scadenza >= :oggi",
              ExpressionAttributeValues: { ":c": comparto, ":oggi": new Date().toISOString() },
            }),
          )
          .then((r) => (r.Items ?? []) as Concorso[]),
      );
    }
    return cache.get(comparto)!;
  };
}

function testoEmail(nome: string | undefined, bandi: Concorso[], settimanale: boolean, disiscrizione: string) {
  const sito = env("SITE_URL");
  const righe = bandi.slice(0, MAX_NELL_EMAIL).map((c) => {
    const dettagli = [c.ente, c.posti ? `${c.posti} ${c.posti === 1 ? "posto" : "posti"}` : "", c.scadenza ? `scade il ${dataIt(c.scadenza)}` : ""]
      .filter(Boolean)
      .join(" · ");
    return `- ${c.figura ?? c.titolo}\n  ${dettagli}\n  ${sito}/app/concorsi/${c.id}`;
  });
  if (bandi.length > MAX_NELL_EMAIL) righe.push(`… e altri ${bandi.length - MAX_NELL_EMAIL}: ${sito}/app/concorsi`);
  return [
    `Ciao${nome ? ` ${nome}` : ""},`,
    "",
    `${settimanale ? "negli ultimi 7 giorni" : "ieri"} ${bandi.length === 1 ? "è uscito 1 bando" : `sono usciti ${bandi.length} bandi`} su inPA nei comparti che segui:`,
    "",
    ...righe,
    "",
    "Ricevi questa email perché hai attivato gli avvisi sui nuovi bandi su iMieiConcorsi.",
    `Comparti e frequenza si cambiano dal profilo: ${sito}/app/profilo`,
    `Per non ricevere più questi avvisi (un clic, senza accedere): ${disiscrizione}`,
    "",
    "Il team di iMieiConcorsi",
  ].join("\n");
}

export const handler = async () => {
  const conteggi = { email: 0, senzaNovita: 0, errori: 0 };
  const bandiDi = bandiPerComparto();
  const ora = new Date();

  for (const u of await iscritti()) {
    if (!u.onboarded || !u.avvisi || u.avvisi === "mai" || !deveAvvisare(u.avvisi, u.ultimoAvvisoIl, ora)) continue;
    try {
      const comparti = u.interessi?.length ? u.interessi : [...COMPARTO_IDS];
      const tutti = (await Promise.all(comparti.map(bandiDi))).flat();
      const nuovi = bandiNuovi(tutti, u.avvisi, ora);

      if (nuovi.length) {
        const utente = await cognito.send(new AdminGetUserCommand({ UserPoolId: userPoolId(), Username: u.username }));
        const attr = (n: string) => utente.UserAttributes?.find((a) => a.Name === n)?.Value;
        const email = attr("email");
        if (utente.Enabled !== false && email) {
          const disiscrizione = linkDisiscrizione(u.userId, env("SITE_URL"));
          await inviaEmail({
            a: email,
            oggetto: nuovi.length === 1 ? "1 nuovo bando per te" : `${nuovi.length} nuovi bandi per te`,
            testo: testoEmail(attr("name"), nuovi, u.avvisi === "settimanale", disiscrizione.pagina),
            intestazioni: disiscrizione.intestazioni,
          });
          conteggi.email++;
        }
      } else {
        conteggi.senzaNovita++;
      }
      // Segna il giorno anche senza novità: se il job viene rilanciato oggi non manda doppioni.
      await db.send(
        new UpdateCommand({
          TableName: tables.users,
          Key: { userId: u.userId },
          UpdateExpression: "SET ultimoAvvisoIl = :o",
          ExpressionAttributeValues: { ":o": ora.toISOString() },
        }),
      );
    } catch (err) {
      conteggi.errori++;
      console.error(`Avvisi: errore su ${u.username}`, err);
    }
  }

  console.log("Avvisi nuovi bandi", conteggi);
  if (conteggi.errori) throw new Error(`${conteggi.errori} utenti non elaborati`);
  return conteggi;
};
