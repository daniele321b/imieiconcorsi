# Guida: accesso con Google e pagamenti

Configurazioni da fare una volta sola. Per Google servono circa 30 minuti.
Le chiavi segrete vanno **solo** nei file `terraform.tfvars`, che non finiscono su git: non incollarle in chat né in altri file.

---

## Parte 1 — Accesso con Google

Il sito non parla direttamente con Google: passa da Cognito. Su Google va
registrato **un solo indirizzo**, quello di Cognito:

```
https://imieiconcorsi-dev.auth.eu-south-1.amazoncognito.com/oauth2/idpresponse
```
(per controllarlo: `scripts/deploy.sh urls`, riga "Redirect Google/Facebook")

### 1. Crea il progetto

1. Vai su <https://console.cloud.google.com> ed entra con il tuo account Google.
2. In alto, accanto al logo, apri l'elenco dei progetti → **Nuovo progetto**.
3. Nome: `imieiconcorsi-dev` → **Crea**.
4. Controlla che in alto ora sia selezionato `imieiconcorsi-dev`.

### 2. Schermata di consenso

È la pagina che l'utente vede quando sceglie "Accedi con Google".

1. Menu ☰ → **API e servizi** → **Schermata consenso OAuth** (nelle console
   nuove si chiama **Google Auth Platform**) → **Inizia**.
2. Compila:
   - **Nome app:** `iMieiConcorsi`
   - **Email di assistenza utenti:** la tua
   - **Pubblico:** **Esterno**
   - **Dati di contatto:** la tua email
3. Accetta le norme → **Crea**.
4. Sezione **Pubblico** → **Utenti di test** → **Aggiungi utenti**: scrivi le
   email Gmail con cui vuoi provare (anche la tua). Finché l'app è "in test",
   solo queste persone possono entrare.

### 3. Crea le credenziali

1. Sezione **Client** (oppure **Credenziali** → **Crea credenziali** → **ID
   client OAuth**).
2. **Tipo di applicazione:** Applicazione web.
3. **Nome:** `imieiconcorsi-dev-cognito`.
4. **Origini JavaScript autorizzate** → Aggiungi URI:
   `https://imieiconcorsi-dev.auth.eu-south-1.amazoncognito.com`
5. **URI di reindirizzamento autorizzati** → Aggiungi URI:
   `https://imieiconcorsi-dev.auth.eu-south-1.amazoncognito.com/oauth2/idpresponse`
6. **Crea**. Compaiono **ID client** e **Client secret**: copiali subito (il
   secret si vede per intero una volta sola; in caso scarica il file JSON).

### 4. Inseriscile nel progetto

Apri `infra/terraform/environments/dev/terraform.tfvars` e compila:
```hcl
google_client_id     = "1234567890-xxxxxxxx.apps.googleusercontent.com"
google_client_secret = "GOCSPX-..."
```
Poi:
```bash
scripts/deploy.sh infra       # terraform chiede "yes"
```
Sulla pagina di accesso compare il pulsante **Continua con Google**.

### 5. Aprirlo a tutti (quando vuoi)

Google Auth Platform → **Pubblico** → **Pubblica app**. Usiamo solo nome ed
email: Google non chiede verifiche.

Se un utente ha già un account con email e password e poi entra con Google con
la stessa email, i due accessi finiscono nello stesso account.

---

## Parte 2 — Pagamenti (Stripe, con PayPal dentro Stripe)

La guida passo passo è in [GUIDA-PAGAMENTI.md](GUIDA-PAGAMENTI.md).
