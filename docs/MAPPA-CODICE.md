# Mappa del codice — file per file

Cosa fa ogni file del progetto e con chi parla. Per il quadro d'insieme (percorso di una
richiesta, flussi, come aggiungere una route o una tabella) leggi prima
[ARCHITETTURA.md](ARCHITETTURA.md). Ogni file ha anche un commento in testa con le stesse
informazioni, più i dettagli.

Legenda: **→** "usa" o "chiama"; **⇢** "è usato da".

---

## Radice

| File | Cosa contiene |
|---|---|
| `package.json` | Workspace npm (`packages/*`), script `test` e `typecheck`. Le dipendenze le installa `scripts/deploy.sh` se mancano |
| `tsconfig.base.json` | Opzioni TypeScript comuni ai tre pacchetti |
| `README.md` | Presentazione e primi comandi |
| `docs/` | Guide: questa mappa, [ARCHITETTURA.md](ARCHITETTURA.md), [COMANDI-RAPIDI.md](COMANDI-RAPIDI.md), [DEPLOY.md](DEPLOY.md), [LOGIN-SOCIAL.md](LOGIN-SOCIAL.md), [GUIDA-PAGAMENTI.md](GUIDA-PAGAMENTI.md), [GUIDA-GOOGLE-PAYPAL.md](GUIDA-GOOGLE-PAYPAL.md); `brand/` con logo e colori |
| `data/domande/<materia>.json` | Banca domande statica, una materia per file (generata da `scripts/domande/genera.py`) |
| `contenuti/` | Fonti della banca statica: `sorgenti/` (domande scritte in Python), `prove/` (frasi-prova), `fonti.csv`, `libri/` (PDF, fuori da git), `VERSIONE` |
| `dist/functions/` | Lambda compilate da `scripts/deploy.sh build` (non si modifica a mano) |

---

## `packages/core` — modello e regole condivise

Importato come `@imieiconcorsi/core/<file>`. I file **senza AWS** (segnati ◆) finiscono anche
nel sito.

| File | Cosa fa | Usato da |
|---|---|---|
| `domain.ts` ◆ | **Il modello**: comparti, materie, piani con prezzi e limiti (`PIANI`, `LISTINO`), costi e tetti dell'AI, tipi delle richieste di assistenza, `Profilo`/`Utente`, `Concorso`, `BancaDati`, `ProgressoBanca`, `CodiceSconto`/`CodiceInvito`, `Domanda`, `Sessione`, `Regole`/`Esito`, gruppi Cognito | Tutto |
| `http.ts` | `service(routes)`: crea l'handler di un servizio API, legge il token (utente, gruppi → piano e limiti), valida i corpi con zod, trasforma `HttpError` in risposte JSON. `richiediAdmin()` | Tutti i `handler.ts` dei servizi |
| `db.ts` | Client DynamoDB, nomi delle tabelle (`tables.*` dalle variabili d'ambiente), `batchGet` a blocchi da 100, `getProfilo` | Backend |
| `env.ts` | `env("NOME")`: variabile d'ambiente obbligatoria | Backend |
| `ids.ts` | Id ordinabili per data (`sortableId`, `timePrefix`) | study, richieste, billing |
| `attivita.ts` | Utenti attivi: `registraAttivita` (chiamata da `service()` a ogni richiesta con login, una scrittura al minuto per utente), `periodi`, `riepilogoAttivita` | tutte le Lambda dell'API, admin |
| `provenienza.ts` | Provenienza degli iscritti dai link UTM: `provenienzaDa` (pulizia dei parametri), `queryProvenienza`, `riepilogoProvenienza` | profile (`GET /me`), admin (`GET /admin/provenienza`), web |
| `account.ts` | `eliminaAccount`: cancella sessioni, seguiti, richieste, progressi, profilo e utente Cognito (restano gli ordini) | profile (`DELETE /me`), admin (`DELETE /admin/utenti/{username}`) |
| `cognito.ts` | Gruppi (piano, admin), nome, eliminazione dell'utente, elenco degli utenti di un gruppo | billing, admin, profile, job scadenze, piani.ts |
| `email.ts` | `inviaEmail` (SES, testo + HTML facoltativo), `avvisaAdmin` | Backend |
| `email-piani.ts` | Email "piano attivato" e "tornato al Free"; `dataIt` | piani, admin, job scadenze |
| `piani.ts` | `assegnaPiano` (gruppo Cognito + scadenza sul profilo; tornando al Free riduce i seguiti), `scadenzaDa` | billing, admin, job scadenze |
| `seguiti.ts` | Concorsi seguiti e storico (tabella `follows`): `righeSeguiti`, `attivi`, `smettiDiSeguire`, `riduciSeguiti`, `daTogliere` | concorsi, piani |
| `concorsi.ts` ◆ | Ordinamenti e filtri della ricerca dei bandi, campi delle liste, bandi scaduti (24 mesi), nomi dei concorsi (maiuscola, anno, `nomiDistinti`), bandi aperti da suggerire per una banca dati | Sito (ricerca), concorsi, cache-bandi |
| `acquisti.ts` ◆ | `esitoAcquisto`: cosa succede comprando con un piano attivo (giorni aggiunti, Medium → Pro convertito, Pro → Medium rifiutato) | billing (acquisto e pagamento), sito (Piani) |
| `sconti.ts` ◆ | Codici sconto: formato, generazione, prezzo scontato, motivo di rifiuto | billing, admin, sito (Piani) |
| `registrazione.ts` ◆ | Domini email ammessi alla registrazione | Sito (`AuthCard`), trigger pre sign-up |
| `risposte.ts` ◆ | `dispongiRisposte`: giusta sempre per prima o mescolata in modo fisso per domanda | study (sessioni e consultazione) |
| `progressi.ts` ◆ | Mappe di bit delle domande fatte, sbagliate e preferite di una banca dati; scelta "nuove / da ripassare / preferite / tutte" | study, sito, test |
| `disiscrizione.ts` | Firme HMAC dei link delle email (disiscrizione, lettura, clic), destinazioni sicure | avvisi, pubblico, profile |
| `domande.ts` ◆ | Schema zod dei file della banca statica | import-domande, test |

---

## `packages/functions` — il backend

Ogni cartella sotto `src/` con un `handler.ts` è **una Lambda**; l'elenco completo (nome →
file) è `LAMBDAS` in `scripts/deploy.sh`. Route e permessi in `environments/dev/main.tf`.

### Servizi API

| File | Cosa fa |
|---|---|
| `profile/handler.ts` | `GET /me` (crea il profilo al primo accesso, conta le risposte dell'assistenza da leggere, riattiva gli avvisi), `PUT /me/profilo` (onboarding e profilo, accettazione dei Termini), `PUT /me/feedback`, `DELETE /me` (cancella tutti i dati dell'utente e l'account Cognito) |
| `concorsi/handler.ts` | Bandi per comparto (aperti e chiusi), dettaglio (con titolo e domande della banca dati collegata), seguire/smettere (limite del piano), storico dei seguiti |
| `study/handler.ts` | Materie, avvio e consegna delle sessioni (punteggio sul server), statistiche, banche dati: elenco con progressi, consultazione 20 domande per volta, azzeramento dei progressi |
| `study/logic.ts` | Puro: `selezionaDomande` (ripartizione tra materie, vicino al livello), `mescola`, `pubblica` (senza soluzione), `calcolaEsito` |
| `study/usi.ts` | Utilizzi settimanali delle banche dati nel piano Free (3 a settimana) |
| `billing/handler.ts` | Piani, acquisto (ordine + Stripe Checkout, o `mock`), verifica del codice sconto, storico dei pagamenti dell'utente, stato dell'ordine (chiede a Stripe se il webhook tarda), invito di un amico, **webhook di Stripe** |
| `billing/ordini.ts` | Tabella `ordini`: salva, legge, `completaOrdine` (attiva il piano una volta sola con le regole di `acquisti.ts`, ricevuta via email, premio invito), `chiudiOrdine`, `inviaConferma` (la ricevuta) |
| `billing/stripe.ts` | API REST di Stripe senza SDK: crea/legge la sessione di pagamento, firma del webhook |
| `billing/inviti.ts` | "Invita un amico": codice personale, codice di chi ha invitato, premio di 30 giorni al primo acquisto dell'amico (massimo 12 l'anno) |
| `ai/handler.ts` | Tutor e allenamento (Bedrock, Claude Haiku 4.5 EU) con tutte le protezioni: tetto della piattaforma, ritmo, gettoni, tetto per utente, fuori tema |
| `ai/logic.ts` | Puro: istruzioni del tutor (con il guardrail `[FUORI_TEMA]`) e dell'autore di domande, messaggi, controllo delle domande generate, punti deboli, stima della spesa |
| `richieste/handler.ts` | Assistenza lato utente: elenco, nuova richiesta (limiti: 5 aperte, 10 al giorno), messaggi, "letta" |
| `pubblico/handler.ts` | Route senza login, protette da firma: disiscrizione dagli avvisi, immagine "aperto" e link "clic" delle email |
| `admin/handler.ts` | Pannello: riepilogo (utenti, richieste aperte, spesa AI), utenti (piano, scadenza, disattivazione), codici sconto, banche dati (carica, estrai, pubblica, ritira, elimina), concorsi conclusi, storico pagamenti, richieste di assistenza |

### Banche dati ufficiali

| File | Cosa fa |
|---|---|
| `banche-dati/estrai.ts` | Lambda lanciata dall'arrivo di un PDF su S3 (o dal pannello): testo con `unpdf`, domande con il parser, file JSON, riepilogo ed esempi, email all'admin |
| `banche-dati/colonne.ts` | Puro: PDF a tabella "Id \| Livello \| Quesito \| Risp_esatta \| Risp_errata_1-3" (es. Polizia penitenziaria). Colonne dall'intestazione di ogni pagina, esponenti riattaccati, domanda e risposta divise se il PDF le unisce, sezione dal titolo "BANCA DATI …" |
| `banche-dati/lettere.ts` | Puro: PDF a tabella senza intestazione "codice \| domanda \| a)-d) \| lettera giusta" (es. Guardia di Finanza). Colonne dalle risposte "a)", "b)"…, titolo di pagina saltato, trattini delle celle conservati |
| `banche-dati/tabella.ts` | Puro: PDF a tabella con la sola risposta esatta (es. Carabinieri). Colonne dalle posizioni del testo, sezioni "Materia : …", alternative ricavate da domande simili (coppie incrociate, relazioni calcolate, numeri vicini), scarto delle domande al negativo |
| `banche-dati/parser.ts` | Puro: dal testo alle domande. Riconosce risposta indicata, segnata (`*`, `(X)`, `✓`), tabella delle soluzioni, "sempre la prima"; sezioni del PDF; numeri di pagina da scartare |
| `banche-dati/pubblica.ts` | Dal file estratto alle risposte che vedono gli utenti (ordine del PDF o mescolato) |

### Job (EventBridge Scheduler)

| File | Quando | Cosa fa |
|---|---|---|
| `jobs/inpa-scraper.ts` | Ogni giorno 06:00 | Bandi aperti e chiusi recenti da inPA → `concorsi`; email all'admin per i nuovi con banca dati; rifà la cache. Con `{ storico }` importa 24 mesi di chiusi |
| `jobs/inpa.ts` | — | API di inPA, paginazione, comparto e materie dedotti dal testo, `toConcorso` |
| `jobs/cache-bandi.ts` | Dopo ogni import | File JSON gzip per comparto nel bucket del sito (`dati/bandi/<versione>/`) + `indice.json` |
| `jobs/pulizia-bandi.ts` | Domenica e mercoledì 03:00 | Toglie i bandi che inPA non elenca più (si rilancia da sola se il tempo non basta; si ferma oltre il 25%) |
| `jobs/avvisi.ts` | Ogni giorno 07:00 | Email con i bandi nuovi dei comparti scelti (giornaliera o il lunedì), con immagine e link firmati |
| `jobs/avvisi-logic.ts` | — | Puro: quando scrivere, quali bandi, rallentamento per chi non legge |
| `jobs/scadenze.ts` | Ogni giorno 06:15 | Piani scaduti → Free (con email); promemoria 3 giorni prima |
| `jobs/scadenze-logic.ts` | — | Puro: `azionePerAbbonato` |

### Altro

| File | Cosa fa |
|---|---|
| `auth/pre-signup.ts` | Trigger di Cognito prima di ogni registrazione: domini email ammessi, collegamento dei login social all'account esistente |
| `auth/accesso.ts` | Trigger di Cognito "pre token generation": registra ogni login nella tabella `accessi` e l'ultimo accesso sul profilo (non blocca mai il login) |
| `auth/collega-account.ts` | Puro: decisione del trigger (procedi, collega, rifiuta) |
| `contenuti/import-domande.ts` | Lambda lanciata da un JSON in `domande/` su S3: scrive le domande della banca statica e toglie quelle sparite |

### Test (`packages/functions/test`, vitest)

| File | Cosa prova |
|---|---|
| `study.test.ts` | Scelta delle domande, punteggio |
| `banche-dati.test.ts` | Parser (anche su righe vere di un PDF), ordine delle risposte |
| `progressi.test.ts` | Mappe di bit e selezione nuove/da ripassare/tutte |
| `assistenza-limiti-ai.test.ts` | Spesa stimata, soglie di avviso, segnale fuori tema, limiti delle richieste |
| `collegamenti-banche.test.ts` | Bandi aperti suggeriti per una banca dati, lista dei concorsi collegati |
| `acquisti-nomi-preferite.test.ts` | Acquisti con un piano attivo, nomi dei concorsi (maiuscola, anno, doppioni), domande preferite |
| `bandi-chiusi-ai.test.ts` | Filtro aperti/chiusi, storico, gettoni, punti deboli, domande generate, messaggi del tutor |
| `inviti-avvisi-seguiti.test.ts` | Prezzi e durate, utilizzi Free, ritorno al Free, inviti, avvisi a chi legge, pulizia bandi |
| `sconti-ricerca-registrazione.test.ts` | Ordinamenti e filtri, codici sconto, email ammesse, piani |
| `piani.test.ts` | Gruppi → piano, scadenze |
| `stripe.test.ts` | Firma del webhook, parametri, prezzi |
| `avvisi.test.ts` | Quando avvisare, bandi nuovi, feedback, link di disiscrizione |
| `inpa.test.ts` | Comparto, conversione dei bandi, banca dati citata, materie |
| `collega-account.test.ts` | Decisioni del trigger pre sign-up |
| `domande.test.ts` | Validità dei file della banca statica |
| `manutenzione.test.ts` | CloudFront Function di sito e API con la manutenzione: spenta, accesa, link di accesso, anteprima |
| `colonne.test.ts` | Banche dati a tabella "Quesito \| esatta \| errate" (intestazione, esponenti, risposta attaccata alla domanda) |
| `lettere.test.ts` | Banche dati a tabella "codice \| domanda \| a)-d) \| lettera giusta" |

---

## `packages/web` — il sito React

Avvio: `index.html` → `src/main.tsx`. Stili: Tailwind (`src/index.css`, colori `brand` e
`accent`). In locale `scripts/deploy.sh local` (Vite su `localhost:5173`, `/api` e `/dati`
inoltrati all'ambiente dev, vedi `vite.config.ts`).

### Struttura delle pagine

```
main.tsx  (caricaConfig → AuthProvider → router)
├── /                      Landing ── AuthCard
├── /auth/callback         AuthCallback (ritorno da Google/Facebook)
├── /privacy /termini /eliminazione-dati   pagine legali (LegalePagina)
├── /disiscrivi            Disiscrivi (link delle email, senza login)
├── /chi-siamo /prezzi /domande-frequenti /contatti /email /cookie   pagine pubbliche (pages/info)
├── /app                   AppLayout (menu, assistenza, profilo; login e onboarding obbligatori)
│   ├── (indice)           Dashboard
│   ├── onboarding         Onboarding ── ProfiloPickers
│   ├── concorsi           Concorsi ── FiltriConcorsiPanel, ConcorsoCard
│   ├── concorsi/:id       ConcorsoDettaglio ── OrdineRisposte
│   ├── studio             Studio
│   ├── banche-dati        BancheDati ── OrdineRisposte (SchedaBanca con progressi)
│   ├── banche-dati/:id    BancaDatiConsulta ── ChiediAlTutor, SegnalaErrore
│   ├── tutor              Tutor ── TutorChat
│   ├── sessione/:id       Sessione (StudioRunner | SimulazioneRunner | Risultati) ── Pubblicita, ChiediAlTutor, SegnalaErrore
│   ├── piani              Piani
│   ├── pagamento          Pagamento (ritorno da Stripe)
│   ├── profilo            Profilo ── ProfiloPickers, StoricoPagamenti, InvitaAmico, StoricoSeguiti, FeedbackApp
│   └── assistenza         Assistenza ── Richieste (Conversazione, RispondiBox, ContestoBox)
└── /admin                 AppLayout (solo gruppo admin)
    ├── (indice)           Admin (riepilogo, utenti, codici sconto)
    ├── banche-dati        AdminBancheDati
    ├── pagamenti          AdminPagamenti
    └── richieste          AdminRichieste ── Richieste
```

### `src/lib` — servizi del sito

| File | Cosa fa |
|---|---|
| `config.ts` | Legge `/config.json` (scritto da Terraform) e configura Amplify (Cognito, Google, Facebook) |
| `auth.tsx` | `AuthProvider`, `useAuth`, `useUtente`: chi è collegato (da `GET /me`), `ricarica`, `esci`; messaggi d'errore di Cognito in italiano |
| `api.ts` | `api()` (chiamata con il token), `useApi()` (dati con caricamento ed errore), `ApiError`, tipi delle risposte, `toneErroreAi` |
| `bandi.ts` | Lista dei bandi dai file in cache su CloudFront (riserva: l'API) |
| `sessioni.ts` | `useAvviaSessione`: avvia una sessione e apre la sua pagina |
| `statoSessione.ts` | `useStatoSessione`: come useState ma salvato in sessionStorage (filtri dei bandi al ritorno da un bando) |
| `ordineRisposte.ts` | Scelta "giusta per prima / mescolata", salvata nel browser e condivisa tra le pagine |
| `invito.ts` | Codice "invita un amico" dal link `?invito=`, mandato dopo il primo accesso |
| `provenienza.ts` | Parametri UTM del primo link aperto, ricordati fino all'iscrizione e mandati con il primo `GET /me` |
| `format.ts` | Date, euro, durate, scadenze a parole, tipi di procedura |
| `appunti.ts` | Copia negli appunti anche sui telefoni che non hanno `navigator.clipboard` |
| `legale.ts` | Dati del titolare per Privacy e Termini (da completare prima del lancio) |

### `src/components` — pezzi riutilizzati

| File | Cosa fa |
|---|---|
| `ui.tsx` | Mattoni grafici: `Button`, `ButtonLink`, `Card`, `Badge`, `Field`, `Alert`, `Spinner`, `ProgressBar`, `EmptyState`, `PageHeader`, `UpgradeBanner`, `PremiumModal`, `cx` |
| `brand.tsx` | Logo, icone e colori delle materie, icone Google/Facebook |
| `AuthCard.tsx` | Accesso, registrazione con codice, password dimenticata, Google e Facebook |
| `ConcorsoCard.tsx` | Scheda di un bando nelle liste, con Segui |
| `FiltriConcorsiPanel.tsx` | Filtri della ricerca (stato, scadenza, uscita, posti, sede, procedura, banca dati) |
| `ProfiloPickers.tsx` | Comparti, livelli per materia, frequenza degli avvisi |
| `OrdineRisposte.tsx` | Interruttore "mescolata / sempre per prima" delle banche dati |
| `ChiediAlTutor.tsx` | "Chiedi al tutor AI" sotto una domanda (Pro: chat; altri: invito al Pro) |
| `TutorChat.tsx` | Chat con il tutor (testo semplice con elenchi e grassetto, gettoni, avvisi) |
| `Pubblicita.tsx` | Annuncio tra le domande del piano Free (AdSense o annuncio interno) |
| `Richieste.tsx` | Assistenza: `SegnalaErrore` (si apre sotto la domanda), `Conversazione`, `RispondiBox`, `ContestoBox`, stati |
| `UtentiAttivi.tsx` | Admin: online ora, oggi, 7 e 30 giorni, mese, grafico (GET /admin/attivita) |
| `ProvenienzaIscritti.tsx` | Admin: nuovi iscritti per fonte, mezzo, campagna e contenuto (GET /admin/provenienza) |
| `ModificaBando.tsx` | Admin: correzione di nome e dati di un bando, e ritorno ai dati di inPA |
| `NumeroDomande.tsx` | "Altro numero" di domande per le simulazioni (Medium e Pro, fino a 100) |
| `InvitaAmico.tsx` | Codice personale da condividere e codice di chi ti ha invitato |
| `StoricoSeguiti.tsx` | Storico dei concorsi seguiti (menu a tendina nel profilo) |
| `StellaPreferita.tsx` | Stella per salvare una domanda di banca dati tra le preferite (consultazione, studio, revisione) |
| `StoricoPagamenti.tsx` | "I tuoi pagamenti" nel profilo: ordini pagati, tentativi non completati a parte, aiuto sull'ordine |
| `FeedbackApp.tsx` | Voto e commento sull'app (modificabile ogni 15 giorni) |

### `src/pages` — una pagina per file

| File | Pagina |
|---|---|
| `Landing.tsx` | Home pubblica con `AuthCard` |
| `AuthCallback.tsx` | Ritorno dal login social (con un nuovo tentativo automatico al primo collegamento) |
| `Disiscrivi.tsx` | Disiscrizione dagli avvisi con conferma |
| `legale/*.tsx` | Privacy, Termini, Eliminazione dei dati, impaginazione comune (`LegalePagina`) e piè di pagina; `parti.tsx` = titolare e "come contattarci" (dati in `lib/legale.ts`) |
| `info/*.tsx` | Pagine pubbliche: Chi siamo, Prezzi (da `PIANI`), Domande frequenti, Contatti (modulo → `POST /pubblico/contatto`), Le nostre email (elenco di tutte le email: tenerlo allineato), Cookie |
| `app/AppLayout.tsx` | Cornice dell'area riservata: menu (in alto e in basso su telefono), icona assistenza con pallino, profilo |
| `app/Dashboard.tsx` | Concorsi seguiti, statistiche, ultime sessioni |
| `app/Onboarding.tsx` | Primo accesso in tre passi + Termini |
| `app/Concorsi.tsx` | Ricerca dei bandi; esporta `useSegui` |
| `app/ConcorsoDettaglio.tsx` | Dettaglio di un bando: segui, studio e simulazione (materie o banca dati), "concluso" per l'admin |
| `app/Studio.tsx` | Sessioni di studio e simulazioni per materia |
| `app/BancheDati.tsx` | Banche dati per comparto, con progressi e scelta delle domande |
| `app/BancaDatiConsulta.tsx` | Consultazione domanda per domanda (frecce, salto, sezioni, "già fatta") |
| `app/Sessione.tsx` | Studio, simulazione a tempo, risultati e revisione |
| `app/Tutor.tsx` | Tutor AI: allenamento sui punti deboli e chat |
| `app/Piani.tsx` | Prezzi, codice sconto, consenso, acquisto |
| `app/Pagamento.tsx` | Esito del pagamento (attende la conferma di Stripe) |
| `app/Profilo.tsx` | Profilo, pagamenti, inviti, storico dei seguiti, assistenza, parere, eliminazione account |
| `app/Assistenza.tsx` | Richieste dell'utente: nuova (con traccia), conversazioni, risposte |
| `app/Admin.tsx` | Pannello: numeri, link, codici sconto, utenti |
| `app/AdminBancheDati.tsx` | Caricamento ed estrazione delle banche dati; concorsi collegati (suggeriti e ricerca a mano, `SceltaConcorsi`) |
| `app/AdminPagamenti.tsx` | Storico degli ordini con totali |
| `app/AdminRichieste.tsx` | Richieste per stato, risposte |

---

## `infra/terraform` — l'infrastruttura

### Ambienti

| Cartella / file | Cosa fa |
|---|---|
| `bootstrap/main.tf` | Bucket S3 dello stato di Terraform (una volta sola, `scripts/deploy.sh bootstrap`) |
| `environments/shared/` | Risorse comuni a dev e prod: SES (mittente, DKIM, MAIL FROM, DMARC) sulla hosted zone del dominio. `outputs.tf` le passa agli ambienti |
| `environments/dev/main.tf` | **Il cuore**: collega i moduli. Contiene l'elenco dei **servizi API** (route, tabelle, permessi, variabili), dei **job** (orari), i contenuti, il monitoraggio e le variabili comuni (`email_env`, `cognito_env`, `site_env`, …) |
| `environments/dev/variables.tf` | Variabili dell'ambiente (regione, email dell'admin, chiavi Stripe, credenziali social, modello AI, tetti di spesa AI, budget) |
| `environments/dev/terraform.tfvars.example` | Esempio commentato da copiare in `terraform.tfvars` (che non va in git) |
| `environments/dev/outputs.tf` | Indirizzi (sito, API, redirect per Google/Facebook), nomi delle funzioni, `web_config`, topic e dashboard del monitoraggio |
| `environments/prod/` | Copia di dev per la produzione: dominio radice, WAF, `protezione = true`, niente localhost, Stripe live. Le differenze sono elencate in testa al suo `main.tf`; ogni modifica a dev va riportata qui |
| `environments/*/backend.tf` | Dove sta lo stato (bucket S3, lock nativo) |

### Moduli

| Modulo | Risorse | Note |
|---|---|---|
| `lambda/` | Zip del codice, log (14 giorni), ruolo IAM, permessi sulle tabelle, funzione Node 22 arm64 | Usato da `api`, `jobs`, `contenuti` e dal trigger di Cognito |
| `api/` | API Gateway HTTP, stage con limiti di richieste, authorizer JWT di Cognito, una Lambda + integrazione + route per servizio | Le route pubbliche hanno `authorization NONE` |
| `auth/` | User pool Cognito, dominio per il login social, Google e Facebook (se configurati), client del sito, gruppi `medium`, `pro`, `admin` | Trigger pre sign-up collegato da `environments/dev` |
| `data/` | Le 12 tabelle DynamoDB (vedi [ARCHITETTURA.md](ARCHITETTURA.md#5-i-dati-dynamodb)) | `outputs.tf` dà ARN, variabili d'ambiente e nomi |
| `web/` | Bucket del sito, CloudFront (sito + `/api` + `/dati/bandi`), certificato e DNS, file del sito e `config.json`, regola che cancella le versioni vecchie della lista bandi | `functions/spa.js` e `functions/api-prefix.js` sono le CloudFront Function; in cima a entrambe Terraform mette `functions/manutenzione.js` (pagina di manutenzione, interruttore nella KeyValueStore `<nome>-manutenzione`, vedi docs/MANUTENZIONE.md) |
| `contenuti/` | Bucket dei contenuti (versionato), import della banca statica, estrazione delle banche dati, notifiche S3 → Lambda, CORS per il caricamento dei PDF | I file di `data/domande/` si caricano da qui |
| `jobs/` | Una Lambda per job, ruolo dello Scheduler, orari in ora italiana con 2 tentativi | Elenco dei job in `environments/dev/main.tf` |
| `ses/` | Identità del mittente e del dominio, record DNS, configuration set (soppressione di rimbalzi e spam), notifiche SNS | Usato da `environments/shared` |
| `waf/` | Web ACL in us-east-1 per CloudFront: regole gestite AWS (Common, Known bad inputs, IP reputation) e limite di richieste per IP | Solo prod (`waf_attivo`) |
| `monitoraggio/` | Topic SNS (anche in us-east-1), allarmi CloudWatch, budget, dashboard (`dashboard.tf`) | Riceve dall'ambiente le Lambda, le tabelle, i job e le soglie |

---

## `scripts`

| File | Cosa fa |
|---|---|
| `deploy.sh` | Tutti i comandi: `check`, `bootstrap`, `shared`, `build`, `infra`, `seed`, `job`, `storico-bandi`, `ai-prova`, `allarmi`, `allarme-prova`, `make-admin`, `unisci-account`, `genera-domande`, `verifica-domande`, `urls`, `status`, `ses-*`, `email-prova`, `logs`, `local`, `test`, `all`, `destroy`. L'elenco `LAMBDAS` dice quali Lambda compilare. `DRY_RUN=1` stampa i comandi senza eseguirli |
| `domande/genera.py` | Da `contenuti/sorgenti/<materia>.py` a `data/domande/<materia>.json` e alle frasi-prova |
| `domande/verifica.py` | Controlla che ogni domanda abbia la sua frase-prova nel testo della fonte |
| `domande/testi.py` | Testo dei PDF delle fonti (pdftotext) normalizzato |
| `domande/da_banca_ministeriale.py` | Blocchi `D(...)` dalle banche dati ministeriali «1° Livello» (risposta giusta = A), da aggiungere al sorgente |
| `domande/cerca.py` | Cerca frasi nei testi di una materia (per scrivere le frasi-prova) |
| `domande/scarica_wikipedia.py` | Scarica voci di Wikipedia come fonti e le registra in `contenuti/fonti.csv` |
