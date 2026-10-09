import { Amplify } from "aws-amplify";
import "aws-amplify/auth/enable-oauth-listener";

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

export let config: AppConfig;

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
