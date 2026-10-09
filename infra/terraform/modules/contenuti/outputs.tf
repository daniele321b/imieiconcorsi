output "bucket" {
  value = aws_s3_bucket.contenuti.id
}

output "import_function_name" {
  value = module.import_domande.function_name
}

output "bucket_arn" {
  value = aws_s3_bucket.contenuti.arn
}
