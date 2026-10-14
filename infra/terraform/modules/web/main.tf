# Un solo CloudFront davanti a:
#   /api/*  -> API Gateway (nessuna cache, passa il token)
#   il resto -> sito statico nel bucket S3 privato
# Un solo indirizzo per sito e API: niente CORS, e in prod il WAF si attacca qui.
# Con domain_name (es. dev.imieiconcorsi.it): certificato ACM in us-east-1 (CloudFront
# li vuole lì) validato via DNS, e record A/AAAA nella hosted zone. Senza: *.cloudfront.net.

terraform {
  required_providers {
    aws = {
      source                = "hashicorp/aws"
      configuration_aliases = [aws.us_east_1]
    }
  }
}

# Con un dominio proprio servono certificato e record DNS.
locals {
  con_dominio = var.domain_name != null
}

# Certificato HTTPS per il dominio (solo se c'è domain_name).
resource "aws_acm_certificate" "web" {
  count             = local.con_dominio ? 1 : 0
  provider          = aws.us_east_1
  domain_name       = var.domain_name
  validation_method = "DNS"

  lifecycle {
    create_before_destroy = true
  }
}

# Il certificato copre un solo nome, quindi un solo record di validazione: con count
# Terraform sa quanti record creare prima ancora di avere il certificato.
resource "aws_route53_record" "cert_validation" {
  count = local.con_dominio ? 1 : 0

  zone_id         = var.zone_id
  name            = tolist(aws_acm_certificate.web[0].domain_validation_options)[0].resource_record_name
  type            = tolist(aws_acm_certificate.web[0].domain_validation_options)[0].resource_record_type
  records         = [tolist(aws_acm_certificate.web[0].domain_validation_options)[0].resource_record_value]
  ttl             = 300
  allow_overwrite = true
}

# Attende che AWS confermi il certificato tramite il record DNS.
resource "aws_acm_certificate_validation" "web" {
  count                   = local.con_dominio ? 1 : 0
  provider                = aws.us_east_1
  certificate_arn         = aws_acm_certificate.web[0].arn
  validation_record_fqdns = [for r in aws_route53_record.cert_validation : r.fqdn]
}

# Bucket del sito (file di packages/web/dist) e della lista dei bandi in cache.
resource "aws_s3_bucket" "web" {
  bucket_prefix = "${var.name}-web-"
  force_destroy = !var.protezione
}

# Cifrato a riposo (SSE-S3, AES-256). AWS lo fa già da sé: qui è dichiarato e non cambia.
resource "aws_s3_bucket_server_side_encryption_configuration" "web" {
  bucket = aws_s3_bucket.web.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
    bucket_key_enabled = true
  }
}

# Privato: i file si leggono solo passando da CloudFront.
resource "aws_s3_bucket_public_access_block" "web" {
  bucket                  = aws_s3_bucket.web.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Identità con cui CloudFront legge il bucket privato (richieste firmate).
resource "aws_cloudfront_origin_access_control" "web" {
  name                              = "${var.name}-web"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

# Politica di cache standard di AWS per i file statici.
data "aws_cloudfront_cache_policy" "caching_optimized" {
  name = "Managed-CachingOptimized"
}

# Inoltra all'API intestazioni e parametri del browser, tranne Host.
data "aws_cloudfront_origin_request_policy" "all_viewer_except_host" {
  name = "Managed-AllViewerExceptHostHeader"
}

# API: in pratica nessuna cache (le risposte hanno Cache-Control: no-store). Authorization
# sta nella chiave di cache perché è l'unico modo per inoltrarlo all'origine sulle GET.
resource "aws_cloudfront_cache_policy" "api" {
  name        = "${var.name}-api"
  min_ttl     = 0
  default_ttl = 0
  max_ttl     = 1

  parameters_in_cache_key_and_forwarded_to_origin {
    cookies_config {
      cookie_behavior = "none"
    }
    headers_config {
      header_behavior = "whitelist"
      headers {
        items = ["Authorization"]
      }
    }
    query_strings_config {
      query_string_behavior = "all"
    }
  }
}

# ── Intestazioni di sicurezza ────────────────────────────────────────────────
# Su ogni risposta (sito e API): HTTPS obbligatorio (HSTS), niente pagine dentro frame di altri
# siti (clickjacking), niente "indovina il tipo" dei file, referrer ridotto, permessi del browser
# spenti e una Content-Security-Policy che fa eseguire solo il codice del nostro sito.
# Se il sito comincia a usare un servizio esterno nuovo (script, font, API), va aggiunto qui.

locals {
  # Google AdSense (solo se attivo): script, frame e chiamate verso i domini degli annunci.
  google_ads = var.pubblicita_esterna ? [
    "https://pagead2.googlesyndication.com", "https://*.googlesyndication.com", "https://*.doubleclick.net",
    "https://*.google.com", "https://*.googleadservices.com", "https://*.gstatic.com",
  ] : []
  csp = join("; ", [
    "default-src 'self'",
    "script-src ${join(" ", concat(["'self'"], local.google_ads))}",
    # 'unsafe-inline' solo per gli stili (attributi style di React e degli annunci), mai per gli script.
    "style-src 'self' 'unsafe-inline'",
    "font-src 'self'",
    "img-src 'self' data:${var.pubblicita_esterna ? " https:" : ""}",
    "connect-src ${join(" ", concat(["'self'"], var.csp_connect_src, local.google_ads))}",
    "frame-src ${var.pubblicita_esterna ? join(" ", local.google_ads) : "'none'"}",
    "frame-ancestors 'none'",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "upgrade-insecure-requests",
  ])
}

# Intestazioni di sicurezza su ogni risposta del sito (HSTS, CSP, anti-frame, niente sniffing).
resource "aws_cloudfront_response_headers_policy" "sicurezza" {
  name    = "${var.name}-sicurezza"
  comment = "Intestazioni di sicurezza di ${var.name} (HSTS, CSP, anti-frame)"

  security_headers_config {
    strict_transport_security {
      access_control_max_age_sec = 63072000
      include_subdomains         = true
      override                   = true
    }
    content_type_options {
      override = true
    }
    frame_options {
      frame_option = "DENY"
      override     = true
    }
    referrer_policy {
      referrer_policy = "strict-origin-when-cross-origin"
      override        = true
    }
    content_security_policy {
      content_security_policy = local.csp
      override                = true
    }
  }

  custom_headers_config {
    items {
      header   = "Permissions-Policy"
      value    = "camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()"
      override = true
    }
    items {
      header   = "Cross-Origin-Opener-Policy"
      value    = "same-origin-allow-popups"
      override = true
    }
  }
}

# Sito a pagina unica: un indirizzo come /app/profilo serve index.html (decide React).
resource "aws_cloudfront_function" "spa" {
  name    = "${var.name}-spa"
  runtime = "cloudfront-js-2.0"
  publish = true
  code    = file("${path.module}/functions/spa.js")
}

# Toglie /api dall'indirizzo prima di passarlo all'API Gateway.
resource "aws_cloudfront_function" "api_prefix" {
  name    = "${var.name}-api-prefix"
  runtime = "cloudfront-js-2.0"
  publish = true
  code    = file("${path.module}/functions/api-prefix.js")
}

# La distribuzione CloudFront: HTTPS, cache dei file statici, /api/* verso l'API Gateway.
resource "aws_cloudfront_distribution" "web" {
  enabled             = true
  comment             = var.name
  default_root_object = "index.html"
  price_class         = "PriceClass_100"
  http_version        = "http2and3"
  web_acl_id          = var.web_acl_arn
  aliases             = local.con_dominio ? [var.domain_name] : []

  origin {
    origin_id                = "web"
    domain_name              = aws_s3_bucket.web.bucket_regional_domain_name
    origin_access_control_id = aws_cloudfront_origin_access_control.web.id
  }

  origin {
    origin_id   = "api"
    domain_name = var.api_domain

    # Segreto che dice alle Lambda "arrivo da CloudFront": chi chiama l'API Gateway direttamente
    # non ce l'ha e viene respinto (core/http.ts, daCloudFront). Sostituisce quello del visitatore.
    custom_header {
      name  = "x-origine-cloudfront"
      value = var.origine_segreta
    }

    custom_origin_config {
      http_port              = 80
      https_port             = 443
      origin_protocol_policy = "https-only"
      origin_ssl_protocols   = ["TLSv1.2"]
    }
  }

  default_cache_behavior {
    target_origin_id           = "web"
    viewer_protocol_policy     = "redirect-to-https"
    allowed_methods            = ["GET", "HEAD"]
    cached_methods             = ["GET", "HEAD"]
    cache_policy_id            = data.aws_cloudfront_cache_policy.caching_optimized.id
    response_headers_policy_id = aws_cloudfront_response_headers_policy.sicurezza.id
    compress                   = true

    function_association {
      event_type   = "viewer-request"
      function_arn = aws_cloudfront_function.spa.arn
    }
  }

  ordered_cache_behavior {
    path_pattern               = "/api/*"
    target_origin_id           = "api"
    viewer_protocol_policy     = "https-only"
    allowed_methods            = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    cached_methods             = ["GET", "HEAD"]
    cache_policy_id            = aws_cloudfront_cache_policy.api.id
    origin_request_policy_id   = data.aws_cloudfront_origin_request_policy.all_viewer_except_host.id
    response_headers_policy_id = aws_cloudfront_response_headers_policy.sicurezza.id
    compress                   = true

    function_association {
      event_type   = "viewer-request"
      function_arn = aws_cloudfront_function.api_prefix.arn
    }
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = !local.con_dominio
    acm_certificate_arn            = local.con_dominio ? aws_acm_certificate_validation.web[0].certificate_arn : null
    ssl_support_method             = local.con_dominio ? "sni-only" : null
    minimum_protocol_version       = local.con_dominio ? "TLSv1.2_2021" : "TLSv1"
  }
}

# Il bucket si lascia leggere solo da questa distribuzione CloudFront, e solo in HTTPS.
resource "aws_s3_bucket_policy" "web" {
  bucket = aws_s3_bucket.web.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = { Service = "cloudfront.amazonaws.com" }
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.web.arn}/*"
        Condition = { StringEquals = { "AWS:SourceArn" = aws_cloudfront_distribution.web.arn } }
      },
      {
        Sid       = "SoloHttps"
        Effect    = "Deny"
        Principal = "*"
        Action    = "s3:*"
        Resource  = [aws_s3_bucket.web.arn, "${aws_s3_bucket.web.arn}/*"]
        Condition = { Bool = { "aws:SecureTransport" = "false" } }
      },
    ]
  })
}

# Lista dei bandi in cache (dati/bandi/<versione>/…): la scrive lo scraper ogni mattina in una
# cartella nuova; le cartelle vecchie spariscono da sole. indice.json si riscrive ogni giorno.
resource "aws_s3_bucket_lifecycle_configuration" "web" {
  bucket = aws_s3_bucket.web.id

  rule {
    id     = "cache-bandi-vecchie"
    status = "Enabled"

    filter {
      prefix = "dati/bandi/"
    }

    expiration {
      days = 45
    }
  }
}

# ── Contenuto del sito ───────────────────────────────────────────────────────

locals {
  content_types = {
    html  = "text/html; charset=utf-8"
    js    = "text/javascript"
    css   = "text/css"
    json  = "application/json"
    svg   = "image/svg+xml"
    png   = "image/png"
    jpg   = "image/jpeg"
    ico   = "image/x-icon"
    webp  = "image/webp"
    woff2 = "font/woff2"
    txt   = "text/plain"
    map   = "application/json"
  }

  # config.json lo scrive Terraform qui sotto: quello eventualmente presente in dist è dello sviluppo locale.
  web_files = setsubtract(fileset(var.dist_dir, "**"), ["config.json"])
}

# Ogni file del sito compilato, con il tipo giusto e la cache adatta.
resource "aws_s3_object" "web" {
  for_each = local.web_files

  bucket       = aws_s3_bucket.web.id
  key          = each.value
  source       = "${var.dist_dir}/${each.value}"
  source_hash  = filemd5("${var.dist_dir}/${each.value}")
  content_type = lookup(local.content_types, reverse(split(".", each.value))[0], "application/octet-stream")
  # Gli asset hanno l'hash nel nome e non cambiano mai; index.html va sempre riletto.
  cache_control = startswith(each.value, "assets/") ? "public, max-age=31536000, immutable" : "no-cache"
}

# config.json: indirizzo dell'API e dati di Cognito per il sito (lib/config.ts).
resource "aws_s3_object" "web_config" {
  bucket        = aws_s3_bucket.web.id
  key           = "config.json"
  content       = jsonencode(var.app_config)
  content_type  = "application/json"
  cache_control = "no-cache"
}

# ── DNS: dominio -> CloudFront ───────────────────────────────────────────────

resource "aws_route53_record" "web" {
  for_each = local.con_dominio ? toset(["A", "AAAA"]) : toset([])

  zone_id = var.zone_id
  name    = var.domain_name
  type    = each.value

  alias {
    name                   = aws_cloudfront_distribution.web.domain_name
    zone_id                = aws_cloudfront_distribution.web.hosted_zone_id
    evaluate_target_health = false
  }
}
