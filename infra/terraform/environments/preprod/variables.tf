# Variabili dell'ambiente preprod (valori in terraform.tfvars e da scripts/deploy.sh).
# Le stesse di prod, senza Stripe (preprod paga in "mock") e con quelle dei test di carico in fondo.

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

# --- Tutor AI del piano Pro (Claude su Amazon Bedrock) ---
# Preprod: il tutor resta fuori dai test di carico (costa a risposta); tetti bassi per sicurezza.

variable "ai_model" {
  description = <<-EOT
    Profilo d'inferenza Bedrock del tutor AI. eu. = i dati restano in Europa (lo promette la
    privacy: mai global.). Sonnet 4.6 (~1 cent a risposta) dal 19/10/2026: il profilo EU di
    Haiku 4.5 (~0,3 cent) non rispondeva più. Cambiando modello aggiorna PREZZI_AI_USD.
  EOT
  type        = string
  default     = "eu.anthropic.claude-sonnet-4-6"
}

variable "ai_tetto_utente_usd" {
  description = <<-EOT
    Spesa AI massima al mese per utente, in dollari (stima dai token consumati). Oltre, il tutor
    si ferma per quell'utente fino al mese dopo. Rete di sicurezza oltre ai gettoni: con Sonnet 4.6
    un utente Pro che usa tutti i 150 gettoni spende 1,5-3 dollari, al massimo ~4,5 con chat lunghe;
    5 non lo blocca mai prima di aver finito i gettoni.
  EOT
  type        = number
  default     = 0.5
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
  default     = 5
  validation {
    condition     = var.ai_tetto_mensile_usd > 0
    error_message = "ai_tetto_mensile_usd deve essere maggiore di zero."
  }
}

# --- Monitoraggio ---

variable "budget_mensile_usd" {
  description = "Budget mensile dell'intero account AWS in dollari (avviso all'80% speso e al 100% previsto). 0 = nessun budget (preprod: c'è già quello di dev o prod)"
  type        = number
  default     = 0
}

# --- Sicurezza ---

variable "waf_attivo" {
  description = "WAF davanti a CloudFront (regole gestite AWS + limite di richieste per IP). Circa 8-10 $ al mese."
  type        = bool
  default     = true
}

# --- Test di carico (docs/TEST-DI-CARICO.md) ---

variable "waf_richieste_per_ip" {
  description = <<-EOT
    Richieste massime dallo stesso IP in 5 minuti (in prod 2000). k6 manda le richieste di tutti
    gli utenti finti dallo stesso IP: il limite va alzato, o il WAF bloccherebbe il test stesso.
  EOT
  type        = number
  default     = 1000000
}

variable "waf_richieste_pubbliche_per_ip" {
  description = "Come waf_richieste_per_ip, per le rotte senza login /api/pubblico/ (in prod 100)"
  type        = number
  default     = 100000
}

variable "concorrenza_riservata" {
  description = <<-EOT
    Esecuzioni contemporanee riservate (e massime) per le Lambda dell'API più usate nei test.
    Il limite di 1000 è dell'intero account, comune a dev, prod e preprod: quello che si riserva qui
    manca agli altri ambienti finché preprod esiste (deve restarne almeno 100 libero). Se nel
    test compaiono "Throttles" su una di queste Lambda, il tetto è basso: alzalo e rifai l'apply.
  EOT
  type        = map(number)
  default     = { profile = 100, concorsi = 100, study = 150 }
}
