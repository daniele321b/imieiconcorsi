import { conMaiuscola } from "@imieiconcorsi/core/concorsi";
import { COMPARTI, MATERIE, type Concorso, type ModificheConcorso } from "@imieiconcorsi/core/domain";
import { Pencil, RotateCcw, ShieldCheck } from "lucide-react";
import { useState } from "react";
import { api, ApiError, type ConcorsoApi } from "../lib/api";
import { dataOra } from "../lib/format";
import { Button, cx } from "./ui";

// Admin: correzione di un bando importato da inPA (nome, ente, scadenza, posti, sedi, comparto,
// materie, testo, banca dati prevista). Si mandano solo i campi cambiati; il server li salva
// anche a parte, così l'import del mattino li riapplica sopra i dati di inPA.

/** Nomi dei campi, per il riepilogo "hai corretto: …". */
const NOMI: Record<string, string> = {
  figura: "nome",
  titolo: "descrizione breve",
  ente: "ente",
  scadenza: "scadenza",
  posti: "posti",
  sedi: "sedi",
  comparto: "comparto",
  materie: "materie",
  materieStimate: "",
  descrizione: "testo del bando",
  bancaDatiPrevista: "banca dati prevista",
};

const campo =
  "mt-1 block w-full rounded-xl border-0 bg-white px-3 py-2 text-sm text-slate-900 ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500 focus:outline-none";

/** ISO → valore di un <input type="datetime-local"> (ora del browser). */
function perInput(iso?: string) {
  if (!iso) return "";
  const d = new Date(iso);
  // Numero a due cifre, es. 7 → "07".
  const due = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${due(d.getMonth() + 1)}-${due(d.getDate())}T${due(d.getHours())}:${due(d.getMinutes())}`;
}

/** Valori del modulo a partire dal bando. */
const iniziali = (c: Concorso) => ({
  figura: conMaiuscola(c.figura || c.titolo),
  titolo: c.titolo,
  ente: c.ente,
  scadenza: perInput(c.scadenza),
  posti: c.posti ? String(c.posti) : "",
  sedi: c.sedi.join(", "),
  comparto: c.comparto,
  materie: c.materie,
  descrizione: c.descrizione ?? "",
  bancaDatiPrevista: c.bancaDatiPrevista,
});

/** Modulo admin per correggere i dati di un bando (o tornare a quelli di inPA). */
export function ModificaBando({ concorso, onSalvato }: { concorso: ConcorsoApi; onSalvato: (c: Concorso) => void }) {
  const [aperto, setAperto] = useState(false);
  const [v, setV] = useState(() => iniziali(concorso));
  const [inCorso, setInCorso] = useState<"salva" | "ripristina">();
  const [errore, setErrore] = useState<string>();
  // Cambia solo i campi indicati del modulo.
  const set = (parziale: Partial<typeof v>) => setV((x) => ({ ...x, ...parziale }));

  /** Solo i campi diversi da come sono ora. */
  function modifiche(): ModificheConcorso {
    const prima = iniziali(concorso);
    const m: ModificheConcorso = {};
    if (v.figura.trim() !== prima.figura) m.figura = v.figura.trim();
    if (v.titolo.trim() !== prima.titolo) m.titolo = v.titolo.trim();
    if (v.ente.trim() !== prima.ente) m.ente = v.ente.trim();
    if (v.scadenza && v.scadenza !== prima.scadenza) m.scadenza = new Date(v.scadenza).toISOString();
    if (v.posti !== prima.posti && v.posti !== "") m.posti = Number(v.posti);
    const sedi = v.sedi.split(",").map((s) => s.trim()).filter(Boolean);
    if (sedi.join(", ") !== prima.sedi) m.sedi = sedi;
    if (v.comparto !== prima.comparto) m.comparto = v.comparto;
    if ([...v.materie].sort().join() !== [...prima.materie].sort().join()) m.materie = v.materie;
    if (v.descrizione.trim() !== prima.descrizione.trim()) m.descrizione = v.descrizione.trim();
    if (v.bancaDatiPrevista !== prima.bancaDatiPrevista) m.bancaDatiPrevista = v.bancaDatiPrevista;
    return m;
  }
  const cambiate = modifiche();

  // Salva le modifiche oppure le cancella (il bando torna come da inPA).
  async function esegui(tipo: "salva" | "ripristina") {
    setInCorso(tipo);
    setErrore(undefined);
    try {
      const url = `/admin/concorsi/${encodeURIComponent(concorso.id)}`;
      const c =
        tipo === "salva" ? await api<Concorso>(url, { method: "PUT", body: cambiate }) : await api<Concorso>(`${url}/modifiche`, { method: "DELETE" });
      onSalvato(c);
      setV(iniziali(c));
      setAperto(false);
    } catch (err) {
      setErrore(err instanceof ApiError ? err.message : "Errore di rete");
    } finally {
      setInCorso(undefined);
    }
  }

  const corretti = Object.keys(concorso.modificheAdmin ?? {})
    .map((k) => NOMI[k])
    .filter(Boolean);

  return (
    <div className="mt-6 space-y-3 rounded-2xl bg-amber-50/60 p-4 text-sm ring-1 ring-amber-200">
      <p className="flex items-center gap-2 font-semibold text-amber-900">
        <ShieldCheck className="size-4" /> Solo per te (admin): dati del bando
      </p>
      {corretti.length > 0 && (
        <p className="text-amber-900/80">
          Hai corretto: {corretti.join(", ")}
          {concorso.modificatoIl && ` (ultima volta il ${dataOra(concorso.modificatoIl)})`}. Le correzioni restano anche quando il
          bando si aggiorna da inPA.
        </p>
      )}

      {!aperto ? (
        <div className="flex flex-wrap gap-2">
          <Button variant="secondary" size="sm" onClick={() => setAperto(true)}>
            <Pencil className="size-4" /> Modifica nome e dati
          </Button>
          {corretti.length > 0 && (
            <Button variant="ghost" size="sm" loading={inCorso === "ripristina"} onClick={() => void esegui("ripristina")}>
              <RotateCcw className="size-4" /> Torna ai dati di inPA
            </Button>
          )}
        </div>
      ) : (
        <div className="space-y-3">
          <label className="block">
            <span className="font-medium text-slate-700">Nome del concorso</span>
            <input className={campo} value={v.figura} maxLength={200} onChange={(e) => set({ figura: e.target.value })} />
            <span className="mt-0.5 block text-xs text-slate-500">È il titolo grande della pagina e delle liste; l'anno si aggiunge da solo se manca.</span>
          </label>
          <label className="block">
            <span className="font-medium text-slate-700">Descrizione breve</span>
            <textarea className={campo} rows={2} value={v.titolo} maxLength={1000} onChange={(e) => set({ titolo: e.target.value })} />
          </label>
          <label className="block">
            <span className="font-medium text-slate-700">Ente</span>
            <input className={campo} value={v.ente} maxLength={300} onChange={(e) => set({ ente: e.target.value })} />
          </label>
          <div className="grid gap-3 sm:grid-cols-2">
            <label className="block">
              <span className="font-medium text-slate-700">Scadenza delle domande</span>
              <input type="datetime-local" className={campo} value={v.scadenza} onChange={(e) => set({ scadenza: e.target.value })} />
            </label>
            <label className="block">
              <span className="font-medium text-slate-700">Posti</span>
              <input type="number" min={0} inputMode="numeric" className={campo} value={v.posti} onChange={(e) => set({ posti: e.target.value })} />
            </label>
          </div>
          <div className="grid gap-3 sm:grid-cols-2">
            <label className="block">
              <span className="font-medium text-slate-700">Sedi (separate da virgola)</span>
              <input className={campo} value={v.sedi} onChange={(e) => set({ sedi: e.target.value })} />
            </label>
            <label className="block">
              <span className="font-medium text-slate-700">Comparto</span>
              <select className={campo} value={v.comparto} onChange={(e) => set({ comparto: e.target.value as Concorso["comparto"] })}>
                {COMPARTI.map((c) => (
                  <option key={c.id} value={c.id}>
                    {c.nome}
                  </option>
                ))}
              </select>
            </label>
          </div>
          <fieldset>
            <legend className="font-medium text-slate-700">Materie d'esame</legend>
            <div className="mt-1 flex flex-wrap gap-1.5">
              {MATERIE.map((m) => {
                const scelta = v.materie.includes(m.id);
                return (
                  <button
                    key={m.id}
                    type="button"
                    aria-pressed={scelta}
                    onClick={() => set({ materie: scelta ? v.materie.filter((x) => x !== m.id) : [...v.materie, m.id] })}
                    className={cx(
                      "rounded-full px-2.5 py-1 text-xs font-semibold transition",
                      scelta ? "bg-brand-600 text-white" : "bg-white text-slate-600 ring-1 ring-slate-200 hover:ring-slate-300",
                    )}
                  >
                    {m.nome}
                  </button>
                );
              })}
            </div>
          </fieldset>
          <label className="block">
            <span className="font-medium text-slate-700">Testo del bando ("Dal bando")</span>
            <textarea className={campo} rows={5} value={v.descrizione} maxLength={10_000} onChange={(e) => set({ descrizione: e.target.value })} />
          </label>
          <label className="flex items-center gap-2">
            <input
              type="checkbox"
              checked={v.bancaDatiPrevista}
              onChange={(e) => set({ bancaDatiPrevista: e.target.checked })}
              className="size-4 rounded border-slate-300 text-brand-600 focus:ring-brand-500"
            />
            <span className="text-slate-700">Il bando prevede una banca dati di domande</span>
          </label>

          <p className="text-xs text-slate-500">
            Qui e nella pagina del bando le modifiche si vedono subito; nelle liste e nella ricerca dal mattino dopo (la lista dei
            bandi si rifà ogni mattina).
          </p>
          {errore && <p className="text-rose-600">{errore}</p>}
          <div className="flex flex-wrap gap-2">
            <Button
              variant="secondary"
              size="sm"
              disabled={!!inCorso}
              onClick={() => {
                setV(iniziali(concorso));
                setAperto(false);
                setErrore(undefined);
              }}
            >
              Annulla
            </Button>
            <Button size="sm" disabled={!Object.keys(cambiate).length || !v.materie.length} loading={inCorso === "salva"} onClick={() => void esegui("salva")}>
              Salva {Object.keys(cambiate).length ? `(${Object.keys(cambiate).length})` : ""}
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}
