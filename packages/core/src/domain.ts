// Modello di dominio condiviso tra frontend e microservizi. Niente dipendenze AWS qui:
// questo file finisce anche nel bundle del browser.

export const COMPARTI = [
  { id: "enti-locali", nome: "Enti locali", descrizione: "Comuni, province, regioni, unioni di comuni" },
  { id: "forze-ordine", nome: "Forze dell'ordine", descrizione: "Polizia, Carabinieri, Guardia di Finanza, Forze armate" },
  { id: "inps", nome: "INPS e previdenza", descrizione: "INPS, INAIL e enti previdenziali" },
  { id: "ministeri", nome: "Ministeri e agenzie", descrizione: "Ministeri, agenzie fiscali, autorità" },
  { id: "sanita", nome: "Sanità", descrizione: "ASL, aziende ospedaliere, ruoli amministrativi" },
  { id: "universita", nome: "Università e ricerca", descrizione: "Atenei ed enti di ricerca" },
  { id: "altro", nome: "Altri enti", descrizione: "Tutti gli altri bandi pubblicati su inPA" },
] as const;
export type CompartoId = (typeof COMPARTI)[number]["id"];
export const COMPARTO_IDS = COMPARTI.map((c) => c.id) as [CompartoId, ...CompartoId[]];

// Materie della banca statica: quelle che chiedono i bandi dei comparti seguiti
// (vedi MATERIE_TIPICHE in packages/functions/src/jobs/inpa.ts).
export const MATERIE = [
  { id: "diritto-amministrativo", nome: "Diritto amministrativo", icona: "scale" },
  { id: "diritto-costituzionale", nome: "Diritto costituzionale", icona: "landmark" },
  { id: "contabilita-pubblica", nome: "Contabilità pubblica", icona: "coins" },
  { id: "diritto-lavoro", nome: "Lavoro pubblico e previdenza", icona: "briefcase" },
  { id: "diritto-penale", nome: "Diritto penale", icona: "gavel" },
  { id: "italiano", nome: "Italiano", icona: "book-open" },
  { id: "storia", nome: "Storia", icona: "hourglass" },
  { id: "geografia", nome: "Geografia", icona: "globe" },
  { id: "logica", nome: "Logica", icona: "puzzle" },
  { id: "matematica", nome: "Matematica", icona: "calculator" },
  { id: "informatica", nome: "Informatica", icona: "monitor" },
  { id: "inglese", nome: "Inglese", icona: "languages" },
] as const;
export type MateriaId = (typeof MATERIE)[number]["id"];
export const MATERIA_IDS = MATERIE.map((m) => m.id) as [MateriaId, ...MateriaId[]];

/** Le domande di una banca dati ufficiale stanno nella "materia" bd#<id della banca>. */
export const PREFISSO_BANCA_DATI = "bd#";
export const nomeMateria = (id: string) =>
  id.startsWith(PREFISSO_BANCA_DATI) ? "Banca dati ufficiale" : (MATERIE.find((m) => m.id === id)?.nome ?? id);
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
  /** Un annuncio ogni DOMANDE_TRA_ANNUNCI domande di studio (solo Free). */
  pubblicita: boolean;
}

/** Lunghezze di una sessione di studio tra cui scegliere; il piano ne fissa il massimo. */
export const DOMANDE_STUDIO = [10, 20, 30] as const;

/** Ogni quante domande di studio compare un annuncio nel piano Free. */
export const DOMANDE_TRA_ANNUNCI = 5;

export interface Piano {
  id: PianoId;
  nome: string;
  slogan: string;
  /** Prezzi provvisori: si decidono sui dati della beta. */
  prezzo: { mensile: number; annuale: number };
  funzioni: string[];
  limiti: Limiti;
}

/**
 * true = tutti i piani a 0,50 € (il minimo di Stripe in euro), per prove con soldi veri.
 * In dev non serve: Stripe è in modalità test e non addebita nulla.
 */
export const PREZZI_DI_PROVA = false;

/** Prezzi di listino, provvisori: si decidono sui dati della beta. */
const LISTINO = {
  medium: { mensile: 9.99, annuale: 79.99 },
  pro: { mensile: 19.99, annuale: 159.99 },
} as const;

const prezzo = (piano: keyof typeof LISTINO) => (PREZZI_DI_PROVA ? { mensile: 0.5, annuale: 0.5 } : { ...LISTINO[piano] });

export const PIANI: Record<PianoId, Piano> = {
  free: {
    id: "free",
    nome: "Free",
    slogan: "Per iniziare",
    prezzo: { mensile: 0, annuale: 0 },
    funzioni: [
      "Avvisi sui nuovi bandi",
      "1 concorso seguito",
      "Domande dalla nostra banca, scritta da libri di testo e fonti online selezionati",
      "Sessioni di studio da 10 domande",
      "1 simulazione a settimana",
      "Con pubblicità ogni 5 domande",
    ],
    limiti: { concorsiSeguiti: 1, simulazioniSettimana: 1, domandePerSessioneStudio: 10, bancheDati: false, ai: false, pubblicita: true },
  },
  medium: {
    id: "medium",
    nome: "Medium",
    slogan: "Tutto per superare il concorso",
    prezzo: prezzo("medium"),
    funzioni: [
      "Banche dati ufficiali dei tuoi concorsi, appena escono",
      "Concorsi seguiti illimitati",
      "Simulazioni illimitate da 50/60 domande",
      "Sessioni di studio da 10, 20 o 30 domande",
      "Statistiche per materia",
      "Senza pubblicità",
    ],
    limiti: { concorsiSeguiti: null, simulazioniSettimana: null, domandePerSessioneStudio: 30, bancheDati: true, ai: false, pubblicita: false },
  },
  pro: {
    id: "pro",
    nome: "Pro",
    slogan: "Con il tutor AI",
    prezzo: prezzo("pro"),
    funzioni: [
      "Tutto il piano Medium, banche dati comprese",
      "Tutor AI interattivo che spiega argomenti ed errori",
      "Domande generate sui tuoi punti deboli",
      "Piano di studio adattivo",
    ],
    limiti: { concorsiSeguiti: null, simulazioniSettimana: null, domandePerSessioneStudio: 30, bancheDati: true, ai: true, pubblicita: false },
  },
};

// ── Feedback sull'app ────────────────────────────────────────────────────────

export interface Feedback {
  /** 1–5 stelle */
  voto: number;
  testo?: string;
  /** Ultima modifica (ISO) */
  il: string;
}

export const GIORNI_TRA_FEEDBACK = 15;

/** Da quando si può di nuovo modificare il feedback; null = si può già adesso. */
export function feedbackModificabileDal(feedback: Feedback | undefined, ora = new Date()): string | null {
  if (!feedback) return null;
  const dal = new Date(Date.parse(feedback.il) + GIORNI_TRA_FEEDBACK * 86_400_000);
  return dal > ora ? dal.toISOString() : null;
}

// ── Documenti legali ─────────────────────────────────────────────────────────

/** Versione di Termini e Informativa: cambia quando cambiano i testi (pagine /termini, /privacy). */
export const VERSIONE_TERMINI = "2026-10-09";

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
  /** Ultima email di avviso sui nuovi bandi (job avvisi). */
  ultimoAvvisoIl?: string;
  /** Scadenza per cui è già partita l'email di promemoria (evita doppioni). */
  promemoriaInviatoPer?: string;
  /** Accettazione di Termini e Informativa (versione e data) */
  terminiAccettati?: { versione: string; il: string };
  /** Ultimo acquisto: prova del consenso all'esecuzione immediata e della rinuncia al recesso */
  ultimoAcquisto?: {
    piano: PianoId;
    periodo: Periodo;
    il: string;
    rinunciaRecesso: true;
    versioneTermini: string;
    /** Importo pagato in euro, sconto compreso */
    importo?: number;
    codiceSconto?: string;
  };
  /** Codici sconto già usati: ognuno vale una volta per utente. */
  codiciUsati?: string[];
  /** Parere sull'app: si può cambiare ogni GIORNI_TRA_FEEDBACK giorni. */
  feedback?: Feedback;
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
  /** Prima volta che lo scraper l'ha visto: serve agli avvisi "nuovi bandi per te". */
  primoImportoIl?: string;
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
  /** Banca dati pubblicata per questo concorso (tabella banche-dati) */
  bancaDatiId?: string;
  /** Segnato dall'admin: il concorso è finito e sparisce anche dai bandi scaduti */
  conclusoIl?: string;
  fonte: "inpa";
  aggiornatoIl: string;
}

/**
 * Banca dati ufficiale di un concorso, caricata dall'admin come PDF (tabella banche-dati).
 * Il PDF va nel bucket dei contenuti; la Lambda estrai-banca-dati ne ricava le domande.
 */
export interface BancaDati {
  id: string;
  /** Comparto in cui compare nella sezione Banche dati (es. forze-ordine) */
  comparto?: CompartoId;
  /** Anno della banca dati, es. 2026 */
  anno?: number;
  /** Concorso a cui è collegata (facoltativo): le sue simulazioni Medium/Pro la usano */
  concorsoId?: string;
  concorsoTitolo?: string;
  titolo: string;
  /** Materia di tutte le domande, se la banca dati è di una sola materia */
  materia?: MateriaId;
  /** Come è indicata la risposta giusta nel PDF (auto = prova tutti i modi) */
  formato: "auto" | "indicata" | "segnata" | "chiave" | "prima";
  stato: "caricamento" | "estrazione" | "estratta" | "errore" | "pubblicata";
  nomeFile: string;
  dimensione: number;
  caricataIl: string;
  caricataDa: string;
  pagine?: number;
  domande?: number;
  scartate?: number;
  /** Quante domande per modo di trovare la giusta, es. { chiave: 980 } */
  formati?: Record<string, number>;
  /** Prime domande estratte, per controllarle prima di pubblicare */
  esempi?: { numero: number; testo: string; opzioni: string[]; corretta: number }[];
  /** Prime domande scartate con il motivo */
  problemi?: { numero: number; motivo: string }[];
  errore?: string;
  estrattaIl?: string;
  pubblicataIl?: string;
}

/**
 * Codice sconto generato dall'admin (tabella codici). Vale sul prezzo del piano scelto,
 * una volta per utente, finché è attivo, non scaduto e con usi disponibili.
 */
export interface CodiceSconto {
  /** Maiuscole e numeri, es. BENVENUTO20 */
  codice: string;
  /** 1–100 */
  percentuale: number;
  /** Piani su cui vale; assente = tutti i piani a pagamento */
  piani?: ("medium" | "pro")[];
  /** Ultimo giorno di validità (ISO); assente = senza scadenza */
  validoFino?: string;
  /** Assente = illimitati */
  usiMassimi?: number;
  usi: number;
  attivo: boolean;
  nota?: string;
  creatoIl: string;
  creatoDa: string;
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
  /** Versione della banca domande: v1, poi v2… */
  versione: string;
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
  /** Sessione sulle domande di una banca dati ufficiale */
  bancaDati?: { id: string; titolo: string };
  consegnataIl?: string;
  risposte?: (number | null)[];
  esito?: Esito;
}
