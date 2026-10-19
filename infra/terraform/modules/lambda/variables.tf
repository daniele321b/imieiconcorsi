# Ingressi del modulo Lambda generica (codice, memoria, variabili d'ambiente, permessi).

variable "name" {
  description = "Nome completo della funzione"
  type        = string
}

variable "source_dir" {
  description = "Cartella con index.mjs prodotto da scripts/build-functions.ts"
  type        = string
}

variable "environment" {
  description = "Variabili d'ambiente della funzione (nomi delle tabelle, email, ecc.)"
  type        = map(string)
  default     = {}
}

variable "write_tables" {
  description = "ARN delle tabelle DynamoDB di cui il servizio è proprietario (lettura e scrittura)"
  type        = list(string)
  default     = []
}

variable "read_tables" {
  description = "ARN delle tabelle di altri servizi, in sola lettura"
  type        = list(string)
  default     = []
}

variable "timeout" {
  description = "Durata massima di un'esecuzione, in secondi"
  type        = number
  default     = 10
}

variable "memory_size" {
  description = "Memoria in MB (anche la CPU cresce con la memoria)"
  type        = number
  default     = 512
}

variable "log_retention_days" {
  description = "Giorni di conservazione dei log"
  type        = number
  default     = 14
}

variable "reserved_concurrency" {
  description = "Esecuzioni contemporanee massime riservate a questa funzione (null = nessun limite proprio)"
  type        = number
  default     = null
}

variable "policy_statements" {
  description = "Permessi IAM in più (es. Cognito, SES): lista di { Effect, Action, Resource }"
  type        = any
  default     = []
}
