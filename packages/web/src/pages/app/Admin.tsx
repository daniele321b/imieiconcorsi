import { PIANI, type PianoId } from "@imieiconcorsi/core/domain";
import { Crown, Search, ShieldCheck, Sparkles, Users } from "lucide-react";
import { useEffect, useState } from "react";
import { Navigate } from "react-router";
import { Alert, Badge, Button, Card, PageHeader, Spinner, cx } from "../../components/ui";
import { api, ApiError, useApi, type AdminRiepilogo, type AdminUtente, type AdminUtenti } from "../../lib/api";
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
      <PageHeader title="Pannello di controllo" subtitle="Utenti registrati, piani e accesso. Le modifiche valgono dal prossimo accesso dell'utente." />

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
      </div>

      <div className="flex flex-wrap items-end gap-3">
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
