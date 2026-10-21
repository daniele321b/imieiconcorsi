// Inoltro della posta in arrivo (info@imieiconcorsi.it e gli altri alias): parte pura, senza AWS.
//
// Un'email ricevuta non si può reinviare così com'è: il mittente originale (es. mario@gmail.com)
// passerebbe dai server di SES, e il provider di chi la riceve (Hotmail) la scarterebbe per i
// controlli antifrode (SPF e DMARC del dominio del mittente). Allora si riscrive l'intestazione:
//   From:     "Mario Rossi tramite iMieiConcorsi" <info@imieiconcorsi.it>   (il nostro dominio, firmato)
//   Reply-To: l'indirizzo vero del mittente (o il suo Reply-To, se ne aveva uno)
// Così "Rispondi" scrive al mittente vero. Il corpo e gli allegati restano byte per byte.

/** Intestazioni da togliere: firme e percorsi del messaggio originale, che dopo la riscrittura
 * non valgono più (una firma DKIM rotta fa scartare il messaggio) o indicano il mittente sbagliato. */
const DA_TOGLIERE = new Set([
  "from",
  "reply-to",
  "sender",
  "return-path",
  "message-id",
  "dkim-signature",
  "domainkey-signature",
  "arc-seal",
  "arc-message-signature",
  "arc-authentication-results",
]);

/** Intestazione "Nome: valore" (con le righe di continuazione già riunite). */
export interface Intestazione {
  nome: string;
  valore: string;
}

/** Divide il messaggio grezzo in intestazioni (una per voce, righe ripiegate riunite) e corpo. */
export function dividiMessaggio(grezzo: string): { intestazioni: Intestazione[]; corpo: string; acapo: string } {
  const acapo = grezzo.includes("\r\n") ? "\r\n" : "\n";
  const fine = grezzo.indexOf(acapo + acapo);
  const testa = fine < 0 ? grezzo : grezzo.slice(0, fine);
  const corpo = fine < 0 ? "" : grezzo.slice(fine + 2 * acapo.length);
  const intestazioni: Intestazione[] = [];
  for (const riga of testa.split(acapo)) {
    // Una riga che inizia con spazio o tab continua l'intestazione di prima (RFC 5322, "folding").
    if (/^[ \t]/.test(riga) && intestazioni.length) {
      intestazioni.at(-1)!.valore += acapo + riga;
      continue;
    }
    const due = riga.indexOf(":");
    if (due > 0) intestazioni.push({ nome: riga.slice(0, due), valore: riga.slice(due + 1).replace(/^ /, "") });
  }
  return { intestazioni, corpo, acapo };
}

/** Il valore di un'intestazione (la prima con quel nome, senza distinguere maiuscole), se c'è. */
export const intestazione = (h: Intestazione[], nome: string) => h.find((x) => x.nome.toLowerCase() === nome.toLowerCase())?.valore;

/**
 * Nome e indirizzo da un campo From: "Mario Rossi <mario@gmail.com>", "mario@gmail.com" o
 * "=?UTF-8?B?...?= <x@y.it>" (il nome codificato resta com'è: lo decodifica il programma di posta).
 */
export function nomeEIndirizzo(from: string): { nome: string; indirizzo: string } {
  const pulito = from.replace(/\r?\n[ \t]+/g, " ").trim();
  const m = pulito.match(/^(.*?)\s*<([^>]+)>\s*$/);
  if (m) return { nome: m[1]!.replace(/^"|"$/g, "").trim(), indirizzo: m[2]!.trim() };
  return { nome: "", indirizzo: pulito };
}

/**
 * Testo per un'intestazione: com'è se ASCII, altrimenti codificato RFC 2047 (=?UTF-8?B?…?=).
 * Il messaggio si tratta come byte grezzi (stringa "latin1": un carattere = un byte), quindi i
 * byte del nome si riprendono così come sono: nelle intestazioni non ASCII sono quasi sempre UTF-8.
 */
export function codifica(testo: string): string {
  if (/^[\x20-\x7e]*$/.test(testo)) return testo;
  return `=?UTF-8?B?${Buffer.from(testo, "latin1").toString("base64")}?=`;
}

/**
 * Il messaggio (byte grezzi in una stringa "latin1", vedi `codifica`) pronto da inoltrare: mittente riscritto sul nostro indirizzo (`alias`, es.
 * info@imieiconcorsi.it), risposta al mittente vero, firme e Message-ID originali tolti (SES ne
 * mette di nuovi). Oggetto, destinatari visibili (To, Cc), corpo e allegati restano com'erano.
 */
export function preparaInoltro(grezzo: string, alias: string, marchio = "iMieiConcorsi"): string {
  const { intestazioni, corpo, acapo } = dividiMessaggio(grezzo);
  const from = intestazione(intestazioni, "From") ?? "";
  const { nome, indirizzo } = nomeEIndirizzo(from);
  const rispondiA = intestazione(intestazioni, "Reply-To") ?? (indirizzo || alias);
  const etichetta = `${nome || indirizzo || "Qualcuno"} tramite ${marchio}`;
  const mittente = /^[\x20-\x7e]*$/.test(etichetta) ? `"${etichetta.replace(/"/g, "'")}" <${alias}>` : `${codifica(etichetta)} <${alias}>`;
  const tenute = intestazioni.filter((h) => !DA_TOGLIERE.has(h.nome.toLowerCase()));
  const testa = [`From: ${mittente}`, `Reply-To: ${rispondiA}`, ...tenute.map((h) => `${h.nome}: ${h.valore}`)];
  return testa.join(acapo) + acapo + acapo + corpo;
}

/**
 * Se il messaggio va scartato invece di inoltrarlo, il motivo. SES controlla virus e spam per noi
 * (receipt.virusVerdict, spamVerdict): FAIL = trovato; GRAY e PROCESSING_FAILED si inoltrano.
 */
export function motivoScarto(verdetti: { virus?: string; spam?: string }): string | undefined {
  if (verdetti.virus === "FAIL") return "virus";
  if (verdetti.spam === "FAIL") return "spam";
  return undefined;
}
