# Deploy su AWS — runbook

Stack autonomo di iMieiConcorsi, tutto serverless in `eu-south-1` (Milano): stato
Terraform, autenticazione, dati e servizi suoi, nessuna dipendenza da altri
progetti. Comandi pronti in [COMANDI-RAPIDI.md](COMANDI-RAPIDI.md).

```
Browser ──HTTPS──▶ CloudFront (*.cloudfront.net)         [prod: + WAF]
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
| CloudFront | Un'unica distribuzione per sito e API (`/api/*`), HTTPS col certificato di default; in dev senza WAF |
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
├── environments/shared/  risorse comuni a dev e prod: SES
├── environments/dev/     ambiente dev: backend, provider, collegamento dei moduli, domande demo
└── modules/
    ├── data/             tabelle DynamoDB
    ├── auth/             Cognito + gruppi medium, pro, admin
    ├── api/              API Gateway + microservizi
    ├── jobs/             job del mattino + scheduler
    ├── ses/              identità SES e configuration set
    ├── web/              S3 + CloudFront + file del sito + config.json
    └── lambda/           una Lambda: zip, ruolo IAM, log
packages/
├── core/                 dominio condiviso (TypeScript)
├── functions/            codice dei microservizi e dello scraper (TypeScript)
└── web/                  sito React (TypeScript)
data/domande-demo.json    domande dimostrative, caricate da Terraform in dev
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
- **Email dell'app** (promemoria scadenze, avvisi admin): SES, configurato
  nell'ambiente **shared**, che dev legge con `terraform_remote_state`.
  - Finché non c'è un dominio, il mittente è un indirizzo verificato.
  - Con un dominio (`domain` in `shared/terraform.tfvars`) Terraform crea
    l'identità con DKIM e mostra i record CNAME da mettere nel DNS (output
    `ses_dkim_records`).
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
- **Poi:** passerà dalla piattaforma di pagamento (repo `paymentplatform`).
  1. `billing` crea l'ordine, con un id anonimo, e il checkout.
  2. L'utente paga con Stripe o PayPal e torna sul sito.
  3. Il piano si attiva dopo la verifica lato server: interrogazione della
     piattaforma, più la notifica firmata come seconda strada.
- **Scadenza:** il job `scadenze` manda il promemoria 3 giorni prima e, alla
  scadenza, riporta l'utente a Free.

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
