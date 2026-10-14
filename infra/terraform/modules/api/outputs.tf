# Uscite del modulo API, lette dagli ambienti.

output "api_url" {
  description = "Indirizzo diretto dell'API Gateway (il sito usa invece <cloudfront>/api)"
  value       = aws_apigatewayv2_api.main.api_endpoint
}

output "api_domain" {
  description = "Host dell'API Gateway, origine di CloudFront per /api"
  value       = replace(aws_apigatewayv2_api.main.api_endpoint, "https://", "")
}

output "function_names" {
  description = "Nomi delle Lambda dei servizi"
  value       = { for k, m in module.service : k => m.function_name }
}

output "api_id" {
  description = "Id dell'API (per allarmi e dashboard)"
  value       = aws_apigatewayv2_api.main.id
}
