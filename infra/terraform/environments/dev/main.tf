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

  # Permessi riusati da più Lambda.
  invia_email = {
    Effect   = "Allow"
    Action   = ["ses:SendEmail"]
    Resource = concat(local.shared.ses_identity_arns, [local.shared.ses_configuration_set_arn])
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
    # Le email di dev si riconoscono a colpo d'occhio.
    EMAIL_SUBJECT_PREFIX = "[dev] "
  }
  cognito_env = { USER_POOL_ID = module.auth.user_pool_id }
  # Link nelle email (es. "torna a un piano a pagamento").
  site_env = { SITE_URL = module.web.url }
  # Firma dei link "non ricevere più avvisi" (valgono senza login).
  disiscrizione_env = { DISISCRIZIONE_SECRET = random_password.disiscrizione.result }
}

resource "random_password" "disiscrizione" {
  length  = 48
  special = false
}

module "data" {
  source = "../../modules/data"
  name   = local.name
}

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

data "aws_caller_identity" "current" {}

module "auth" {
  source     = "../../modules/auth"
  name       = local.name
  aws_region = var.aws_region

  pre_sign_up_enabled    = true
  pre_sign_up_lambda_arn = module.auth_trigger.arn

  # Solo in dev il login accetta anche il sito in locale (scripts/deploy.sh local).
  app_origins = ["http://localhost:5173", module.web.url]

  google_client_id     = var.google_client_id
  google_client_secret = var.google_client_secret
  facebook_app_id      = var.facebook_app_id
  facebook_app_secret  = var.facebook_app_secret
}

module "api" {
  source        = "../../modules/api"
  name          = local.name
  functions_dir = local.functions_dir
  jwt_issuer    = module.auth.issuer
  jwt_audience  = module.auth.client_id
  environment   = module.data.table_env

  services = {
    profile = {
      routes = ["GET /me", "PUT /me/profilo", "PUT /me/feedback", "DELETE /me"]
      # DELETE /me cancella l'account: profilo, concorsi seguiti, sessioni e utente Cognito.
      write_tables = [module.data.table_arns.users, module.data.table_arns.follows, module.data.table_arns.attempts]
      read_tables  = []
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
        "GET /me/concorsi", "PUT /me/concorsi/{id}", "DELETE /me/concorsi/{id}",
      ]
      write_tables = [module.data.table_arns.follows]
      read_tables  = [module.data.table_arns.concorsi, module.data.table_arns.users]
    }
    study = {
      routes = [
        "GET /materie", "POST /sessioni", "GET /sessioni/{id}",
        "POST /sessioni/{id}/consegna", "GET /me/statistiche", "GET /banche-dati",
      ]
      write_tables = [module.data.table_arns.attempts]
      read_tables = [
        module.data.table_arns.questions, module.data.table_arns.concorsi, module.data.table_arns.users,
        module.data.table_arns.banche,
      ]
      # Sezione Banche dati: elenco delle banche pubblicate (tabella piccola, uno Scan).
      policies = jsonencode([{
        Effect   = "Allow"
        Action   = ["dynamodb:Scan"]
        Resource = module.data.table_arns.banche
      }])
    }
    billing = {
      routes = ["GET /piani", "POST /me/abbonamento", "POST /me/codice-sconto", "GET /me/ordini/{id}"]
      # Conferme di Stripe: rotta senza login, protetta dalla firma del webhook.
      public_routes = ["POST /pubblico/stripe/webhook"]
      # Il piano è il gruppo Cognito; sul profilo stanno scadenza e periodo.
      # Ordini: uno per acquisto. Codici sconto: si conta l'uso a pagamento riuscito.
      write_tables = [module.data.table_arns.users, module.data.table_arns.codici, module.data.table_arns.ordini]
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
        # Email per la conferma d'acquisto: sta solo in Cognito.
        Effect   = "Allow"
        Action   = ["cognito-idp:AdminGetUser"]
        Resource = module.auth.user_pool_arn
      }])
    }
    pubblico = {
      # Disiscrizione dagli avvisi in un clic, dal link firmato nell'email o da Gmail & co.
      routes        = []
      public_routes = ["POST /pubblico/disiscrivi"]
      write_tables  = [module.data.table_arns.users]
      read_tables   = []
      environment   = local.disiscrizione_env
    }
    admin = {
      # Pannello di controllo: ogni route controlla il gruppo "admin" del token.
      routes = [
        "GET /admin/riepilogo", "GET /admin/utenti",
        "PUT /admin/utenti/{username}/piano", "PUT /admin/utenti/{username}/stato",
        "GET /admin/codici", "POST /admin/codici", "PUT /admin/codici/{codice}",
        "GET /admin/banche-dati", "POST /admin/banche-dati", "PUT /admin/banche-dati/{id}",
        "POST /admin/banche-dati/{id}/estrai", "POST /admin/banche-dati/{id}/pubblica", "POST /admin/banche-dati/{id}/ritira",
        "PUT /admin/concorsi/{id}/concluso",
      ]
      # Banche dati: pubblicare scrive le domande ufficiali e collega il concorso.
      write_tables = [
        module.data.table_arns.users, module.data.table_arns.codici, module.data.table_arns.banche,
        module.data.table_arns.questions, module.data.table_arns.concorsi,
      ]
      read_tables = []
      # Cambiando piano a un utente gli arriva l'email (piano attivato / tornato Free).
      environment = merge(local.cognito_env, local.email_env, local.site_env, { CONTENUTI_BUCKET = module.contenuti.bucket })
      policies = jsonencode([local.cognito_piani, local.invia_email, {
        # PDF delle banche dati: link firmato per il caricamento, lettura delle domande estratte,
        # copia su se stesso per rifare l'estrazione.
        Effect   = "Allow"
        Action   = ["s3:PutObject", "s3:GetObject"]
        Resource = "${module.contenuti.bucket_arn}/banche-dati/*"
        }, {
        Effect   = "Allow"
        Action   = ["dynamodb:Scan"]
        Resource = module.data.table_arns.banche
        }, {
        # Elenco dei codici sconto nel pannello: la tabella è piccola, basta uno Scan.
        Effect   = "Allow"
        Action   = ["dynamodb:Scan"]
        Resource = module.data.table_arns.codici
        }, {
        Effect = "Allow"
        Action = [
          "cognito-idp:ListUsers", "cognito-idp:ListUsersInGroup", "cognito-idp:AdminGetUser",
          "cognito-idp:AdminListGroupsForUser",
          "cognito-idp:DescribeUserPool", "cognito-idp:AdminEnableUser", "cognito-idp:AdminDisableUser",
        ]
        Resource = module.auth.user_pool_arn
      }])
    }
  }
}

module "jobs" {
  source        = "../../modules/jobs"
  name          = local.name
  functions_dir = local.functions_dir
  environment   = merge(module.data.table_env, local.email_env)

  jobs = {
    inpa-scraper = {
      description  = "Importa i bandi aperti da inPA e avvisa l'admin dei nuovi con banca dati"
      schedule     = "cron(0 6 * * ? *)"
      write_tables = [module.data.table_arns.concorsi]
      policies     = jsonencode([local.invia_email])
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
      write_tables = [module.data.table_arns.users]
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
