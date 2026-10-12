variable "name" {
  description = "Prefisso dei nomi delle risorse, es. imieiconcorsi-dev"
  type        = string
}

variable "functions_dir" {
  description = "Cartella con le Lambda impacchettate (dist/functions/<servizio>/index.mjs)"
  type        = string
}

variable "jwt_issuer" {
  description = "Emittente dei token Cognito (indirizzo del user pool), per l'authorizer JWT"
  type        = string
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
    # Secondi; l'API Gateway HTTP aspetta al massimo 30 secondi.
    timeout = optional(number, 10)
    # Permessi IAM in più, come JSON (jsonencode([...])): statement di forme diverse
    # (Resource stringa o lista) non starebbero in un unico tipo Terraform.
    policies = optional(string, "[]")
  }))
}

variable "richieste_al_secondo" {
  description = "Richieste al secondo che l'API accetta in tutto (oltre: 429). 1000 regge circa 1.000 utenti attivi insieme"
  type        = number
  default     = 1000
}

variable "picco_richieste" {
  description = "Picco momentaneo di richieste accettate (burst)"
  type        = number
  default     = 2000
}

variable "write_tables_comuni" {
  description = "Tabelle che tutte le Lambda dell'API possono scrivere (es. attivita: utenti attivi)"
  type        = list(string)
  default     = []
}
