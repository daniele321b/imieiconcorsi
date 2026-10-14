# Uscite del modulo login, lette dagli ambienti.

output "user_pool_id" {
  description = "Id dello user pool"
  value       = aws_cognito_user_pool.main.id
}

output "client_id" {
  description = "Id del client web (usato dal sito)"
  value       = aws_cognito_user_pool_client.web.id
}

output "issuer" {
  description = "Emittente dei token, per l'authorizer JWT dell'API"
  value       = "https://cognito-idp.${var.aws_region}.amazonaws.com/${aws_cognito_user_pool.main.id}"
}

output "domain" {
  description = "Host del login social (senza https://)"
  value       = "${aws_cognito_user_pool_domain.main.domain}.auth.${var.aws_region}.amazoncognito.com"
}

output "idp_redirect_uri" {
  description = "Da registrare su Google e Facebook come URI di reindirizzamento"
  value       = "https://${aws_cognito_user_pool_domain.main.domain}.auth.${var.aws_region}.amazoncognito.com/oauth2/idpresponse"
}

output "social_providers" {
  description = "Login social attivi (google, facebook)"
  value       = concat(local.google_enabled ? ["google"] : [], local.facebook_enabled ? ["facebook"] : [])
}

output "user_pool_arn" {
  description = "ARN dello user pool (per i permessi IAM)"
  value       = aws_cognito_user_pool.main.arn
}
