# Contenuti dell'app, nello stesso bucket:
#   domande/<materia>.json  banca domande statica: Terraform carica i file e ognuno fa
#                           partire la Lambda che lo importa nella tabella delle domande;
#   banche-dati/<id>.pdf    banche dati ufficiali caricate dal pannello admin: ogni PDF fa
#                           partire l'estrazione delle domande (banche-dati/<id>.json).

resource "aws_s3_bucket" "contenuti" {
  bucket_prefix = "${var.name}-contenuti-"
  force_destroy = true
}

resource "aws_s3_bucket_public_access_block" "contenuti" {
  bucket                  = aws_s3_bucket.contenuti.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "contenuti" {
  bucket = aws_s3_bucket.contenuti.id
  versioning_configuration {
    status = "Enabled"
  }
}

module "import_domande" {
  source       = "../lambda"
  name         = "${var.name}-import-domande"
  source_dir   = "${var.functions_dir}/import-domande"
  timeout      = 300
  environment  = merge(var.environment, { CONTENUTI_BUCKET = aws_s3_bucket.contenuti.id })
  write_tables = [var.questions_table_arn]
  policy_statements = [{
    Effect   = "Allow"
    Action   = ["s3:GetObject", "s3:ListBucket"]
    Resource = [aws_s3_bucket.contenuti.arn, "${aws_s3_bucket.contenuti.arn}/*"]
  }]
}

resource "aws_lambda_permission" "s3" {
  statement_id  = "AllowS3"
  action        = "lambda:InvokeFunction"
  function_name = module.import_domande.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.contenuti.arn
}

resource "aws_s3_bucket_notification" "domande" {
  bucket = aws_s3_bucket.contenuti.id

  lambda_function {
    lambda_function_arn = module.import_domande.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = "domande/"
    filter_suffix       = ".json"
  }

  lambda_function {
    lambda_function_arn = module.estrai_banca_dati.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = "banche-dati/"
    filter_suffix       = ".pdf"
  }

  depends_on = [aws_lambda_permission.s3, aws_lambda_permission.s3_banche_dati]
}

# --- Banche dati ufficiali ---------------------------------------------------

# Il pannello admin carica il PDF direttamente sul bucket (link firmato): serve il CORS.
resource "aws_s3_bucket_cors_configuration" "contenuti" {
  bucket = aws_s3_bucket.contenuti.id

  cors_rule {
    allowed_methods = ["PUT"]
    allowed_origins = var.upload_origins
    allowed_headers = ["content-type"]
    max_age_seconds = 3000
  }
}

module "estrai_banca_dati" {
  source       = "../lambda"
  name         = "${var.name}-estrai-banca-dati"
  source_dir   = "${var.functions_dir}/estrai-banca-dati"
  timeout      = 900
  memory_size  = 3008
  environment  = merge(var.environment, var.email_environment, { CONTENUTI_BUCKET = aws_s3_bucket.contenuti.id })
  write_tables = [var.banche_dati_table_arn]
  policy_statements = concat([{
    Effect   = "Allow"
    Action   = ["s3:GetObject", "s3:PutObject"]
    Resource = "${aws_s3_bucket.contenuti.arn}/banche-dati/*"
  }], var.email_policy_statements)
}

resource "aws_lambda_permission" "s3_banche_dati" {
  statement_id  = "AllowS3"
  action        = "lambda:InvokeFunction"
  function_name = module.estrai_banca_dati.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.contenuti.arn
}

# Un oggetto per materia; cambia solo se cambia il file (etag = md5).
resource "aws_s3_object" "domande" {
  for_each = fileset(var.domande_dir, "*.json")

  bucket       = aws_s3_bucket.contenuti.id
  key          = "domande/${each.value}"
  source       = "${var.domande_dir}/${each.value}"
  etag         = filemd5("${var.domande_dir}/${each.value}")
  content_type = "application/json"

  # Prima la notifica, poi i file: altrimenti il primo caricamento non verrebbe importato.
  depends_on = [aws_s3_bucket_notification.domande]
}
