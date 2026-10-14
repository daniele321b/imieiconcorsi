# Uscite del modulo contenuti, lette dagli ambienti.

output "bucket" {
  description = "Nome del bucket dei contenuti"
  value       = aws_s3_bucket.contenuti.id
}

output "import_function_name" {
  description = "Lambda che importa le domande dal bucket in DynamoDB"
  value       = module.import_domande.function_name
}

output "bucket_arn" {
  description = "ARN del bucket dei contenuti (per i permessi IAM)"
  value       = aws_s3_bucket.contenuti.arn
}

output "function_names" {
  description = "Nomi delle Lambda del modulo"
  value = {
    import-domande    = module.import_domande.function_name
    estrai-banca-dati = module.estrai_banca_dati.function_name
  }
}
