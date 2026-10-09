import { Amplify } from "aws-amplify";
import "aws-amplify/auth/enable-oauth-listener";

// Configurazione del sito letta all'avvio da /config.json (indirizzo dell'API, dati di Cognito,
// accessi social attivi): così lo stesso build vale per ogni ambiente. Configura anche Amplify,
// la libreria che gestisce login e token.

/** Accessi social attivabili (quelli configurati in Terraform). */
export type SocialProvider = "google" | "facebook";

/** Scritto da Terraform in config.json accanto al sito (in locale da `npm run dev`). */
export interface AppConfig {
  apiUrl: string;
  region: string;
  userPoolId: string;
  userPoolClientId: string;
  cognitoDomain: string;
  social: SocialProvider[];
  /**
   * Annunci del piano Free. Senza AdSense configurato si vedono annunci interni
   * (promozione dei piani), che non usano cookie di terze parti.
   */
  pubblicita?: { adsenseClient?: string; adsenseSlot?: string };
}

/** Configurazione corrente: disponibile dopo caricaConfig(), cioè prima di mostrare il sito. */
export let config: AppConfig;

/** Legge config.json e prepara Amplify (Cognito, login con Google e Facebook). */
export async function caricaConfig() {
  const res = await fetch("/config.json", { cache: "no-store" });
  if (!res.ok) throw new Error(`config.json non disponibile (${res.status})`);
  config = (await res.json()) as AppConfig;

  Amplify.configure({
    Auth: {
      Cognito: {
        userPoolId: config.userPoolId,
        userPoolClientId: config.userPoolClientId,
        signUpVerificationMethod: "code",
        loginWith: {
          email: true,
          oauth: {
            domain: config.cognitoDomain,
            scopes: ["openid", "email", "profile"],
            redirectSignIn: [`${location.origin}/auth/callback`],
            redirectSignOut: [`${location.origin}/`],
            responseType: "code",
          },
        },
      },
    },
  });
}
