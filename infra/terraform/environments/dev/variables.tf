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

# --- Pubblicità del piano Free: facoltativa. Vuoti = annunci interni sui piani ---
# Con Google AdSense serve anche il banner dei cookie (consenso) prima di attivarlo.

variable "adsense_client" {
  description = "ID editore AdSense, es. ca-pub-1234567890123456"
  type        = string
  default     = ""
}

variable "adsense_slot" {
  description = "ID dell'unità pubblicitaria AdSense"
  type        = string
  default     = ""
}

# --- Pagamenti con Stripe (docs/GUIDA-PAGAMENTI.md). Vuoti = modalità "mock" (gratis) ---

variable "stripe_secret_key" {
  description = "Chiave segreta Stripe: sk_test_... in dev"
  type        = string
  default     = ""
  sensitive   = true
}

variable "stripe_webhook_secret" {
  description = "Segreto di firma dell'endpoint webhook Stripe (whsec_...)"
  type        = string
  default     = ""
  sensitive   = true
}
