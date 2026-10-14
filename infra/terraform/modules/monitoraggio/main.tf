# Monitoraggio: allarmi CloudWatch sulle risorse principali e una dashboard.
# Ogni allarme (e il suo ritorno alla normalità) va sul topic SNS <name>-monitoraggio;
# CloudFront e budget vivono in us-east-1, quindi hanno un secondo topic lì.
#
#   Lambda      errori di ogni funzione, throttling e concorrenza vicina al limite dell'account
#   API Gateway errori 5xx e latenza p95
#   DynamoDB    richieste rifiutate per capacità (throttling) su tutte le tabelle
#   CloudFront  percentuale di errori 5xx del sito
#   SES         reputazione: rimbalzi e segnalazioni di spam (AWS sospende l'invio oltre certe soglie)
#   Job         esecuzioni mancate (lo scraper o le scadenze che non girano)
#   Spesa       budget mensile dell'account (AWS Budgets)

terraform {
  required_providers {
    aws = {
      source                = "hashicorp/aws"
      configuration_aliases = [aws.us_east_1]
    }
  }
}

# Id dell'account, per i permessi dei topic SNS.
data "aws_caller_identity" "current" {}

# Concorrenza Lambda dell'account: sui conti nuovi può essere bassa (anche 10).
data "aws_servicequotas_service_quota" "lambda_concorrenza" {
  service_code = "lambda"
  quota_code   = "L-B99A9384"
}

# Lambda da sorvegliare, destinazioni degli allarmi e soglia di concorrenza (80% della quota).
locals {
  tutte_le_lambda    = merge(var.api_functions, var.job_functions, var.other_functions)
  azioni             = [aws_sns_topic.monitoraggio.arn]
  azioni_us          = [aws_sns_topic.monitoraggio_us.arn]
  soglia_concorrenza = floor(data.aws_servicequotas_service_quota.lambda_concorrenza.value * 0.8)
}

# ── Topic ────────────────────────────────────────────────────────────────────

resource "aws_sns_topic" "monitoraggio" {
  name = "${var.name}-monitoraggio"
}

# Email all'admin per ogni allarme (va confermata cliccando il link di AWS).
resource "aws_sns_topic_subscription" "email" {
  count     = var.email == "" ? 0 : 1
  topic_arn = aws_sns_topic.monitoraggio.arn
  protocol  = "email"
  endpoint  = var.email
}

# Topic gemello in us-east-1, per gli allarmi di CloudFront e il budget.
resource "aws_sns_topic" "monitoraggio_us" {
  provider = aws.us_east_1
  name     = "${var.name}-monitoraggio-us-east-1"
}

# Stessa email anche per il topic di us-east-1.
resource "aws_sns_topic_subscription" "email_us" {
  provider  = aws.us_east_1
  count     = var.email == "" ? 0 : 1
  topic_arn = aws_sns_topic.monitoraggio_us.arn
  protocol  = "email"
  endpoint  = var.email
}

# Il topic di us-east-1 riceve anche dal servizio Budgets: serve un permesso esplicito.
resource "aws_sns_topic_policy" "monitoraggio_us" {
  provider = aws.us_east_1
  arn      = aws_sns_topic.monitoraggio_us.arn
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "Account"
        Effect    = "Allow"
        Principal = { AWS = "*" }
        Action    = ["SNS:Publish", "SNS:Subscribe", "SNS:Receive", "SNS:GetTopicAttributes", "SNS:SetTopicAttributes", "SNS:ListSubscriptionsByTopic"]
        Resource  = aws_sns_topic.monitoraggio_us.arn
        Condition = { StringEquals = { "AWS:SourceOwner" = data.aws_caller_identity.current.account_id } }
      },
      {
        Sid       = "AllarmiEBudget"
        Effect    = "Allow"
        Principal = { Service = ["cloudwatch.amazonaws.com", "budgets.amazonaws.com"] }
        Action    = "SNS:Publish"
        Resource  = aws_sns_topic.monitoraggio_us.arn
        Condition = { StringEquals = { "aws:SourceAccount" = data.aws_caller_identity.current.account_id } }
      },
    ]
  })
}

# ── Lambda ───────────────────────────────────────────────────────────────────

# Le funzioni dell'API trasformano gli errori in risposte 500 (le conta l'allarme 5xx): qui
# finiscono crash e timeout. Per l'API si tollera un caso isolato, per job e trigger nemmeno uno.
resource "aws_cloudwatch_metric_alarm" "lambda_errori" {
  for_each = local.tutte_le_lambda

  alarm_name          = "${var.name}-lambda-${each.key}-errori"
  alarm_description   = "La Lambda ${each.value} è andata in errore (crash o timeout). Log: /aws/lambda/${each.value}"
  namespace           = "AWS/Lambda"
  metric_name         = "Errors"
  dimensions          = { FunctionName = each.value }
  statistic           = "Sum"
  period              = 300
  evaluation_periods  = 1
  threshold           = contains(keys(var.api_functions), each.key) ? 3 : 1
  comparison_operator = "GreaterThanOrEqualToThreshold"
  treat_missing_data  = "notBreaching"
  alarm_actions       = local.azioni
  ok_actions          = local.azioni
}

# Lambda rifiutate per troppe esecuzioni contemporanee.
resource "aws_cloudwatch_metric_alarm" "lambda_throttle" {
  alarm_name          = "${var.name}-lambda-throttle"
  alarm_description   = "Lambda rifiutate per limite di concorrenza dell'account: utenti che vedono errori"
  namespace           = "AWS/Lambda"
  metric_name         = "Throttles"
  statistic           = "Sum"
  period              = 300
  evaluation_periods  = 1
  threshold           = 1
  comparison_operator = "GreaterThanOrEqualToThreshold"
  treat_missing_data  = "notBreaching"
  alarm_actions       = local.azioni
  ok_actions          = local.azioni
}

# Esecuzioni contemporanee oltre l'80% del limite dell'account.
resource "aws_cloudwatch_metric_alarm" "lambda_concorrenza" {
  alarm_name          = "${var.name}-lambda-concorrenza"
  alarm_description   = "Concorrenza Lambda oltre l'80% del limite dell'account (${data.aws_servicequotas_service_quota.lambda_concorrenza.value}): chiedere un aumento in Service Quotas"
  namespace           = "AWS/Lambda"
  metric_name         = "ConcurrentExecutions"
  statistic           = "Maximum"
  period              = 60
  evaluation_periods  = 3
  threshold           = local.soglia_concorrenza
  comparison_operator = "GreaterThanOrEqualToThreshold"
  treat_missing_data  = "notBreaching"
  alarm_actions       = local.azioni
  ok_actions          = local.azioni
}

# ── API Gateway ──────────────────────────────────────────────────────────────

resource "aws_cloudwatch_metric_alarm" "api_5xx" {
  alarm_name          = "${var.name}-api-5xx"
  alarm_description   = "Almeno 5 risposte 5xx dell'API in 5 minuti: errori interni dei servizi"
  namespace           = "AWS/ApiGateway"
  metric_name         = "5xx"
  dimensions          = { ApiId = var.api_id }
  statistic           = "Sum"
  period              = 300
  evaluation_periods  = 1
  threshold           = 5
  comparison_operator = "GreaterThanOrEqualToThreshold"
  treat_missing_data  = "notBreaching"
  alarm_actions       = local.azioni
  ok_actions          = local.azioni
}

# API lenta: il 95% delle richieste oltre la soglia.
resource "aws_cloudwatch_metric_alarm" "api_latenza" {
  alarm_name          = "${var.name}-api-latenza"
  alarm_description   = "Il 5% più lento delle richieste API supera 3 secondi per 15 minuti"
  namespace           = "AWS/ApiGateway"
  metric_name         = "Latency"
  dimensions          = { ApiId = var.api_id }
  extended_statistic  = "p95"
  period              = 300
  evaluation_periods  = 3
  datapoints_to_alarm = 3
  threshold           = 3000
  comparison_operator = "GreaterThanOrEqualToThreshold"
  treat_missing_data  = "notBreaching"
  alarm_actions       = local.azioni
  ok_actions          = local.azioni
}

# ── DynamoDB ─────────────────────────────────────────────────────────────────

# Una richiesta rifiutata su qualsiasi tabella: un allarme somma più tabelle. CloudWatch accetta
# al massimo 10 metriche per allarme, quindi le tabelle vanno a gruppi di 8.
locals {
  gruppi_tabelle = chunklist(sort(keys(var.table_names)), 8)
  allarmi_throttle = merge([
    for tipo, metrica in { lettura = "ReadThrottleEvents", scrittura = "WriteThrottleEvents" } : {
      for i, gruppo in local.gruppi_tabelle : (i == 0 ? tipo : "${tipo}-${i + 1}") => { tipo = tipo, metrica = metrica, tabelle = gruppo }
    }
  ]...)
}

# Un allarme per tipo (lettura/scrittura) e gruppo di tabelle.
resource "aws_cloudwatch_metric_alarm" "dynamodb_throttle" {
  for_each = local.allarmi_throttle

  alarm_name          = "${var.name}-dynamodb-throttle-${each.key}"
  alarm_description   = "Richieste di ${each.value.tipo} rifiutate da DynamoDB (throttling) su una di queste tabelle: ${join(", ", each.value.tabelle)}"
  evaluation_periods  = 1
  threshold           = 1
  comparison_operator = "GreaterThanOrEqualToThreshold"
  treat_missing_data  = "notBreaching"
  alarm_actions       = local.azioni
  ok_actions          = local.azioni

  metric_query {
    id          = "totale"
    expression  = "SUM(METRICS())"
    label       = "Throttling ${each.value.tipo}"
    return_data = true
  }

  dynamic "metric_query" {
    for_each = toset(each.value.tabelle)
    content {
      id = "t_${replace(metric_query.value, "-", "_")}"
      metric {
        namespace   = "AWS/DynamoDB"
        metric_name = each.value.metrica
        dimensions  = { TableName = var.table_names[metric_query.value] }
        period      = 300
        stat        = "Sum"
      }
    }
  }
}

# ── CloudFront (metriche in us-east-1) ───────────────────────────────────────

resource "aws_cloudwatch_metric_alarm" "cloudfront_5xx" {
  provider            = aws.us_east_1
  alarm_name          = "${var.name}-cloudfront-5xx"
  alarm_description   = "Più del 5% delle richieste al sito finisce in errore 5xx per 10 minuti"
  namespace           = "AWS/CloudFront"
  metric_name         = "5xxErrorRate"
  dimensions          = { DistributionId = var.distribution_id, Region = "Global" }
  statistic           = "Average"
  period              = 300
  evaluation_periods  = 2
  datapoints_to_alarm = 2
  threshold           = 5
  comparison_operator = "GreaterThanOrEqualToThreshold"
  treat_missing_data  = "notBreaching"
  alarm_actions       = local.azioni_us
  ok_actions          = local.azioni_us
}

# ── SES: reputazione dell'account ────────────────────────────────────────────

resource "aws_cloudwatch_metric_alarm" "ses" {
  for_each = {
    # AWS mette sotto osservazione oltre il 5% di rimbalzi e lo 0,1% di segnalazioni di spam.
    rimbalzi     = { metrica = "Reputation.BounceRate", soglia = 0.04 }
    segnalazioni = { metrica = "Reputation.ComplaintRate", soglia = 0.0008 }
  }

  alarm_name          = "${var.name}-ses-${each.key}"
  alarm_description   = "Email: percentuale di ${each.key} vicina alla soglia oltre cui AWS sospende l'invio"
  namespace           = "AWS/SES"
  metric_name         = each.value.metrica
  statistic           = "Maximum"
  period              = 3600
  evaluation_periods  = 1
  threshold           = each.value.soglia
  comparison_operator = "GreaterThanOrEqualToThreshold"
  treat_missing_data  = "notBreaching"
  alarm_actions       = local.azioni
  ok_actions          = local.azioni
}

# ── Job: esecuzioni mancate ──────────────────────────────────────────────────

# Nessuna esecuzione per N giorni di fila = lo scheduler o il job sono fermi.
# Dati mancanti contano come "non eseguito": dopo il primo deploy l'allarme può scattare
# finché il job non gira la prima volta (si sblocca subito con scripts/deploy.sh job <nome>).
# I giorni sono "di calendario" (UTC): N deve coprire l'intervallo tra due esecuzioni più
# un giorno, altrimenti l'allarme scatta tra la mezzanotte e l'ora del job.
resource "aws_cloudwatch_metric_alarm" "job_fermo" {
  for_each = var.job_heartbeat

  alarm_name          = "${var.name}-job-${each.key}-fermo"
  alarm_description   = "Il job ${each.key} non gira da ${each.value} giorni"
  namespace           = "AWS/Lambda"
  metric_name         = "Invocations"
  dimensions          = { FunctionName = var.job_functions[each.key] }
  statistic           = "Sum"
  period              = 86400
  evaluation_periods  = each.value
  datapoints_to_alarm = each.value
  threshold           = 1
  comparison_operator = "LessThanThreshold"
  treat_missing_data  = "breaching"
  alarm_actions       = local.azioni
  ok_actions          = local.azioni
}

# ── Spesa ────────────────────────────────────────────────────────────────────

# Budget di tutto l'account (anche le altre app che ci girano): per limitarlo a questo
# progetto vanno prima attivati i tag Project/Environment come cost allocation tag in Billing.
resource "aws_budgets_budget" "mensile" {
  count        = var.budget_mensile_usd > 0 ? 1 : 0
  name         = "${var.name}-account-mensile"
  budget_type  = "COST"
  limit_amount = tostring(var.budget_mensile_usd)
  limit_unit   = "USD"
  time_unit    = "MONTHLY"

  notification {
    comparison_operator       = "GREATER_THAN"
    threshold                 = 80
    threshold_type            = "PERCENTAGE"
    notification_type         = "ACTUAL"
    subscriber_sns_topic_arns = local.azioni_us
  }

  notification {
    comparison_operator       = "GREATER_THAN"
    threshold                 = 100
    threshold_type            = "PERCENTAGE"
    notification_type         = "FORECASTED"
    subscriber_sns_topic_arns = local.azioni_us
  }

  depends_on = [aws_sns_topic_policy.monitoraggio_us]
}
