// Regole del trigger "pre sign-up" (pre-signup.ts) per evitare account doppi: chi ha già un
// account email e password e poi entra con Google o Facebook (stessa email) finisce nello
// stesso account. Senza AWS: le prova la suite di test.

/** Provider social come li chiama Cognito (identity provider configurati in Terraform). */
const PROVIDER: Record<string, string> = { google: "Google", facebook: "Facebook" };

/**
 * Da username federato ("facebook_1234…", "Google_5678…") a provider e id dell'utente
 * presso il provider, come li vuole AdminLinkProviderForUser.
 */
export function providerDaUsername(username: string) {
  const i = username.indexOf("_");
  if (i <= 0) return undefined;
  const nome = PROVIDER[username.slice(0, i).toLowerCase()];
  return nome ? { nome, id: username.slice(i + 1) } : undefined;
}

/** Un account già presente con la stessa email (username Cognito e stato, es. CONFIRMED). */
export interface UtenteEsistente {
  username: string;
  stato?: string;
}

/** Cosa fa il trigger: lasciar procedere, collegare a un account esistente o rifiutare con un messaggio. */
export type Decisione =
  | { azione: "procedi" }
  | { azione: "collega"; destinazione: string }
  | { azione: "rifiuta"; messaggio: string };

/**
 * Una persona = un account, qualunque sia il modo di accesso.
 * - Accesso social con un account email/password già confermato con la stessa email:
 *   si collega il social a quell'account (stesso profilo, stessi gruppi).
 *   Solo account confermati: un account mai verificato non può "catturare" un social.
 * - Registrazione email/password con email già usata: rifiuto con l'indicazione giusta.
 */
export function decidi(trigger: string, esistenti: UtenteEsistente[]): Decisione {
  if (trigger === "PreSignUp_ExternalProvider") {
    const nativo = esistenti.find((u) => u.stato === "CONFIRMED");
    return nativo ? { azione: "collega", destinazione: nativo.username } : { azione: "procedi" };
  }
  if (trigger === "PreSignUp_SignUp" && esistenti.length) {
    const social = [...new Set(esistenti.map((u) => providerDaUsername(u.username)?.nome).filter(Boolean))];
    return {
      azione: "rifiuta",
      messaggio: social.length
        ? `Esiste già un account con questa email: accedi con ${social.join(" o ")}.`
        : "Esiste già un account con questa email: accedi con email e password.",
    };
  }
  return { azione: "procedi" };
}
