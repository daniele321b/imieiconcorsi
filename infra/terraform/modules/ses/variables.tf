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

variable "zone_id" {
  description = "Hosted zone Route 53 del dominio (obbligatoria con domain)"
  type        = string
  default     = null
}

variable "dmarc_policy" {
  description = "Record DMARC. Si parte con p=none (solo osservazione), poi quarantine/reject."
  type        = string
  default     = "v=DMARC1; p=none; adkim=r; aspf=r"
}

variable "sandbox_recipients" {
  description = "Destinatari da verificare finché l'account SES è in sandbox"
  type        = list(string)
  default     = []
}

variable "notifiche_email" {
  description = "Dove arrivano le notifiche di rimbalzi e reclami SES. null = solo sul topic SNS."
  type        = string
  default     = null
}
