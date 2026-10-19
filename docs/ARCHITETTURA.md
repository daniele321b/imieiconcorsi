# Architettura di iMieiConcorsi — guida per sviluppatori

Schema ad alto livello di ogni ambiente (account, region, rete, servizi e flussi): [architettura/iMieiConcorsi-HLD.drawio](architettura/iMieiConcorsi-HLD.drawio), pagine Dev, Prod e Shared (si apre con draw.io; si rigenera con `docs/architettura/genera_hld.py`).

Questa guida spiega **come è fatta l'app e come ragiona il codice**: i pezzi, il
percorso di una richiesta, i flussi principali e come aggiungere qualcosa senza
rompere il resto. La mappa file per file è in [MAPPA-CODICE.md](MAPPA-CODICE.md);
i comandi pronti in [COMANDI-RAPIDI.md](COMANDI-RAPIDI.md); il runbook del deploy
in [DEPLOY.md](DEPLOY.md).

Ordine di lettura consigliato per chi arriva: questa pagina → `packages/core/src/domain.ts`
(il modello dei dati) → `packages/core/src/http.ts` (come nasce ogni API) →
`infra/terraform/environments/dev/main.tf` (cosa esiste su AWS e chi può fare cosa).

---

## 1. In una frase

Un sito React servito da CloudFront, che chiama un'API (API Gateway + una Lambda
per servizio) protetta dal login di Cognito; i dati stanno in DynamoDB, i file in
S3; ogni mattina dei job importano i bandi da inPA e mandano le email. Tutto in
`eu-south-1` (Milano), tutto serverless, tutto descritto in Terraform.

```
Browser ──HTTPS──▶ CloudFront (dev.imieiconcorsi.it)
                     ├── /api/*        ──▶ API Gateway HTTP (token Cognito) ──▶ Lambda di servizio ──▶ DynamoDB
                     ├── /dati/bandi/* ──▶ S3: lista dei bandi in cache (JSON gzip, rifatta ogni mattina)
                     └── tutto il resto ──▶ S3: sito React + config.json
Browser ──HTTPS──▶ Cognito (email e password, Google, Facebook)

EventBridge Scheduler (ora italiana)
  06:00 inpa-scraper   bandi da inPA → tabella concorsi → lista in cache; email all'admin
  06:15 scadenze       piani scaduti → Free; promemoria 3 giorni prima
  07:00 avvisi         email con i bandi nuovi a chi li ha chiesti
  dom e mer 03:00 pulizia-bandi  toglie i bandi che inPA non elenca più

S3 contenuti ──▶ import-domande (banca domande statica) · estrai-banca-dati (PDF ufficiali)
Lambda ai ──▶ Amazon Bedrock (Claude Sonnet 4.6, profilo EU)
Lambda billing ◀──▶ Stripe Checkout (pagamenti) · SES (email) · CloudWatch + SNS (allarmi)
```

## 2. Le tre cartelle del codice

| Cartella | Cosa contiene | Gira dove |
|---|---|---|
| `packages/core` | Modello dei dati e regole condivise (piani, limiti, filtri, sconti, ordine delle risposte, progressi) e i "mattoni" AWS comuni (DynamoDB, Cognito, email, `service()`) | Nelle Lambda; i file senza AWS anche nel browser |
| `packages/functions` | Il backend: una cartella per servizio API, i job, l'estrazione delle banche dati, il trigger di Cognito. Test in `test/` | AWS Lambda (Node.js 22, arm64) |
| `packages/web` | Il sito React (Vite + Tailwind + React Router + Amplify per il login) | Browser |
| `infra/terraform` | Tutta l'infrastruttura: moduli riutilizzabili e gli ambienti `dev` e `prod` che li collegano (prod = copia di dev con WAF, protezioni e dominio radice) | `terraform apply` da `scripts/deploy.sh infra` (`ENVIRONMENT=prod` per prod) |
| `scripts/deploy.sh` | Un comando per ogni operazione (build, infra, job, log, prove) | Terminale |
| `data/domande`, `contenuti/` | Banca domande statica (un JSON per materia) e le sue fonti | Caricati da Terraform su S3 |

`core` è importato come `@imieiconcorsi/core/<file>` sia dal backend sia dal sito:
**un tipo o una regola cambiata lì vale ovunque**, e TypeScript segnala dove adeguare.
Per questo `domain.ts` non deve importare nulla di AWS (finisce nel bundle del browser).

## 3. Il percorso di una richiesta

Esempio: l'utente segue un concorso (`PUT /me/concorsi/123`).

1. **Sito** — `useSegui()` in `pages/app/Concorsi.tsx` chiama `api("/me/concorsi/123", { method: "PUT" })`
   (`lib/api.ts`), che aggiunge il token di Cognito preso da Amplify.
2. **CloudFront** — l'indirizzo inizia con `/api`: una CloudFront Function toglie il
   prefisso e passa la richiesta all'API Gateway (stesso dominio del sito: niente CORS).
3. **API Gateway** — l'authorizer JWT controlla il token; la route `PUT /me/concorsi/{id}`
   è collegata alla Lambda `imieiconcorsi-dev-concorsi` (vedi `services` in `environments/dev/main.tf`).
4. **Lambda** — `service({...})` (`core/src/http.ts`) trova la funzione con la chiave
   `"PUT /me/concorsi/{id}"`, costruisce il contesto `ctx`:
   - `userId` = `sub` di Cognito, l'unico identificativo usato nelle tabelle;
   - `piano` e `admin` dai **gruppi Cognito** nel token (nessuna lettura dal database);
   - `limiti` = `PIANI[piano].limiti` da `domain.ts`;
   - `params`, `query`, `body(schemaZod)`.
5. **Logica** — la route controlla il limite del piano e scrive in DynamoDB (`follows`).
   Un `HttpError(403, "…", "LIMITE_PIANO")` diventa `{ error, code }` con stato 403.
6. **Sito** — `ApiError` con `code === "LIMITE_PIANO"` mostra l'`UpgradeBanner` invece di un errore rosso.

Codici di errore usati dal sito per reagire: `LIMITE_PIANO` (invito al piano superiore),
`GETTONI_FINITI`, `TROPPO_VELOCE`, `AI_IN_PAUSA`, `AI_NON_DISPONIBILE` (tutor AI),
`NESSUNA_DOMANDA`, `CODICE_NON_VALIDO`, `SOLO_ADMIN`.

## 4. Identità, piani e privacy

- **Cognito** tiene email, nome, password, collegamenti Google/Facebook e i **gruppi**
  `medium`, `pro`, `admin`. Il piano di un utente *è* il suo gruppo (nessun gruppo = Free).
- **DynamoDB** conosce l'utente solo per il `sub` (anonimo). Niente email o nomi nelle tabelle,
  tranne lo `username` Cognito dove serve per scrivere all'utente (richieste, inviti).
- Sul profilo (`users`) stanno solo scadenza e durata del piano. Cambiare piano = cambiare
  gruppo (`core/src/piani.ts → assegnaPiano`), lo fanno solo billing, admin e il job scadenze.
- Il token si rinnova ogni ora: dopo un cambio di piano il sito chiama
  `ricarica({ rinnovaToken: true })` per vederlo subito.
- **Una persona = un account**: il trigger `auth/pre-signup.ts` collega un login social
  all'account email/password già esistente con la stessa email, e accetta registrazioni
  solo da provider di posta diffusi (`core/src/registrazione.ts`).
- Eliminare l'account (`DELETE /me`) cancella profilo, seguiti, sessioni, richieste,
  progressi e l'utente Cognito; gli ordini restano 10 anni (obbligo contabile), anonimi.

## 5. I dati (DynamoDB)

Tutte le tabelle sono *on demand* (si paga per richiesta) e si chiamano `imieiconcorsi-dev-<nome>`.
Nel codice si usano con `tables.<nome>` (`core/src/db.ts`), che legge il nome dalla
variabile d'ambiente passata da Terraform.

| Tabella | Chiave | Indici | Cosa contiene | Chi scrive |
|---|---|---|---|---|
| `users` | `userId` | — | Profilo di studio, piano (scadenza), contatori (gettoni AI, utilizzi banche dati, avvisi), feedback, inviti | profile, study, billing, ai, admin, pubblico, job |
| `concorsi` | `id` | `byComparto` (comparto + scadenza) | Bandi importati da inPA | inpa-scraper, pulizia-bandi, admin |
| `follows` | `userId` + `concorsoId` | — | Concorsi seguiti e storico (`rimossoIl`) | concorsi, billing (ritorno al Free), admin, job scadenze |
| `questions` | `materia` + `id` | — | Domande: banca statica (`materia` = es. `logica`) e banche dati ufficiali (`materia` = `bd#<id>`, `id` = `n00042`) | import-domande, admin (pubblica) |
| `attempts` | `userId` + `id` (ordinabile per data) | — | Sessioni di studio e simulazioni, con risposte ed esito | study |
| `codici` | `codice` | — | Codici sconto e codici "invita un amico" (`tipo: "invito"`) | admin, billing |
| `ordini` | `id` | `perUtente` (userId + creatoIl) | Un acquisto ciascuno (stato, importo, consenso, sessione Stripe); l'indice dà lo storico pagamenti dell'utente | billing |
| `banche-dati` | `id` | — | Banche dati caricate: stato dell'estrazione, conteggi, esempi, sezioni | admin, estrai-banca-dati |
| `richieste` | `userId` + `id` | `perStato` (stato + aggiornataIl) | Richieste di assistenza con i messaggi | richieste, admin |
| `progressi` | `userId` + `bancaId` | — | Domande fatte, sbagliate e preferite per banca dati (mappe di bit) | study |
| `contatori` | `id` | — | Contatori della piattaforma, es. `ai#2026-10` = token e spesa AI del mese | ai |
| `attivita` | `periodo` + `userId` | — (TTL: minuti 2 giorni, giorni 400) | Utenti attivi: "m#minuto" e "g#giorno" con l'impronta anonima dell'utente | tutte le Lambda dell'API (`core/attivita.ts`), letta da admin |
| `accessi` | `userId` + `il` | — (TTL 12 mesi) | Un login per riga: data e modo (email o social) | trigger Cognito `auth/accesso.ts` |

Gli id "ordinabili" (`core/src/ids.ts`) iniziano con il timestamp: le righe di un utente
escono già in ordine di data con una semplice Query.

Su S3: bucket del **sito** (file di `packages/web/dist`, `config.json`, lista bandi in
`dati/bandi/`) e bucket dei **contenuti** (`domande/<materia>.json`, `banche-dati/<id>.pdf|json`).

## 6. I servizi API

Ogni servizio è una Lambda (`packages/functions/src/<servizio>/handler.ts`) con le sue route
e i suoi permessi (`services` in `environments/dev/main.tf`). **Le route devono essere uguali
nei due posti**: nel codice (chiavi della mappa passata a `service()`) e in Terraform.

| Servizio | Route principali | Cosa fa |
|---|---|---|
| `profile` | `GET /me`, `PUT /me/profilo`, `PUT /me/feedback`, `DELETE /me` | Profilo (nasce al primo `GET /me`), parere, eliminazione account |
| `concorsi` | `GET /concorsi[/{id}]`, `GET/PUT/DELETE /me/concorsi/{id}`, `GET /me/storico-concorsi` | Bandi e concorsi seguiti |
| `study` | `GET /materie`, `POST /sessioni`, `GET /sessioni/{id}`, `POST /sessioni/{id}/consegna`, `GET /me/statistiche`, `GET /banche-dati`, `GET /banche-dati/{id}/domande`, `DELETE /me/progressi/{bancaId}`, `PUT /me/progressi/{bancaId}/preferite/{numero}` | Studio, simulazioni, banche dati, progressi e preferite, statistiche |
| `billing` | `GET /piani`, `POST /me/abbonamento`, `POST /me/codice-sconto`, `GET /me/ordini[/{id}]`, `POST /me/ordini/{id}/ricevuta`, `GET/POST /me/invito`, pubblica `POST /pubblico/stripe/webhook` | Acquisti con Stripe, codici sconto, inviti |
| `ai` | `GET /ai/stato`, `POST /ai/tutor`, `POST /ai/allenamento` | Tutor e allenamento del piano Pro (Bedrock) |
| `richieste` | `GET/POST /me/richieste`, `POST /me/richieste/{id}/messaggi`, `PUT /me/richieste/{id}/letta` | Assistenza agli utenti |
| _(tutte)_ | Le Lambda dell'API accettano solo richieste con l'intestazione segreta di CloudFront (`daCloudFront` in `core/http.ts`) | Niente accessi diretti all'API Gateway che scavalchino WAF e limiti |
| `pubblico` | pubbliche: `POST /pubblico/disiscrivi`, `GET /pubblico/aperto`, `GET /pubblico/clic`, `POST /pubblico/contatto` | Link delle email (firmati) e modulo Contatti (all'admin via SNS, max 5/ora per IP con `contatori`), senza login |
| `admin` | `/admin/...` (riepilogo, utenti, codici, banche dati e concorsi collegati, ordini, richieste, concorsi) | Pannello di controllo, solo gruppo `admin` |

Le route **pubbliche** non hanno login: si proteggono con una firma (HMAC per i link
delle email, firma di Stripe per il webhook).

## 7. I flussi principali

### Accesso
`AuthCard` (home) → Amplify → Cognito (email/password con codice di verifica, oppure
Google/Facebook sul dominio Cognito → ritorno su `/auth/callback`) → `AuthProvider`
(`lib/auth.tsx`) chiama `GET /me` → se il profilo non è completo, `AppLayout` porta
all'**onboarding** (comparti, livelli, avvisi, Termini).

### Bandi
1. Alle 06:00 `jobs/inpa-scraper.ts` legge da inPA tutti i bandi aperti e i chiusi
   recenti (`jobs/inpa.ts`: comparto e materie dedotti dal testo) e li salva in `concorsi`.
2. `jobs/cache-bandi.ts` scrive un file JSON gzip per comparto in una cartella nuova
   del bucket del sito e infine `indice.json`, che punta alla versione nuova.
3. Il sito (`lib/bandi.ts`) scarica l'indice e i file dei comparti: **la ricerca non
   tocca né l'API né DynamoDB**. Filtri e ordinamenti sono in `core/src/concorsi.ts`.
4. La domenica e il mercoledì `jobs/pulizia-bandi.ts` toglie i bandi che inPA non elenca più (con un freno:
   se dovesse cancellarne più di un quarto, si ferma e avvisa l'admin).

### Studio e simulazioni
1. `POST /sessioni` sceglie le domande (`study/logic.ts → selezionaDomande`: ripartite tra le
   materie, vicine al livello dell'utente) e salva in `attempts` solo le loro chiavi.
2. Il sito le riceve: in **studio** con soluzione e spiegazione; in **simulazione** senza
   (`pubblica()`), con il timer.
3. `POST /sessioni/{id}/consegna` calcola il punteggio **sul server** (`calcolaEsito`:
   +1, −0,25, 0; si passa al 70%) e, se la sessione è su una banca dati, aggiorna i progressi.

### Banche dati ufficiali
1. L'admin crea la banca (`POST /admin/banche-dati`) con i **concorsi da collegare** (anche più
   d'uno, `BancaDati.concorsi`): il pannello propone i bandi aperti simili
   (`core/src/concorsi.ts → concorsiSuggeriti`) e permette la ricerca a mano; si cambiano anche
   dopo (`POST/DELETE /admin/banche-dati/{id}/concorsi`). Il browser carica il PDF su S3 con un
   link firmato.
2. L'arrivo del PDF fa partire `banche-dati/estrai.ts`: testo con `unpdf`, domande con
   `banche-dati/parser.ts` (formati: risposta indicata, segnata, tabella delle soluzioni,
   "sempre la prima"), file `banche-dati/<id>.json`, riepilogo ed esempi sul record, email all'admin.
3. L'admin controlla gli esempi e **pubblica**: le domande vanno in `questions` con
   `materia = bd#<id>`; ogni concorso collegato riceve `bancaDatiId` (un concorso ha una sola banca
   dati) e mostra il link alla consultazione `/app/banche-dati/<id>`, anche come segno "Banca dati"
   nelle liste dei bandi.
4. L'utente sceglie se vedere la risposta giusta **sempre per prima** o **mescolata**
   (`core/src/risposte.ts → dispongiRisposte`: ordine casuale ma fisso per domanda). La scelta
   viaggia con ogni richiesta e vale anche per il punteggio.
5. **Progressi**: alla consegna, `study/handler.ts → salvaProgresso` accende i bit delle
   domande fatte e sbagliate (`core/src/progressi.ts`); la stella salva una domanda tra le
   preferite (terza mappa nella stessa riga, `modificaProgresso` la conserva). Le sessioni
   propongono prima le mai fatte, o solo quelle da ripassare, o le preferite.
6. Piano Free: 3 utilizzi a settimana (`study/usi.ts`).

### Acquisto di un piano
1. `POST /me/abbonamento` controlla con `core/src/acquisti.ts → esitoAcquisto` cosa succede al
   piano in corso (stesso piano: giorni aggiunti; Medium → Pro: giorni convertiti; Pro → Medium:
   rifiutato) e crea un **ordine** `in-attesa` (`billing/ordini.ts`) con il consenso
   alla rinuncia al recesso, e una sessione **Stripe Checkout** (`billing/stripe.ts`, API REST
   senza SDK); il sito porta l'utente alla pagina di Stripe.
2. Pagato, Stripe chiama il **webhook** (`POST /pubblico/stripe/webhook`, firma controllata) →
   `completaOrdine` → di nuovo `esitoAcquisto` sul piano di quel momento → `assegnaPiano` (gruppo
   Cognito + scadenza) → email con la **ricevuta** (rimandabile da `POST /me/ordini/{id}/ricevuta`) →
   eventuale premio a chi ha invitato (`billing/inviti.ts`).
3. Intanto `/app/pagamento` interroga `GET /me/ordini/{id}`; se il webhook tarda, il server
   chiede lo stato direttamente a Stripe. Senza chiave Stripe (`BILLING_MODE=mock`) l'ordine si
   completa subito, gratis, per le prove.
4. Alle 06:15 `jobs/scadenze.ts` riporta al Free i piani scaduti (restano seguiti solo
   gli ultimi concorsi consentiti) e manda il promemoria 3 giorni prima.

### Avvisi sui nuovi bandi
Alle 07:00 `jobs/avvisi.ts` scrive a chi ha attivato gli avvisi (ogni giorno o il lunedì)
i bandi nuovi dei suoi comparti. Ogni email ha un'immagine invisibile e link firmati
(`core/src/disiscrizione.ts`) che passano da `pubblico/handler.ts`: così si sa se gli avvisi
vengono letti. Chi non li apre passa al settimanale e poi in pausa (`jobs/avvisi-logic.ts`),
finché non torna nell'app.

### Tutor AI (piano Pro)
`POST /ai/tutor` e `POST /ai/allenamento` (`ai/handler.ts`) chiamano Claude Sonnet 4.6 su
Bedrock (profilo d'inferenza EU). Prima di ogni chiamata, in ordine: tetto di spesa della
piattaforma (tabella `contatori`), ritmo (6 al minuto), gettoni (150 al mese) e tetto di
spesa dell'utente; dopo, si registrano token e spesa stimata. Il tutor risponde solo su
argomenti di studio: per il resto dà il segnale `[FUORI_TEMA]` e il gettone torna indietro.
Prompt e regole pure in `ai/logic.ts`.

### Assistenza
`POST /me/richieste` (pagina Assistenza, o "Segnala un errore" che si apre sotto la domanda senza cambiare pagina) → email
all'admin → l'admin risponde da `/admin/richieste` (`POST /admin/richieste/{userId}/{id}`) →
email all'utente e `daLeggere` sulla richiesta → `GET /me` restituisce `richiesteDaLeggere`
→ pallino rosso sull'icona dell'assistenza.

### Monitoraggio
`modules/monitoraggio`: allarmi CloudWatch (errori e throttling delle Lambda, 5xx e latenza
dell'API, throttling DynamoDB, 5xx di CloudFront, reputazione SES, job che non girano,
budget) → topic SNS `imieiconcorsi-dev-monitoraggio` → email all'admin. Dashboard
`imieiconcorsi-dev` in CloudWatch.

## 8. Come si estende

### Una route nuova in un servizio esistente
1. Aggiungi la funzione nella mappa di `service({...})` del servizio, con un commento.
   Valida il corpo con uno schema zod (`ctx.body(Schema)`); per le pagine admin chiama
   `richiediAdmin(ctx)`.
2. Aggiungi la stessa chiave (`"POST /me/qualcosa"`) a `routes` del servizio in
   `infra/terraform/environments/dev/main.tf` **e** `environments/prod/main.tf`, e i permessi
   sulle tabelle se servono. Ogni modifica a dev va riportata in prod (i due file sono uguali
   tranne le differenze elencate in testa a quello di prod).
3. Nel sito chiamala con `api()` o `useApi()` e aggiungi il tipo della risposta in `lib/api.ts`.
4. `scripts/deploy.sh build && scripts/deploy.sh infra`.

### Un servizio (Lambda) nuovo
1. `packages/functions/src/<nome>/handler.ts` con `export const handler = service({...})`.
2. In `scripts/deploy.sh`, aggiungi `"<nome>:<nome>/handler.ts"` all'elenco `LAMBDAS`
   (`:aws` in fondo se deve includere l'SDK AWS nel pacchetto, come `ai`).
3. In `environments/dev/main.tf` e `environments/prod/main.tf`, una voce in `services` con
   `routes`, `write_tables`, `read_tables` e, se serve, `environment` e `policies`.

### Una tabella nuova
1. `infra/terraform/modules/data/main.tf` (risorsa) e `outputs.tf` (`table_arns`, `table_env`,
   `table_names`: il monitoraggio la prende da qui da solo).
2. `packages/core/src/db.ts`: un getter in `tables` con la variabile d'ambiente.
3. Permessi ai servizi che la usano. Se contiene dati di un utente, cancellali in `DELETE /me`
   (`profile/handler.ts`) e citali nell'Informativa (`pages/legale/Privacy.tsx`).

### Un job nuovo
1. `packages/functions/src/jobs/<nome>.ts` con `export const handler`; la logica pura in un
   `<nome>-logic.ts` a parte, così si prova con i test.
2. `LAMBDAS` in `scripts/deploy.sh` e la lista dei job di `cmd_job`.
3. Voce in `jobs` di `environments/dev/main.tf` e `prod/main.tf` (orario `cron(...)` in ora italiana) e in
   `job_heartbeat` del modulo `monitoraggio` (giorni senza esecuzioni prima dell'allarme, 1-7:
   l'intervallo tra due esecuzioni più un giorno, quindi 2 per un job di ogni giorno).

### Una pagina nuova
1. `packages/web/src/pages/app/<Nome>.tsx` con un commento in testa.
2. La route in `packages/web/src/main.tsx` (sotto `/app` o `/admin`), e se serve la voce in
   `NAV` di `AppLayout.tsx`.

### Prezzi, limiti, gettoni
Tutto in `packages/core/src/domain.ts`: `LISTINO`, `PIANI` (limiti per piano),
`USI_BANCHE_DATI_FREE`, `COSTI_AI`, `GETTONI_AI_PRO`, `AI_AL_MINUTO`, `PREZZI_AI_USD`. I tetti
di spesa AI si cambiano da `terraform.tfvars` (`ai_tetto_utente_usd`, `ai_tetto_mensile_usd`).
Se cambiano le condizioni per l'utente, aggiorna Termini/Privacy e `VERSIONE_TERMINI`.

## 9. Regole del codice

- **Italiano** per nomi, commenti, messaggi e interfaccia. Ogni file ha un commento in testa
  che dice a cosa serve; ogni funzione esportata ha una riga che dice cosa fa.
- **Logica pura separata da AWS** (`logic.ts`, `*-logic.ts`, gran parte di `core`): si prova con
  `vitest` in `packages/functions/test/` senza toccare AWS.
- **Variabili d'ambiente** solo da Terraform, lette con `env("NOME")` (errore chiaro se manca).
- **Il server decide**: punteggi, limiti del piano, prezzi e sconti si calcolano sempre
  nelle Lambda; il sito mostra e basta.
- **Errori per l'utente** con `HttpError(stato, messaggio, codice)`; tutto il resto diventa 500
  e finisce nei log (mai contenuti personali nei log).
- **Privacy**: niente email o nomi in DynamoDB; tutto sotto il `sub` anonimo.
- **Comandi**: tutto passa da `scripts/deploy.sh` (build, infra, test, job, log). In locale
  `scripts/deploy.sh local` apre il sito collegato all'ambiente dev su AWS.

## 10. Test e controlli

```bash
scripts/deploy.sh test     # controllo dei tipi (core, functions, web) + vitest
```

I test (`packages/functions/test/*.test.ts`) coprono le parti pure: scelta delle domande e
punteggio, parser delle banche dati, ordine delle risposte, progressi, piani e scadenze,
codici sconto e inviti, avvisi, collegamento degli account, Stripe (firma del webhook,
parametri), limiti dell'AI e dell'assistenza, import da inPA.
