# Ambiente prod: versione di Terraform, provider (AWS in eu-south-1 e us-east-1 per CloudFront)
# e stato remoto su S3 (prod/terraform.tfstate).

terraform {
  required_version = ">= 1.10"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.7"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
  }

  # Bucket creato da infra/terraform/bootstrap: imieiconcorsi-tfstate-<account id>.
  # Il nome lo passa scripts/deploy.sh a "terraform init" (-backend-config=bucket=...),
  # così non va riscritto se cambia l'account AWS.
  backend "s3" {
    key          = "prod/terraform.tfstate"
    region       = "eu-south-1"
    encrypt      = true
    use_lockfile = true
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "imieiconcorsi"
      Environment = "prod"
    }
  }
}

# CloudFront vuole i certificati (e in prod il WAF) in us-east-1.
provider "aws" {
  alias  = "us_east_1"
  region = "us-east-1"

  default_tags {
    tags = {
      Project     = "imieiconcorsi"
      Environment = "prod"
    }
  }
}
