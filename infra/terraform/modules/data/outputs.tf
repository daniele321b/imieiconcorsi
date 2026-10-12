output "table_arns" {
  value = {
    users     = aws_dynamodb_table.users.arn
    concorsi  = aws_dynamodb_table.concorsi.arn
    follows   = aws_dynamodb_table.follows.arn
    questions = aws_dynamodb_table.questions.arn
    attempts  = aws_dynamodb_table.attempts.arn
    codici    = aws_dynamodb_table.codici.arn
    ordini    = aws_dynamodb_table.ordini.arn
    banche    = aws_dynamodb_table.banche_dati.arn
    richieste = aws_dynamodb_table.richieste.arn
    progressi = aws_dynamodb_table.progressi.arn
    contatori = aws_dynamodb_table.contatori.arn
    accessi   = aws_dynamodb_table.accessi.arn
  }
}

output "questions_table_name" {
  value = aws_dynamodb_table.questions.name
}

# Variabili d'ambiente delle Lambda, lette da packages/core/src/db.ts
output "table_env" {
  value = {
    USERS_TABLE       = aws_dynamodb_table.users.name
    CONCORSI_TABLE    = aws_dynamodb_table.concorsi.name
    FOLLOWS_TABLE     = aws_dynamodb_table.follows.name
    QUESTIONS_TABLE   = aws_dynamodb_table.questions.name
    ATTEMPTS_TABLE    = aws_dynamodb_table.attempts.name
    CODICI_TABLE      = aws_dynamodb_table.codici.name
    ORDINI_TABLE      = aws_dynamodb_table.ordini.name
    BANCHE_DATI_TABLE = aws_dynamodb_table.banche_dati.name
    RICHIESTE_TABLE   = aws_dynamodb_table.richieste.name
    PROGRESSI_TABLE   = aws_dynamodb_table.progressi.name
    CONTATORI_TABLE   = aws_dynamodb_table.contatori.name
    ACCESSI_TABLE     = aws_dynamodb_table.accessi.name
  }
}

output "table_names" {
  value = {
    users     = aws_dynamodb_table.users.name
    concorsi  = aws_dynamodb_table.concorsi.name
    follows   = aws_dynamodb_table.follows.name
    questions = aws_dynamodb_table.questions.name
    attempts  = aws_dynamodb_table.attempts.name
    codici    = aws_dynamodb_table.codici.name
    ordini    = aws_dynamodb_table.ordini.name
    banche    = aws_dynamodb_table.banche_dati.name
    richieste = aws_dynamodb_table.richieste.name
    progressi = aws_dynamodb_table.progressi.name
    contatori = aws_dynamodb_table.contatori.name
    accessi   = aws_dynamodb_table.accessi.name
  }
}
