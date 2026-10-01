import { UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { attributo, utentiNelGruppo } from "@imieiconcorsi/core/cognito";
import { batchGet, db, tables } from "@imieiconcorsi/core/db";
import { GRUPPI, PIANI, type Profilo } from "@imieiconcorsi/core/domain";
import { inviaEmail } from "@imieiconcorsi/core/email";
import { env } from "@imieiconcorsi/core/env";
import { assegnaPiano } from "@imieiconcorsi/core/piani";
import { azionePerAbbonato } from "./scadenze-logic";

// Ogni mattina: chi ha il piano scaduto torna Free, chi scade entro 3 giorni riceve un'email.

const dataIt = (iso: string) =>
  new Intl.DateTimeFormat("it-IT", { day: "numeric", month: "long", year: "numeric", timeZone: "Europe/Rome" }).format(
    new Date(iso),
  );

export const handler = async () => {
  const conteggi = { scaduti: 0, promemoria: 0, errori: 0 };

  for (const gruppo of [GRUPPI.medium, GRUPPI.pro] as const) {
    const abbonati = [];
    for await (const u of utentiNelGruppo(gruppo)) abbonati.push(u);
    const profili = await batchGet<Profilo>(
      tables.users,
      abbonati.map((u) => ({ userId: attributo(u, "sub") })),
    );
    const profiloDi = new Map(profili.map((p) => [p.userId, p]));

    for (const u of abbonati) {
      const sub = attributo(u, "sub")!;
      const profilo = profiloDi.get(sub);
      const azione = azionePerAbbonato(profilo?.scadenzaPiano, profilo?.promemoriaInviatoPer);
      try {
        if (azione === "scaduto") {
          await assegnaPiano({ userId: sub, username: u.Username!, piano: "free", scadenza: null });
          conteggi.scaduti++;
        } else if (azione === "promemoria") {
          const email = attributo(u, "email");
          if (email) {
            const nome = attributo(u, "name");
            await inviaEmail({
              a: email,
              oggetto: `Il tuo piano ${PIANI[gruppo].nome} scade il ${dataIt(profilo!.scadenzaPiano!)}`,
              testo: [
                `Ciao${nome ? ` ${nome}` : ""},`,
                "",
                `il tuo piano ${PIANI[gruppo].nome} su iMieiConcorsi scade il ${dataIt(profilo!.scadenzaPiano!)}.`,
                "Dopo quella data il tuo account torna al piano Free: i tuoi progressi restano salvati.",
                "",
                `Per rinnovarlo: ${env("SITE_URL")}/app/piani`,
                "",
                "Il team di iMieiConcorsi",
              ].join("\n"),
            });
          }
          await db.send(
            new UpdateCommand({
              TableName: tables.users,
              Key: { userId: sub },
              UpdateExpression: "SET promemoriaInviatoPer = :s",
              ExpressionAttributeValues: { ":s": profilo!.scadenzaPiano },
            }),
          );
          conteggi.promemoria++;
        }
      } catch (err) {
        // Un utente che fallisce non blocca gli altri: si riprova domani.
        conteggi.errori++;
        console.error(`Scadenze: errore su ${u.Username}`, err);
      }
    }
  }

  console.log("Scadenze piani", conteggi);
  if (conteggi.errori) throw new Error(`${conteggi.errori} utenti non elaborati`);
  return conteggi;
};
