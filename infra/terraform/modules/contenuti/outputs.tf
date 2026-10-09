output "bucket" {
  value = aws_s3_bucket.contenuti.id
}

output "import_function_name" {
  value = module.import_domande.function_name
}

output "bucket_arn" {
  value = aws_s3_bucket.contenuti.arn
}

output "function_names" {
  value = {
    import-domande    = module.import_domande.function_name
    estrai-banca-dati = module.estrai_banca_dati.function_name
  }
}
