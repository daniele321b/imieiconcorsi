# Contenuti dell'app, nello stesso bucket:
#   domande/<materia>.json  banca domande statica: Terraform carica i file e ognuno fa
#                           partire la Lambda che lo importa nella tabella delle domande;
#   banche-dati/<id>.pdf    banche dati ufficiali caricate dal pannello admin: ogni PDF fa
#                           partire l'estrazione delle domande (banche-dati/<id>.json).

# Il bucket (nome con un suffisso casuale: i nomi S3 sono unici nel mondo).
resource "aws_s3_bucket" "contenuti" {
  bucket_prefix = "${var.name}-contenuti-"
  force_destroy = !var.protezione
}

# Cifrato a riposo (SSE-S3, AES-256), anche i PDF caricati dall'admin.
resource "aws_s3_bucket_server_side_encryption_configuration" "contenuti" {
  bucket = aws_s3_bucket.contenuti.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
    bucket_key_enabled = true
  }
}

# Niente di pubblico: lo leggono solo le Lambda con i permessi giusti.
resource "aws_s3_bucket_public_access_block" "contenuti" {
  bucket                  = aws_s3_bucket.contenuti.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Solo connessioni cifrate (HTTPS), per chiunque: anche le Lambda e i caricamenti dell'admin.
resource "aws_s3_bucket_policy" "contenuti" {
  bucket     = aws_s3_bucket.contenuti.id
  depends_on = [aws_s3_bucket_public_access_block.contenuti]
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid       = "SoloHttps"
      Effect    = "Deny"
      Principal = "*"
      Action    = "s3:*"
      Resource  = [aws_s3_bucket.contenuti.arn, "${aws_s3_bucket.contenuti.arn}/*"]
      Condition = { Bool = { "aws:SecureTransport" = "false" } }
    }]
  })
}

# Versioni: un file sovrascritto o cancellato per errore si può recuperare.
resource "aws_s3_bucket_versioning" "contenuti" {
  bucket = aws_s3_bucket.contenuti.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Banche dati eliminate dall'admin o PDF ricopiati per rifare l'estrazione: le versioni
# vecchie restano 30 giorni (per recuperare un errore), poi spariscono.
resource "aws_s3_bucket_lifecycle_configuration" "contenuti" {
  bucket     = aws_s3_bucket.contenuti.id
  depends_on = [aws_s3_bucket_versioning.contenuti]

  rule {
    id     = "banche-dati-versioni-vecchie"
    status = "Enabled"

    filter {
      prefix = "banche-dati/"
    }

    noncurrent_version_expiration {
      noncurrent_days = 30
    }

    expiration {
      expired_object_delete_marker = true
    }
  }
}

# Lambda che importa un file di domande nella tabella questions (functions/src/contenuti).
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

# Permesso a S3 di far partire l'import.
resource "aws_lambda_permission" "s3" {
  statement_id  = "AllowS3"
  action        = "lambda:InvokeFunction"
  function_name = module.import_domande.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.contenuti.arn
}

# Cosa fa partire cosa: un JSON in domande/ → import; un PDF in banche-dati/ → estrazione.
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

# Lambda che estrae le domande da un PDF (functions/src/banche-dati/estrai.ts): fino a 15
# minuti e 3 GB di memoria, per PDF di migliaia di pagine. A fine lavoro scrive all'admin.
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

# Permesso a S3 di far partire l'estrazione.
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
