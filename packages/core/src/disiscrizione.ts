import { createHmac, timingSafeEqual } from "node:crypto";
import { env } from "./env";

// Link "non ricevere più avvisi" nelle email: funziona senza login, quindi è firmato.
// La firma lega il link a un solo utente; il segreto lo genera Terraform (DISISCRIZIONE_SECRET).

// Lo stesso segreto firma anche i link "aperto" (immagine nell'email) e "clic": lo scopo fa
// parte della firma, così un link per un uso non vale per un altro.
type Scopo = "disiscrivi" | "aperto";

const firma = (userId: string, segreto: string, scopo: Scopo = "disiscrivi") =>
  createHmac("sha256", segreto).update(`${scopo}:${userId}`).digest("base64url").slice(0, 32);

/** Firma del link "non ricevere più avvisi" di un utente. */
export const firmaDisiscrizione = (userId: string, segreto = env("DISISCRIZIONE_SECRET")) => firma(userId, segreto);

/** Controlla la firma di un link (confronto a tempo costante, contro chi prova a indovinarla). */
export function firmaValida(userId: string, token: string, segreto = env("DISISCRIZIONE_SECRET"), scopo: Scopo = "disiscrivi") {
  const attesa = Buffer.from(firma(userId, segreto, scopo));
  const ricevuta = Buffer.from(token);
  return attesa.length === ricevuta.length && timingSafeEqual(attesa, ricevuta);
}

/**
 * Link per sapere se gli avvisi vengono letti: l'immagine invisibile dell'email e i link
 * che passano dall'API prima di aprire la pagina del sito (solo percorsi del sito).
 */
export function linkLettura(userId: string, sito: string, segreto = env("DISISCRIZIONE_SECRET")) {
  const qs = new URLSearchParams({ u: userId, t: firma(userId, segreto, "aperto") });
  return {
    immagine: `${sito}/api/pubblico/aperto?${qs}`,
    clic: (percorso: string) => `${sito}/api/pubblico/clic?${qs}&vai=${encodeURIComponent(percorso)}`,
  };
}

/** Destinazione di un clic: solo un percorso del sito (niente redirect verso altri domini). */
export const percorsoSicuro = (vai: string | undefined) => (vai && /^\/(?!\/)[\w\-./?=&%]*$/.test(vai) ? vai : "/app");

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

/** Campi che segnano una lettura degli avvisi: il contatore dei non aperti torna a zero. */
export const LETTURA_AVVISI = "SET avvisiNonAperti = :zero, ultimaLetturaIl = :ora";
/** Valori per LETTURA_AVVISI. */
export const valoriLettura = () => ({ ":zero": 0, ":ora": new Date().toISOString() });
