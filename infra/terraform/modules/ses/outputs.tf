# Uscite del modulo email (SES), lette da environments/shared.

output "sender_email" {
  description = "Indirizzo mittente"
  value       = var.sender_email
}

output "identity_arns" {
  description = "Identità che le Lambda possono usare per inviare"
  value = concat(
    aws_sesv2_email_identity.sender[*].arn,
    aws_sesv2_email_identity.domain[*].arn,
    [for r in aws_sesv2_email_identity.recipient : r.arn],
  )
}

output "configuration_set_name" {
  description = "Nome del configuration set"
  value       = aws_sesv2_configuration_set.main.configuration_set_name
}

output "configuration_set_arn" {
  description = "ARN del configuration set (per i permessi IAM)"
  value       = aws_sesv2_configuration_set.main.arn
}

output "dkim_records" {
  description = "Record DKIM creati nella hosted zone (vuoto senza dominio)"
  value       = [for r in aws_route53_record.dkim : r.fqdn]
}

output "notifiche_topic_arn" {
  description = "Topic SNS con rimbalzi, reclami e invii rifiutati"
  value       = aws_sns_topic.notifiche.arn
}
