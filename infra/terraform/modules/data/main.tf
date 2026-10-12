# Tabelle DynamoDB. Ogni microservizio è proprietario delle sue; gli altri le leggono soltanto.

# Servizio profilo: profilo, onboarding e piano dell'utente.
resource "aws_dynamodb_table" "users" {
  name                        = "${var.name}-users"
  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = var.protezione
  hash_key                    = "userId"

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
  name                        = "${var.name}-concorsi"
  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = var.protezione
  hash_key                    = "id"

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
  name                        = "${var.name}-follows"
  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = var.protezione
  hash_key                    = "userId"
  range_key                   = "concorsoId"

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
  name                        = "${var.name}-questions"
  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = var.protezione
  hash_key                    = "materia"
  range_key                   = "id"

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
  name                        = "${var.name}-attempts"
  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = var.protezione
  hash_key                    = "userId"
  range_key                   = "id"

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
  name                        = "${var.name}-codici"
  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = var.protezione
  hash_key                    = "codice"

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
  name                        = "${var.name}-ordini"
  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = var.protezione
  hash_key                    = "id"

  attribute {
    name = "id"
    type = "S"
  }
  attribute {
    name = "userId"
    type = "S"
  }
  attribute {
    name = "creatoIl"
    type = "S"
  }

  # Storico dei pagamenti di un utente (pagina Profilo), dal più recente.
  global_secondary_index {
    name            = "perUtente"
    projection_type = "ALL"
    key_schema {
      attribute_name = "userId"
      key_type       = "HASH"
    }
    key_schema {
      attribute_name = "creatoIl"
      key_type       = "RANGE"
    }
  }

  point_in_time_recovery {
    enabled = true
  }
}

# Pannello admin: banche dati ufficiali caricate in PDF (stato dell'estrazione, riepilogo).
resource "aws_dynamodb_table" "banche_dati" {
  name                        = "${var.name}-banche-dati"
  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = var.protezione
  hash_key                    = "id"

  attribute {
    name = "id"
    type = "S"
  }
}

# Richieste di assistenza degli utenti (una conversazione per richiesta). L'indice perStato
# serve al pannello admin: le aperte, le in lavorazione, le chiuse, dalla più recente.
resource "aws_dynamodb_table" "richieste" {
  name                        = "${var.name}-richieste"
  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = var.protezione
  hash_key                    = "userId"
  range_key                   = "id"

  attribute {
    name = "userId"
    type = "S"
  }
  attribute {
    name = "id"
    type = "S"
  }
  attribute {
    name = "stato"
    type = "S"
  }
  attribute {
    name = "aggiornataIl"
    type = "S"
  }

  global_secondary_index {
    name            = "perStato"
    projection_type = "ALL"

    key_schema {
      attribute_name = "stato"
      key_type       = "HASH"
    }
    key_schema {
      attribute_name = "aggiornataIl"
      key_type       = "RANGE"
    }
  }

  point_in_time_recovery {
    enabled = true
  }
}

# Domande delle banche dati già fatte da ogni utente: una riga per utente e banca dati,
# con due mappe di bit (fatte, sbagliate l'ultima volta) indicizzate dal numero della domanda.
resource "aws_dynamodb_table" "progressi" {
  name                        = "${var.name}-progressi"
  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = var.protezione
  hash_key                    = "userId"
  range_key                   = "bancaId"

  attribute {
    name = "userId"
    type = "S"
  }
  attribute {
    name = "bancaId"
    type = "S"
  }
}

# Contatori della piattaforma, una riga per contatore: per ora la spesa AI del mese
# ("ai#2026-10": token e dollari stimati), per il tetto di spesa mensile del tutor.
resource "aws_dynamodb_table" "contatori" {
  name                        = "${var.name}-contatori"
  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = var.protezione
  hash_key                    = "id"

  attribute {
    name = "id"
    type = "S"
  }

  # Contatori temporanei (es. limite del modulo contatti per IP) con "scade": si cancellano da
  # soli. Quelli senza "scade" (spesa AI del mese) restano.
  ttl {
    attribute_name = "scade"
    enabled        = true
  }
}

# Accessi degli utenti (login con email e password, Google o Facebook), registrati da Cognito
# (functions/src/auth/accesso.ts). Si cancellano da soli dopo 12 mesi (TTL su "scade").
resource "aws_dynamodb_table" "accessi" {
  name                        = "${var.name}-accessi"
  billing_mode                = "PAY_PER_REQUEST"
  deletion_protection_enabled = var.protezione
  hash_key                    = "userId"
  range_key                   = "il"

  attribute {
    name = "userId"
    type = "S"
  }
  attribute {
    name = "il"
    type = "S"
  }

  ttl {
    attribute_name = "scade"
    enabled        = true
  }
}
