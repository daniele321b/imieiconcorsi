import { BookOpenCheck } from "lucide-react";
import { IconaMateria } from "../../components/brand";
import { Alert, Button, Card, PageHeader, Spinner, UpgradeBanner, cx } from "../../components/ui";
import { useApi, type MateriaApi } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { useAvviaSessione } from "../../lib/sessioni";

export function Studio() {
  const { utente } = useUtente();
  const { data, loading, error } = useApi<{ materie: MateriaApi[] }>("/materie");
  const { avvia, inCorso, errore, chiudiErrore } = useAvviaSessione();
  const numero = utente.limiti.domandePerSessioneStudio;

  return (
    <div>
      <PageHeader
        title="Studio"
        subtitle={`Sessioni da ${Math.min(10, numero)} domande con la spiegazione subito dopo ogni risposta.`}
      />

      <div className="space-y-4">
        {errore &&
          (errore.code === "LIMITE_PIANO" ? (
            <UpgradeBanner message={errore.message} onClose={chiudiErrore} />
          ) : (
            <Alert tone="error" onClose={chiudiErrore}>
              {errore.message}
            </Alert>
          ))}
        {error && <Alert tone="error">{error.message}</Alert>}

        {loading ? (
          <Spinner />
        ) : (
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {data?.materie.map((m) => (
              <Card key={m.id} className="flex flex-col">
                <div className="flex items-center gap-3">
                  <IconaMateria icona={m.icona} materia={m.id} className="size-12" />
                  <div>
                    <p className="font-bold text-slate-900">{m.nome}</p>
                    <p className="text-sm text-slate-500">{m.domande} domande disponibili</p>
                  </div>
                </div>
                <div className="mt-4 flex items-center gap-1.5" aria-label={`Il tuo livello: ${m.livello ?? "non indicato"}`}>
                  {[1, 2, 3, 4, 5].map((n) => (
                    <span key={n} className={cx("h-1.5 flex-1 rounded-full", m.livello && n <= m.livello ? "bg-brand-500" : "bg-slate-100")} />
                  ))}
                </div>
                <p className="mt-1 text-xs text-slate-500">Il tuo livello {m.livello ? `${m.livello}/5` : "non indicato"}</p>
                <Button
                  className="mt-5"
                  disabled={!m.domande}
                  loading={inCorso === m.id}
                  onClick={() => void avvia({ tipo: "studio", materie: [m.id], numero: Math.min(10, numero) }, m.id)}
                >
                  <BookOpenCheck className="size-4" /> {m.domande ? "Inizia" : "In arrivo"}
                </Button>
              </Card>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
