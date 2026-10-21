# Risorse condivise da dev e prod: dominio (hosted zone), SES (mittente email) e posta in arrivo
# per gli indirizzi di contatto (info@ e info-dev@, inoltrati all'admin).
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

# Posta in arrivo (modules/posta-in-arrivo): info@ (prod) e info-dev@ (dev) arrivano all'admin.
# Serve la Lambda compilata: scripts/deploy.sh build lambda prima di scripts/deploy.sh shared.
module "posta" {
  source           = "../../modules/posta-in-arrivo"
  name             = var.project_name
  domain           = var.domain
  zone_id          = data.aws_route53_zone.main.zone_id
  alias            = var.posta_alias
  inoltra_a        = coalesce(var.posta_inoltra_a, var.notifiche_email, try(var.sandbox_recipients[0], null))
  functions_dir    = abspath("${path.root}/../../../../dist/functions")
  ses_identity_arn = one([for a in module.ses.identity_arns : a if endswith(a, "identity/${var.domain}")])

  configuration_set_name = module.ses.configuration_set_name
  configuration_set_arn  = module.ses.configuration_set_arn
}
