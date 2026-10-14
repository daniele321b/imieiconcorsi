import { PIANI, USI_BANCHE_DATI_FREE, type PianoId } from "./domain";
import { inviaEmail } from "./email";

// Email sul cambio di piano: passaggio a un piano a pagamento e ritorno al Free.
// (La conferma di un acquisto con il riepilogo del pagamento la manda billing.)
// Se l'email non parte il cambio di piano resta valido: l'errore finisce nei log.

/** Data per le email, in ora italiana: "9 ottobre 2026". */
export const dataIt = (iso: string) =>
  new Intl.DateTimeFormat("it-IT", { day: "numeric", month: "long", year: "numeric", timeZone: "Europe/Rome" }).format(
    new Date(iso),
  );

/** Indirizzo del sito, per i link nelle email. */
const sito = () => process.env.SITE_URL ?? "";
/** Prima riga dell'email, con il nome se c'è. */
const saluto = (nome?: string) => `Ciao${nome ? ` ${nome}` : ""},`;

/** Invia un'email di testo con la firma del team; un errore viene solo registrato, non blocca l'operazione. */
async function invia(a: string, oggetto: string, righe: string[]) {
  try {
    await inviaEmail({ a, oggetto, testo: [...righe, "", "Il team di iMieiConcorsi"].join("\n") });
  } catch (err) {
    console.error(`Email "${oggetto}" non inviata`, err);
  }
}

/** Piano a pagamento attivato dall'amministratore (omaggio, assistenza…). */
export async function emailPianoAttivato(args: { a: string; nome?: string; piano: Exclude<PianoId, "free">; scadenza: string | null }) {
  const p = PIANI[args.piano];
  await invia(args.a, `Il piano ${p.nome} è attivo`, [
    saluto(args.nome),
    "",
    `sul tuo account iMieiConcorsi ora è attivo il piano ${p.nome}${args.scadenza ? `, valido fino al ${dataIt(args.scadenza)}` : ""}.`,
    "Hai accesso subito a tutte le sue funzioni, senza pubblicità.",
    ...(args.scadenza ? ["Il piano non si rinnova da solo: alla scadenza l'account torna Free e ti avvisiamo 3 giorni prima."] : []),
    "",
    `Inizia da qui: ${sito()}/app`,
  ]);
}

/** Ritorno al Free: per scadenza del periodo pagato, per scelta dell'utente o dall'admin. */
export async function emailTornatoFree(args: {
  a: string;
  nome?: string;
  pianoPrecedente: Exclude<PianoId, "free">;
  motivo: "scadenza" | "scelta" | "admin";
}) {
  const prima = PIANI[args.pianoPrecedente].nome;
  const perche = {
    scadenza: `il tuo piano ${prima} è scaduto e il tuo account è tornato al piano Free.`,
    scelta: `come hai chiesto, il tuo account è passato dal piano ${prima} al piano Free.`,
    admin: `il tuo account è passato dal piano ${prima} al piano Free.`,
  }[args.motivo];
  await invia(args.a, "Il tuo account è tornato al piano Free", [
    saluto(args.nome),
    "",
    perche,
    "I tuoi progressi e le statistiche restano salvati. Con il Free hai 1 concorso seguito",
    "(resta quello che hai seguito per ultimo; gli altri li ritrovi nello storico del profilo),",
    `sessioni da 10 domande, 1 simulazione e ${USI_BANCHE_DATI_FREE} utilizzi delle banche dati a settimana, e un annuncio ogni 5 domande.`,
    "",
    `Per tornare a un piano a pagamento: ${sito()}/app/piani`,
  ]);
}
