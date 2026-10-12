# SES: mittente delle email dell'app (promemoria scadenze, avvisi admin, in futuro digest bandi).
# Vive in un ambiente a sé (environments/shared) e lo usano sia dev sia prod.
#
# Con il dominio (imieiconcorsi.it) Terraform crea anche i record nella hosted zone:
#   - DKIM (3 CNAME): firma delle email
#   - MAIL FROM mail.<dominio> (MX + SPF): mittente tecnico allineato al dominio
#   - DMARC (_dmarc): policy per i provider di posta (p=none: solo report, per iniziare)
# così la posta arriva in "in arrivo" e non nello spam.

locals {
  con_dominio = var.domain != null
  mail_from   = local.con_dominio ? "mail.${var.domain}" : null
}

data "aws_region" "current" {}

# Indirizzo mittente (senza dominio va verificato cliccando il link che arriva per email).
resource "aws_sesv2_email_identity" "sender" {
  count          = local.con_dominio ? 0 : 1
  email_identity = var.sender_email
}

# Il dominio intero come mittente verificato (con i record DKIM qui sotto).
resource "aws_sesv2_email_identity" "domain" {
  count          = local.con_dominio ? 1 : 0
  email_identity = var.domain
}

# Easy DKIM: SES dà sempre 3 token.
resource "aws_route53_record" "dkim" {
  count   = local.con_dominio ? 3 : 0
  zone_id = var.zone_id
  name    = "${aws_sesv2_email_identity.domain[0].dkim_signing_attributes[0].tokens[count.index]}._domainkey.${var.domain}"
  type    = "CNAME"
  ttl     = 1800
  records = ["${aws_sesv2_email_identity.domain[0].dkim_signing_attributes[0].tokens[count.index]}.dkim.${data.aws_region.current.region}.amazonses.com"]
}

# Mittente tecnico mail.<dominio>: SPF allineato, meno probabilità di finire nello spam.
resource "aws_sesv2_email_identity_mail_from_attributes" "domain" {
  count                  = local.con_dominio ? 1 : 0
  email_identity         = aws_sesv2_email_identity.domain[0].email_identity
  mail_from_domain       = local.mail_from
  behavior_on_mx_failure = "USE_DEFAULT_VALUE"
}

# Dove tornano i rimbalzi del mittente tecnico (server di SES della regione).
resource "aws_route53_record" "mail_from_mx" {
  count   = local.con_dominio ? 1 : 0
  zone_id = var.zone_id
  name    = local.mail_from
  type    = "MX"
  ttl     = 1800
  records = ["10 feedback-smtp.${data.aws_region.current.region}.amazonses.com"]
}

# SPF: SES è autorizzato a spedire per mail.<dominio>.
resource "aws_route53_record" "mail_from_spf" {
  count   = local.con_dominio ? 1 : 0
  zone_id = var.zone_id
  name    = local.mail_from
  type    = "TXT"
  ttl     = 1800
  records = ["v=spf1 include:amazonses.com ~all"]
}

# DMARC: regola per i provider di posta (per ora solo rapporti, nessun blocco).
resource "aws_route53_record" "dmarc" {
  count   = local.con_dominio ? 1 : 0
  zone_id = var.zone_id
  name    = "_dmarc.${var.domain}"
  type    = "TXT"
  ttl     = 1800
  records = [var.dmarc_policy]
}

# Indirizzi da verificare in sandbox per poterli usare come destinatari (es. l'admin, i tester).
resource "aws_sesv2_email_identity" "recipient" {
  for_each       = toset([for e in var.sandbox_recipients : e if e != var.sender_email])
  email_identity = each.value
}

# Soppressione anche a livello di account (tutte le email della regione, non solo quelle con il
# configuration set): un indirizzo che rimbalza o segnala spam non riceve più nulla. AWS lo
# guarda quando valuta l'uscita dalla sandbox.
resource "aws_sesv2_account_suppression_attributes" "account" {
  suppressed_reasons = ["BOUNCE", "COMPLAINT"]
}

# Insieme di regole usato da tutte le email dell'app (nome passato alle Lambda).
resource "aws_sesv2_configuration_set" "main" {
  configuration_set_name = var.name

  reputation_options {
    reputation_metrics_enabled = true
  }

  # Rimbalzi e segnalazioni di spam: SES smette di scrivere a quegli indirizzi.
  suppression_options {
    suppressed_reasons = ["BOUNCE", "COMPLAINT"]
  }

  sending_options {
    sending_enabled = true
  }

  # Le email (ricevute, avvisi) si consegnano solo con TLS: se il server del destinatario non lo
  # supporta, SES non la manda in chiaro (rimbalza e lo vediamo dalle notifiche).
  delivery_options {
    tls_policy = "REQUIRE"
  }
}

# Ogni rimbalzo, segnalazione di spam o invio rifiutato arriva anche per email
# (SES -> SNS -> email): AWS chiede che chi spedisce se ne accorga subito.
data "aws_caller_identity" "current" {}

# Chiave KMS del topic: i messaggi contengono gli indirizzi email che rimbalzano (dati
# personali). Serve una chiave nostra (circa 1 $ al mese): con quella gestita da AWS
# (alias/aws/sns) SES non potrebbe pubblicare.
resource "aws_kms_key" "notifiche" {
  description         = "Cifratura del topic ${var.name}-ses-notifiche"
  enable_key_rotation = true
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "Account"
        Effect    = "Allow"
        Principal = { AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root" }
        Action    = "kms:*"
        Resource  = "*"
      },
      {
        Sid       = "SesPubblica"
        Effect    = "Allow"
        Principal = { Service = "ses.amazonaws.com" }
        Action    = ["kms:GenerateDataKey*", "kms:Decrypt"]
        Resource  = "*"
        Condition = { StringEquals = { "aws:SourceAccount" = data.aws_caller_identity.current.account_id } }
      },
    ]
  })
}

resource "aws_kms_alias" "notifiche" {
  name          = "alias/${var.name}-ses-notifiche"
  target_key_id = aws_kms_key.notifiche.key_id
}

# Topic che riceve rimbalzi e segnalazioni di spam da SES (cifrato).
resource "aws_sns_topic" "notifiche" {
  name              = "${var.name}-ses-notifiche"
  kms_master_key_id = aws_kms_key.notifiche.arn
}

# Solo SES (di questo account) può pubblicare sul topic.
resource "aws_sns_topic_policy" "notifiche" {
  arn = aws_sns_topic.notifiche.arn
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "ses.amazonaws.com" }
      Action    = "sns:Publish"
      Resource  = aws_sns_topic.notifiche.arn
      Condition = {
        StringEquals = {
          "AWS:SourceAccount" = data.aws_caller_identity.current.account_id
          "AWS:SourceArn"     = aws_sesv2_configuration_set.main.arn
        }
      }
    }]
  })
}

# Quali eventi mandare al topic: rimbalzi, spam, invii rifiutati.
resource "aws_sesv2_configuration_set_event_destination" "notifiche" {
  configuration_set_name = aws_sesv2_configuration_set.main.configuration_set_name
  event_destination_name = "rimbalzi-e-reclami"

  event_destination {
    enabled              = true
    matching_event_types = ["BOUNCE", "COMPLAINT", "REJECT"]
    sns_destination {
      topic_arn = aws_sns_topic.notifiche.arn
    }
  }

  depends_on = [aws_sns_topic_policy.notifiche]
}

# Arriva un'email di AWS "Subscription Confirmation": il link va cliccato una volta.
resource "aws_sns_topic_subscription" "notifiche_email" {
  count     = var.notifiche_email == null ? 0 : 1
  topic_arn = aws_sns_topic.notifiche.arn
  protocol  = "email"
  endpoint  = var.notifiche_email
}
