# Uscite del modulo Lambda, lette da chi lo usa (moduli api, jobs, contenuti e gli ambienti).

output "function_name" {
  description = "Nome della funzione"
  value       = aws_lambda_function.this.function_name
}

output "arn" {
  description = "ARN della funzione"
  value       = aws_lambda_function.this.arn
}

output "invoke_arn" {
  description = "ARN da usare nelle integrazioni di API Gateway"
  value       = aws_lambda_function.this.invoke_arn
}
