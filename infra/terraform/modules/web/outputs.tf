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

output "manutenzione_kvs_arn" {
  description = "ARN della KeyValueStore della manutenzione (scripts/deploy.sh manutenzione)"
  value       = aws_cloudfront_key_value_store.manutenzione.arn
}
