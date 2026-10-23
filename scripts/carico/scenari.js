// Test di carico di iMieiConcorsi con k6 (https://k6.io), contro l'ambiente preprod.
// Si lancia con scripts/deploy.sh carico avvia [scenario], che passa tutte le variabili;
// spiegazioni e lettura dei risultati in docs/TEST-DI-CARICO.md.
//
// Due tipi di utenti finti, insieme:
// - anonimi (QUOTA_ANONIMI, di base il 20%): home, config.json, file del sito, lista dei bandi
//   dai file statici. Tutto da CloudFront, nessuna Lambda: misura il sito pubblico;
// - iscritti (il resto): login su Cognito con un utente di prova (scripts/carico/preprod.mjs),
//   onboarding al primo giro, poi visite come quelle vere: profilo, concorsi seguiti, materie,
//   bandi, sessioni di studio con consegna; chi è Medium anche simulazioni (con pausa) e banche
//   dati. Il tutor AI resta fuori: costa a risposta e il suo limite è Bedrock, non l'app.
//
// Variabili (-e NOME=valore):
//   BASE_URL       https://preprod.imieiconcorsi.it
//   REGION         eu-south-1
//   CLIENT_ID      client Cognito del sito (output user_pool_client_id)
//   PASSWORD       password degli utenti di prova (.carico/password)
//   UTENTI         quanti utenti di prova esistono (di base 1000)
//   SCENARIO       fumo | carico | picco | resistenza | rottura (di base fumo)
//   VU             utenti contemporanei al massimo dello scenario (di base 1000)
//   QUOTA_ANONIMI  parte di utenti senza login (di base 0.2)
//   RITMO          moltiplica le pause tra un'azione e l'altra (di base 1; 0.5 = utenti più veloci)
//   RISORSE        1 = scarica anche JS e CSS del sito come un browser senza cache (di base 1)
//   OUT            cartella dove scrivere il riepilogo (riepilogo.json, riepilogo.txt)
//   COGNITO_URL    solo per provare lo script contro un server finto (di base il Cognito vero)
//
// Il codice gira dentro k6 (non in Node): solo i moduli k6/*, niente librerie npm.

import { check, fail, group, sleep } from "k6";
import exec from "k6/execution";
import http from "k6/http";
import { Counter, Trend } from "k6/metrics";
import { textSummary } from "https://jslib.k6.io/k6-summary/0.1.0/index.js";

const BASE_URL = (__ENV.BASE_URL || "").replace(/\/$/, "");
const API = `${BASE_URL}/api`;
const REGION = __ENV.REGION || "eu-south-1";
const CLIENT_ID = __ENV.CLIENT_ID || "";
const PASSWORD = __ENV.PASSWORD || "";
const UTENTI = Number(__ENV.UTENTI || 1000);
const SCENARIO = __ENV.SCENARIO || "fumo";
const VU = Number(__ENV.VU || 1000);
const QUOTA_ANONIMI = Number(__ENV.QUOTA_ANONIMI || 0.2);
const RITMO = Number(__ENV.RITMO || 1);
const RISORSE = (__ENV.RISORSE || "1") === "1";
const COGNITO_URL = __ENV.COGNITO_URL || `https://cognito-idp.${REGION}.amazonaws.com/`;

if (!BASE_URL) throw new Error("manca BASE_URL (es. https://preprod.imieiconcorsi.it)");
// Mai contro la produzione: il test crea utenti, sessioni e carico veri.
if (/^https:\/\/(www\.)?imieiconcorsi\.it$/.test(BASE_URL)) throw new Error("BASE_URL è la produzione: i test di carico vanno su preprod");

// Comparti e materie come in packages/core/src/domain.ts (COMPARTI, MATERIE).
const COMPARTI = ["enti-locali", "forze-ordine", "inps", "ministeri", "sanita", "universita", "altro"];
const MATERIE = [
  "diritto-amministrativo", "diritto-costituzionale", "contabilita-pubblica", "diritto-lavoro", "diritto-penale",
  "italiano", "storia", "geografia", "attualita", "logica", "matematica", "informatica", "inglese",
];

// --- Scenari ------------------------------------------------------------------
// Ogni scenario è una sequenza di tappe: "in tot tempo arriva a questa parte di VU".
// Gli utenti finti si dividono tra anonimi e iscritti secondo QUOTA_ANONIMI.

const TAPPE = {
  // Prova dello script e dell'ambiente: 5 utenti (non dipende da VU) per due minuti, così ognuno
  // finisce almeno una visita. Sempre per primo. Controlla che tutto funzioni, non i tempi.
  fumo: [
    { duration: "10s", target: 5 / VU },
    { duration: "2m", target: 5 / VU },
  ],
  // Il test vero: salita in 10 minuti fino a VU, 20 minuti fermi lì, discesa.
  carico: [
    { duration: "2m", target: 0.1 },
    { duration: "8m", target: 1 },
    { duration: "20m", target: 1 },
    { duration: "2m", target: 0 },
  ],
  // Picco improvviso (es. post virale, uscita di un bando): da 10% a 100% in un minuto.
  picco: [
    { duration: "2m", target: 0.1 },
    { duration: "1m", target: 1 },
    { duration: "5m", target: 1 },
    { duration: "1m", target: 0.1 },
    { duration: "2m", target: 0.1 },
    { duration: "1m", target: 0 },
  ],
  // Metà di VU per due ore: perdite lente (memoria, token che scadono dopo un'ora, tabelle che crescono).
  resistenza: [
    { duration: "5m", target: 0.5 },
    { duration: "2h", target: 0.5 },
    { duration: "2m", target: 0 },
  ],
  // A gradini oltre VU (fino a 2,5 volte) per trovare dove si rompe: si ferma da solo quando
  // gli errori superano il 5% (abortOnFail).
  rottura: [
    { duration: "5m", target: 0.5 },
    { duration: "5m", target: 1 },
    { duration: "5m", target: 1.5 },
    { duration: "5m", target: 2 },
    { duration: "5m", target: 2.5 },
    { duration: "2m", target: 0 },
  ],
};
if (!TAPPE[SCENARIO]) throw new Error(`scenario sconosciuto: ${SCENARIO} (fumo, carico, picco, resistenza, rottura)`);

/** Le tappe dello scenario per una parte (quota) degli utenti: almeno 1 VU dove serve. */
function tappe(quota) {
  return TAPPE[SCENARIO].map((t) => ({ duration: t.duration, target: t.target === 0 ? 0 : Math.max(1, Math.round(VU * quota * t.target)) }));
}

const scenari = {
  iscritti: { executor: "ramping-vus", exec: "iscritto", startVUs: 0, stages: tappe(1 - QUOTA_ANONIMI), gracefulRampDown: "30s", gracefulStop: "1m" },
};
if (QUOTA_ANONIMI > 0) {
  scenari.anonimi = { executor: "ramping-vus", exec: "anonimo", startVUs: 0, stages: tappe(QUOTA_ANONIMI), gracefulRampDown: "30s", gracefulStop: "1m" };
}

// --- Soglie: quando il test è "passato" -------------------------------------------
// I criteri di docs/TEST-DI-CARICO.md. k6 esce con codice 99 se una soglia non è rispettata.
const rottura = SCENARIO === "rottura";
// Nel fumo i tempi si mostrano ma non decidono l'esito: con poche decine di richieste il p95 è
// fatto quasi solo dagli avvii a freddo delle Lambda (la prima chiamata a ogni servizio, ~1 s).
const tempi = (soglie) => (SCENARIO === "fumo" ? ["max>=0"] : soglie);
const soglie = {
  // Errori veri (5xx, timeout, 4xx inattesi) sotto l'1%; nella prova di rottura ci si ferma al 5%.
  http_req_failed: rottura ? [{ threshold: "rate<0.05", abortOnFail: true, delayAbortEval: "1m" }] : ["rate<0.01"],
  // API: il 95% sotto 800 ms, il 99% sotto 2 secondi.
  "http_req_duration{tipo:api}": tempi(["p(95)<800", "p(99)<2000"]),
  // File statici da CloudFront: il 95% sotto 500 ms.
  "http_req_duration{tipo:statico}": tempi(["p(95)<500"]),
  // Login su Cognito (con il trigger degli accessi): il 95% sotto 1,5 secondi.
  "http_req_duration{tipo:login}": tempi(["p(95)<1500"]),
  // Le risposte hanno il contenuto atteso.
  checks: ["rate>0.99"],
};
// Tempi di ogni rotta dell'API nel riepilogo, per trovare subito la più lenta. "max>=0" è sempre
// vera: serve solo a far stampare la riga a k6, non decide l'esito.
const ROTTE = [
  "GET /me", "PUT /me/profilo", "GET /me/concorsi", "GET /me/statistiche", "GET /concorsi/{id}", "PUT /me/concorsi/{id}",
  "GET /materie", "POST /sessioni", "POST /sessioni/{id}/consegna", "POST /sessioni/{id}/pausa",
  "GET /banche-dati", "GET /banche-dati/{id}/domande",
];
for (const r of ROTTE) soglie[`http_req_duration{name:${r}}`] = ["max>=0"];

export const options = {
  scenarios: scenari,
  thresholds: soglie,
  // Riassunto con mediana, p90, p95 e p99 (di base k6 non mostra il p99).
  summaryTrendStats: ["avg", "min", "med", "p(90)", "p(95)", "p(99)", "max"],
  // Un nome riconoscibile nei log di CloudFront e WAF.
  userAgent: "imieiconcorsi-carico/1.0 (k6)",
  // Le risposte servono solo dove le si legge (responseType: "text" in quelle richieste).
  discardResponseBodies: true,
};

// Metriche nostre: quanto dura una visita intera e quante sessioni si consegnano.
const durataVisita = new Trend("visita_durata", true);
const sessioniConsegnate = new Counter("sessioni_consegnate");
const loginFatti = new Counter("login_fatti");

// --- Utilità ---------------------------------------------------------------------

/** Pausa "da persona" tra min e max secondi, moltiplicata per RITMO. */
function pensa(min, max) {
  sleep((min + Math.random() * (max - min)) * RITMO);
}

/** Un elemento a caso. */
const aCaso = (lista) => lista[Math.floor(Math.random() * lista.length)];

/** n elementi diversi a caso. */
function alcuni(lista, n) {
  const copia = lista.slice();
  const out = [];
  while (out.length < n && copia.length) out.push(copia.splice(Math.floor(Math.random() * copia.length), 1)[0]);
  return out;
}

/** Il JSON della risposta, o null (es. corpo vuoto o errore). */
function corpo(res) {
  try {
    return res.json();
  } catch (_) {
    return null;
  }
}

/**
 * Come un browser: chiede le risposte compresse (k6 da solo non lo fa e scaricherebbe i file
 * interi, il JS del sito 785 KB invece di 211). k6 le decomprime da sé.
 */
const COMPRESSIONE = { "Accept-Encoding": "gzip, deflate, br" };

/** Email dell'utente di prova n: la stessa regola di scripts/carico/preprod.mjs (emailUtente). */
const emailUtente = (n) => `success+carico${String(n).padStart(4, "0")}@simulator.amazonses.com`;

// --- Login (un utente di prova per VU, token tenuto finché vale) ---------------------
// Ogni VU ha le sue variabili: queste valgono per il singolo utente finto.

let token = null;
let scadeAlle = 0;
let profilo = null;

/** Login su Cognito con email e password (USER_PASSWORD_AUTH, attivo solo in preprod). */
function login() {
  const n = ((exec.vu.idInTest - 1) % UTENTI) + 1;
  const res = http.post(
    COGNITO_URL,
    JSON.stringify({ AuthFlow: "USER_PASSWORD_AUTH", ClientId: CLIENT_ID, AuthParameters: { USERNAME: emailUtente(n), PASSWORD: PASSWORD } }),
    {
      headers: { "Content-Type": "application/x-amz-json-1.1", "X-Amz-Target": "AWSCognitoIdentityProviderService.InitiateAuth" },
      tags: { tipo: "login", name: "Cognito InitiateAuth" },
      responseType: "text",
    },
  );
  const dati = corpo(res);
  const ok = check(res, { "login riuscito": (r) => r.status === 200 && !!(dati && dati.AuthenticationResult) });
  if (!ok) {
    // Utente di prova mancante o password sbagliata: il VU riprova al giro dopo.
    console.warn(`login di ${emailUtente(n)} non riuscito: ${res.status} ${String(res.body).slice(0, 200)}`);
    sleep(5);
    return false;
  }
  token = dati.AuthenticationResult.IdToken;
  // Il token vale un'ora: lo si rinnova 5 minuti prima (conta per lo scenario resistenza).
  scadeAlle = Date.now() + (dati.AuthenticationResult.ExpiresIn - 300) * 1000;
  loginFatti.add(1);
  return true;
}

/** Chiamata all'API come fa il sito (lib/api.ts): token nell'intestazione, JSON in entrata e uscita. */
function api(metodo, percorso, body, nome, attesi) {
  const params = {
    headers: Object.assign({ authorization: `Bearer ${token}`, "content-type": "application/json" }, COMPRESSIONE),
    tags: { tipo: "api", name: `${metodo} ${nome || percorso}` },
    responseType: "text",
  };
  // Stati attesi oltre ai 2xx (es. 403 LIMITE_PIANO): non contano come errori.
  if (attesi) params.responseCallback = http.expectedStatuses({ min: 200, max: 299 }, ...attesi);
  const res = http.request(metodo, `${API}${percorso}`, body === undefined ? null : JSON.stringify(body), params);
  return { res, dati: corpo(res) };
}

/** Un file statico (sito, config, bandi), tag "statico". */
function statico(percorso, nome, leggi) {
  return http.get(`${BASE_URL}${percorso}`, { headers: COMPRESSIONE, tags: { tipo: "statico", name: nome || percorso }, responseType: leggi ? "text" : "none" });
}

// --- Pezzi di visita ---------------------------------------------------------------

/** La prima pagina come la carica un browser: HTML, config.json e (con RISORSE) JS e CSS. */
function aprePagina(percorso) {
  const res = statico(percorso, "pagina (index.html)", true);
  check(res, { "pagina 200": (r) => r.status === 200 });
  statico("/config.json", "/config.json");
  if (RISORSE && res.body) {
    const risorse = [];
    const re = /(?:src|href)="(\/assets\/[^"]+\.(?:js|css))"/g;
    let m;
    while ((m = re.exec(res.body))) risorse.push(m[1]);
    if (risorse.length) {
      http.batch(risorse.map((r) => ["GET", `${BASE_URL}${r}`, null, { headers: COMPRESSIONE, tags: { tipo: "statico", name: "/assets/*" } }]));
    }
  }
}

/** Lista dei bandi dai file statici (lib/bandi.ts): indice e file dei comparti scelti. Restituisce i bandi. */
function bandi(comparti) {
  const res = statico("/dati/bandi/indice.json", "/dati/bandi/indice.json", true);
  const indice = corpo(res);
  check(res, { "indice dei bandi": (r) => r.status === 200 && !!(indice && indice.comparti) });
  if (!indice || !indice.comparti) return [];
  let tutti = [];
  for (const c of comparti) {
    const voce = indice.comparti[c];
    if (!voce || !voce.file) continue;
    const r = statico(voce.file, "/dati/bandi/<versione>/<comparto>.json", true);
    const lista = corpo(r);
    if (Array.isArray(lista)) tutti = tutti.concat(lista);
  }
  return tutti;
}

/** Primo accesso: profilo creato da GET /me, poi l'onboarding (comparti, livelli, termini). */
function onboarding() {
  const interessi = alcuni(COMPARTI, 1 + Math.floor(Math.random() * 2));
  const livelli = {};
  for (const m of alcuni(MATERIE, 4)) livelli[m] = 1 + Math.floor(Math.random() * 5);
  pensa(5, 15);
  // Avvisi "mai": il job delle 7 non manda email agli utenti di prova.
  const { res, dati } = api("PUT", "/me/profilo", { interessi, livelli, avvisi: "mai", accettaTermini: true });
  check(res, { "onboarding salvato": (r) => r.status === 200 });
  if (dati) profilo = dati;
}

/** Sessione dall'inizio alla consegna: domande, tempo per rispondere, risposte a caso. */
function sessione(richiesta, secondiPerDomanda) {
  const { res, dati } = api("POST", "/sessioni", richiesta, null, [409]);
  // 409 = nessuna domanda (es. banca dati senza domande nuove): non è un errore dell'app.
  if (res.status === 409) return;
  if (!check(res, { "sessione creata": (r) => r.status === 200 && !!(dati && dati.id && dati.domande && dati.domande.length) })) return;

  const n = dati.domande.length;
  // Simulazione: a volte una pausa a metà (POST /sessioni/{id}/pausa, prima e dopo).
  if (richiesta.tipo === "simulazione" && Math.random() < 0.2) {
    pensa((n * secondiPerDomanda) / 2, (n * secondiPerDomanda) / 2);
    check(api("POST", `/sessioni/${dati.id}/pausa`, { pausa: true }, "/sessioni/{id}/pausa").res, { "pausa": (r) => r.status === 200 });
    pensa(10, 30);
    check(api("POST", `/sessioni/${dati.id}/pausa`, { pausa: false }, "/sessioni/{id}/pausa").res, { "ripresa": (r) => r.status === 200 });
    pensa((n * secondiPerDomanda) / 2, (n * secondiPerDomanda) / 2);
  } else {
    pensa(n * secondiPerDomanda * 0.7, n * secondiPerDomanda * 1.3);
  }
  // Una risposta su dieci lasciata vuota, come chi salta le domande.
  const risposte = dati.domande.map((d) => (Math.random() < 0.1 ? null : Math.floor(Math.random() * ((d.opzioni && d.opzioni.length) || 4))));
  const consegna = api("POST", `/sessioni/${dati.id}/consegna`, { risposte }, "/sessioni/{id}/consegna");
  if (check(consegna.res, { "consegna con esito": (r) => r.status === 200 && !!(consegna.dati && consegna.dati.esito) })) sessioniConsegnate.add(1);
  pensa(5, 20); // lettura dei risultati
}

// --- I due tipi di utente ----------------------------------------------------------

/** Visitatore senza login: home, lista dei bandi di un paio di comparti, una pagina informativa. */
export function anonimo() {
  const inizio = Date.now();
  group("visitatore", () => {
    aprePagina("/");
    pensa(3, 10);
    bandi(alcuni(COMPARTI, 2));
    pensa(5, 20);
    // Un'altra pagina dell'app: stesso index.html, i file JS ora sono in cache nel browser.
    check(statico(aCaso(["/prezzi", "/chi-siamo", "/domande-frequenti", "/contatti"]), "pagina (index.html)"), { "pagina 200": (r) => r.status === 200 });
    pensa(5, 15);
  });
  durataVisita.add(Date.now() - inizio, { tipo: "anonimo" });
  pensa(10, 30);
}

/** Iscritto: login (una volta, poi solo quando il token scade), una visita da 2-5 minuti a giro. */
export function iscritto() {
  if (!token || Date.now() > scadeAlle) {
    // Primo giro: l'app come la vede il browser (che rimanda al login), poi Cognito.
    if (!token) aprePagina("/app");
    if (!login()) return;
  }
  const inizio = Date.now();

  group("apertura app", () => {
    const me = api("GET", "/me");
    if (!check(me.res, { "profilo": (r) => r.status === 200 && !!(me.dati && me.dati.userId) })) {
      if (me.res.status === 401) token = null; // token rifiutato: nuovo login al prossimo giro
      return;
    }
    profilo = me.dati;
    if (!profilo.onboarded) onboarding();
    // Dashboard: concorsi seguiti e statistiche.
    api("GET", "/me/concorsi");
    api("GET", "/me/statistiche");
  });
  if (!profilo || !profilo.onboarded) return;
  const medium = profilo.piano === "medium" || profilo.piano === "pro";
  pensa(3, 10);

  // Metà delle visite: ricerca dei bandi, un dettaglio, e a volte lo si segue.
  if (Math.random() < 0.5) {
    group("bandi", () => {
      const lista = bandi(profilo.interessi && profilo.interessi.length ? profilo.interessi : ["altro"]);
      pensa(5, 20);
      if (!lista.length) return;
      const bando = aCaso(lista);
      const dettaglio = api("GET", `/concorsi/${encodeURIComponent(bando.id)}`, undefined, "/concorsi/{id}");
      check(dettaglio.res, { "dettaglio del bando": (r) => r.status === 200 });
      pensa(10, 30);
      if (Math.random() < 0.3) {
        // Free: un solo concorso seguito, il secondo dà 403 LIMITE_PIANO (risposta prevista).
        const segui = api("PUT", `/me/concorsi/${encodeURIComponent(bando.id)}`, {}, "/me/concorsi/{id}", [403]);
        check(segui.res, { "segui il bando": (r) => r.status === 200 || r.status === 403 });
      }
    });
    pensa(3, 10);
  }

  // Studio: quasi sempre una sessione; i Medium a volte simulazione o banca dati ufficiale.
  group("studio", () => {
    const materie = api("GET", "/materie");
    check(materie.res, { "materie": (r) => r.status === 200 });
    pensa(3, 10);
    const tiro = Math.random();
    if (medium && tiro < 0.25) {
      sessione({ tipo: "simulazione", materie: alcuni(MATERIE, 3), numero: 30 }, 4);
    } else if (medium && tiro < 0.5) {
      const catalogo = api("GET", "/banche-dati");
      const banche = (catalogo.dati && catalogo.dati.banche) || [];
      pensa(3, 10);
      if (banche.length) {
        const banca = aCaso(banche);
        // Consultazione di una pagina di domande, poi una sessione sulle domande nuove.
        api("GET", `/banche-dati/${encodeURIComponent(banca.id)}/domande?da=1`, undefined, "/banche-dati/{id}/domande");
        pensa(10, 30);
        sessione({ tipo: "studio", bancaDatiId: banca.id, numero: 20 }, 3);
      } else {
        sessione({ tipo: "studio", materie: alcuni(MATERIE, 2), numero: 20 }, 3);
      }
    } else if (tiro < 0.9) {
      sessione({ tipo: "studio", materie: alcuni(MATERIE, 1 + Math.floor(Math.random() * 2)), numero: medium ? 20 : 10 }, 3);
    }
  });

  durataVisita.add(Date.now() - inizio, { tipo: "iscritto" });
  // Tra una visita e l'altra l'utente chiude l'app per un po'.
  pensa(15, 60);
}

/** Senza login né utenti di prova niente test: si controlla subito, prima di partire. */
export function setup() {
  const res = http.get(`${BASE_URL}/config.json`, { responseType: "text" });
  if (res.status !== 200) fail(`${BASE_URL}/config.json risponde ${res.status}: l'ambiente è su? È in manutenzione?`);
  if (QUOTA_ANONIMI < 1 && (!CLIENT_ID || !PASSWORD)) fail("mancano CLIENT_ID o PASSWORD: lancia il test con scripts/deploy.sh carico avvia");
  console.log(`Scenario ${SCENARIO}: fino a ${Math.round(VU * Math.max(...TAPPE[SCENARIO].map((t) => t.target)))} utenti contemporanei su ${BASE_URL}`);
}

/** Riepilogo finale: a terminale e, con OUT, in riepilogo.txt e riepilogo.json. */
export function handleSummary(data) {
  const testo = textSummary(data, { indent: " ", enableColors: false });
  const out = { stdout: textSummary(data, { indent: " ", enableColors: true }) };
  if (__ENV.OUT) {
    out[`${__ENV.OUT}/riepilogo.txt`] = testo;
    out[`${__ENV.OUT}/riepilogo.json`] = JSON.stringify(data, null, 2);
  }
  return out;
}
