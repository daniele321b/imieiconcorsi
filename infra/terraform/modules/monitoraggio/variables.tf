variable "name" {
  description = "Prefisso delle risorse, es. imieiconcorsi-dev"
  type        = string
}

variable "aws_region" {
  description = "Regione dell'app (le metriche di CloudFront e il budget stanno invece in us-east-1)"
  type        = string
}

variable "email" {
  description = "Chi riceve gli allarmi (iscrizione email al topic: va confermata dal link di AWS). Vuoto = nessuna iscrizione"
  type        = string
  default     = ""
}

variable "api_id" {
  description = "Id dell'API Gateway HTTP"
  type        = string
}

variable "api_functions" {
  description = "Lambda dei microservizi dietro l'API: chiave -> nome della funzione"
  type        = map(string)
}

variable "job_functions" {
  description = "Lambda dei job pianificati: chiave -> nome della funzione"
  type        = map(string)
}

variable "other_functions" {
  description = "Altre Lambda (import domande, estrazione banche dati, trigger di Cognito)"
  type        = map(string)
  default     = {}
}

variable "job_heartbeat" {
  description = "Job che devono girare: chiave (come in job_functions) -> giorni massimi senza esecuzioni (1-7)"
  type        = map(number)
  default     = {}

  # CloudWatch non guarda indietro più di una settimana con periodi di un giorno.
  validation {
    condition     = alltrue([for giorni in values(var.job_heartbeat) : giorni >= 1 && giorni <= 7 && floor(giorni) == giorni])
    error_message = "I giorni di job_heartbeat vanno da 1 a 7 (limite di CloudWatch: una settimana)."
  }
}

variable "table_names" {
  description = "Tabelle DynamoDB: chiave -> nome"
  type        = map(string)
}

variable "distribution_id" {
  description = "Distribuzione CloudFront del sito"
  type        = string
}

variable "ai_model" {
  description = "Profilo d'inferenza Bedrock del tutor AI (per i grafici dei token)"
  type        = string
  default     = ""
}

variable "budget_mensile_usd" {
  description = "Budget mensile di TUTTO l'account AWS in dollari: avviso all'80% speso e al 100% previsto. 0 = nessun budget"
  type        = number
  default     = 50
}
