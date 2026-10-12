import { BellRing, CheckCircle2, Target, Timer, TrendingUp } from "lucide-react";
import { Link, Navigate } from "react-router";
import { AuthCard } from "../components/AuthCard";
import { PiePagina } from "./legale/LegalePagina";
import { Logo } from "../components/brand";
import { FullPageSpinner } from "../components/ui";
import { useAuth } from "../lib/auth";

// Home pubblica (/): presentazione dell'app e riquadro di accesso (AuthCard). Chi è già
// collegato viene portato direttamente nell'app.

/** I tre punti di forza mostrati sotto il titolo. */
const PUNTI = [
  { Icon: BellRing, titolo: "Il bando giusto, appena esce", testo: "Ogni mattina leggiamo inPA e ti avvisiamo solo per i comparti che ti interessano." },
  { Icon: Target, titolo: "Studi le materie del tuo bando", testo: "Schede brevi e quiz calibrati sul tuo livello, materia per materia." },
  { Icon: Timer, titolo: "Simulazioni come all'esame", testo: "60 domande, timer e penalità sugli errori. Poi vedi dove migliorare." },
];

/** Pagina "/". */
export function Landing() {
  const { stato } = useAuth();
  if (stato === "caricamento") return <FullPageSpinner />;
  if (stato === "autenticato") return <Navigate to="/app" replace />;

  return (
    <div className="relative min-h-screen overflow-hidden bg-brand-950">
      {/* Sfondo: bagliori e griglia */}
      <div aria-hidden className="pointer-events-none absolute inset-0">
        <div className="absolute -top-40 -left-40 size-[36rem] rounded-full bg-brand-600/40 blur-3xl" />
        <div className="absolute top-1/3 -right-32 size-[28rem] rounded-full bg-fuchsia-500/20 blur-3xl" />
        <div className="absolute -bottom-40 left-1/3 size-[30rem] rounded-full bg-accent-400/10 blur-3xl" />
        <div
          className="absolute inset-0 opacity-[0.07]"
          style={{
            backgroundImage:
              "linear-gradient(to right, white 1px, transparent 1px), linear-gradient(to bottom, white 1px, transparent 1px)",
            backgroundSize: "48px 48px",
            maskImage: "radial-gradient(ellipse at 30% 40%, black 30%, transparent 75%)",
          }}
        />
      </div>

      <div className="relative mx-auto grid min-h-screen max-w-7xl content-center items-center gap-10 px-4 py-8 sm:px-6 lg:grid-cols-[1.15fr_1fr] lg:gap-16 lg:px-8">
        {/* Racconto */}
        <section className="animate-fade-up text-white">
          <div className="flex flex-wrap items-center justify-between gap-x-6 gap-y-3">
            <Logo light className="text-xl" />
            <nav className="flex flex-wrap gap-x-5 gap-y-1 text-sm font-semibold text-brand-100/80">
              <Link to="/prezzi" className="hover:text-white">
                Prezzi
              </Link>
              <Link to="/domande-frequenti" className="hover:text-white">
                Domande frequenti
              </Link>
              <Link to="/chi-siamo" className="hover:text-white">
                Chi siamo
              </Link>
            </nav>
          </div>

          <div className="mt-10 inline-flex items-center gap-2 rounded-full bg-white/10 px-3 py-1 text-xs font-semibold text-brand-100 ring-1 ring-white/15 backdrop-blur">
            <span className="relative flex size-2">
              <span className="absolute inline-flex size-full animate-ping rounded-full bg-emerald-400 opacity-75" />
              <span className="relative inline-flex size-2 rounded-full bg-emerald-400" />
            </span>
            Bandi di inPA aggiornati ogni mattina
          </div>

          <h1 className="mt-5 text-4xl leading-[1.1] font-extrabold tracking-tight sm:text-5xl lg:text-6xl">
            Il tuo concorso pubblico,{" "}
            <span className="bg-gradient-to-r from-accent-300 via-amber-200 to-fuchsia-300 bg-clip-text text-transparent">
              studiato su misura.
            </span>
          </h1>
          <p className="mt-5 max-w-xl text-lg text-brand-100/80">
            Scegli il bando: ti prepariamo sulle sue materie, al tuo livello, fino alla simulazione con le regole vere
            della prova.
          </p>

          <ul className="mt-8 hidden gap-5 sm:grid">
            {PUNTI.map(({ Icon, titolo, testo }) => (
              <li key={titolo} className="flex gap-4">
                <span className="grid size-11 shrink-0 place-items-center rounded-xl bg-white/10 text-accent-300 ring-1 ring-white/15">
                  <Icon className="size-5" />
                </span>
                <div>
                  <p className="font-semibold">{titolo}</p>
                  <p className="text-sm text-brand-100/70">{testo}</p>
                </div>
              </li>
            ))}
          </ul>

          <p className="mt-10 hidden text-xs font-medium tracking-wide text-brand-200/60 uppercase lg:block">
            Enti locali · Forze dell'ordine · INPS · Ministeri · Sanità
          </p>
        </section>

        {/* Accesso */}
        <section className="animate-fade-up [animation-delay:120ms]">
          <div className="relative mx-auto max-w-md">
            <MockupFluttuanti />
            <AuthCard />
          </div>
        </section>
      </div>
      <div className="relative">
        <PiePagina scuro />
      </div>
    </div>
  );
}

/** Due schede decorative che suggeriscono l'esperienza dentro l'app. */
function MockupFluttuanti() {
  return (
    <div aria-hidden className="pointer-events-none hidden xl:block">
      <div className="absolute -top-16 -left-44 z-0 w-60 animate-float rounded-2xl bg-white/95 p-4 shadow-2xl shadow-brand-950/50 rotate-[-6deg]">
        <p className="text-[11px] font-semibold text-sky-600 uppercase">Diritto costituzionale</p>
        <p className="mt-1 text-sm font-semibold text-slate-800">Quanto dura il mandato del Presidente della Repubblica?</p>
        <div className="mt-3 flex items-center gap-2 rounded-lg bg-emerald-50 px-3 py-2 text-sm font-semibold text-emerald-700 ring-1 ring-emerald-200">
          <CheckCircle2 className="size-4" /> 7 anni
        </div>
      </div>
      <div className="absolute -right-20 -bottom-28 z-20 w-52 animate-float rounded-2xl bg-white/95 p-4 shadow-2xl shadow-brand-950/50 [animation-delay:1.5s] rotate-[5deg]">
        <div className="flex items-center justify-between">
          <p className="text-[11px] font-semibold text-slate-500 uppercase">Simulazione</p>
          <TrendingUp className="size-4 text-emerald-500" />
        </div>
        <p className="mt-1 text-3xl font-extrabold text-slate-900">
          52<span className="text-lg text-slate-400">/60</span>
        </p>
        <p className="text-xs font-semibold text-emerald-600">Prova superata · +8 rispetto alla scorsa</p>
      </div>
    </div>
  );
}
