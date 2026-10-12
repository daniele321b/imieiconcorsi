// Modello di dominio condiviso tra frontend e microservizi. Niente dipendenze AWS qui:
// questo file finisce anche nel bundle del browser.
//
// Contiene: comparti e materie, piani con prezzi e limiti, costi e tetti dell'AI, tipi delle
// richieste di assistenza, profilo dell'utente, concorsi, banche dati, progressi, codici
// sconto e invito, domande e sessioni. Se cambi un tipo qui, controlla sia le Lambda
// (packages/functions) sia il sito (packages/web): TypeScript segnala dove serve adeguare.

/** Comparti in cui si dividono i bandi (sezione "Concorsi", interessi del profilo, banche dati). */
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
/** Gli id dei comparti come tupla, per gli schemi zod (z.enum). */
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
/** Gli id delle materie come tupla, per gli schemi zod (z.enum). */
export const MATERIA_IDS = MATERIE.map((m) => m.id) as [MateriaId, ...MateriaId[]];

/** Le domande di una banca dati ufficiale stanno nella "materia" bd#<id della banca>. */
export const PREFISSO_BANCA_DATI = "bd#";
/** Nome leggibile di una materia ("logica" → "Logica"); per le banche dati, "Banca dati ufficiale". */
export const nomeMateria = (id: string) =>
  id.startsWith(PREFISSO_BANCA_DATI) ? "Banca dati ufficiale" : (MATERIE.find((m) => m.id === id)?.nome ?? id);
/** Nome leggibile di un comparto. */
export const nomeComparto = (id: string) => COMPARTI.find((c) => c.id === id)?.nome ?? id;

/** Ogni quanto l'utente riceve l'email con i nuovi bandi dei suoi comparti (profilo). */
export type FrequenzaAvvisi = "giornaliero" | "settimanale" | "mai";

/** Risposte delle banche dati: la giusta sempre per prima, o mescolate (core/risposte.ts). */
export type ModoRisposte = "prima" | "mescolate";

// ── Piani ────────────────────────────────────────────────────────────────────

/** I tre piani. Il piano di un utente è il suo gruppo Cognito (nessun gruppo = free). */
export type PianoId = "free" | "medium" | "pro";

/** Durate vendute: pagamento unico, nessun rinnovo automatico. Il trimestre copre la preparazione di un concorso. */
export const PERIODI = [
  { id: "mensile", nome: "30 giorni", giorni: 30, mesi: 1 },
  { id: "trimestrale", nome: "90 giorni", giorni: 90, mesi: 3 },
  { id: "annuale", nome: "1 anno", giorni: 365, mesi: 12 },
] as const;
export type Periodo = (typeof PERIODI)[number]["id"];
export const PERIODO_IDS = PERIODI.map((p) => p.id) as [Periodo, ...Periodo[]];
/** Dettagli di una durata (nome, giorni, mesi). */
export const periodo = (id: Periodo) => PERIODI.find((p) => p.id === id)!;

/** Cosa può fare un utente con il suo piano: lo controllano le Lambda (ctx.limiti) e il sito. */
export interface Limiti {
  /** null = illimitato */
  concorsiSeguiti: number | null;
  simulazioniSettimana: number | null;
  domandePerSessioneStudio: number;
  /** Massimo di domande in una simulazione; oltre SIMULAZIONE_STANDARD si sceglie a mano (Medium e Pro). */
  domandePerSimulazione: number;
  /** Banche dati ufficiali senza limiti (Medium e Pro). */
  bancheDati: boolean;
  /** Utilizzi delle banche dati a settimana (sessioni o consultazione); null = illimitati. */
  usiBancheDatiSettimana: number | null;
  /** Tutor e domande generate (solo Pro). */
  ai: boolean;
  /** Crediti AI al mese (vedi COSTI_AI); 0 = niente AI. */
  gettoniAi: number;
  /** Un annuncio ogni DOMANDE_TRA_ANNUNCI domande di studio (solo Free). */
  pubblicita: boolean;
}

/** Domande massime di una simulazione nel Free (le scelte 30, 50, 60). */
export const SIMULAZIONE_STANDARD = 60;
/** Medium e Pro scelgono a mano quante domande, fino a questo numero. */
export const SIMULAZIONE_MAX = 100;
/** Domande minime di una sessione. */
export const DOMANDE_MIN = 5;

/** Lunghezze di una sessione di studio tra cui scegliere; il piano ne fissa il massimo. */
export const DOMANDE_STUDIO = [10, 20, 30] as const;

/** Ogni quante domande di studio compare un annuncio nel piano Free. */
export const DOMANDE_TRA_ANNUNCI = 5;

/**
 * Quanti gettoni costa ogni azione AI. Il costo vero dipende dai token: una risposta del
 * tutor ne usa ~1.500, un allenamento da 5 domande ~5.000 (Claude Haiku 4.5 su Bedrock,
 * ~0,2 e ~1 centesimo). Con GETTONI_AI_PRO al mese un utente Pro costa al massimo ~0,5-1 €.
 */
export const COSTI_AI = { tutor: 1, allenamento: 3 } as const;
/** Gettoni AI al mese del piano Pro. */
export const GETTONI_AI_PRO = 150;

/**
 * Prezzi del modello in dollari per milione di token (Claude Haiku 4.5 su Bedrock, profilo EU),
 * arrotondati per eccesso: servono a stimare la spesa per i tetti qui sotto. Se cambi modello,
 * aggiorna anche questi.
 */
export const PREZZI_AI_USD = { ingresso: 1.1, uscita: 5.5 } as const;
/**
 * Tetti di spesa AI al mese, in dollari: per utente e per tutta la piattaforma. Sono una rete
 * di sicurezza oltre ai gettoni (contro abusi e bollette inattese): in dev si cambiano da
 * Terraform (ai_tetto_utente_usd, ai_tetto_mensile_usd), questi sono i valori di riserva.
 */
export const TETTO_AI_UTENTE_USD = 3;
/** Tetto di riserva per tutta la piattaforma (vedi sopra). */
export const TETTO_AI_MESE_USD = 50;
/** Richieste AI al minuto per utente (contro script e doppi clic a raffica). */
export const AI_AL_MINUTO = 6;
/** Domande generate per ogni allenamento AI. */
export const DOMANDE_ALLENAMENTO_AI = 5;

/** Un piano come lo mostra la pagina Piani: nome, prezzi per durata, funzioni elencate e limiti. */
export interface Piano {
  id: PianoId;
  nome: string;
  slogan: string;
  /** Prezzi provvisori: si decidono sui dati della beta. */
  prezzo: Record<Periodo, number>;
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
  medium: { mensile: 9.99, trimestrale: 19.99, annuale: 39.99 },
  pro: { mensile: 14.99, trimestrale: 29.99, annuale: 69.99 },
} as const;

const prezzo = (piano: keyof typeof LISTINO) =>
  PREZZI_DI_PROVA ? { mensile: 0.5, trimestrale: 0.5, annuale: 0.5 } : { ...LISTINO[piano] };

/** Utilizzi gratuiti delle banche dati ufficiali a settimana nel piano Free. */
export const USI_BANCHE_DATI_FREE = 3;

/** I tre piani con prezzi, testi e limiti: unica fonte per backend e sito. */
export const PIANI: Record<PianoId, Piano> = {
  free: {
    id: "free",
    nome: "Free",
    slogan: "Per iniziare",
    prezzo: { mensile: 0, trimestrale: 0, annuale: 0 },
    funzioni: [
      "Avvisi sui nuovi bandi",
      "1 concorso seguito",
      "Domande dalla nostra banca, scritta da libri di testo e fonti online selezionati",
      `Banche dati ufficiali: ${USI_BANCHE_DATI_FREE} utilizzi a settimana`,
      "Sessioni di studio da 10 domande",
      "1 simulazione a settimana",
      "Con pubblicità ogni 5 domande",
    ],
    limiti: { concorsiSeguiti: 1, simulazioniSettimana: 1, domandePerSessioneStudio: 10, domandePerSimulazione: SIMULAZIONE_STANDARD, bancheDati: false, usiBancheDatiSettimana: USI_BANCHE_DATI_FREE, ai: false, gettoniAi: 0, pubblicita: true },
  },
  medium: {
    id: "medium",
    nome: "Medium",
    slogan: "Tutto per superare il concorso",
    prezzo: prezzo("medium"),
    funzioni: [
      "Banche dati ufficiali senza limiti, appena escono",
      "Concorsi seguiti illimitati",
      `Simulazioni illimitate, con il numero di domande che vuoi (fino a ${SIMULAZIONE_MAX})`,
      "Sessioni di studio da 10, 20 o 30 domande",
      "Statistiche per materia",
      "Senza pubblicità",
    ],
    limiti: { concorsiSeguiti: null, simulazioniSettimana: null, domandePerSessioneStudio: 30, domandePerSimulazione: SIMULAZIONE_MAX, bancheDati: true, usiBancheDatiSettimana: null, ai: false, gettoniAi: 0, pubblicita: false },
  },
  pro: {
    id: "pro",
    nome: "Pro",
    slogan: "Con il tutor AI",
    prezzo: prezzo("pro"),
    funzioni: [
      "Tutto il piano Medium, banche dati comprese",
      "Tutor AI che spiega argomenti ed errori, domanda per domanda",
      "Allenamenti mirati: domande nuove, scritte dal tutor sugli argomenti in cui sbagli",
      `${GETTONI_AI_PRO} crediti AI al mese: ${COSTI_AI.tutor} per ogni domanda al tutor, ${COSTI_AI.allenamento} per un allenamento`,
    ],
    limiti: { concorsiSeguiti: null, simulazioniSettimana: null, domandePerSessioneStudio: 30, domandePerSimulazione: SIMULAZIONE_MAX, bancheDati: true, usiBancheDatiSettimana: null, ai: true, gettoniAi: GETTONI_AI_PRO, pubblicita: false },
  },
};

// ── Feedback sull'app ────────────────────────────────────────────────────────

/** Parere sull'app lasciato dal profilo. */
export interface Feedback {
  /** 1–5 stelle */
  voto: number;
  testo?: string;
  /** Ultima modifica (ISO) */
  il: string;
}

/** Giorni da aspettare prima di poter cambiare il parere. */
export const GIORNI_TRA_FEEDBACK = 15;

/** Da quando si può di nuovo modificare il feedback; null = si può già adesso. */
export function feedbackModificabileDal(feedback: Feedback | undefined, ora = new Date()): string | null {
  if (!feedback) return null;
  const dal = new Date(Date.parse(feedback.il) + GIORNI_TRA_FEEDBACK * 86_400_000);
  return dal > ora ? dal.toISOString() : null;
}

// ── Richieste di assistenza ──────────────────────────────────────────────────

/** Tipi di richiesta, ognuno con un modello di testo già compilato da completare. */
export const TIPI_RICHIESTA = [
  {
    id: "banca-dati",
    nome: "Aggiungere una banca dati",
    modello: "Concorso: \nEnte: \nLink alla banca dati ufficiale (se lo hai): \n",
  },
  {
    id: "domanda-errata",
    nome: "Domanda o risposta sbagliata",
    modello: "Cosa non va nella domanda: \nQual è secondo te la risposta giusta (e dove l'hai letto): \n",
  },
  {
    id: "accesso",
    nome: "Problema di accesso",
    modello: "Come accedi (email e password, Google o Facebook): \nCosa succede, con il messaggio di errore se c'è: \n",
  },
  {
    id: "pagamento",
    nome: "Problema con un pagamento",
    modello: "Codice dell'ordine (se ce l'hai, dall'email di conferma): \nData del pagamento: \nCosa è successo: \n",
  },
  { id: "piano", nome: "Piano e scadenza", modello: "Il tuo piano: \nLa domanda: \n" },
  {
    id: "errore-app",
    nome: "Errore nell'app",
    modello: "In quale pagina: \nCosa stavi facendo: \nCosa è successo invece: \nDispositivo e browser (es. iPhone, Chrome): \n",
  },
  { id: "suggerimento", nome: "Suggerimento", modello: "" },
  { id: "altro", nome: "Altro", modello: "" },
] as const;
export type TipoRichiesta = (typeof TIPI_RICHIESTA)[number]["id"];
/** Gli id dei tipi come tupla, per lo schema zod della nuova richiesta. */
export const TIPO_RICHIESTA_IDS = TIPI_RICHIESTA.map((t) => t.id) as [TipoRichiesta, ...TipoRichiesta[]];
/** Nome leggibile di un tipo di richiesta. */
export const nomeTipoRichiesta = (id: TipoRichiesta) => TIPI_RICHIESTA.find((t) => t.id === id)?.nome ?? id;

/** Aperta = in attesa di risposta; in lavorazione = l'assistenza ci sta lavorando; chiusa = risolta. */
export type StatoRichiesta = "aperta" | "in-lavorazione" | "chiusa";

/** Richiesta di un utente alla piattaforma (tabella richieste: userId + id). */
export interface Richiesta {
  userId: string;
  /** Ordinabile per data (come le sessioni) */
  id: string;
  /** cognito:username, per scrivere all'utente quando l'assistenza risponde */
  username: string;
  tipo: TipoRichiesta;
  stato: StatoRichiesta;
  /** Da dove nasce: la domanda segnalata, il concorso, la banca dati, l'ordine */
  contesto?: {
    concorsoId?: string;
    bancaDatiId?: string;
    ordineId?: string;
    domanda?: { materia: string; id: string; testo: string };
  };
  /** Il primo messaggio è la richiesta; poi risposte dell'assistenza e dell'utente */
  messaggi: { da: "utente" | "assistenza"; testo: string; il: string }[];
  /** C'è una risposta dell'assistenza che l'utente non ha ancora visto */
  daLeggere?: boolean;
  creataIl: string;
  aggiornataIl: string;
}

// ── Documenti legali ─────────────────────────────────────────────────────────

/** Versione di Termini e Informativa: cambia quando cambiano i testi (pagine /termini, /privacy). */
export const VERSIONE_TERMINI = "2026-10-10";

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
  /** Avvisi mandati e non aperti di fila: oltre una soglia si riducono, poi si sospendono */
  avvisiNonAperti?: number;
  /** Ultima volta che ha aperto un avviso, cliccato un suo link o usato l'app */
  ultimaLetturaIl?: string;
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
  /** Codice "invita un amico" di questo utente (tabella codici, tipo invito) */
  codiceInvito?: string;
  /** userId di chi l'ha invitato (si può indicare solo prima del primo acquisto) */
  invitatoDa?: string;
  /** Quando il suo primo acquisto ha fatto scattare il premio per chi l'ha invitato */
  invitoPremiato?: string;
  /** Premi ricevuti per gli amici invitati, per anno (massimo MAX_PREMI_INVITO_ANNO) */
  premiInvito?: { anno: string; n: number };
  /** Parere sull'app: si può cambiare ogni GIORNI_TRA_FEEDBACK giorni. */
  feedback?: Feedback;
  /** Utilizzi delle banche dati nella settimana (piano Free): settimana = lunedì UTC, aperte = banche già consultate. */
  usiBancheDati?: { settimana: string; usi: number; aperte?: string[] };
  /**
   * Uso dell'AI nel mese (YYYY-MM, UTC), a mese nuovo si riparte da zero: gettoni usati,
   * token consumati e spesa stimata in milionesimi di dollaro (per il tetto per utente).
   */
  ai?: { mese: string; usati: number; tokenIngresso?: number; tokenUscita?: number; spesaMicroUsd?: number };
  /** Minuto (YYYY-MM-DDTHH:MM) e richieste AI fatte in quel minuto: massimo AI_AL_MINUTO. */
  aiMinuto?: string;
  aiNelMinuto?: number;
  /** Ultimo login (trigger Cognito, functions/src/auth/accesso.ts) e quanti in tutto */
  ultimoAccessoIl?: string;
  accessi?: number;
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
  /** Richieste di assistenza con una risposta che l'utente non ha ancora visto (solo GET /me) */
  richiesteDaLeggere?: number;
}

/** Bando di concorso importato da inPA ogni mattina (tabella concorsi). */
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
  /** Il testo del bando prevede una banca dati di domande: quando esce va scaricata (avviso all'admin). */
  bancaDatiPrevista: boolean;
  /** La frase del bando da cui lo si capisce, mostrata nella pagina del bando */
  bancaDatiFrase?: string;
  /** La banca dati ufficiale è stata pubblicata e importata. */
  bancaDati: boolean;
  /** Banca dati pubblicata per questo concorso (tabella banche-dati) */
  bancaDatiId?: string;
  /** Segnato dall'admin: il concorso è finito e sparisce anche dai bandi scaduti */
  conclusoIl?: string;
  /**
   * Campi corretti dall'admin (nome, ente, scadenza…): sono già applicati al bando e l'import
   * del mattino li riapplica sopra i dati di inPA (core/concorsi.ts, conModificheAdmin).
   */
  modificheAdmin?: ModificheConcorso;
  /** Valori di inPA dei campi corretti (null = su inPA il campo manca): per annullare le modifiche */
  originaliInpa?: Partial<Record<CampoModificabile, unknown>>;
  modificatoIl?: string;
  fonte: "inpa";
  aggiornatoIl: string;
}

/** Campi di un bando che l'admin può correggere. "figura" è il nome che si vede (l'anno si aggiunge da solo). */
export const CAMPI_MODIFICABILI = ["figura", "titolo", "ente", "scadenza", "posti", "sedi", "comparto", "materie", "descrizione", "bancaDatiPrevista"] as const;
export type CampoModificabile = (typeof CAMPI_MODIFICABILI)[number] | "materieStimate";
/** Le correzioni dell'admin a un bando. */
export type ModificheConcorso = Partial<Pick<Concorso, CampoModificabile>>;

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
  /** Primo concorso collegato (campo storico: la lista completa è `concorsi`) */
  concorsoId?: string;
  concorsoTitolo?: string;
  /**
   * Concorsi collegati (anche più di uno, es. una banca "Polizia 2026" per più bandi aperti):
   * da pubblicata, ognuno ha bancaDatiId = questa banca, il link alla consultazione e le
   * simulazioni con le domande ufficiali. Si legge con concorsiDellaBanca().
   */
  concorsi?: { id: string; titolo: string; ente?: string }[];
  titolo: string;
  /** Materia di tutte le domande, se la banca dati è di una sola materia */
  materia?: MateriaId;
  /**
   * Come è indicata la risposta giusta nel PDF (auto = prova tutti i modi). "risposta" = tabella
   * con la sola risposta esatta: le alternative si ricavano (functions/src/banche-dati/tabella.ts).
   */
  formato: "auto" | "indicata" | "segnata" | "chiave" | "prima" | "risposta";
  /**
   * Ordine delle risposte agli utenti. Assente o "mescolate": ordine casuale fisso per domanda,
   * così non si impara la lettera (in molti PDF la giusta è sempre la A). "pdf": come nel file.
   */
  ordineRisposte?: "mescolate" | "pdf";
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
  /** Domande estratte da controllare prima di pubblicare, nell'ordine del PDF (le prime di ogni sezione) */
  esempi?: { numero: number; testo: string; opzioni: string[]; corretta: number; sezione?: string; alternativeRicavate?: boolean }[];
  /** Domande con le alternative ricavate da domande simili (il PDF dava solo la risposta esatta) */
  alternativeRicavate?: number;
  /** Sezioni del PDF (es. "Matematica"): diventano l'argomento delle domande */
  sezioni?: string[];
  /** Dove inizia ogni sezione (numero della prima domanda) e quante domande ha: per saltarci consultando */
  indiceSezioni?: { sezione: string; da: number; domande: number }[];
  /** Prime domande scartate con il motivo */
  problemi?: { numero: number; motivo: string }[];
  errore?: string;
  estrattaIl?: string;
  pubblicataIl?: string;
}

/** Concorsi collegati a una banca dati (anche quelle salvate prima della lista `concorsi`). */
export function concorsiDellaBanca(b: Pick<BancaDati, "concorsi" | "concorsoId" | "concorsoTitolo">): { id: string; titolo: string; ente?: string }[] {
  if (b.concorsi) return b.concorsi;
  return b.concorsoId ? [{ id: b.concorsoId, titolo: b.concorsoTitolo ?? b.concorsoId }] : [];
}

/** Nome di un concorso con l'ente, in una riga: "Ente — figura" (es. nelle email all'admin). */
export const nomeConcorsoBreve = (c: Pick<Concorso, "ente" | "figura" | "titolo">) => `${c.ente} — ${c.figura || c.titolo}`.slice(0, 300);

// ── Progressi nelle banche dati ──────────────────────────────────────────────

/**
 * Domande già fatte da un utente in una banca dati (tabella progressi: userId + bancaId).
 * Due mappe di bit indicizzate dal numero della domanda (bit n = domanda n): 6.000 domande
 * stanno in 750 byte per mappa. Si aggiornano alla consegna di ogni sessione sulla banca dati.
 */
export interface ProgressoBanca {
  userId: string;
  bancaId: string;
  /** Bit acceso = domanda risposta almeno una volta (in bianco non conta) */
  fatte: Uint8Array;
  /** Bit acceso = domanda sbagliata l'ultima volta che è stata fatta */
  sbagliate: Uint8Array;
  nFatte: number;
  nSbagliate: number;
  /** Bit acceso = domanda salvata tra le preferite (stella), per ritrovarla dopo */
  preferite?: Uint8Array;
  nPreferite?: number;
  /** Estrazione della banca a cui si riferiscono i numeri: se l'admin la rifà, si riparte da zero */
  estrattaIl?: string;
  /** Sale a ogni scrittura: due consegne insieme non si cancellano a vicenda */
  rev: number;
  aggiornatoIl: string;
}

/** Quali domande di una banca dati proporre in una sessione. */
export const SELEZIONI_BANCA = ["nuove", "sbagliate", "preferite", "tutte"] as const;
export type SelezioneBanca = (typeof SELEZIONI_BANCA)[number];

// ── Invita un amico ──────────────────────────────────────────────────────────

/** Giorni gratis a chi invita, quando l'amico compra un piano (30 giorni o più). */
export const GIORNI_PREMIO_INVITO = 30;
/** Premi massimi in un anno per uno stesso utente. */
export const MAX_PREMI_INVITO_ANNO = 12;

/** Codice "invita un amico" (tabella codici, accanto ai codici sconto). */
export interface CodiceInvito {
  codice: string;
  tipo: "invito";
  /** userId di chi invita */
  proprietario: string;
  /** Amici che hanno inserito il codice */
  iscritti: number;
  /** Amici che hanno comprato un piano (premi scattati) */
  premi: number;
  creatoIl: string;
}

/**
 * Codice sconto generato dall'admin (tabella codici). Vale sul prezzo del piano scelto,
 * una volta per utente, finché è attivo, non scaduto e con usi disponibili.
 */
export interface CodiceSconto {
  /** Maiuscole e numeri, es. BENVENUTO20 */
  codice: string;
  /** Assente = codice sconto; "invito" = codice di un utente (CodiceInvito), non uno sconto */
  tipo?: "invito";
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

/**
 * Domanda a scelta multipla (tabella questions: materia + id). Le domande delle banche dati
 * ufficiali hanno materia "bd#<id banca>" e id "n00042" (il numero nel PDF).
 */
export interface Domanda {
  materia: MateriaId;
  id: string;
  argomento: string;
  /** Difficoltà da 1 a 5: lo studio propone prima le domande vicine al livello dell'utente */
  livello: number;
  testo: string;
  opzioni: string[];
  /** Indice della risposta giusta in opzioni (0 = A) */
  corretta: number;
  spiegazione: string;
  /** Da dove viene: legge, manuale o banca dati ufficiale */
  fonte: string;
  /** Versione della banca domande: v1, poi v2… */
  versione: string;
}

/** Domanda come la vede l'utente durante una simulazione (senza soluzione). */
export type DomandaPubblica = Omit<Domanda, "corretta" | "spiegazione" | "fonte">;

/** Studio = correzione subito dopo ogni risposta; simulazione = a tempo, correzione alla consegna. */
export type TipoSessione = "studio" | "simulazione";

/** Punteggio delle simulazioni: punti per risposta giusta, sbagliata e non data. */
export interface Regole {
  corretta: number;
  errata: number;
  omessa: number;
  /** Percentuale minima del punteggio massimo per superare la prova */
  soglia: number;
}

/** Regole usate da tutte le sessioni: +1 giusta, −0,25 sbagliata, 0 non data, si passa con il 70%. */
export const REGOLE_DEFAULT: Regole = { corretta: 1, errata: -0.25, omessa: 0, soglia: 0.7 };

/** Risultato di una sessione consegnata, in totale e per materia. */
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

/**
 * Sessione di studio o simulazione (tabella attempts: userId + id ordinabile per data).
 * Contiene solo le chiavi delle domande: il testo si rilegge dalla tabella questions.
 */
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
  /**
   * Sessione sulle domande di una banca dati ufficiale. ordine = come l'utente ha scelto di
   * vedere le risposte (le sessioni di prima non ce l'hanno: restano come salvate).
   */
  bancaDati?: { id: string; titolo: string; mescolate?: boolean; ordine?: ModoRisposte };
  consegnataIl?: string;
  risposte?: (number | null)[];
  esito?: Esito;
}
