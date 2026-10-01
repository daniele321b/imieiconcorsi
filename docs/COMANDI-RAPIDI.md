# Comandi rapidi

Comandi pronti da copiare. Il runbook con le spiegazioni è [DEPLOY.md](DEPLOY.md).

Tutti i comandi si lanciano dalla cartella del repo, dopo:
```bash
cd ~/Documents/projects/concorsi/imieiconcorsi
export AWS_PROFILE=<il-tuo-profilo>
```

Ambienti Terraform:
- **shared**: risorse comuni a dev e prod (oggi SES, il mittente delle email). Si
  crea una volta e non si distrugge con gli ambienti.
- **dev**: tutte le risorse si chiamano `imieiconcorsi-dev-…`.

## 1. Primo deploy

Prerequisiti sul Mac: `aws`, `terraform` (>= 1.10) e `node` (>= 22).

Configurazione, una volta sola. I file `terraform.tfvars` non vanno su git:
```bash
cp infra/terraform/environments/shared/terraform.tfvars.example infra/terraform/environments/shared/terraform.tfvars
# metti sender_email = il tuo indirizzo (mittente finché non c'è un dominio)
cp infra/terraform/environments/dev/terraform.tfvars.example infra/terraform/environments/dev/terraform.tfvars
# metti admin_email = dove vuoi ricevere gli avvisi (in sandbox: lo stesso indirizzo, o aggiungilo a sandbox_recipients in shared)
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

Le 60 domande dimostrative le carica Terraform.

**Dopo il primo `all`:**
1. Apri l'email di AWS ("Amazon Web Services – Email Address Verification
   Request") e clicca il link. Va fatto per ogni indirizzo da verificare.
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
scripts/deploy.sh urls        # "Sito  https://xxxx.cloudfront.net" -> aprilo nel browser
```
Registrati con la tua email: arriva un codice a 6 cifre (controlla anche lo
spam). Poi: onboarding → Concorsi → Segui → Studio o Simulazione. Il cambio di
piano in "Piani" è gratuito e immediato (modalità di prova), con scadenza a 30 o
365 giorni.

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
entro un'ora.

## 4. Email (SES) e job del mattino

Ogni mattina, ora italiana:

| Ora | Job | Cosa fa |
|---|---|---|
| 6:00 | `inpa-scraper` | Importa i bandi da inPA e ti scrive se ci sono bandi nuovi che citano una banca dati |
| 6:15 | `scadenze` | Riporta a Free chi ha il piano scaduto; manda l'email di promemoria 3 giorni prima della scadenza |

Per lanciarli subito:
```bash
scripts/deploy.sh job inpa-scraper
scripts/deploy.sh job scadenze
```

SES parte in **sandbox**: scrive solo agli indirizzi verificati, massimo 200 al
giorno. Per controllare:
```bash
scripts/deploy.sh ses-status
```
Per scrivere a tutti gli utenti si chiede ad AWS l'uscita dalla sandbox, una
volta per account. Meglio farlo dopo aver configurato il dominio:
```bash
scripts/deploy.sh ses-production https://<indirizzo-del-sito>   # scrivi "si"; AWS risponde in 24-48 ore
```
Un nuovo tester in sandbox va aggiunto a `sandbox_recipients` in
`infra/terraform/environments/shared/terraform.tfvars`. Poi:
```bash
scripts/deploy.sh shared      # terraform chiede "yes"; il tester riceve l'email di verifica da cliccare
```

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

## 7. Log

```bash
scripts/deploy.sh logs profile        # oppure: concorsi, study, billing, admin, inpa-scraper, scadenze (Ctrl+C per uscire)
```

## 8. Smontare

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
