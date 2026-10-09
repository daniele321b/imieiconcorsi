# Job pianificati (ora italiana): ognuno è una Lambda lanciata da EventBridge Scheduler.

module "job" {
  source   = "../lambda"
  for_each = var.jobs

  name              = "${var.name}-${each.key}"
  source_dir        = "${var.functions_dir}/${each.key}"
  environment       = merge(var.environment, each.value.environment)
  write_tables      = each.value.write_tables
  read_tables       = each.value.read_tables
  policy_statements = jsondecode(each.value.policies)
  timeout           = each.value.timeout
}

resource "aws_iam_role" "scheduler" {
  name = "${var.name}-scheduler"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "scheduler.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "scheduler" {
  name = "invoke"
  role = aws_iam_role.scheduler.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "lambda:InvokeFunction"
      Resource = [for m in module.job : m.arn]
    }]
  })
}

resource "aws_scheduler_schedule" "job" {
  for_each = var.jobs

  name                         = "${var.name}-${each.key}"
  description                  = each.value.description
  schedule_expression          = each.value.schedule
  schedule_expression_timezone = "Europe/Rome"

  flexible_time_window {
    mode = "OFF"
  }

  target {
    arn      = module.job[each.key].arn
    role_arn = aws_iam_role.scheduler.arn

    retry_policy {
      maximum_retry_attempts = 2
    }
  }
}
