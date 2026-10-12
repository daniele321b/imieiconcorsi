# Cognito: email + password, Google e Facebook (si attivano quando ci sono le credenziali).

locals {
  # Sapere SE c'è un secret non rivela il secret: senza nonsensitive() Terraform
  # marcherebbe come sensibili anche la lista dei provider e il config.json del sito.
  google_enabled   = var.google_client_id != "" && nonsensitive(var.google_client_secret != "")
  facebook_enabled = var.facebook_app_id != "" && nonsensitive(var.facebook_app_secret != "")
}

# Il "pool" degli utenti: login con l'email, codice di verifica per email, password di almeno
# 8 caratteri con maiuscola, minuscola e numero, recupero password via email.
resource "aws_cognito_user_pool" "main" {
  name                     = var.name
  username_attributes      = ["email"]
  auto_verified_attributes = ["email"]
  deletion_protection      = var.protezione ? "ACTIVE" : "INACTIVE"

  password_policy {
    minimum_length                   = 8
    require_lowercase                = true
    require_uppercase                = true
    require_numbers                  = true
    require_symbols                  = false
    temporary_password_validity_days = 7
  }

  account_recovery_setting {
    recovery_mechanism {
      name     = "verified_email"
      priority = 1
    }
  }

  verification_message_template {
    default_email_option = "CONFIRM_WITH_CODE"
    email_subject        = "Il tuo codice di verifica — iMieiConcorsi"
    email_message        = "Benvenuto su iMieiConcorsi! Il tuo codice di verifica è {####}"
  }

  # Email di Cognito: massimo 50 al giorno, sufficiente per dev. Con più utenti si passa a SES.
  email_configuration {
    email_sending_account = "COGNITO_DEFAULT"
  }

  # Una persona = un account: collega i login social all'account con la stessa email.
  # Accessi: a ogni login (email e password, Google, Facebook) il trigger "pre token generation"
  # registra l'accesso nella tabella accessi (modules/data), visibile nel pannello admin.
  dynamic "lambda_config" {
    for_each = var.pre_sign_up_enabled || var.accessi_enabled ? [1] : []
    content {
      pre_sign_up          = var.pre_sign_up_enabled ? var.pre_sign_up_lambda_arn : null
      pre_token_generation = var.accessi_enabled ? var.accessi_lambda_arn : null
    }
  }
}

# Permesso a Cognito di chiamare il trigger pre sign-up (functions/src/auth/pre-signup.ts).
# Permesso a Cognito di chiamare il trigger degli accessi.
resource "aws_lambda_permission" "accessi" {
  # Un booleano e non "arn != null": l'ARN si conosce solo dopo aver creato la Lambda.
  count         = var.accessi_enabled ? 1 : 0
  statement_id  = "AllowCognitoAccessi"
  action        = "lambda:InvokeFunction"
  function_name = var.accessi_lambda_arn
  principal     = "cognito-idp.amazonaws.com"
  source_arn    = aws_cognito_user_pool.main.arn
}

resource "aws_lambda_permission" "pre_sign_up" {
  count         = var.pre_sign_up_enabled ? 1 : 0
  statement_id  = "AllowCognito"
  action        = "lambda:InvokeFunction"
  function_name = var.pre_sign_up_lambda_arn
  principal     = "cognito-idp.amazonaws.com"
  source_arn    = aws_cognito_user_pool.main.arn
}

# Dominio del login social: https://<nome>.auth.<regione>.amazoncognito.com, senza certificati nostri.
resource "aws_cognito_user_pool_domain" "main" {
  domain       = var.name
  user_pool_id = aws_cognito_user_pool.main.id
}

# Accesso con Google: solo se in terraform.tfvars ci sono client id e secret (docs/LOGIN-SOCIAL.md).
resource "aws_cognito_identity_provider" "google" {
  count         = local.google_enabled ? 1 : 0
  user_pool_id  = aws_cognito_user_pool.main.id
  provider_name = "Google"
  provider_type = "Google"

  provider_details = {
    authorize_scopes = "openid email profile"
    client_id        = var.google_client_id
    client_secret    = var.google_client_secret
  }

  attribute_mapping = {
    email    = "email"
    name     = "name"
    username = "sub"
  }
}

# Accesso con Facebook: solo se ci sono app id e secret.
resource "aws_cognito_identity_provider" "facebook" {
  count         = local.facebook_enabled ? 1 : 0
  user_pool_id  = aws_cognito_user_pool.main.id
  provider_name = "Facebook"
  provider_type = "Facebook"

  provider_details = {
    authorize_scopes = "public_profile,email"
    client_id        = var.facebook_app_id
    client_secret    = var.facebook_app_secret
  }

  attribute_mapping = {
    email    = "email"
    name     = "name"
    username = "id"
  }
}

# Il "client" usato dal sito (senza secret: gira nel browser). Token di accesso e d'identità
# valgono un'ora, il token di rinnovo 30 giorni: si resta collegati senza rifare il login.
resource "aws_cognito_user_pool_client" "web" {
  name            = "${var.name}-web"
  user_pool_id    = aws_cognito_user_pool.main.id
  generate_secret = false

  explicit_auth_flows           = ["ALLOW_USER_SRP_AUTH", "ALLOW_REFRESH_TOKEN_AUTH"]
  prevent_user_existence_errors = "ENABLED"

  allowed_oauth_flows_user_pool_client = true
  allowed_oauth_flows                  = ["code"]
  allowed_oauth_scopes                 = ["openid", "email", "profile"]
  callback_urls                        = [for o in var.app_origins : "${o}/auth/callback"]
  logout_urls                          = [for o in var.app_origins : "${o}/"]

  supported_identity_providers = concat(
    ["COGNITO"],
    aws_cognito_identity_provider.google[*].provider_name,
    aws_cognito_identity_provider.facebook[*].provider_name,
  )

  access_token_validity  = 1
  id_token_validity      = 1
  refresh_token_validity = 30
  token_validity_units {
    access_token  = "hours"
    id_token      = "hours"
    refresh_token = "days"
  }
}

# Piani a pagamento e ruolo admin: finiscono nel token (claim cognito:groups) e i
# servizi li leggono da lì. Solo un admin o i servizi del backend possono cambiarli.
resource "aws_cognito_user_group" "medium" {
  name         = "medium"
  user_pool_id = aws_cognito_user_pool.main.id
  description  = "Piano Medium: banche dati ufficiali"
  precedence   = 20
}

resource "aws_cognito_user_group" "pro" {
  name         = "pro"
  user_pool_id = aws_cognito_user_pool.main.id
  description  = "Piano Pro: banche dati + AI interattiva"
  precedence   = 10
}

resource "aws_cognito_user_group" "admin" {
  name         = "admin"
  user_pool_id = aws_cognito_user_pool.main.id
  description  = "Amministratori: pannello di controllo e tutte le funzioni"
  precedence   = 1
}
