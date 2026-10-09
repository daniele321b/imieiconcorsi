# Comandi rapidi

Comandi pronti da copiare. Il runbook con le spiegazioni è [DEPLOY.md](DEPLOY.md).

Tutti i comandi si lanciano dalla cartella del repo, dopo:
```bash
cd ~/Documents/projects/concorsi/imieiconcorsi
export AWS_PROFILE=<il-tuo-profilo>
```

Dominio: **imieiconcorsi.it** (comprato su Route 53, la hosted zone esiste già).

Ambienti Terraform:
- **shared**: risorse comuni a dev e prod. Contiene il dominio (record DNS delle
  email) e SES, con mittente `noreply@imieiconcorsi.it`. Si crea una volta e non
  si distrugge con gli ambienti.
- **dev**: su **https://dev.imieiconcorsi.it**; tutte le risorse si chiamano
  `imieiconcorsi-dev-…`.
- **prod** (da creare): su **https://imieiconcorsi.it**.

## 1. Primo deploy

Prerequisiti sul Mac: `aws`, `terraform` (>= 1.10) e `node` (>= 22).

A mano su AWS non si crea niente: basta che la **registrazione del dominio sia
finita**. La console Route 53 → Domini registrati deve mostrare il dominio, non
più "in corso". La hosted zone c'è da subito, ma finché il dominio non risponde
su internet il certificato HTTPS e la verifica delle email non partono. Per
controllare:
```bash
scripts/deploy.sh check       # "dominio attivo" = si può partire; altrimenti riprova più tardi
```
Durante la registrazione controlla anche la posta: per alcuni domini AWS chiede
di confermare l'indirizzo email del titolare con un link.

Configurazione, una volta sola. I file `terraform.tfvars` non vanno su git:
```bash
cp infra/terraform/environments/shared/terraform.tfvars.example infra/terraform/environments/shared/terraform.tfvars
# metti il tuo indirizzo in sandbox_recipients (finché SES è in sandbox riceve solo chi è verificato)
cp infra/terraform/environments/dev/terraform.tfvars.example infra/terraform/environments/dev/terraform.tfvars
# metti admin_email = lo stesso indirizzo (riceve gli avvisi admin)
```

Deploy:
```bash
scripts/deploy.sh bootstrap   # UNA volta sola; terraform chiede "yes"; se il bucket esiste già non fa nulla
scripts/deploy.sh check
scripts/deploy.sh all         # terraform chiede "yes" due volte (shared e dev); 10-15 minuti la prima volta
```
`all` esegue in ordine:
1. controlli
2. `shared` (SES)
3. build di Lambda e sito
4. `terraform apply` di dev
5. import dei bandi da inPA
6. stampa degli indirizzi

La banca domande (oltre 200 domande per ognuna delle 12 materie) la carica l'import dopo `infra`.

**Dopo il primo `all`:**
1. Apri l'email di AWS ("Amazon Web Services – Email Address Verification
   Request") e clicca il link. Va fatto per ogni indirizzo in `sandbox_recipients`.
   Il dominio invece si verifica da solo: Terraform crea i record DKIM nella
   hosted zone, e SES li vede in pochi minuti.
2. Registrati sul sito, poi diventa admin:
   ```bash
   scripts/deploy.sh make-admin tua@email.it
   ```
   Esci e rientra nel sito: compare la voce **Admin**.

Se `all` si ferma con un errore, dopo la correzione rilancia lo stesso
`scripts/deploy.sh all`. Riparte da dove serve: Terraform crea solo quello che
manca, e `bootstrap` non va ripetuto.

## 2. Provare l'app

```bash
scripts/deploy.sh urls        # Sito: https://dev.imieiconcorsi.it
```
Registrati con la tua email: arriva un codice a 6 cifre (controlla anche lo
spam). Con email e password si registrano solo indirizzi dei provider diffusi
(Gmail, Outlook/Hotmail, Yahoo, iCloud, Libero, Virgilio, Alice/TIM…): le
caselle usa e getta vengono rifiutate. L'elenco è in
`packages/core/src/registrazione.ts`; con Google o Facebook si entra sempre. Poi: onboarding → Concorsi → Segui → Studio o Simulazione. Il cambio di
piano in "Piani" è gratuito e immediato (modalità di prova), con scadenza a 30 o
365 giorni.

Nella ricerca dei concorsi il menu **Ordina** mette i bandi per scadenza più
vicina, per data di uscita o per numero di posti (più posti o meno posti). In
Studio la sessione è da 10 domande nel Free; Medium e Pro scelgono 10, 20 o 30
(nel Free le opzioni bloccate aprono un popup sui piani). Nel piano Free compare un
annuncio ogni 5 domande di studio (nei piani a pagamento no); senza AdSense
configurato è un annuncio interno sui piani (vedi punto 8).

Contenuto delle tabelle (bandi, domande, utenti, sessioni):
```bash
scripts/deploy.sh status
```

## 3. Pannello admin

```bash
scripts/deploy.sh make-admin tua@email.it   # una volta; poi esci e rientra nel sito
scripts/deploy.sh urls                      # riga "Pannello admin"
```
Dal pannello vedi tutti gli utenti e quanti sono Medium e Pro. Per ogni utente
puoi cambiare piano e scadenza (scadenza vuota = senza scadenza) e
disattivarlo. L'utente vede il nuovo piano al suo prossimo accesso, al massimo
entro un'ora, e riceve un'email ("piano attivato" o "tornato al Free").

**Codici sconto.** Nel riquadro "Codici sconto" del pannello: percentuale, piano
(Medium, Pro o entrambi), ultimo giorno valido e usi massimi sono facoltativi;
il codice lo scegli tu (es. `BENVENUTO20`) o lo genera il sistema. L'utente lo
inserisce in **Piani** → "Hai un codice sconto?" e vede subito i prezzi
scontati. Ogni codice vale una volta per utente; con "Disattiva" smette subito
di funzionare. Usi e importo pagato restano sul profilo (`ultimoAcquisto`).

**Account doppi** (stessa email con email e password e con Facebook/Google). Dai
nuovi accessi in poi non succede più: il login social viene collegato da solo
all'account esistente. Per unire quelli creati prima:
```bash
scripts/deploy.sh unisci-account tua@email.it   # per ogni account social: scrivi "si"
```
Tiene l'account email e password (con il suo ruolo admin) e cancella il doppione
social, i cui dati di studio si perdono. Al prossimo accesso con Facebook entri
nell'account unito: la prima volta la pagina si ricarica da sola una volta.

**Richieste di assistenza.** Gli utenti registrati scrivono dalla pagina
**Assistenza** (icona salvagente in alto, o Profilo → Assistenza) scegliendo il
tipo: banca dati da aggiungere, domanda o risposta sbagliata, problema di
accesso, problema con un pagamento, piano e scadenza, errore nell'app,
suggerimento, altro. Ogni tipo propone una traccia da completare. Sotto ogni
domanda (studio, revisione, consultazione della banca dati) c'è **Segnala un
errore**, che apre una richiesta con la domanda già allegata; dalla pagina di
ritorno del pagamento, **Problemi con il pagamento?** allega il codice
dell'ordine. Ti arriva un'email per ogni richiesta e ogni messaggio nuovo.
Rispondi da Pannello admin → **Richieste**: l'utente riceve un'email e vede un
pallino rosso sull'icona dell'assistenza. Rispondendo, una richiesta aperta passa
"in lavorazione"; scegli "chiusa" quando è risolta (se l'utente riscrive, si
riapre). Limiti contro gli abusi: 5 richieste non chiuse insieme e 10 nuove al
giorno per utente.

**Storico pagamenti.** Pannello admin → **Pagamenti**: tutti gli ordini (pagati,
in attesa, non completati, falliti) con email, piano, importo, sconto e
scadenza, filtri per stato, piano ed email, e i totali incassati (mese e
sempre). Il pulsante con il codice dell'ordine lo copia insieme alla sessione
Stripe, per cercarla nella Dashboard di Stripe. Ogni utente vede i suoi in
**Profilo → I tuoi pagamenti** (link anche dalla pagina Piani): pagati, e a parte
i tentativi non completati, con **Aiuto** per aprire una richiesta su quell'ordine.

## 4. Email (SES) e job del mattino

Ogni mattina, ora italiana:

| Ora | Job | Cosa fa |
|---|---|---|
| 6:00 | `inpa-scraper` | Importa i bandi aperti da inPA (e i chiusi degli ultimi 7 giorni), rifà la lista in cache (`/dati/bandi/` su CloudFront) e ti scrive se ci sono bandi nuovi che citano una banca dati |
| Domenica e mercoledì 3:00 | `pulizia-bandi` | Rilegge i chiusi degli ultimi 18 mesi e cancella i bandi che inPA non elenca più (si ferma e ti scrive se dovrebbe cancellarne più del 25%) |
| 6:15 | `scadenze` | Riporta a Free chi ha il piano scaduto (con email "tornato al Free"); manda il promemoria 3 giorni prima della scadenza |
| 7:00 | `avvisi` | Email con i bandi usciti su inPA ieri nei comparti scelti nel profilo (il lunedì: ultimi 7 giorni, per chi ha scelto "ogni settimana"). Solo a chi li legge: dopo 7 avvisi non aperti si passa al lunedì, dopo altri 4 si sospendono; ripartono quando la persona apre un'email, clicca un link o entra nell'app |

Email sul piano: conferma d'acquisto (con l'eventuale sconto) quando si passa a
un piano a pagamento; "tornato al Free" alla scadenza, quando l'utente sceglie
Free o quando l'admin lo riporta a Free; "piano attivato" quando l'admin dà un
piano a pagamento.

Per lanciarli subito:
```bash
scripts/deploy.sh job inpa-scraper
scripts/deploy.sh job avvisi        # una sola email al giorno per utente, anche se lo rilanci
scripts/deploy.sh job scadenze
scripts/deploy.sh job pulizia-bandi # parte in background (~30 minuti): avanzamento con scripts/deploy.sh logs pulizia-bandi
```

**Se le email non arrivano**, prima di tutto:
```bash
scripts/deploy.sh email-prova tua@email.it   # dice se il dominio è verificato e se sei in sandbox, poi spedisce
```
Le cause tipiche sono due:
1. **Dominio non verificato.** Fino al 7 ottobre i record DKIM erano sbagliati (mancava
   la region): lancia `scripts/deploy.sh shared` e aspetta che `ses-status` dica
   SUCCESS per `imieiconcorsi.it`.
2. **Sandbox.** Il destinatario deve essere in `sandbox_recipients` e aver cliccato il
   link di verifica di AWS.

SES parte in **sandbox**: scrive solo agli indirizzi verificati, massimo 200 al
giorno. Per controllare:
```bash
scripts/deploy.sh ses-status
```
Per scrivere a tutti gli utenti si chiede ad AWS l'uscita dalla sandbox, una
volta per account. Va fatto dopo il primo `shared`, quando il dominio risulta
verificato:
```bash
scripts/deploy.sh ses-production   # usa https://imieiconcorsi.it; scrivi "si"; AWS risponde in 24-48 ore
```
### Uscire dalla sandbox SES

Prima di chiedere (AWS lo guarda):
1. `scripts/deploy.sh shared` → arriva un'email di AWS "Subscription
   Confirmation": **clicca il link**. Da lì ogni rimbalzo o segnalazione di spam
   ti arriva per email (la manda il topic `imieiconcorsi-ses-notifiche`).
2. `scripts/deploy.sh build && scripts/deploy.sh infra`: le email degli avvisi
   hanno il link "non ricevere più avvisi" e la disiscrizione in un clic.
3. Qualche giorno di invii in sandbox ai tester, senza rimbalzi.

Poi:
```bash
scripts/deploy.sh ses-status       # colonna richiesta_uscita
scripts/deploy.sh ses-production   # se non c'è nessuna richiesta: la invia con il testo già pronto
```
Se `richiesta_uscita` è **DENIED** (il caso di Fleet Audit, stesso account e
stessa regione) da comando non si può rifare: console AWS → **Support Center** →
apri il caso (numero in `caso_supporto`) → **Reply**, e incolla:

> Hello, we would like to ask for a re-evaluation of production access in eu-south-1. Since the previous review we have:
> (1) added SNS notifications for every bounce, complaint and rejection, delivered to the account owner;
> (2) enabled account-level suppression for bounces and complaints;
> (3) added one-click unsubscribe (RFC 8058 List-Unsubscribe and List-Unsubscribe-Post headers) plus an unsubscribe link to every recurring email;
> (4) been sending in the sandbox only to verified testers, with no bounces or complaints.
>
> The account hosts two small Italian web apps. This request is mainly for iMieiConcorsi (https://dev.imieiconcorsi.it), a study app for Italian public-sector job competitions. Recipients are only people who registered on our website with their own address, confirmed through Amazon Cognito; we never use purchased, imported or scraped lists, and we send no marketing campaigns.
>
> Emails we send: purchase confirmations; one reminder 3 days before a paid plan expires; a notice when a plan ends; and, only for users who opt in from their profile, a daily or weekly digest of newly published public competitions in the sectors they chose. Each digest says why the user receives it and has a one-click unsubscribe link.
>
> Example digest — subject: "3 nuovi bandi per te"; body: the list of new competitions with deadline and link, the reason for receiving it, and the unsubscribe link.
>
> Expected volume during the beta: under 100 emails per day. The sending domain imieiconcorsi.it is verified with DKIM, with a custom MAIL FROM domain (SPF) and DMARC. Privacy policy: https://dev.imieiconcorsi.it/privacy
>
> Thank you.

AWS di solito risponde entro 24-48 ore, per email e nel caso stesso.

Un nuovo tester in sandbox va aggiunto a `sandbox_recipients` in
`infra/terraform/environments/shared/terraform.tfvars`. Poi:
```bash
scripts/deploy.sh shared      # terraform chiede "yes"; il tester riceve l'email di verifica da cliccare
```

## Banca domande (piano Free)

Oggi c'è la **v1**: almeno 200 domande per ognuna delle 12 materie (2.407 in
tutto), scritte da libri di testo e fonti online. Le fonti sono elencate in fondo
alla pagina Studio, insieme alla versione della banca.

**Nuova versione (v2, v3…).** Le domande restano in `contenuti/sorgenti/` (si
correggono, si aggiungono, si tolgono); la versione si cambia in un punto solo:
```bash
echo v2 > contenuti/VERSIONE
scripts/deploy.sh genera-domande      # ogni domanda prende la versione v2
scripts/deploy.sh verifica-domande
scripts/deploy.sh test
scripts/deploy.sh infra               # terraform chiede "yes": l'import sostituisce la banca
```
Le sessioni già fatte restano valide: le domande che restano tengono lo stesso id.

Le domande stanno in `data/domande/<materia>.json`, un file per materia. Dopo
averle aggiunte o corrette:
```bash
scripts/deploy.sh test        # controlla schema, id unici e doppioni
scripts/deploy.sh infra       # carica i file cambiati: l'import parte da solo
```
Per reimportare tutto a mano: `scripts/deploy.sh job import-domande`. Il file è
la fonte di verità: una domanda tolta dal file sparisce anche dal sito.

Le domande si scrivono in `contenuti/sorgenti/<materia>.py`. Ognuna ha la sua
fonte e la frase del PDF che conferma la risposta giusta. Dopo una modifica:
```bash
scripts/deploy.sh genera-domande              # sorgenti -> data/domande (o: genera-domande storia)
scripts/deploy.sh verifica-domande            # ogni risposta ha la sua frase-prova nel PDF; serve: brew install poppler
scripts/deploy.sh test
scripts/deploy.sh infra                       # terraform chiede "yes"
```
I libri vanno in `contenuti/libri/<materia>/` (non vanno su git) e vanno
registrati in `contenuti/fonti.csv`. Le regole sul diritto d'autore sono in
`contenuti/README.md`.

## Banche dati ufficiali (piani Medium e Pro)

Ogni mattina lo scraper ti scrive quali bandi nuovi citano una banca dati. Quando
l'ente la pubblica:
1. Scarica il PDF dal sito dell'ente.
2. Pannello admin → **Banche dati** → titolo (es. "Banca dati Polizia di Stato
   2026"), comparto e anno, poi i **concorsi a cui collegarla**: mentre scrivi il
   titolo compaiono i **bandi aperti simili** (parole in comune con ente e titolo,
   stesso comparto, anno; "molto simile" = almeno due parole in comune e il bando
   cita una banca dati) da aggiungere con **+** o tutti insieme con "Collega i …
   molto simili"; con **Cerca un altro concorso** trovi qualsiasi bando a mano (anche
   chiuso, togliendo "Solo aperti"). Si può lasciare senza concorsi: resta nella
   sezione Banche dati del suo comparto. Poi materia se è una sola, come è segnata
   la risposta giusta (**Automatico** va bene quasi sempre) → **Carica ed estrai**.

   I concorsi collegati si cambiano anche dopo, dalla riga della banca dati
   (pulsante **Concorsi**): stessi suggeriti e stessa ricerca, × per scollegare. Un
   concorso può avere una sola banca dati: se ne ha già un'altra, prima va
   scollegato da quella.
3. L'estrazione parte da sola; quando finisce arriva un'email e la riga diventa
   "da controllare". **Vedi esempi**: le prime due domande di ogni sezione del
   PDF, **nell'ordine del PDF**: controlla testo, risposte e giusta (in verde)
   confrontandole con il file, e i motivi delle scartate. Le sezioni del PDF
   (es. "Matematica", "Storia") diventano l'argomento delle domande.
   **Ordine delle risposte**: lo sceglie ogni utente entrando nella banca dati (sezione Banche dati,
   pagina del concorso, consultazione): "Mescolata" (predefinito, ordine casuale ma fisso per ogni
   domanda) o "Sempre per prima (A)". La scelta resta salvata nel browser e vale anche per il punteggio
   delle sessioni.
4. Se le giuste sono sbagliate o le scartate sono tante: cambia il formato dal
   menu della riga (l'estrazione riparte) oppure mandami il PDF.
5. **Pubblica**: la banca dati compare nella sezione **Banche dati** dell'app
   (per comparto, con l'elenco dei concorsi per cui vale) e **in ogni concorso
   collegato**: nella pagina del concorso il riquadro "Banca dati ufficiale" con
   titolo, numero di domande, il link **Consultala domanda per domanda** (la nostra
   consultazione) e lo studio; nella simulazione la scelta "Banca dati ufficiale /
   Materie del bando"; nelle liste dei bandi il segno verde **Banca dati**, che
   porta alla consultazione (compare dal mattino dopo, quando si rifà la lista in
   cache). Collegando un concorso a una banca già pubblicata, tutto questo vale
   subito. **Ritira** la toglie da tutti i concorsi e la lascia ripubblicabile.
6. **Elimina** (riga della banca dati, con conferma): la toglie per sempre, con
   PDF, domande estratte e domande pubblicate; i concorsi collegati tornano alle
   nostre domande. Le sessioni già fatte restano nelle statistiche. Il PDF resta
   recuperabile per 30 giorni come versione vecchia nel bucket, poi sparisce.

**Bandi con le domande chiuse.** Nella ricerca, **Filtri → Stato del bando**:
"Aperti" (predefinito), "Aperti e chiusi" o "Solo chiusi". I chiusi sono i bandi
scaduti da meno di 18 mesi: chi ha già fatto domanda continua a prepararsi.
Quando un concorso è davvero finito, dalla sua pagina (da admin) **Segna come
concluso** e sparisce anche da lì.

Lo scraper di ogni mattina prende i chiusi degli ultimi 7 giorni. Lo **storico**
(circa 30.000 bandi chiusi negli ultimi 18 mesi) si importa una volta sola, dopo
il primo `infra` con questa versione:
```bash
scripts/deploy.sh storico-bandi        # ~30 minuti, a blocchi da ~13 minuti
scripts/deploy.sh storico-bandi 250    # se si interrompe: riparte dalla pagina indicata
```

Serve un PDF con il testo selezionabile: se è una scansione l'estrazione lo dice.

**Domande già fatte (progressi).** Per ogni utente e banca dati si salvano le
domande fatte e quelle sbagliate l'ultima volta (tabella `progressi`, due mappe
di bit: 6.000 domande stanno in meno di 1 KB). Si aggiornano alla consegna di
ogni sessione di studio o simulazione sulla banca dati; le domande lasciate in
bianco non contano. Nell'app:
- scheda della banca dati: barra "fatte / da ripassare" e la scelta **Nuove**
  (predefinita: prima le mai fatte, finite quelle le altre), **Da ripassare**
  (solo le sbagliate l'ultima volta) o **Tutte**; **Ricomincia** azzera;
- consultazione: su ogni domanda "Già fatta" o "Sbagliata l'ultima volta".

Se rifai l'estrazione di una banca dati (i numeri delle domande possono
cambiare), i progressi su quella banca ripartono da zero.

## Piani, inviti e limiti del Free

- **Prezzi** (`LISTINO` in `packages/core/src/domain.ts`): Medium 9,99 € / 30 giorni, 19,99 € / 90 giorni,
  39,99 € / anno; Pro 14,99 € / 30 giorni, 29,99 € / 90 giorni, 69,99 € / anno. La pagina Piani propone il
  trimestre.
- **Ritorno al Free** (scadenza, scelta o admin): resta seguito solo l'ultimo concorso seguito; gli
  altri finiscono nello **storico** del profilo (menu "Storico dei concorsi seguiti": nome e giorno).
- **Banche dati per il Free**: 3 utilizzi a settimana (da lunedì). Un utilizzo = una sessione di studio
  o simulazione su una banca dati, oppure la prima consultazione di una banca dati nella settimana.
  Consultazione domanda per domanda: `/app/banche-dati/<id>`.
- **Invita un amico**: ogni utente ha un codice `AMICO-…` e un link `/?invito=…` nel profilo. Se l'amico
  lo usa prima del suo primo acquisto, quando compra un piano chi l'ha invitato riceve 30 giorni gratis
  (Medium se era Free, altrimenti il suo piano si allunga), al massimo 12 volte l'anno. I codici invito
  stanno nella tabella dei codici sconto ma non compaiono nel pannello.

## Tutor AI (piano Pro)

Il tutor usa Claude Haiku 4.5 su Amazon Bedrock, profilo d'inferenza **EU** (i
dati restano in Europa), pagato a consumo sulla bolletta AWS. Ogni utente Pro ha
300 gettoni al mese: 1 per risposta del tutor, 3 per un allenamento da 5
domande. Costo indicativo: ~0,3 centesimi a risposta, ~1,5 centesimi ad
allenamento, quindi al massimo 1-2 € al mese per utente Pro.

**Prima volta (una volta per account AWS):** console AWS → Amazon Bedrock →
Model catalog → **Claude Haiku 4.5** → compila il modulo sul caso d'uso di
Anthropic. Poi:
```bash
scripts/deploy.sh ai-prova    # una chiamata vera al modello: dice se risponde o cosa manca
```
Per cambiare modello (per esempio uno più capace e più caro) metti `ai_model`
in `environments/dev/terraform.tfvars` e lancia `infra`. Gettoni e costi delle
azioni: `GETTONI_AI_PRO` e `COSTI_AI` in `packages/core/src/domain.ts`; se cambi
modello aggiorna anche `PREZZI_AI_USD` (servono a stimare la spesa).

**Limiti contro le spese indesiderate**, dal primo all'ultimo controllo:
| Limite | Valore | Dove si cambia |
|---|---|---|
| Gettoni per utente | 300 al mese | `GETTONI_AI_PRO`, `COSTI_AI` (domain.ts) |
| Spesa per utente | 3 $ al mese (stimata dai token) | `ai_tetto_utente_usd` (terraform.tfvars) |
| Ritmo | 6 richieste al minuto per utente | `AI_AL_MINUTO` (domain.ts) |
| Spesa di tutta la piattaforma | 50 $ al mese: email all'80%, pausa al 100% | `ai_tetto_mensile_usd` (terraform.tfvars) |
| Lunghezza | 800 token a risposta, ultimi 8 messaggi della chat | `MAX_TOKEN_*` (ai/handler.ts), `MAX_MESSAGGI` (ai/logic.ts) |

La spesa del mese e il tetto si vedono nel pannello admin (riquadro "Spesa AI
del mese"); i contatori stanno nella tabella `contatori` (riga `ai#AAAA-MM`).
Raggiunto il tetto della piattaforma, tutor e allenamenti si fermano per tutti
fino al mese dopo, o finché non alzi `ai_tetto_mensile_usd` e lanci `infra`.

**Solo studio (guardrail).** Le istruzioni del tutor gli dicono di rispondere
solo su studio e concorsi (materie d'esame, bandi e prove, metodo di studio).
Per il resto (email, temi, codice per lavoro, ricette, consigli personali,
richieste di ignorare le regole o di mostrare le istruzioni) risponde solo con il
segnale `[FUORI_TEMA]`: il server lo riconosce, mostra all'utente un avviso
gentile e **restituisce il gettone**; i token consumati contano comunque per i
tetti di spesa. Un passo in più, se servisse: un Guardrail di Amazon Bedrock
(argomenti vietati e filtri di contenuto), che costa a parte per ogni testo
controllato.

Nell'app: voce **Tutor AI** nel menu (allenamento sui punti deboli + chat
libera) e **Chiedi al tutor AI** sotto ogni domanda corretta, in studio e nella
revisione dopo la consegna. Free e Medium vedono l'invito al piano Pro.

## 5. Dopo una modifica al codice

```bash
scripts/deploy.sh test        # test + controllo dei tipi
scripts/deploy.sh build       # Lambda + sito
scripts/deploy.sh infra       # terraform chiede "yes": aggiorna solo ciò che è cambiato
```

Solo il frontend, in locale (si collega all'API e al login dell'ambiente dev):
```bash
scripts/deploy.sh local       # http://localhost:5173, Ctrl+C per chiudere
```

## 6. Login con Google e Facebook

Guida passo passo per creare le app su Google e Facebook:
[LOGIN-SOCIAL.md](LOGIN-SOCIAL.md).

1. Indirizzo da registrare come URI di reindirizzamento (in dev è sempre
   `https://imieiconcorsi-dev.auth.eu-south-1.amazoncognito.com/oauth2/idpresponse`):
   ```bash
   scripts/deploy.sh urls     # riga "Redirect Google/Facebook"
   ```
2. Crea il client OAuth su Google e l'app su Meta for Developers seguendo la guida.
3. Credenziali in `infra/terraform/environments/dev/terraform.tfvars`: compila
   `google_client_id`, `google_client_secret`, `facebook_app_id`, `facebook_app_secret`.
   Poi:
   ```bash
   scripts/deploy.sh infra    # terraform chiede "yes"; i pulsanti compaiono da soli
   ```

## 6b. Pagamenti con Stripe

Pagamenti diretti con Stripe Checkout (carta, PayPal, Apple Pay, Google Pay):
guida passo passo in [GUIDA-PAGAMENTI.md](GUIDA-PAGAMENTI.md). Con
`stripe_secret_key` in `terraform.tfvars` si paga con Stripe (in dev: modalità
test, carta `4242 4242 4242 4242`); senza, il cambio di piano è gratuito
("mock"). Prezzi di prova a 0,50 € finché `PREZZI_DI_PROVA = true` in
`packages/core/src/domain.ts`.

## Monitoraggio

Allarmi CloudWatch sulle risorse principali, mandati al topic SNS
`imieiconcorsi-dev-monitoraggio` (CloudFront e budget: `imieiconcorsi-dev-monitoraggio-us-east-1`,
perché quelle metriche stanno in us-east-1). Ogni allarme manda un'email quando scatta e quando
torna normale. L'email è `admin_email` di `terraform.tfvars`: dopo il primo `infra` arrivano due email
"AWS Notification - Subscription Confirmation", una per topic: **clicca il link in entrambe**.

| Risorsa | Allarme |
|---|---|
| Lambda (tutte, una per una) | crash o timeout: 1 per job e trigger, 3 in 5 minuti per le funzioni dell'API |
| Lambda (account) | richieste rifiutate (throttling); concorrenza oltre l'80% del limite dell'account |
| API Gateway | almeno 5 errori 5xx in 5 minuti; latenza p95 oltre 3 secondi per 15 minuti |
| DynamoDB (tutte le tabelle) | letture o scritture rifiutate (throttling) |
| CloudFront | più del 5% di errori 5xx per 10 minuti |
| SES | rimbalzi oltre il 4% o segnalazioni di spam oltre lo 0,08% (AWS interviene al 5% e allo 0,1%) |
| Job | `inpa-scraper`, `avvisi`, `scadenze` fermi da 2 giorni, `pulizia-bandi` da 5 (gira domenica e mercoledì). Appena creato, l'allarme di un job resta acceso finché il job non gira la prima volta: `scripts/deploy.sh job <nome>` lo sblocca subito |
| Spesa | budget mensile **dell'intero account AWS** (`budget_mensile_usd`, 50 $): avviso all'80% speso e al 100% previsto |

Dashboard "imieiconcorsi-dev" in CloudWatch: stato degli allarmi, richieste ed errori dell'API,
latenza, errori e durata delle Lambda, concorrenza, esecuzioni dei job, capacità DynamoDB,
CloudFront, email, token del tutor AI.

```bash
scripts/deploy.sh allarme-prova   # email di prova sul topic: verifica che l'iscrizione sia confermata
scripts/deploy.sh allarmi         # cosa è in allarme adesso
scripts/deploy.sh urls            # tra gli indirizzi anche la dashboard
```

Dopo il primo deploy gli allarmi "job fermo" possono scattare finché i job non girano la prima
volta (il mattino dopo, o subito con `scripts/deploy.sh job …`). Costo indicativo: circa 6 $ al mese
tra allarmi e dashboard.

## 7. Log

```bash
scripts/deploy.sh logs profile        # oppure: concorsi, study, billing, admin, ai, inpa-scraper, scadenze (Ctrl+C per uscire)
```

## 7b. Prove delle funzioni del piano

- **Ritorno al Free alla scadenza:** pannello admin → utente di prova → piano
  Medium con scadenza **ieri** → Salva. Poi `scripts/deploy.sh job scadenze`:
  l'utente torna Free e riceve l'email "tornato al piano Free".
- **Email di cambio piano:** dal pannello admin metti Medium a un utente
  (email "piano attivato"), poi riportalo a Free (email "tornato al Free").
  Dalla pagina Piani: acquisto (email di conferma) e "Torna a Free".
- **Pubblicità:** con un utente Free fai una sessione di Studio: dopo la 5ª
  risposta, "Prossima domanda" mostra l'annuncio. Con Medium non compare.
- **Domini email:** registrati con un indirizzo come `prova@mailinator.com`: il
  modulo lo rifiuta subito. Con Gmail, Outlook, Libero… va avanti.
- **Avvisi sui bandi:** nel profilo scegli "Ogni giorno", poi
  `scripts/deploy.sh job inpa-scraper` e `scripts/deploy.sh job avvisi`. Arriva
  solo se ieri su inPA sono usciti bandi nei tuoi comparti; una volta al giorno
  (per riprovare lo stesso giorno serve aspettare domani).
- **Feedback:** Profilo → "Il tuo parere sull'app". Arriva un'email all'admin
  e il voto compare nella riga dell'utente nel pannello; si può cambiare dopo
  15 giorni.

## 8. Pubblicità del piano Free (facoltativa)

Senza configurazione l'annuncio ogni 5 domande è interno (promuove i piani) e non
usa cookie. Per usare Google AdSense, in
`infra/terraform/environments/dev/terraform.tfvars`:
```hcl
adsense_client = "ca-pub-…"   # ID editore AdSense
adsense_slot   = "…"          # ID dell'unità pubblicitaria
```
Prima di attivarlo serve il banner di consenso ai cookie e l'aggiornamento della
pagina privacy (AdSense usa cookie di profilazione). Poi:
```bash
scripts/deploy.sh infra       # terraform chiede "yes"
```

## 9. Smontare

```bash
scripts/deploy.sh destroy     # solo dev: scrivi "si", poi terraform chiede "yes"
```
Si perdono utenti, profili e sessioni di dev. Restano il bucket dello stato
Terraform e l'ambiente shared (SES con gli indirizzi già verificati). Per
ricreare tutto: `scripts/deploy.sh all`.

Solo se SES non serve più a nessun ambiente:
```bash
scripts/deploy.sh destroy-shared   # scrivi "si", poi "yes"
```

## Prova a secco

Qualsiasi comando con `DRY_RUN=1` davanti stampa cosa farebbe senza eseguirlo:
```bash
DRY_RUN=1 scripts/deploy.sh all
```
