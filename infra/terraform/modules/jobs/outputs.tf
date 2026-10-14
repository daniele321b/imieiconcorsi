# Uscite del modulo dei lavori pianificati, lette dagli ambienti.

output "function_names" {
  description = "Nomi delle Lambda dei lavori, per lavoro"
  value       = { for k, m in module.job : k => m.function_name }
}
