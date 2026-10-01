variable "name" {
  description = "Nome completo della funzione"
  type        = string
}

variable "source_dir" {
  description = "Cartella con index.mjs prodotto da scripts/build-functions.ts"
  type        = string
}

variable "environment" {
  type    = map(string)
  default = {}
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
  type    = number
  default = 10
}

variable "memory_size" {
  type    = number
  default = 512
}

variable "log_retention_days" {
  type    = number
  default = 14
}

variable "policy_statements" {
  description = "Permessi IAM in più (es. Cognito, SES): lista di { Effect, Action, Resource }"
  type        = any
  default     = []
}
