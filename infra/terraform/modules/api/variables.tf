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
    routes       = list(string)
    write_tables = list(string)
    read_tables  = list(string)
    environment  = optional(map(string), {})
    policies     = optional(any, [])
  }))
}
