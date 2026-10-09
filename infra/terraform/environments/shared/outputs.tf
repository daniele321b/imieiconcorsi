# Letti dagli ambienti (dev, prod) con terraform_remote_state.

output "domain" {
  value = var.domain
}

output "zone_id" {
  value = data.aws_route53_zone.main.zone_id
}

output "ses_sender_email" {
  value = module.ses.sender_email
}

output "ses_identity_arns" {
  value = module.ses.identity_arns
}

output "ses_configuration_set_name" {
  value = module.ses.configuration_set_name
}

output "ses_configuration_set_arn" {
  value = module.ses.configuration_set_arn
}

output "ses_dkim_records" {
  value = module.ses.dkim_records
}
