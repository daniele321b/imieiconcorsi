# Ingressi del modulo della posta in arrivo (alias del dominio inoltrati all'admin).

variable "name" {
  description = "Prefisso dei nomi delle risorse, es. imieiconcorsi"
  type        = string
}

variable "domain" {
  description = "Dominio che riceve la posta, es. imieiconcorsi.it"
  type        = string
}

variable "zone_id" {
  description = "Hosted zone Route 53 del dominio (per il record MX)"
  type        = string
}

variable "alias" {
  description = "Parti prima della @ degli indirizzi che ricevono, es. [\"info\", \"info-dev\"]"
  type        = list(string)
}

variable "inoltra_a" {
  description = "Indirizzo dell'admin a cui arriva la posta degli alias"
  type        = string
}

variable "functions_dir" {
  description = "Cartella delle Lambda compilate (dist/functions): serve inoltro-posta"
  type        = string
}

variable "ses_identity_arn" {
  description = "ARN dell'identità SES del dominio, da cui parte l'inoltro"
  type        = string
}

variable "configuration_set_name" {
  description = "Configuration set SES dell'inoltro (rimbalzi e reclami)"
  type        = string
}

variable "configuration_set_arn" {
  description = "ARN del configuration set qui sopra (per il permesso di invio)"
  type        = string
}

variable "giorni_conservazione" {
  description = "Giorni per cui i messaggi ricevuti restano nel bucket come copia di riserva"
  type        = number
  default     = 30
}
