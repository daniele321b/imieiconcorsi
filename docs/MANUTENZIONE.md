# Manutenzione: chiudere il sito quando c'è un problema

Procedura da seguire quando iMieiConcorsi va chiuso a tutti, per esempio per:

- un guasto;
- un errore grave nei dati;
- un problema di sicurezza;
- un intervento sul database.

Con la manutenzione accesa:

- **sito pubblico, area privata e API** rispondono con la pagina "Siamo in manutenzione"
  (stato HTTP 503);
- **chi ha l'app già aperta** viene portato sulla pagina alla prima azione;
- **tu** puoi entrare con un link personale per controllare prima di riaprire.

Si accende e si spegne in **pochi secondi**, senza deploy.

Comandi in breve (su prod con `ENVIRONMENT=prod` davanti):

```bash
ENVIRONMENT=prod scripts/deploy.sh manutenzione on "Torniamo entro le 18:00."   # chiude
ENVIRONMENT=prod scripts/deploy.sh manutenzione stato                           # com'è adesso
ENVIRONMENT=prod scripts/deploy.sh manutenzione off                             # riapre
```

---

## 1. Come funziona

Ogni richiesta a `imieiconcorsi.it` passa da CloudFront, che la fa passare da due piccole
funzioni (CloudFront Functions):

| Funzione | File | Cosa fa |
|---|---|---|
| sito | `infra/terraform/modules/web/functions/spa.js` | Gestisce le pagine e i file del sito |
| API | `infra/terraform/modules/web/functions/api-prefix.js` | Gestisce le chiamate a `/api/…` |

Prima di tutto, entrambe eseguono il controllo della manutenzione, che sta in
`infra/terraform/modules/web/functions/manutenzione.js`. Il controllo legge un interruttore
nella **KeyValueStore** di CloudFront dell'ambiente: `imieiconcorsi-prod-manutenzione`
(oppure `imieiconcorsi-dev-manutenzione`).

| Chiave | Valore | Effetto |
|---|---|---|
| `attiva` | `si` | Manutenzione accesa |
| `attiva` | `no`, oppure chiave assente | Sito normale |
| `messaggio` | Testo libero | Frase in evidenza nella pagina (al massimo 300 caratteri) |
| `accesso` | Codice casuale | Codice del link personale per entrare a sito chiuso |

**Cosa vede chi visita il sito.** Una pagina con:

- il logo;
- la scritta "Siamo in manutenzione";
- il tuo messaggio;
- la frase "I tuoi dati, i progressi e il tuo piano sono al sicuro: non devi fare nulla";
- il pulsante **Riprova**.

La pagina è chiara o scura secondo il telefono, non viene salvata in cache e chiede ai
motori di ricerca di non indicizzarla.

**API e dati.** Le chiamate all'API e i file di dati (lista dei bandi, `config.json`)
ricevono un JSON 503 con `code: "MANUTENZIONE"`. L'app già aperta, quando lo riceve,
ricarica la pagina (`packages/web/src/lib/api.ts`).

**Cosa NON si ferma.** Restano attivi:

- **i job programmati**: scraper inPA, avvisi, scadenze, pulizia bandi;
- **le email** che i job mandano;
- **il login di Cognito**.

Vedi il punto 6 se devi fermare anche quelli.

I **webhook di Stripe** (`/api/pubblico/stripe/webhook`) ricevono 503. Stripe li ripete da
solo per un massimo di 3 giorni, quindi i pagamenti fatti in quel periodo vengono registrati
alla riapertura.

**Un deploy non spegne la manutenzione.** Le chiavi non sono gestite da Terraform, quindi
`scripts/deploy.sh infra` lascia l'interruttore com'è.

---

## 2. Prima volta (una sola volta per ambiente)

La KeyValueStore e le funzioni nuove nascono con il deploy. Prova prima su dev, poi su prod:

```bash
scripts/deploy.sh infra                              # dev
scripts/deploy.sh manutenzione anteprima             # apri il link e guarda la pagina
scripts/deploy.sh manutenzione on "Prova di manutenzione"
# apri il sito da una finestra in incognito: deve comparire la pagina
# apri il link "Per entrare tu" stampato dal comando: devi vedere il sito normale
scripts/deploy.sh manutenzione off

ENVIRONMENT=prod scripts/deploy.sh infra             # prod (quando allinei)
ENVIRONMENT=prod scripts/deploy.sh manutenzione stato
```

Serve `jq` sul Mac. Su macOS recenti c'è già; altrimenti installalo con `brew install jq`.

---

## 3. Chiudere il sito

1. **Accendi la manutenzione** con un messaggio chiaro, che dica cosa succede e quando
   pensi di riaprire:

   ```bash
   ENVIRONMENT=prod scripts/deploy.sh manutenzione on "Stiamo risolvendo un problema tecnico. Torniamo entro le 18:00."
   ```

   Su prod il comando chiede conferma: scrivi `si`.

   Il comando:
   - accende l'interruttore;
   - crea un nuovo codice di accesso;
   - stampa il link **"Per entrare tu"** (`https://imieiconcorsi.it/?accesso=…`);
   - controlla che la home risponda 503, aspettando al massimo un minuto.

2. **Controlla** da una finestra in incognito o dal telefono con i dati mobili: deve
   comparire la pagina di manutenzione.

3. **Avvisa gli utenti**, se serve, sui social. Il sito lo dice già da solo.

Senza messaggio (`manutenzione on`) la pagina dice: "Stiamo aggiornando iMieiConcorsi.
Torniamo il prima possibile."

Per **cambiare il messaggio** a sito già chiuso, ripeti
`manutenzione on "nuovo messaggio"`. Attenzione: il codice di accesso cambia, quindi usa il
link nuovo.

---

## 4. Lavorare a sito chiuso

- **Entrare tu**: apri il link "Per entrare tu" nel browser che usi per controllare.
  Ricevi un cookie valido 12 ore, solo in quel browser, e vedi sito e app come sempre:
  login, pannello admin e API.
- **Rivedere il link**: `ENVIRONMENT=prod scripts/deploy.sh manutenzione stato`.
- Il link vale finché non riaccendi la manutenzione con un nuovo `on`. **Non condividerlo**:
  chi lo ha entra.
- Puoi fare deploy normalmente (`ENVIRONMENT=prod scripts/deploy.sh infra`): la manutenzione
  resta accesa.

---

## 5. Riaprire il sito

1. Con il link di accesso controlla che tutto funzioni: login, Concorsi, Studio, una
   sessione, pannello admin.
2. Spegni la manutenzione:

   ```bash
   ENVIRONMENT=prod scripts/deploy.sh manutenzione off
   ```

   Scrivi `si`. Il comando controlla che la home torni a rispondere 200.
3. Controlla da una finestra in incognito.
4. Se avevi avvisato sui social, scrivi che il sito è tornato.

---

## 6. Fermare anche i job (solo se il problema è nei dati)

Se il guasto riguarda le tabelle e non vuoi che i job le scrivano mentre lavori, blocca le
loro Lambda: con "concorrenza riservata" a 0 non partono. Gli orari restano in EventBridge
Scheduler: quando un job non riesce a partire riprova 2 volte, poi salta quel giro.

```bash
cd infra/terraform/environments/prod
JOBS=$(terraform output -json job_functions | jq -r '.[]')     # nomi delle Lambda dei job
cd -

# Ferma i job
for f in $JOBS; do aws lambda put-function-concurrency --region eu-south-1 --function-name "$f" --reserved-concurrent-executions 0; done

# Li riattiva: da fare prima di riaprire
for f in $JOBS; do aws lambda delete-function-concurrency --region eu-south-1 --function-name "$f"; done
```

Terraform non gestisce questa impostazione, quindi un deploy non la tocca: ricordati di
riattivarli. Per lanciare a mano un job saltato: `ENVIRONMENT=prod scripts/deploy.sh job inpa-scraper`.

---

## 7. Se qualcosa non va

| Problema | Cosa fare |
|---|---|
| "KeyValueStore della manutenzione non trovata" | L'ambiente non ha ancora il deploy con la manutenzione: `scripts/deploy.sh infra` |
| "serve jq" | `brew install jq` |
| Errore `PreconditionFailed` / ETag | Qualcuno ha cambiato le chiavi nello stesso momento: ripeti il comando |
| "la home risponde ancora 200" (o 503) | La modifica arriva a CloudFront in qualche secondo: aspetta e controlla con `manutenzione stato`. Ricarica il browser forzando (Cmd+Shift+R) |
| Il link di accesso non funziona | Hai riacceso la manutenzione e il codice è cambiato: prendi quello nuovo con `manutenzione stato` |
| `deploy.sh` non funziona (credenziali, Terraform) | Usa la console AWS: vedi sotto |

**Dalla console AWS, senza `deploy.sh`.** Apri CloudFront, poi Functions, poi la scheda
**KeyValueStores**, e scegli `imieiconcorsi-prod-manutenzione`. Da lì:

- **per chiudere**: chiave `attiva` = `si`, e se vuoi anche `messaggio`;
- **per riaprire**: chiave `attiva` = `no`.

Funziona subito come il comando, ma senza il link di accesso, a meno che tu non aggiunga
anche la chiave `accesso` con un codice a tua scelta.

**Dalla riga di comando AWS:**

```bash
ARN=$(terraform -chdir=infra/terraform/environments/prod output -raw manutenzione_kvs_arn)
ETAG=$(aws cloudfront-keyvaluestore describe-key-value-store --region us-east-1 --kvs-arn "$ARN" --query ETag --output text)
aws cloudfront-keyvaluestore put-key --region us-east-1 --kvs-arn "$ARN" --if-match "$ETAG" --key attiva --value si   # oppure no
```

---

## 8. Vedere la pagina senza chiudere il sito

```bash
ENVIRONMENT=prod scripts/deploy.sh manutenzione anteprima
```

Apri l'indirizzo che stampa (`https://imieiconcorsi.it/?manutenzione=anteprima`). Vedi la
pagina con il messaggio salvato, mentre il sito resta aperto per tutti.

Per cambiare **testo o grafica** della pagina, modifica
`infra/terraform/modules/web/functions/manutenzione.js` (funzione `paginaManutenzione`) e
fai `scripts/deploy.sh infra`. Il file deve restare sotto i 10 KB, limite delle CloudFront
Functions; oggi è circa 6 KB. Prima del deploy, `scripts/deploy.sh test` prova i casi in
`packages/functions/test/manutenzione.test.ts`.

**Costi**: trascurabili. Ogni richiesta fa una lettura della KeyValueStore, circa 0,03 $
per milione di letture.
