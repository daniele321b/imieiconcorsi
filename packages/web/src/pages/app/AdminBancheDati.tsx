import { concorsiSuggeriti, scaduto, type ConcorsoInLista } from "@imieiconcorsi/core/concorsi";
import {
  COMPARTI,
  COMPARTO_IDS,
  concorsiDellaBanca,
  MATERIE,
  nomeComparto,
  nomeConcorsoBreve,
  nomeMateria,
  type BancaDati,
  type CompartoId,
  type MateriaId,
} from "@imieiconcorsi/core/domain";
import { ArrowLeft, Database, FileUp, Link2, Loader2, Plus, RefreshCw, Trash2, X } from "lucide-react";
import { type FormEvent, type ReactNode, useEffect, useMemo, useState } from "react";
import { Link, Navigate } from "react-router";
import { Alert, Badge, Button, Card, PageHeader, Spinner, cx } from "../../components/ui";
import { api, ApiError, useApi } from "../../lib/api";
import { caricaBandi } from "../../lib/bandi";
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

// Pannello admin → Banche dati (/admin/banche-dati): carica il PDF di una banca dati ufficiale,
// collegala ai concorsi (suggeriti tra i bandi aperti simili o cercati a mano, anche dopo),
// segui l'estrazione, controlla gli esempi, poi pubblica, ritira o elimina. Il PDF va
// direttamente su S3 con un link firmato dal backend.

/** Pagina /admin/banche-dati: chi non è admin torna all'app. */
export function AdminBancheDati() {
  const { utente } = useUtente();
  if (!utente.admin) return <Navigate to="/app" replace />;
  return <Pannello />;
}

/** Elenco delle banche dati e modulo di caricamento. */
function Pannello() {
  const { data, loading, error, reload } = useApi<{ banche: BancaDati[] }>("/admin/banche-dati");
  const { bandi, errore: erroreBandi } = useBandi();
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

      {erroreBandi && <Alert tone="error">Elenco dei bandi non disponibile: {erroreBandi}</Alert>}
      <Caricamento bandi={bandi} onCaricata={() => void reload()} />

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
          data.banche.map((b) => <RigaBanca key={b.id} banca={b} bandi={bandi} onCambio={() => void reload()} />)
        ) : (
          <p className="text-sm text-slate-500">Nessuna banca dati caricata.</p>
        )}
      </section>
    </div>
  );
}

/** Tutti i bandi (aperti e chiusi da poco), dalla lista in cache: per suggerire e cercare i concorsi da collegare. */
function useBandi() {
  const [bandi, setBandi] = useState<ConcorsoInLista[]>();
  const [errore, setErrore] = useState<string>();
  useEffect(() => {
    caricaBandi(COMPARTO_IDS)
      .then(setBandi)
      .catch((err) => setErrore(messaggio(err)));
  }, []);
  return { bandi, errore };
}

/** Modulo per caricare una nuova banca dati (comparto e anno, titolo, concorsi da collegare, formato, PDF). */
function Caricamento({ bandi, onCaricata }: { bandi?: ConcorsoInLista[]; onCaricata: () => void }) {
  const [comparto, setComparto] = useState<CompartoId | "">("");
  const [anno, setAnno] = useState(String(new Date().getFullYear()));
  const [collegati, setCollegati] = useState<{ id: string; titolo: string; comparto: CompartoId }[]>([]);
  const [titolo, setTitolo] = useState("");
  const [materia, setMateria] = useState<MateriaId | "">("");
  const [formato, setFormato] = useState<Formato>("auto");
  const [file, setFile] = useState<File>();
  const [fase, setFase] = useState<string>();
  const [esito, setEsito] = useState<{ tone: "success" | "error"; testo: string }>();

  async function carica(e: FormEvent) {
    e.preventDefault();
    if (!file) return;
    setEsito(undefined);
    try {
      setFase("Preparo il caricamento…");
      const { upload } = await api<{ banca: BancaDati; upload: string }>("/admin/banche-dati", {
        method: "POST",
        body: {
          concorsiIds: collegati.map((c) => c.id),
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
      setCollegati([]);
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
        <label className="text-xs font-semibold text-slate-500 sm:col-span-2">
          Titolo della banca dati
          <input required minLength={3} value={titolo} onChange={(e) => setTitolo(e.target.value)} placeholder="es. Banca dati Polizia di Stato 2026 — agenti" className={campo} />
        </label>
        <label className="text-xs font-semibold text-slate-500">
          Comparto{collegati.length > 0 && " (vuoto = quello del primo concorso)"}
          <select required={!collegati.length} value={comparto} onChange={(e) => setComparto(e.target.value as CompartoId | "")} className={campo}>
            <option value="">{collegati.length ? "Come il concorso" : "Scegli…"}</option>
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
        <div className="rounded-xl bg-slate-50 p-3 sm:col-span-2">
          <p className="text-sm font-semibold text-slate-800">Concorsi a cui collegarla (facoltativo)</p>
          <p className="mt-0.5 text-xs text-slate-500">
            Dal titolo e dal comparto ti proponiamo i bandi aperti che le somigliano; puoi anche cercarne altri. I concorsi collegati
            mostrano il link alla banca dati e, da pubblicata, le loro simulazioni usano le domande ufficiali. Puoi cambiarli anche
            dopo, dalla riga della banca dati.
          </p>
          <SceltaConcorsi
            bandi={bandi}
            banca={{ titolo, comparto: comparto || undefined, anno: anno ? Number(anno) : undefined }}
            collegati={collegati}
            onAggiungi={(c) => setCollegati((l) => (l.some((x) => x.id === c.id) ? l : [...l, { id: c.id, titolo: nomeConcorsoBreve(c), comparto: c.comparto }]))}
            onTogli={(id) => setCollegati((l) => l.filter((c) => c.id !== id))}
          />
        </div>
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
        <label className="text-xs font-semibold text-slate-500 sm:col-span-2">
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
          <Button type="submit" loading={!!fase} disabled={!file || (!comparto && !collegati.length)}>
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

/**
 * Concorsi collegati a una banca dati: quelli già scelti (con ×), i suggeriti (bandi aperti
 * simili per titolo, comparto e anno: core/concorsi.ts → concorsiSuggeriti) e la ricerca a mano
 * tra tutti i bandi. Si usa nel modulo di caricamento e nella riga di ogni banca dati.
 */
function SceltaConcorsi({
  bandi,
  banca,
  collegati,
  onAggiungi,
  onTogli,
  inCorso,
}: {
  bandi?: ConcorsoInLista[];
  banca: { titolo: string; comparto?: CompartoId; anno?: number };
  collegati: { id: string; titolo: string }[];
  /** Restituisce una promessa se collega sul server: "Collega i molto simili" le aspetta una per una */
  onAggiungi: (c: ConcorsoInLista) => void | Promise<unknown>;
  onTogli: (id: string) => void;
  /** Id del concorso che si sta collegando o scollegando */
  inCorso?: string;
}) {
  const [cerca, setCerca] = useState("");
  const [soloAperti, setSoloAperti] = useState(true);
  const giaCollegati = useMemo(() => new Set(collegati.map((c) => c.id)), [collegati]);
  const perId = useMemo(() => new Map((bandi ?? []).map((c) => [c.id, c])), [bandi]);
  const suggeriti = useMemo(() => concorsiSuggeriti(banca, bandi ?? [], { esclusi: giaCollegati }), [banca.titolo, banca.comparto, banca.anno, bandi, giaCollegati]);
  const forti = suggeriti.filter((s) => s.forte);
  const trovati = useMemo(() => {
    const q = cerca.trim().toLowerCase();
    if (q.length < 3) return [];
    return (bandi ?? [])
      .filter((c) => !giaCollegati.has(c.id) && (!soloAperti || !scaduto(c)))
      .filter((c) => [c.id, c.ente, c.titolo, c.figura].some((x) => x?.toLowerCase().includes(q)))
      .slice(0, 8);
  }, [bandi, cerca, soloAperti, giaCollegati]);

  const riga = (c: ConcorsoInLista, extra?: ReactNode) => (
    <li key={c.id} className="flex items-center gap-2">
      <button
        type="button"
        disabled={!!inCorso}
        onClick={() => onAggiungi(c)}
        className="grid size-6 shrink-0 place-items-center rounded-md bg-white text-brand-600 ring-1 ring-slate-200 hover:bg-brand-50 disabled:opacity-50"
        title="Collega"
      >
        {inCorso === c.id ? <Loader2 className="size-3.5 animate-spin" /> : <Plus className="size-3.5" />}
      </button>
      <span className="min-w-0 flex-1 truncate">
        {nomeConcorsoBreve(c)} <span className="text-slate-400">· {scaduto(c) ? "domande chiuse" : `scade ${dataBreve(c.scadenza)}`}</span>
        {c.bancaDati && <span className="text-amber-600"> · ha già una banca dati</span>}
      </span>
      {extra}
    </li>
  );

  return (
    <div className="mt-3 space-y-3 text-sm">
      {collegati.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {collegati.map((c) => {
            const bando = perId.get(c.id);
            return (
              <span key={c.id} className="inline-flex max-w-full items-center gap-1.5 rounded-full bg-white py-1 pr-1 pl-3 text-xs font-medium text-slate-700 ring-1 ring-slate-200">
                <Link to={`/app/concorsi/${c.id}`} className="truncate hover:text-brand-700" title={c.titolo}>
                  {c.titolo}
                </Link>
                {bando?.scadenza && <span className="shrink-0 text-slate-400">{scaduto(bando) ? "chiuso" : `scade ${dataBreve(bando.scadenza)}`}</span>}
                <button
                  type="button"
                  disabled={!!inCorso}
                  onClick={() => onTogli(c.id)}
                  className="grid size-5 shrink-0 place-items-center rounded-full text-slate-400 hover:bg-rose-50 hover:text-rose-600"
                  title="Scollega"
                >
                  {inCorso === c.id ? <Loader2 className="size-3 animate-spin" /> : <X className="size-3" />}
                </button>
              </span>
            );
          })}
        </div>
      )}

      {!bandi ? (
        <Spinner label="Carico i bandi…" />
      ) : (
        <>
          {suggeriti.length > 0 && (
            <div>
              <div className="flex flex-wrap items-center justify-between gap-2">
                <p className="text-xs font-semibold text-slate-500">Bandi aperti simili</p>
                {forti.length > 1 && (
                  <Button
                    type="button"
                    variant="ghost"
                    size="sm"
                    disabled={!!inCorso}
                    onClick={async () => {
                      // Uno alla volta: ogni collegamento riscrive la lista dei concorsi della banca dati.
                      for (const s of forti) await onAggiungi(s.concorso);
                    }}
                  >
                    Collega i {forti.length} molto simili
                  </Button>
                )}
              </div>
              <ul className="mt-1 space-y-1">
                {suggeriti.map((s) => riga(s.concorso, s.forte ? <Badge tone="green">molto simile</Badge> : undefined))}
              </ul>
            </div>
          )}
          <div>
            <div className="flex flex-wrap items-center gap-3">
              <input
                value={cerca}
                onChange={(e) => setCerca(e.target.value)}
                placeholder="Cerca un altro concorso: ente, titolo o id inPA…"
                className="h-9 min-w-56 flex-1 rounded-lg border-0 bg-white px-3 text-sm ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500"
              />
              <label className="flex items-center gap-1.5 text-xs text-slate-600">
                <input type="checkbox" checked={soloAperti} onChange={(e) => setSoloAperti(e.target.checked)} className="size-4 rounded border-slate-300" />
                Solo aperti
              </label>
            </div>
            {cerca.trim().length >= 3 && (
              <ul className="mt-2 space-y-1">{trovati.length ? trovati.map((c) => riga(c)) : <li className="text-xs text-slate-500">Nessun bando trovato.</li>}</ul>
            )}
          </div>
        </>
      )}
    </div>
  );
}

/** Una banca dati: stato, numeri dell'estrazione, esempi da controllare e azioni. */
function RigaBanca({ banca, bandi, onCambio }: { banca: BancaDati; bandi?: ConcorsoInLista[]; onCambio: () => void }) {
  const [aperta, setAperta] = useState(banca.stato === "estratta");
  const collegati = concorsiDellaBanca(banca);
  // Concorsi: aperto da controllare prima di pubblicare, o se non ce n'è ancora nessuno.
  const [concorsiAperti, setConcorsiAperti] = useState(banca.stato === "estratta" || !collegati.length);
  const [avviso, setAvviso] = useState<string>();
  const [inCorso, setInCorso] = useState<string>();
  const [errore, setErrore] = useState<string>();
  // Eliminare è definitivo: serve un secondo clic di conferma.
  const [confermaElimina, setConfermaElimina] = useState(false);

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
            {[
              banca.comparto && nomeComparto(banca.comparto),
              banca.anno,
              collegati.length === 1 ? collegati[0]!.titolo : collegati.length ? `${collegati.length} concorsi collegati` : "senza concorsi collegati",
            ]
              .filter(Boolean)
              .join(" · ")}{" "}
            ·{" "}
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
            <Button
              size="sm"
              loading={inCorso === "pubblica"}
              onClick={() =>
                void azione("pubblica", async () => {
                  const r = await api<{ domande: number; occupati: string[] }>(`/admin/banche-dati/${banca.id}/pubblica`, { method: "POST" });
                  // Concorsi che hanno già un'altra banca dati: restano com'erano.
                  setAvviso(r.occupati.length ? `Pubblicata. Non collegati perché hanno già un'altra banca dati: ${r.occupati.join("; ")}.` : undefined);
                })
              }
            >
              Pubblica {banca.domande} domande
            </Button>
          )}
          {banca.stato === "pubblicata" && (
            <Button variant="secondary" size="sm" loading={inCorso === "ritira"} onClick={() => void azione("ritira", () => api(`/admin/banche-dati/${banca.id}/ritira`, { method: "POST" }))}>
              Ritira
            </Button>
          )}
          <Button variant="ghost" size="sm" onClick={() => setConcorsiAperti((a) => !a)}>
            <Link2 className="size-4" /> Concorsi ({collegati.length})
          </Button>
          {!!banca.esempi?.length && (
            <Button variant="ghost" size="sm" onClick={() => setAperta((a) => !a)}>
              {aperta ? "Nascondi esempi" : "Vedi esempi"}
            </Button>
          )}
          {!confermaElimina && (
            <Button variant="ghost" size="sm" disabled={!!inCorso} onClick={() => setConfermaElimina(true)} className="text-rose-600 hover:bg-rose-50">
              <Trash2 className="size-4" /> Elimina
            </Button>
          )}
        </div>
      </div>

      {confermaElimina && (
        <div className="flex flex-wrap items-center gap-3 rounded-xl bg-rose-50 p-3 text-sm text-rose-900 ring-1 ring-rose-200">
          <p className="min-w-0 flex-1">
            Elimino <strong>{banca.titolo}</strong> per sempre, con il PDF e le domande estratte.
            {banca.stato === "pubblicata" && " Sparisce subito dalla sezione Banche dati degli utenti."}
            {banca.stato === "pubblicata" && collegati.length > 0 && " I concorsi collegati tornano alle domande della nostra banca."} Le sessioni già
            fatte restano nelle statistiche.
          </p>
          <Button variant="ghost" size="sm" disabled={inCorso === "elimina"} onClick={() => setConfermaElimina(false)}>
            Annulla
          </Button>
          <Button
            variant="danger"
            size="sm"
            loading={inCorso === "elimina"}
            onClick={() => void azione("elimina", () => api(`/admin/banche-dati/${banca.id}`, { method: "DELETE" }))}
          >
            Elimina definitivamente
          </Button>
        </div>
      )}

      {errore && <Alert tone="error">{errore}</Alert>}
      {avviso && (
        <Alert tone="info" onClose={() => setAvviso(undefined)}>
          {avviso}
        </Alert>
      )}

      {concorsiAperti && (
        <div className="rounded-xl bg-slate-50 p-4">
          <p className="text-sm font-semibold text-slate-800">Concorsi collegati</p>
          <p className="mt-0.5 text-xs text-slate-500">
            {banca.stato === "pubblicata"
              ? "Collegando un concorso, la sua pagina mostra subito il link a questa banca dati e le sue simulazioni usano le domande ufficiali."
              : "Alla pubblicazione, ogni concorso collegato mostrerà il link a questa banca dati e le sue simulazioni useranno le domande ufficiali."}{" "}
            Il segno "Banca dati" nelle liste dei bandi compare dal giorno dopo (la lista in cache si rifà ogni mattina).
          </p>
          <SceltaConcorsi
            bandi={bandi}
            banca={{ titolo: banca.titolo, comparto: banca.comparto, anno: banca.anno }}
            collegati={collegati}
            inCorso={inCorso?.startsWith("concorso:") ? inCorso.slice(9) : undefined}
            onAggiungi={(c) => azione(`concorso:${c.id}`, () => api(`/admin/banche-dati/${banca.id}/concorsi`, { method: "POST", body: { concorsoId: c.id } }))}
            onTogli={(id) => void azione(`concorso:${id}`, () => api(`/admin/banche-dati/${banca.id}/concorsi/${encodeURIComponent(id)}`, { method: "DELETE" }))}
          />
        </div>
      )}

      {aperta && !!banca.esempi?.length && (
        <div className="space-y-3 rounded-xl bg-slate-50 p-4 text-sm">
          <div>
            <p className="font-semibold text-slate-700">
              Controlla che testo, risposte e giusta (in verde) siano come nel PDF
              {!!banca.sezioni?.length && <> · sezioni trovate: {banca.sezioni.join(", ")}</>}
            </p>
            <p className="mt-0.5 text-xs text-slate-500">
              Qui le risposte sono nell'ordine del PDF. Gli utenti scelgono entrando nella banca dati se vedere la giusta sempre per
              prima o mescolata.
            </p>
          </div>
          {banca.esempi.map((d) => (
            <div key={d.numero}>
              <p className="font-medium text-slate-900">
                {d.sezione && <Badge className="mr-1.5 align-middle">{d.sezione}</Badge>}
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
