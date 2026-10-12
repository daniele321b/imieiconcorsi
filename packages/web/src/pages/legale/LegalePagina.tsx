import { ArrowLeft } from "lucide-react";
import type { ReactNode } from "react";
import { Link } from "react-router";
import { Logo } from "../../components/brand";
import { data } from "../../lib/format";
import { LEGALE } from "../../lib/legale";

/**
 * Impaginazione comune delle pagine pubbliche (Privacy, Termini, Chi siamo, Prezzi, Contatti…).
 * `versione` = mostra la data della versione (per i documenti legali).
 */
export function LegalePagina({ titolo, sotto, versione = true, children }: { titolo: string; sotto?: string; versione?: boolean; children: ReactNode }) {
  return (
    <div className="min-h-screen bg-slate-50">
      <header className="border-b border-slate-200 bg-white">
        <div className="mx-auto flex h-16 max-w-3xl items-center justify-between px-4 sm:px-6">
          <Link to="/">
            <Logo />
          </Link>
          <Link to="/" className="inline-flex items-center gap-1 text-sm font-semibold text-slate-500 hover:text-slate-800">
            <ArrowLeft className="size-4" /> Torna al sito
          </Link>
        </div>
      </header>
      <main className="mx-auto max-w-3xl px-4 py-10 sm:px-6">
        <h1 className="text-3xl font-extrabold tracking-tight text-slate-900">{titolo}</h1>
        {sotto && <p className="mt-2 text-lg text-slate-600">{sotto}</p>}
        {versione && <p className="mt-2 text-sm text-slate-500">Versione del {data(LEGALE.versione)}</p>}
        <article className="legale mt-8 space-y-4 text-slate-700">{children}</article>
      </main>
      <PiePagina />
    </div>
  );
}

/** Link del piè di pagina, in tutte le pagine pubbliche e nell'app. */
const LINK_PIE = [
  { to: "/chi-siamo", nome: "Chi siamo" },
  { to: "/prezzi", nome: "Prezzi" },
  { to: "/domande-frequenti", nome: "Domande frequenti" },
  { to: "/contatti", nome: "Contatti" },
  { to: "/email", nome: "Le nostre email" },
  { to: "/privacy", nome: "Privacy" },
  { to: "/cookie", nome: "Cookie" },
  { to: "/termini", nome: "Termini e condizioni" },
  { to: "/eliminazione-dati", nome: "Eliminazione dei dati" },
];

/** Piè di pagina con i link alle pagine pubbliche; `scuro` per la home. */
export function PiePagina({ scuro }: { scuro?: boolean }) {
  const cls = scuro ? "text-brand-200/70 hover:text-white" : "text-slate-500 hover:text-slate-800";
  return (
    <footer className="mx-auto flex max-w-6xl flex-wrap items-center justify-center gap-x-5 gap-y-1.5 px-4 py-6 text-xs">
      <span className={scuro ? "text-brand-200/50" : "text-slate-400"}>
        © {new Date().getFullYear()} {LEGALE.nome}
      </span>
      {LINK_PIE.map((l) => (
        <Link key={l.to} to={l.to} className={cls}>
          {l.nome}
        </Link>
      ))}
    </footer>
  );
}
