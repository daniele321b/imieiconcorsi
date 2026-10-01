import { SendEmailCommand, SESv2Client } from "@aws-sdk/client-sesv2";
import { env } from "./env";

const ses = new SESv2Client({});

/**
 * Email transazionale con SES (identità e configuration set dall'ambiente "shared").
 * In sandbox SES consegna solo agli indirizzi verificati.
 */
export async function inviaEmail({ a, oggetto, testo }: { a: string | string[]; oggetto: string; testo: string }) {
  await ses.send(
    new SendEmailCommand({
      FromEmailAddress: `iMieiConcorsi <${env("SES_SENDER")}>`,
      Destination: { ToAddresses: Array.isArray(a) ? a : [a] },
      ConfigurationSetName: env("SES_CONFIGURATION_SET"),
      Content: {
        Simple: {
          Subject: { Data: oggetto, Charset: "UTF-8" },
          Body: { Text: { Data: testo, Charset: "UTF-8" } },
        },
      },
    }),
  );
}

/** Avviso all'amministratore (ADMIN_EMAIL). Senza indirizzo configurato scrive solo nei log. */
export async function avvisaAdmin(oggetto: string, testo: string) {
  const admin = process.env.ADMIN_EMAIL;
  if (!admin) {
    console.warn(`ADMIN_EMAIL non impostato, avviso non inviato: ${oggetto}`);
    return;
  }
  await inviaEmail({ a: admin, oggetto: `[admin] ${oggetto}`, testo });
}
