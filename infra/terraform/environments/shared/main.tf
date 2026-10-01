# Risorse condivise da dev e prod. Oggi: SES (mittente email).
# Si crea una volta (scripts/deploy.sh shared) e NON si distrugge con gli ambienti.

module "ses" {
  source             = "../../modules/ses"
  name               = var.project_name
  sender_email       = var.sender_email
  domain             = var.domain
  sandbox_recipients = var.sandbox_recipients
}
