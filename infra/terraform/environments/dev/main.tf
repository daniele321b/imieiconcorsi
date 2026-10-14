# Ambiente dev di iMieiConcorsi. Tutte le risorse si chiamano imieiconcorsi-dev-…
#
# Un solo CloudFront su https://dev.imieiconcorsi.it: il sito (S3
# privato) e, sotto /api, l'API Gateway che inoltra ai microservizi Lambda; i dati
# stanno in DynamoDB. In dev niente WAF (in prod: web_acl_arn sul modulo web).
# Piani e ruolo admin sono gruppi Cognito. Ogni mattina alle 6 i job importano i
# bandi da inPA e gestiscono le scadenze dei piani. Le email partono da SES,
# configurato nell'ambiente "shared" (comune a dev e prod).
#
# Le Lambda e il sito vanno compilati prima dell'apply: scripts/deploy.sh build.

# SES e altre risorse comuni: environments/shared (stesso bucket di stato).
data "terraform_remote_state" "shared" {
  backend = "s3"
  config = {
    bucket = var.state_bucket
    key    = "shared/terraform.tfstate"
    region = var.aws_region
  }
}

# Nomi e percorsi comuni dell'ambiente e configurazione letta dal sito.
locals {
  name          = "${var.project_name}-dev"
  repo          = abspath("${path.root}/../../../..")
  functions_dir = "${local.repo}/dist/functions"
  shared        = data.terraform_remote_state.shared.outputs
  # Prod userà la radice del dominio; dev il sottodominio.
  domain_name = "dev.${local.shared.domain}"

  # /config.json letto dal browser all'avvio: lo stesso build del frontend vale per ogni ambiente.
  app_config = {
    apiUrl           = "/api"
    region           = var.aws_region
    userPoolId       = module.auth.user_pool_id
    userPoolClientId = module.auth.client_id
    cognitoDomain    = module.auth.domain
    social           = module.auth.social_providers
    # Annunci del piano Free: vuoto = annunci interni (promozione dei piani), senza cookie di terzi.
    pubblicita = { adsenseClient = var.adsense_client, adsenseSlot = var.adsense_slot }
  }

  # Permessi riusati da più Lambda: email con SES e avvisi all'admin sul topic SNS.
  invia_email = {
    Effect   = "Allow"
    Action   = ["ses:SendEmail", "sns:Publish"]
    Resource = concat(local.shared.ses_identity_arns, [local.shared.ses_configuration_set_arn, aws_sns_topic.avvisi_admin.arn])
  }
  cognito_piani = {
    Effect   = "Allow"
    Action   = ["cognito-idp:AdminAddUserToGroup", "cognito-idp:AdminRemoveUserFromGroup"]
    Resource = module.auth.user_pool_arn
  }

  email_env = {
    SES_SENDER            = local.shared.ses_sender_email
    SES_CONFIGURATION_SET = local.shared.ses_configuration_set_name
    ADMIN_EMAIL           = var.admin_email
    # Avvisi all'admin: via SNS (niente sandbox di SES), vedi aws_sns_topic.avvisi_admin.
    ADMIN_TOPIC_ARN = aws_sns_topic.avvisi_admin.arn
    # Le email di dev si riconoscono a colpo d'occhio.
    EMAIL_SUBJECT_PREFIX = "[dev] "
  }
  cognito_env = { USER_POOL_ID = module.auth.user_pool_id }
  # Link nelle email (es. "torna a un piano a pagamento").
  site_env = { SITE_URL = module.web.url }
  # Firma dei link "non ricevere più avvisi" (valgono senza login).
  disiscrizione_env = { DISISCRIZIONE_SECRET = random_password.disiscrizione.result }

  # Lista dei bandi in cache: file nel bucket del sito, serviti da CloudFront sotto /dati/bandi/.
  cache_bandi_env = { WEB_BUCKET = module.web.bucket }
  cache_bandi = {
    Effect   = "Allow"
    Action   = ["s3:PutObject"]
    Resource = "arn:aws:s3:::${module.web.bucket}/dati/*"
  }

  # Modello del profilo d'inferenza senza il prefisso di area (eu., us., global.…).
  ai_base_model = replace(var.ai_model, "/^(eu|us|apac|jp|global)\\./", "")
}

# Avvisi all'admin (nuovi bandi con banca dati, richieste di assistenza, ricevute non partite,
# spesa AI…): un topic SNS con l'iscrizione email ad admin_email. Al primo apply arriva l'email
# "AWS Notification - Subscription Confirmation": il link va cliccato una volta.
resource "aws_sns_topic" "avvisi_admin" {
  name = "${local.name}-avvisi-admin"
  # Cifrato: ci passano i messaggi del modulo contatti. Pubblicano solo le nostre Lambda,
  # quindi basta la chiave gestita da AWS.
  kms_master_key_id = "alias/aws/sns"
}

# L'email dell'amministratore riceve gli avvisi (si conferma dal link che arriva).
resource "aws_sns_topic_subscription" "avvisi_admin" {
  count     = var.admin_email == "" ? 0 : 1
  topic_arn = aws_sns_topic.avvisi_admin.arn
  protocol  = "email"
  endpoint  = var.admin_email
}

# Segreto tra CloudFront e le Lambda dell'API: senza, l'indirizzo diretto dell'API Gateway
# scavalcherebbe WAF e limiti (core/http.ts, daCloudFront).
resource "random_password" "origine" {
  length  = 40
  special = false
}

# Segreto che firma i link delle email (disiscrizione, lettura): generato una volta e tenuto nello stato.
resource "random_password" "disiscrizione" {
  length  = 48
  special = false
}

# Tabelle DynamoDB (modules/data): utenti, concorsi, domande, sessioni, ordini, richieste, progressi…
module "data" {
  source = "../../modules/data"
  name   = local.name
}

# Sito e lista dei bandi in cache dietro CloudFront, con /api verso l'API Gateway (modules/web).
module "web" {
  source      = "../../modules/web"
  name        = local.name
  dist_dir    = "${local.repo}/packages/web/dist"
  api_domain  = module.api.api_domain
  domain_name = local.domain_name
  zone_id     = local.shared.zone_id

  providers = {
    aws           = aws
    aws.us_east_1 = aws.us_east_1
  }

  app_config = local.app_config

  # CSP: oltre al nostro sito, il login (Cognito) e l'invio dei PDF delle banche dati (S3).
  origine_segreta = random_password.origine.result
  csp_connect_src = [
    "https://cognito-idp.${var.aws_region}.amazonaws.com",
    "https://${module.auth.domain}",
    "https://${module.contenuti.bucket}.s3.${var.aws_region}.amazonaws.com",
    "https://${module.contenuti.bucket}.s3.amazonaws.com",
  ]
  pubblicita_esterna = var.adsense_client != ""
}

# Trigger Cognito: collega Google/Facebook all'account con la stessa email.
# Permesso su tutti i user pool dell'account nella regione: l'ARN preciso del pool
# creerebbe un ciclo (il pool conosce il trigger, il trigger conoscerebbe il pool).
module "auth_trigger" {
  source     = "../../modules/lambda"
  name       = "${local.name}-auth-pre-signup"
  source_dir = "${local.functions_dir}/auth-pre-signup"
  policy_statements = [{
    Effect   = "Allow"
    Action   = ["cognito-idp:ListUsers", "cognito-idp:AdminLinkProviderForUser"]
    Resource = "arn:aws:cognito-idp:${var.aws_region}:${data.aws_caller_identity.current.account_id}:userpool/*"
  }]
}

# Trigger Cognito degli accessi: a ogni login scrive una riga nella tabella accessi (12 mesi) e
# l'ultimo accesso sul profilo. Non blocca mai il login, anche se non riesce a scrivere.
module "auth_accessi" {
  source       = "../../modules/lambda"
  name         = "${local.name}-auth-accessi"
  source_dir   = "${local.functions_dir}/auth-accessi"
  environment  = module.data.table_env
  write_tables = [module.data.table_arns.accessi, module.data.table_arns.users]
}

# Id dell'account AWS (per gli ARN dei permessi Bedrock).
data "aws_caller_identity" "current" {}

# Cognito: account, login social, gruppi dei piani (modules/auth).
module "auth" {
  source     = "../../modules/auth"
  name       = local.name
  aws_region = var.aws_region

  pre_sign_up_enabled    = true
  pre_sign_up_lambda_arn = module.auth_trigger.arn
  accessi_enabled        = true
  accessi_lambda_arn     = module.auth_accessi.arn

  # Solo in dev il login accetta anche il sito in locale (scripts/deploy.sh local).
  app_origins = ["http://localhost:5173", module.web.url]

  google_client_id     = var.google_client_id
  google_client_secret = var.google_client_secret
  facebook_app_id      = var.facebook_app_id
  facebook_app_secret  = var.facebook_app_secret
}

# API: un microservizio Lambda per voce di services, con le sue route e i suoi permessi (modules/api).
# Le route devono coincidere con quelle del codice (service() in packages/functions/src/<servizio>/handler.ts).
module "api" {
  source        = "../../modules/api"
  name          = local.name
  functions_dir = local.functions_dir
  jwt_issuer    = module.auth.issuer
  jwt_audience  = module.auth.client_id
  # Variabili di tutte le Lambda dell'API: tabelle e segreto dell'origine CloudFront.
  environment = merge(module.data.table_env, { ORIGINE_SEGRETA = random_password.origine.result })
  # Ogni richiesta con login segna l'utente come attivo (pannello admin → Utenti attivi).
  write_tables_comuni = [module.data.table_arns.attivita]

  services = {
    profile = {
      routes = ["GET /me", "PUT /me/profilo", "PUT /me/feedback", "DELETE /me"]
      # DELETE /me cancella l'account: profilo, concorsi seguiti, sessioni, richieste, progressi e utente Cognito.
      # Ordini: eliminando l'account ci si scrivono email e nome (restano 10 anni per legge).
      write_tables = [
        module.data.table_arns.users, module.data.table_arns.follows, module.data.table_arns.attempts,
        module.data.table_arns.richieste, module.data.table_arns.progressi, module.data.table_arns.ordini,
        module.data.table_arns.accessi,
      ]
      read_tables = []
      # Il nome è un dato personale: si salva su Cognito, non nel database.
      # Un nuovo feedback sull'app arriva all'admin per email.
      environment = merge(local.cognito_env, local.email_env)
      policies = jsonencode([local.invia_email, {
        Effect   = "Allow"
        Action   = ["cognito-idp:AdminUpdateUserAttributes", "cognito-idp:AdminDeleteUser"]
        Resource = module.auth.user_pool_arn
      }])
    }
    concorsi = {
      routes = [
        "GET /concorsi", "GET /concorsi/{id}",
        "GET /me/concorsi", "PUT /me/concorsi/{id}", "DELETE /me/concorsi/{id}", "GET /me/storico-concorsi",
      ]
      write_tables = [module.data.table_arns.follows]
      # banche: il titolo della banca dati collegata, nel dettaglio del concorso.
      read_tables = [module.data.table_arns.concorsi, module.data.table_arns.users, module.data.table_arns.banche]
    }
    study = {
      routes = [
        "GET /materie", "POST /sessioni", "GET /sessioni/{id}",
        "POST /sessioni/{id}/consegna", "GET /me/statistiche", "GET /banche-dati", "GET /banche-dati/{id}/domande",
        "DELETE /me/progressi/{bancaId}", "PUT /me/progressi/{bancaId}/preferite/{numero}",
      ]
      # Sul profilo: il contatore degli utilizzi settimanali delle banche dati (piano Free).
      # Progressi: domande delle banche dati già fatte e sbagliate, aggiornati a ogni consegna.
      write_tables = [module.data.table_arns.attempts, module.data.table_arns.users, module.data.table_arns.progressi]
      read_tables = [
        module.data.table_arns.questions, module.data.table_arns.concorsi, module.data.table_arns.banche,
      ]
      # Sezione Banche dati: elenco delle banche pubblicate (tabella piccola, uno Scan).
      policies = jsonencode([{
        Effect   = "Allow"
        Action   = ["dynamodb:Scan"]
        Resource = module.data.table_arns.banche
      }])
    }
    billing = {
      routes = [
        "GET /piani", "POST /me/abbonamento", "POST /me/codice-sconto", "GET /me/ordini", "GET /me/ordini/{id}", "POST /me/ordini/{id}/ricevuta",
        "GET /me/invito", "POST /me/invito",
      ]
      # Conferme di Stripe: rotta senza login, protetta dalla firma del webhook.
      public_routes = ["POST /pubblico/stripe/webhook"]
      # Il piano è il gruppo Cognito; sul profilo stanno scadenza e periodo.
      # Ordini: uno per acquisto. Codici sconto: si conta l'uso a pagamento riuscito.
      # follows: al ritorno al Free resta seguito un solo concorso (gli altri vanno nello storico).
      write_tables = [module.data.table_arns.users, module.data.table_arns.codici, module.data.table_arns.ordini, module.data.table_arns.follows]
      read_tables  = []
      # Con la chiave Stripe in terraform.tfvars si paga davvero (modalità test di Stripe in dev);
      # senza, "mock": cambio piano immediato e gratuito.
      # Dopo l'acquisto parte l'email di conferma (supporto durevole per il consenso).
      environment = merge(local.cognito_env, local.email_env, local.site_env, {
        BILLING_MODE          = var.stripe_secret_key == "" ? "mock" : "stripe"
        STRIPE_SECRET_KEY     = var.stripe_secret_key
        STRIPE_WEBHOOK_SECRET = var.stripe_webhook_secret
      })
      policies = jsonencode([local.cognito_piani, local.invia_email, {
        # Email per la conferma d'acquisto: sta solo in Cognito. Gruppi: piano di chi ha invitato un amico.
        Effect   = "Allow"
        Action   = ["cognito-idp:AdminGetUser", "cognito-idp:AdminListGroupsForUser"]
        Resource = module.auth.user_pool_arn
      }])
    }
    ai = {
      # Piano Pro: tutor e allenamenti con domande generate (Claude su Bedrock).
      # Sul profilo: gettoni, token e spesa del mese, richieste al minuto.
      # Contatori: spesa AI del mese di tutta la piattaforma (tetto mensile, email all'admin).
      routes       = ["GET /ai/stato", "POST /ai/tutor", "POST /ai/allenamento"]
      write_tables = [module.data.table_arns.users, module.data.table_arns.contatori]
      read_tables  = [module.data.table_arns.attempts, module.data.table_arns.questions]
      environment = merge(local.email_env, {
        AI_MODEL             = var.ai_model
        AI_TETTO_UTENTE_USD  = tostring(var.ai_tetto_utente_usd)
        AI_TETTO_MENSILE_USD = tostring(var.ai_tetto_mensile_usd)
      })
      # Un allenamento da 5 domande può richiedere 15-20 secondi.
      timeout = 29
      policies = jsonencode([local.invia_email, {
        # Il profilo d'inferenza EU smista la richiesta tra le regioni europee:
        # servono il profilo (qui) e il modello in ogni regione di destinazione.
        Effect = "Allow"
        Action = ["bedrock:InvokeModel"]
        Resource = [
          "arn:aws:bedrock:${var.aws_region}:${data.aws_caller_identity.current.account_id}:inference-profile/${var.ai_model}",
          "arn:aws:bedrock:*::foundation-model/${local.ai_base_model}",
        ]
      }])
    }
    richieste = {
      # Assistenza: richieste degli utenti registrati (banca dati, domanda sbagliata, accesso,
      # pagamento…). Ogni richiesta o messaggio nuovo arriva all'admin per email.
      routes = [
        "GET /me/richieste", "POST /me/richieste", "POST /me/richieste/{id}/messaggi", "PUT /me/richieste/{id}/letta",
      ]
      write_tables = [module.data.table_arns.richieste]
      read_tables  = []
      environment  = merge(local.email_env, local.site_env)
      policies     = jsonencode([local.invia_email])
    }
    pubblico = {
      # Disiscrizione dagli avvisi in un clic, dal link firmato nell'email o da Gmail & co.
      routes = []
      # Lettura degli avvisi: immagine invisibile e link delle email (firmati come la disiscrizione).
      # Modulo della pagina /contatti: il messaggio va all'admin sul topic SNS; contatori = limite per IP.
      public_routes = ["POST /pubblico/disiscrivi", "GET /pubblico/aperto", "GET /pubblico/clic", "POST /pubblico/contatto"]
      write_tables  = [module.data.table_arns.users, module.data.table_arns.contatori]
      read_tables   = []
      environment   = merge(local.disiscrizione_env, local.email_env)
      policies      = jsonencode([local.invia_email])
    }
    admin = {
      # Pannello di controllo: ogni route controlla il gruppo "admin" del token.
      routes = [
        "GET /admin/riepilogo", "GET /admin/utenti",
        "PUT /admin/utenti/{username}/piano", "PUT /admin/utenti/{username}/stato", "DELETE /admin/utenti/{username}",
        "GET /admin/utenti/{username}/accessi", "GET /admin/attivita", "GET /admin/provenienza",
        "GET /admin/codici", "POST /admin/codici", "PUT /admin/codici/{codice}", "DELETE /admin/codici/{codice}",
        "GET /admin/banche-dati", "POST /admin/banche-dati", "PUT /admin/banche-dati/{id}",
        "POST /admin/banche-dati/{id}/estrai", "POST /admin/banche-dati/{id}/pdf", "POST /admin/banche-dati/{id}/pubblica", "POST /admin/banche-dati/{id}/ritira",
        "DELETE /admin/banche-dati/{id}",
        "POST /admin/banche-dati/{id}/concorsi", "DELETE /admin/banche-dati/{id}/concorsi/{concorsoId}",
        "PUT /admin/concorsi/{id}/concluso", "PUT /admin/concorsi/{id}", "DELETE /admin/concorsi/{id}/modifiche",
        "GET /admin/ordini",
        "GET /admin/richieste", "POST /admin/richieste/{userId}/{id}",
      ]
      # Banche dati: pubblicare scrive le domande ufficiali e collega il concorso.
      write_tables = [
        module.data.table_arns.users, module.data.table_arns.codici, module.data.table_arns.banche,
        module.data.table_arns.questions, module.data.table_arns.concorsi, module.data.table_arns.follows,
        module.data.table_arns.richieste,
        # Eliminare un utente cancella anche le sue sessioni e i progressi.
        module.data.table_arns.attempts, module.data.table_arns.progressi,
        # Ordini: email e nome dell'utente eliminato restano sui suoi ordini.
        # Accessi: storico dei login di ogni utente, e cancellati con l'utente.
        module.data.table_arns.ordini, module.data.table_arns.accessi,
      ]
      # Contatori: spesa AI del mese nel riepilogo del pannello.
      read_tables = [module.data.table_arns.contatori]
      # Cambiando piano a un utente gli arriva l'email (piano attivato / tornato Free).
      environment = merge(local.cognito_env, local.email_env, local.site_env, {
        CONTENUTI_BUCKET     = module.contenuti.bucket
        AI_TETTO_MENSILE_USD = tostring(var.ai_tetto_mensile_usd)
      })
      policies = jsonencode([local.cognito_piani, local.invia_email, {
        # PDF delle banche dati: link firmato per il caricamento, lettura delle domande estratte,
        # copia su se stesso per rifare l'estrazione, cancellazione quando l'admin la elimina.
        Effect   = "Allow"
        Action   = ["s3:PutObject", "s3:GetObject", "s3:DeleteObject"]
        Resource = "${module.contenuti.bucket_arn}/banche-dati/*"
        }, {
        Effect   = "Allow"
        Action   = ["dynamodb:Scan"]
        Resource = module.data.table_arns.banche
        }, {
        # Codici sconto e storico pagamenti (tabelle piccole); provenienza degli iscritti
        # (users, due soli campi per profilo).
        Effect   = "Allow"
        Action   = ["dynamodb:Scan"]
        Resource = [module.data.table_arns.codici, module.data.table_arns.ordini, module.data.table_arns.users]
        }, {
        Effect = "Allow"
        Action = [
          "cognito-idp:ListUsers", "cognito-idp:ListUsersInGroup", "cognito-idp:AdminGetUser",
          "cognito-idp:AdminListGroupsForUser",
          "cognito-idp:DescribeUserPool", "cognito-idp:AdminEnableUser", "cognito-idp:AdminDisableUser",
          "cognito-idp:AdminDeleteUser",
        ]
        Resource = module.auth.user_pool_arn
      }])
    }
  }
}

# Job pianificati (modules/jobs): orari in ora italiana, codice in packages/functions/src/jobs/.
module "jobs" {
  source        = "../../modules/jobs"
  name          = local.name
  functions_dir = local.functions_dir
  environment   = merge(module.data.table_env, local.email_env)

  jobs = {
    inpa-scraper = {
      description = "Importa i bandi aperti e i chiusi recenti da inPA, rifà la lista in cache, avvisa l'admin dei nuovi con banca dati"
      schedule    = "cron(0 6 * * ? *)"
      # Il massimo di Lambda: l'import dello storico dei chiusi (storico-bandi) va a blocchi da ~13 minuti.
      timeout      = 900
      write_tables = [module.data.table_arns.concorsi]
      # SITE_URL: nell'email all'admin il link ai bandi da caricare.
      environment = merge(local.cache_bandi_env, local.site_env)
      policies    = jsonencode([local.invia_email, local.cache_bandi])
    }
    pulizia-bandi = {
      description = "Domenica e mercoledì: toglie i bandi che inPA non elenca più e rifà la lista in cache"
      # Due volte a settimana: così il controllo "job fermo" (al massimo 7 giorni in CloudWatch)
      # vede sempre almeno un'esecuzione, senza falsi allarmi prima del giro.
      schedule = "cron(0 3 ? * SUN,WED *)"
      timeout  = 900
      # Cancella dalla tabella dei bandi; Scan per trovare quelli non più su inPA.
      write_tables = [module.data.table_arns.concorsi]
      environment  = local.cache_bandi_env
      policies = jsonencode([local.invia_email, local.cache_bandi, {
        Effect   = "Allow"
        Action   = ["dynamodb:Scan"]
        Resource = module.data.table_arns.concorsi
        }, {
        # Il giro di tutte le pagine non sta in una Lambda: si rilancia da sola.
        Effect   = "Allow"
        Action   = ["lambda:InvokeFunction"]
        Resource = "arn:aws:lambda:${var.aws_region}:${data.aws_caller_identity.current.account_id}:function:${local.name}-pulizia-bandi"
      }])
    }
    avvisi = {
      description  = "Email con i bandi nuovi dei comparti scelti: ogni giorno o il lunedì"
      schedule     = "cron(0 7 * * ? *)"
      write_tables = [module.data.table_arns.users]
      read_tables  = [module.data.table_arns.concorsi]
      environment  = merge(local.cognito_env, local.site_env, local.disiscrizione_env)
      policies = jsonencode([local.invia_email, {
        # Elenco di chi vuole gli avvisi: tabella users per intero.
        Effect   = "Allow"
        Action   = ["dynamodb:Scan"]
        Resource = module.data.table_arns.users
        }, {
        # L'email sta solo in Cognito (anonimizzazione).
        Effect   = "Allow"
        Action   = ["cognito-idp:AdminGetUser"]
        Resource = module.auth.user_pool_arn
      }])
    }
    scadenze = {
      description  = "Piani scaduti -> Free (con email); promemoria 3 giorni prima della scadenza"
      schedule     = "cron(15 6 * * ? *)"
      write_tables = [module.data.table_arns.users, module.data.table_arns.follows]
      environment  = merge(local.cognito_env, local.site_env)
      policies = jsonencode([local.invia_email, local.cognito_piani, {
        Effect   = "Allow"
        Action   = ["cognito-idp:ListUsersInGroup"]
        Resource = module.auth.user_pool_arn
      }])
    }
  }
}

# --- Banca domande statica ---------------------------------------------------
# I file data/domande/<materia>.json vanno nel bucket dei contenuti e una Lambda li
# importa nella tabella: modificare un file e lanciare infra basta ad aggiornarla.

module "contenuti" {
  source              = "../../modules/contenuti"
  name                = local.name
  functions_dir       = local.functions_dir
  domande_dir         = "${local.repo}/data/domande"
  questions_table_arn = module.data.table_arns.questions
  environment         = module.data.table_env

  banche_dati_table_arn = module.data.table_arns.banche
  # Il dominio e non module.web.url: il sito dipende dall'API, che dipende da questo modulo.
  upload_origins          = ["http://localhost:5173", "https://${local.domain_name}"]
  email_environment       = local.email_env
  email_policy_statements = [local.invia_email]
}

# Le 60 domande di prova erano item gestiti da Terraform: ora le carica l'import.
# "removed" le toglie dallo stato SENZA cancellarle dalla tabella.
removed {
  from = aws_dynamodb_table_item.domanda_demo

  lifecycle {
    destroy = false
  }
}

# --- Monitoraggio -------------------------------------------------------------
# Allarmi CloudWatch sulle risorse principali -> topic SNS imieiconcorsi-dev-monitoraggio
# (email a admin_email, da confermare dal link di AWS) + dashboard "imieiconcorsi-dev".

module "monitoraggio" {
  source     = "../../modules/monitoraggio"
  name       = local.name
  aws_region = var.aws_region
  email      = var.admin_email

  api_id          = module.api.api_id
  api_functions   = module.api.function_names
  job_functions   = module.jobs.function_names
  other_functions = merge(module.contenuti.function_names, { auth-pre-signup = module.auth_trigger.function_name, auth-accessi = module.auth_accessi.function_name })
  # Giorni senza esecuzioni prima dell'allarme: 2 per i job di ogni giorno, 5 per la pulizia
  # (domenica e mercoledì, al massimo 4 giorni tra un giro e l'altro). Con 1 giorno l'allarme
  # scatterebbe ogni notte tra la mezzanotte e l'ora del job.
  job_heartbeat = { inpa-scraper = 2, avvisi = 2, scadenze = 2, pulizia-bandi = 5 }

  table_names        = module.data.table_names
  distribution_id    = module.web.distribution_id
  ai_model           = var.ai_model
  budget_mensile_usd = var.budget_mensile_usd

  providers = {
    aws           = aws
    aws.us_east_1 = aws.us_east_1
  }
}
