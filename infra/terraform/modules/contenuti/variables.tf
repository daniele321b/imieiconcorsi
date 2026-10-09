variable "name" {
  type = string
}

variable "functions_dir" {
  type = string
}

variable "domande_dir" {
  description = "Cartella con i file della banca domande (data/domande)"
  type        = string
}

variable "questions_table_arn" {
  type = string
}

variable "environment" {
  description = "Variabili d'ambiente della Lambda di import (nomi delle tabelle)"
  type        = map(string)
  default     = {}
}

variable "banche_dati_table_arn" {
  description = "Tabella delle banche dati ufficiali (stato e riepilogo delle estrazioni)"
  type        = string
}

variable "upload_origins" {
  description = "Siti da cui il pannello admin carica i PDF (CORS del bucket)"
  type        = list(string)
}

variable "email_environment" {
  description = "Variabili per l'avviso all'admin a estrazione finita (SES)"
  type        = map(string)
  default     = {}
}

variable "email_policy_statements" {
  description = "Permessi SES per l'avviso all'admin"
  type        = list(any)
  default     = []
}
