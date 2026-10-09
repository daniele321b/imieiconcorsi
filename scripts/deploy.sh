#!/usr/bin/env bash
#
# Deploy di iMieiConcorsi su AWS: un comando per ogni passo, con controlli
# prima di fare danni. Spiegazioni in docs/DEPLOY.md, comandi pronti in
# docs/COMANDI-RAPIDI.md. Tutta l'infrastruttura è Terraform (infra/terraform).
#
#   scripts/deploy.sh check                  # strumenti, credenziali, bucket di stato
#   scripts/deploy.sh bootstrap              # crea il bucket dello stato Terraform (una volta sola)
#   scripts/deploy.sh shared                 # risorse comuni a dev e prod: SES (una volta, poi solo se cambia)
#   scripts/deploy.sh build [lambda|web]     # compila le Lambda (dist/functions) e il sito (packages/web/dist)
#   scripts/deploy.sh infra                  # terraform init + apply dell'ambiente
#   scripts/deploy.sh seed                   # importa subito i bandi aperti da inPA (lo scraper gira poi ogni mattina)
#   scripts/deploy.sh job NOME               # lancia subito un job: inpa-scraper, avvisi, scadenze, import-domande (reimporta data/domande)
#   scripts/deploy.sh make-admin EMAIL       # mette l'utente nel gruppo admin (pannello di controllo)
#   scripts/deploy.sh unisci-account EMAIL   # unisce gli account doppi (email + Facebook/Google) creati prima del trigger
#   scripts/deploy.sh genera-domande [MAT]   # data/domande/<materia>.json da contenuti/sorgenti (vuoto = tutte)
#   scripts/deploy.sh verifica-domande       # ogni domanda ha la sua frase-prova nel PDF della fonte
#   scripts/deploy.sh urls                   # indirizzi: sito, pannello admin, API, redirect URI Google/Facebook
#   scripts/deploy.sh status                 # quanti bandi e domande ci sono nelle tabelle
#   scripts/deploy.sh ses-status             # SES: sandbox o produzione, indirizzi verificati
#   scripts/deploy.sh ses-production [URL]   # chiede ad AWS di uscire dalla sandbox SES (una volta per account)
#   scripts/deploy.sh email-prova EMAIL      # manda un'email di prova da SES e spiega perché non parte
#   scripts/deploy.sh logs [servizio]        # log in tempo reale: profile, concorsi, study, billing, admin, inpa-scraper, avvisi, scadenze
#   scripts/deploy.sh local                  # sito in locale (http://localhost:5173) collegato all'ambiente su AWS
#   scripts/deploy.sh test                   # test e controllo dei tipi del codice applicativo
#   scripts/deploy.sh all                    # check -> shared -> build -> infra -> seed -> urls
#   scripts/deploy.sh destroy                # smonta l'ambiente (chiede conferma; shared resta)
#   scripts/deploy.sh destroy-shared         # smonta le risorse comuni (SES) — solo se non serve più a nessun ambiente
#
# Variabili: AWS_PROFILE (opzionale), ENVIRONMENT (default dev), REGION (default
# eu-south-1), DOMAIN (default imieiconcorsi.it), DRY_RUN=1 stampa i comandi senza eseguirli.

set -euo pipefail

REGION="${REGION:-eu-south-1}"
PROJECT="imieiconcorsi"
DOMAIN="${DOMAIN:-imieiconcorsi.it}"
ENVIRONMENT="${ENVIRONMENT:-dev}"
NAME="${PROJECT}-${ENVIRONMENT}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TF_ROOT="${ROOT}/infra/terraform"
TF_DIR="${TF_ROOT}/environments/${ENVIRONMENT}"
TF_SHARED="${TF_ROOT}/environments/shared"
DIST_FUNCTIONS="${ROOT}/dist/functions"
DIST_WEB="${ROOT}/packages/web/dist"
DRY_RUN="${DRY_RUN:-0}"

# Lambda: nome -> sorgente (packages/functions/src/...)
LAMBDAS=(
  "profile:profile/handler.ts"
  "concorsi:concorsi/handler.ts"
  "study:study/handler.ts"
  "billing:billing/handler.ts"
  "admin:admin/handler.ts"
  "pubblico:pubblico/handler.ts"
  "auth-pre-signup:auth/pre-signup.ts"
  "inpa-scraper:jobs/inpa-scraper.ts"
  "avvisi:jobs/avvisi.ts"
  "scadenze:jobs/scadenze.ts"
  "import-domande:contenuti/import-domande.ts"
  "estrai-banca-dati:banche-dati/estrai.ts"
)

export AWS_DEFAULT_REGION="$REGION"

# ------------------------------------------------------------------ utilità --

bold() { printf '\033[1m%s\033[0m\n' "$*"; }
ok()   { printf '  \033[32m✔\033[0m %s\n' "$*"; }
warn() { printf '  \033[33m!\033[0m %s\n' "$*"; }
die()  { printf '\033[31mERRORE:\033[0m %s\n' "$*" >&2; exit 1; }

run() {
  if [[ "$DRY_RUN" == "1" ]]; then
    printf '  [dry-run] %s\n' "$*"
  else
    "$@"
  fi
}

capture() {
  local placeholder="$1"
  shift
  if [[ "$DRY_RUN" == "1" ]]; then
    printf '%s' "$placeholder"
  else
    "$@"
  fi
}

confirm() {
  [[ "$DRY_RUN" == "1" ]] && return 0
  local answer
  # Dal terminale, non da stdin: confirm può stare dentro un ciclo che legge un elenco.
  read -r -p "$1 [scrivi 'si' per confermare] " answer < /dev/tty
  [[ "$answer" == "si" ]]
}

tf_output() { capture "<$1>" terraform -chdir="$TF_DIR" output -raw "$1"; }
account_id() { capture "123456789012" aws sts get-caller-identity --query Account --output text; }
state_bucket() { printf '%s-tfstate-%s' "$PROJECT" "$(account_id)"; }

# Dipendenze Node del codice applicativo: installate solo se mancano o se il lockfile è cambiato.
node_deps() {
  if [[ ! -d "${ROOT}/node_modules" || "${ROOT}/package-lock.json" -nt "${ROOT}/node_modules/.package-lock.json" ]]; then
    bold "Dipendenze Node (npm ci)"
    run npm --prefix "$ROOT" ci --no-audit --no-fund
  fi
}

# ------------------------------------------------------------------- check ---

cmd_check() {
  bold "Controllo prerequisiti"
  local missing=0 tool
  for tool in aws terraform node npm; do
    if command -v "$tool" >/dev/null 2>&1; then ok "$tool"; else warn "$tool NON trovato"; missing=1; fi
  done
  [[ "$DRY_RUN" == "1" ]] || [[ $missing -eq 0 ]] \
    || die "installa gli strumenti mancanti (brew install awscli hashicorp/tap/terraform node@24) e riprova"
  [[ "$DRY_RUN" == "1" ]] && return

  local identity
  identity="$(aws sts get-caller-identity --query Arn --output text 2>&1)" \
    || die "credenziali AWS non valide (${identity}). Configura AWS_PROFILE o aws configure."
  ok "AWS: ${identity}"

  bold "Stato Terraform"
  if aws s3api head-bucket --bucket "$(state_bucket)" >/dev/null 2>&1; then
    ok "bucket di stato $(state_bucket)"
  else
    die "manca il bucket di stato $(state_bucket): lancia prima  scripts/deploy.sh bootstrap"
  fi

  bold "Dominio"
  local zone
  zone="$(aws route53 list-hosted-zones-by-name --dns-name "${DOMAIN}" \
    --query "HostedZones[?Name=='${DOMAIN}.'].Id | [0]" --output text 2>/dev/null || true)"
  [[ -n "$zone" && "$zone" != "None" ]] && ok "hosted zone ${DOMAIN} (${zone##*/})" \
    || die "nessuna hosted zone per ${DOMAIN} su questo account AWS"

  # Il dominio è utilizzabile quando su internet risponde con i nameserver della hosted
  # zone: serve al certificato HTTPS e alla verifica SES. Finché la registrazione è in
  # corso non succede, e Terraform resterebbe ad aspettare il certificato.
  local ns_zona ns_internet
  ns_zona="$(aws route53 get-hosted-zone --id "${zone##*/}" --query 'DelegationSet.NameServers' --output text \
    | tr '\t' '\n' | tr 'A-Z' 'a-z' | sed 's/\.$//' | sort | tr '\n' ' ')"
  ns_internet="$(dig +short NS "$DOMAIN" 2>/dev/null | tr 'A-Z' 'a-z' | sed 's/\.$//' | sort | tr '\n' ' ')"
  if [[ -n "$ns_internet" && "$ns_internet" == "$ns_zona" ]]; then
    ok "dominio attivo: ${DOMAIN} risponde con i nameserver della hosted zone"
  else
    die "${DOMAIN} non è ancora attivo su internet (registrazione in corso?). Riprova più tardi: scripts/deploy.sh check"
  fi

  bold "Configurazione"
  if [[ -f "${TF_SHARED}/terraform.tfvars" ]]; then
    ok "shared/terraform.tfvars presente (dominio, destinatari sandbox SES)"
  else
    die "manca ${TF_SHARED#"${ROOT}/"}/terraform.tfvars: copia terraform.tfvars.example e metti il tuo indirizzo in sandbox_recipients"
  fi
  if [[ -f "${TF_DIR}/terraform.tfvars" ]]; then
    ok "${ENVIRONMENT}/terraform.tfvars presente (email admin, Google/Facebook se compilati)"
  else
    warn "nessun ${ENVIRONMENT}/terraform.tfvars: niente avvisi admin, login solo con email e password"
  fi
  bold "Tutto a posto."
}

# --------------------------------------------------------------- bootstrap ---

cmd_bootstrap() {
  bold "Bucket dello stato Terraform (una volta sola)"
  if [[ "$DRY_RUN" != "1" ]] && aws s3api head-bucket --bucket "$(state_bucket)" >/dev/null 2>&1; then
    ok "esiste già: $(state_bucket)"
    return
  fi
  run terraform -chdir="${TF_ROOT}/bootstrap" init -input=false
  run terraform -chdir="${TF_ROOT}/bootstrap" apply
}

# ------------------------------------------------------------------- build ---

build_lambda() {
  local entry name src
  bold "Build delle Lambda (esbuild)"
  run rm -rf "$DIST_FUNCTIONS"
  for entry in "${LAMBDAS[@]}"; do
    name="${entry%%:*}"
    src="${ROOT}/packages/functions/src/${entry#*:}"
    # L'SDK AWS v3 è già nel runtime Lambda; il banner rende disponibile require nelle dipendenze CommonJS.
    run "${ROOT}/node_modules/.bin/esbuild" "$src" \
      --bundle --platform=node --target=node22 --format=esm --minify --sourcemap \
      --external:'@aws-sdk/*' \
      --banner:js="import { createRequire } from 'module'; const require = createRequire(import.meta.url);" \
      --outfile="${DIST_FUNCTIONS}/${name}/index.mjs" --log-level=warning
    ok "$name"
  done
}

build_web() {
  bold "Build del sito (Vite)"
  run npm --prefix "$ROOT" run build -w packages/web
}

cmd_build() {
  node_deps
  case "${1:-all}" in
    all) build_lambda; build_web ;;
    lambda) build_lambda ;;
    web) build_web ;;
    *) die "cosa compilo? lambda, web (vuoto = entrambi)" ;;
  esac
}

# ------------------------------------------------------------------- infra ---

tf_init() {
  local dir="${1:-$TF_DIR}"
  # L'ambiente legge le risorse comuni (shared) dallo stesso bucket di stato.
  export TF_VAR_state_bucket
  TF_VAR_state_bucket="$(state_bucket)"
  run terraform -chdir="$dir" init -input=false -backend-config="bucket=${TF_VAR_state_bucket}"
}

cmd_shared() {
  [[ "$DRY_RUN" == "1" || -f "${TF_SHARED}/terraform.tfvars" ]] \
    || die "manca ${TF_SHARED#"${ROOT}/"}/terraform.tfvars: copia terraform.tfvars.example e metti il tuo indirizzo in sandbox_recipients"
  bold "Risorse comuni a dev e prod (dominio ${DOMAIN}, SES)"
  tf_init "$TF_SHARED"
  run terraform -chdir="$TF_SHARED" apply
  printf "  Se è la prima volta: AWS manda un'email di conferma a ogni indirizzo da verificare. Clicca il link.\n"
  printf '  Stato:  scripts/deploy.sh ses-status\n'
}

cmd_infra() {
  [[ "$DRY_RUN" == "1" || ( -d "$DIST_FUNCTIONS" && -f "${DIST_WEB}/index.html" ) ]] \
    || die "mancano le Lambda o il sito compilati: lancia prima  scripts/deploy.sh build"
  bold "terraform init + apply (${ENVIRONMENT})"
  tf_init
  run terraform -chdir="$TF_DIR" apply
}

# -------------------------------------------------------------------- seed ---

cmd_job() {
  local job="${1:-}" fn out
  case "$job" in
    inpa-scraper|avvisi|scadenze|import-domande) ;;
    *) die "quale job? inpa-scraper, avvisi, scadenze, import-domande" ;;
  esac
  fn="${NAME}-${job}"
  out="$(mktemp)"
  bold "Job ${job} (può richiedere un minuto)"
  if [[ "$DRY_RUN" == "1" ]]; then
    printf '  [dry-run] aws lambda invoke --function-name %s\n' "$fn"
  else
    aws lambda invoke --function-name "$fn" --cli-read-timeout 330 "$out" >/dev/null
    ok "risposta: $(cat "$out")"
  fi
  rm -f "$out"
}

cmd_seed() {
  cmd_job inpa-scraper
  printf '  Le domande (data/domande/*.json) le carica infra: ogni file caricato viene importato da solo.\n'
}

# --------------------------------------------------------------- admin/SES ---

cmd_make_admin() {
  local email="${1:-}" pool users u
  [[ -n "$email" ]] || die "uso: scripts/deploy.sh make-admin tua@email.it   (l'utente deve essersi già registrato)"
  pool="$(tf_output user_pool_id)"
  # Stessa email = possibili più utenti (email/password, Google, Facebook): admin a tutti.
  users="$(capture "<username>" aws cognito-idp list-users --user-pool-id "$pool" \
    --filter "email = \"${email}\"" --query 'Users[].Username' --output text)"
  [[ -n "$users" && "$users" != "None" ]] || die "nessun utente con email ${email}: registrati prima sul sito"
  bold "Gruppo admin per ${email}"
  for u in $users; do
    run aws cognito-idp admin-add-user-to-group --user-pool-id "$pool" --username "$u" --group-name admin
    ok "$u"
  done
  printf '  Esci e rientra nel sito: il nuovo ruolo arriva con il token. Pannello: %s/admin\n' "$(tf_output web_url)"
}

cmd_unisci_account() {
  local email="${1:-}" pool righe nativo="" user stato prefisso provider id
  [[ -n "$email" ]] || die "uso: scripts/deploy.sh unisci-account tua@email.it"
  pool="$(tf_output user_pool_id)"
  righe="$(capture "uuid-nativo CONFIRMED
facebook_123 EXTERNAL_PROVIDER" aws cognito-idp list-users --user-pool-id "$pool" \
    --filter "email = \"${email}\"" --query 'Users[].[Username,UserStatus]' --output text)"
  while read -r user stato; do
    [[ "$stato" == "CONFIRMED" ]] && nativo="$user"
  done <<< "$righe"
  [[ -n "$nativo" ]] || die "nessun account email/password confermato per ${email}: niente da unire"

  bold "Account per ${email}: tengo ${nativo} (email e password)"
  while read -r user stato; do
    [[ "$stato" == "EXTERNAL_PROVIDER" ]] || continue
    prefisso="$(printf '%s' "${user%%_*}" | tr 'A-Z' 'a-z')"
    id="${user#*_}"
    case "$prefisso" in
      google) provider="Google" ;;
      facebook) provider="Facebook" ;;
      *) warn "salto ${user}: provider sconosciuto"; continue ;;
    esac
    warn "${user} (${provider}) verrà cancellato e il suo accesso collegato a ${nativo}: i dati di studio di quell'account si perdono"
    confirm "Procedo con ${user}?" || { warn "saltato ${user}"; continue; }
    run aws cognito-idp admin-delete-user --user-pool-id "$pool" --username "$user"
    run aws cognito-idp admin-link-provider-for-user --user-pool-id "$pool" \
      --destination-user "ProviderName=Cognito,ProviderAttributeValue=${nativo}" \
      --source-user "ProviderName=${provider},ProviderAttributeName=Cognito_Subject,ProviderAttributeValue=${id}"
    ok "${provider} ora entra nell'account ${nativo}"
  done <<< "$righe"
}

cmd_ses_status() {
  bold "SES (${REGION})"
  run aws sesv2 get-account --region "$REGION" \
    --query '{produzione:ProductionAccessEnabled,invii_24h:SendQuota.Max24HourSend,stato:EnforcementStatus,richiesta_uscita:Details.ReviewDetails.Status,caso_supporto:Details.ReviewDetails.CaseId}' --output table
  run aws sesv2 list-email-identities --region "$REGION" \
    --query 'EmailIdentities[].{identita:IdentityName,verificata:VerificationStatus}' --output table
  printf '  In sandbox SES scrive solo agli indirizzi verificati (max 200 email/giorno).\n'
}

cmd_ses_production() {
  local url="${1:-https://${DOMAIN}}" stato
  bold "Richiesta ad AWS di uscire dalla sandbox SES"
  # Una richiesta già inviata blocca la seconda (ConflictException): prima si guarda a che punto è.
  stato="$(capture "NESSUNA" aws sesv2 get-account --region "$REGION" \
    --query 'join(`/`, [to_string(ProductionAccessEnabled), Details.ReviewDetails.Status || `NESSUNA`])' --output text 2>/dev/null || echo "?")"
  case "$stato" in
    true/*)    ok "SES è già in produzione: scrive a tutti"; return ;;
    */PENDING) ok "richiesta già inviata e in esame da AWS: la risposta arriva per email all'indirizzo dell'account AWS (scripts/deploy.sh ses-status)"; return ;;
    */GRANTED) ok "richiesta approvata: tra poco ses-status mostrerà produzione = True"; return ;;
    */DENIED)
      warn "la richiesta precedente risulta rifiutata: da comando AWS non ne accetta un'altra (ConflictException)"
      printf '  Si chiede la rivalutazione rispondendo al caso: console AWS -> Support Center -> caso indicato da\n'
      printf '  "scripts/deploy.sh ses-status" (colonna caso_supporto) -> Reply. Testo pronto: docs/COMANDI-RAPIDI.md, "Uscire dalla sandbox SES".\n'
      return ;;
  esac
  confirm "Invio la richiesta per l'account (email transazionali di iMieiConcorsi)?" || die "annullato"
  run aws sesv2 put-account-details --region "$REGION" \
    --production-access-enabled --mail-type TRANSACTIONAL --website-url "$url" --contact-language EN \
    --use-case-description "Our AWS account hosts two small Italian web applications. A previous request for one of them (Fleet Audit, September 2026) was declined; since then we added SNS notifications for every bounce, complaint and rejection (delivered to the account owner), account-level suppression for bounces and complaints, one-click unsubscribe (RFC 8058 List-Unsubscribe headers) on every recurring email, and we have been sending in the sandbox to verified testers only. This request is for iMieiConcorsi (${url}), a study app for Italian public-sector job competitions. We send only to people who registered on our website with their own address (email confirmation through Amazon Cognito): purchase confirmations, a plan-expiry reminder (once, 3 days before), a notice when a plan ends, and - only if the user opts in from their profile - a daily or weekly digest of new public competitions, with an unsubscribe link and List-Unsubscribe headers. No purchased, imported or scraped address lists, no marketing campaigns. Expected volume during the beta: under 100 emails per day. Domain verified with DKIM, custom MAIL FROM with SPF, and DMARC. Privacy policy: ${url}/privacy. Example digest email: subject '3 nuovi bandi per te', body: list of the new competitions with deadline and link, the reason the user receives it, and a one-click unsubscribe link."
  ok "richiesta inviata: AWS risponde di solito entro 24-48 ore (scripts/deploy.sh ses-status)"
}

# Prova di invio con lo stesso mittente e configuration set delle Lambda.
cmd_email_prova() {
  local a="${1:-}" mittente config dominio
  [[ -n "$a" ]] || die "uso: scripts/deploy.sh email-prova tua@email.it"
  mittente="$(capture "noreply@${DOMAIN}" terraform -chdir="$TF_SHARED" output -raw ses_sender_email)"
  config="$(capture "<config-set>" terraform -chdir="$TF_SHARED" output -raw ses_configuration_set_name)"
  bold "Email di prova da ${mittente} a ${a}"

  dominio="$(capture "?" aws sesv2 get-email-identity --region "$REGION" --email-identity "$DOMAIN" --query VerificationStatus --output text 2>/dev/null || echo "NON TROVATO")"
  [[ "$dominio" == "SUCCESS" ]] && ok "dominio ${DOMAIN} verificato" \
    || warn "dominio ${DOMAIN}: ${dominio} — senza dominio verificato SES non spedisce (controlla i record DKIM: scripts/deploy.sh shared)"
  if [[ "$(capture "false" aws sesv2 get-account --region "$REGION" --query ProductionAccessEnabled --output text 2>/dev/null || echo False)" != "True" ]]; then
    warn "SES è in sandbox: ${a} deve essere tra gli indirizzi verificati (sandbox_recipients in environments/shared)"
  fi

  run aws sesv2 send-email --region "$REGION" \
    --from-email-address "iMieiConcorsi <${mittente}>" \
    --destination "ToAddresses=${a}" \
    --configuration-set-name "$config" \
    --content "Simple={Subject={Data='[prova] Email da iMieiConcorsi',Charset=UTF-8},Body={Text={Data='Se leggi questa email, SES funziona.',Charset=UTF-8}}}" \
    && ok "inviata: controlla anche lo spam"
}

# ------------------------------------------------------------------ status ---

cmd_urls() {
  bold "Indirizzi (${ENVIRONMENT})"
  printf '  Sito                     %s\n' "$(tf_output web_url)"
  printf '  Pannello admin           %s/admin\n' "$(tf_output web_url)"
  printf '  API (stesso CloudFront)  %s\n' "$(tf_output api_url)"
  printf '  API Gateway diretto      %s\n' "$(tf_output api_gateway_url)"
  printf '  Redirect Google/Facebook %s\n' "$(tf_output cognito_idp_redirect_uri)"
}

cmd_status() {
  local table
  bold "Contenuto delle tabelle (${NAME})"
  for table in concorsi questions users attempts follows; do
    printf '  %-10s %s\n' "$table" "$(capture "<n>" aws dynamodb scan --table-name "${NAME}-${table}" \
      --select COUNT --query Count --output text)"
  done
  cmd_urls
}

cmd_logs() {
  local service="${1:-}"
  [[ -n "$service" ]] || die "quale servizio? profile, concorsi, study, billing, admin, inpa-scraper, scadenze"
  run aws logs tail "/aws/lambda/${NAME}-${service}" --follow --format short
}

# ------------------------------------------------------------------- local ---

cmd_local() {
  node_deps
  bold "Sito in locale collegato all'ambiente ${ENVIRONMENT}: http://localhost:5173  (Ctrl+C per chiudere)"
  if [[ "$DRY_RUN" == "1" ]]; then
    printf '  [dry-run] terraform output -json web_config > packages/web/public/config.json\n'
  else
    terraform -chdir="$TF_DIR" output -json web_config > "${ROOT}/packages/web/public/config.json"
    ok "packages/web/public/config.json"
  fi
  # Vite inoltra /api al CloudFront dell'ambiente (vedi packages/web/vite.config.ts).
  export API_PROXY_TARGET
  API_PROXY_TARGET="$(tf_output web_url)"
  run npm --prefix "$ROOT" run dev -w packages/web
}

# ---------------------------------------------------------- banca domande ---

cmd_genera_domande() {
  local m
  if [[ -n "${1:-}" ]]; then
    run python3 "${ROOT}/scripts/domande/genera.py" "$1"
  else
    for m in "${ROOT}"/contenuti/sorgenti/*.py; do run python3 "${ROOT}/scripts/domande/genera.py" "$(basename "${m%.py}")"; done
  fi
}

cmd_verifica_domande() {
  command -v pdftotext >/dev/null 2>&1 || die "serve pdftotext: brew install poppler"
  bold "Verifica delle domande sulle fonti (contenuti/libri)"
  run python3 "${ROOT}/scripts/domande/verifica.py" "$@"
}

cmd_test() {
  node_deps
  bold "Test (vitest)"
  run npm --prefix "$ROOT" test
  bold "Controllo dei tipi (TypeScript)"
  run npm --prefix "$ROOT" run typecheck
}

# ----------------------------------------------------------------- destroy ---

cmd_destroy() {
  bold "ATTENZIONE: elimina TUTTO l'ambiente ${ENVIRONMENT} (utenti Cognito e dati compresi)"
  confirm "Sei sicuro?" || die "annullato"
  tf_init
  run terraform -chdir="$TF_DIR" destroy
}

cmd_destroy_shared() {
  bold "ATTENZIONE: elimina le risorse comuni (SES) usate da TUTTI gli ambienti"
  confirm "Nessun ambiente le usa più?" || die "annullato"
  tf_init "$TF_SHARED"
  run terraform -chdir="$TF_SHARED" destroy
}

# --------------------------------------------------------------------- all ---

cmd_all() {
  cmd_check
  cmd_shared
  cmd_build
  cmd_infra
  cmd_seed
  cmd_urls
  bold "Fatto. Apri l'indirizzo del sito, registrati, poi:  scripts/deploy.sh make-admin <tua email>"
}

usage() { sed -n '3,31p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; }

main() {
  local cmd="${1:-}"
  [[ $# -gt 0 ]] && shift
  case "$cmd" in
    check)     cmd_check ;;
    bootstrap) cmd_bootstrap ;;
    build)     cmd_build "$@" ;;
    infra)     cmd_infra ;;
    shared)    cmd_shared ;;
    seed)      cmd_seed ;;
    job)       cmd_job "$@" ;;
    genera-domande) cmd_genera_domande "$@" ;;
    verifica-domande) cmd_verifica_domande "$@" ;;
    make-admin) cmd_make_admin "$@" ;;
    unisci-account) cmd_unisci_account "$@" ;;
    ses-status) cmd_ses_status ;;
    ses-production) cmd_ses_production "$@" ;;
    email-prova) cmd_email_prova "$@" ;;
    destroy-shared) cmd_destroy_shared ;;
    urls)      cmd_urls ;;
    status)    cmd_status ;;
    logs)      cmd_logs "$@" ;;
    local)     cmd_local ;;
    test)      cmd_test ;;
    all)       cmd_all ;;
    destroy)   cmd_destroy ;;
    ""|-h|--help|help) usage ;;
    *) usage; die "comando sconosciuto: ${cmd}" ;;
  esac
}

main "$@"
