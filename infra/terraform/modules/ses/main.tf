# SES: mittente delle email dell'app (promemoria scadenze, avvisi admin, in futuro digest bandi).
# Vive in un ambiente a sé (environments/shared) e lo usano sia dev sia prod.
#
# - Senza dominio: si verifica un singolo indirizzo (arriva un'email con il link di conferma).
# - Con un dominio: identità di dominio con DKIM; i record CNAME stanno negli output.
#   Con il dominio la posta finisce in arrivo e non nello spam.

resource "aws_sesv2_email_identity" "sender" {
  count          = var.domain == null ? 1 : 0
  email_identity = var.sender_email
}

resource "aws_sesv2_email_identity" "domain" {
  count          = var.domain == null ? 0 : 1
  email_identity = var.domain
}

# Indirizzi da verificare in sandbox per poterli usare come destinatari (es. l'admin, i tester).
resource "aws_sesv2_email_identity" "recipient" {
  for_each       = toset([for e in var.sandbox_recipients : e if e != var.sender_email])
  email_identity = each.value
}

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
}
