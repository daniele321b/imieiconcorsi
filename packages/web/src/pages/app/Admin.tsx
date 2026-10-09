import { PIANI, type CodiceSconto, type PianoId } from "@imieiconcorsi/core/domain";
import { Copy, Crown, Database, Search, ShieldCheck, Sparkles, Tag, Users } from "lucide-react";
import { type FormEvent, useEffect, useState } from "react";
import { Navigate } from "react-router";
import { Alert, Badge, Button, ButtonLink, Card, PageHeader, Spinner, cx } from "../../components/ui";
import { copiaTesto } from "../../lib/appunti";
import { api, ApiError, useApi, type AdminCodici, type AdminRiepilogo, type AdminUtente, type AdminUtenti } from "../../lib/api";
import { useUtente } from "../../lib/auth";
import { dataBreve } from "../../lib/format";

const toDate = (iso?: string) => (iso ? iso.slice(0, 10) : "");

export function Admin() {
  const { utente } = useUtente();
  if (!utente.admin) return <Navigate to="/app" replace />;
  return <Pannello />;
}

function Pannello() {
  const riepilogo = useApi<AdminRiepilogo>("/admin/riepilogo");
  const [cerca, setCerca] = useState("");
  const [filtro, setFiltro] = useState("");
  const [utenti, setUtenti] = useState<AdminUtente[]>([]);
  const [pagina, setPagina] = useState<string>();
  const [caricamento, setCaricamento] = useState(true);
  const [errore, setErrore] = useState<string>();

  // Ricerca per inizio dell'email, con una piccola attesa mentre si scrive.
  useEffect(() => {
    const t = setTimeout(() => setFiltro(cerca.trim()), 350);
    return () => clearTimeout(t);
  }, [cerca]);

  async function carica(token?: string) {
    setCaricamento(true);
    setErrore(undefined);
    try {
      const qs = new URLSearchParams();
      if (filtro) qs.set("cerca", filtro);
      if (token) qs.set("pagina", token);
      const res = await api<AdminUtenti>(`/admin/utenti?${qs}`);
      setUtenti((prima) => (token ? [...prima, ...res.utenti] : res.utenti));
      setPagina(res.pagina);
    } catch (err) {
      setErrore(err instanceof ApiError ? err.message : "Errore di rete");
    } finally {
      setCaricamento(false);
    }
  }

  // Si ricarica dalla prima pagina a ogni nuova ricerca.
  useEffect(() => {
    void carica();
  }, [filtro]);

  const aggiorna = (u: AdminUtente) => {
    setUtenti((lista) => lista.map((x) => (x.username === u.username ? u : x)));
    void riepilogo.reload();
  };

  return (
    <div className="space-y-6">
      <PageHeader
        title="Pannello di controllo"
        subtitle="Utenti registrati, piani e accesso. Le modifiche valgono dal prossimo accesso dell'utente."
        actions={
          <ButtonLink to="/admin/banche-dati" variant="secondary">
            <Database className="size-4" /> Banche dati
          </ButtonLink>
        }
      />

      <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
        {[
          { label: "Utenti", valore: riepilogo.data?.utenti, Icon: Users, cls: "text-brand-600" },
          { label: "Medium", valore: riepilogo.data?.medium, Icon: Crown, cls: "text-amber-500" },
          { label: "Pro", valore: riepilogo.data?.pro, Icon: Sparkles, cls: "text-fuchsia-500" },
          { label: "Admin", valore: riepilogo.data?.admin, Icon: ShieldCheck, cls: "text-slate-600" },
        ].map(({ label, valore, Icon, cls }) => (
          <Card key={label}>
            <Icon className={cx("size-5", cls)} />
            <p className="mt-2 text-2xl font-extrabold">{valore ?? "…"}</p>
            <p className="text-sm text-slate-500">{label}</p>
          </Card>
        ))}
      </div>

      <CodiciSconto />

      <h2 className="pt-2 text-lg font-bold text-slate-900">Utenti</h2>
      <label className="relative block max-w-md">
        <Search className="pointer-events-none absolute top-1/2 left-3.5 size-4 -translate-y-1/2 text-slate-400" />
        <input
          value={cerca}
          onChange={(e) => setCerca(e.target.value)}
          placeholder="Cerca per email (inizio dell'indirizzo)…"
          className="h-11 w-full rounded-xl border-0 bg-white pr-4 pl-10 shadow-sm ring-1 ring-slate-200 focus:ring-2 focus:ring-brand-500 focus:outline-none"
        />
      </label>

      {errore && <Alert tone="error">{errore}</Alert>}

      <div className="space-y-3">
        {utenti.map((u) => (
          <RigaUtente key={u.username} utente={u} onAggiornato={aggiorna} />
        ))}
        {caricamento ? (
          <Spinner label="Carico gli utenti…" />
        ) : (
          !utenti.length && <p className="py-10 text-center text-sm text-slate-500">Nessun utente trovato.</p>
        )}
        {pagina && !caricamento && (
          <div className="flex justify-center">
            <Button variant="secondary" onClick={() => void carica(pagina)}>
              Carica altri
            </Button>
          </div>
        )}
      </div>
    </div>
  );
}

function RigaUtente({ utente, onAggiornato }: { utente: AdminUtente; onAggiornato: (u: AdminUtente) => void }) {
  const [piano, setPiano] = useState<PianoId>(utente.piano);
  const [scadenza, setScadenza] = useState(toDate(utente.scadenzaPiano));
  const [salvataggio, setSalvataggio] = useState(false);
  const [esito, setEsito] = useState<{ tone: "success" | "error"; testo: string }>();

  const modificato = piano !== utente.piano || scadenza !== toDate(utente.scadenzaPiano);

  async function salvaPiano() {
    setSalvataggio(true);
    setEsito(undefined);
    try {
      await api(`/admin/utenti/${encodeURIComponent(utente.username)}/piano`, {
        method: "PUT",
        body: { piano, scadenza: piano === "free" || !scadenza ? null : scadenza },
      });
      onAggiornato({ ...utente, piano, scadenzaPiano: piano === "free" || !scadenza ? undefined : `${scadenza}T23:59:59.000Z` });
      setEsito({ tone: "success", testo: "Salvato" });
    } catch (err) {
      setEsito({ tone: "error", testo: err instanceof ApiError ? err.message : "Errore di rete" });
    } finally {
      setSalvataggio(false);
    }
  }

  async function cambiaStato() {
    setSalvataggio(true);
    setEsito(undefined);
    try {
      await api(`/admin/utenti/${encodeURIComponent(utente.username)}/stato`, {
        method: "PUT",
        body: { abilitato: !utente.abilitato },
      });
      onAggiornato({ ...utente, abilitato: !utente.abilitato });
    } catch (err) {
      setEsito({ tone: "error", testo: err instanceof ApiError ? err.message : "Errore di rete" });
    } finally {
      setSalvataggio(false);
    }
  }

  return (
    <Card className={cx("flex flex-col gap-4 lg:flex-row lg:items-center", !utente.abilitato && "opacity-60")}>
      <div className="min-w-0 flex-1">
        <div className="flex flex-wrap items-center gap-2">
          <p className="truncate font-semibold text-slate-900">{utente.email ?? utente.username}</p>
          {utente.admin && <Badge tone="amber">admin</Badge>}
          {!utente.abilitato && <Badge tone="red">disattivato</Badge>}
          {utente.stato === "UNCONFIRMED" && <Badge>email non confermata</Badge>}
        </div>
        <p className="mt-0.5 text-sm text-slate-500">
          {utente.nome ? `${utente.nome} · ` : ""}accesso con {utente.accesso} · iscritto il {dataBreve(utente.creatoIl)}
          {!utente.onboarded && " · onboarding da fare"}
        </p>
        {utente.feedback && (
          <p className="mt-1 text-sm text-slate-600">
            <span className="text-accent-500">{"★".repeat(utente.feedback.voto)}</span>
            <span className="text-slate-300">{"★".repeat(5 - utente.feedback.voto)}</span>
            {utente.feedback.testo && <span className="ml-1.5 italic">“{utente.feedback.testo}”</span>}
          </p>
        )}
      </div>

      <div className="flex flex-wrap items-end gap-3">
        {utente.admin ? (
          <p className="text-sm text-slate-500">Admin: tutte le funzioni, nessun piano</p>
        ) : (
          <>
            <label className="text-xs font-semibold text-slate-500">
              Piano
              <select
                value={piano}
                onChange={(e) => setPiano(e.target.value as PianoId)}
                className="mt-1 block h-10 rounded-xl border-0 bg-white px-3 text-sm font-medium text-slate-900 ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500"
              >
                {Object.values(PIANI).map((p) => (
                  <option key={p.id} value={p.id}>
                    {p.nome}
                  </option>
                ))}
              </select>
            </label>
            <label className="text-xs font-semibold text-slate-500">
              Scadenza
              <input
                type="date"
                value={scadenza}
                disabled={piano === "free"}
                onChange={(e) => setScadenza(e.target.value)}
                title="Vuota = senza scadenza"
                className="mt-1 block h-10 rounded-xl border-0 bg-white px-3 text-sm text-slate-900 ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500 disabled:bg-slate-50 disabled:text-slate-400"
              />
            </label>
            <Button disabled={!modificato} loading={salvataggio} onClick={() => void salvaPiano()}>
              Salva
            </Button>
          </>
        )}
        <Button variant={utente.abilitato ? "ghost" : "secondary"} disabled={salvataggio} onClick={() => void cambiaStato()}>
          {utente.abilitato ? "Disattiva" : "Riattiva"}
        </Button>
      </div>

      {esito && (
        <p className={cx("text-sm font-medium lg:w-20", esito.tone === "success" ? "text-emerald-600" : "text-rose-600")}>{esito.testo}</p>
      )}
    </Card>
  );
}

// ── Codici sconto ────────────────────────────────────────────────────────────

const campo =
  "mt-1 block h-10 w-full rounded-xl border-0 bg-white px-3 text-sm text-slate-900 ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500";

function CodiciSconto() {
  const { data, loading, error, setData } = useApi<AdminCodici>("/admin/codici");
  const [codice, setCodice] = useState("");
  const [percentuale, setPercentuale] = useState("20");
  const [piano, setPiano] = useState<"" | "medium" | "pro">("");
  const [validoFino, setValidoFino] = useState("");
  const [usiMassimi, setUsiMassimi] = useState("");
  const [nota, setNota] = useState("");
  const [inCorso, setInCorso] = useState(false);
  const [esito, setEsito] = useState<{ tone: "success" | "error"; testo: string }>();
  const [copiato, setCopiato] = useState<string>();

  async function copia(codice: string) {
    if (await copiaTesto(codice)) {
      setCopiato(codice);
      setTimeout(() => setCopiato((c) => (c === codice ? undefined : c)), 2000);
    } else {
      setEsito({ tone: "error", testo: `Copia non riuscita: tieni premuto sul codice ${codice} per selezionarlo.` });
    }
  }

  async function crea(e: FormEvent) {
    e.preventDefault();
    setInCorso(true);
    setEsito(undefined);
    try {
      const nuovo = await api<CodiceSconto>("/admin/codici", {
        method: "POST",
        body: {
          codice: codice.trim() || undefined,
          percentuale: Number(percentuale),
          piani: piano ? [piano] : undefined,
          validoFino: validoFino || null,
          usiMassimi: usiMassimi ? Number(usiMassimi) : null,
          nota: nota.trim() || undefined,
        },
      });
      setData((d) => ({ codici: [nuovo, ...(d?.codici ?? [])] }));
      setEsito({ tone: "success", testo: `Creato il codice ${nuovo.codice}` });
      setCodice("");
      setNota("");
    } catch (err) {
      setEsito({ tone: "error", testo: err instanceof ApiError ? err.message : "Errore di rete" });
    } finally {
      setInCorso(false);
    }
  }

  async function cambiaStato(c: CodiceSconto) {
    try {
      await api(`/admin/codici/${encodeURIComponent(c.codice)}`, { method: "PUT", body: { attivo: !c.attivo } });
      setData((d) => d && { codici: d.codici.map((x) => (x.codice === c.codice ? { ...x, attivo: !c.attivo } : x)) });
    } catch (err) {
      setEsito({ tone: "error", testo: err instanceof ApiError ? err.message : "Errore di rete" });
    }
  }

  return (
    <Card className="space-y-5">
      <div className="flex items-center gap-2">
        <Tag className="size-5 text-brand-600" />
        <h2 className="text-lg font-bold text-slate-900">Codici sconto</h2>
      </div>
      <p className="text-sm text-slate-500">
        Lo sconto vale sul prezzo del piano scelto, una volta per utente. L'utente lo inserisce nella pagina Piani.
      </p>

      <form onSubmit={(e) => void crea(e)} className="grid gap-3 sm:grid-cols-2 lg:grid-cols-6 lg:items-end">
        <label className="text-xs font-semibold text-slate-500 lg:col-span-2">
          Codice (vuoto = generato)
          <input value={codice} onChange={(e) => setCodice(e.target.value.toUpperCase())} placeholder="es. BENVENUTO20" className={cx(campo, "font-mono")} />
        </label>
        <label className="text-xs font-semibold text-slate-500">
          Sconto %
          <input type="number" min={1} max={100} required value={percentuale} onChange={(e) => setPercentuale(e.target.value)} className={campo} />
        </label>
        <label className="text-xs font-semibold text-slate-500">
          Piano
          <select value={piano} onChange={(e) => setPiano(e.target.value as "" | "medium" | "pro")} className={campo}>
            <option value="">Medium e Pro</option>
            <option value="medium">Solo Medium</option>
            <option value="pro">Solo Pro</option>
          </select>
        </label>
        <label className="text-xs font-semibold text-slate-500">
          Valido fino al
          <input type="date" value={validoFino} onChange={(e) => setValidoFino(e.target.value)} title="Vuota = senza scadenza" className={campo} />
        </label>
        <label className="text-xs font-semibold text-slate-500">
          Usi massimi
          <input type="number" min={1} value={usiMassimi} onChange={(e) => setUsiMassimi(e.target.value)} placeholder="illimitati" className={campo} />
        </label>
        <label className="text-xs font-semibold text-slate-500 sm:col-span-2 lg:col-span-5">
          Nota (solo per te)
          <input value={nota} maxLength={200} onChange={(e) => setNota(e.target.value)} placeholder="es. campagna Instagram ottobre" className={campo} />
        </label>
        <Button type="submit" loading={inCorso}>
          Genera codice
        </Button>
      </form>

      {esito && (
        <Alert tone={esito.tone} onClose={() => setEsito(undefined)}>
          {esito.testo}
        </Alert>
      )}
      {error && <Alert tone="error">{error.message}</Alert>}

      {loading ? (
        <Spinner label="Carico i codici…" />
      ) : data?.codici.length ? (
        <div className="divide-y divide-slate-100">
          {data.codici.map((c) => (
            <div key={c.codice} className={cx("flex flex-wrap items-center gap-3 py-3", !c.attivo && "opacity-60")}>
              <button
                type="button"
                onClick={() => void copia(c.codice)}
                title="Copia"
                className="inline-flex select-all items-center gap-1.5 rounded-lg bg-slate-100 px-2.5 py-1 font-mono text-sm font-bold text-slate-800 hover:bg-slate-200"
              >
                {c.codice}
                {copiato === c.codice ? (
                  <span className="font-sans text-xs font-semibold text-emerald-600">Copiato</span>
                ) : (
                  <Copy className="size-3.5 text-slate-400" />
                )}
              </button>
              <Badge tone="green">−{c.percentuale}%</Badge>
              <span className="text-sm text-slate-500">
                {c.piani?.length ? `solo ${PIANI[c.piani[0]].nome}` : "Medium e Pro"} · usato {c.usi}
                {c.usiMassimi ? `/${c.usiMassimi}` : ""} {c.usi === 1 ? "volta" : "volte"}
                {c.validoFino ? ` · fino al ${dataBreve(c.validoFino)}` : ""}
                {c.nota ? ` · ${c.nota}` : ""}
              </span>
              {!c.attivo && <Badge tone="red">disattivato</Badge>}
              <Button variant="ghost" size="sm" className="ml-auto" onClick={() => void cambiaStato(c)}>
                {c.attivo ? "Disattiva" : "Riattiva"}
              </Button>
            </div>
          ))}
        </div>
      ) : (
        <p className="text-sm text-slate-500">Nessun codice ancora.</p>
      )}
    </Card>
  );
}
