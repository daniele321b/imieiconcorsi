import { Hub } from "aws-amplify/utils";
import { useEffect, useState } from "react";
import { Link, Navigate } from "react-router";
import { Alert, Spinner } from "../components/ui";
import { useAuth } from "../lib/auth";

/** Ritorno dal login Google/Facebook: Amplify scambia il codice, poi l'AuthProvider aggiorna lo stato. */
export function AuthCallback() {
  const { stato } = useAuth();
  const [errore, setErrore] = useState(false);

  useEffect(
    () =>
      Hub.listen("auth", ({ payload }) => {
        if (payload.event === "signInWithRedirect_failure") setErrore(true);
      }),
    [],
  );

  if (stato === "autenticato") return <Navigate to="/app" replace />;

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
