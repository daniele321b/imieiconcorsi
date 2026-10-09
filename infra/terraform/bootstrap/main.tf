# Bootstrap: il bucket S3 per lo stato remoto di iMieiConcorsi.
# Si esegue UNA SOLA VOLTA (scripts/deploy.sh bootstrap), con stato locale.
#
# Nome con l'account id per non scontrarsi con bucket già presi (i nomi S3 sono
# globali). Il lock usa il file nativo su S3 (use_lockfile, Terraform >= 1.10):
# nessuna tabella DynamoDB da mantenere.

terraform {
  required_version = ">= 1.10"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  type    = string
  default = "eu-south-1"
}

variable "project_name" {
  type    = string
  default = "imieiconcorsi"
}

data "aws_caller_identity" "current" {}

# Il bucket dello stato di Terraform (protetto dalla cancellazione).
resource "aws_s3_bucket" "state" {
  bucket = "${var.project_name}-tfstate-${data.aws_caller_identity.current.account_id}"

  lifecycle {
    prevent_destroy = true
  }
}

# Versioni: uno stato rovinato si può recuperare.
resource "aws_s3_bucket_versioning" "state" {
  bucket = aws_s3_bucket.state.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Cifratura dei file di stato (contengono anche segreti).
resource "aws_s3_bucket_server_side_encryption_configuration" "state" {
  bucket = aws_s3_bucket.state.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Mai pubblico.
resource "aws_s3_bucket_public_access_block" "state" {
  bucket                  = aws_s3_bucket.state.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

output "state_bucket_name" {
  value = aws_s3_bucket.state.id
}
