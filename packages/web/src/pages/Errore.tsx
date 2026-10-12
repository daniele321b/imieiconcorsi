import { AlertTriangle, RotateCcw } from "lucide-react";
import { useRouteError } from "react-router";
import { Logo } from "../components/brand";
import { Button } from "../components/ui";

// Pagina mostrata quando una pagina va in errore (errorElement delle route in main.tsx), al
// posto della schermata tecnica di React. Il dettaglio resta nella console del browser.

/** Errore imprevisto: messaggio comprensibile e i due modi per ripartire. */
export function Errore() {
  const errore = useRouteError();
  console.error(errore);
  return (
    <div className="grid min-h-screen place-items-center bg-slate-50 p-6">
      <div className="w-full max-w-md space-y-5 rounded-3xl bg-white p-8 text-center shadow-sm ring-1 ring-slate-200">
        <div className="flex justify-center">
          <Logo />
        </div>
        <AlertTriangle className="mx-auto size-10 text-amber-500" />
        <div>
          <h1 className="text-xl font-extrabold text-slate-900">Qualcosa è andato storto</h1>
          <p className="mt-2 text-sm text-slate-500">
            La pagina ha avuto un problema. I tuoi dati sono al sicuro: riprova, oppure torna alla dashboard. Se succede di nuovo,
            scrivici dall'Assistenza.
          </p>
        </div>
        <div className="flex flex-wrap justify-center gap-3">
          <Button variant="secondary" onClick={() => window.location.reload()}>
            <RotateCcw className="size-4" /> Riprova
          </Button>
          <Button onClick={() => window.location.assign("/app")}>Torna alla dashboard</Button>
        </div>
      </div>
    </div>
  );
}
