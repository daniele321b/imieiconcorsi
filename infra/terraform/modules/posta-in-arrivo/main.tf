# Posta in arrivo: gli indirizzi di contatto (info@<dominio> per prod, info-dev@<dominio> per dev)
# non sono caselle vere. SES riceve i messaggi, scarta virus e spam, li salva in un bucket privato
# e una Lambda li inoltra all'admin (packages/functions/src/posta: mittente riscritto sul nostro
# indirizzo, "Rispondi" al mittente vero). Vive in environments/shared: in una regione può essere
# attivo un solo insieme di regole di ricezione SES per account.

# Regione corrente: il server di posta in entrata di SES (record MX).
data "aws_region" "current" {}
# Account corrente: nome unico del bucket e condizione dei permessi di SES.
data "aws_caller_identity" "current" {}

# Alias e cartella dei messaggi, usati da più risorse qui sotto.
locals {
  # Indirizzo completo → dove inoltrarlo (oggi tutti all'admin).
  inoltri = { for a in var.alias : "${a}@${var.domain}" => var.inoltra_a }
  # Cartella del bucket con i messaggi ricevuti (chiave = prefisso + id del messaggio SES).
  prefisso = "in-arrivo/"
}

# La posta per il dominio va ai server di SES della regione (il dominio non ha altre caselle).
resource "aws_route53_record" "mx" {
  zone_id = var.zone_id
  name    = var.domain
  type    = "MX"
  ttl     = 300
  records = ["10 inbound-smtp.${data.aws_region.current.region}.amazonaws.com"]
}

# Messaggi ricevuti, così come sono: privati e cancellati dopo var.giorni_conservazione giorni.
resource "aws_s3_bucket" "posta" {
  bucket = "${var.name}-posta-${data.aws_caller_identity.current.account_id}"
}

# Cifratura dei messaggi salvati (chiavi gestite da S3: SES può scriverci senza permessi KMS).
resource "aws_s3_bucket_server_side_encryption_configuration" "posta" {
  bucket = aws_s3_bucket.posta.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
    bucket_key_enabled = true
  }
}

# Niente accesso pubblico, mai.
resource "aws_s3_bucket_public_access_block" "posta" {
  bucket                  = aws_s3_bucket.posta.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Copia di riserva per qualche settimana (se l'inoltro fallisce il messaggio si ritrova qui), poi via.
resource "aws_s3_bucket_lifecycle_configuration" "posta" {
  bucket = aws_s3_bucket.posta.id
  rule {
    id     = "cancella-messaggi-vecchi"
    status = "Enabled"
    filter {}
    expiration {
      days = var.giorni_conservazione
    }
  }
}

# Solo SES di questo account scrive i messaggi; nessuno legge senza HTTPS.
resource "aws_s3_bucket_policy" "posta" {
  bucket     = aws_s3_bucket.posta.id
  depends_on = [aws_s3_bucket_public_access_block.posta]
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "SesScriveLaPosta"
        Effect    = "Allow"
        Principal = { Service = "ses.amazonaws.com" }
        Action    = "s3:PutObject"
        Resource  = "${aws_s3_bucket.posta.arn}/${local.prefisso}*"
        Condition = { StringEquals = { "AWS:SourceAccount" = data.aws_caller_identity.current.account_id } }
      },
      {
        Sid       = "SoloHttps"
        Effect    = "Deny"
        Principal = "*"
        Action    = "s3:*"
        Resource  = [aws_s3_bucket.posta.arn, "${aws_s3_bucket.posta.arn}/*"]
        Condition = { Bool = { "aws:SecureTransport" = "false" } }
      },
    ]
  })
}

# Lambda che legge il messaggio dal bucket e lo inoltra con SES (packages/functions/src/posta).
module "inoltro" {
  source      = "../lambda"
  name        = "${var.name}-inoltro-posta"
  source_dir  = "${var.functions_dir}/inoltro-posta"
  timeout     = 30
  memory_size = 256
  environment = {
    INOLTRI               = jsonencode(local.inoltri)
    POSTA_BUCKET          = aws_s3_bucket.posta.id
    POSTA_PREFISSO        = local.prefisso
    SES_CONFIGURATION_SET = var.configuration_set_name
  }
  policy_statements = [
    {
      Effect   = "Allow"
      Action   = ["s3:GetObject"]
      Resource = ["${aws_s3_bucket.posta.arn}/${local.prefisso}*"]
    },
    {
      Effect   = "Allow"
      Action   = ["ses:SendEmail", "ses:SendRawEmail"]
      Resource = [var.ses_identity_arn, var.configuration_set_arn]
    },
  ]
}

# SES di questo account può far partire la Lambda.
resource "aws_lambda_permission" "ses" {
  statement_id   = "AllowSES"
  action         = "lambda:InvokeFunction"
  function_name  = module.inoltro.function_name
  principal      = "ses.amazonaws.com"
  source_account = data.aws_caller_identity.current.account_id
}

# Insieme di regole di ricezione, attivo nella regione (uno solo per account e regione).
resource "aws_ses_receipt_rule_set" "posta" {
  rule_set_name = "${var.name}-posta"
}

# Attiva l'insieme di regole qui sopra.
resource "aws_ses_active_receipt_rule_set" "posta" {
  rule_set_name = aws_ses_receipt_rule_set.posta.rule_set_name
}

# Per gli alias: controllo antivirus e antispam, salvataggio nel bucket, poi la Lambda di inoltro.
# Gli altri indirizzi del dominio non hanno una regola: SES rifiuta il messaggio.
resource "aws_ses_receipt_rule" "inoltro" {
  name          = "inoltro-alias"
  rule_set_name = aws_ses_receipt_rule_set.posta.rule_set_name
  recipients    = keys(local.inoltri)
  enabled       = true
  scan_enabled  = true
  tls_policy    = "Optional"

  s3_action {
    bucket_name       = aws_s3_bucket.posta.id
    object_key_prefix = local.prefisso
    position          = 1
  }

  lambda_action {
    function_arn    = module.inoltro.arn
    invocation_type = "Event"
    position        = 2
  }

  depends_on = [aws_s3_bucket_policy.posta, aws_lambda_permission.ses]
}
