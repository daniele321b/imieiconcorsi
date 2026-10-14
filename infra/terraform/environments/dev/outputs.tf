# Valori dell'ambiente dev stampati da terraform output e letti da scripts/deploy.sh.

output "web_url" {
  description = "Il sito"
  value       = module.web.url
}

output "api_url" {
  description = "L'API come la usa il sito"
  value       = "${module.web.url}/api"
}

output "api_gateway_url" {
  description = "API Gateway diretto, per debug"
  value       = module.api.api_url
}

output "cognito_idp_redirect_uri" {
  description = "URI di reindirizzamento da registrare su Google e Facebook"
  value       = module.auth.idp_redirect_uri
}

output "inpa_scraper_function" {
  description = "Lambda che scarica i bandi da inPA (per avviarla a mano)"
  value       = module.jobs.function_names["inpa-scraper"]
}

output "job_functions" {
  description = "Nomi delle Lambda dei lavori pianificati"
  value       = module.jobs.function_names
}

output "user_pool_id" {
  description = "Id dello user pool Cognito"
  value       = module.auth.user_pool_id
}

output "function_names" {
  description = "Nomi delle Lambda dell'API, per servizio"
  value       = module.api.function_names
}

# Usato da scripts/deploy.sh local per il sito in locale.
output "web_config" {
  description = "Configurazione del sito (API, Cognito, login social)"
  value       = local.app_config
}

output "contenuti_bucket" {
  description = "Bucket S3 dei contenuti (banca domande, PDF delle banche dati)"
  value       = module.contenuti.bucket
}

output "monitoraggio_topic_arn" {
  description = "Topic SNS degli allarmi"
  value       = module.monitoraggio.topic_arn
}

output "dashboard_url" {
  description = "Dashboard CloudWatch dell'ambiente"
  value       = module.monitoraggio.dashboard_url
}
