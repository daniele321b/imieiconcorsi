# Login con Google e Facebook — guida

Come creare le credenziali OAuth di Google e Facebook e collegarle all'ambiente
**dev**. Serve circa mezz'ora la prima volta. I comandi da lanciare sono anche
in [COMANDI-RAPIDI.md](COMANDI-RAPIDI.md), al punto 4.

## Come funziona

Il sito non parla mai direttamente con Google o Facebook: passa da Cognito.

```
Sito ──▶ Cognito (imieiconcorsi-dev.auth…) ──▶ Google / Facebook
                         ▲                              │
                         └── /oauth2/idpresponse ◀──────┘   (l'utente ha detto "sì")
Cognito ──▶ Sito /auth/callback  (utente loggato)
```

Su Google e Facebook va quindi registrato **un solo indirizzo**, quello di
Cognito. Nell'ambiente dev è sempre lo stesso, anche se distruggi e ricrei
tutto:

| Cosa | Valore |
|---|---|
| Dominio Cognito | `imieiconcorsi-dev.auth.eu-south-1.amazoncognito.com` |
| URI di reindirizzamento | `https://imieiconcorsi-dev.auth.eu-south-1.amazoncognito.com/oauth2/idpresponse` |

Per controllarli:
```bash
scripts/deploy.sh urls        # riga "Redirect Google/Facebook"
```

Le credenziali vanno in `infra/terraform/environments/dev/terraform.tfvars`,
che **non** finisce su git:
```bash
cp infra/terraform/environments/dev/terraform.tfvars.example infra/terraform/environments/dev/terraform.tfvars
```

Puoi attivare anche uno solo dei due provider: quello lasciato vuoto resta
spento e il suo pulsante non compare.

---

## Google

### 1. Progetto

1. Vai su <https://console.cloud.google.com> con il tuo account Google.
2. In alto, menu dei progetti → **Nuovo progetto** → nome `imieiconcorsi-dev` → **Crea**.
3. Controlla che in alto sia selezionato il progetto appena creato.

### 2. Schermata di consenso ("Google Auth Platform")

Menu ☰ → **API e servizi** → **Schermata consenso OAuth**. Nelle console più
recenti la voce si chiama **Google Auth Platform**. Poi **Inizia**:

- **Nome app:** `iMieiConcorsi`
- **Email di assistenza utenti:** la tua
- **Pubblico:** **Esterno**
- **Dati di contatto:** la tua email → accetta le norme → **Crea**

Poi, nella sezione **Pubblico**:

- Lo stato di pubblicazione resta **Test**.
- **Utenti di test → Aggiungi utenti:** inserisci gli indirizzi Gmail con cui
  vuoi provare, fino a 100. Con l'app in "Test" **solo questi** possono
  entrare; gli altri vedono "Accesso bloccato".

Usiamo solo `openid`, `email` e `profile`, che Google considera non sensibili:
quando vorrai aprirlo a tutti basterà **Pubblica app**, senza verifica di
Google.

### 3. Client OAuth

**Client** (oppure **Credenziali → Crea credenziali → ID client OAuth**):

- **Tipo di applicazione:** Applicazione web
- **Nome:** `imieiconcorsi-dev-cognito`
- **Origini JavaScript autorizzate:** `https://imieiconcorsi-dev.auth.eu-south-1.amazoncognito.com`
- **URI di reindirizzamento autorizzati:** `https://imieiconcorsi-dev.auth.eu-south-1.amazoncognito.com/oauth2/idpresponse`
- **Crea**

Copia subito **ID client** e **Client secret**. Nelle console nuove il secret
si vede per intero una volta sola: in caso scarica il JSON.

### 4. In terraform.tfvars

```hcl
google_client_id     = "1234567890-xxxxxxxx.apps.googleusercontent.com"
google_client_secret = "GOCSPX-..."
```

---

## Facebook (Meta)

### 1. Account sviluppatore

1. Vai su <https://developers.facebook.com> ed entra con il tuo account Facebook.
2. Se è la prima volta: **Inizia / Registrati** come sviluppatore. Meta chiede
   di verificare il numero di telefono.

### 2. Crea l'app

**Le mie app** → **Crea app**:

- **Nome dell'app:** `iMieiConcorsi dev`
- **Email di contatto:** la tua
- **Caso d'uso:** "**Autentica e richiedi dati agli utenti con Facebook Login**"
- **Business portfolio:** per ora "non voglio collegare un portfolio"
- **Crea app** (chiede la password di Facebook)

### 3. Configura Facebook Login

Dashboard dell'app → **Casi d'uso** → Facebook Login → **Personalizza**:

- **Autorizzazioni:** aggiungi **email** (`public_profile` c'è già).
- **Impostazioni:**
  - **Login OAuth client:** Sì
  - **Login OAuth web:** Sì
  - **Imponi HTTPS:** Sì
  - **URI di reindirizzamento OAuth validi:** `https://imieiconcorsi-dev.auth.eu-south-1.amazoncognito.com/oauth2/idpresponse`
  - **Salva modifiche**

### 4. Impostazioni di base

**Impostazioni app → Di base**:

- **Domini app:** `imieiconcorsi-dev.auth.eu-south-1.amazoncognito.com`
- **URL dell'informativa sulla privacy:** serve solo per passare l'app in
  modalità Live. Per i test in sviluppo puoi lasciarlo vuoto.
- In fondo: **Aggiungi piattaforma → Sito web → URL del sito:**
  `https://imieiconcorsi-dev.auth.eu-south-1.amazoncognito.com/`
- **Salva modifiche**

Copia **ID app** e **Chiave segreta** (pulsante "Mostra").

### 5. Chi può entrare

L'app nasce in **modalità sviluppo**: possono entrare solo le persone con un
ruolo sull'app. Tu ce l'hai già. Per altri tester: **Ruoli app → Ruoli →
Aggiungi persone → Tester**, poi la persona deve accettare l'invito.

### 6. In terraform.tfvars

```hcl
facebook_app_id     = "1234567890123456"
facebook_app_secret = "abcdef0123456789..."
```

---

## Applica e prova

```bash
scripts/deploy.sh infra       # terraform chiede "yes"
```
Terraform crea gli identity provider su Cognito e li abilita sul client del
sito. Il `config.json` del sito si aggiorna da solo e i pulsanti "Continua con
Google / Facebook" compaiono. Ricarica la pagina, eventualmente svuotando la
cache.

## Problemi tipici

| Errore | Causa e soluzione |
|---|---|
| Google: `Errore 400: redirect_uri_mismatch` | L'URI nel client Google non coincide carattere per carattere con quello di Cognito: niente spazi, `https`, `/oauth2/idpresponse` alla fine. |
| Google: "Accesso bloccato: l'app non ha completato la verifica" | Il tuo indirizzo non è tra gli **utenti di test** (Google Auth Platform → Pubblico). |
| Facebook: "Questa app non è attiva" o "funzionalità non disponibile" | Chi prova non ha un ruolo sull'app (punto 5), oppure l'URI non è tra quelli validi. |
| Facebook: entra ma Cognito dà errore sull'email | L'account Facebook non ha un'email confermata o non l'ha condivisa: l'app ha bisogno dell'email. |
| Il pulsante non compare | `terraform.tfvars` incompleto: servono **sia** l'id **sia** il secret. Poi `scripts/deploy.sh infra`. |
| Dopo il login torni alla home ma non sei dentro | Apri la console del browser; di solito la callback non è tra quelle ammesse. Rilancia `scripts/deploy.sh infra`. |

## Da sapere

- **Account separati.** Se ti registri con email e password e poi entri con
  Google usando la stessa email, Cognito crea **due utenti diversi**. Il
  collegamento automatico degli account lo aggiungeremo più avanti.
- **I secret** stanno solo in `terraform.tfvars` (locale) e nello stato
  Terraform (bucket S3 privato e cifrato). Non vanno mai su git né in chat.
- **Distruggere e ricreare dev** non richiede di toccare Google e Facebook: il
  dominio Cognito si chiama sempre `imieiconcorsi-dev`.
- **Per prod** serviranno app OAuth separate (o almeno altri URI), con l'app
  Google pubblicata e quella Facebook in modalità Live, con informativa privacy.
- **"Currently ineligible for submission" su Meta:** riguarda solo il passaggio a
  Live, non i test in sviluppo. Per pubblicare servono:
  - categoria **Istruzione**;
  - icona 1024 × 1024: `docs/brand/icona-1024.png`;
  - URL dell'informativa privacy: `https://dev.imieiconcorsi.it/privacy`;
  - URL con le istruzioni per eliminare i dati: `https://dev.imieiconcorsi.it/eliminazione-dati`.

  Prima della pubblicazione vanno compilati i dati del titolare in
  `packages/web/src/lib/legale.ts`, e i testi vanno rivisti da un legale.
