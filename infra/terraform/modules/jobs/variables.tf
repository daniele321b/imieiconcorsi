variable "name" {
  type = string
}

variable "functions_dir" {
  type = string
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
    policies     = optional(any, [])
    environment  = optional(map(string), {})
  }))
}
