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
  value = module.jobs.function_names["inpa-scraper"]
}

output "job_functions" {
  value = module.jobs.function_names
}

output "user_pool_id" {
  value = module.auth.user_pool_id
}

output "function_names" {
  value = module.api.function_names
}

# Usato da scripts/deploy.sh local per il sito in locale.
output "web_config" {
  value = local.app_config
}
