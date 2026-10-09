variable "aws_region" {
  description = "Regione AWS delle risorse condivise"
  type        = string
  default     = "eu-south-1"
}

variable "project_name" {
  description = "Nome del progetto, primo pezzo del nome di ogni risorsa"
  type        = string
  default     = "imieiconcorsi"
}

variable "domain" {
  description = "Dominio comprato su Route 53: prod sta sulla radice, dev su dev.<dominio>"
  type        = string
  default     = "imieiconcorsi.it"
}

variable "sender_email" {
  description = "Mittente delle email. null = noreply@<dominio>"
  type        = string
  default     = null
}

variable "sandbox_recipients" {
  description = "Destinatari verificati finché SES è in sandbox (es. l'admin, i tester)"
  type        = list(string)
  default     = []
}

variable "notifiche_email" {
  description = "Email che riceve rimbalzi e reclami SES (vuoto = il primo di sandbox_recipients)"
  type        = string
  default     = null
}
