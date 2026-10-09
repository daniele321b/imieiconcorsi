import { ArrowLeft } from "lucide-react";
import type { ReactNode } from "react";
import { Link } from "react-router";
import { Logo } from "../../components/brand";
import { Alert } from "../../components/ui";
import { data } from "../../lib/format";
import { LEGALE, legaleInBozza } from "../../lib/legale";

/** Impaginazione comune di Privacy, Termini ed Eliminazione dati (pagine pubbliche). */
export function LegalePagina({ titolo, children }: { titolo: string; children: ReactNode }) {
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
        <p className="mt-2 text-sm text-slate-500">Versione del {data(LEGALE.versione)}</p>
        {legaleInBozza && (
          <div className="mt-6">
            <Alert tone="error">
              Bozza: mancano i dati del titolare (packages/web/src/lib/legale.ts) e il testo va fatto rivedere da un legale prima
              del lancio.
            </Alert>
          </div>
        )}
        <article className="legale mt-8 space-y-4 text-slate-700">{children}</article>
      </main>
      <PiePagina />
    </div>
  );
}

export function PiePagina({ scuro }: { scuro?: boolean }) {
  const cls = scuro ? "text-brand-200/70 hover:text-white" : "text-slate-500 hover:text-slate-800";
  return (
    <footer className="mx-auto flex max-w-6xl flex-wrap items-center justify-center gap-x-5 gap-y-1 px-4 py-6 text-xs">
      <span className={scuro ? "text-brand-200/50" : "text-slate-400"}>© {new Date().getFullYear()} iMieiConcorsi</span>
      <Link to="/privacy" className={cls}>
        Privacy
      </Link>
      <Link to="/termini" className={cls}>
        Termini e condizioni
      </Link>
      <Link to="/eliminazione-dati" className={cls}>
        Eliminazione dei dati
      </Link>
    </footer>
  );
}
