import { nomeConcorso } from "@imieiconcorsi/core/concorsi";
import { MATERIE, nomeMateria, PIANI } from "@imieiconcorsi/core/domain";
import { ArrowRight, BookOpenCheck, CheckCircle2, Clock, Database, Search, Sparkles, Timer, Trophy } from "lucide-react";
import { Link } from "react-router";
import { IconaMateria } from "../../components/brand";
import { ConcorsoCard } from "../../components/ConcorsoCard";
import { Alert, Badge, Button, ButtonLink, Card, EmptyState, ProgressBar, Spinner, UpgradeBanner } from "../../components/ui";
import { useApi, type ConcorsoApi, type Statistiche } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { dataBreve, durata, giorniA } from "../../lib/format";
import { useAvviaSessione } from "../../lib/sessioni";

// Dashboard (/app): concorsi seguiti, statistiche (risposte per materia, andamento delle
// simulazioni), ultime sessioni e scorciatoie per studiare.

/** Pagina /app. */
export function Dashboard() {
  const { utente } = useUtente();
  const seguiti = useApi<{ concorsi: ConcorsoApi[] }>("/me/concorsi");
  const stats = useApi<Statistiche>("/me/statistiche");
  const { avvia, inCorso, errore, chiudiErrore } = useAvviaSessione();

  const prossimo = seguiti.data?.concorsi[0];
  const giorni = giorniA(prossimo?.scadenza);

  // La materia su cui l'utente va peggio (o si sente più debole) è quella da allenare oggi.
  // Solo le materie della banca statica (le banche dati hanno righe a parte).
  const perMateria = (stats.data?.perMateria ?? []).filter((m) => MATERIE.some((x) => x.id === m.materia));
  const perBancaDati = stats.data?.perBancaDati ?? [];
  const materiaDebole =
    perMateria.slice().sort((a, b) => a.percentuale - b.percentuale)[0]?.materia ??
    MATERIE.slice().sort((a, b) => (utente.livelli[a.id] ?? 3) - (utente.livelli[b.id] ?? 3))[0].id;

  return (
    <div className="space-y-8">
      {/* Benvenuto */}
      <section className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-brand-700 via-brand-600 to-fuchsia-600 p-6 text-white shadow-xl shadow-brand-600/20 sm:p-8">
        <div aria-hidden className="absolute -top-16 -right-16 size-64 rounded-full bg-white/10 blur-2xl" />
        <div className="relative flex flex-wrap items-end justify-between gap-6">
          <div>
            <p className="text-sm font-semibold text-brand-100">Ciao{utente.nome ? `, ${utente.nome}` : ""} 👋</p>
            <h1 className="mt-1 text-2xl font-extrabold tracking-tight sm:text-3xl">
              {prossimo
                ? giorni !== undefined && giorni >= 0
                  ? `Mancano ${giorni} giorni alla scadenza del tuo concorso`
                  : "Continua a prepararti"
                : "Scegli il concorso da preparare"}
            </h1>
            {prossimo && <p className="mt-1 line-clamp-1 max-w-xl text-brand-100">{nomeConcorso(prossimo)}</p>}
          </div>
          <div className="flex flex-wrap gap-2">
            <Button
              variant="accent"
              loading={inCorso === "studio"}
              onClick={() => void avvia({ tipo: "studio", materie: [materiaDebole], numero: 10 })}
            >
              <BookOpenCheck className="size-4" /> Studia {nomeMateria(materiaDebole).toLowerCase()}
            </Button>
            {prossimo && (
              <Button
                variant="secondary"
                loading={inCorso === "simulazione"}
                onClick={() => void avvia({ tipo: "simulazione", concorsoId: prossimo.id, numero: 60 })}
              >
                <Timer className="size-4" /> Simulazione
              </Button>
            )}
          </div>
        </div>
      </section>

      {errore &&
        (errore.code === "LIMITE_PIANO" ? (
          <UpgradeBanner message={errore.message} onClose={chiudiErrore} />
        ) : (
          <Alert tone="error" onClose={chiudiErrore}>
            {errore.message}
          </Alert>
        ))}

      <div className="grid gap-8 lg:grid-cols-[1.4fr_1fr]">
        {/* Concorsi seguiti (min-w-0: sul telefono la colonna non si allarga oltre lo schermo) */}
        <section className="min-w-0">
          <div className="mb-4 flex items-center justify-between">
            <h2 className="text-lg font-bold text-slate-900">I tuoi concorsi</h2>
            <Link to="/app/concorsi" className="inline-flex items-center gap-1 text-sm font-semibold text-brand-600 hover:text-brand-700">
              Trova altri <ArrowRight className="size-4" />
            </Link>
          </div>
          {seguiti.loading ? (
            <Spinner />
          ) : seguiti.data?.concorsi.length ? (
            <div className="grid gap-4">
              {seguiti.data.concorsi.map((c) => (
                <ConcorsoCard key={c.id} concorso={c} />
              ))}
            </div>
          ) : (
            <EmptyState
              icon={<Search className="size-6" />}
              title="Non segui ancora nessun concorso"
              action={<ButtonLink to="/app/concorsi">Cerca tra i bandi aperti</ButtonLink>}
            >
              Seguine uno per avere il conto alla rovescia e le simulazioni sulle sue materie.
            </EmptyState>
          )}
        </section>

        {/* Progressi */}
        <section className="min-w-0 space-y-4">
          <h2 className="text-lg font-bold text-slate-900">I tuoi progressi</h2>
          {stats.loading ? (
            <Spinner />
          ) : (
            <>
              <div className="grid grid-cols-3 gap-3 sm:gap-4">
                <Card>
                  <BookOpenCheck className="size-5 text-brand-500" />
                  <p className="mt-2 text-2xl font-extrabold">{stats.data?.domandeRisposte ?? 0}</p>
                  <p className="text-sm text-slate-500">domande risposte</p>
                </Card>
                {/* Giuste sul totale, con la percentuale. */}
                <Card>
                  <CheckCircle2 className="size-5 text-emerald-500" />
                  <p className="mt-2 text-2xl font-extrabold">{stats.data?.risposteCorrette ?? 0}</p>
                  <p className="text-sm text-slate-500">
                    risposte corrette
                    {!!stats.data?.domandeRisposte && (
                      <span className="block font-semibold text-emerald-700">
                        {Math.round(((stats.data.risposteCorrette ?? 0) / stats.data.domandeRisposte) * 100)}%
                      </span>
                    )}
                  </p>
                </Card>
                <Card>
                  <Trophy className="size-5 text-accent-500" />
                  <p className="mt-2 text-2xl font-extrabold">{stats.data?.simulazioni.filter((s) => s.superata).length ?? 0}</p>
                  <p className="text-sm text-slate-500">simulazioni superate</p>
                </Card>
              </div>

              {/* Le materie di studio e le banche dati ufficiali in due riquadri separati. */}
              <Card>
                <p className="mb-4 font-semibold text-slate-900">Risposte giuste per materia</p>
                {perMateria.length ? (
                  <ul className="space-y-3">
                    {perMateria.map((m) => {
                      const info = MATERIE.find((x) => x.id === m.materia)!;
                      return (
                        <li key={m.materia} className="flex items-center gap-3">
                          <IconaMateria icona={info.icona} materia={m.materia} piccola />
                          <div className="min-w-0 flex-1">
                            <div className="flex justify-between gap-2 text-sm">
                              <span className="truncate font-medium">{info.nome}</span>
                              <span className="font-semibold text-slate-600">{m.percentuale}%</span>
                            </div>
                            <ProgressBar value={m.percentuale} tone={m.percentuale >= 70 ? "green" : m.percentuale >= 50 ? "amber" : "red"} className="mt-1" />
                          </div>
                        </li>
                      );
                    })}
                  </ul>
                ) : (
                  <p className="text-sm text-slate-500">Completa una sessione di studio sulle materie per vedere i tuoi punti forti e deboli.</p>
                )}
              </Card>

              {perBancaDati.length > 0 && (
                <Card>
                  <p className="mb-4 font-semibold text-slate-900">Risultati nelle banche dati ufficiali</p>
                  <ul className="space-y-3">
                    {perBancaDati.map((b) => (
                      <li key={b.bancaId} className="flex items-center gap-3">
                        <span className="grid size-8 shrink-0 place-items-center rounded-lg bg-brand-50 text-brand-600">
                          <Database className="size-4" />
                        </span>
                        <div className="min-w-0 flex-1">
                          <div className="flex justify-between gap-2 text-sm">
                            <Link to={`/app/banche-dati/${b.bancaId}`} className="truncate font-medium hover:text-brand-700">
                              {b.titolo}
                            </Link>
                            <span className="shrink-0 font-semibold text-slate-600">{b.percentuale}%</span>
                          </div>
                          <ProgressBar value={b.percentuale} tone={b.percentuale >= 70 ? "green" : b.percentuale >= 50 ? "amber" : "red"} className="mt-1" />
                          <p className="mt-0.5 text-xs text-slate-500">
                            {b.corrette} giuste su {b.totale} risposte
                          </p>
                        </div>
                      </li>
                    ))}
                  </ul>
                </Card>
              )}

              {!!stats.data?.recenti.length && (
                <Card>
                  <p className="mb-3 font-semibold text-slate-900">Ultime sessioni</p>
                  <ul className="divide-y divide-slate-100">
                    {stats.data.recenti.map((s) => (
                      <li key={s.id}>
                        <Link to={`/app/sessione/${s.id}`} className="flex items-center gap-3 py-2.5 text-sm hover:text-brand-700">
                          <Clock className="size-4 shrink-0 text-slate-400" />
                          <span className="min-w-0 flex-1">
                            <span className="block truncate">
                              {s.bancaDati
                                ? `${s.tipo === "simulazione" ? "Prova finale" : "Studio"} · ${s.bancaDati}`
                                : s.tipo === "simulazione"
                                  ? "Prova finale"
                                  : `Studio · ${s.materie.map(nomeMateria).join(", ")}`}
                            </span>
                            <span className="block text-xs text-slate-400">
                              {dataBreve(s.data)}
                              {s.tipo === "simulazione" && s.durataMs !== undefined && ` · ${durata(s.durataMs)}`}
                            </span>
                          </span>
                          <Badge tone={s.percentuale >= 70 ? "green" : "slate"}>{s.percentuale}%</Badge>
                        </Link>
                      </li>
                    ))}
                  </ul>
                </Card>
              )}

              {utente.piano === "free" && (
                <Card className="bg-gradient-to-br from-amber-50 to-white ring-amber-200">
                  <Sparkles className="size-5 text-accent-500" />
                  <p className="mt-2 font-semibold">Sblocca tutto con {PIANI.medium.nome}</p>
                  <p className="mt-1 text-sm text-slate-600">Concorsi illimitati e simulazioni senza limiti settimanali.</p>
                  <ButtonLink to="/app/piani" variant="accent" size="sm" className="mt-3">
                    Scopri i piani
                  </ButtonLink>
                </Card>
              )}
            </>
          )}
        </section>
      </div>
    </div>
  );
}
