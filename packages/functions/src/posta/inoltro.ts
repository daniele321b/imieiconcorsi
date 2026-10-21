import { GetObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { SendEmailCommand, SESv2Client } from "@aws-sdk/client-sesv2";
import type { SESEvent } from "aws-lambda";
import { motivoScarto, preparaInoltro } from "./logic";

// Lambda "inoltro-posta" (ambiente shared, modules/posta-in-arrivo): SES riceve la posta per
// info@<dominio> e gli altri alias, la salva nel bucket S3 della posta e chiama questa funzione,
// che la rimanda all'indirizzo vero dell'admin (variabile INOLTRI: {"info@…": "admin@…"}).
// Il mittente viene riscritto sul nostro indirizzo e "Rispondi" va al mittente vero (logic.ts).

const s3 = new S3Client({});
const ses = new SESv2Client({});

/** Alias → indirizzo a cui inoltrare, da Terraform (JSON). */
const inoltri = (): Record<string, string> => JSON.parse(process.env.INOLTRI ?? "{}");

/**
 * Il messaggio grezzo che SES ha salvato nel bucket (chiave = prefisso + id del messaggio), come
 * stringa "latin1": un carattere per byte, così corpo e allegati in qualsiasi codifica restano identici.
 */
async function leggiMessaggio(messageId: string): Promise<string> {
  const res = await s3.send(new GetObjectCommand({ Bucket: process.env.POSTA_BUCKET, Key: `${process.env.POSTA_PREFISSO ?? ""}${messageId}` }));
  return Buffer.from(await res.Body!.transformToByteArray()).toString("latin1");
}

/** Entrata: un evento SES per messaggio ricevuto; inoltra una copia per ogni alias destinatario. */
export const handler = async (event: SESEvent) => {
  const mappa = inoltri();
  for (const record of event.Records) {
    const { mail, receipt } = record.ses;
    const scarto = motivoScarto({ virus: receipt.virusVerdict?.status, spam: receipt.spamVerdict?.status });
    if (scarto) {
      console.log(`Messaggio ${mail.messageId} da ${mail.source} scartato: ${scarto}`);
      continue;
    }
    const grezzo = await leggiMessaggio(mail.messageId);
    // Un alias può essere in copia insieme ad altri: si inoltra una volta per ognuno dei nostri.
    for (const alias of receipt.recipients.map((r) => r.toLowerCase())) {
      const verso = mappa[alias];
      if (!verso || mappa[verso.toLowerCase()]) continue; // alias sconosciuto, o che punta a un altro alias (niente giri)
      await ses.send(
        new SendEmailCommand({
          FromEmailAddress: alias,
          Destination: { ToAddresses: [verso] },
          Content: { Raw: { Data: Buffer.from(preparaInoltro(grezzo, alias), "latin1") } },
          ConfigurationSetName: process.env.SES_CONFIGURATION_SET || undefined,
        }),
      );
      console.log(`Messaggio ${mail.messageId} per ${alias} inoltrato`);
    }
  }
};
