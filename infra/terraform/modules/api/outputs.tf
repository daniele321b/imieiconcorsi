output "api_url" {
  description = "Indirizzo diretto dell'API Gateway (il sito usa invece <cloudfront>/api)"
  value       = aws_apigatewayv2_api.main.api_endpoint
}

output "api_domain" {
  value = replace(aws_apigatewayv2_api.main.api_endpoint, "https://", "")
}

output "function_names" {
  value = { for k, m in module.service : k => m.function_name }
}

output "api_id" {
  value = aws_apigatewayv2_api.main.id
}
