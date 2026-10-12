variable "name" {
  description = "Prefisso delle risorse (es. imieiconcorsi-dev)"
  type        = string
}

variable "protezione" {
  description = "Prod: le tabelle non si possono cancellare (né con terraform destroy né dalla console) finché non la si spegne"
  type        = bool
  default     = false
}
