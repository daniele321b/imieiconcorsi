# Ambiente dev di iMieiConcorsi. Tutte le risorse si chiamano imieiconcorsi-dev-…
#
# Un solo CloudFront all'indirizzo *.cloudfront.net, già in HTTPS: il sito (S3
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

  # /config.json letto dal browser all'avvio: lo stesso build del frontend vale per ogni ambiente.
  app_config = {
    apiUrl           = "/api"
    region           = var.aws_region
    userPoolId       = module.auth.user_pool_id
    userPoolClientId = module.auth.client_id
    cognitoDomain    = module.auth.domain
    social           = module.auth.social_providers
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
  }
  cognito_env = { USER_POOL_ID = module.auth.user_pool_id }
}

module "data" {
  source = "../../modules/data"
  name   = local.name
}

module "web" {
  source     = "../../modules/web"
  name       = local.name
  dist_dir   = "${local.repo}/packages/web/dist"
  api_domain = module.api.api_domain

  app_config = local.app_config
}

module "auth" {
  source     = "../../modules/auth"
  name       = local.name
  aws_region = var.aws_region

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
      routes       = ["GET /me", "PUT /me/profilo"]
      write_tables = [module.data.table_arns.users]
      read_tables  = []
      # Il nome è un dato personale: si salva su Cognito, non nel database.
      environment = local.cognito_env
      policies = [{
        Effect   = "Allow"
        Action   = ["cognito-idp:AdminUpdateUserAttributes"]
        Resource = module.auth.user_pool_arn
      }]
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
        "POST /sessioni/{id}/consegna", "GET /me/statistiche",
      ]
      write_tables = [module.data.table_arns.attempts]
      read_tables  = [module.data.table_arns.questions, module.data.table_arns.concorsi, module.data.table_arns.users]
    }
    billing = {
      routes = ["GET /piani", "POST /me/abbonamento"]
      # Il piano è il gruppo Cognito; sul profilo stanno scadenza e periodo.
      write_tables = [module.data.table_arns.users]
      read_tables  = []
      # "mock": cambio piano immediato e gratuito, finché non colleghiamo la piattaforma di pagamento.
      environment = merge(local.cognito_env, { BILLING_MODE = "mock" })
      policies    = [local.cognito_piani]
    }
    admin = {
      # Pannello di controllo: ogni route controlla il gruppo "admin" del token.
      routes = [
        "GET /admin/riepilogo", "GET /admin/utenti",
        "PUT /admin/utenti/{username}/piano", "PUT /admin/utenti/{username}/stato",
      ]
      write_tables = [module.data.table_arns.users]
      read_tables  = []
      environment  = local.cognito_env
      policies = [local.cognito_piani, {
        Effect = "Allow"
        Action = [
          "cognito-idp:ListUsers", "cognito-idp:ListUsersInGroup", "cognito-idp:AdminGetUser",
          "cognito-idp:DescribeUserPool", "cognito-idp:AdminEnableUser", "cognito-idp:AdminDisableUser",
        ]
        Resource = module.auth.user_pool_arn
      }]
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
      policies     = [local.invia_email]
    }
    scadenze = {
      description  = "Piani scaduti -> Free; email di promemoria 3 giorni prima della scadenza"
      schedule     = "cron(15 6 * * ? *)"
      write_tables = [module.data.table_arns.users]
      environment  = merge(local.cognito_env, { SITE_URL = module.web.url })
      policies = [local.invia_email, local.cognito_piani, {
        Effect   = "Allow"
        Action   = ["cognito-idp:ListUsersInGroup"]
        Resource = module.auth.user_pool_arn
      }]
    }
  }
}

# --- Domande dimostrative (solo dev) ------------------------------------------
# 60 domande scritte a mano (data/domande-demo.json) per provare studio e
# simulazioni finché la pipeline sui libri non genera la banca vera.

locals {
  domande_demo = { for d in jsondecode(file("${local.repo}/data/domande-demo.json")) : "${d.materia}/${d.id}" => d }
}

resource "aws_dynamodb_table_item" "domanda_demo" {
  for_each   = local.domande_demo
  table_name = module.data.questions_table_name
  hash_key   = "materia"
  range_key  = "id"

  item = jsonencode({
    materia     = { S = each.value.materia }
    id          = { S = each.value.id }
    argomento   = { S = each.value.argomento }
    livello     = { N = tostring(each.value.livello) }
    testo       = { S = each.value.testo }
    opzioni     = { L = [for o in each.value.opzioni : { S = o }] }
    corretta    = { N = tostring(each.value.corretta) }
    spiegazione = { S = each.value.spiegazione }
    fonte       = { S = each.value.fonte }
  })
}
