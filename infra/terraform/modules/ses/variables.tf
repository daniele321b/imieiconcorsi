variable "name" {
  description = "Nome del configuration set (es. imieiconcorsi)"
  type        = string
}

variable "sender_email" {
  description = "Indirizzo mittente (es. noreply@dominio.it, oppure il tuo indirizzo finché non c'è il dominio)"
  type        = string
}

variable "domain" {
  description = "Dominio da verificare con DKIM. null = si verifica solo sender_email."
  type        = string
  default     = null
}

variable "sandbox_recipients" {
  description = "Destinatari da verificare finché l'account SES è in sandbox"
  type        = list(string)
  default     = []
}
