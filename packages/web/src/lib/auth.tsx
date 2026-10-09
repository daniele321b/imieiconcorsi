import { fetchAuthSession, getCurrentUser, signOut } from "aws-amplify/auth";
import { Hub } from "aws-amplify/utils";
import { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from "react";
import { api, type UtenteApi } from "./api";

type Stato = "caricamento" | "ospite" | "autenticato";

interface AuthContextValue {
  stato: Stato;
  utente?: UtenteApi;
  setUtente: (u: UtenteApi) => void;
  /** rinnovaToken: dopo un cambio di piano o di nome (gruppi e nome viaggiano nel token Cognito) */
  ricarica: (opzioni?: { rinnovaToken?: boolean }) => Promise<void>;
  esci: () => Promise<void>;
}

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [stato, setStato] = useState<Stato>("caricamento");
  const [utente, setUtente] = useState<UtenteApi>();

  const ricarica = useCallback(async ({ rinnovaToken = false } = {}) => {
    try {
      await getCurrentUser();
      if (rinnovaToken) await fetchAuthSession({ forceRefresh: true });
      // GET /me crea il profilo al primo accesso.
      setUtente(await api<UtenteApi>("/me"));
      setStato("autenticato");
    } catch {
      setUtente(undefined);
      setStato("ospite");
    }
  }, []);

  useEffect(() => {
    void ricarica();
    return Hub.listen("auth", ({ payload }) => {
      if (payload.event === "signedIn" || payload.event === "signInWithRedirect") void ricarica();
      if (payload.event === "signedOut") {
        setUtente(undefined);
        setStato("ospite");
      }
    });
  }, [ricarica]);

  const esci = useCallback(async () => {
    await signOut();
  }, []);

  return <AuthContext.Provider value={{ stato, utente, setUtente, ricarica, esci }}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth fuori da AuthProvider");
  return ctx;
}

/** Versione per le pagine dell'area riservata, dove l'utente c'è sempre. */
export function useUtente() {
  const { utente, setUtente } = useAuth();
  if (!utente) throw new Error("useUtente senza utente autenticato");
  return { utente, setUtente };
}

/** Messaggi comprensibili per gli errori di Cognito. */
export function messaggioErrore(err: unknown): string {
  const name = err instanceof Error ? err.name : "";
  switch (name) {
    case "NotAuthorizedException":
    case "UserNotFoundException":
      return "Email o password non corretti.";
    case "UsernameExistsException":
      return "Esiste già un account con questa email. Prova ad accedere.";
    case "InvalidPasswordException":
      return "La password deve avere almeno 8 caratteri, con una maiuscola, una minuscola e un numero.";
    case "CodeMismatchException":
      return "Il codice non è corretto.";
    case "ExpiredCodeException":
      return "Il codice è scaduto: richiedine uno nuovo.";
    case "LimitExceededException":
    case "TooManyRequestsException":
      return "Troppi tentativi. Riprova tra qualche minuto.";
    case "InvalidParameterException":
      return "Controlla i dati inseriti.";
    case "UserLambdaValidationException":
      // Messaggio del trigger pre sign-up (es. "Esiste già un account con questa email: accedi con Facebook.")
      return err instanceof Error ? err.message.replace(/^PreSignUp failed with error\s*/i, "") : "Registrazione non riuscita.";
    default:
      return err instanceof Error && err.message ? err.message : "Qualcosa è andato storto. Riprova.";
  }
}
