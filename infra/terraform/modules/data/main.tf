# Tabelle DynamoDB. Ogni microservizio è proprietario delle sue; gli altri le leggono soltanto.

# Servizio profilo: profilo, onboarding e piano dell'utente.
resource "aws_dynamodb_table" "users" {
  name         = "${var.name}-users"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userId"

  attribute {
    name = "userId"
    type = "S"
  }

  point_in_time_recovery {
    enabled = true
  }
}

# Servizio concorsi: bandi importati da inPA.
resource "aws_dynamodb_table" "concorsi" {
  name         = "${var.name}-concorsi"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
  attribute {
    name = "comparto"
    type = "S"
  }
  attribute {
    name = "scadenza"
    type = "S"
  }

  global_secondary_index {
    name            = "byComparto"
    projection_type = "ALL"

    key_schema {
      attribute_name = "comparto"
      key_type       = "HASH"
    }
    key_schema {
      attribute_name = "scadenza"
      key_type       = "RANGE"
    }
  }
}

# Servizio concorsi: concorsi seguiti dagli utenti.
resource "aws_dynamodb_table" "follows" {
  name         = "${var.name}-follows"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userId"
  range_key    = "concorsoId"

  attribute {
    name = "userId"
    type = "S"
  }
  attribute {
    name = "concorsoId"
    type = "S"
  }
}

# Servizio studio: banca domande, partizionata per materia.
resource "aws_dynamodb_table" "questions" {
  name         = "${var.name}-questions"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "materia"
  range_key    = "id"

  attribute {
    name = "materia"
    type = "S"
  }
  attribute {
    name = "id"
    type = "S"
  }
}

# Servizio studio: sessioni di studio e simulazioni (id ordinabile per data).
resource "aws_dynamodb_table" "attempts" {
  name         = "${var.name}-attempts"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userId"
  range_key    = "id"

  attribute {
    name = "userId"
    type = "S"
  }
  attribute {
    name = "id"
    type = "S"
  }

  point_in_time_recovery {
    enabled = true
  }
}

# Servizio billing: codici sconto generati dall'admin (pannello di controllo).
resource "aws_dynamodb_table" "codici" {
  name         = "${var.name}-codici"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "codice"

  attribute {
    name = "codice"
    type = "S"
  }

  point_in_time_recovery {
    enabled = true
  }
}

# Servizio billing: ordini dei piani a pagamento (uno per ogni tentativo di acquisto).
# Niente dati personali: l'email si legge da Cognito quando serve.
resource "aws_dynamodb_table" "ordini" {
  name         = "${var.name}-ordini"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }

  point_in_time_recovery {
    enabled = true
  }
}

# Pannello admin: banche dati ufficiali caricate in PDF (stato dell'estrazione, riepilogo).
resource "aws_dynamodb_table" "banche_dati" {
  name         = "${var.name}-banche-dati"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "id"

  attribute {
    name = "id"
    type = "S"
  }
}
