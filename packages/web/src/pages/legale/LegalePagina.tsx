import { ArrowLeft } from "lucide-react";
import type { ReactNode } from "react";
import { Link } from "react-router";
import { Logo } from "../../components/brand";
import { cx } from "../../components/ui";
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

/**
 * Link del piè di pagina, in tutte le pagine pubbliche e nell'app: sopra il servizio, sotto i
 * documenti legali. "Le nostre email" ed "Eliminazione dei dati" non ci sono: si raggiungono da
 * Privacy e Domande frequenti (e i loro indirizzi restano quelli dati ad AWS e Meta).
 */
const LINK_SERVIZIO = [
  { to: "/chi-siamo", nome: "Chi siamo" },
  { to: "/prezzi", nome: "Prezzi" },
  { to: "/domande-frequenti", nome: "Domande frequenti" },
  { to: "/contatti", nome: "Contatti" },
];
const LINK_LEGALI = [
  { to: "/privacy", nome: "Privacy" },
  { to: "/cookie", nome: "Cookie" },
  { to: "/termini", nome: "Termini" },
];

/** Piè di pagina con i link alle pagine pubbliche, su due righe; `scuro` per la home. */
export function PiePagina({ scuro }: { scuro?: boolean }) {
  const cls = scuro ? "text-brand-200/70 hover:text-white" : "text-slate-500 hover:text-slate-800";
  const tenue = scuro ? "text-brand-200/50" : "text-slate-400";
  return (
    <footer className="mx-auto max-w-6xl space-y-2 px-4 py-6 text-center text-xs">
      <nav className="flex flex-wrap justify-center gap-x-5 gap-y-1.5">
        {LINK_SERVIZIO.map((l) => (
          <Link key={l.to} to={l.to} className={cx("font-semibold", cls)}>
            {l.nome}
          </Link>
        ))}
      </nav>
      <div className="flex flex-wrap justify-center gap-x-4 gap-y-1.5">
        <span className={tenue}>
          © {new Date().getFullYear()} {LEGALE.nome}
        </span>
        {LINK_LEGALI.map((l) => (
          <Link key={l.to} to={l.to} className={cls}>
            {l.nome}
          </Link>
        ))}
      </div>
    </footer>
  );
}
