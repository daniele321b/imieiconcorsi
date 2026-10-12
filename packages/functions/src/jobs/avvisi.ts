import { AdminGetUserCommand } from "@aws-sdk/client-cognito-identity-provider";
import { QueryCommand, ScanCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { cognito, userPoolId } from "@imieiconcorsi/core/cognito";
import { nomeConcorso, scadenzaVera } from "@imieiconcorsi/core/concorsi";
import { db, tables } from "@imieiconcorsi/core/db";
import { linkDisiscrizione, linkLettura } from "@imieiconcorsi/core/disiscrizione";
import { COMPARTO_IDS, type CompartoId, type Concorso, type Profilo } from "@imieiconcorsi/core/domain";
import { inviaEmail } from "@imieiconcorsi/core/email";
import { dataIt } from "@imieiconcorsi/core/email-piani";
import { env } from "@imieiconcorsi/core/env";
import { bandiNuovi, deveAvvisare, frequenzaEffettiva } from "./avvisi-logic";

// Ogni mattina alle 7, dopo l'import dei bandi: a chi ha scelto gli avvisi arrivano i bandi
// dei suoi comparti usciti su inPA ieri (ogni giorno) o nell'ultima settimana (il lunedì).
// Solo a chi li legge: chi non ne apre nessuno per un po' passa al lunedì, poi gli avvisi si
// sospendono finché non apre un'email, clicca un link o torna nell'app (frequenzaEffettiva).

/** Bandi elencati al massimo in un'email (poi il link alla ricerca). */
const MAX_NELL_EMAIL = 20;

/** I campi del profilo che servono per decidere e scrivere l'avviso. */
type Iscritto = Pick<Profilo, "userId" | "username" | "avvisi" | "interessi" | "onboarded" | "ultimoAvvisoIl" | "avvisiNonAperti">;

/** Utenti con gli avvisi attivi e il profilo completato (Scan della tabella users). */
async function iscritti() {
  const out: Iscritto[] = [];
  let ExclusiveStartKey: Record<string, unknown> | undefined;
  do {
    const res = await db.send(
      new ScanCommand({
        TableName: tables.users,
        ProjectionExpression: "userId, username, avvisi, interessi, onboarded, ultimoAvvisoIl, avvisiNonAperti",
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

/** Testo sicuro dentro l'HTML dell'email. */
const escape = (t: string) => t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

/** Riga di dettaglio di un bando: ente, posti, scadenza. */
function righeBando(c: Concorso) {
  return [c.ente, c.posti ? `${c.posti} ${c.posti === 1 ? "posto" : "posti"}` : "", scadenzaVera(c.scadenza) ? `scade il ${dataIt(c.scadenza!)}` : "senza scadenza"]
    .filter(Boolean)
    .join(" · ");
}

/** Prima frase dell'email: quanti bandi e in che periodo. */
function intro(bandi: Concorso[], settimanale: boolean) {
  return `${settimanale ? "negli ultimi 7 giorni" : "ieri"} ${bandi.length === 1 ? "è uscito 1 bando" : `sono usciti ${bandi.length} bandi`} su inPA nei comparti che segui:`;
}

/** Versione solo testo dell'email (per i programmi di posta che non mostrano l'HTML). */
function testoEmail(nome: string | undefined, bandi: Concorso[], settimanale: boolean, disiscrizione: string) {
  const sito = env("SITE_URL");
  const righe = bandi.slice(0, MAX_NELL_EMAIL).map((c) => `- ${nomeConcorso(c)}\n  ${righeBando(c)}\n  ${sito}/app/concorsi/${c.id}`);
  if (bandi.length > MAX_NELL_EMAIL) righe.push(`… e altri ${bandi.length - MAX_NELL_EMAIL}: ${sito}/app/concorsi`);
  return [
    `Ciao${nome ? ` ${nome}` : ""},`,
    "",
    intro(bandi, settimanale),
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

/** Versione HTML: i link passano dall'API (lettura registrata) e un'immagine invisibile segna l'apertura. */
function htmlEmail(nome: string | undefined, bandi: Concorso[], settimanale: boolean, disiscrizione: string, lettura: ReturnType<typeof linkLettura>) {
  const p = (t: string) => `<p style="margin:0 0 12px">${t}</p>`;
  const voci = bandi
    .slice(0, MAX_NELL_EMAIL)
    .map(
      (c) =>
        `<li style="margin:0 0 12px"><a href="${escape(lettura.clic(`/app/concorsi/${c.id}`))}" style="color:#4338ca;font-weight:600">${escape(nomeConcorso(c))}</a><br><span style="color:#64748b">${escape(righeBando(c))}</span></li>`,
    )
    .join("");
  const altri = bandi.length > MAX_NELL_EMAIL ? p(`<a href="${escape(lettura.clic("/app/concorsi"))}">… e altri ${bandi.length - MAX_NELL_EMAIL}</a>`) : "";
  return [
    '<div style="font-family:Arial,sans-serif;font-size:15px;line-height:1.5;color:#0f172a;max-width:560px">',
    p(`Ciao${nome ? ` ${escape(nome)}` : ""},`),
    p(intro(bandi, settimanale)),
    `<ul style="padding-left:20px;margin:0 0 12px">${voci}</ul>`,
    altri,
    `<p style="margin:16px 0 4px;font-size:13px;color:#64748b">Ricevi questa email perché hai attivato gli avvisi sui nuovi bandi. <a href="${escape(lettura.clic("/app/profilo"))}">Comparti e frequenza</a> · <a href="${escape(disiscrizione)}">Non ricevere più avvisi</a></p>`,
    `<img src="${escape(lettura.immagine)}" width="1" height="1" alt="" style="display:block;border:0">`,
    "</div>",
  ].join("");
}

/** Entrata del job: per ogni iscritto decide se scrivere, con quali bandi, e registra l'invio. */
export const handler = async () => {
  const conteggi = { email: 0, senzaNovita: 0, inPausa: 0, errori: 0 };
  const bandiDi = bandiPerComparto();
  const ora = new Date();

  for (const u of await iscritti()) {
    if (!u.onboarded || !u.avvisi || u.avvisi === "mai") continue;
    const frequenza = frequenzaEffettiva(u.avvisi, u.avvisiNonAperti);
    if (frequenza === "pausa") {
      conteggi.inPausa++;
      continue;
    }
    if (!deveAvvisare(frequenza, u.ultimoAvvisoIl, ora)) continue;
    try {
      const comparti = u.interessi?.length ? u.interessi : [...COMPARTO_IDS];
      const tutti = (await Promise.all(comparti.map(bandiDi))).flat();
      const nuovi = bandiNuovi(tutti, frequenza, ora);
      let mandata = false;

      if (nuovi.length) {
        const utente = await cognito.send(new AdminGetUserCommand({ UserPoolId: userPoolId(), Username: u.username }));
        const attr = (n: string) => utente.UserAttributes?.find((a) => a.Name === n)?.Value;
        const email = attr("email");
        if (utente.Enabled !== false && email) {
          const disiscrizione = linkDisiscrizione(u.userId, env("SITE_URL"));
          const settimanale = frequenza === "settimanale";
          await inviaEmail({
            a: email,
            oggetto: nuovi.length === 1 ? "1 nuovo bando per te" : `${nuovi.length} nuovi bandi per te`,
            testo: testoEmail(attr("name"), nuovi, settimanale, disiscrizione.pagina),
            html: htmlEmail(attr("name"), nuovi, settimanale, disiscrizione.pagina, linkLettura(u.userId, env("SITE_URL"))),
            intestazioni: disiscrizione.intestazioni,
          });
          conteggi.email++;
          mandata = true;
        }
      } else {
        conteggi.senzaNovita++;
      }
      // Segna il giorno anche senza novità: se il job viene rilanciato oggi non manda doppioni.
      await db.send(
        new UpdateCommand({
          TableName: tables.users,
          Key: { userId: u.userId },
          // Un avviso in più non ancora aperto: si azzera quando la persona lo legge o usa l'app.
          UpdateExpression: mandata ? "SET ultimoAvvisoIl = :o ADD avvisiNonAperti :uno" : "SET ultimoAvvisoIl = :o",
          ExpressionAttributeValues: { ":o": ora.toISOString(), ...(mandata ? { ":uno": 1 } : {}) },
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
