import { COMPARTI, MATERIE, nomeComparto, nomeMateria, type BancaDati, type CompartoId, type MateriaId } from "@imieiconcorsi/core/domain";
import { ArrowLeft, Database, FileUp, RefreshCw } from "lucide-react";
import { type FormEvent, useEffect, useMemo, useState } from "react";
import { Link, Navigate } from "react-router";
import { Alert, Badge, Button, Card, PageHeader, Spinner, cx } from "../../components/ui";
import { api, ApiError, useApi, type ConcorsoApi } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { dataBreve } from "../../lib/format";

type Formato = BancaDati["formato"];

const FORMATI: { id: Formato; nome: string; spiegazione: string }[] = [
  { id: "auto", nome: "Automatico", spiegazione: "Prova tutti i modi qui sotto e usa quello che trova." },
  { id: "indicata", nome: "Indicata", spiegazione: "Sotto ogni domanda: «Risposta esatta: B»." },
  { id: "segnata", nome: "Segnata", spiegazione: "La giusta ha un segno: * oppure (X)." },
  { id: "chiave", nome: "Tabella soluzioni", spiegazione: "In fondo: «Soluzioni» e poi 1 B, 2 A…" },
  { id: "prima", nome: "Sempre la prima", spiegazione: "Il bando dice che la giusta è sempre la A." },
];

const STATO: Record<BancaDati["stato"], { testo: string; tone: "slate" | "brand" | "green" | "red" | "amber" }> = {
  caricamento: { testo: "in caricamento", tone: "slate" },
  estrazione: { testo: "estrazione in corso", tone: "brand" },
  estratta: { testo: "da controllare", tone: "amber" },
  errore: { testo: "errore", tone: "red" },
  pubblicata: { testo: "pubblicata", tone: "green" },
};

const campo =
  "mt-1 block h-10 w-full rounded-xl border-0 bg-white px-3 text-sm text-slate-900 ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500";

const messaggio = (err: unknown) => (err instanceof ApiError ? err.message : err instanceof Error ? err.message : "Errore di rete");

export function AdminBancheDati() {
  const { utente } = useUtente();
  if (!utente.admin) return <Navigate to="/app" replace />;
  return <Pannello />;
}

function Pannello() {
  const { data, loading, error, reload } = useApi<{ banche: BancaDati[] }>("/admin/banche-dati");
  const inLavorazione = data?.banche.some((b) => b.stato === "caricamento" || b.stato === "estrazione");

  // Mentre una banca dati è in estrazione la lista si aggiorna da sola.
  useEffect(() => {
    if (!inLavorazione) return;
    const t = setInterval(() => void reload(), 5000);
    return () => clearInterval(t);
  }, [inLavorazione, reload]);

  return (
    <div className="space-y-6">
      <Link to="/admin" className="inline-flex items-center gap-1 text-sm font-medium text-slate-500 hover:text-slate-800">
        <ArrowLeft className="size-4" /> Pannello di controllo
      </Link>
      <PageHeader
        title="Banche dati ufficiali"
        subtitle="Carica il PDF di una banca dati: le domande vengono estratte da sole, controlli gli esempi e pubblichi. Le banche dati pubblicate compaiono nella sezione Banche dati (Medium e Pro), divise per comparto; se le colleghi a un concorso, anche le sue simulazioni usano le domande ufficiali."
      />

      <Caricamento onCaricata={() => void reload()} />

      <section className="space-y-3">
        <div className="flex items-center justify-between">
          <h2 className="text-lg font-bold text-slate-900">Caricate</h2>
          <Button variant="ghost" size="sm" onClick={() => void reload()}>
            <RefreshCw className="size-4" /> Aggiorna
          </Button>
        </div>
        {error && <Alert tone="error">{error.message}</Alert>}
        {loading && !data ? (
          <Spinner />
        ) : data?.banche.length ? (
          data.banche.map((b) => <RigaBanca key={b.id} banca={b} onCambio={() => void reload()} />)
        ) : (
          <p className="text-sm text-slate-500">Nessuna banca dati caricata.</p>
        )}
      </section>
    </div>
  );
}

function Caricamento({ onCaricata }: { onCaricata: () => void }) {
  const bandi = useApi<{ concorsi: ConcorsoApi[] }>("/concorsi?comparto=tutti&scaduti=1");
  const [modo, setModo] = useState<"concorso" | "libera">("concorso");
  const [comparto, setComparto] = useState<CompartoId | "">("");
  const [anno, setAnno] = useState(String(new Date().getFullYear()));
  const [cerca, setCerca] = useState("");
  const [soloConBanca, setSoloConBanca] = useState(true);
  const [concorsoId, setConcorsoId] = useState("");
  const [titolo, setTitolo] = useState("");
  const [materia, setMateria] = useState<MateriaId | "">("");
  const [formato, setFormato] = useState<Formato>("auto");
  const [file, setFile] = useState<File>();
  const [fase, setFase] = useState<string>();
  const [esito, setEsito] = useState<{ tone: "success" | "error"; testo: string }>();

  const opzioni = useMemo(() => {
    const q = cerca.trim().toLowerCase();
    return (bandi.data?.concorsi ?? [])
      .filter((c) => !soloConBanca || c.bancaDatiPrevista || c.bancaDati)
      .filter((c) => !q || [c.id, c.ente, c.titolo, c.figura].some((s) => s?.toLowerCase().includes(q)))
      .slice(0, 200);
  }, [bandi.data, cerca, soloConBanca]);

  async function carica(e: FormEvent) {
    e.preventDefault();
    if (!file) return;
    setEsito(undefined);
    try {
      setFase("Preparo il caricamento…");
      const { upload } = await api<{ banca: BancaDati; upload: string }>("/admin/banche-dati", {
        method: "POST",
        body: {
          concorsoId: modo === "concorso" ? concorsoId : undefined,
          comparto: comparto || undefined,
          anno: anno ? Number(anno) : undefined,
          titolo,
          materia: materia || undefined,
          formato,
          nomeFile: file.name,
          dimensione: file.size,
        },
      });
      setFase(`Carico il PDF (${(file.size / 1024 / 1024).toFixed(1)} MB)…`);
      const res = await fetch(upload, { method: "PUT", headers: { "content-type": "application/pdf" }, body: file });
      if (!res.ok) throw new Error(`Caricamento non riuscito (${res.status})`);
      setEsito({ tone: "success", testo: "PDF caricato: l'estrazione è partita. Ti arriva anche un'email quando finisce." });
      setTitolo("");
      setFile(undefined);
      onCaricata();
    } catch (err) {
      setEsito({ tone: "error", testo: messaggio(err) });
    } finally {
      setFase(undefined);
    }
  }

  return (
    <Card className="space-y-4">
      <div className="flex items-center gap-2">
        <FileUp className="size-5 text-brand-600" />
        <h2 className="text-lg font-bold text-slate-900">Carica una banca dati</h2>
      </div>
      <form onSubmit={(e) => void carica(e)} className="grid gap-3 sm:grid-cols-2">
        <div className="sm:col-span-2">
          <div className="inline-grid grid-cols-2 rounded-xl bg-slate-100 p-1 text-sm font-semibold" role="radiogroup">
            {(
              [
                ["concorso", "Collegata a un concorso"],
                ["libera", "Banca dati a sé (per comparto)"],
              ] as const
            ).map(([id, nome]) => (
              <button
                key={id}
                type="button"
                role="radio"
                aria-checked={modo === id}
                onClick={() => setModo(id)}
                className={cx("rounded-lg px-4 py-2 transition", modo === id ? "bg-white text-brand-700 shadow-sm" : "text-slate-600")}
              >
                {nome}
              </button>
            ))}
          </div>
          <p className="mt-1 text-xs text-slate-500">
            {modo === "concorso"
              ? "Le simulazioni Medium e Pro di quel concorso useranno queste domande; la banca dati compare anche nella sezione Banche dati."
              : "Per esempio «Banca dati Polizia di Stato 2026»: compare solo nella sezione Banche dati, sotto il comparto scelto."}
          </p>
        </div>
        <label className="text-xs font-semibold text-slate-500">
          Comparto{modo === "concorso" && " (vuoto = quello del concorso)"}
          <select required={modo === "libera"} value={comparto} onChange={(e) => setComparto(e.target.value as CompartoId | "")} className={campo}>
            <option value="">{modo === "concorso" ? "Come il concorso" : "Scegli…"}</option>
            {COMPARTI.map((c) => (
              <option key={c.id} value={c.id}>
                {c.nome}
              </option>
            ))}
          </select>
        </label>
        <label className="text-xs font-semibold text-slate-500">
          Anno
          <input type="number" min={2000} max={2100} value={anno} onChange={(e) => setAnno(e.target.value)} className={campo} />
        </label>
        {modo === "concorso" && (
        <div className="sm:col-span-2">
          <label className="text-xs font-semibold text-slate-500">
            Concorso
            <input value={cerca} onChange={(e) => setCerca(e.target.value)} placeholder="Cerca per ente, titolo o id inPA…" className={campo} />
          </label>
          <label className="mt-2 flex items-center gap-2 text-sm text-slate-600">
            <input type="checkbox" checked={soloConBanca} onChange={(e) => setSoloConBanca(e.target.checked)} className="size-4 rounded border-slate-300" />
            Solo i bandi che citano una banca dati
          </label>
          {bandi.loading ? (
            <Spinner label="Carico i bandi…" />
          ) : (
            <select required value={concorsoId} onChange={(e) => setConcorsoId(e.target.value)} className={cx(campo, "mt-2")} size={6}>
              {opzioni.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.ente} — {c.figura ?? c.titolo} (scade {dataBreve(c.scadenza)}){c.bancaDati ? " · banca dati pubblicata" : ""}
                </option>
              ))}
            </select>
          )}
        </div>
        )}
        <label className="text-xs font-semibold text-slate-500">
          Titolo della banca dati
          <input required minLength={3} value={titolo} onChange={(e) => setTitolo(e.target.value)} placeholder={modo === "concorso" ? "es. Banca dati prova preselettiva 2026" : "es. Banca dati Polizia di Stato 2026"} className={campo} />
        </label>
        <label className="text-xs font-semibold text-slate-500">
          Materia (se è una sola)
          <select value={materia} onChange={(e) => setMateria(e.target.value as MateriaId | "")} className={campo}>
            <option value="">Più materie / non indicata</option>
            {MATERIE.map((m) => (
              <option key={m.id} value={m.id}>
                {m.nome}
              </option>
            ))}
          </select>
        </label>
        <label className="text-xs font-semibold text-slate-500">
          Risposta giusta nel PDF
          <select value={formato} onChange={(e) => setFormato(e.target.value as Formato)} className={campo}>
            {FORMATI.map((f) => (
              <option key={f.id} value={f.id}>
                {f.nome}
              </option>
            ))}
          </select>
          <span className="mt-1 block font-normal text-slate-400">{FORMATI.find((f) => f.id === formato)?.spiegazione}</span>
        </label>
        <label className="text-xs font-semibold text-slate-500">
          File PDF (testo selezionabile, fino a 200 MB)
          <input
            required
            type="file"
            accept="application/pdf"
            onChange={(e) => setFile(e.target.files?.[0])}
            className="mt-1 block w-full text-sm text-slate-700 file:mr-3 file:rounded-lg file:border-0 file:bg-brand-50 file:px-3 file:py-2 file:font-semibold file:text-brand-700"
          />
        </label>
        <div className="flex items-center gap-3 sm:col-span-2">
          <Button type="submit" loading={!!fase} disabled={!file || (modo === "concorso" ? !concorsoId : !comparto)}>
            <FileUp className="size-4" /> Carica ed estrai
          </Button>
          {fase && <span className="text-sm text-slate-500">{fase}</span>}
        </div>
      </form>
      {esito && (
        <Alert tone={esito.tone} onClose={() => setEsito(undefined)}>
          {esito.testo}
        </Alert>
      )}
    </Card>
  );
}

function RigaBanca({ banca, onCambio }: { banca: BancaDati; onCambio: () => void }) {
  const [aperta, setAperta] = useState(banca.stato === "estratta");
  const [inCorso, setInCorso] = useState<string>();
  const [errore, setErrore] = useState<string>();

  async function azione(nome: string, fn: () => Promise<unknown>) {
    setInCorso(nome);
    setErrore(undefined);
    try {
      await fn();
      onCambio();
    } catch (err) {
      setErrore(messaggio(err));
    } finally {
      setInCorso(undefined);
    }
  }

  const stato = STATO[banca.stato];
  const lavorazione = banca.stato === "caricamento" || banca.stato === "estrazione";

  return (
    <Card className="space-y-3">
      <div className="flex flex-wrap items-start gap-3">
        <Database className="mt-0.5 size-5 shrink-0 text-brand-600" />
        <div className="min-w-0 flex-1">
          <div className="flex flex-wrap items-center gap-2">
            <p className="font-semibold text-slate-900">{banca.titolo}</p>
            <Badge tone={stato.tone}>{stato.testo}</Badge>
          </div>
          <p className="mt-0.5 text-sm text-slate-500">
            {[banca.comparto && nomeComparto(banca.comparto), banca.anno, banca.concorsoTitolo ?? "senza concorso"].filter(Boolean).join(" · ")} ·{" "}
            {banca.nomeFile} · caricata il {dataBreve(banca.caricataIl)}
            {banca.materia && ` · ${nomeMateria(banca.materia)}`}
          </p>
          {banca.domande !== undefined && (
            <p className="mt-1 text-sm text-slate-700">
              <strong>{banca.domande}</strong> domande riconosciute su {banca.pagine} pagine
              {!!banca.scartate && <>, {banca.scartate} scartate</>}
              {banca.formati && Object.keys(banca.formati).length > 0 && (
                <span className="text-slate-500">
                  {" "}
                  (risposta giusta: {Object.entries(banca.formati).map(([f, n]) => `${FORMATI.find((x) => x.id === f)?.nome.toLowerCase() ?? f} ${n}`).join(", ")})
                </span>
              )}
            </p>
          )}
          {banca.errore && <p className="mt-1 text-sm text-rose-600">{banca.errore}</p>}
        </div>
        <div className="flex flex-wrap items-center gap-2">
          {lavorazione && <Spinner label="" />}
          {(banca.stato === "estratta" || banca.stato === "errore") && (
            <select
              value={banca.formato}
              disabled={!!inCorso}
              onChange={(e) =>
                void azione("formato", () => api(`/admin/banche-dati/${banca.id}`, { method: "PUT", body: { formato: e.target.value } }))
              }
              className="h-9 rounded-xl border-0 bg-white px-2 text-sm ring-1 ring-slate-300"
              title="Cambiando il formato l'estrazione riparte"
            >
              {FORMATI.map((f) => (
                <option key={f.id} value={f.id}>
                  {f.nome}
                </option>
              ))}
            </select>
          )}
          {(banca.stato === "estratta" || banca.stato === "errore") && (
            <Button variant="ghost" size="sm" loading={inCorso === "estrai"} onClick={() => void azione("estrai", () => api(`/admin/banche-dati/${banca.id}/estrai`, { method: "POST" }))}>
              Rifai estrazione
            </Button>
          )}
          {banca.stato === "estratta" && !!banca.domande && (
            <Button size="sm" loading={inCorso === "pubblica"} onClick={() => void azione("pubblica", () => api(`/admin/banche-dati/${banca.id}/pubblica`, { method: "POST" }))}>
              Pubblica {banca.domande} domande
            </Button>
          )}
          {banca.stato === "pubblicata" && (
            <Button variant="secondary" size="sm" loading={inCorso === "ritira"} onClick={() => void azione("ritira", () => api(`/admin/banche-dati/${banca.id}/ritira`, { method: "POST" }))}>
              Ritira
            </Button>
          )}
          {!!banca.esempi?.length && (
            <Button variant="ghost" size="sm" onClick={() => setAperta((a) => !a)}>
              {aperta ? "Nascondi esempi" : "Vedi esempi"}
            </Button>
          )}
        </div>
      </div>

      {errore && <Alert tone="error">{errore}</Alert>}

      {aperta && !!banca.esempi?.length && (
        <div className="space-y-3 rounded-xl bg-slate-50 p-4 text-sm">
          <p className="font-semibold text-slate-700">Prime domande estratte: controlla che testo, risposte e giusta (in verde) siano corretti</p>
          {banca.esempi.map((d) => (
            <div key={d.numero}>
              <p className="font-medium text-slate-900">
                {d.numero}. {d.testo}
              </p>
              <ul className="mt-1 space-y-0.5">
                {d.opzioni.map((o, i) => (
                  <li key={i} className={i === d.corretta ? "font-semibold text-emerald-700" : "text-slate-600"}>
                    {String.fromCharCode(65 + i)}) {o}
                  </li>
                ))}
              </ul>
            </div>
          ))}
          {!!banca.problemi?.length && (
            <div>
              <p className="font-semibold text-slate-700">Scartate (prime {banca.problemi.length})</p>
              <ul className="mt-1 text-slate-600">
                {banca.problemi.map((p) => (
                  <li key={p.numero}>
                    n. {p.numero}: {p.motivo}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </Card>
  );
}
