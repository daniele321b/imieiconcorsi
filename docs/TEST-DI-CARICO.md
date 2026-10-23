# Test di carico (ambiente preprod)

Prima del lancio va verificato che l'app regga **1.000 utenti contemporanei** (requisito di
produzione). Il test non si fa su prod: si crea **preprod**, una copia di prod su
`https://preprod.imieiconcorsi.it`. Lì [k6](https://k6.io) simula gli utenti, poi si leggono i
risultati e si smonta tutto.

Pezzi coinvolti:

| Cosa | Dove |
| --- | --- |
| Ambiente preprod (Terraform) | `infra/terraform/environments/preprod/` (differenze da prod in testa a `main.tf`) |
| Utenti di prova e copia delle banche dati | `scripts/carico/preprod.mjs` |
| Scenari di k6 (gli utenti finti) | `scripts/carico/scenari.js` |
| Comandi | `scripts/deploy.sh carico …`, solo con `ENVIRONMENT=preprod` |
| Password di prova e risultati | `.carico/` alla radice del repo (non va in git) |

## In breve

```bash
brew install k6                                        # una volta (oppure Docker Desktop acceso)

scripts/deploy.sh build
ENVIRONMENT=preprod scripts/deploy.sh infra            # "yes"; la prima volta 15-20 minuti
ENVIRONMENT=preprod scripts/deploy.sh carico prepara   # 1.000 utenti di prova, banche dati, bandi

ENVIRONMENT=preprod scripts/deploy.sh carico avvia fumo          # 2 minuti, 5 utenti: funziona tutto?
ENVIRONMENT=preprod scripts/deploy.sh carico avvia carico 1000   # il test vero, ~32 minuti
ENVIRONMENT=preprod scripts/deploy.sh carico avvia picco 1000    # picco improvviso, ~12 minuti

ENVIRONMENT=preprod scripts/deploy.sh destroy          # alla fine: smonta tutto
```

## 1. L'ambiente preprod

È `environments/prod` con poche differenze, tutte segnate "Preprod:" nei commenti di `main.tf`:

| | prod | preprod |
| --- | --- | --- |
| Indirizzo | imieiconcorsi.it | preprod.imieiconcorsi.it |
| Protezione dalla cancellazione | sì | no: si smonta dopo il test |
| WAF | sì, 2.000 richieste per IP in 5 minuti | sì, stesse regole, ma 1.000.000 per IP (k6 esce da un solo IP) |
| Lambda dell'API | nessun tetto proprio | `profile` 100, `concorsi` 100, `study` 150 esecuzioni riservate |
| Login | SRP (dal sito) | anche email e password diretta, per k6 |
| Pagamenti | Stripe live (o chiusi) | "mock", come dev |
| Tutor AI | tetti 5 $ per utente, 50 $ al mese | 0,5 $ e 5 $: il tutor resta fuori dal test |
| Email | normali | oggetto con "[preprod]", contatti su info-dev@ |
| Budget AWS | sì | no (c'è già quello dell'account) |
| Allarmi via email | ad `admin_email` | a nessuno, salvo `admin_email` in `preprod/terraform.tfvars` |

**Cose condivise con dev e prod (stesso account AWS):**
- **Esecuzioni Lambda contemporanee:** il limite è 1.000 per tutto l'account. Le 350 riservate
  a preprod mancano a dev e prod finché preprod esiste (ne restano circa 640). Le riservate fanno
  anche da tetto: preprod sotto carico non può prendersi tutto il resto e lasciare prod senza
  Lambda. Si cambiano con `concorrenza_riservata` in `preprod/terraform.tfvars`.
- **Cognito:** 1.000 utenti di prova che fanno login contano come 1.000 utenti attivi del mese.
  Sono gratis fino a 10.000 al mese in tutto l'account.
- **SES:** gli utenti di prova hanno email `success+caricoNNNN@simulator.amazonses.com`. È il
  simulatore di SES: accetta e non consegna, e non tocca la reputazione del dominio. Con
  l'onboarding gli utenti scelgono "avvisi: mai", quindi il job delle 7 non manda loro niente.

**Costi.** Acceso e fermo, preprod costa circa 0,50 $ al giorno: WAF, allarmi e dashboard,
cioè 15 $ al mese. Va bene tenerlo qualche giorno, non mesi. Un test da mezz'ora costa
pochi dollari (Lambda, DynamoDB, CloudFront, WAF a richiesta).

**AWS.** I test di carico sulle proprie risorse non richiedono autorizzazione. La policy di AWS
sui "network stress test" riguarda traffici oltre 1 Gbps, molto sopra questo test. Mai lanciare
k6 contro prod: lo script si rifiuta se l'indirizzo è imieiconcorsi.it.

## 2. Preparazione (il giorno prima)

1. **k6** sul Mac: `brew install k6`. In alternativa basta Docker Desktop acceso: senza k6,
   `deploy.sh` usa l'immagine `grafana/k6:2.3.0`.
2. **L'ambiente.** La build è la stessa di dev e prod:
   ```bash
   scripts/deploy.sh build
   ENVIRONMENT=preprod scripts/deploy.sh infra
   ```
   Senza `preprod/terraform.tfvars` vanno bene i valori di base. Per ricevere gli allarmi
   durante il test, copia `terraform.tfvars.example` in `terraform.tfvars` e metti `admin_email`.
   Poi conferma le email "Subscription Confirmation" che arrivano.
3. **Dati e utenti:**
   ```bash
   ENVIRONMENT=preprod scripts/deploy.sh carico prepara        # 1000 utenti; "prepara 2000" per averne di più
   ```
   Fa tre cose:
   - crea gli utenti di prova su Cognito (5-10 minuti per 1.000; si può rilanciare, completa
     quelli che mancano). Uno su tre è nel piano Medium;
   - copia le banche dati pubblicate di dev con le loro domande (solo lettura su dev). Da prod:
     `CARICO_BANCHE_DA=prod ENVIRONMENT=preprod scripts/deploy.sh carico prepara`;
   - se non ci sono bandi, lancia lo scraper di inPA (come `seed`).

   La banca domande (`data/domande`) la carica già `infra`.
4. **Facoltativo:** registrati su https://preprod.imieiconcorsi.it e lancia
   `ENVIRONMENT=preprod scripts/deploy.sh make-admin tua@email.it`. Nel pannello admin vedi
   gli "Utenti attivi" salire durante il test.
5. **Controllo:**
   ```bash
   ENVIRONMENT=preprod scripts/deploy.sh carico stato     # limite Lambda, riservate, utenti di prova
   ENVIRONMENT=preprod scripts/deploy.sh status           # bandi e domande nelle tabelle
   ```

## 3. Gli scenari

| Scenario | Cosa fa | Durata | Quando |
| --- | --- | --- | --- |
| `fumo` | 5 utenti per due minuti | ~3 min | Sempre per primo: script, login e dati sono a posto? Decidono l'esito solo errori e controlli; i tempi si mostrano ma non contano, perché con poche richieste il p95 è fatto dagli avvii a freddo delle Lambda (~1 s alla prima chiamata di ogni servizio) |
| `carico` | Sale in 10 minuti fino a VU utenti, resta lì 20 minuti, scende | ~32 min | **Il test vero** (VU = 1000) |
| `picco` | Da 10% a 100% di VU in un minuto (post virale, uscita di un bando) | ~12 min | Dopo `carico`: regge l'arrivo improvviso (Lambda a freddo, WAF, Cognito)? |
| `rottura` | Gradini da 50% a 250% di VU; si ferma da solo oltre il 5% di errori | fino a ~27 min | Per sapere quanto margine c'è oltre 1.000. Con più utenti finti che utenti di prova, due VU usano lo stesso account: va bene, ma `carico prepara 2500` è più realistico |
| `resistenza` | Metà di VU per due ore | ~2 h 7 min | Facoltativo: problemi lenti (token che scadono dopo un'ora, tabelle che crescono) |

```bash
ENVIRONMENT=preprod scripts/deploy.sh carico avvia SCENARIO [VU]     # VU di base 1000
```

Ordine consigliato per il giorno del test: `fumo` → `carico 1000` → `picco 1000` →
`rottura 1000`. Tra uno e l'altro lascia qualche minuto: le metriche di CloudWatch restano
separate e si leggono meglio. Prima di ogni scenario (tranne `fumo`) `deploy.sh` chiede "si".

## 4. Cosa fanno gli utenti finti

Due tipi, insieme. Gli **anonimi** sono il 20% (`CARICO_ANONIMI`): home, `config.json`, i file
JS e CSS del sito, la lista dei bandi di un paio di comparti dai file statici, una pagina
informativa. È tutto CloudFront, nessuna Lambda.

Gli **iscritti** sono l'80%. Fanno login una volta (e di nuovo quando il token scade) e
l'onboarding al primo giro. Poi ripetono visite di qualche minuto, come chi apre l'app:
- **sempre:** profilo, concorsi seguiti e statistiche;
- **una visita su due:** lista dei bandi, il dettaglio di uno e a volte "segui". Nel Free il
  secondo concorso dà 403 `LIMITE_PIANO`, che è la risposta prevista;
- **studio:** materie, poi quasi sempre una sessione con consegna. I Medium a volte fanno una
  simulazione da 30 domande (una su cinque con pausa e ripresa), oppure aprono una banca dati,
  consultano una pagina di domande e fanno una sessione sulle domande nuove;
- **tra una visita e l'altra:** chiudono l'app per 15-60 secondi.

Tra un'azione e l'altra ci sono pause "da persona", e ogni domanda prende circa 3 secondi. Per
questo **1.000 utenti contemporanei sono circa 50 richieste all'API al secondo, più circa 40 di
file statici**. Il tutor AI è escluso: costa a risposta, e il suo limite è Bedrock.

Variabili facoltative davanti al comando:

| Variabile | Effetto |
| --- | --- |
| `CARICO_RITMO=0.2` | Pause 5 volte più corte: stessi utenti, 5 volte le richieste. Con `rottura` misura il vero tetto tecnico |
| `CARICO_ANONIMI=0.5` | Metà anonimi (es. lancio con molto traffico dai social) |
| `CARICO_RISORSE=0` | Non scarica JS e CSS: utile se la rete di casa è il collo di bottiglia |

Esempio: `CARICO_RITMO=0.2 ENVIRONMENT=preprod scripts/deploy.sh carico avvia rottura 1000`.

## 5. Durante il test

- **Report dal vivo di k6:** http://localhost:5665 (richieste al secondo, tempi, errori).
- **Dashboard CloudWatch** `imieiconcorsi-preprod`: il link lo stampa `carico avvia`.
- **Log di un servizio:** `ENVIRONMENT=preprod scripts/deploy.sh logs study`.
- **Allarmi accesi:** `ENVIRONMENT=preprod scripts/deploy.sh allarmi`.
- **Per fermarlo:** Ctrl+C. k6 chiude le visite in corso e scrive comunque il riepilogo.
- **Freno d'emergenza:** se qualcosa sembra toccare prod, oltre a Ctrl+C c'è
  `ENVIRONMENT=preprod scripts/deploy.sh manutenzione on`. CloudFront risponde 503 a tutto e
  nessuna richiesta arriva più alle Lambda.

Cosa guardare:

| Dove | Metrica | Va bene se |
| --- | --- | --- |
| Lambda (profile, concorsi, study) | Errors, Throttles | Zero. I throttle vogliono dire tetto basso: alza `concorrenza_riservata` |
| Lambda | Duration p95 | Qualche centinaio di ms; i primi minuti sono più lenti (avvii a freddo) |
| Lambda | ConcurrentExecutions (account) | Ben sotto 1.000 (l'allarme scatta all'80%) |
| API Gateway | 5xx, 4xx, Latency p95 | 5xx a zero; i 4xx sono i 403 previsti del Free |
| DynamoDB | ThrottledRequests, ConsumedReadCapacity | Nessun throttle; letture vedi [§7](#7-punti-gi-noti-da-osservare) |
| CloudFront | 5xxErrorRate | Zero |
| WAF | BlockedRequests | Zero: se blocca, il limite per IP è basso |

## 6. Leggere i risultati

Ogni prova salva in `.carico/risultati/<data>-<scenario>/` questi file:
- `riepilogo.txt`: il riassunto stampato a fine test;
- `riepilogo.json`: tutti i numeri;
- `report.html`: i grafici nel tempo. Si apre nel browser.

A fine test `deploy.sh` dice se le soglie sono rispettate: **PASSATO** (codice 0) oppure "soglie
NON rispettate" (codice 99). Nel riepilogo, le righe con ✗ sono quelle fallite.

**Criteri di successo** (le soglie in `scenari.js`):

| Soglia | Valore | Riga del riepilogo |
| --- | --- | --- |
| Richieste fallite (5xx, timeout, 4xx inattesi) | sotto l'1% | `http_req_failed` |
| Tempi dell'API | 95% sotto 800 ms, 99% sotto 2 s | `http_req_duration{tipo:api}` |
| File statici | 95% sotto 500 ms | `http_req_duration{tipo:statico}` |
| Login (Cognito) | 95% sotto 1,5 s | `http_req_duration{tipo:login}` |
| Controlli sul contenuto delle risposte | oltre il 99% | `checks` |

Altre righe utili: `sessioni_consegnate` (sessioni completate), `login_fatti`, `visita_durata`, e
i tempi di ogni rotta dell'API (`{ name:POST /sessioni }` e le altre), per trovare subito la più
lenta. Hanno sempre la spunta verde: sono lì solo da leggere.

Nei primi minuti di ogni scenario i tempi sono più alti: ogni nuova istanza Lambda impiega circa
un secondo alla prima richiesta (avvio a freddo). Nel `carico` da 30 minuti pesano poco sul p95;
nel `picco` sono proprio ciò che si misura.

**Se qualcosa non va:**

| Sintomo | Causa probabile | Cosa fare |
| --- | --- | --- |
| 5xx su un servizio | Errore nel codice sotto carico | `logs <servizio>`, cerca "ERROR" |
| 5xx/503 e Throttles su una Lambda | Tetto di `concorrenza_riservata` | Alzalo in `preprod/terraform.tfvars`, `infra`, rifai il test |
| Login falliti con `TooManyRequestsException` | Limite di Cognito (circa 120 login al secondo) | Salita più lenta; in prod i login sono distribuiti nel tempo |
| 403 non previsti, BlockedRequests nel WAF | Limite per IP del WAF | Alza `waf_richieste_per_ip` |
| 429 dall'API | Limite dello stage (1.000 al secondo) | Solo con `CARICO_RITMO` molto basso; in prod vale lo stesso limite |
| Tutto lento anche i file statici, Mac al 100% di CPU o rete piena | Il limite è il Mac, non AWS | `CARICO_RISORSE=0`, oppure k6 da EC2 (sotto) |
| Tempi alti con `http_req_receiving` alto e `http_req_waiting` basso | Il server risponde subito, è il download a essere lento: rete di casa | Guarda `data_received` (MB/s) rispetto alla tua linea; `CARICO_RISORSE=0` o EC2 |
| Richieste lente o in timeout tutte nello stesso istante, statici compresi | Un'interruzione della rete di casa, se nella dashboard Latency dell'API e Duration delle Lambda in quel momento sono normali | Niente: conta il p95 su tutta la prova |
| ThrottledRequests su DynamoDB | Partizione calda della tabella questions | Vedi §7 |

Dopo una correzione al codice: `scripts/deploy.sh build`, poi
`ENVIRONMENT=preprod scripts/deploy.sh infra` e di nuovo lo scenario.

### k6 da un'istanza EC2 (se la rete di casa non basta)

1. Console EC2 → regione Milano → "Avvia istanza": Amazon Linux 2023, tipo `c7g.xlarge`.
   Coppia di chiavi o Session Manager per entrare.
2. Sull'istanza:
   ```bash
   sudo dnf install -y https://dl.k6.io/rpm/repo.rpm && sudo dnf install -y k6
   ulimit -n 65535
   ```
3. Copia `scripts/carico/scenari.js` sull'istanza (scp, o incollalo in un file).
4. Sul Mac `ENVIRONMENT=preprod scripts/deploy.sh carico comando carico 1000` stampa la riga di
   k6 completa, password compresa. Lanciala sull'istanza nella cartella di `scenari.js`.
5. Finito il test, **termina l'istanza**.

## 7. Punti già noti da osservare

Dalla lettura del codice ci sono tre letture DynamoDB che crescono con il numero di domande.
Il test dice se pesano davvero. Se le soglie passano e la spesa resta bassa, non serve toccarle.

- **`GET /materie`** (ogni apertura di Studio): 13 query `COUNT`, una per materia, sulla tabella
  `questions`. DynamoDB fa pagare un `COUNT` come la lettura di tutte le domande contate: circa
  5.000 domande, centinaia di unità di lettura a chiamata. Correzione possibile: contare le
  domande una volta all'import (`import-domande`) o tenerle in memoria nella Lambda.
- **`POST /sessioni`**: legge tutte le domande delle materie scelte (circa 500 per materia) per
  sceglierne 10-30. Tutte le sessioni di una materia vanno sulla stessa partizione
  (`materia`), che regge 3.000 unità di lettura al secondo.
- **`GET /banche-dati`**: uno Scan della tabella delle banche a ogni apertura. La tabella è
  piccola: va bene finché le banche sono qualche decina.

Nella dashboard: `ConsumedReadCapacityUnits` della tabella `imieiconcorsi-preprod-questions`.

## 8. Dopo il test

1. Copia i numeri principali in una nota: utenti, richieste al secondo, p95 e p99 dell'API,
   errori, sessioni consegnate, costo. I file in `.carico/risultati/` restano sul Mac.
2. Smonta l'ambiente:
   ```bash
   ENVIRONMENT=preprod scripts/deploy.sh destroy      # "si", poi "yes"; 10-15 minuti
   ```
   Spariscono utenti di prova, tabelle, bucket, CloudFront, WAF e allarmi. Le esecuzioni
   riservate tornano libere per dev e prod: lo conferma
   `aws lambda get-account-settings` (UnreservedConcurrentExecutions di nuovo circa 990).
3. Per rifare il test con utenti "nuovi" senza smontare tutto: `carico pulisci`, poi
   `carico prepara`.

## 9. Tenere preprod allineato a prod

`environments/preprod/main.tf` è la copia di `environments/prod/main.tf`. Quando cambi prod
(route, tabelle, job, permessi), riporta la modifica anche qui prima del prossimo test. Per
vedere le differenze:

```bash
diff infra/terraform/environments/prod/main.tf infra/terraform/environments/preprod/main.tf
```

Devono comparire solo i blocchi segnati "Preprod:".
