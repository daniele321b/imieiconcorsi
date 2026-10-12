variable "aws_region" {
  description = "Regione AWS dell'ambiente (Milano: eu-south-1)"
  type        = string
  default     = "eu-south-1"
}

variable "project_name" {
  description = "Nome del progetto, primo pezzo del nome di ogni risorsa"
  type        = string
  default     = "imieiconcorsi"
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
  description = "Client id OAuth di Google (docs/LOGIN-SOCIAL.md); vuoto = niente accesso con Google"
  type        = string
  default     = ""
}

variable "google_client_secret" {
  description = "Client secret OAuth di Google"
  type        = string
  default     = ""
  sensitive   = true
}

variable "facebook_app_id" {
  description = "App id di Facebook (docs/LOGIN-SOCIAL.md); vuoto = niente accesso con Facebook"
  type        = string
  default     = ""
}

variable "facebook_app_secret" {
  description = "App secret di Facebook"
  type        = string
  default     = ""
  sensitive   = true
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
  description = "Chiave segreta Stripe: sk_live_... in prod (vuota = acquisti chiusi)"
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

# --- Tutor AI del piano Pro (Claude su Amazon Bedrock) ---

variable "ai_model" {
  description = <<-EOT
    Profilo d'inferenza Bedrock del tutor AI. eu. = i dati restano in Europa.
    Haiku 4.5 è il più economico (~0,3 cent a risposta); per risposte più ricche
    si può passare a un modello più grande, a costo maggiore.
  EOT
  type        = string
  default     = "eu.anthropic.claude-haiku-4-5-20251001-v1:0"
}

variable "ai_tetto_utente_usd" {
  description = <<-EOT
    Spesa AI massima al mese per utente, in dollari (stima dai token consumati). Oltre, il tutor
    si ferma per quell'utente fino al mese dopo. Rete di sicurezza oltre ai gettoni: un utente Pro
    che usa tutti i 300 gettoni spende di solito 1-2 dollari.
  EOT
  type        = number
  default     = 3
  validation {
    condition     = var.ai_tetto_utente_usd > 0
    error_message = "ai_tetto_utente_usd deve essere maggiore di zero."
  }
}

variable "ai_tetto_mensile_usd" {
  description = <<-EOT
    Spesa AI massima al mese di tutta la piattaforma, in dollari. All'80% l'admin riceve
    un'email; al 100% tutor e allenamenti AI vanno in pausa per tutti fino al mese dopo.
  EOT
  type        = number
  default     = 50
  validation {
    condition     = var.ai_tetto_mensile_usd > 0
    error_message = "ai_tetto_mensile_usd deve essere maggiore di zero."
  }
}

# --- Monitoraggio ---

variable "budget_mensile_usd" {
  description = "Budget mensile dell'intero account AWS in dollari (avviso all'80% speso e al 100% previsto). 0 = nessun budget"
  type        = number
  default     = 50
}

# --- Sicurezza ---

variable "waf_attivo" {
  description = "WAF davanti a CloudFront (regole gestite AWS + limite di richieste per IP). Circa 8-10 $ al mese."
  type        = bool
  default     = true
}
