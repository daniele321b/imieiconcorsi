import { PIANI } from "@imieiconcorsi/core/domain";
import { BookOpenCheck, Crown, LayoutDashboard, LifeBuoy, LogOut, Search, ShieldCheck, Sparkles } from "lucide-react";
import { useEffect } from "react";
import { Link, Navigate, NavLink, Outlet, useLocation } from "react-router";
import { Logo } from "../../components/brand";
import { Badge, FullPageSpinner, cx } from "../../components/ui";
import { useAuth } from "../../lib/auth";
import { useBandiDaCaricare } from "../../lib/bandi";
import { inviaInvitoRicordato } from "../../lib/invito";
import { PiePagina } from "../legale/LegalePagina";

// Cornice dell'area riservata (/app e /admin): intestazione con menu (da 1024 px), assistenza e
// profilo, barra in basso su telefono e tablet, piè di pagina. Rimanda alla home chi non è collegato e
// all'onboarding chi non ha ancora completato il profilo.

/** Voce del menu: `zona` = percorsi per cui la voce è evidenziata (es. Studio anche nelle banche dati). */
interface Voce {
  to: string;
  label: string;
  Icon: typeof Search;
  zona: RegExp;
}

/** Voci del menu: in alto su computer (da 1024 px), nella barra in basso su telefono e tablet. */
const NAV: Voce[] = [
  { to: "/app", label: "Dashboard", Icon: LayoutDashboard, zona: /^\/app\/?$/ },
  { to: "/app/concorsi", label: "Concorsi", Icon: Search, zona: /^\/app\/concorsi/ },
  // Le banche dati stanno dentro Studio (riquadro nella pagina Studio).
  { to: "/app/studio", label: "Studio", Icon: BookOpenCheck, zona: /^\/app\/(studio|banche-dati|sessione)/ },
  { to: "/app/tutor", label: "Tutor AI", Icon: Sparkles, zona: /^\/app\/tutor/ },
  { to: "/app/piani", label: "Piani", Icon: Crown, zona: /^\/app\/(piani|pagamento)/ },
];
const ADMIN: Voce = { to: "/admin", label: "Admin", Icon: ShieldCheck, zona: /^\/admin/ };

/** Layout comune delle pagine riservate: le pagine si vedono al posto di <Outlet />. */
export function AppLayout() {
  const { stato, utente, esci } = useAuth();
  const { pathname } = useLocation();
  const pronto = stato !== "caricamento" && !!utente?.onboarded;
  const daCaricare = useBandiDaCaricare(pronto && !!utente?.admin);

  // Codice di un amico dal link d'invito: si manda una volta, a profilo completato.
  useEffect(() => {
    if (pronto) void inviaInvitoRicordato();
  }, [pronto]);

  if (stato === "caricamento") return <FullPageSpinner />;
  if (stato === "ospite" || !utente) return <Navigate to="/" replace />;
  if (!utente.onboarded && pathname !== "/app/onboarding") return <Navigate to="/app/onboarding" replace />;
  if (pathname === "/app/onboarding") return <Outlet />;

  const piano = PIANI[utente.piano];
  // L'admin ha tutte le funzioni: niente piani da comprare, al loro posto il pannello.
  const voci = utente.admin ? [...NAV.filter((v) => v.to !== "/app/piani"), ADMIN] : NAV;
  // In basso: le stesse 5 voci, con il Tutor AI al centro.
  const basso = [voci[0]!, voci[1]!, voci[3]!, voci[2]!, voci[4]!];
  const attiva = (v: Voce) => v.zona.test(pathname);
  // Bandi nuovi con una banca dati da caricare, non ancora visti nell'elenco (pallino rosso su Admin).
  const notifica = (v: Voce) =>
    v === ADMIN && !!daCaricare?.daVedere ? (
      <span
        className="absolute -top-1.5 -right-2 grid size-4 place-items-center rounded-full bg-rose-500 text-[10px] font-bold text-white ring-2 ring-white"
        aria-label={`${daCaricare.daVedere} bandi nuovi da caricare`}
      >
        {daCaricare.daVedere > 9 ? "9+" : daCaricare.daVedere}
      </span>
    ) : null;
  const destinazione = (v: Voce) => (v === ADMIN && daCaricare?.daVedere ? "/admin/banche-dati#da-caricare" : v.to);

  return (
    <div className="min-h-screen pb-24 lg:pb-0">
      <header className="sticky top-0 z-30 border-b border-slate-200/70 bg-white/80 backdrop-blur">
        <div className="mx-auto flex h-16 max-w-6xl items-center gap-6 px-4 sm:px-6">
          <Link to="/app">
            <Logo />
          </Link>
          <nav className="hidden items-center gap-1 lg:flex">
            {voci.map((v) => (
              <Link
                key={v.to}
                to={destinazione(v)}
                aria-current={attiva(v) ? "page" : undefined}
                className={cx(
                  "relative inline-flex items-center gap-2 rounded-lg px-3 py-2 text-sm font-semibold transition",
                  v.to === "/app/tutor"
                    ? cx("bg-gradient-to-r from-brand-950 via-brand-700 to-fuchsia-600 text-white shadow-sm hover:opacity-90", attiva(v) && "ring-2 ring-accent-300")
                    : attiva(v)
                      ? "bg-brand-50 text-brand-700"
                      : "text-slate-600 hover:bg-slate-100 hover:text-slate-900",
                )}
              >
                <v.Icon className="size-4" /> {v.label}
                {notifica(v)}
              </Link>
            ))}
          </nav>
          <div className="ml-auto flex items-center gap-2">
            {!utente.admin && (
              <Link to="/app/piani">
                <Badge tone={utente.piano === "free" ? "slate" : "amber"}>
                  {utente.piano !== "free" && <Crown className="size-3" />} {piano.nome}
                </Badge>
              </Link>
            )}
            {/* Assistenza, con il pallino quando c'è una risposta da leggere. */}
            <NavLink
              to="/app/assistenza"
              aria-label={utente.richiesteDaLeggere ? `Assistenza: ${utente.richiesteDaLeggere} risposte da leggere` : "Assistenza"}
              title="Assistenza"
              className={({ isActive }) => cx("relative rounded-lg p-2 hover:bg-slate-100", isActive ? "text-brand-600" : "text-slate-500")}
            >
              <LifeBuoy className="size-5" />
              {!!utente.richiesteDaLeggere && <span className="absolute top-1.5 right-1.5 size-2.5 rounded-full bg-rose-500 ring-2 ring-white" />}
            </NavLink>
            <NavLink
              to="/app/profilo"
              aria-label="Profilo"
              className="grid size-9 place-items-center rounded-full bg-brand-600 text-sm font-bold text-white"
            >
              {(utente.nome ?? utente.email ?? "?").charAt(0).toUpperCase()}
            </NavLink>
            <button onClick={() => void esci()} aria-label="Esci" className="hidden rounded-lg p-2 text-slate-500 hover:bg-slate-100 lg:block">
              <LogOut className="size-4" />
            </button>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-6xl px-4 py-8 sm:px-6">
        <Outlet />
      </main>
      <PiePagina />

      {/* Barra in basso su telefono e tablet: il Tutor AI al centro, rialzato, con i colori della home. */}
      <nav className="fixed inset-x-0 bottom-0 z-30 border-t border-slate-200 bg-white/95 pb-[env(safe-area-inset-bottom)] backdrop-blur lg:hidden">
        <div className="mx-auto grid max-w-xl grid-cols-5 items-end">
          {basso.map((v) =>
            v.to === "/app/tutor" ? (
              <Link key={v.to} to={v.to} className="flex flex-col items-center pb-2 text-center text-[11px] leading-tight font-semibold">
                <span
                  className={cx(
                    "-mt-6 grid size-14 place-items-center rounded-full bg-gradient-to-br from-brand-950 via-brand-700 to-fuchsia-600 text-accent-300 shadow-lg shadow-brand-900/40 ring-4 ring-white transition",
                    attiva(v) && "scale-105",
                  )}
                >
                  <v.Icon className="size-6" />
                </span>
                <span className={cx("mt-1", attiva(v) ? "text-brand-700" : "text-slate-600")}>{v.label}</span>
              </Link>
            ) : (
              <Link
                key={v.to}
                to={destinazione(v)}
                aria-current={attiva(v) ? "page" : undefined}
                className={cx(
                  "flex flex-col items-center gap-0.5 py-2.5 text-center text-[11px] leading-tight font-semibold",
                  attiva(v) ? "text-brand-600" : "text-slate-500",
                )}
              >
                <span className="relative">
                  <v.Icon className="size-5" />
                  {notifica(v)}
                </span>
                {v.label}
              </Link>
            ),
          )}
        </div>
      </nav>
    </div>
  );
}
