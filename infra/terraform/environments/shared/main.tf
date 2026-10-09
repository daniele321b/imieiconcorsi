# Risorse condivise da dev e prod: dominio (hosted zone) e SES (mittente email).
# Si crea una volta (scripts/deploy.sh shared) e NON si distrugge con gli ambienti.

# La hosted zone l'ha creata Route 53 all'acquisto del dominio: qui si legge soltanto.
data "aws_route53_zone" "main" {
  name         = var.domain
  private_zone = false
}

# Mittente delle email (modules/ses), usato da tutti gli ambienti.
module "ses" {
  source             = "../../modules/ses"
  name               = var.project_name
  domain             = var.domain
  zone_id            = data.aws_route53_zone.main.zone_id
  sender_email       = coalesce(var.sender_email, "noreply@${var.domain}")
  sandbox_recipients = var.sandbox_recipients
  # Senza un indirizzo dedicato le notifiche vanno al primo destinatario della sandbox (di solito l'admin).
  notifiche_email = try(coalesce(var.notifiche_email, var.sandbox_recipients[0]), null)
}
