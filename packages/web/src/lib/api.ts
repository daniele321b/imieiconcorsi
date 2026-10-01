import type {
  Concorso,
  Domanda,
  DomandaPubblica,
  MATERIE,
  MateriaId,
  Periodo,
  Piano,
  PianoId,
  Sessione,
  TipoSessione,
  Utente,
} from "@imieiconcorsi/core/domain";
import { fetchAuthSession } from "aws-amplify/auth";
import { useCallback, useEffect, useState } from "react";
import { config } from "./config";

export class ApiError extends Error {
  constructor(
    public status: number,
    message: string,
    public code?: string,
  ) {
    super(message);
  }
}

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

export type UtenteApi = Utente;
export type ConcorsoApi = Concorso & { seguito: boolean };

export interface MateriaApi {
  id: MateriaId;
  nome: string;
  icona: (typeof MATERIE)[number]["icona"];
  domande: number;
  livello?: number;
}

export type SessioneApi = Omit<Sessione, "userId" | "domande"> & {
  domande: (Domanda | DomandaPubblica)[];
};

export interface NuovaSessione {
  tipo: TipoSessione;
  materie?: MateriaId[];
  concorsoId?: string;
  numero?: number;
}

export interface Statistiche {
  domandeRisposte: number;
  perMateria: { materia: MateriaId; corrette: number; totale: number; percentuale: number }[];
  simulazioni: { id: string; data: string; percentuale: number; superata: boolean }[];
  recenti: { id: string; tipo: TipoSessione; materie: MateriaId[]; concorsoId?: string; data: string; percentuale: number }[];
}

export interface PianiApi {
  piani: Piano[];
  attuale: PianoId;
  periodo?: Periodo;
  scadenza?: string;
  modalita: string;
}

// ── Pannello admin ───────────────────────────────────────────────────────────

export interface AdminRiepilogo {
  utenti: number;
  medium: number;
  pro: number;
  admin: number;
}

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
}

export interface AdminUtenti {
  utenti: AdminUtente[];
  pagina?: string;
}

export const haSoluzione = (d: Domanda | DomandaPubblica): d is Domanda => "corretta" in d;
