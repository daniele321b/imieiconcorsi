variable "aws_region" {
  type    = string
  default = "eu-south-1"
}

variable "project_name" {
  type    = string
  default = "imieiconcorsi"
}

variable "sender_email" {
  description = "Mittente delle email (in terraform.tfvars)"
  type        = string
}

variable "domain" {
  description = "Dominio per SES con DKIM, quando ci sarà. null = solo sender_email."
  type        = string
  default     = null
}

variable "sandbox_recipients" {
  description = "Destinatari verificati finché SES è in sandbox (es. l'admin, i tester)"
  type        = list(string)
  default     = []
}
