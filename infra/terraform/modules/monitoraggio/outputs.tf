# Uscite del modulo monitoraggio, lette dagli ambienti.

output "topic_arn" {
  description = "Topic SNS degli allarmi (regione dell'ambiente)"
  value       = aws_sns_topic.monitoraggio.arn
}

output "topic_us_east_1_arn" {
  description = "Topic SNS degli allarmi di CloudFront e del budget (us-east-1)"
  value       = aws_sns_topic.monitoraggio_us.arn
}

output "dashboard_url" {
  description = "Indirizzo della dashboard CloudWatch"
  value       = "https://${var.aws_region}.console.aws.amazon.com/cloudwatch/home?region=${var.aws_region}#dashboards/dashboard/${aws_cloudwatch_dashboard.main.dashboard_name}"
}
