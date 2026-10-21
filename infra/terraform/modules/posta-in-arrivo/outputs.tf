# Uscite del modulo della posta in arrivo.

output "indirizzi" {
  description = "Indirizzi che ricevono e dove arriva la loro posta"
  value       = local.inoltri
}

output "bucket" {
  description = "Bucket con i messaggi ricevuti (copia di riserva)"
  value       = aws_s3_bucket.posta.id
}
