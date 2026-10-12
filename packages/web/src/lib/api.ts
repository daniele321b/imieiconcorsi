import type {
  CodiceSconto,
  Concorso,
  Domanda,
  DomandaPubblica,
  Feedback,
  MATERIE,
  MateriaId,
  Periodo,
  Piano,
  PianoId,
  Richiesta,
  SelezioneBanca,
  Sessione,
  TipoSessione,
  Utente,
} from "@imieiconcorsi/core/domain";
import { fetchAuthSession } from "aws-amplify/auth";
import { useCallback, useEffect, useState } from "react";
import { config } from "./config";

// Chiamate all'API del backend (API Gateway → Lambda) con il token di Cognito, più i tipi delle
// risposte. Ogni pagina usa api() per le azioni e useApi() per i dati da mostrare.

/** Errore restituito dall'API: stato HTTP, messaggio in italiano e codice (es. LIMITE_PIANO). */
export class ApiError extends Error {
  constructor(
    public status: number,
    message: string,
    public code?: string,
  ) {
    super(message);
  }
}

/** Chiamata all'API con il token dell'utente; errore ApiError se la risposta non è 2xx. */
export async function api<T>(path: string, init: { method?: string; body?: unknown } = {}): Promise<T> {
  const session = await fetchAuthSession();
  const token = session.tokens?.idToken?.toString();
  if (!token) throw new ApiError(401, "Sessione scaduta, accedi di nuovo");

  const res = await fetch(config.apiUrl + path, {
    method: init.method ?? "GET",
    headers: {
      authorization: `Bearer ${token}`,
      ...(init.body !== undefined ? { "content-type": "application/json" } : {}),
    },
    body: init.body !== undefined ? JSON.stringify(init.body) : undefined,
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new ApiError(res.status, data.error ?? "Errore di comunicazione con il server", data.code);
  return data as T;
}

/**
 * Errori dell'AI che sono avvisi e non guasti (gettoni o limite del mese finiti, troppe
 * richieste di fila, AI in pausa, domanda fuori tema): si mostrano in blu, non in rosso.
 */
const AVVISI_AI = new Set(["GETTONI_FINITI", "TROPPO_VELOCE", "AI_IN_PAUSA", "FUORI_TEMA"]);
export const toneErroreAi = (err: ApiError) => (err.code && AVVISI_AI.has(err.code) ? ("info" as const) : ("error" as const));

/** GET con stato di caricamento; `path = null` sospende la richiesta. */
export function useApi<T>(path: string | null) {
  const [data, setData] = useState<T>();
  const [error, setError] = useState<ApiError>();
  const [loading, setLoading] = useState(path !== null);

  const reload = useCallback(async () => {
    if (path === null) return;
    setLoading(true);
    setError(undefined);
    try {
      setData(await api<T>(path));
    } catch (err) {
      setError(err instanceof ApiError ? err : new ApiError(0, "Errore di rete"));
    } finally {
      setLoading(false);
    }
  }, [path]);

  useEffect(() => {
    void reload();
  }, [reload]);

  return { data, error, loading, reload, setData };
}

// ── Tipi delle risposte ──────────────────────────────────────────────────────

/** L'utente collegato, come lo restituisce GET /me: profilo + email, nome, piano, limiti. */
export type UtenteApi = Utente;
/** Richiesta di assistenza vista dall'utente (senza le chiavi interne) */
export type RichiestaApi = Omit<Richiesta, "userId" | "username">;
/** Richiesta di assistenza nel pannello admin: con l'email di chi l'ha scritta */
export type RichiestaAdmin = Omit<Richiesta, "username"> & { email?: string };
/** Da dove nasce una richiesta: si passa alla pagina Assistenza con lo stato del link */
export type ContestoRichiesta = NonNullable<Richiesta["contesto"]>;
/**
 * Un bando con l'indicazione se l'utente lo segue; nel dettaglio, se ha una banca dati
 * ufficiale pubblicata, anche il suo titolo e il numero di domande.
 */
export type ConcorsoApi = Concorso & { seguito: boolean; bancaDatiTitolo?: string; bancaDatiDomande?: number };

/** Una materia della banca statica con il numero di domande e il livello dell'utente. */
export interface MateriaApi {
  id: MateriaId;
  nome: string;
  icona: (typeof MATERIE)[number]["icona"];
  domande: number;
  livello?: number;
}

/** Una sessione con le domande complete (con soluzione in studio e dopo la consegna). */
export type SessioneApi = Omit<Sessione, "userId" | "domande"> & {
  /** Domande delle banche dati: `preferita` = salvata con la stella */
  domande: ((Domanda | DomandaPubblica) & { preferita?: boolean })[];
};

/** Cosa si manda a POST /sessioni per avviare studio o simulazione. */
export interface NuovaSessione {
  tipo: TipoSessione;
  materie?: MateriaId[];
  concorsoId?: string;
  bancaDatiId?: string;
  numero?: number;
  ordineRisposte?: "prima" | "mescolate";
  /** Banca dati: prima le mai fatte (predefinito), solo le sbagliate, o tutte */
  selezione?: SelezioneBanca;
}

/** Statistiche della dashboard (GET /me/statistiche). */
export interface Statistiche {
  domandeRisposte: number;
  perMateria: { materia: MateriaId; corrette: number; totale: number; percentuale: number }[];
  /** Risposte giuste nelle banche dati ufficiali (assente nelle risposte di prima) */
  perBancaDati?: { bancaId: string; titolo: string; corrette: number; totale: number; percentuale: number }[];
  simulazioni: { id: string; data: string; percentuale: number; superata: boolean }[];
  recenti: { id: string; tipo: TipoSessione; materie: MateriaId[]; concorsoId?: string; data: string; percentuale: number; durataMs?: number; bancaDati?: string }[];
}

/** Codice sconto valido, dopo il controllo nella pagina Piani. */
export interface CodiceScontoApi {
  codice: string;
  percentuale: number;
  /** Piani su cui vale */
  piani: ("medium" | "pro")[];
}

/** Stato di un ordine, per la pagina di ritorno dal pagamento. */
export interface OrdineApi {
  id: string;
  stato: "in-attesa" | "pagato" | "scaduto" | "fallito";
  piano: "medium" | "pro";
  periodo: Periodo;
  importo: number;
  scadenzaPiano?: string;
}

/** Un ordine nello storico dei pagamenti dell'utente (GET /me/ordini). */
export interface PagamentoApi extends OrdineApi {
  prezzo: number;
  codiceSconto?: string;
  percentualeSconto?: number;
  creatoIl: string;
  pagatoIl?: string;
}

/** Pagina Piani: piani in vendita, piano attuale con scadenza, modalità di pagamento (stripe o mock). */
export interface PianiApi {
  piani: Piano[];
  attuale: PianoId;
  periodo?: Periodo;
  scadenza?: string;
  modalita: string;
}

// ── Pannello admin ───────────────────────────────────────────────────────────

/** Numeri del pannello admin (GET /admin/riepilogo). */
export interface AdminRiepilogo {
  utenti: number;
  medium: number;
  pro: number;
  admin: number;
  /** Richieste di assistenza in attesa di una prima risposta */
  richiesteAperte: number;
  /** Spesa AI stimata del mese di tutta la piattaforma e tetto oltre il quale l'AI va in pausa */
  ai: { spesaUsd: number; tettoUsd: number; chiamate: number };
}

/** Un utente nell'elenco del pannello admin. */
export interface AdminUtente {
  username: string;
  email?: string;
  nome?: string;
  /** "email", "google", "facebook" */
  accesso: string;
  stato?: string;
  abilitato: boolean;
  creatoIl?: string;
  piano: PianoId;
  admin: boolean;
  scadenzaPiano?: string;
  periodo?: Periodo;
  onboarded: boolean;
  feedback?: Feedback;
  /** Ultimo login e quanti in tutto (registrati da Cognito) */
  ultimoAccessoIl?: string;
  accessi?: number;
}

/** Codici sconto nel pannello admin. */
export interface AdminCodici {
  codici: CodiceSconto[];
}

/** Una pagina di utenti; `pagina` è il segnaposto per caricare la successiva. */
export interface AdminUtenti {
  utenti: AdminUtente[];
  pagina?: string;
}

/** true se la domanda arriva con la soluzione (studio, o simulazione già consegnata). */
export const haSoluzione = (d: Domanda | DomandaPubblica): d is Domanda => "corretta" in d;

// ── Tutor AI (piano Pro) ─────────────────────────────────────────────────────

/** Gettoni AI del mese. */
export interface GettoniAi {
  totale: number;
  usati: number;
  restanti: number;
  /** Primo giorno del mese prossimo (ISO) */
  rinnovoIl: string;
}

/** Pagina Tutor: AI attiva, gettoni, materie deboli e costo di ogni azione. */
export interface AiStato {
  attivo: boolean;
  gettoni: GettoniAi;
  /** Materie dalla percentuale più bassa */
  puntiDeboli: { materia: MateriaId; percentuale: number; risposte: number }[];
  costi: { tutor: number; allenamento: number };
}

/** Domanda su cui si chiede al tutor: la soluzione serve al modello per spiegarla. */
export interface DomandaTutor {
  materia?: string;
  argomento?: string;
  testo: string;
  opzioni: string[];
  corretta: number;
  risposta?: number | null;
  spiegazione?: string;
}

/** Un messaggio della chat con il tutor. */
export interface MessaggioTutor {
  ruolo: "studente" | "tutor";
  testo: string;
}

/** Una domanda generata per l'allenamento (non salvata: si fa nella pagina e basta). */
export interface DomandaAllenamento {
  id: string;
  materia: MateriaId;
  argomento: string;
  testo: string;
  opzioni: string[];
  corretta: number;
  spiegazione: string;
}
