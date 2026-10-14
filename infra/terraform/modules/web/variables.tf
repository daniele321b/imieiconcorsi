# Ingressi del modulo sito (CloudFront davanti al bucket S3 e all'API, certificato e DNS).

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

variable "protezione" {
  description = "Prod: il bucket del sito non si svuota da solo con terraform destroy"
  type        = bool
  default     = false
}

variable "csp_connect_src" {
  description = "Indirizzi esterni a cui il sito si collega (Cognito, bucket dei PDF caricati dall'admin): connect-src della CSP"
  type        = list(string)
  default     = []
}

variable "pubblicita_esterna" {
  description = "AdSense attivo: la CSP permette gli script e i frame di Google per gli annunci"
  type        = bool
  default     = false
}

variable "origine_segreta" {
  description = "Segreto che CloudFront aggiunge alle chiamate all'API (intestazione x-origine-cloudfront)"
  type        = string
  sensitive   = true
}
