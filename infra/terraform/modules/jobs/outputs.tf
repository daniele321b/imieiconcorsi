output "function_names" {
  value = { for k, m in module.job : k => m.function_name }
}
