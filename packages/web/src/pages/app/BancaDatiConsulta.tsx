import { ArrowLeft, ArrowRight, CheckCircle2, Eye, EyeOff, Star } from "lucide-react";
import { type FormEvent, useCallback, useEffect, useRef, useState } from "react";
import { Link, useParams, useSearchParams } from "react-router";
import { ChiediAlTutor } from "../../components/ChiediAlTutor";
import { OrdineRisposte } from "../../components/OrdineRisposte";
import { SegnalaErrore } from "../../components/Richieste";
import { StellaPreferita } from "../../components/StellaPreferita";
import { Alert, Badge, Button, Card, Spinner, UpgradeBanner, cx } from "../../components/ui";
import { api, ApiError } from "../../lib/api";
import { useOrdineRisposte } from "../../lib/ordineRisposte";
import type { UsiApi } from "./BancheDati";

// Consultazione di una banca dati ufficiale, una domanda per volta, con la risposta giusta.
// La stella salva una domanda tra le preferite; "Preferite" fa scorrere solo quelle (?preferite=1).
// Le domande arrivano 20 per volta (avanti con ?da=, indietro con ?fino=).

interface DomandaConsulta {
  numero: number;
  argomento: string;
  testo: string;
  opzioni: string[];
  corretta: number;
  /** Già fatta in una sessione su questa banca dati; sbagliata = l'ultima risposta era sbagliata */
  fatta: boolean;
  sbagliata: boolean;
  /** Salvata con la stella */
  preferita: boolean;
}

interface PaginaConsulta {
  banca: { id: string; titolo: string; domande: number; indiceSezioni: { sezione: string; da: number; domande: number }[]; mescolate: boolean; alternativeRicavate?: boolean };
  domande: DomandaConsulta[];
  altre: boolean;
  usi: UsiApi | null;
  progresso?: { fatte: number; sbagliate: number; preferite: number };
}

const CHIAVE_RISPOSTE = "consulta:mostra-risposte";

function preferenzaRisposte() {
  try {
    return localStorage.getItem(CHIAVE_RISPOSTE) === "1";
  } catch {
    return false;
  }
}

/** Pagina /app/banche-dati/:id. */
export function BancaDatiConsulta() {
  const { id } = useParams();
  // ?preferite=1: si scorrono solo le domande salvate con la stella.
  const [params, setParams] = useSearchParams();
  const soloPreferite = params.get("preferite") === "1";
  const [nPreferite, setNPreferite] = useState(0);
  const [banca, setBanca] = useState<PaginaConsulta["banca"]>();
  const [domande, setDomande] = useState<DomandaConsulta[]>([]);
  // Ci sono altre domande prima della prima caricata / dopo l'ultima?
  const [altrePrima, setAltrePrima] = useState(false);
  const [altreDopo, setAltreDopo] = useState(false);
  const [indice, setIndice] = useState(0);
  const [usi, setUsi] = useState<UsiApi | null>(null);
  const [caricamento, setCaricamento] = useState(true);
  const [errore, setErrore] = useState<ApiError>();
  const [sempre, setSempre] = useState(preferenzaRisposte);
  const [rivelata, setRivelata] = useState(false);
  const [salto, setSalto] = useState("");
  // Ordine delle risposte scelto dall'utente: letto da un ref, così cambiarlo non riporta alla domanda 1.
  const [ordine] = useOrdineRisposte();
  const ordineRef = useRef(ordine);
  ordineRef.current = ordine;

  const carica = useCallback(
    async (query: string) => {
      setCaricamento(true);
      setErrore(undefined);
      try {
        return await api<PaginaConsulta>(`/banche-dati/${id}/domande?${query}&ordine=${ordineRef.current}${soloPreferite ? "&preferite=1" : ""}`);
      } catch (err) {
        setErrore(err instanceof ApiError ? err : new ApiError(0, "Errore di rete"));
        return undefined;
      } finally {
        setCaricamento(false);
      }
    },
    [id, soloPreferite],
  );

  /** Ricomincia dalla domanda `numero` (o dalla prima dopo, se manca). */
  const vaiA = useCallback(
    async (numero: number) => {
      const p = await carica(`da=${numero}`);
      if (!p) return;
      setBanca(p.banca);
      setUsi(p.usi);
      setNPreferite(p.progresso?.preferite ?? 0);
      setDomande(p.domande);
      setAltreDopo(p.altre);
      setAltrePrima((p.domande.at(0)?.numero ?? 1) > 1);
      setIndice(0);
      setRivelata(false);
    },
    [carica],
  );

  useEffect(() => {
    void vaiA(1);
  }, [vaiA]);

  async function avanti() {
    setRivelata(false);
    if (indice < domande.length - 1) return setIndice((i) => i + 1);
    if (!altreDopo) return;
    const p = await carica(`da=${domande.at(-1)!.numero + 1}`);
    if (!p || !p.domande.length) return setAltreDopo(false);
    setDomande((d) => [...d, ...p.domande]);
    setAltreDopo(p.altre);
    setIndice((i) => i + 1);
  }

  async function indietro() {
    setRivelata(false);
    if (indice > 0) return setIndice((i) => i - 1);
    if (!altrePrima) return;
    const p = await carica(`fino=${domande.at(0)!.numero - 1}`);
    if (!p || !p.domande.length) return setAltrePrima(false);
    setDomande((d) => [...p.domande, ...d]);
    setAltrePrima(p.altre);
    setIndice(p.domande.length - 1);
  }

  // Frecce della tastiera per scorrere.
  useEffect(() => {
    const tasto = (e: KeyboardEvent) => {
      // Mentre si scrive (numero da cercare, domanda al tutor) i tasti restano al campo.
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;
      if (e.key === "ArrowRight") void avanti();
      if (e.key === "ArrowLeft") void indietro();
      if (e.key === " ") {
        e.preventDefault();
        setRivelata((r) => !r);
      }
    };
    window.addEventListener("keydown", tasto);
    return () => window.removeEventListener("keydown", tasto);
  });

  function cambiaSempre(valore: boolean) {
    setSempre(valore);
    try {
      localStorage.setItem(CHIAVE_RISPOSTE, valore ? "1" : "0");
    } catch {}
  }

  function onSalto(e: FormEvent) {
    e.preventDefault();
    const n = Number(salto);
    if (n >= 1) void vaiA(n);
    setSalto("");
  }

  /** Stella cambiata sulla domanda che si sta guardando. */
  function cambiaPreferita(numero: number, preferita: boolean, quante: number) {
    setDomande((lista) => lista.map((x) => (x.numero === numero ? { ...x, preferita } : x)));
    setNPreferite(quante);
  }

  const d = domande.at(indice);
  const mostra = sempre || rivelata;
  const sezioneCorrente = banca?.indiceSezioni.filter((s) => d && s.da <= d.numero).at(-1)?.sezione;

  return (
    <div className="mx-auto max-w-3xl space-y-4">
      <Link to="/app/banche-dati" className="inline-flex items-center gap-1 text-sm font-semibold text-slate-500 hover:text-slate-800">
        <ArrowLeft className="size-4" /> Banche dati
      </Link>

      {errore &&
        (errore.code === "LIMITE_PIANO" ? <UpgradeBanner message={errore.message} /> : <Alert tone="error">{errore.message}</Alert>)}

      {banca && (
        <header>
          <h1 className="text-2xl font-extrabold tracking-tight text-slate-900">{banca.titolo}</h1>
          <p className="mt-1 text-sm text-slate-500">
            {banca.domande.toLocaleString("it-IT")} domande ufficiali
            {usi && ` · piano Free: ${usi.restanti} utilizzi rimasti questa settimana`}
          </p>
        </header>
      )}

      {banca && banca.indiceSezioni.length > 1 && (
        <div className="-mx-1 flex gap-2 overflow-x-auto px-1 pb-1" aria-label="Sezioni">
          {banca.indiceSezioni.map((s) => (
            <button
              key={s.sezione}
              onClick={() => void vaiA(s.da)}
              className={cx(
                "shrink-0 rounded-full px-3 py-1.5 text-sm font-semibold transition",
                sezioneCorrente === s.sezione ? "bg-brand-600 text-white" : "bg-white text-slate-600 ring-1 ring-slate-200 hover:ring-slate-300",
              )}
            >
              {s.sezione} <span className="opacity-70">({s.domande})</span>
            </button>
          ))}
        </div>
      )}

      {banca && (
        <div className="space-y-3 rounded-2xl bg-white p-3 ring-1 ring-slate-200 sm:p-4">
          <div className="flex flex-wrap items-center gap-2">
          <form onSubmit={onSalto} className="flex items-center gap-2 text-sm">
            <label htmlFor="salto" className="text-slate-500">
              Vai alla domanda
            </label>
            <input
              id="salto"
              inputMode="numeric"
              value={salto}
              onChange={(e) => setSalto(e.target.value.replace(/\D/g, ""))}
              placeholder="n."
              className="h-9 w-20 rounded-lg border-0 bg-white px-2 ring-1 ring-slate-300 focus:ring-2 focus:ring-brand-500 focus:outline-none"
            />
            <Button type="submit" size="sm" variant="secondary" disabled={!salto}>
              Vai
            </Button>
          </form>
          <button
            onClick={() => setParams(soloPreferite ? {} : { preferite: "1" }, { replace: true })}
            aria-pressed={soloPreferite}
            className={cx(
              "ml-auto inline-flex h-9 items-center gap-1.5 rounded-lg px-3 text-sm font-semibold ring-1 transition",
              soloPreferite ? "bg-amber-50 text-amber-800 ring-amber-300" : "bg-white text-slate-600 ring-slate-200 hover:ring-slate-300",
            )}
          >
            <Star className={cx("size-4", soloPreferite && "fill-amber-400 text-amber-500")} /> Preferite ({nPreferite})
          </button>
          </div>
          <div className="flex flex-wrap items-center justify-between gap-x-4 gap-y-2">
          {/* Si riparte dalla domanda che si sta guardando, con le risposte nel nuovo ordine. */}
          <OrdineRisposte onCambio={() => void vaiA(d?.numero ?? 1)} />
          <label className="flex items-center gap-2 text-sm font-medium text-slate-700">
            <input
              type="checkbox"
              checked={sempre}
              onChange={(e) => cambiaSempre(e.target.checked)}
              className="size-4 rounded border-slate-300 text-brand-600 focus:ring-brand-500"
            />
            Mostra sempre la risposta
          </label>
          </div>
        </div>
      )}

      {caricamento && !d ? (
        <Spinner />
      ) : d ? (
        <Card key={d.numero} className="animate-fade-up p-6 sm:p-8">
          <div className="flex flex-wrap items-center justify-between gap-2">
            <p className="min-w-0 text-xs font-semibold tracking-wide break-words text-slate-400 uppercase">{d.argomento}</p>
            <div className="flex flex-wrap items-center gap-1.5">
              {d.sbagliata ? <Badge tone="red">Sbagliata l'ultima volta</Badge> : d.fatta && <Badge tone="green">Già fatta</Badge>}
              <Badge tone="brand">n. {d.numero}</Badge>
              <StellaPreferita bancaId={banca!.id} numero={d.numero} preferita={d.preferita} onCambio={(p, n) => cambiaPreferita(d.numero, p, n)} />
            </div>
          </div>
          <h2 className="mt-2 text-lg font-bold break-words text-slate-900 sm:text-xl">{d.testo}</h2>
          <ol className="mt-6 grid gap-3">
            {d.opzioni.map((o, i) => {
              const giusta = mostra && i === d.corretta;
              return (
                <li
                  key={i}
                  className={cx(
                    "flex items-center gap-3 rounded-xl p-4 font-medium ring-1",
                    giusta ? "bg-emerald-50 text-emerald-900 ring-2 ring-emerald-500" : "ring-slate-200",
                    mostra && !giusta && "opacity-60",
                  )}
                >
                  <span className="grid size-7 shrink-0 place-items-center rounded-lg bg-slate-100 text-sm font-bold text-slate-600">
                    {String.fromCharCode(65 + i)}
                  </span>
                  <span className="flex-1">{o}</span>
                  {giusta && <CheckCircle2 className="size-5 text-emerald-600" />}
                </li>
              );
            })}
          </ol>
          {mostra && (
            <div key={d.numero} className="mt-6 animate-fade-up rounded-xl bg-slate-50 p-4 text-sm">
              <p className="font-semibold text-slate-900">Risposta giusta: {String.fromCharCode(65 + d.corretta)}</p>
              <p className="mt-1 text-slate-600">
                Indicata nella banca dati ufficiale del concorso. Il perché te lo spiega il tutor.
                {banca?.alternativeRicavate &&
                  " La banca dati ufficiale riporta solo la risposta esatta: le altre alternative le prendiamo da domande simili della stessa banca dati."}
              </p>
              <ChiediAlTutor domanda={{ argomento: d.argomento, testo: d.testo, opzioni: d.opzioni, corretta: d.corretta }} />
              <SegnalaErrore
                className="mt-3 flex"
                contesto={{ bancaDatiId: banca!.id, domanda: { materia: d.argomento.slice(0, 100), id: `n. ${d.numero}`, testo: d.testo.slice(0, 1500) } }}
              />
            </div>
          )}
          {!sempre && (
            <Button variant="secondary" className="mt-6" onClick={() => setRivelata((r) => !r)}>
              {rivelata ? <EyeOff className="size-4" /> : <Eye className="size-4" />}
              {rivelata ? "Nascondi la risposta" : "Mostra la risposta"}
            </Button>
          )}
        </Card>
      ) : (
        !errore &&
        (soloPreferite ? (
          <Alert tone="info">
            Non hai domande preferite {nPreferite ? "da questo numero in poi" : "in questa banca dati"}: tocca la stella su una domanda per
            salvarla.{" "}
            <button onClick={() => setParams({}, { replace: true })} className="font-semibold underline">
              Torna a tutte le domande
            </button>
          </Alert>
        ) : (
          <Alert tone="info">Nessuna domanda da questo numero in poi.</Alert>
        ))
      )}

      {d && (
        <div className="flex items-center justify-between">
          <Button variant="secondary" disabled={(indice === 0 && !altrePrima) || caricamento} onClick={() => void indietro()}>
            <ArrowLeft className="size-4" /> Precedente
          </Button>
          <p className="hidden text-xs text-slate-400 sm:block">Frecce per scorrere, spazio per la risposta</p>
          <Button disabled={(indice === domande.length - 1 && !altreDopo) || caricamento} onClick={() => void avanti()}>
            Successiva <ArrowRight className="size-4" />
          </Button>
        </div>
      )}
    </div>
  );
}
