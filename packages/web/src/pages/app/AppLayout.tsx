import { PIANI } from "@imieiconcorsi/core/domain";
import { BookOpenCheck, Crown, Database, LayoutDashboard, LogOut, Search, ShieldCheck, User } from "lucide-react";
import { Navigate, NavLink, Outlet, useLocation } from "react-router";
import { Logo } from "../../components/brand";
import { Badge, FullPageSpinner, cx } from "../../components/ui";
import { useAuth } from "../../lib/auth";
import { PiePagina } from "../legale/LegalePagina";

const NAV = [
  { to: "/app", label: "Dashboard", Icon: LayoutDashboard, end: true },
  { to: "/app/concorsi", label: "Concorsi", Icon: Search },
  { to: "/app/studio", label: "Studio", Icon: BookOpenCheck },
  { to: "/app/banche-dati", label: "Banche dati", Icon: Database },
  { to: "/app/piani", label: "Piani", Icon: Crown },
];

export function AppLayout() {
  const { stato, utente, esci } = useAuth();
  const { pathname } = useLocation();

  if (stato === "caricamento") return <FullPageSpinner />;
  if (stato === "ospite" || !utente) return <Navigate to="/" replace />;
  if (!utente.onboarded && pathname !== "/app/onboarding") return <Navigate to="/app/onboarding" replace />;
  if (pathname === "/app/onboarding") return <Outlet />;

  const piano = PIANI[utente.piano];
  // L'admin ha tutte le funzioni: niente piani da comprare, al loro posto il pannello.
  const voci = utente.admin
    ? [...NAV.filter((v) => v.to !== "/app/piani"), { to: "/admin", label: "Admin", Icon: ShieldCheck, end: false }]
    : NAV;

  return (
    <div className="min-h-screen pb-20 md:pb-0">
      <header className="sticky top-0 z-30 border-b border-slate-200/70 bg-white/80 backdrop-blur">
        <div className="mx-auto flex h-16 max-w-6xl items-center gap-6 px-4 sm:px-6">
          <NavLink to="/app">
            <Logo />
          </NavLink>
          <nav className="hidden items-center gap-1 md:flex">
            {voci.map(({ to, label, Icon, end }) => (
              <NavLink
                key={to}
                to={to}
                end={end}
                className={({ isActive }) =>
                  cx(
                    "inline-flex items-center gap-2 rounded-lg px-3 py-2 text-sm font-semibold transition",
                    isActive ? "bg-brand-50 text-brand-700" : "text-slate-600 hover:bg-slate-100 hover:text-slate-900",
                  )
                }
              >
                <Icon className="size-4" /> {label}
              </NavLink>
            ))}
          </nav>
          <div className="ml-auto flex items-center gap-2">
            {utente.admin ? (
              <NavLink to="/admin" className="hidden sm:block">
                <Badge tone="amber">
                  <ShieldCheck className="size-3" /> Admin
                </Badge>
              </NavLink>
            ) : (
              <NavLink to="/app/piani" className="hidden sm:block">
                <Badge tone={utente.piano === "free" ? "slate" : "amber"}>
                  {utente.piano !== "free" && <Crown className="size-3" />} {piano.nome}
                </Badge>
              </NavLink>
            )}
            <NavLink
              to="/app/profilo"
              aria-label="Profilo"
              className="grid size-9 place-items-center rounded-full bg-brand-600 text-sm font-bold text-white"
            >
              {(utente.nome ?? utente.email ?? "?").charAt(0).toUpperCase()}
            </NavLink>
            <button onClick={() => void esci()} aria-label="Esci" className="hidden rounded-lg p-2 text-slate-500 hover:bg-slate-100 md:block">
              <LogOut className="size-4" />
            </button>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-6xl px-4 py-8 sm:px-6">
        <Outlet />
      </main>
      <PiePagina />

      {/* Navigazione in basso su mobile */}
      <nav className="fixed inset-x-0 bottom-0 z-30 grid auto-cols-fr grid-flow-col border-t border-slate-200 bg-white/95 backdrop-blur md:hidden">
        {[...voci.filter((v) => v.to !== "/admin"), { to: "/app/profilo", label: "Profilo", Icon: User, end: false }].map(({ to, label, Icon, end }) => (
          <NavLink
            key={to}
            to={to}
            end={end}
            className={({ isActive }) =>
              cx("flex flex-col items-center gap-0.5 py-2.5 text-center text-[10px] leading-tight font-semibold sm:text-[11px]", isActive ? "text-brand-600" : "text-slate-500")
            }
          >
            <Icon className="size-5" />
            {label}
          </NavLink>
        ))}
      </nav>
    </div>
  );
}
