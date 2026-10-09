variable "name" {
  description = "Prefisso dei nomi delle risorse, es. imieiconcorsi-dev"
  type        = string
}

variable "functions_dir" {
  description = "Cartella delle Lambda compilate (dist/functions)"
  type        = string
}

variable "environment" {
  description = "Variabili d'ambiente comuni a tutti i job"
  type        = map(string)
  default     = {}
}

variable "jobs" {
  description = "Job: orario (cron, ora italiana), permessi e variabili propri"
  type = map(object({
    description  = string
    schedule     = string
    timeout      = optional(number, 300)
    write_tables = optional(list(string), [])
    read_tables  = optional(list(string), [])
    # Permessi IAM in più, come JSON (jsonencode([...])): statement di forme diverse
    # (Resource stringa o lista) non starebbero in un unico tipo Terraform.
    policies    = optional(string, "[]")
    environment = optional(map(string), {})
  }))
}
