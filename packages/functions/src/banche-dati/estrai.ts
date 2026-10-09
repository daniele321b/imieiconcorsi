import { GetObjectCommand, PutObjectCommand, S3Client } from "@aws-sdk/client-s3";
import { GetCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { db, tables } from "@imieiconcorsi/core/db";
import type { BancaDati } from "@imieiconcorsi/core/domain";
import { avvisaAdmin } from "@imieiconcorsi/core/email";
import { env } from "@imieiconcorsi/core/env";
import type { S3Event } from "aws-lambda";
import { extractText, getDocumentProxy } from "unpdf";
import { estraiDomande } from "./parser";

// Estrazione delle domande da una banca dati caricata dall'admin.
// Parte da sola quando arriva il PDF (banche-dati/<id>.pdf nel bucket dei contenuti) oppure
// su richiesta dal pannello ({ id }) per riprovare con un altro formato.
// Risultato: banche-dati/<id>.json con tutte le domande + riepilogo ed esempi sul record.

const s3 = new S3Client({});
const bucket = () => env("CONTENUTI_BUCKET");

async function aggiorna(id: string, campi: Partial<BancaDati>) {
  const nomi = Object.keys(campi);
  await db.send(
    new UpdateCommand({
      TableName: tables.bancheDati,
      Key: { id },
      UpdateExpression: `SET ${nomi.map((n, i) => `#k${i} = :v${i}`).join(", ")}`,
      ExpressionAttributeNames: Object.fromEntries(nomi.map((n, i) => [`#k${i}`, n])),
      ExpressionAttributeValues: Object.fromEntries(nomi.map((n, i) => [`:v${i}`, campi[n as keyof BancaDati]])),
    }),
  );
}

async function estrai(id: string) {
  const res = await db.send(new GetCommand({ TableName: tables.bancheDati, Key: { id } }));
  const banca = res.Item as BancaDati | undefined;
  if (!banca) throw new Error(`Banca dati ${id} non trovata`);
  await aggiorna(id, { stato: "estrazione" });

  try {
    const pdf = await s3.send(new GetObjectCommand({ Bucket: bucket(), Key: `banche-dati/${id}.pdf` }));
    const doc = await getDocumentProxy(new Uint8Array(await pdf.Body!.transformToByteArray()));
    const { totalPages, text } = await extractText(doc, { mergePages: true });
    if ((text as string).replace(/\s/g, "").length < 200) {
      throw new Error("Nel PDF non c'è testo leggibile: probabilmente è una scansione (immagini). Serve un PDF con il testo selezionabile.");
    }

    const { domande, scartate, formati } = estraiDomande(text as string, banca.formato);
    await s3.send(
      new PutObjectCommand({
        Bucket: bucket(),
        Key: `banche-dati/${id}.json`,
        Body: JSON.stringify({ domande }),
        ContentType: "application/json",
      }),
    );
    await aggiorna(id, {
      stato: "estratta",
      pagine: totalPages,
      domande: domande.length,
      scartate: scartate.length,
      formati,
      esempi: domande.slice(0, 5),
      problemi: scartate.slice(0, 30),
      errore: domande.length ? "" : "Nessuna domanda riconosciuta: prova un altro formato o mandami il PDF.",
      estrattaIl: new Date().toISOString(),
    });
    await avvisaAdmin(
      `Banca dati estratta: ${domande.length} domande`,
      [
        [banca.titolo, banca.concorsoTitolo].filter(Boolean).join(" — "),
        `Pagine: ${totalPages} · domande riconosciute: ${domande.length} · scartate: ${scartate.length}`,
        "",
        "Controlla gli esempi e pubblica dal pannello admin → Banche dati.",
      ].join("\n"),
    ).catch((err) => console.error("Avviso admin non inviato", err));
  } catch (err) {
    console.error(`Estrazione ${id} non riuscita`, err);
    await aggiorna(id, { stato: "errore", errore: err instanceof Error ? err.message : String(err) });
  }
}

export const handler = async (event: S3Event | { id: string }) => {
  const ids =
    "Records" in event
      ? event.Records.map((r) => decodeURIComponent(r.s3.object.key.replace(/\+/g, " ")).match(/^banche-dati\/(.+)\.pdf$/)?.[1]).filter(
          (x): x is string => !!x,
        )
      : [event.id];
  for (const id of ids) await estrai(id);
};
