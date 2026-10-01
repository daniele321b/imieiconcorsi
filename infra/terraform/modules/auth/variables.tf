variable "name" {
  description = "Prefisso delle risorse; è anche il prefisso del dominio Cognito"
  type        = string
}

variable "aws_region" {
  type = string
}

variable "app_origins" {
  description = "Origini del sito ammesse come callback e logout (es. https://xxx.cloudfront.net)"
  type        = list(string)
}

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
