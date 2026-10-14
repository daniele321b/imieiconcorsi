# Letti dagli ambienti (dev, prod) con terraform_remote_state.

output "domain" {
  description = "Dominio del sito (es. imieiconcorsi.it)"
  value       = var.domain
}

output "zone_id" {
  description = "Hosted zone Route 53 del dominio"
  value       = data.aws_route53_zone.main.zone_id
}

output "ses_sender_email" {
  description = "Indirizzo mittente delle email"
  value       = module.ses.sender_email
}

output "ses_identity_arns" {
  description = "Identità SES con cui le Lambda possono inviare"
  value       = module.ses.identity_arns
}

output "ses_configuration_set_name" {
  description = "Configuration set SES (rimbalzi e reclami)"
  value       = module.ses.configuration_set_name
}

output "ses_configuration_set_arn" {
  description = "ARN del configuration set SES"
  value       = module.ses.configuration_set_arn
}

output "ses_dkim_records" {
  description = "Record DKIM creati nella hosted zone"
  value       = module.ses.dkim_records
}
