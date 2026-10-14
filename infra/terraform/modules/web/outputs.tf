# Uscite del modulo sito, lette dagli ambienti.

output "url" {
  description = "Indirizzo del sito (dominio se c'è, altrimenti CloudFront)"
  value       = local.con_dominio ? "https://${var.domain_name}" : "https://${aws_cloudfront_distribution.web.domain_name}"
}

output "cloudfront_url" {
  description = "Indirizzo CloudFront del sito"
  value       = "https://${aws_cloudfront_distribution.web.domain_name}"
}

output "bucket" {
  description = "Bucket S3 dei file del sito"
  value       = aws_s3_bucket.web.id
}

output "distribution_id" {
  description = "Id della distribuzione CloudFront (per invalidare la cache)"
  value       = aws_cloudfront_distribution.web.id
}
