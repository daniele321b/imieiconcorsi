# Dashboard <name>: le metriche normali delle risorse principali, a colpo d'occhio.

locals {
  grafico = { width = 12, height = 6 }

  grafici = concat(
    [
      {
        title   = "API: richieste ed errori (somma ogni 5 minuti)"
        stat    = "Sum"
        metrics = [for m in ["Count", "4xx", "5xx"] : ["AWS/ApiGateway", m, "ApiId", var.api_id, { label = m == "Count" ? "richieste" : m }]]
      },
      {
        title = "API: latenza (ms)"
        stat  = "p95"
        metrics = [
          ["AWS/ApiGateway", "Latency", "ApiId", var.api_id, { stat = "p50", label = "mediana" }],
          ["AWS/ApiGateway", "Latency", "ApiId", var.api_id, { stat = "p95", label = "p95" }],
        ]
      },
      {
        title   = "Lambda: errori (crash e timeout) per funzione"
        stat    = "Sum"
        metrics = [for k, f in local.tutte_le_lambda : ["AWS/Lambda", "Errors", "FunctionName", f, { label = k }]]
      },
      {
        title   = "Lambda dell'API: durata p95 (ms)"
        stat    = "p95"
        metrics = [for k, f in var.api_functions : ["AWS/Lambda", "Duration", "FunctionName", f, { label = k }]]
      },
      {
        title = "Lambda: concorrenza e throttling (account)"
        stat  = "Maximum"
        metrics = [
          ["AWS/Lambda", "ConcurrentExecutions", { label = "concorrenza massima" }],
          ["AWS/Lambda", "Throttles", { stat = "Sum", label = "rifiutate", yAxis = "right" }],
        ]
        annotations = { horizontal = [{ label = "80% del limite", value = local.soglia_concorrenza }] }
      },
      {
        title   = "Job pianificati: esecuzioni al giorno"
        stat    = "Sum"
        period  = 86400
        metrics = [for k, f in var.job_functions : ["AWS/Lambda", "Invocations", "FunctionName", f, { label = k }]]
      },
      {
        title   = "DynamoDB: capacità letta (unità ogni 5 minuti)"
        stat    = "Sum"
        metrics = [for k, t in var.table_names : ["AWS/DynamoDB", "ConsumedReadCapacityUnits", "TableName", t, { label = k }]]
      },
      {
        title   = "DynamoDB: capacità scritta (unità ogni 5 minuti)"
        stat    = "Sum"
        metrics = [for k, t in var.table_names : ["AWS/DynamoDB", "ConsumedWriteCapacityUnits", "TableName", t, { label = k }]]
      },
      {
        title  = "CloudFront: richieste e % di errori"
        region = "us-east-1"
        stat   = "Sum"
        metrics = [
          ["AWS/CloudFront", "Requests", "DistributionId", var.distribution_id, "Region", "Global", { label = "richieste" }],
          ["AWS/CloudFront", "4xxErrorRate", "DistributionId", var.distribution_id, "Region", "Global", { stat = "Average", label = "% 4xx", yAxis = "right" }],
          ["AWS/CloudFront", "5xxErrorRate", "DistributionId", var.distribution_id, "Region", "Global", { stat = "Average", label = "% 5xx", yAxis = "right" }],
        ]
      },
      {
        title  = "Email (SES): inviate, rimbalzi, segnalazioni"
        stat   = "Sum"
        period = 3600
        metrics = [
          ["AWS/SES", "Send", { label = "inviate" }],
          ["AWS/SES", "Bounce", { label = "rimbalzi" }],
          ["AWS/SES", "Complaint", { label = "segnalazioni di spam" }],
        ]
      },
    ],
    var.ai_model == "" ? [] : [
      {
        title  = "Tutor AI (Bedrock): token all'ora"
        stat   = "Sum"
        period = 3600
        metrics = [
          ["AWS/Bedrock", "InputTokenCount", "ModelId", var.ai_model, { label = "token in ingresso" }],
          ["AWS/Bedrock", "OutputTokenCount", "ModelId", var.ai_model, { label = "token in uscita" }],
        ]
      },
    ],
  )

  allarmi_regione = concat(
    [for a in aws_cloudwatch_metric_alarm.lambda_errori : a.arn],
    [aws_cloudwatch_metric_alarm.lambda_throttle.arn, aws_cloudwatch_metric_alarm.lambda_concorrenza.arn],
    [aws_cloudwatch_metric_alarm.api_5xx.arn, aws_cloudwatch_metric_alarm.api_latenza.arn],
    [for a in aws_cloudwatch_metric_alarm.dynamodb_throttle : a.arn],
    [for a in aws_cloudwatch_metric_alarm.ses : a.arn],
    [for a in aws_cloudwatch_metric_alarm.job_fermo : a.arn],
  )

  # Stato degli allarmi in cima, poi i grafici due per riga.
  widget_allarmi = {
    type   = "alarm"
    x      = 0
    y      = 0
    width  = 24
    height = 4
    properties = {
      title  = "Allarmi (CloudFront e budget sono in us-east-1)"
      alarms = local.allarmi_regione
    }
  }

  widget_grafici = [
    for i, g in local.grafici : {
      type   = "metric"
      x      = (i % 2) * local.grafico.width
      y      = 4 + floor(i / 2) * local.grafico.height
      width  = local.grafico.width
      height = local.grafico.height
      properties = merge(
        {
          title   = g.title
          region  = lookup(g, "region", var.aws_region)
          view    = "timeSeries"
          stacked = false
          stat    = g.stat
          period  = lookup(g, "period", 300)
          metrics = g.metrics
        },
        contains(keys(g), "annotations") ? { annotations = g.annotations } : {},
      )
    }
  ]
}

# La dashboard (link nell'output dashboard_url).
resource "aws_cloudwatch_dashboard" "main" {
  dashboard_name = var.name
  dashboard_body = jsonencode({ widgets = concat([local.widget_allarmi], local.widget_grafici) })
}
