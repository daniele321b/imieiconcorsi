# Deploy su AWS — runbook

Stack autonomo di iMieiConcorsi, tutto serverless in `eu-south-1` (Milano): stato
Terraform, autenticazione, dati e servizi suoi, nessuna dipendenza da altri
progetti. Comandi pronti in [COMANDI-RAPIDI.md](COMANDI-RAPIDI.md).

```
Browser ──HTTPS──▶ CloudFront: dev.imieiconcorsi.it (prod: imieiconcorsi.it, + WAF)
                     ├── /api/*  ──▶ API Gateway HTTP (JWT Cognito)
                     │                 ├── profile    /me, /me/profilo                       ──▶ users
                     │                 ├── concorsi   /concorsi, /me/concorsi                ──▶ follows   (legge concorsi, users)
                     │                 ├── study      /materie, /sessioni, /me/statistiche   ──▶ attempts  (legge questions, concorsi, users)
                     │                 ├── billing    /piani, /me/abbonamento                ──▶ users + gruppi Cognito
                     │                 └── admin      /admin/riepilogo, /admin/utenti/...    ──▶ users + Cognito (solo gruppo admin)
                     └── tutto il resto ──▶ S3 privato: sito React + config.json
Browser ──HTTPS──▶ Cognito (login email/password, Google, Facebook; gruppi medium, pro, admin)

EventBridge Scheduler, ora italiana
  06:00 ──▶ inpa-scraper ──▶ concorsi            ──▶ email all'admin: nuovi bandi con banca dati
  06:15 ──▶ scadenze     ──▶ gruppi Cognito, users ──▶ email agli utenti: piano in scadenza tra 3 giorni

Ambiente "shared" (comune a dev e prod): SES, mittente delle email
```

**Piani e ruoli sono gruppi Cognito** (`medium`, `pro`, `admin`): finiscono nel
token di login e ogni servizio li legge da lì, senza chiedere al database. Solo
il backend (pagamenti, pannello admin, job delle scadenze) può cambiarli. Dopo
un cambio, l'utente vede il nuovo piano quando il token si rinnova: subito se il
cambio parte da lui, altrimenti entro un'ora. Sul profilo restano solo la
scadenza e il periodo.

**Privacy:** email e nome stanno solo in Cognito. Il database conosce gli utenti
solo per il loro id anonimo (`sub`).

Sito e API stanno allo **stesso indirizzo**: niente CORS, e in produzione basta
un WAF su CloudFront per proteggere entrambi. Due CloudFront Function fanno da
smistamento: una toglie il prefisso `/api` prima di passare all'API Gateway,
l'altra manda a `index.html` le route del sito (`/app/...`). L'API non viene
mai messa in cache (`Cache-Control: no-store`).

| Risorsa (`imieiconcorsi-dev-…`) | Note |
|---|---|
| CloudFront | Un'unica distribuzione per sito e API (`/api/*`) su `dev.imieiconcorsi.it`, certificato ACM (in us-east-1, validato via DNS); in dev senza WAF |
| Route 53 | Hosted zone `imieiconcorsi.it`, creata all'acquisto del dominio e solo letta da Terraform. Record: `dev` → CloudFront; DKIM, MAIL FROM e DMARC per le email |
| S3 `web-…` | Sito statico, bucket privato (accesso solo da CloudFront) |
| Cognito user pool + dominio `imieiconcorsi-dev.auth.eu-south-1.amazoncognito.com` | Email come username, verifica con codice; Google/Facebook se configurati |
| API Gateway HTTP | Autorizzazione JWT su tutte le route, limite 50 richieste/s in dev. In dev risponde anche al suo indirizzo diretto (`scripts/deploy.sh urls`); in prod quell'accesso va bloccato |
| 5 Lambda di servizio (`profile`, `concorsi`, `study`, `billing`, `admin`) + 2 job (`inpa-scraper`, `scadenze`) | Node.js 22, arm64; ognuna con un ruolo IAM limitato alle sue tabelle e ai permessi Cognito/SES che le servono |
| DynamoDB `users`, `concorsi`, `follows`, `questions`, `attempts` | On demand; backup continuo su `users` e `attempts` |
| EventBridge Scheduler | Lancia i job alle 6:00 e alle 6:15, ora italiana |
| SES (ambiente shared, nome `imieiconcorsi`) | Mittente verificato e configuration set con soppressione automatica di rimbalzi e reclami. Parte in sandbox |
| S3 `imieiconcorsi-tfstate-<account>` | Stato Terraform (creato da `bootstrap`, versionato e cifrato) |

Costo indicativo dev: pochi centesimi al giorno con poco traffico. Non ci sono
NAT, load balancer né database sempre accesi, quindi si può lasciare acceso.

## Struttura del codice

```
infra/terraform/
├── bootstrap/            bucket dello stato (una volta sola)
├── environments/shared/  risorse comuni a dev e prod: dominio (record email) e SES
├── environments/dev/     ambiente dev: backend, provider, collegamento dei moduli, domande demo
└── modules/
    ├── data/             tabelle DynamoDB
    ├── auth/             Cognito + gruppi medium, pro, admin
    ├── api/              API Gateway + microservizi
    ├── jobs/             job del mattino + scheduler
    ├── ses/              identità SES e configuration set
    ├── contenuti/        bucket dei contenuti + import automatico della banca domande
    ├── web/              S3 + CloudFront + file del sito + config.json
    └── lambda/           una Lambda: zip, ruolo IAM, log
packages/
├── core/                 dominio condiviso (TypeScript)
├── functions/            codice dei microservizi e dello scraper (TypeScript)
└── web/                  sito React (TypeScript)
data/domande/             banca domande statica, un file per materia (importata da modules/contenuti)
contenuti/                libri (fuori da git) e registro delle fonti
scripts/deploy.sh         tutti i comandi
```

## Come funziona un deploy

1. **Build** (`scripts/deploy.sh build`): esbuild impacchetta ogni Lambda in
   `dist/functions/<nome>/index.mjs`, Vite compila il sito in
   `packages/web/dist`. Le dipendenze Node le installa lo script se mancano.
2. **Infra** (`scripts/deploy.sh infra`): `terraform apply` zippa le Lambda,
   crea o aggiorna le risorse, carica i file del sito su S3 e scrive
   `config.json` (indirizzo dell'API, id di Cognito). Il sito legge
   `config.json` all'avvio, quindi lo stesso build vale per ogni ambiente.
   Terraform aggiorna solo le Lambda il cui codice è cambiato.

`index.html` e `config.json` sono serviti con `no-cache`; i file in `assets/`
hanno l'hash nel nome e sono in cache per un anno. Non servono invalidazioni
di CloudFront.

## Primo deploy

1. Profilo AWS con permessi di amministratore sull'account: `export AWS_PROFILE=...`
2. `scripts/deploy.sh bootstrap` crea `imieiconcorsi-tfstate-<account id>`. Il
   nome del bucket lo passa lo script a `terraform init`, quindi non va scritto
   da nessuna parte.
3. `scripts/deploy.sh all`. La prima volta CloudFront impiega 5-10 minuti.

## Email

- **Codici di verifica del login:** li manda Cognito con il suo servizio di
  default (massimo 50 al giorno, mittente `no-reply@verificationemail.com`).
  Quando c'è il dominio si possono passare su SES.
- **Email dell'app** (conferma d'acquisto, piano attivato o tornato Free,
  promemoria scadenze, avvisi admin): SES, configurato
  nell'ambiente **shared**, che dev legge con `terraform_remote_state`.
  - Mittente `noreply@imieiconcorsi.it`. Terraform crea nella hosted zone i 3
    record DKIM, il MAIL FROM `mail.imieiconcorsi.it` (MX + SPF) e il DMARC
    (`p=none` per iniziare, poi si stringe).
  - Le email di dev hanno l'oggetto che inizia con `[dev]`.
- **Sandbox:** SES consegna solo agli indirizzi verificati, fino a 200 email al
  giorno. L'uscita si chiede con `scripts/deploy.sh ses-production`, una volta per
  account: conviene farlo dopo aver configurato il dominio.

## Login social

Si attiva compilando `infra/terraform/environments/dev/terraform.tfvars` (vedi
COMANDI-RAPIDI, punto 4). Con le credenziali vuote Terraform non crea gli
identity provider e il sito nasconde i pulsanti.

## Pagamenti

Pagamenti singoli, senza rinnovo automatico: Medium o Pro per 30 o 365 giorni.

- **Oggi:** il servizio `billing` gira con `BILLING_MODE = "mock"` (in
  `environments/dev/main.tf`). Il cambio di piano è immediato e gratuito: mette
  l'utente nel gruppo Cognito e fissa la scadenza.
- **Poi (deciso il 2026-10-09):** Stripe Checkout diretto, senza la
  piattaforma `paymentplatform`. PayPal, Apple Pay e Google Pay si attivano
  dentro Stripe.
  1. `billing` crea l'ordine e la sessione Stripe, con il prezzo calcolato dal
     server.
  2. L'utente paga sulla pagina di Stripe e torna sul sito.
  3. Il piano si attiva con il webhook firmato di Stripe
     (`/api/pubblico/stripe/webhook`), una volta sola.
  Guida: `docs/GUIDA-PAGAMENTI.md`.
- **Scadenza:** il job `scadenze` manda il promemoria 3 giorni prima e, alla
  scadenza, riporta l'utente a Free e gli manda l'email.
- **Codici sconto:** tabella `imieiconcorsi-dev-codici`, scritta dal pannello
  admin (`/admin/codici`). `billing` li controlla (`POST /me/codice-sconto`) e,
  all'acquisto, conta l'uso con una scrittura condizionata: due acquisti insieme
  non superano gli usi massimi. Con Stripe l'importo
  scontato sarà quello dell'ordine.
- **Avvisi sui bandi:** job `avvisi` alle 7:00. Legge da `users` chi vuole gli
  avvisi e prende i bandi dei suoi comparti con data di pubblicazione inPA di
  ieri (ultimi 7 giorni per il settimanale); senza data conta `primoImportoIl`,
  scritto dallo scraper. L'email arriva da Cognito.
- **Pubblicità:** nel piano Free (`limiti.pubblicita`) un annuncio ogni 5
  domande di studio. AdSense è facoltativo (`adsense_client`, `adsense_slot`);
  senza, l'annuncio è interno.

## Produzione (da fare)

Requisiti già decisi, dettagli nel piano MVP ("Produzione e banche dati"):
WAF su CloudFront (`web_acl_arn` del modulo `web`, ACL creata in `us-east-1`),
test di carico a 1.000 utenti in parallelo, dati personali solo in Cognito con
pagina privacy da accettare, banche dati ufficiali su S3 per i piani Medium e
Pro. Per prod si crea `infra/terraform/environments/prod` sullo stesso modello di
dev.

## Smontare

`scripts/deploy.sh destroy` elimina tutto l'ambiente tranne il bucket di stato
(protetto da `prevent_destroy`).
