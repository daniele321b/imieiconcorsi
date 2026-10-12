variable "name" {
  description = "Prefisso delle risorse; è anche il prefisso del dominio Cognito"
  type        = string
}

variable "aws_region" {
  description = "Regione AWS del user pool"
  type        = string
}

# Interruttore separato dall'ARN: l'ARN di una Lambda nuova è noto solo dopo l'apply,
# mentre count e for_each devono essere noti già nel plan.
variable "pre_sign_up_enabled" {
  description = "Attiva il trigger pre sign-up (collegamento account con la stessa email)"
  type        = bool
  default     = false
}

variable "pre_sign_up_lambda_arn" {
  description = "Lambda del trigger pre sign-up (obbligatoria con pre_sign_up_enabled)"
  type        = string
  default     = null
}

variable "app_origins" {
  description = "Origini del sito ammesse come callback e logout (es. https://xxx.cloudfront.net)"
  type        = list(string)
}

variable "google_client_id" {
  description = "Client id OAuth di Google; vuoto = niente accesso con Google"
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
  description = "App id di Facebook; vuoto = niente accesso con Facebook"
  type        = string
  default     = ""
}

variable "facebook_app_secret" {
  description = "App secret di Facebook"
  type        = string
  default     = ""
  sensitive   = true
}

variable "protezione" {
  description = "Prod: il pool degli utenti non si può cancellare finché non la si spegne"
  type        = bool
  default     = false
}

variable "accessi_enabled" {
  description = "Registra ogni accesso con il trigger pre token generation (serve accessi_lambda_arn)"
  type        = bool
  default     = false
}

variable "accessi_lambda_arn" {
  description = "Lambda che registra ogni accesso (obbligatoria con accessi_enabled)"
  type        = string
  default     = null
}
