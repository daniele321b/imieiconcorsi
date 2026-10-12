# WAF davanti a CloudFront (sito e API, stesso indirizzo): solo in prod. Le regole gestite da
# AWS fermano le richieste malevole più comuni (iniezioni, exploit noti, IP con cattiva
# reputazione) e una regola a soglia frena chi manda troppe richieste dallo stesso IP.
# Scope CLOUDFRONT: va creato in us-east-1 (provider aws.us_east_1). Costo indicativo: 5 $ al
# mese per il web ACL, 1 $ per regola e 0,60 $ per milione di richieste.

terraform {
  required_providers {
    aws = { source = "hashicorp/aws", configuration_aliases = [aws.us_east_1] }
  }
}

locals {
  gestite = {
    # Regole di base (OWASP): niente limite di 8 KB sul corpo, le chat del tutor possono superarlo.
    AWSManagedRulesCommonRuleSet = { priorita = 10, eccezioni = ["SizeRestrictions_BODY"] }
    # Richieste con schemi di attacco noti (es. Log4j).
    AWSManagedRulesKnownBadInputsRuleSet = { priorita = 20, eccezioni = [] }
    # IP segnalati da Amazon per attività malevole.
    AWSManagedRulesAmazonIpReputationList = { priorita = 30, eccezioni = [] }
  }
}

resource "aws_wafv2_web_acl" "main" {
  provider    = aws.us_east_1
  name        = var.name
  description = "WAF di ${var.name}: regole gestite AWS e limite di richieste per IP"
  scope       = "CLOUDFRONT"

  default_action {
    allow {}
  }

  # Troppe richieste dallo stesso IP in 5 minuti: blocco temporaneo (riparte da solo).
  rule {
    name     = "limite-per-ip"
    priority = 1
    action {
      block {}
    }
    statement {
      rate_based_statement {
        limit              = var.richieste_per_ip
        aggregate_key_type = "IP"
      }
    }
    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "${var.name}-limite-per-ip"
      sampled_requests_enabled   = true
    }
  }

  dynamic "rule" {
    for_each = local.gestite
    content {
      name     = rule.key
      priority = rule.value.priorita
      override_action {
        none {}
      }
      statement {
        managed_rule_group_statement {
          vendor_name = "AWS"
          name        = rule.key
          # Regole del gruppo che si limitano a contare invece di bloccare.
          dynamic "rule_action_override" {
            for_each = rule.value.eccezioni
            content {
              name = rule_action_override.value
              action_to_use {
                count {}
              }
            }
          }
        }
      }
      visibility_config {
        cloudwatch_metrics_enabled = true
        metric_name                = "${var.name}-${rule.key}"
        sampled_requests_enabled   = true
      }
    }
  }

  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name                = var.name
    sampled_requests_enabled   = true
  }
}
