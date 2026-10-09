import { SendEmailCommand, SESv2Client } from "@aws-sdk/client-sesv2";
import { env } from "./env";

// Invio delle email con Amazon SES. Mittente e "configuration set" (che registra consegne,
// rimbalzi e segnalazioni di spam) arrivano da Terraform (local.email_env). Lo usano tutte le
// Lambda che scrivono agli utenti o all'amministratore; serve il permesso local.invia_email.

const ses = new SESv2Client({});

/**
 * Email transazionale con SES (identità e configuration set dall'ambiente "shared").
 * In sandbox SES consegna solo agli indirizzi verificati.
 */
export async function inviaEmail({
  a,
  oggetto,
  testo,
  html,
  intestazioni,
}: {
  a: string | string[];
  oggetto: string;
  testo: string;
  /** Versione HTML (facoltativa): i programmi di posta mostrano questa, il testo resta per gli altri */
  html?: string;
  /** Intestazioni in più, es. List-Unsubscribe */
  intestazioni?: { Name: string; Value: string }[];
}) {
  await ses.send(
    new SendEmailCommand({
      FromEmailAddress: `iMieiConcorsi <${env("SES_SENDER")}>`,
      Destination: { ToAddresses: Array.isArray(a) ? a : [a] },
      ConfigurationSetName: env("SES_CONFIGURATION_SET"),
      Content: {
        Simple: {
          Subject: { Data: `${process.env.EMAIL_SUBJECT_PREFIX ?? ""}${oggetto}`, Charset: "UTF-8" },
          Body: { Text: { Data: testo, Charset: "UTF-8" }, ...(html ? { Html: { Data: html, Charset: "UTF-8" } } : {}) },
          ...(intestazioni?.length ? { Headers: intestazioni } : {}),
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
