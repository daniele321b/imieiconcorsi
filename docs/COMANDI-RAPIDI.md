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
- **prod**: su **https://imieiconcorsi.it**; risorse `imieiconcorsi-prod-…`. Stessi
  comandi di dev con `ENVIRONMENT=prod` davanti: vedi [Produzione](#10-produzione).

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

La banca domande (13 materie, 5.150 domande) la carica l'import dopo `infra`.

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
`packages/core/src/registrazione.ts` e resta interno: il modulo non lo mostra e a chi usa un
altro dominio compare solo un errore generico («Questo indirizzo email non è accettato…»);
con Google o Facebook si entra sempre. Poi: onboarding → Concorsi → Segui → Studio o Simulazione. Il cambio di
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
puoi cambiare piano e scadenza (scadenza vuota = senza scadenza), disattivarlo
oppure **eliminarlo** (con conferma: profilo, sessioni, progressi, concorsi
seguiti, richieste e login spariscono; restano solo gli ordini, senza dati
personali; gli admin non si eliminano da qui). L'utente vede il nuovo piano al suo prossimo accesso, al massimo
entro un'ora, e riceve un'email ("piano attivato" o "tornato al Free").

**Codici sconto.** Nel riquadro "Codici sconto" del pannello: percentuale, piano
(Medium, Pro o entrambi), ultimo giorno valido e usi massimi sono facoltativi;
il codice lo scegli tu (es. `BENVENUTO20`) o lo genera il sistema. L'utente lo
inserisce in **Piani** → "Hai un codice sconto?" e vede subito i prezzi
scontati. Ogni codice vale una volta per utente; con "Disattiva" smette subito
di funzionare (e "Riattiva" lo rimette). Il cestino lo **elimina per sempre**, con
conferma: gli ordini che l'hanno usato restano com'erano e chi l'ha già usato non può
riusarlo neanche se ricrei un codice con lo stesso nome. Usi e importo pagato restano sul
profilo (`ultimoAcquisto`).

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

**Avvisi all'admin** (nuovi bandi con banca dati, richieste di assistenza, ricevute non partite,
spesa AI, scraper fermo): arrivano ad `admin_email` dal topic SNS `imieiconcorsi-dev-avvisi-admin`,
che non ha i limiti della sandbox di SES. **Dopo il primo `infra` arriva l'email "AWS Notification -
Subscription Confirmation": clicca il link**, altrimenti gli avvisi non arrivano (stessa cosa per prod).

**Utenti attivi.** In cima al pannello: quanti sono online ora (hanno usato l'app negli
ultimi 5 minuti), oggi, ieri, negli ultimi 7 e 30 giorni, nel mese in corso e in quello
scorso (persone diverse), più il grafico degli ultimi 30 giorni; si aggiorna da solo ogni
minuto. Conta chi usa davvero l'app (ogni azione con l'accesso fatto, admin esclusi), non chi
ha solo una scheda aperta: ogni Lambda dell'API segna l'utente nella tabella `attivita` al
massimo una volta al minuto, con un'impronta anonima (`core/attivita.ts`). Si conta dal giorno
del primo deploy di questa funzione.

**Provenienza iscritti.** Sotto gli utenti attivi: quanti nuovi iscritti negli ultimi 7 e
30 giorni e in tutto, per fonte, mezzo, campagna e contenuto. Si basa sui link con i parametri
UTM che mettiamo nelle bio e negli annunci, per esempio
`https://imieiconcorsi.it/?utm_source=instagram&utm_medium=social&utm_campaign=bio`
(per un annuncio aggiungi `&utm_content=annuncio-a` per distinguerlo dagli altri). Il sito
ricorda il primo link aperto fino all'iscrizione (massimo 30 giorni) e lo salva nel profilo
quando nasce, una volta sola (`core/provenienza.ts`); chi si iscrive senza link è «diretto».
Nella scheda di ogni utente compare anche «da instagram / bio». Usa solo minuscole, cifre e
trattini nei valori: il resto viene tolto.

**Accessi.** A ogni login (email e password, Google o Facebook) Cognito registra data, ora e modo
nella tabella `accessi` (si cancellano da soli dopo 12 mesi). Nel pannello, per ogni utente:
"Ultimo accesso" e il pulsante **Accessi (n)** con gli ultimi 50.

**Bandi da caricare.** Sulla voce **Admin** del menu compare un numero rosso: i bandi
nuovi della settimana che citano una banca dati da caricare e che non hai ancora visto.
Porta all'elenco, e aprendo l'elenco il numero si azzera (lo ricorda il browser). Il pannello admin mostra quanti bandi aperti citano una
banca dati non ancora caricata (e quanti sono usciti nell'ultima settimana); in
**Banche dati** c'è l'elenco, con "nuovo" sui bandi della settimana e **Carica la
banca dati**, che precompila il modulo con quel concorso. L'email del mattino sui
nuovi bandi con banca dati porta a questo elenco.

**Storico pagamenti.** Pannello admin → **Pagamenti**: tutti gli ordini (pagati,
in attesa, non completati, falliti) con email, piano, importo, sconto e
scadenza, filtri per stato, piano ed email, e i totali incassati (mese e
sempre). Il pulsante con il codice dell'ordine lo copia insieme alla sessione
Stripe, per cercarla nella Dashboard di Stripe. Ogni ordine conserva email e nome di chi ha
pagato: se l'account viene eliminato restano nello storico, con l'etichetta "account eliminato".
La colonna **Ricevuta** dice se l'email è partita o il motivo per cui no (es. SES in sandbox). Ogni utente vede i suoi in
**Profilo → I tuoi pagamenti** (link anche dalla pagina Piani): pagati, e a parte
i tentativi non completati, con **Aiuto** per aprire una richiesta su quell'ordine.

## 4. Email (SES) e job del mattino

Ogni mattina, ora italiana:

| Ora | Job | Cosa fa |
|---|---|---|
| 6:00 | `inpa-scraper` | Importa i bandi aperti da inPA (e i chiusi degli ultimi 7 giorni), rifà la lista in cache (`/dati/bandi/` su CloudFront) e ti scrive se ci sono bandi nuovi che citano una banca dati |
| Domenica e mercoledì 3:00 | `pulizia-bandi` | Rilegge i chiusi degli ultimi 24 mesi e cancella i bandi che inPA non elenca più o chiusi da più di 24 mesi (si ferma e ti scrive se dovrebbe cancellarne più del 25%) |
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
`ses-production` scrive i dati della richiesta sull'account (sito, descrizione) e apre
l'esame. Controlla sempre con `ses-status` che il sito sia `https://imieiconcorsi.it`: fino al
14 ottobre 2026 sull'account c'era ancora la richiesta di Fleet Audit (sito
`dev.fleetaudit.it`, non più raggiungibile), e le richieste di rivalutazione finivano su quella.

Se `richiesta_uscita` è **DENIED** da comando non si può rifare. Apri un caso **nuovo**
(non rispondere a quelli vecchi): console AWS → **Support Center** → **Create case** →
**Account and billing** oppure **Service limit increase** → servizio **SES Sending Limits**,
regione **Europe (Milan)**, tipo di email **Transactional**, sito `https://imieiconcorsi.it`,
e incolla:

> Hello,
>
> We would like to ask for Amazon SES production access in eu-south-1 (Europe - Milan) for the transactional emails of iMieiConcorsi (https://imieiconcorsi.it).
>
> How we send:
> 1. Set up SNS notifications for every bounce, complaint and rejection, delivered by email to the account owner, and enabled suppression of bounced and complaining addresses in our configuration set and at account level.
> 2. Added one-click unsubscribe (RFC 8058 List-Unsubscribe and List-Unsubscribe-Post headers) and a visible unsubscribe link to every recurring email. Recurring emails also slow down and then stop automatically for users who do not open them.
> 3. Authenticated the sending domain imieiconcorsi.it with Easy DKIM, a custom MAIL FROM domain (mail.imieiconcorsi.it, SPF) and DMARC.
> 4. Sent only to verified test addresses while in the sandbox, with no bounces or complaints.
> 5. Published a public page that lists every email we send, how often, and how to stop it: https://imieiconcorsi.it/email
>
> About the service: iMieiConcorsi is a study app for people preparing for Italian public-sector job competitions. Users register on the website with their own email address, confirmed through Amazon Cognito. We never use purchased, imported or scraped address lists, and we send no marketing emails or newsletters.
>
> Emails we send, only to registered users:
> - purchase receipts and plan activation notices;
> - one reminder 3 days before a paid plan expires, and a notice when it ends;
> - replies to support requests the user opened;
> - only for users who opt in from their profile: a daily or weekly digest of newly published public competitions in the sectors they chose. Example subject: "3 nuovi bandi per te"; the body lists the new competitions with deadline and link, explains why the user receives it, and has the unsubscribe link.
>
> Bounces and complaints: suppressed addresses are never retried, and every bounce or complaint reaches us by SNS so we can review it.
>
> Expected volume: under 100 emails per day during the beta, up to about 1,000 per day after launch. A daily quota of 1,000 emails with the default sending rate is enough for us.
>
> Public pages: privacy policy https://imieiconcorsi.it/privacy, terms https://imieiconcorsi.it/termini, contact https://imieiconcorsi.it/contatti, about https://imieiconcorsi.it/chi-siamo, pricing https://imieiconcorsi.it/prezzi.
>
> Thank you.

AWS di solito risponde entro 24-48 ore, per email e nel caso stesso.

Un nuovo tester in sandbox va aggiunto a `sandbox_recipients` in
`infra/terraform/environments/shared/terraform.tfvars`. Poi:
```bash
scripts/deploy.sh shared      # terraform chiede "yes"; il tester riceve l'email di verifica da cliccare
```

## Pagine pubbliche e dati del gestore

Senza account si vedono: home, **Chi siamo**, **Prezzi**, **Domande frequenti**, **Contatti**,
**Le nostre email** (tutte le email che mandiamo e come smettere), **Privacy**, **Cookie**,
**Termini**, **Eliminazione dei dati**. Nel piè di pagina, su due righe: Chi siamo, Prezzi,
Domande frequenti, Contatti; sotto Privacy, Cookie, Termini. Le nostre email ed Eliminazione dei
dati si raggiungono da Privacy e Domande frequenti (indirizzi dati ad AWS e Meta). Servono agli utenti e a chi valuta il servizio (AWS per SES, Stripe, Google e Meta).

- **Gestore**: per ora le pagine non parlano di società, dicono solo "iMieiConcorsi
  (imieiconcorsi.it)". Quando ci sarà, compila `ragioneSociale`, `sede` e `partitaIva` in
  `packages/web/src/lib/legale.ts`: le pagine li mostrano da sole. Servono per legge prima di
  accettare pagamenti veri (Stripe live).
- **Contatti**: il modulo della pagina Contatti funziona senza account e ti arriva per email
  dal topic SNS degli avvisi admin (non serve SES). Rispondi direttamente all'indirizzo che
  trovi nel messaggio. Al massimo 5 messaggi l'ora per indirizzo IP. Se un giorno c'è una
  casella vera (es. `info@imieiconcorsi.it`), mettila in `email` in `legale.ts`.
- **Le nostre email** va tenuta allineata al codice: una email nuova = una voce in più.

## Banca domande (piano Free)

Oggi c'è la **v4**: 13 materie, 5.150 domande in tutto. Ci sono 500 domande per
geografia, italiano, matematica e attualità e cultura generale, 350 per le altre.
Le domande sono scritte da libri di testo e fonti online. Le 150 domande in più di
geografia, italiano e matematica e le 500 di attualità vengono invece dalle banche
dati ministeriali «1° Livello» in `contenuti/libri/`, riportate così come sono.
Le fonti sono elencate in fondo alla pagina Studio, insieme alla versione della banca.

**Domande da una banca dati ministeriale.** Metti il PDF in
`contenuti/libri/<materia>/`, poi:
```bash
python3 scripts/domande/da_banca_ministeriale.py <materia> <file.pdf> <quante> <primo-id> >> contenuti/sorgenti/<materia>.py
```
Lo script prende la risposta A) del PDF come giusta. Sceglie le domande lungo
tutto il file e salta:
- quelle con figure;
- quelle con dati superati, come popolazioni o satelliti;
- i doppioni con le domande già presenti.

Le domande sbagliate nel PDF si escludono per numero in `ESCLUDI`, dentro lo
script. Rileggi sempre il blocco aggiunto prima di generare.

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
   **PDF con la sola risposta esatta** (tabella "numero | domanda | risposta", es.
   Carabinieri: "In questo file trovi solo la domanda con la relativa risposta esatta"):
   formato **Solo risposta esatta** (anche "Automatico" lo riconosce). Le colonne si leggono
   dalla posizione nella pagina, "Materia : …" diventa la sezione. Le altre 3 alternative
   si **ricavano** da risposte di domande dello stesso tipo nello stesso file (negli esempi
   sono segnate "ricavata"): vero/falso → l'opposto; numeri e lettere → valori vicini;
   relazioni "A<B" → calcolate in modo che non siano anch'esse vere; coppie (X/Y, "a / b")
   → incrociate, mai una coppia vera del file. **Scartate**: le domande al negativo ("Non ha
   nulla a che fare con…", "Non attinente…": un'alternativa presa a caso sarebbe giusta
   anche lei) e quelle che citano parole che il file non riporta. Agli utenti la
   spiegazione dice che le alternative sono ricavate.
   **PDF a tabella con esatta ed errate in colonna** (es. Polizia penitenziaria, Ministero
   della Giustizia: "Id | Livello | Quesito | Risp_esatta | Risp_errata_1-3"): formato
   **Tabella esatta ed errate** (anche "Automatico" lo riconosce e lo preferisce alla
   "Solo risposta esatta"). Le colonne vengono dall'intestazione ripetuta in ogni pagina,
   anche con le pagine in orizzontale. Il titolo "… BANCA DATI ARITMETICA" diventa la
   sezione e le copertine delle materie si saltano. Gli esponenti tornano a posto
   (4a², 10⁻⁶). I pedici scritti come testo normale nel PDF restano come sono ("x2=-2").
   Scartate solo le righe con due risposte uguali nel PDF.
   **PDF a tabella con la lettera della giusta** (es. Guardia di Finanza, "Materiale
   testologico": "TSUYB00000076 | domanda | a) | b) | c) | d) | b", senza riga di
   intestazione): formato **Tabella con lettera giusta** (anche "Automatico" lo riconosce).
   Le colonne vengono dalle risposte "a)", "b)"… che stanno sempre alla stessa x. Il numero
   della domanda è la parte numerica del codice e il titolo in cima alle pagine si salta.
   Le divisioni in sillabe ("Au- to- re") e i trattini restano come nel PDF.
   Attenzione: questi PDF portano scritto "VIETATA LA PUBBLICAZIONE, LA RIPRODUZIONE E LA
   DIVULGAZIONE". Prima di pubblicarli nell'app verifica di poterlo fare.
5. **Pubblica**: la banca dati compare nella sezione **Banche dati** dell'app
   (per comparto, con l'elenco dei concorsi per cui vale) e **in ogni concorso
   collegato**: nella pagina del concorso il riquadro "Banca dati ufficiale" con
   titolo, numero di domande, il link **Consultala domanda per domanda** (la nostra
   consultazione) e lo studio; nella simulazione la scelta "Banca dati ufficiale /
   Materie del bando"; nelle liste dei bandi il segno verde **Banca dati**, che
   porta alla consultazione (compare dal mattino dopo, quando si rifà la lista in
   cache). Collegando un concorso a una banca già pubblicata, tutto questo vale
   subito. **Ritira** la toglie da tutti i concorsi e la lascia ripubblicabile.
6. **Modifica** (riga della banca dati): titolo, comparto, anno, materia e formato della
   risposta giusta si cambiano quando vuoi. Su una banca pubblicata, cambiando titolo o
   materia le domande si ripubblicano da sole; cambiando il formato l'estrazione riparte e la
   banca va ripubblicata. **Sostituisci il PDF** (versione corretta o file sbagliato): solo
   con la banca non pubblicata (prima **Ritira**), perché con un file nuovo le domande cambiano
   numero; le domande estratte prima si cancellano e l'estrazione riparte. I concorsi collegati
   si cambiano dal pulsante **Concorsi**.
7. **Elimina** (riga della banca dati, con conferma): la toglie per sempre, con
   PDF, domande estratte e domande pubblicate; i concorsi collegati tornano alle
   nostre domande. Le sessioni già fatte restano nelle statistiche. Il PDF resta
   recuperabile per 30 giorni come versione vecchia nel bucket, poi sparisce.

**Menu.** Da 1024 px in su il menu è in alto; su telefono e tablet (anche iPad) c'è la barra
in basso con Dashboard, Concorsi, Tutor AI al centro, Studio e Piani (Admin per l'admin). Le
banche dati si aprono dal riquadro in cima alla pagina **Studio**. Il profilo è il cerchio in alto.

**Ordinamenti della ricerca.** Scadenza più vicina / più lontana, usciti di recente / da più
tempo, più / meno posti, nome del concorso dalla A alla Z / dalla Z alla A.

**"Con banca dati".** Il filtro "Solo bandi con banca dati" tiene i bandi che hanno già una banca
dati caricata, più quelli il cui testo su inPA (titolo, descrizione breve o completa) ha una frase
che nomina una "banca dati" **delle domande della prova** (quesiti, domande, prova, preselettiva,
test, quiz) **senza negarla** ("non è prevista", "nessuna", "senza"…) e che non parla di altre banche
dati (contratti pubblici, INPS, del personale, giuridiche…): `fraseBancaDati` in
`packages/functions/src/jobs/inpa.ts`. Nella pagina del bando si vede la frase da cui lo
deduciamo. Si ricalcola a ogni import (gli aperti ogni mattina).

**Tipi di bando.** Filtri → **Tipo di bando**: Concorsi, Tempo determinato, Mobilità, Incarichi e
collaborazioni, Tirocini e borse, Interni e progressioni (riconosciuti dal titolo,
`TIPI_BANDO` in `packages/core/src/concorsi.ts`); le schede dei tipi diversi da "Concorsi" hanno
un'etichetta. Altre fonti oltre a inPA (Gazzetta Ufficiale, scuola, Forze armate) non sono
ancora importate. Il segno verde "Banca dati" sulle schede c'è solo quando la banca dati è
pubblicata e collegata.

**Nomi dei bandi.** Tutti con la maiuscola iniziale (anche quelli scritti in minuscolo su
inPA: li sistema l'import, e il sito li mostra già così) e con l'anno di pubblicazione, così i
concorsi che si ripetono si distinguono ("Agente di Polizia di Stato 2026" e "… 2025"). Se lo
stesso ente ha due bandi con lo stesso nome nello stesso anno, nella lista si aggiungono la
data e un pezzo del codice inPA; il codice intero è nella pagina del bando.

**Punteggi.** Simulazione: punteggio d'esame (+1 giusta, −0,25 sbagliata, 0 non data) sul
massimo, si passa al 70%. Studio: percentuale delle giuste sulle risposte date, senza penalità
(2 giuste su 10 = 20%). Nello studio **Esci** interrompe: le risposte date restano nei progressi
e nelle statistiche, le domande non fatte non contano.

**Prove d'esame.** La simulazione ha un cronometro in alto: tempo rimasto in grande, tempo
trascorso, barra del tempo e ritmo (quante domande sei indietro rispetto al tempo passato);
negli ultimi 5 minuti diventa rosso. Lo studio mostra il tempo trascorso; i risultati il tempo
impiegato. Domande: 30, 50 o 60 (nella banca dati 30 o 60); con **Medium e Pro** si può scrivere un altro
numero, da 5 a 100 (`SIMULAZIONE_MAX` in `domain.ts`, controllato anche dal server).

**Banche dati (pagina utente).** Ogni scheda mostra titolo, domande e progressi; toccandola si
aprono le tre scelte **Consulta**, **Studia**, **Simulazione**. Scelto Studia o Simulazione:
quali domande (nuove, da ripassare, preferite, tutte), quante, e il pulsante per iniziare.

**Segnala un errore** (sotto le domande): si apre un riquadro lì sotto, senza cambiare pagina;
dopo l'invio **Torna alla domanda** lo chiude e si riprende dallo stesso punto. La segnalazione
finisce in Assistenza come le altre richieste.

**Bandi con le domande chiuse.** Nella ricerca, accanto alla barra e prima
dell'ordinamento: **Tutti** (predefinito), **Aperti** o **Chiusi**. I chiusi sono i bandi
scaduti da meno di 24 mesi: chi ha già fatto domanda continua a prepararsi.
Quando un concorso è davvero finito, dalla sua pagina (da admin) **Segna come
concluso** e sparisce anche da lì.

**Correggere un bando** (admin). Nella pagina del bando, riquadro "Solo per te (admin): dati
del bando" → **Modifica nome e dati**: nome (il titolo grande; l'anno si aggiunge da solo se
manca), descrizione breve, ente, scadenza, posti, sedi, comparto, materie d'esame, testo "Dal
bando", banca dati prevista. Si salvano solo i campi cambiati, anche a parte
(`modificheAdmin` sul bando): l'import del mattino li **riapplica sopra i dati di inPA**,
quindi non si perdono. I valori di inPA restano salvati (`originaliInpa`): **Torna ai dati di
inPA** annulla tutte le correzioni. Nella pagina del bando si vedono subito; nelle liste e
nella ricerca dal mattino dopo (la lista in cache si rifà ogni mattina).

Lo scraper di ogni mattina prende i chiusi degli ultimi 7 giorni. Lo **storico**
(circa 40.000 bandi chiusi negli ultimi 24 mesi) si importa una volta sola, dopo
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
- scheda della banca dati: barra "fatte / da ripassare / preferite" e la scelta
  **Nuove** (predefinita: prima le mai fatte, finite quelle le altre), **Da
  ripassare** (solo le sbagliate l'ultima volta), **Preferite** o **Tutte**;
  **Ricomincia** azzera fatte e sbagliate (le preferite restano);
- consultazione: su ogni domanda "Già fatta" o "Sbagliata l'ultima volta" e la
  **stella** per salvarla tra le **preferite**; il pulsante "Preferite (n)" fa
  scorrere solo quelle (`/app/banche-dati/<id>?preferite=1`). La stella c'è anche
  in studio e nella revisione dopo la consegna (terza mappa di bit nella stessa riga).

Se rifai l'estrazione di una banca dati (i numeri delle domande possono
cambiare), i progressi su quella banca ripartono da zero.

## Piani, inviti e limiti del Free

- **Prezzi** (`LISTINO` in `packages/core/src/domain.ts`): Medium 9,99 € / 30 giorni, 19,99 € / 90 giorni,
  39,99 € / anno; Pro 14,99 € / 30 giorni, 29,99 € / 90 giorni, 69,99 € / anno. La pagina Piani propone il
  trimestre.
- **Acquisti con un piano attivo** (`packages/core/src/acquisti.ts`, valgono per la pagina Piani e per il
  server): stesso piano = i giorni comprati si **aggiungono** alla scadenza (Pro di un anno + trimestrale =
  +90 giorni); da Medium a Pro = i giorni Medium rimasti diventano giorni Pro in proporzione ai prezzi, più
  quelli comprati; da Pro a Medium mentre il Pro è attivo = non si può ("Non disponibile", con il motivo).
  La scheda di ogni piano spiega cosa succede prima di pagare.
- **Ricevuta** (se non arriva: finché SES è in sandbox parte solo verso gli indirizzi verificati;
  `scripts/deploy.sh ses-status`, `scripts/deploy.sh email-prova indirizzo`, `scripts/deploy.sh logs billing`
  e cerca "Ricevuta dell'acquisto non inviata"; "Rimanda la ricevuta" ora dice il motivo): dopo ogni pagamento parte un'email "Ricevuta del tuo acquisto" (data, ordine, piano, prezzo,
  sconto, totale, scadenza, consenso). L'utente la fa rimandare da **Profilo → I tuoi pagamenti →
  Rimanda la ricevuta** (al massimo una ogni 10 minuti); in modalità live anche Stripe manda la sua.
- **Ritorno al Free** (alla scadenza o dall'admin; con Medium o Pro attivi l'utente non può sceglierlo a mano): resta seguito solo l'ultimo concorso seguito; gli
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
150 crediti AI al mese (nel codice "gettoni"): 1 per risposta del tutor, 3 per un allenamento da 5
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
| Crediti AI per utente | 150 al mese | `GETTONI_AI_PRO`, `COSTI_AI` (domain.ts) |
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

Nell'app: voce **Tutor AI** nel menu (su telefono è il pulsante rotondo al centro della
barra in basso; allenamento sui punti deboli + chat libera) e **Chiedi al tutor AI** sotto ogni domanda corretta, in studio e nella
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

## Sicurezza

Cosa protegge l'app (dev e prod, salvo dove indicato):

- **Accesso**: Cognito con login SRP (la password non viaggia mai), password di almeno 8
  caratteri con maiuscole, minuscole e numeri, nessun indizio su quali email sono registrate,
  niente email temporanee. Ogni API vuole un token valido (authorizer JWT), tranne
  `/pubblico/…`, che usa link firmati o limiti propri. Il pannello admin controlla il gruppo
  `admin` nel token firmato, su ognuna delle sue route.
- **Dati di un utente**: ogni lettura e scrittura usa l'id preso dal token, mai dall'indirizzo
  o dal corpo della richiesta (sessioni, ordini, richieste, progressi).
- **Solo da CloudFront**: CloudFront aggiunge alle chiamate all'API un'intestazione segreta
  (`x-origine-cloudfront`); le Lambda respingono chi chiama l'indirizzo diretto dell'API
  Gateway, che altrimenti scavalcherebbe WAF e limiti (`core/http.ts`, `daCloudFront`).
- **Intestazioni di sicurezza** su sito e API: HTTPS obbligatorio (HSTS 2 anni),
  Content-Security-Policy (solo il codice del nostro sito, più Cognito e il caricamento dei
  PDF; AdSense solo se attivo), niente frame da altri siti, niente sniffing dei tipi, referrer
  ridotto, permessi del browser spenti. Se il sito comincia a usare un servizio esterno nuovo,
  va aggiunto alla CSP in `modules/web`. Il font è servito dal nostro sito (niente Google Fonts).
- **WAF (solo prod)**: regole AWS per gli attacchi comuni (OWASP), input malevoli noti, IP con
  cattiva reputazione; massimo 2.000 richieste in 5 minuti per IP e 100 invii (POST) alle rotte
  senza login. In dev non c'è (costa circa 8-10 $ al mese).
- **Limiti**: API Gateway 1.000 richieste al secondo in tutto (picchi 2.000; variabili
  `richieste_al_secondo` e `picco_richieste` del modulo `api`); tutor AI con crediti, 6 al
  minuto e tetti di spesa; modulo contatti 5 l'ora per IP.
- **Dati**: bucket S3 privati, solo HTTPS, cifrati; tabelle DynamoDB cifrate con backup
  continuo; in prod protezione dalla cancellazione. Ogni Lambda ha un ruolo IAM con le sole
  tabelle che le servono.
- **Cifratura a riposo**: DynamoDB, Cognito, log CloudWatch e variabili delle Lambda (cifrature
  di AWS, sempre attive); bucket S3 sito, contenuti e stato Terraform con SSE-S3 (AES-256);
  topic SNS degli avvisi admin (`alias/aws/sns`) e delle notifiche SES (chiave KMS nostra con
  rotazione annuale, circa 1 $ al mese). Non cifrati solo i topic degli allarmi
  (`…-monitoraggio`), che non contengono dati personali: servirebbe una chiave KMS per regione.
- **Cifratura in transito**: browser → CloudFront solo HTTPS (TLS 1.2+, HSTS); CloudFront →
  API Gateway e → S3 solo HTTPS; caricamento dei PDF su S3 con URL firmato HTTPS; Lambda →
  servizi AWS (DynamoDB, S3, SES, SNS, Bedrock, Cognito) sempre HTTPS con firma IAM; Stripe,
  inPA, Google e Facebook in HTTPS; SES consegna le email solo con TLS (`tls_policy = REQUIRE`).
  Niente VPC: il traffico tra le Lambda e i servizi AWS va agli endpoint AWS cifrato e
  autenticato, non su una rete privata (servirebbero VPC, endpoint e NAT, circa 40-70 $ al mese).
- **Pagamenti**: i dati della carta restano su Stripe; il webhook è accettato solo con la firma
  di Stripe; in prod senza chiavi gli acquisti sono chiusi.
- **Dipendenze**: `npm audit` senza vulnerabilità note (12 ottobre 2026).

Al primo `infra` dopo questa modifica, per qualche minuto (finché CloudFront non ha propagato
l'intestazione segreta) le chiamate all'API possono rispondere "Accesso non consentito": basta
aspettare e ricaricare.

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

## 10. Produzione

`environments/prod` è la copia di dev con: indirizzo **https://imieiconcorsi.it**, WAF
davanti a sito e API, tabelle/utenti/bucket protetti dalla cancellazione, login senza
localhost, email senza "[dev]", Stripe in modalità live. Ogni comando di questa pagina vale
anche per prod mettendo `ENVIRONMENT=prod` davanti; con prod `infra` e `destroy` mostrano
un avviso rosso e chiedono "si" (poi Terraform chiede "yes"). `local` funziona solo su dev.

**Prima volta**
1. Credenziali di prod:
   ```bash
   cp infra/terraform/environments/prod/terraform.tfvars.example infra/terraform/environments/prod/terraform.tfvars
   ```
   Compila `admin_email` e, se usi il login social, gli stessi id/secret di Google e Facebook.
   Le chiavi **live** di Stripe (`sk_live_…` e il segreto di un webhook live su
   `https://imieiconcorsi.it/api/pubblico/stripe/webhook`) servono solo per vendere: **vuote =
   acquisti chiusi** (i piani si vedono ma non si comprano; funzionano i codici sconto al 100% e i
   piani dati dall'admin). In prod non esiste il "mock" di dev, che darebbe i piani gratis.
   Metti `budget_mensile_usd = 0` se il budget c'è già in dev (stesso account).
2. Compila e crea l'ambiente (la build è la stessa di dev):
   ```bash
   scripts/deploy.sh build
   ENVIRONMENT=prod scripts/deploy.sh infra      # scrivi "si", poi "yes" (circa 15 minuti la prima volta: certificato e CloudFront)
   ```
3. Bandi, storico dei chiusi e admin:
   ```bash
   ENVIRONMENT=prod scripts/deploy.sh seed
   ENVIRONMENT=prod scripts/deploy.sh storico-bandi
   ENVIRONMENT=prod scripts/deploy.sh make-admin tua@email.it   # dopo esserti registrato su imieiconcorsi.it
   ENVIRONMENT=prod scripts/deploy.sh urls
   ```
4. Login social: su Google e Facebook aggiungi l'URI "Redirect Google/Facebook" stampato da
   `ENVIRONMENT=prod scripts/deploy.sh urls` (in prod il dominio Cognito è `imieiconcorsi-prod.auth…`).
5. Email: finché SES è in sandbox arrivano solo agli indirizzi verificati. Prima di aprire
   agli utenti serve l'accesso di produzione di SES (vedi [Uscire dalla sandbox SES](#uscire-dalla-sandbox-ses)).
6. Conferma le email di AWS "Subscription Confirmation" di prod: allarmi
   (`imieiconcorsi-prod-monitoraggio`) e avvisi admin (`imieiconcorsi-prod-avvisi-admin`, ci
   arrivano anche i messaggi del modulo Contatti).
7. Le banche dati pubblicate in dev non passano da sole: in prod si ricaricano i PDF da
   Admin → Banche dati.

**Aggiornare la produzione** (dopo aver provato su dev):
```bash
scripts/deploy.sh build
scripts/deploy.sh infra                     # dev
ENVIRONMENT=prod scripts/deploy.sh piano    # prod: solo il piano, riassunto + testo completo in environments/prod/piano.txt
ENVIRONMENT=prod scripts/deploy.sh infra    # prod: "si", poi "yes"
```

Log, job e allarmi di prod: `ENVIRONMENT=prod scripts/deploy.sh logs study`,
`ENVIRONMENT=prod scripts/deploy.sh job inpa-scraper`, `ENVIRONMENT=prod scripts/deploy.sh allarmi`.

Quando cambi `environments/dev/main.tf` (route, tabelle, job, permessi) riporta la stessa
modifica in `environments/prod/main.tf`: i due file sono uguali tranne le differenze elencate
in testa a quello di prod.

## Prova a secco

Qualsiasi comando con `DRY_RUN=1` davanti stampa cosa farebbe senza eseguirlo:
```bash
DRY_RUN=1 scripts/deploy.sh all
```
