# API Gateway HTTP con autenticazione Cognito davanti ai microservizi (una Lambda ciascuno).
# Il browser la raggiunge da CloudFront sotto /api, stesso indirizzo del sito: niente CORS.

resource "aws_apigatewayv2_api" "main" {
  name          = var.name
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_stage" "default" {
  api_id      = aws_apigatewayv2_api.main.id
  name        = "$default"
  auto_deploy = true

  default_route_settings {
    throttling_burst_limit = 100
    throttling_rate_limit  = 50
  }
}

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

locals {
  routes = merge([
    for service, cfg in var.services : { for route in cfg.routes : route => service }
  ]...)
}

module "service" {
  source   = "../lambda"
  for_each = var.services

  name              = "${var.name}-${each.key}"
  source_dir        = "${var.functions_dir}/${each.key}"
  environment       = merge(var.environment, each.value.environment)
  write_tables      = each.value.write_tables
  read_tables       = each.value.read_tables
  policy_statements = each.value.policies
}

resource "aws_apigatewayv2_integration" "service" {
  for_each = var.services

  api_id                 = aws_apigatewayv2_api.main.id
  integration_type       = "AWS_PROXY"
  integration_uri        = module.service[each.key].invoke_arn
  payload_format_version = "2.0"
}

resource "aws_apigatewayv2_route" "service" {
  for_each = local.routes

  api_id             = aws_apigatewayv2_api.main.id
  route_key          = each.key
  target             = "integrations/${aws_apigatewayv2_integration.service[each.value].id}"
  authorization_type = "JWT"
  authorizer_id      = aws_apigatewayv2_authorizer.cognito.id
}

resource "aws_lambda_permission" "api" {
  for_each = var.services

  statement_id  = "AllowApiGateway"
  action        = "lambda:InvokeFunction"
  function_name = module.service[each.key].function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.main.execution_arn}/*/*"
}
