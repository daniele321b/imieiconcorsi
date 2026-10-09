import { createHmac, timingSafeEqual } from "node:crypto";
import { env } from "./env";

// Link "non ricevere più avvisi" nelle email: funziona senza login, quindi è firmato.
// La firma lega il link a un solo utente; il segreto lo genera Terraform (DISISCRIZIONE_SECRET).

const firma = (userId: string, segreto: string) => createHmac("sha256", segreto).update(`disiscrivi:${userId}`).digest("base64url").slice(0, 32);

export const firmaDisiscrizione = (userId: string, segreto = env("DISISCRIZIONE_SECRET")) => firma(userId, segreto);

export function firmaValida(userId: string, token: string, segreto = env("DISISCRIZIONE_SECRET")) {
  const attesa = Buffer.from(firma(userId, segreto));
  const ricevuta = Buffer.from(token);
  return attesa.length === ricevuta.length && timingSafeEqual(attesa, ricevuta);
}

/** Link per la persona (pagina del sito) e intestazioni per Gmail & co. (disiscrizione in un clic, RFC 8058). */
export function linkDisiscrizione(userId: string, sito: string) {
  const qs = new URLSearchParams({ u: userId, t: firmaDisiscrizione(userId) });
  return {
    pagina: `${sito}/disiscrivi?${qs}`,
    intestazioni: [
      { Name: "List-Unsubscribe", Value: `<${sito}/api/pubblico/disiscrivi?${qs}>` },
      { Name: "List-Unsubscribe-Post", Value: "List-Unsubscribe=One-Click" },
    ],
  };
}
