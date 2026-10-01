import {
  autoSignIn,
  confirmResetPassword,
  confirmSignUp,
  resendSignUpCode,
  resetPassword,
  signIn,
  signInWithRedirect,
  signUp,
} from "aws-amplify/auth";
import { ArrowLeft, Mail } from "lucide-react";
import { useState, type FormEvent } from "react";
import { messaggioErrore } from "../lib/auth";
import { config, type SocialProvider } from "../lib/config";
import { FacebookIcon, GoogleIcon } from "./brand";
import { Alert, Button, Field, cx } from "./ui";

type Modo = "accedi" | "registrati" | "conferma" | "recupera" | "nuova-password";

export function AuthCard() {
  const [modo, setModo] = useState<Modo>("accedi");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [nome, setNome] = useState("");
  const [codice, setCodice] = useState("");
  const [errore, setErrore] = useState<string>();
  const [info, setInfo] = useState<string>();
  const [inCorso, setInCorso] = useState(false);

  const vai = (m: Modo) => {
    setModo(m);
    setErrore(undefined);
    setInfo(undefined);
    setCodice("");
  };

  async function esegui(fn: () => Promise<void>) {
    setInCorso(true);
    setErrore(undefined);
    try {
      await fn();
    } catch (err) {
      if (err instanceof Error && err.name === "UserNotConfirmedException") {
        await resendSignUpCode({ username: email }).catch(() => {});
        vai("conferma");
        setInfo("Devi ancora confermare l'email: ti abbiamo inviato un nuovo codice.");
      } else {
        setErrore(messaggioErrore(err));
      }
    } finally {
      setInCorso(false);
    }
  }

  // Al termine del login l'AuthProvider riceve l'evento "signedIn" e la Landing reindirizza.
  const onAccedi = (e: FormEvent) => {
    e.preventDefault();
    void esegui(async () => {
      const res = await signIn({ username: email, password });
      if (res.nextStep.signInStep === "CONFIRM_SIGN_UP") {
        await resendSignUpCode({ username: email });
        vai("conferma");
      }
    });
  };

  const onRegistrati = (e: FormEvent) => {
    e.preventDefault();
    void esegui(async () => {
      await signUp({
        username: email,
        password,
        options: { userAttributes: { email, ...(nome ? { name: nome } : {}) }, autoSignIn: true },
      });
      vai("conferma");
      setInfo(`Ti abbiamo inviato un codice a ${email}.`);
    });
  };

  const onConferma = (e: FormEvent) => {
    e.preventDefault();
    void esegui(async () => {
      const res = await confirmSignUp({ username: email, confirmationCode: codice.trim() });
      if (res.nextStep.signUpStep === "COMPLETE_AUTO_SIGN_IN") await autoSignIn();
      else if (password) await signIn({ username: email, password });
      else {
        vai("accedi");
        setInfo("Email confermata. Ora puoi accedere.");
      }
    });
  };

  const onRecupera = (e: FormEvent) => {
    e.preventDefault();
    void esegui(async () => {
      await resetPassword({ username: email });
      vai("nuova-password");
      setInfo(`Se l'email è registrata, riceverai un codice a ${email}.`);
    });
  };

  const onNuovaPassword = (e: FormEvent) => {
    e.preventDefault();
    void esegui(async () => {
      await confirmResetPassword({ username: email, confirmationCode: codice.trim(), newPassword: password });
      await signIn({ username: email, password });
    });
  };

  const social = (provider: SocialProvider) =>
    void esegui(() => signInWithRedirect({ provider: provider === "google" ? "Google" : "Facebook" }));

  const intestazioni: Record<Modo, { titolo: string; sotto: string }> = {
    accedi: { titolo: "Bentornato", sotto: "Accedi per continuare a prepararti." },
    registrati: { titolo: "Crea il tuo account", sotto: "Gratis, senza carta di credito." },
    conferma: { titolo: "Controlla la tua email", sotto: "Inserisci il codice a 6 cifre che ti abbiamo inviato." },
    recupera: { titolo: "Password dimenticata", sotto: "Ti inviamo un codice per sceglierne una nuova." },
    "nuova-password": { titolo: "Nuova password", sotto: "Inserisci il codice ricevuto e la nuova password." },
  };

  return (
    <div className="relative z-10 mx-auto w-full max-w-md rounded-3xl bg-white p-6 shadow-2xl shadow-brand-950/40 ring-1 ring-white/20 sm:p-8">
      {(modo === "accedi" || modo === "registrati") && (
        <div className="mb-6 grid grid-cols-2 rounded-xl bg-slate-100 p-1 text-sm font-semibold" role="tablist">
          {(["accedi", "registrati"] as const).map((m) => (
            <button
              key={m}
              role="tab"
              aria-selected={modo === m}
              onClick={() => vai(m)}
              className={cx("rounded-lg py-2 transition", modo === m ? "bg-white text-slate-900 shadow-sm" : "text-slate-500 hover:text-slate-700")}
            >
              {m === "accedi" ? "Accedi" : "Registrati"}
            </button>
          ))}
        </div>
      )}

      {modo !== "accedi" && modo !== "registrati" && (
        <button onClick={() => vai("accedi")} className="mb-4 inline-flex items-center gap-1 text-sm font-medium text-slate-500 hover:text-slate-800">
          <ArrowLeft className="size-4" /> Torna all'accesso
        </button>
      )}

      <h2 className="text-2xl font-extrabold tracking-tight text-slate-900">{intestazioni[modo].titolo}</h2>
      <p className="mt-1 text-sm text-slate-500">{intestazioni[modo].sotto}</p>

      <div className="mt-5 space-y-3">
        {errore && <Alert tone="error">{errore}</Alert>}
        {info && <Alert tone="info">{info}</Alert>}
      </div>

      {modo === "accedi" && (
        <form onSubmit={onAccedi} className="mt-5 space-y-4">
          <Field label="Email" name="email" type="email" autoComplete="email" required value={email} onChange={(e) => setEmail(e.target.value)} placeholder="nome@esempio.it" />
          <Field label="Password" name="password" type="password" autoComplete="current-password" required value={password} onChange={(e) => setPassword(e.target.value)} />
          <div className="flex justify-end">
            <button type="button" onClick={() => vai("recupera")} className="text-sm font-medium text-brand-600 hover:text-brand-700">
              Password dimenticata?
            </button>
          </div>
          <Button type="submit" size="lg" className="w-full" loading={inCorso}>
            Accedi
          </Button>
        </form>
      )}

      {modo === "registrati" && (
        <form onSubmit={onRegistrati} className="mt-5 space-y-4">
          <Field label="Nome" name="name" autoComplete="given-name" value={nome} onChange={(e) => setNome(e.target.value)} placeholder="Come ti chiami?" />
          <Field label="Email" name="email" type="email" autoComplete="email" required value={email} onChange={(e) => setEmail(e.target.value)} placeholder="nome@esempio.it" />
          <Field
            label="Password"
            name="password"
            type="password"
            autoComplete="new-password"
            required
            minLength={8}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            hint="Almeno 8 caratteri, con una maiuscola, una minuscola e un numero."
          />
          <Button type="submit" size="lg" className="w-full" loading={inCorso}>
            Crea account gratuito
          </Button>
        </form>
      )}

      {modo === "conferma" && (
        <form onSubmit={onConferma} className="mt-5 space-y-4">
          <div className="flex items-center gap-3 rounded-xl bg-slate-50 p-3 text-sm text-slate-600">
            <Mail className="size-4 text-brand-600" /> {email}
          </div>
          <CodiceField value={codice} onChange={setCodice} />
          <Button type="submit" size="lg" className="w-full" loading={inCorso}>
            Conferma e entra
          </Button>
          <button
            type="button"
            className="w-full text-sm font-medium text-brand-600 hover:text-brand-700"
            onClick={() =>
              void esegui(async () => {
                await resendSignUpCode({ username: email });
                setInfo("Codice inviato di nuovo.");
              })
            }
          >
            Non hai ricevuto il codice? Invialo di nuovo
          </button>
        </form>
      )}

      {modo === "recupera" && (
        <form onSubmit={onRecupera} className="mt-5 space-y-4">
          <Field label="Email" name="email" type="email" autoComplete="email" required value={email} onChange={(e) => setEmail(e.target.value)} />
          <Button type="submit" size="lg" className="w-full" loading={inCorso}>
            Invia il codice
          </Button>
        </form>
      )}

      {modo === "nuova-password" && (
        <form onSubmit={onNuovaPassword} className="mt-5 space-y-4">
          <CodiceField value={codice} onChange={setCodice} />
          <Field
            label="Nuova password"
            name="password"
            type="password"
            autoComplete="new-password"
            required
            minLength={8}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            hint="Almeno 8 caratteri, con una maiuscola, una minuscola e un numero."
          />
          <Button type="submit" size="lg" className="w-full" loading={inCorso}>
            Salva e accedi
          </Button>
        </form>
      )}

      {(modo === "accedi" || modo === "registrati") && config.social.length > 0 && (
        <>
          <div className="my-6 flex items-center gap-3 text-xs font-medium text-slate-400">
            <span className="h-px flex-1 bg-slate-200" /> oppure <span className="h-px flex-1 bg-slate-200" />
          </div>
          <div className="grid gap-3">
            {config.social.includes("google") && (
              <Button variant="secondary" size="lg" onClick={() => social("google")} disabled={inCorso}>
                <GoogleIcon className="size-5" /> Continua con Google
              </Button>
            )}
            {config.social.includes("facebook") && (
              <Button variant="secondary" size="lg" onClick={() => social("facebook")} disabled={inCorso}>
                <FacebookIcon className="size-5" /> Continua con Facebook
              </Button>
            )}
          </div>
        </>
      )}

      {modo === "registrati" && (
        <p className="mt-6 text-center text-xs text-slate-400">
          Registrandoti accetti i termini del servizio e l'informativa privacy.
        </p>
      )}
    </div>
  );
}

function CodiceField({ value, onChange }: { value: string; onChange: (v: string) => void }) {
  return (
    <label className="block">
      <span className="mb-1.5 block text-sm font-medium text-slate-700">Codice di verifica</span>
      <input
        inputMode="numeric"
        autoComplete="one-time-code"
        required
        maxLength={6}
        value={value}
        onChange={(e) => onChange(e.target.value.replace(/\D/g, ""))}
        className="block h-14 w-full rounded-xl border-0 text-center font-mono text-2xl tracking-[0.5em] ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500 focus:outline-none"
        placeholder="••••••"
      />
    </label>
  );
}
