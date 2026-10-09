# Guida: pagamenti con Stripe

iMieiConcorsi incassa direttamente con **Stripe Checkout**. Carta, PayPal,
Apple Pay e Google Pay passano tutti dalla stessa pagina di Stripe, e trovi ogni
pagamento nella dashboard di Stripe. Niente piattaforma di pagamento nostra.

Le chiavi segrete vanno **solo** in
`infra/terraform/environments/dev/terraform.tfvars` (non va su git): non
incollarle in chat né in altri file.

## Come funziona

```
Piani → "Scegli Medium" ──▶ billing: prezzo calcolato dal server (sconto compreso),
                            crea la sessione di pagamento Stripe
                                   │
          ┌────────────────────────┘
          ▼
   Pagina di Stripe: carta / PayPal / Apple Pay / Google Pay
          │                                  │
          ▼                                  ▼
   L'utente torna sul sito          Stripe manda la conferma firmata
   (pagina "esito pagamento")       a /api/pubblico/stripe/webhook
                                             │
                                             ▼
                                    piano attivato, una volta sola,
                                    + email di conferma
```
- I dati della carta li vede solo Stripe. A Stripe non mandiamo il nome
  dell'utente: solo l'email per la ricevuta e un codice d'ordine.
- Pagamento unico per 30 o 365 giorni, senza rinnovo automatico (come oggi).
- Il piano si attiva **solo** con la conferma di Stripe: tornare sul sito senza
  pagare non attiva nulla.

## Chi fa cosa

| Passo | Cosa | Chi |
|---|---|---|
| 1 | Account Stripe e chiave di prova | tu |
| 2 | Aspetto della pagina di pagamento e ricevute | tu |
| 3 | Attivare PayPal, Apple Pay e Google Pay | tu |
| 4 | Collegamento nel codice | fatto |
| 5 | Endpoint per le conferme (webhook) | tu, dopo il passo 4 |
| 6 | Prova completa | tu |
| 7 | Soldi veri | tu, alla fine |

---

## Passo 1 — Account Stripe e chiave di prova

1. Vai su <https://dashboard.stripe.com/register>: email, nome, password,
   paese **Italia**. Per le prove non servono partita IVA né IBAN.
2. In alto nella dashboard attiva la **Modalità test** (Test mode). I pagamenti
   di prova sono separati da quelli veri e non costano nulla.
3. **Sviluppatori** (Developers) → **Chiavi API** → **Chiave segreta** →
   **Mostra** → copia la chiave che inizia con `sk_test_`.
4. In `infra/terraform/environments/dev/terraform.tfvars` aggiungi:
   ```hcl
   stripe_secret_key = "sk_test_..."
   ```
   (La riga la metto io anche in `terraform.tfvars.example` con il passo 4.)

## Passo 2 — Aspetto della pagina e ricevute

1. **Impostazioni** → **Dati aziendali** (Business details): nome pubblico
   `iMieiConcorsi`, sito `https://imieiconcorsi.it`, email di assistenza.
2. **Impostazioni** → **Branding**: logo, icona e colore principale (il viola
   del sito). Così la pagina di pagamento sembra parte di iMieiConcorsi.
3. **Impostazioni** → **Email clienti**: attiva **Pagamenti riusciti**. Stripe
   manda la ricevuta del pagamento; la nostra email di conferma (piano,
   scadenza, rinuncia al recesso) parte comunque.

## Passo 3 — PayPal, Apple Pay e Google Pay

**Impostazioni** → **Metodi di pagamento** (Payment methods), in modalità test:
- **PayPal** → Attiva. Prima leggi commissioni e condizioni, che compaiono lì;
  in modalità live Stripe può chiedere di collegare un conto PayPal.
- **Apple Pay** e **Google Pay**: di solito sono già attivi. Apple Pay compare
  solo su Safari/iPhone, Google Pay su Chrome/Android.
- **Carte**: già attive.

Nel codice non va scritto nulla per questi metodi: Stripe mostra da solo quelli
attivi e adatti al dispositivo dell'utente.

## Passo 4 — Collegamento nel codice (fatto)

1. **Ordini:** una tabella nuova con codice d'ordine, utente, piano, periodo,
   importo, eventuale codice sconto e stato (in attesa, pagato, scaduto).
2. **Acquisto:** in Piani, con la casella del recesso spuntata, "Scegli
   Medium" porta alla pagina di Stripe. Prezzo e sconto li calcola il server,
   non il browser.
3. **Conferma da Stripe** su `/api/pubblico/stripe/webhook`:
   - la firma viene verificata;
   - il piano si attiva una volta sola, anche se Stripe manda la conferma due
     volte;
   - il codice sconto si consuma solo qui, a pagamento riuscito;
   - parte l'email di conferma.
4. **Pagina "esito pagamento":** mostra "Pagamento riuscito" appena arriva la
   conferma, "Pagamento annullato" se l'utente torna indietro.
5. **Modalità di prova:** senza `stripe_secret_key` il cambio di piano resta
   gratuito ("mock"); con la chiave si paga con Stripe.
6. **Prezzi di prova:** finché `PREZZI_DI_PROVA = true` in
   `packages/core/src/domain.ts` ogni piano costa 0,50 € (il minimo di
   Stripe). Prima dei soldi veri va rimesso `false`.
7. **Anche senza webhook** il piano si attiva: la pagina di ritorno chiede
   l'esito direttamente a Stripe. Il webhook (passo 5) serve se l'utente chiude
   il browser prima di tornare sul sito.

Poi:
```bash
scripts/deploy.sh test && scripts/deploy.sh build
scripts/deploy.sh infra        # terraform chiede "yes"
```

## Passo 5 — Endpoint per le conferme (webhook)

Dopo il deploy del passo 4:
1. Dashboard Stripe (in modalità test) → **Sviluppatori** → **Webhook** →
   **Aggiungi endpoint** (Add endpoint).
2. **URL dell'endpoint:**
   `https://dev.imieiconcorsi.it/api/pubblico/stripe/webhook`
3. **Eventi da inviare** → seleziona:
   - `checkout.session.completed`
   - `checkout.session.async_payment_succeeded`
   - `checkout.session.async_payment_failed`
   - `checkout.session.expired`
4. **Aggiungi endpoint**. Nella pagina dell'endpoint, **Segreto di firma**
   (Signing secret) → **Mostra** → copia il valore `whsec_...`.
5. In `terraform.tfvars`:
   ```hcl
   stripe_webhook_secret = "whsec_..."
   ```
6. Applica:
   ```bash
   scripts/deploy.sh infra        # terraform chiede "yes"
   ```

## Passo 6 — Prova completa

Su <https://dev.imieiconcorsi.it> con un utente di prova:
1. **Piani** → spunta la casella del recesso → **Scegli Medium**.
2. Sulla pagina di Stripe paga con la carta `4242 4242 4242 4242`, scadenza
   futura qualsiasi, CVC qualsiasi.
3. Torni sul sito: "Pagamento riuscito", piano Medium attivo, email di
   conferma (più la ricevuta di Stripe).
4. Altre prove:

   | Prova | Risultato atteso |
   |---|---|
   | carta `4000 0025 0000 3155` (chiede il 3D Secure: "Complete") | piano attivo |
   | carta `4000 0000 0000 0002` | rifiutata, piano invariato |
   | "Indietro" dalla pagina di Stripe | "Pagamento annullato", piano invariato |
   | PayPal (pagina di prova di PayPal: "Authorize") | piano attivo |
   | con un codice sconto | importo scontato su Stripe, codice consumato solo dopo il pagamento |

5. Nella dashboard Stripe → **Pagamenti** vedi ogni prova. In **Sviluppatori →
   Webhook** → il tuo endpoint vedi le conferme inviate: devono essere tutte
   "200".

## Passo 7 — Soldi veri (alla fine)

1. Dashboard → **Attiva i pagamenti** (Activate payments): tipo di attività
   (ditta individuale o società), **partita IVA**, documento d'identità e
   **IBAN** su cui ricevere i soldi.
2. Disattiva la modalità test e rifai, nella parte live, il passo 1 (chiave
   `sk_live_...`), il passo 3 (metodi di pagamento) e il passo 5 (webhook, con
   un nuovo `whsec_...`).
3. Le chiavi live vanno nel `terraform.tfvars` dell'ambiente di **produzione**
   (quando lo creeremo); dev resta in modalità test.

Prima dei pagamenti veri controlla anche:
- prezzi definitivi in `packages/core/src/domain.ts`;
- dati del titolare in `packages/web/src/lib/legale.ts` (Termini e Privacy), da
  far rivedere a un legale;
- fatture: la ricevuta di Stripe non è una fattura. Si può usare Stripe
  Invoicing o il tuo gestionale: va deciso con il commercialista.

## Altri progetti

Lo stesso account Stripe può servire tutte le tue app. Nella dashboard ogni
pagamento porta il nome dell'app nella descrizione e nei metadati, e puoi
filtrare. In ogni progetto l'integrazione è la stessa: un servizio che crea la
sessione di pagamento e una rotta che riceve la conferma, ognuna con il suo
endpoint webhook.
