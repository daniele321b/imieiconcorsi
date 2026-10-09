import { signInWithRedirect } from "aws-amplify/auth";
import { Hub } from "aws-amplify/utils";
import { useEffect, useState } from "react";
import { Link, Navigate } from "react-router";
import { Alert, Spinner } from "../components/ui";
import { useAuth } from "../lib/auth";

// Pagina /auth/callback: qui torna il browser dopo il login con Google o Facebook.

/** Nel sessionStorage: il login social è già stato ritentato una volta (niente cicli). */
const CHIAVE_RIPROVA = "login-social-riprova";

/**
 * Primo accesso social con un'email già registrata: il trigger Cognito collega il
 * social all'account esistente, ma quella volta Cognito risponde "Already found an
 * entry for username Facebook_…". Rifacendo il login si entra nell'account collegato.
 */
function providerDaRiprovare(): "Google" | "Facebook" | undefined {
  const errore = new URLSearchParams(location.search).get("error_description") ?? "";
  const m = /already found an entry for username\s+(google|facebook)_/i.exec(errore);
  if (!m) return undefined;
  return m[1].toLowerCase() === "google" ? "Google" : "Facebook";
}

/** Ritorno dal login Google/Facebook: Amplify scambia il codice, poi l'AuthProvider aggiorna lo stato. */
export function AuthCallback() {
  const { stato } = useAuth();
  const [errore, setErrore] = useState(false);

  useEffect(() => {
    const provider = providerDaRiprovare();
    let giaRiprovato = false;
    try {
      giaRiprovato = sessionStorage.getItem(CHIAVE_RIPROVA) === "1";
    } catch {}
    if (provider && !giaRiprovato) {
      try {
        sessionStorage.setItem(CHIAVE_RIPROVA, "1");
      } catch {}
      void signInWithRedirect({ provider }).catch(() => setErrore(true));
      return;
    }
    if (new URLSearchParams(location.search).has("error")) setErrore(true);

    return Hub.listen("auth", ({ payload }) => {
      if (payload.event === "signInWithRedirect_failure") setErrore(true);
    });
  }, []);

  if (stato === "autenticato") {
    try {
      sessionStorage.removeItem(CHIAVE_RIPROVA);
    } catch {}
    return <Navigate to="/app" replace />;
  }

  return (
    <div className="grid min-h-screen place-items-center bg-slate-50 px-4">
      {errore ? (
        <div className="max-w-sm space-y-4 text-center">
          <Alert tone="error">Non siamo riusciti a completare l'accesso. Riprova.</Alert>
          <Link to="/" className="text-sm font-semibold text-brand-600">
            Torna alla pagina di accesso
          </Link>
        </div>
      ) : (
        <Spinner label="Accesso in corso…" />
      )}
    </div>
  );
}
