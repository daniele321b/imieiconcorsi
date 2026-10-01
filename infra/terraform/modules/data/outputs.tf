output "table_arns" {
  value = {
    users     = aws_dynamodb_table.users.arn
    concorsi  = aws_dynamodb_table.concorsi.arn
    follows   = aws_dynamodb_table.follows.arn
    questions = aws_dynamodb_table.questions.arn
    attempts  = aws_dynamodb_table.attempts.arn
  }
}

output "questions_table_name" {
  value = aws_dynamodb_table.questions.name
}

# Variabili d'ambiente delle Lambda, lette da packages/core/src/db.ts
output "table_env" {
  value = {
    USERS_TABLE     = aws_dynamodb_table.users.name
    CONCORSI_TABLE  = aws_dynamodb_table.concorsi.name
    FOLLOWS_TABLE   = aws_dynamodb_table.follows.name
    QUESTIONS_TABLE = aws_dynamodb_table.questions.name
    ATTEMPTS_TABLE  = aws_dynamodb_table.attempts.name
  }
}
