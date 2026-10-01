// Modello di dominio condiviso tra frontend e microservizi. Niente dipendenze AWS qui:
// questo file finisce anche nel bundle del browser.

export const COMPARTI = [
  { id: "enti-locali", nome: "Enti locali", descrizione: "Comuni, province, regioni, unioni di comuni", contenuti: true },
  { id: "forze-ordine", nome: "Forze dell'ordine", descrizione: "Polizia, Carabinieri, Guardia di Finanza, Forze armate", contenuti: true },
  { id: "inps", nome: "INPS e previdenza", descrizione: "INPS, INAIL e enti previdenziali", contenuti: false },
  { id: "ministeri", nome: "Ministeri e agenzie", descrizione: "Ministeri, agenzie fiscali, autorità", contenuti: false },
  { id: "sanita", nome: "Sanità", descrizione: "ASL, aziende ospedaliere, ruoli amministrativi", contenuti: false },
  { id: "universita", nome: "Università e ricerca", descrizione: "Atenei ed enti di ricerca", contenuti: false },
  { id: "altro", nome: "Altri enti", descrizione: "Tutti gli altri bandi pubblicati su inPA", contenuti: false },
] as const;
export type CompartoId = (typeof COMPARTI)[number]["id"];
export const COMPARTO_IDS = COMPARTI.map((c) => c.id) as [CompartoId, ...CompartoId[]];

export const MATERIE = [
  { id: "diritto-amministrativo", nome: "Diritto amministrativo", icona: "scale" },
  { id: "diritto-costituzionale", nome: "Diritto costituzionale", icona: "landmark" },
  { id: "italiano", nome: "Italiano", icona: "book-open" },
  { id: "storia", nome: "Storia", icona: "hourglass" },
  { id: "logica", nome: "Logica", icona: "puzzle" },
  { id: "informatica", nome: "Informatica", icona: "monitor" },
] as const;
export type MateriaId = (typeof MATERIE)[number]["id"];
export const MATERIA_IDS = MATERIE.map((m) => m.id) as [MateriaId, ...MateriaId[]];

export const nomeMateria = (id: string) => MATERIE.find((m) => m.id === id)?.nome ?? id;
export const nomeComparto = (id: string) => COMPARTI.find((c) => c.id === id)?.nome ?? id;

export type FrequenzaAvvisi = "giornaliero" | "settimanale" | "mai";

// ── Piani ────────────────────────────────────────────────────────────────────

export type PianoId = "free" | "medium" | "pro";
export type Periodo = "mensile" | "annuale";

export interface Limiti {
  /** null = illimitato */
  concorsiSeguiti: number | null;
  simulazioniSettimana: number | null;
  domandePerSessioneStudio: number;
  /** Banche dati ufficiali dei concorsi (Medium e Pro); il Free usa solo la banca dei nostri libri. */
  bancheDati: boolean;
  /** Tutor e domande generate (solo Pro). */
  ai: boolean;
}

export interface Piano {
  id: PianoId;
  nome: string;
  slogan: string;
  /** Prezzi provvisori: si decidono sui dati della beta. */
  prezzo: { mensile: number; annuale: number };
  funzioni: string[];
  limiti: Limiti;
}

export const PIANI: Record<PianoId, Piano> = {
  free: {
    id: "free",
    nome: "Free",
    slogan: "Per iniziare",
    prezzo: { mensile: 0, annuale: 0 },
    funzioni: [
      "Avvisi sui nuovi bandi",
      "1 concorso seguito",
      "Domande dalla nostra banca, generata da libri selezionati",
      "Sessioni di studio da 10 domande",
      "1 simulazione a settimana",
    ],
    limiti: { concorsiSeguiti: 1, simulazioniSettimana: 1, domandePerSessioneStudio: 10, bancheDati: false, ai: false },
  },
  medium: {
    id: "medium",
    nome: "Medium",
    slogan: "Tutto per superare il concorso",
    prezzo: { mensile: 9.99, annuale: 79.99 },
    funzioni: [
      "Banche dati ufficiali dei tuoi concorsi, appena escono",
      "Concorsi seguiti illimitati",
      "Simulazioni illimitate da 50/60 domande",
      "Sessioni di studio complete",
      "Statistiche per materia",
    ],
    limiti: { concorsiSeguiti: null, simulazioniSettimana: null, domandePerSessioneStudio: 30, bancheDati: true, ai: false },
  },
  pro: {
    id: "pro",
    nome: "Pro",
    slogan: "Con il tutor AI",
    prezzo: { mensile: 19.99, annuale: 159.99 },
    funzioni: [
      "Tutto il piano Medium, banche dati comprese",
      "Tutor AI interattivo che spiega argomenti ed errori",
      "Domande generate sui tuoi punti deboli",
      "Piano di studio adattivo",
    ],
    limiti: { concorsiSeguiti: null, simulazioniSettimana: null, domandePerSessioneStudio: 30, bancheDati: true, ai: true },
  },
};

// ── Gruppi Cognito: piano e ruolo stanno qui, non nel database ──────────────

/** Nomi dei gruppi Cognito (creati da Terraform, modules/auth). */
export const GRUPPI = { medium: "medium", pro: "pro", admin: "admin" } as const;

/** Piano dai gruppi del token: pro > medium > free. L'admin ha tutto. */
export function pianoDaGruppi(gruppi: readonly string[]): PianoId {
  if (gruppi.includes(GRUPPI.pro) || gruppi.includes(GRUPPI.admin)) return "pro";
  if (gruppi.includes(GRUPPI.medium)) return "medium";
  return "free";
}

// ── Entità ───────────────────────────────────────────────────────────────────

/**
 * Profilo nel database (tabella users). Solo dati di studio, identificati da un id
 * anonimo: email e nome stanno solo in Cognito.
 */
export interface Profilo {
  /** sub di Cognito */
  userId: string;
  /** cognito:username, serve per le operazioni admin su Cognito (es. google_123…) */
  username: string;
  onboarded: boolean;
  interessi: CompartoId[];
  /** Autovalutazione 1–5 per materia */
  livelli: Partial<Record<MateriaId, number>>;
  avvisi: FrequenzaAvvisi;
  /** Fine del periodo pagato (ISO). Assente = piano free, o assegnato dall'admin senza scadenza. */
  scadenzaPiano?: string;
  periodo?: Periodo;
  /** Scadenza per cui è già partita l'email di promemoria (evita doppioni). */
  promemoriaInviatoPer?: string;
  createdAt: string;
  updatedAt: string;
}

/** Quello che l'app riceve da GET /me: profilo + dati dal token Cognito. */
export interface Utente extends Profilo {
  email?: string;
  nome?: string;
  piano: PianoId;
  admin: boolean;
  limiti: Limiti;
}

export interface Concorso {
  id: string;
  titolo: string;
  ente: string;
  sedi: string[];
  comparto: CompartoId;
  /** ISO 8601 */
  scadenza?: string;
  pubblicatoIl?: string;
  tipoProcedura?: string;
  posti?: number;
  figura?: string;
  descrizione?: string;
  url: string;
  materie: MateriaId[];
  /** true finché le materie sono dedotte in automatico e non lette dal bando */
  materieStimate: boolean;
  /** Il testo del bando cita una banca dati: quando esce va scaricata (avviso all'admin). */
  bancaDatiPrevista: boolean;
  /** La banca dati ufficiale è stata pubblicata e importata. */
  bancaDati: boolean;
  fonte: "inpa";
  aggiornatoIl: string;
}

export interface Domanda {
  materia: MateriaId;
  id: string;
  argomento: string;
  livello: number;
  testo: string;
  opzioni: string[];
  corretta: number;
  spiegazione: string;
  fonte: string;
}

/** Domanda come la vede l'utente durante una simulazione (senza soluzione). */
export type DomandaPubblica = Omit<Domanda, "corretta" | "spiegazione" | "fonte">;

export type TipoSessione = "studio" | "simulazione";

export interface Regole {
  corretta: number;
  errata: number;
  omessa: number;
  /** Percentuale minima del punteggio massimo per superare la prova */
  soglia: number;
}

export const REGOLE_DEFAULT: Regole = { corretta: 1, errata: -0.25, omessa: 0, soglia: 0.7 };

export interface Esito {
  corrette: number;
  errate: number;
  omesse: number;
  punteggio: number;
  massimo: number;
  percentuale: number;
  superata: boolean;
  perMateria: { materia: MateriaId; corrette: number; totale: number }[];
}

export interface Sessione {
  userId: string;
  id: string;
  tipo: TipoSessione;
  concorsoId?: string;
  materie: MateriaId[];
  domande: { materia: MateriaId; id: string }[];
  stato: "in-corso" | "consegnata";
  regole: Regole;
  creataIl: string;
  /** Solo simulazioni: termine per la consegna */
  scadeIl?: string;
  consegnataIl?: string;
  risposte?: (number | null)[];
  esito?: Esito;
}
