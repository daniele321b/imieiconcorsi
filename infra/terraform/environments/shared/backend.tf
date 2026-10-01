terraform {
  required_version = ">= 1.10"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  # Stesso bucket di stato degli ambienti (lo passa scripts/deploy.sh a terraform init).
  backend "s3" {
    key          = "shared/terraform.tfstate"
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
      Environment = "shared"
    }
  }
}
