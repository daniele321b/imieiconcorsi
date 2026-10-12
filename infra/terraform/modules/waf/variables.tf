variable "name" {
  description = "Nome del web ACL, es. imieiconcorsi-prod"
  type        = string
}

variable "richieste_per_ip" {
  description = "Richieste massime dallo stesso IP in 5 minuti prima del blocco temporaneo"
  type        = number
  default     = 2000
}

variable "richieste_pubbliche_per_ip" {
  description = "Richieste massime dallo stesso IP in 5 minuti sulle rotte senza login (/api/pubblico/)"
  type        = number
  default     = 100
}
