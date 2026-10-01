variable "aws_region" {
  type    = string
  default = "eu-south-1"
}

variable "project_name" {
  type    = string
  default = "imieiconcorsi"
}

variable "state_bucket" {
  description = "Bucket dello stato Terraform, per leggere l'ambiente shared (lo passa scripts/deploy.sh)"
  type        = string
}

variable "admin_email" {
  description = "Dove arrivano gli avvisi per l'admin (es. nuovi bandi con banca dati). In sandbox SES deve essere verificato."
  type        = string
  default     = ""
}

# --- Login social: facoltativi. Vuoti = solo email e password ---
# Vanno in terraform.tfvars (non versionato).

variable "google_client_id" {
  type    = string
  default = ""
}

variable "google_client_secret" {
  type      = string
  default   = ""
  sensitive = true
}

variable "facebook_app_id" {
  type    = string
  default = ""
}

variable "facebook_app_secret" {
  type      = string
  default   = ""
  sensitive = true
}
