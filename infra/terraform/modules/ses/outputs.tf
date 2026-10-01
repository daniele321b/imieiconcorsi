output "sender_email" {
  value = var.sender_email
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
  value = aws_sesv2_configuration_set.main.configuration_set_name
}

output "configuration_set_arn" {
  value = aws_sesv2_configuration_set.main.arn
}

output "dkim_records" {
  description = "Record CNAME da creare nel DNS del dominio (vuoto senza dominio)"
  value = [
    for t in try(aws_sesv2_email_identity.domain[0].dkim_signing_attributes[0].tokens, []) : {
      name  = "${t}._domainkey.${var.domain}"
      type  = "CNAME"
      value = "${t}.dkim.amazonses.com"
    }
  ]
}
