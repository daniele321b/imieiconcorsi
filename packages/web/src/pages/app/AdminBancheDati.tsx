import { concorsiSuggeriti, conMaiuscola, nomeConcorso, scadenzaVera, scaduto, type ConcorsoInLista } from "@imieiconcorsi/core/concorsi";
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
import { ArrowLeft, Bell, Database, FileUp, Link2, Loader2, Pencil, Plus, RefreshCw, Trash2, X } from "lucide-react";
import { type FormEvent, type ReactNode, useEffect, useMemo, useState } from "react";
import { Link, Navigate } from "react-router";
import { Alert, Badge, Button, Card, PageHeader, Spinner, cx } from "../../components/ui";
import { api, ApiError, useApi } from "../../lib/api";
import { caricaBandi, segnaBandiVisti } from "../../lib/bandi";
import { useUtente } from "../../lib/auth";
import { dataBreve } from "../../lib/format";

// Pannello admin → Banche dati (/admin/banche-dati): carica il PDF di una banca dati ufficiale,
// collegala ai concorsi (suggeriti tra i bandi aperti simili o cercati a mano, anche dopo),
// segui l'estrazione, controlla gli esempi, poi pubblica, ritira o elimina. Il PDF va
// direttamente su S3 con un link firmato dal backend.

type Formato = BancaDati["formato"];

const FORMATI: { id: Formato; nome: string; spiegazione: string }[] = [
  { id: "auto", nome: "Automatico", spiegazione: "Prova tutti i modi qui sotto e usa quello che trova." },
  { id: "indicata", nome: "Indicata", spiegazione: "Sotto ogni domanda: «Risposta esatta: B»." },
  { id: "segnata", nome: "Segnata", spiegazione: "La giusta ha un segno: * oppure (X)." },
  { id: "chiave", nome: "Tabella soluzioni", spiegazione: "In fondo: «Soluzioni» e poi 1 B, 2 A…" },
  { id: "prima", nome: "Sempre la prima", spiegazione: "Il bando dice che la giusta è sempre la A." },
  {
    id: "risposta",
    nome: "Solo risposta esatta",
    spiegazione: "Tabella numero | domanda | risposta (es. Carabinieri): le altre alternative si ricavano da domande simili.",
  },
  {
    id: "colonne",
    nome: "Tabella esatta ed errate",
    spiegazione: "Tabella Id | Livello | Quesito | Risp_esatta | Risp_errata 1-3 (es. Polizia penitenziaria).",
  },
  {
    id: "lettera",
    nome: "Tabella con lettera giusta",
    spiegazione: "Tabella codice | domanda | a) | b) | c) | d) | lettera della giusta, senza intestazione (es. Guardia di Finanza).",
  },
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

/** Testo dell'errore da mostrare. */
const messaggio = (err: unknown) => (err instanceof ApiError ? err.message : err instanceof Error ? err.message : "Errore di rete");

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
  // Bando scelto da "Bandi da caricare": il modulo di caricamento parte già collegato a lui.
  const [preselezionato, setPreselezionato] = useState<ConcorsoInLista>();
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
      <DaCaricare
        bandi={bandi}
        onCarica={(c) => {
          setPreselezionato(c);
          document.getElementById("carica-banca")?.scrollIntoView({ behavior: "smooth" });
        }}
      />
      <Caricamento bandi={bandi} preselezionato={preselezionato} onCaricata={() => void reload()} />

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
function Caricamento({
  bandi,
  preselezionato,
  onCaricata,
}: {
  bandi?: ConcorsoInLista[];
  /** Bando scelto da "Bandi da caricare": si aggiunge ai collegati e propone il titolo */
  preselezionato?: ConcorsoInLista;
  onCaricata: () => void;
}) {
  const [comparto, setComparto] = useState<CompartoId | "">("");
  const [anno, setAnno] = useState(String(new Date().getFullYear()));
  const [collegati, setCollegati] = useState<{ id: string; titolo: string; ente?: string; comparto: CompartoId }[]>([]);
  const [titolo, setTitolo] = useState("");
  const [materia, setMateria] = useState<MateriaId | "">("");
  const [formato, setFormato] = useState<Formato>("auto");
  const [file, setFile] = useState<File>();
  const [fase, setFase] = useState<string>();
  const [esito, setEsito] = useState<{ tone: "success" | "error"; testo: string }>();

  useEffect(() => {
    if (!preselezionato) return;
    setCollegati((l) =>
      l.some((c) => c.id === preselezionato.id)
        ? l
        : [...l, { id: preselezionato.id, titolo: nomeConcorso(preselezionato), ente: conMaiuscola(preselezionato.ente), comparto: preselezionato.comparto }],
    );
    setTitolo((t) => t || `Banca dati ${nomeConcorso(preselezionato)}`);
    setComparto((c) => c || preselezionato.comparto);
  }, [preselezionato]);

  // Crea la banca dati, carica il PDF su S3 con il link firmato e la collega ai concorsi scelti.
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
    <Card className="scroll-mt-24 space-y-4">
      <div id="carica-banca" className="flex items-center gap-2">
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
            onAggiungi={(c) =>
              setCollegati((l) => (l.some((x) => x.id === c.id) ? l : [...l, { id: c.id, titolo: nomeConcorso(c), ente: conMaiuscola(c.ente), comparto: c.comparto }]))
            }
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

/** Giorni in cui un bando da caricare è "nuovo". */
const GIORNI_NUOVO = 7;

/**
 * Bandi aperti che citano una banca dati ufficiale non ancora caricata: i nuovi (ultima
 * settimana) in cima. "Carica la banca dati" precompila il modulo qui sotto. Ogni mattina lo
 * scraper manda anche un'email per i nuovi.
 */
function DaCaricare({ bandi, onCarica }: { bandi?: ConcorsoInLista[]; onCarica: (c: ConcorsoInLista) => void }) {
  const [tutti, setTutti] = useState(false);
  const lista = useMemo(
    () =>
      (bandi ?? [])
        .filter((c) => c.bancaDatiPrevista && !c.bancaDati && !scaduto(c))
        .sort((a, b) => (b.pubblicatoIl ?? "").localeCompare(a.pubblicatoIl ?? "")),
    [bandi],
  );
  // Bando pubblicato da meno di GIORNI_NUOVO giorni.
  const nuovo = (c: ConcorsoInLista) => !!c.pubblicatoIl && Date.now() - Date.parse(c.pubblicatoIl) < GIORNI_NUOVO * 86_400_000;
  // Elenco aperto: questi bandi sono visti e il pallino rosso su "Admin" si spegne.
  useEffect(() => {
    if (lista.length) segnaBandiVisti(lista.map((c) => c.id));
  }, [lista]);
  const nuovi = lista.filter(nuovo).length;
  const mostrati = tutti ? lista : lista.slice(0, 5);
  if (!bandi) return null;

  return (
    <section id="da-caricare" className="scroll-mt-24">
      <Card className="space-y-3">
        <div className="flex flex-wrap items-center gap-2">
          <Bell className="size-5 text-amber-500" />
          <h2 className="text-lg font-bold text-slate-900">Bandi da caricare</h2>
          <Badge tone={nuovi ? "amber" : "slate"}>{nuovi ? `${nuovi} ${nuovi === 1 ? "nuovo" : "nuovi"} questa settimana` : `${lista.length} in attesa`}</Badge>
        </div>
        <p className="text-sm text-slate-500">
          Bandi aperti che citano una banca dati ufficiale non ancora caricata. Quando l'ente la pubblica, carica il PDF: il bando resta
          qui finché non lo colleghi a una banca dati pubblicata.
        </p>
        {!lista.length ? (
          <p className="text-sm text-slate-500">Nessun bando in attesa.</p>
        ) : (
          <ul className="divide-y divide-slate-100">
            {mostrati.map((c) => (
              <li key={c.id} className="flex flex-col gap-2 py-3 sm:flex-row sm:items-center">
                <div className="min-w-0 flex-1">
                  <Link to={`/app/concorsi/${c.id}`} className="font-semibold break-words text-slate-900 hover:text-brand-700">
                    {nomeConcorso(c)}
                  </Link>
                  {nuovo(c) && <Badge tone="amber" className="ml-2 align-middle">nuovo</Badge>}
                  <p className="text-xs break-words text-slate-500">
                    {conMaiuscola(c.ente)} · pubblicato il {dataBreve(c.pubblicatoIl)} · {scadenzaVera(c.scadenza) ? `scade il ${dataBreve(c.scadenza)}` : "senza scadenza"}
                  </p>
                </div>
                <Button size="sm" variant="secondary" className="self-start sm:self-auto" onClick={() => onCarica(c)}>
                  <FileUp className="size-4" /> Carica la banca dati
                </Button>
              </li>
            ))}
          </ul>
        )}
        {lista.length > 5 && (
          <button onClick={() => setTutti((t) => !t)} className="text-sm font-semibold text-brand-600 hover:text-brand-700">
            {tutti ? "Mostra meno" : `Mostra tutti (${lista.length})`}
          </button>
        )}
      </Card>
    </section>
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
  collegati: { id: string; titolo: string; ente?: string }[];
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

  /** Scadenza a parole, per le righe. */
  const quando = (c: Pick<ConcorsoInLista, "scadenza">) => (scaduto(c) ? "domande chiuse" : scadenzaVera(c.scadenza) ? `scade il ${dataBreve(c.scadenza)}` : "senza scadenza");

  /** Un bando da collegare: nome grande, ente e scadenza sotto, pulsante + a destra. */
  const riga = (c: ConcorsoInLista, extra?: ReactNode) => (
    <li key={c.id} className="flex items-start gap-3 rounded-xl bg-white p-3 ring-1 ring-slate-200">
      <div className="min-w-0 flex-1">
        <p className="font-semibold break-words text-slate-900">
          {nomeConcorso(c)} {extra}
        </p>
        <p className="mt-0.5 text-xs break-words text-slate-500">
          {conMaiuscola(c.ente)} · {quando(c)}
          {c.bancaDati && <span className="text-amber-600"> · ha già una banca dati</span>}
        </p>
      </div>
      <button
        type="button"
        disabled={!!inCorso}
        onClick={() => onAggiungi(c)}
        className="grid size-9 shrink-0 place-items-center rounded-lg bg-brand-600 text-white shadow-sm hover:bg-brand-700 disabled:opacity-50"
        title="Collega"
        aria-label={`Collega ${nomeConcorso(c)}`}
      >
        {inCorso === c.id ? <Loader2 className="size-4 animate-spin" /> : <Plus className="size-4" />}
      </button>
    </li>
  );

  return (
    <div className="mt-3 space-y-4 text-sm">
      {collegati.length > 0 && (
        <ul className="space-y-2">
          {collegati.map((c) => {
            // Dati aggiornati dalla lista dei bandi, se il bando c'è ancora; altrimenti quelli salvati.
            const bando = perId.get(c.id);
            return (
              <li key={c.id} className="flex items-start gap-3 rounded-xl bg-emerald-50 p-3 ring-1 ring-emerald-200">
                <div className="min-w-0 flex-1">
                  <Link to={`/app/concorsi/${c.id}`} className="font-semibold break-words text-slate-900 hover:text-brand-700">
                    {bando ? nomeConcorso(bando) : c.titolo}
                  </Link>
                  <p className="mt-0.5 text-xs break-words text-slate-500">
                    {[bando ? conMaiuscola(bando.ente) : c.ente, bando && quando(bando)].filter(Boolean).join(" · ") || "collegato"}
                  </p>
                </div>
                <button
                  type="button"
                  disabled={!!inCorso}
                  onClick={() => onTogli(c.id)}
                  className="grid size-9 shrink-0 place-items-center rounded-lg text-slate-500 ring-1 ring-slate-200 hover:bg-rose-50 hover:text-rose-600 disabled:opacity-50"
                  title="Scollega"
                  aria-label="Scollega"
                >
                  {inCorso === c.id ? <Loader2 className="size-4 animate-spin" /> : <X className="size-4" />}
                </button>
              </li>
            );
          })}
        </ul>
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
              <ul className="mt-2 space-y-2">
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
                className="h-10 w-full rounded-lg border-0 bg-white px-3 text-sm ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500 sm:w-auto sm:flex-1"
              />
              <label className="flex items-center gap-1.5 text-xs text-slate-600">
                <input type="checkbox" checked={soloAperti} onChange={(e) => setSoloAperti(e.target.checked)} className="size-4 rounded border-slate-300" />
                Solo aperti
              </label>
            </div>
            {cerca.trim().length >= 3 && (
              <ul className="mt-2 space-y-2">{trovati.length ? trovati.map((c) => riga(c)) : <li className="text-xs text-slate-500">Nessun bando trovato.</li>}</ul>
            )}
          </div>
        </>
      )}
    </div>
  );
}

/**
 * Modifica dei dati inseriti al caricamento: titolo, comparto, anno, materia, formato e, se la
 * banca non è pubblicata, il PDF. Si mandano solo i campi cambiati (PUT /admin/banche-dati/{id});
 * il PDF nuovo passa da POST …/pdf e l'estrazione riparte da sola.
 */
function ModificaBanca({ banca, onFatto, onAnnulla }: { banca: BancaDati; onFatto: (avviso: string) => void; onAnnulla: () => void }) {
  const [titolo, setTitolo] = useState(banca.titolo);
  const [comparto, setComparto] = useState<CompartoId | "">(banca.comparto ?? "");
  const [anno, setAnno] = useState(banca.anno ? String(banca.anno) : "");
  const [materia, setMateria] = useState<MateriaId | "">(banca.materia ?? "");
  const [formato, setFormato] = useState<Formato>(banca.formato);
  const [file, setFile] = useState<File>();
  const [fase, setFase] = useState<string>();
  const [errore, setErrore] = useState<string>();
  const pubblicata = banca.stato === "pubblicata";
  const lavorazione = banca.stato === "caricamento" || banca.stato === "estrazione";

  // Solo i campi cambiati.
  const modifiche: Record<string, unknown> = {};
  if (titolo.trim() !== banca.titolo) modifiche.titolo = titolo.trim();
  if (comparto && comparto !== banca.comparto) modifiche.comparto = comparto;
  if (anno !== (banca.anno ? String(banca.anno) : "")) modifiche.anno = anno ? Number(anno) : null;
  if (materia !== (banca.materia ?? "")) modifiche.materia = materia || null;
  if (formato !== banca.formato) modifiche.formato = formato;
  const cambiato = Object.keys(modifiche).length > 0 || !!file;

  // Salva le modifiche ai dati e, se c'è, carica il nuovo PDF.
  async function salva(e: FormEvent) {
    e.preventDefault();
    setErrore(undefined);
    try {
      const avvisi: string[] = [];
      if (Object.keys(modifiche).length) {
        setFase(pubblicata && (modifiche.titolo || modifiche.materia !== undefined) ? "Salvo e aggiorno le domande pubblicate…" : "Salvo…");
        await api(`/admin/banche-dati/${banca.id}`, { method: "PUT", body: modifiche });
        avvisi.push(modifiche.formato ? "Dati salvati: con il formato nuovo l'estrazione è ripartita." : "Dati salvati.");
      }
      if (file) {
        setFase("Preparo il caricamento…");
        const { upload } = await api<{ upload: string }>(`/admin/banche-dati/${banca.id}/pdf`, {
          method: "POST",
          body: { nomeFile: file.name, dimensione: file.size },
        });
        setFase(`Carico il PDF (${(file.size / 1024 / 1024).toFixed(1)} MB)…`);
        const res = await fetch(upload, { method: "PUT", headers: { "content-type": "application/pdf" }, body: file });
        if (!res.ok) throw new Error(`Caricamento non riuscito (${res.status})`);
        avvisi.push("PDF sostituito: l'estrazione è partita, ti arriva un'email quando finisce.");
      }
      onFatto(avvisi.join(" "));
    } catch (err) {
      setErrore(messaggio(err));
    } finally {
      setFase(undefined);
    }
  }

  return (
    <form onSubmit={(e) => void salva(e)} className="grid gap-3 rounded-xl bg-slate-50 p-4 sm:grid-cols-2">
      <p className="text-sm font-semibold text-slate-800 sm:col-span-2">Modifica la banca dati</p>
      <label className="text-xs font-semibold text-slate-500 sm:col-span-2">
        Titolo
        <input required minLength={3} maxLength={200} value={titolo} onChange={(e) => setTitolo(e.target.value)} className={campo} />
      </label>
      <label className="text-xs font-semibold text-slate-500">
        Comparto
        <select value={comparto} onChange={(e) => setComparto(e.target.value as CompartoId)} className={campo}>
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
        <select value={formato} disabled={lavorazione} onChange={(e) => setFormato(e.target.value as Formato)} className={campo}>
          {FORMATI.map((f) => (
            <option key={f.id} value={f.id}>
              {f.nome}
            </option>
          ))}
        </select>
        {formato !== banca.formato && (
          <span className="mt-1 block font-normal text-amber-700">
            L'estrazione riparte{pubblicata && ": la banca esce dalla sezione Banche dati finché non la ripubblichi"}.
          </span>
        )}
      </label>
      <label className="text-xs font-semibold text-slate-500 sm:col-span-2">
        Sostituisci il PDF (ora: {banca.nomeFile})
        <input
          type="file"
          accept="application/pdf"
          disabled={pubblicata || lavorazione}
          onChange={(e) => setFile(e.target.files?.[0])}
          className="mt-1 block w-full text-sm text-slate-700 file:mr-3 file:rounded-lg file:border-0 file:bg-brand-50 file:px-3 file:py-2 file:font-semibold file:text-brand-700 disabled:opacity-50"
        />
        <span className="mt-1 block font-normal text-slate-400">
          {pubblicata
            ? "Per sostituire il PDF di una banca pubblicata, prima premi Ritira: con un file nuovo le domande cambiano numero."
            : lavorazione
              ? "Aspetta che finisca l'estrazione in corso."
              : "L'estrazione riparte dal file nuovo; le domande estratte prima si cancellano."}
        </span>
      </label>
      {pubblicata && (modifiche.titolo !== undefined || modifiche.materia !== undefined) && (
        <p className="text-xs text-slate-500 sm:col-span-2">Titolo e materia sono scritti anche sulle domande: salvando, la banca si ripubblica da sola.</p>
      )}
      {errore && (
        <div className="sm:col-span-2">
          <Alert tone="error">{errore}</Alert>
        </div>
      )}
      <div className="flex flex-wrap items-center gap-2 sm:col-span-2">
        <Button type="button" variant="secondary" size="sm" disabled={!!fase} onClick={onAnnulla}>
          Annulla
        </Button>
        <Button type="submit" size="sm" disabled={!cambiato || !titolo.trim()} loading={!!fase}>
          Salva
        </Button>
        {fase && <span className="text-sm text-slate-500">{fase}</span>}
      </div>
    </form>
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
  const [modifica, setModifica] = useState(false);

  // Esegue un'azione sulla banca dati (pubblica, ritira, elimina…) con il pulsante `nome` in attesa.
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
          <Button variant="ghost" size="sm" onClick={() => setModifica((m) => !m)}>
            <Pencil className="size-4" /> Modifica
          </Button>
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

      {modifica && (
        <ModificaBanca
          banca={banca}
          onAnnulla={() => setModifica(false)}
          onFatto={(testo) => {
            setModifica(false);
            setAvviso(testo);
            onCambio();
          }}
        />
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
            {!!banca.alternativeRicavate && (
              <p className="mt-1 text-xs text-amber-800">
                Il PDF riporta solo la risposta esatta: per {banca.alternativeRicavate} domande le altre alternative (in grigio, "ricavata")
                sono risposte di domande simili dello stesso file, scelte in modo che siano sbagliate. Le domande al negativo ("Non ha
                nulla a che fare con…") e quelle senza le parole tra cui scegliere sono tra le scartate.
              </p>
            )}
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
                    {d.alternativeRicavate && i !== d.corretta && <span className="ml-1.5 text-xs text-slate-400">ricavata</span>}
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
