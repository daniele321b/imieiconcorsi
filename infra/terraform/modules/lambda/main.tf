# Una funzione Lambda con tutto quello che le serve: codice, log, ruolo e permessi.
# La usano i moduli api (un microservizio per Lambda) e jobs (un job per Lambda), e il
# trigger di Cognito. Il codice arriva già compilato da scripts/deploy.sh build in
# dist/functions/<nome>/index.mjs: qui si comprime in uno zip e si carica.

# Zip del codice compilato (cambia solo se cambia il codice: allora la Lambda si aggiorna).
data "archive_file" "code" {
  type        = "zip"
  source_dir  = var.source_dir
  output_path = "${path.root}/.build/${var.name}.zip"
}

# Log della funzione, tenuti per log_retention_days giorni (14 di solito).
resource "aws_cloudwatch_log_group" "this" {
  name              = "/aws/lambda/${var.name}"
  retention_in_days = var.log_retention_days
}

# Ruolo con cui gira la funzione: può essere assunto solo dal servizio Lambda.
resource "aws_iam_role" "this" {
  name = var.name
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

# Permessi minimi: scrivere i propri log, leggere/scrivere solo le tabelle indicate
# (write_tables, read_tables, con i loro indici) e le regole in più di policy_statements.
resource "aws_iam_role_policy" "this" {
  name = "access"
  role = aws_iam_role.this.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = concat(
      [{
        Effect   = "Allow"
        Action   = ["logs:CreateLogStream", "logs:PutLogEvents"]
        Resource = "${aws_cloudwatch_log_group.this.arn}:*"
      }],
      length(var.write_tables) == 0 ? [] : [{
        Effect = "Allow"
        Action = [
          "dynamodb:GetItem", "dynamodb:BatchGetItem", "dynamodb:Query",
          "dynamodb:PutItem", "dynamodb:UpdateItem", "dynamodb:DeleteItem", "dynamodb:BatchWriteItem",
        ]
        Resource = flatten([for arn in var.write_tables : [arn, "${arn}/index/*"]])
      }],
      length(var.read_tables) == 0 ? [] : [{
        Effect   = "Allow"
        Action   = ["dynamodb:GetItem", "dynamodb:BatchGetItem", "dynamodb:Query"]
        Resource = flatten([for arn in var.read_tables : [arn, "${arn}/index/*"]])
      }],
      var.policy_statements,
    )
  })
}

# La funzione: Node.js 22 su processori ARM (Graviton, costano meno), entrata index.handler.
resource "aws_lambda_function" "this" {
  function_name    = var.name
  role             = aws_iam_role.this.arn
  runtime          = "nodejs22.x"
  architectures    = ["arm64"]
  handler          = "index.handler"
  filename         = data.archive_file.code.output_path
  source_code_hash = data.archive_file.code.output_base64sha256
  timeout          = var.timeout
  memory_size      = var.memory_size

  environment {
    variables = merge({ NODE_OPTIONS = "--enable-source-maps" }, var.environment)
  }

  logging_config {
    log_format = "Text"
    log_group  = aws_cloudwatch_log_group.this.name
  }

  depends_on = [aws_iam_role_policy.this]
}
