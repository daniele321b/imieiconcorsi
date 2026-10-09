variable "name" {
  description = "Prefisso dei nomi delle risorse, es. imieiconcorsi-dev"
  type        = string
}

variable "dist_dir" {
  description = "Build del frontend (packages/web/dist)"
  type        = string
}

variable "app_config" {
  description = "Contenuto di /config.json, letto dal browser all'avvio (URL API, id Cognito…)"
  type        = any
}

variable "api_domain" {
  description = "Host dell'API Gateway (senza https://), servito sotto /api"
  type        = string
}

variable "web_acl_arn" {
  description = "ARN del WAF (scope CLOUDFRONT, in us-east-1). null in dev: nessun WAF."
  type        = string
  default     = null
}

variable "domain_name" {
  description = "Dominio del sito (es. dev.imieiconcorsi.it). null = indirizzo *.cloudfront.net."
  type        = string
  default     = null
}

variable "zone_id" {
  description = "Hosted zone Route 53 del dominio (obbligatoria con domain_name)"
  type        = string
  default     = null
}
