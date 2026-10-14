# API Gateway HTTP con autenticazione Cognito davanti ai microservizi (una Lambda ciascuno).
# Il browser la raggiunge da CloudFront sotto /api, stesso indirizzo del sito: niente CORS.
#
# Ogni voce di var.services (profile, concorsi, study, billing, ai, richieste, pubblico, admin)
# diventa una Lambda (packages/functions/src/<nome>/handler.ts) con le sue route. Le chiavi
# delle route ("GET /me") devono essere le stesse della mappa in service() del codice.

resource "aws_apigatewayv2_api" "main" {
  name          = var.name
  protocol_type = "HTTP"
}

# Unico stage, pubblicato a ogni modifica. Limite di richieste di tutta l'API (somma di tutti gli
# utenti): var.richieste_al_secondo, con picchi fino a var.picco_richieste. Contro gli abusi del
# singolo ci sono il WAF (per IP, in prod) e i limiti propri (AI, contatti).
resource "aws_apigatewayv2_stage" "default" {
  api_id      = aws_apigatewayv2_api.main.id
  name        = "$default"
  auto_deploy = true

  default_route_settings {
    throttling_burst_limit = var.picco_richieste
    throttling_rate_limit  = var.richieste_al_secondo
  }
}

# Controllo del token: ogni route (tranne le pubbliche) vuole un token valido di Cognito
# nell'intestazione Authorization. Le Lambda ricevono già i dati dell'utente (claims).
resource "aws_apigatewayv2_authorizer" "cognito" {
  api_id           = aws_apigatewayv2_api.main.id
  name             = "cognito"
  authorizer_type  = "JWT"
  identity_sources = ["$request.header.Authorization"]

  jwt_configuration {
    issuer   = var.jwt_issuer
    audience = [var.jwt_audience]
  }
}

# Mappe derivate da var.services, usate per le route qui sotto.
locals {
  # Route → nome del servizio che la gestisce, es. "GET /me" = "profile".
  routes = merge([
    for service, cfg in var.services : { for route in concat(cfg.routes, cfg.public_routes) : route => service }
  ]...)
  # Route senza login (webhook di Stripe, link delle email): si proteggono da sole con una firma.
  public_routes = toset(flatten([for cfg in values(var.services) : cfg.public_routes]))
}

# Una Lambda per servizio.
module "service" {
  source   = "../lambda"
  for_each = var.services

  name              = "${var.name}-${each.key}"
  source_dir        = "${var.functions_dir}/${each.key}"
  environment       = merge(var.environment, each.value.environment)
  write_tables      = concat(each.value.write_tables, var.write_tables_comuni)
  read_tables       = each.value.read_tables
  policy_statements = jsondecode(each.value.policies)
  timeout           = each.value.timeout
}

# Collegamento API → Lambda del servizio (formato evento 2.0).
resource "aws_apigatewayv2_integration" "service" {
  for_each = var.services

  api_id                 = aws_apigatewayv2_api.main.id
  integration_type       = "AWS_PROXY"
  integration_uri        = module.service[each.key].invoke_arn
  payload_format_version = "2.0"
}

# Una route per ogni "METODO /percorso" dichiarato nei servizi.
resource "aws_apigatewayv2_route" "service" {
  for_each = local.routes

  api_id             = aws_apigatewayv2_api.main.id
  route_key          = each.key
  target             = "integrations/${aws_apigatewayv2_integration.service[each.value].id}"
  authorization_type = contains(local.public_routes, each.key) ? "NONE" : "JWT"
  authorizer_id      = contains(local.public_routes, each.key) ? null : aws_apigatewayv2_authorizer.cognito.id
}

# Permesso all'API Gateway di chiamare la Lambda.
resource "aws_lambda_permission" "api" {
  for_each = var.services

  statement_id  = "AllowApiGateway"
  action        = "lambda:InvokeFunction"
  function_name = module.service[each.key].function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.main.execution_arn}/*/*"
}
