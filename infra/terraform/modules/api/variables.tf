variable "name" {
  type = string
}

variable "functions_dir" {
  description = "Cartella con le Lambda impacchettate (dist/functions/<servizio>/index.mjs)"
  type        = string
}

variable "jwt_issuer" {
  type = string
}

variable "jwt_audience" {
  description = "Client id Cognito del sito"
  type        = string
}

variable "environment" {
  description = "Variabili d'ambiente comuni a tutti i servizi"
  type        = map(string)
  default     = {}
}

variable "services" {
  description = "Microservizi: route, tabelle scrivibili, tabelle in sola lettura, variabili proprie"
  type = map(object({
    routes = list(string)
    # Route senza login (es. disiscrizione da email): il servizio deve proteggerle da sé (firma).
    public_routes = optional(list(string), [])
    write_tables  = list(string)
    read_tables   = list(string)
    environment   = optional(map(string), {})
    # Permessi IAM in più, come JSON (jsonencode([...])): statement di forme diverse
    # (Resource stringa o lista) non starebbero in un unico tipo Terraform.
    policies = optional(string, "[]")
  }))
}
