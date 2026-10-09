import {
  BookOpen,
  Briefcase,
  Calculator,
  Coins,
  Gavel,
  Globe,
  Hourglass,
  Landmark,
  Languages,
  Monitor,
  Puzzle,
  Scale,
  type LucideIcon,
} from "lucide-react";
import type { MateriaApi } from "../lib/api";
import { cx } from "./ui";

// Elementi grafici del marchio: logo, icone e colori delle materie, icone di Google e Facebook.

/** Logo di iMieiConcorsi; `light` per gli sfondi scuri. */
export function Logo({ className, light }: { className?: string; light?: boolean }) {
  return (
    <span className={cx("inline-flex items-center gap-2 font-extrabold tracking-tight", className)}>
      <svg viewBox="0 0 32 32" className="size-8" aria-hidden>
        <rect width="32" height="32" rx="9" fill={light ? "#fff" : "#4f46e5"} />
        <path d="M9 17.5l4.5 4.5L23 11" fill="none" stroke={light ? "#4f46e5" : "#fbbf24"} strokeWidth="3.5" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
      <span className={light ? "text-white" : "text-slate-900"}>
        iMiei<span className={light ? "text-accent-300" : "text-brand-600"}>Concorsi</span>
      </span>
    </span>
  );
}

/** Icona di ogni materia (il nome viene da MATERIE in core/domain.ts). */
const ICONE: Record<MateriaApi["icona"], LucideIcon> = {
  scale: Scale,
  landmark: Landmark,
  "book-open": BookOpen,
  hourglass: Hourglass,
  puzzle: Puzzle,
  monitor: Monitor,
  coins: Coins,
  briefcase: Briefcase,
  gavel: Gavel,
  globe: Globe,
  calculator: Calculator,
  languages: Languages,
};

/** Colori di sfondo e testo di ogni materia, per riconoscerle a colpo d'occhio. */
export const COLORI_MATERIA: Record<string, string> = {
  "diritto-amministrativo": "bg-indigo-50 text-indigo-600",
  "diritto-costituzionale": "bg-sky-50 text-sky-600",
  italiano: "bg-rose-50 text-rose-600",
  storia: "bg-amber-50 text-amber-600",
  logica: "bg-emerald-50 text-emerald-600",
  informatica: "bg-violet-50 text-violet-600",
  "contabilita-pubblica": "bg-teal-50 text-teal-600",
  "diritto-lavoro": "bg-orange-50 text-orange-600",
  "diritto-penale": "bg-red-50 text-red-600",
  geografia: "bg-lime-50 text-lime-700",
  matematica: "bg-cyan-50 text-cyan-600",
  inglese: "bg-fuchsia-50 text-fuchsia-600",
};

/** Icona colorata di una materia. */
export function IconaMateria({ icona, materia, className }: { icona: MateriaApi["icona"]; materia: string; className?: string }) {
  const Icon = ICONE[icona];
  return (
    <span className={cx("grid size-10 shrink-0 place-items-center rounded-xl", COLORI_MATERIA[materia], className)}>
      <Icon className="size-5" />
    </span>
  );
}

/** Logo di Google per il pulsante di accesso. */
export function GoogleIcon({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" className={className} aria-hidden>
      <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 0 1-2.2 3.32v2.77h3.57c2.08-1.92 3.27-4.74 3.27-8.1z" />
      <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84A11 11 0 0 0 12 23z" />
      <path fill="#FBBC05" d="M5.84 14.09A6.6 6.6 0 0 1 5.5 12c0-.73.13-1.43.34-2.09V7.07H2.18A11 11 0 0 0 1 12c0 1.78.43 3.45 1.18 4.93l3.66-2.84z" />
      <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1A11 11 0 0 0 2.18 7.07l3.66 2.84C6.71 7.31 9.14 5.38 12 5.38z" />
    </svg>
  );
}

/** Logo di Facebook per il pulsante di accesso. */
export function FacebookIcon({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" className={className} aria-hidden>
      <path fill="#1877F2" d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.04V9.41c0-3.02 1.8-4.7 4.54-4.7 1.31 0 2.68.24 2.68.24v2.97h-1.5c-1.5 0-1.96.93-1.96 1.89v2.26h3.33l-.53 3.5h-2.8V24C19.62 23.1 24 18.1 24 12.07z" />
      <path fill="#fff" d="M16.67 15.56l.53-3.49h-3.33V9.81c0-.96.47-1.89 1.96-1.89h1.51V4.95s-1.37-.24-2.68-.24c-2.74 0-4.53 1.68-4.53 4.7v2.66H7.08v3.49h3.05V24a12.2 12.2 0 0 0 3.74 0v-8.44h2.8z" />
    </svg>
  );
}
