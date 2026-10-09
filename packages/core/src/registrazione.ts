// Registrazione con email e password: solo dai provider di posta più diffusi, per
// tenere fuori le caselle usa e getta. Lo controllano il sito (subito, nel modulo)
// e il trigger Cognito pre sign-up (sempre). L'accesso con Google o Facebook non passa
// di qui: l'email l'ha già verificata il provider.

export const DOMINI_EMAIL_CONSENTITI = [
  // Google
  "gmail.com", "googlemail.com",
  // Microsoft
  "outlook.com", "outlook.it", "hotmail.com", "hotmail.it", "live.com", "live.it", "msn.com",
  // Yahoo, AOL
  "yahoo.com", "yahoo.it", "ymail.com", "aol.com",
  // Apple
  "icloud.com", "me.com", "mac.com",
  // Provider italiani
  "libero.it", "virgilio.it", "inwind.it", "iol.it", "blu.it", "giallo.it",
  "alice.it", "tim.it", "tin.it", "tiscali.it", "email.it", "fastwebnet.it", "vodafone.it", "katamail.com", "poste.it",
  // Altri provider affidabili
  "proton.me", "protonmail.com", "pm.me", "gmx.com", "gmx.it", "gmx.net", "zoho.com", "tutanota.com", "fastmail.com",
] as const;

export const dominioEmail = (email: string) => email.trim().toLowerCase().split("@").pop() ?? "";

export const emailConsentita = (email: string) =>
  (DOMINI_EMAIL_CONSENTITI as readonly string[]).includes(dominioEmail(email));

export const MESSAGGIO_EMAIL_NON_CONSENTITA =
  "Per registrarti usa un indirizzo di un provider diffuso (Gmail, Outlook/Hotmail, Yahoo, iCloud, Libero, Virgilio, Alice/TIM…) oppure accedi con Google o Facebook.";
