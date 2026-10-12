# Diritto amministrativo — fonti: testi vigenti da Normattiva.
L241 = "norma_L241-1990_procedimento-amministrativo.txt"
TUEL = "norma_DLgs267-2000_TUEL.txt"
D165 = "norma_DLgs165-2001_pubblico-impiego.txt"
D33 = "norma_DLgs33-2013_trasparenza.txt"
L190 = "norma_L190-2012_anticorruzione.txt"
P62 = "norma_DPR62-2013_codice-comportamento.txt"
P445 = "norma_DPR445-2000_documentazione-amministrativa.txt"
D36 = "norma_DLgs36-2023_codice-contratti.txt"

# --- Legge 241/1990: procedimento amministrativo ---
D("amm-001", "Procedimento amministrativo", 1, "Quale legge detta le regole generali sul procedimento amministrativo e sul diritto di accesso?",
  "La legge 7 agosto 1990, n. 241", ["Il D.Lgs. 30 marzo 2001, n. 165", "Il D.Lgs. 18 agosto 2000, n. 267", "La legge 6 novembre 2012, n. 190"],
  "La L. 241/1990 disciplina procedimento amministrativo e accesso ai documenti; il D.Lgs. 165/2001 riguarda il pubblico impiego, il TUEL gli enti locali, la L. 190/2012 l'anticorruzione.",
  "L. 241/1990, art. 1", L241, "Principi generali dell'attività amministrativa")

D("amm-002", "Procedimento amministrativo", 2, "Secondo l'art. 1 della L. 241/1990, l'attività amministrativa è retta da criteri di:",
  "economicità, efficacia, imparzialità, pubblicità e trasparenza", ["sussidiarietà, adeguatezza e differenziazione", "legalità, tipicità e nominatività", "rapidità, gratuità e oralità"],
  "L'art. 1 elenca i criteri di economicità, efficacia, imparzialità, pubblicità e trasparenza. Sussidiarietà, differenziazione e adeguatezza sono i principi dell'art. 118 della Costituzione.",
  "L. 241/1990, art. 1", L241, "è retta da criteri di economicità, di efficacia, di imparzialità, di pubblicità e di trasparenza")

D("amm-003", "Procedimento amministrativo", 2, "Se la legge non fissa un termine diverso, entro quanti giorni deve concludersi un procedimento delle amministrazioni statali?",
  "30 giorni", ["60 giorni", "90 giorni", "120 giorni"],
  "Art. 2, comma 2: in mancanza di un termine diverso, i procedimenti si concludono entro trenta giorni.",
  "L. 241/1990, art. 2", L241, "devono concludersi entro il termine di trenta giorni")

D("amm-004", "Procedimento amministrativo", 2, "Secondo l'art. 3 della L. 241/1990, deve essere motivato anche il provvedimento che riguarda lo svolgimento dei pubblici concorsi?",
  "Sì, ogni provvedimento amministrativo deve essere motivato, compresi quelli sui concorsi", ["No, i provvedimenti sui concorsi sono esclusi", "Solo se lo chiede il candidato", "Solo se negativo"],
  "L'art. 3 impone la motivazione di ogni provvedimento, compresi quelli su organizzazione, concorsi e personale; restano esclusi solo gli atti normativi e a contenuto generale.",
  "L. 241/1990, art. 3", L241, "lo svolgimento dei pubblici concorsi ed il personale, deve essere motivato")

D("amm-005", "Partecipazione", 3, "Prima di adottare un provvedimento negativo su un'istanza di parte, l'amministrazione deve:",
  "comunicare i motivi ostativi all'accoglimento (preavviso di rigetto)", ["chiedere il parere del Consiglio di Stato", "sospendere il procedimento per 90 giorni", "convocare una conferenza di servizi"],
  "L'art. 10-bis impone di comunicare tempestivamente agli istanti i motivi che ostano all'accoglimento della domanda.",
  "L. 241/1990, art. 10-bis", L241, "comunica tempestivamente agli istanti i motivi che ostano all'accoglimento della domanda")

D("amm-006", "Partecipazione", 3, "Dopo aver ricevuto il preavviso di rigetto, entro quanti giorni l'istante può presentare osservazioni scritte?",
  "10 giorni", ["5 giorni", "30 giorni", "60 giorni"],
  "Art. 10-bis: entro dieci giorni dal ricevimento della comunicazione gli istanti possono presentare per iscritto le loro osservazioni.",
  "L. 241/1990, art. 10-bis", L241, "Entro il termine di dieci giorni dal ricevimento della comunicazione")

D("amm-007", "Semplificazione", 3, "In caso di SCIA, entro quanti giorni l'amministrazione può vietare la prosecuzione dell'attività per carenza dei requisiti?",
  "60 giorni dal ricevimento della segnalazione", ["30 giorni dal ricevimento della segnalazione", "90 giorni dall'inizio dell'attività", "In qualsiasi momento, senza limiti"],
  "Art. 19, comma 3: l'amministrazione, accertata la carenza dei requisiti, nel termine di sessanta giorni adotta provvedimenti di divieto di prosecuzione dell'attività.",
  "L. 241/1990, art. 19", L241, "nel termine di sessanta giorni dal ricevimento della segnalazione")

D("amm-008", "Semplificazione", 2, "Nel silenzio assenso (art. 20 L. 241/1990), il silenzio dell'amministrazione equivale a:",
  "provvedimento di accoglimento della domanda", ["rigetto della domanda", "sospensione del procedimento", "richiesta di integrazione documentale"],
  "Art. 20: nei procedimenti a istanza di parte il silenzio dell'amministrazione competente equivale ad accoglimento, salvi i casi esclusi.",
  "L. 241/1990, art. 20", L241, "il silenzio dell'amministrazione competente equivale a provvedimento di accoglimento della domanda")

D("amm-009", "Invalidità del provvedimento", 3, "Un provvedimento adottato in violazione di legge, viziato da eccesso di potere o da incompetenza è:",
  "annullabile", ["nullo", "inesistente", "valido ma irregolare"],
  "Art. 21-octies: sono i tre vizi di legittimità che rendono il provvedimento annullabile.",
  "L. 241/1990, art. 21-octies", L241, "È annullabile il provvedimento amministrativo adottato in violazione di legge o viziato da eccesso di potere o da incompetenza")

D("amm-010", "Invalidità del provvedimento", 4, "Quale di questi casi rende NULLO un provvedimento amministrativo?",
  "La mancanza degli elementi essenziali", ["L'eccesso di potere", "L'incompetenza relativa", "La violazione di legge"],
  "Art. 21-septies: è nullo il provvedimento che manca degli elementi essenziali, è viziato da difetto assoluto di attribuzione, è adottato in violazione o elusione del giudicato, o negli altri casi previsti dalla legge.",
  "L. 241/1990, art. 21-septies", L241, "È nullo il provvedimento amministrativo che manca degli elementi essenziali")

D("amm-011", "Autotutela", 5, "Entro quale termine massimo può essere annullato d'ufficio un provvedimento illegittimo di autorizzazione o di attribuzione di vantaggi economici?",
  "Sei mesi dall'adozione", ["Dodici mesi dall'adozione", "Diciotto mesi dall'adozione", "Tre anni dall'adozione"],
  "Il testo vigente dell'art. 21-nonies fissa un termine ragionevole, comunque non superiore a sei mesi, per i provvedimenti di autorizzazione o di attribuzione di vantaggi economici.",
  "L. 241/1990, art. 21-nonies", L241, "comunque non superiore a ((sei mesi)) dal momento dell'adozione dei provvedimenti di autorizzazione")

D("amm-012", "Autotutela", 4, "Per quale motivo l'amministrazione può revocare un provvedimento ad efficacia durevole?",
  "Per sopravvenuti motivi di pubblico interesse", ["Per un vizio di incompetenza", "Perché manca un elemento essenziale", "Per violazione del giudicato"],
  "La revoca (art. 21-quinquies) colpisce atti legittimi per ragioni di opportunità: sopravvenuti motivi di pubblico interesse o mutamento della situazione di fatto. I vizi di legittimità portano invece all'annullamento.",
  "L. 241/1990, art. 21-quinquies", L241, "Per sopravvenuti motivi di pubblico interesse ovvero nel caso di mutamento della situazione di fatto")

D("amm-013", "Accesso ai documenti", 2, "Chi può esercitare il diritto di accesso ai documenti ai sensi della L. 241/1990?",
  "Chi ha un interesse diretto, concreto e attuale collegato al documento", ["Chiunque, senza motivazione", "Solo i cittadini italiani maggiorenni", "Solo i dipendenti dell'amministrazione"],
  "Art. 22: sono interessati i soggetti con un interesse diretto, concreto e attuale, corrispondente a una situazione giuridicamente tutelata. L'accesso di chiunque è invece l'accesso civico del D.Lgs. 33/2013.",
  "L. 241/1990, art. 22", L241, "che abbiano un interesse diretto, concreto e attuale")

D("amm-014", "Accesso ai documenti", 3, "Cosa succede se l'amministrazione non risponde entro 30 giorni a una richiesta di accesso documentale?",
  "La richiesta si intende respinta", ["La richiesta si intende accolta", "Il termine si proroga di altri 30 giorni", "Decide il Difensore civico"],
  "Art. 25: decorsi inutilmente trenta giorni dalla richiesta, questa si intende respinta (silenzio rigetto).",
  "L. 241/1990, art. 25", L241, "Decorsi inutilmente trenta giorni dalla richiesta, questa si intende respinta")

D("amm-015", "Accesso ai documenti", 3, "Nel procedimento di accesso, chi sono i «controinteressati»?",
  "I soggetti che dall'accesso vedrebbero compromesso il loro diritto alla riservatezza", ["I funzionari che detengono il documento", "Gli altri richiedenti dello stesso documento", "Le associazioni di consumatori"],
  "Art. 22, lettera c: sono controinteressati i soggetti che dall'esercizio dell'accesso vedrebbero compromesso il diritto alla riservatezza.",
  "L. 241/1990, art. 22", L241, "dall'esercizio dell'accesso vedrebbero compromesso il loro diritto al")

D("amm-016", "Procedimento amministrativo", 5, "Un comune respinge un'istanza senza aver inviato il preavviso di rigetto, e il ricorrente dimostra che con le sue osservazioni la decisione sarebbe cambiata. Il provvedimento è:",
  "annullabile, perché non si applica la «salvezza» dell'art. 21-octies, comma 2", ["nullo per mancanza di un elemento essenziale", "valido, perché il preavviso è facoltativo", "inesistente"],
  "L'omissione del preavviso (art. 10-bis) è violazione di legge, quindi vizio di annullabilità; il comma 2 dell'art. 21-octies non salva il provvedimento adottato in violazione dell'art. 10-bis.",
  "L. 241/1990, artt. 10-bis e 21-octies", L241, "adottato in violazione dell'articolo 10-bis")

# --- TUEL ---
D("amm-017", "Enti locali", 1, "Quali sono gli organi di governo del comune?",
  "Il consiglio, la giunta e il sindaco", ["Il sindaco e il segretario comunale", "Il consiglio e il revisore dei conti", "La giunta e i dirigenti"],
  "Art. 36 TUEL: sono organi di governo del comune il consiglio, la giunta, il sindaco.",
  "D.Lgs. 267/2000 (TUEL), art. 36", TUEL, "Sono organi di governo del comune il consiglio, la giunta, il sindaco")

D("amm-018", "Enti locali", 2, "Quale organo comunale è definito «di indirizzo e di controllo politico-amministrativo»?",
  "Il consiglio comunale", ["La giunta comunale", "Il sindaco", "Il segretario comunale"],
  "Art. 42 TUEL: il consiglio è l'organo di indirizzo e di controllo politico-amministrativo e approva gli atti fondamentali.",
  "D.Lgs. 267/2000 (TUEL), art. 42", TUEL, "Il consiglio è l'organo di indirizzo e di controllo politico-amministrativo")

D("amm-019", "Enti locali", 2, "Come opera la giunta comunale?",
  "Collabora con il sindaco e opera attraverso deliberazioni collegiali", ["Decide da sola gli atti fondamentali del comune", "È un organo tecnico guidato dal segretario", "Opera solo su delega del consiglio"],
  "Art. 48 TUEL: la giunta collabora con il sindaco nel governo del comune e opera attraverso deliberazioni collegiali.",
  "D.Lgs. 267/2000 (TUEL), art. 48", TUEL, "La giunta collabora con il sindaco o con il presidente della provincia nel governo del comune")

D("amm-020", "Enti locali", 1, "Quanto durano in carica il sindaco e il consiglio comunale?",
  "Cinque anni", ["Quattro anni", "Sei anni", "Tre anni"],
  "Art. 51 TUEL: sindaco e consiglio comunale durano in carica per un periodo di cinque anni.",
  "D.Lgs. 267/2000 (TUEL), art. 51", TUEL, "durano in carica per un periodo di cinque anni")

D("amm-021", "Enti locali", 3, "Da chi dipende il segretario comunale titolare, secondo il testo dell'art. 97 TUEL?",
  "Dall'Agenzia autonoma per la gestione dell'albo dei segretari comunali e provinciali", ["Dal sindaco", "Dalla Prefettura", "Dal consiglio comunale"],
  "L'art. 97 TUEL indica il segretario come dipendente dall'Agenzia autonoma per la gestione dell'albo (le cui funzioni sono oggi del Ministero dell'interno).",
  "D.Lgs. 267/2000 (TUEL), art. 97", TUEL, "hanno un segretario titolare dipendente dall'Agenzia autonoma per la gestione dell'albo")

D("amm-022", "Enti locali", 3, "A chi spetta, nel comune, la direzione degli uffici e dei servizi?",
  "Ai dirigenti", ["Al sindaco", "Alla giunta", "Al consiglio comunale"],
  "Art. 107 TUEL: spetta ai dirigenti la direzione degli uffici e dei servizi; agli organi politici l'indirizzo e il controllo.",
  "D.Lgs. 267/2000 (TUEL), art. 107", TUEL, "Spetta ai dirigenti la direzione degli uffici e dei servizi")

D("amm-023", "Enti locali", 3, "Entro quale data gli enti locali deliberano il bilancio di previsione finanziario?",
  "Entro il 31 dicembre dell'anno precedente", ["Entro il 30 aprile", "Entro il 31 luglio", "Entro il 30 giugno"],
  "Art. 151 TUEL: gli enti locali deliberano il bilancio di previsione entro il 31 dicembre, con orizzonte almeno triennale. Il rendiconto si approva invece entro il 30 aprile.",
  "D.Lgs. 267/2000 (TUEL), art. 151", TUEL, "deliberano il bilancio di previsione finanziario entro il 31 dicembre")

D("amm-024", "Enti locali", 4, "Chi ha ricoperto per due mandati consecutivi la carica di sindaco può essere rieletto subito per un terzo mandato?",
  "No, salvo le eccezioni previste dalla legge (es. comuni più piccoli)", ["Sì, sempre", "Sì, ma solo con il voto di due terzi del consiglio", "No, mai più per tutta la vita"],
  "L'art. 51, comma 2, limita i mandati consecutivi; la legge prevede eccezioni per i comuni di minori dimensioni.",
  "D.Lgs. 267/2000 (TUEL), art. 51", TUEL, "Chi ha ricoperto per due mandati consecutivi la carica di sindaco")

# --- D.Lgs. 165/2001 ---
D("amm-025", "Pubblico impiego", 2, "Secondo il D.Lgs. 165/2001, quali funzioni esercitano gli organi di governo?",
  "Funzioni di indirizzo politico-amministrativo", ["La gestione finanziaria e tecnica", "L'adozione di tutti i provvedimenti verso l'esterno", "La direzione degli uffici"],
  "Art. 4: agli organi di governo spetta l'indirizzo politico-amministrativo; ai dirigenti la gestione (principio di separazione).",
  "D.Lgs. 165/2001, art. 4", D165, "Gli organi di governo esercitano le funzioni di indirizzo politico-amministrativo")

D("amm-026", "Pubblico impiego", 3, "A chi spetta, secondo l'art. 4 del D.Lgs. 165/2001, l'adozione degli atti che impegnano l'amministrazione verso l'esterno?",
  "Ai dirigenti", ["Al ministro", "Agli organi di governo", "Al Consiglio dei ministri"],
  "Ai dirigenti spetta l'adozione degli atti e provvedimenti amministrativi, compresi quelli che impegnano l'amministrazione verso l'esterno.",
  "D.Lgs. 165/2001, art. 4", D165, "Ai dirigenti spetta l'adozione degli atti e provvedimenti amministrativi")

D("amm-027", "Pubblico impiego", 2, "Come avviene, di regola, l'assunzione nelle pubbliche amministrazioni?",
  "Con contratto individuale di lavoro, tramite procedure selettive", ["Con decreto di nomina del ministro", "Per chiamata diretta del dirigente", "Con elezione da parte del consiglio"],
  "Art. 35: l'assunzione avviene con contratto individuale di lavoro, tramite procedure selettive che garantiscano l'accesso dall'esterno.",
  "D.Lgs. 165/2001, art. 35", D165, "avviene con contratto individuale di lavoro: a) tramite procedure selettive")

# --- Trasparenza e anticorruzione ---
D("amm-028", "Trasparenza", 3, "In base al D.Lgs. 33/2013, chi può chiedere i dati e i documenti detenuti dalle pubbliche amministrazioni, ulteriori a quelli da pubblicare (accesso civico generalizzato)?",
  "Chiunque", ["Solo chi ha un interesse diretto, concreto e attuale", "Solo i giornalisti iscritti all'albo", "Solo i residenti nel territorio dell'ente"],
  "Art. 5, comma 2: chiunque ha diritto di accedere ai dati e documenti detenuti dalle amministrazioni, ulteriori rispetto a quelli oggetto di pubblicazione.",
  "D.Lgs. 33/2013, art. 5", D33, "chiunque ha diritto di accedere ai dati e ai documenti detenuti dalle pubbliche amministrazioni")

D("amm-029", "Trasparenza", 2, "Se un'amministrazione non pubblica un documento che è obbligata a pubblicare, chi può richiederlo con l'accesso civico «semplice»?",
  "Chiunque", ["Solo il diretto interessato", "Solo il Responsabile della trasparenza", "Solo l'ANAC"],
  "Art. 5, comma 1: l'obbligo di pubblicazione comporta il diritto di chiunque di richiedere i documenti, nei casi in cui ne sia stata omessa la pubblicazione.",
  "D.Lgs. 33/2013, art. 5", D33, "comporta il diritto di chiunque di richiedere i medesimi")

D("amm-030", "Trasparenza", 1, "Come si chiama la sezione del sito istituzionale dove le amministrazioni pubblicano i dati previsti dal D.Lgs. 33/2013?",
  "Amministrazione trasparente", ["Albo pretorio", "Area riservata", "Portale dei servizi"],
  "Il D.Lgs. 33/2013 prevede la sezione «Amministrazione trasparente» del sito istituzionale.",
  "D.Lgs. 33/2013", D33, "della sezione \"Amministrazione trasparente\"")

D("amm-031", "Anticorruzione", 2, "Quale autorità individua la L. 190/2012 in ambito nazionale per la prevenzione della corruzione?",
  "L'Autorità nazionale anticorruzione (ANAC)", ["La Corte dei conti", "Il Garante per la privacy", "L'Autorità garante della concorrenza e del mercato"],
  "L'art. 1 della L. 190/2012 individua l'Autorità nazionale anticorruzione e gli altri organi incaricati del controllo e della prevenzione.",
  "L. 190/2012, art. 1", L190, "la presente legge individua, in ambito nazionale, l'Autorità nazionale anticorruzione")

D("amm-032", "Anticorruzione", 3, "Tra chi viene individuato, di norma, il Responsabile della prevenzione della corruzione e della trasparenza (RPCT)?",
  "Tra i dirigenti di ruolo in servizio", ["Tra i consiglieri comunali", "Tra i revisori dei conti esterni", "Tra i dipendenti a tempo determinato"],
  "L'organo di indirizzo individua l'RPCT, di norma tra i dirigenti di ruolo in servizio (art. 1, comma 7, L. 190/2012).",
  "L. 190/2012, art. 1", L190, "di norma tra i dirigenti di ruolo in servizio, il Responsabile della prevenzione della corruzione e della trasparenza")

D("amm-033", "Codice di comportamento", 2, "Secondo il codice di comportamento dei dipendenti pubblici, quale è il valore orientativo massimo dei regali di «modico valore»?",
  "150 euro", ["50 euro", "250 euro", "500 euro"],
  "Art. 4 del D.P.R. 62/2013: sono di modico valore i regali di valore non superiore, in via orientativa, a 150 euro, anche sotto forma di sconto.",
  "D.P.R. 62/2013, art. 4", P62, "non superiore, in via orientativa, a 150 euro")

D("amm-034", "Codice di comportamento", 4, "I codici di comportamento delle singole amministrazioni possono fissare un limite per i regali diverso da 150 euro?",
  "Sì, possono prevedere limiti inferiori, anche fino all'esclusione", ["No, il limite è fisso per tutti", "Sì, ma solo superiori", "Solo con il consenso dell'ANAC"],
  "Art. 4, comma 5: i codici delle singole amministrazioni possono prevedere limiti inferiori, anche fino all'esclusione della possibilità di riceverli.",
  "D.P.R. 62/2013, art. 4", P62, "I codici di comportamento adottati dalle singole amministrazioni possono prevedere limiti")

# --- D.P.R. 445/2000 ---
D("amm-035", "Documentazione amministrativa", 2, "Quanto valgono, salvo diversa disposizione, i certificati che attestano stati e fatti soggetti a modificazione?",
  "Sei mesi dalla data di rilascio", ["Tre mesi", "Un anno", "Hanno validità illimitata"],
  "Art. 41 del D.P.R. 445/2000: i certificati non relativi a stati immutabili hanno validità di sei mesi dalla data di rilascio, salvo validità superiore prevista dalla legge.",
  "D.P.R. 445/2000, art. 41", P445, "Le restanti certificazioni hanno validità di sei mesi dalla data di rilascio")

D("amm-036", "Documentazione amministrativa", 2, "Con quale strumento il cittadino sostituisce i normali certificati (es. residenza, titolo di studio) nei rapporti con la PA?",
  "Dichiarazioni sostitutive di certificazioni (autocertificazione)", ["Atto notarile", "Testimonianza davanti al sindaco", "Visura camerale"],
  "Art. 46 del D.P.R. 445/2000: stati, qualità e fatti elencati sono comprovati con dichiarazioni sottoscritte dall'interessato in sostituzione delle certificazioni.",
  "D.P.R. 445/2000, art. 46", P445, "prodotte in sostituzione delle normali certificazioni")

D("amm-037", "Documentazione amministrativa", 3, "Quale strumento si usa per dichiarare che la copia di un documento è conforme all'originale, senza autenticazione?",
  "La dichiarazione sostitutiva dell'atto di notorietà", ["La dichiarazione sostitutiva di certificazione", "Il certificato anagrafico", "L'atto di notorietà davanti al giudice"],
  "Art. 19 del D.P.R. 445/2000: la dichiarazione sostitutiva dell'atto di notorietà (art. 47) può attestare la conformità all'originale della copia.",
  "D.P.R. 445/2000, art. 19", P445, "La dichiarazione sostitutiva dell'atto di notorietà di cui all'articolo 47 può riguardare anche il fatto che la copia")

# --- Codice dei contratti pubblici ---
D("amm-038", "Contratti pubblici", 2, "Quale principio apre il Codice dei contratti pubblici del 2023 (D.Lgs. 36/2023), all'art. 1?",
  "Il principio del risultato", ["Il principio del prezzo più basso", "Il principio di rotazione", "Il principio di territorialità"],
  "Il D.Lgs. 36/2023 si apre con il principio del risultato (art. 1), seguito da quello della fiducia (art. 2) e dell'accesso al mercato (art. 3).",
  "D.Lgs. 36/2023, art. 1", D36, "Articolo 1 Principio del risultato")

D("amm-039", "Contratti pubblici", 3, "Su quale principio si fonda, secondo l'art. 2 del D.Lgs. 36/2023, l'attribuzione e l'esercizio del potere nel settore dei contratti pubblici?",
  "Sulla reciproca fiducia tra amministrazione, funzionari e operatori economici", ["Sul controllo preventivo della Corte dei conti", "Sulla discrezionalità assoluta della stazione appaltante", "Sull'autorizzazione dell'ANAC per ogni gara"],
  "L'art. 2 introduce il principio della fiducia nell'azione legittima, trasparente e corretta dell'amministrazione, dei suoi funzionari e degli operatori economici.",
  "D.Lgs. 36/2023, art. 2", D36, "si fonda sul principio della reciproca fiducia")

D("amm-040", "Contratti pubblici", 3, "Come si chiama, nel Codice dei contratti del 2023, la figura che sostituisce il «responsabile unico del procedimento»?",
  "Responsabile unico del progetto (RUP)", ["Direttore generale dei lavori", "Responsabile della transizione digitale", "Coordinatore della sicurezza"],
  "Il D.Lgs. 36/2023 mantiene la sigla RUP ma la riferisce al responsabile unico del progetto, che segue tutte le fasi dell'intervento.",
  "D.Lgs. 36/2023, art. 15", D36, "il responsabile unico del progetto")

D("amm-041", "Enti locali", 5, "Un sindaco firma da solo un contratto d'appalto per conto del comune, senza alcun atto del dirigente competente. Quale principio viola?",
  "La separazione tra indirizzo politico (organi di governo) e gestione (dirigenti)", ["Il principio di sussidiarietà verticale", "Il principio del contraddittorio", "Il principio di rotazione degli incarichi"],
  "L'art. 107 TUEL riserva ai dirigenti gli atti di gestione, compresa la stipula dei contratti; gli organi politici danno indirizzi e controllano.",
  "D.Lgs. 267/2000 (TUEL), art. 107", TUEL, "Questi si uniformano al principio per cui i poter")


# --- Blocco 2: L. 241/1990 (testo vigente) ---
def L(id, arg, liv, testo, giusta, sbagliate, spieg, art, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, f"L. 241/1990, {art}", L241, frase)

L("amm-042", "Principi", 2, "Secondo l'art. 1 della L. 241/1990, come agisce la PA quando adotta atti di natura non autoritativa?",
  "Secondo le norme di diritto privato, salvo che la legge disponga diversamente", ["Sempre con provvedimenti autoritativi", "Secondo le norme del codice penale", "Solo previa autorizzazione del prefetto"],
  "Il comma 1-bis stabilisce che negli atti non autoritativi la PA agisce secondo il diritto privato, salvo diversa previsione di legge.",
  "art. 1, c. 1-bis", "agisce secondo le norme di diritto privato salvo che la legge disponga diversamente")

L("amm-043", "Principi", 2, "Quando la PA può aggravare il procedimento amministrativo?",
  "Solo per straordinarie e motivate esigenze imposte dall'istruttoria", ["Ogni volta che lo ritiene opportuno", "Mai, in nessun caso", "Solo su richiesta del privato"],
  "Il divieto di aggravamento (art. 1, c. 2) ammette eccezioni solo per esigenze straordinarie e motivate dell'istruttoria.",
  "art. 1, c. 2", "non può aggravare il procedimento se non per straordinarie e motivate esigenze")

L("amm-044", "Principi", 3, "A quali principi sono improntati i rapporti tra cittadino e PA secondo l'art. 1, c. 2-bis?",
  "Collaborazione e buona fede", ["Gerarchia e obbedienza", "Segretezza e riservatezza", "Onerosità e reciprocità"],
  "Il comma 2-bis, introdotto nel 2020, richiama i principi di collaborazione e buona fede.",
  "art. 1, c. 2-bis", "sono improntati ai principi della collaborazione e della buona fede")

L("amm-045", "Principi", 3, "I soggetti privati che esercitano attività amministrative devono rispettare i principi della L. 241/1990?",
  "Sì, con un livello di garanzia non inferiore a quello delle pubbliche amministrazioni", ["No, perché sono soggetti privati", "Solo se lo prevede il loro statuto", "Solo per l'accesso ai documenti"],
  "Il comma 1-ter estende criteri e principi ai privati preposti all'esercizio di attività amministrative.",
  "art. 1, c. 1-ter", "con un livello di garanzia non inferiore a quello cui sono tenute le pubbliche")

L("amm-046", "Conclusione del procedimento", 3, "Come conclude la PA un procedimento su una domanda manifestamente irricevibile o infondata?",
  "Con un provvedimento espresso in forma semplificata", ["Archiviando la domanda senza alcun atto", "Con il silenzio-rigetto", "Rinviando la domanda al TAR"],
  "L'art. 2, c. 1 consente un provvedimento in forma semplificata, con motivazione sintetica sul punto risolutivo.",
  "art. 2, c. 1", "concludono il procedimento con un provvedimento espresso redatto in forma semplificata")

L("amm-047", "Conclusione del procedimento", 3, "Qual è il termine massimo che i DPCM possono fissare per i procedimenti statali, nei casi ordinari?",
  "Novanta giorni", ["Trenta giorni", "Sessanta giorni", "Un anno"],
  "I decreti dell'art. 2, c. 3 individuano termini non superiori a novanta giorni; oltre servono le condizioni del comma 4.",
  "art. 2, c. 3", "sono individuati i termini non superiori a novanta giorni")

L("amm-048", "Conclusione del procedimento", 4, "Qual è il limite massimo, salvo eccezioni, per i termini dei procedimenti statali particolarmente complessi?",
  "Centottanta giorni", ["Novanta giorni", "Trecentosessantacinque giorni", "Duecentoquaranta giorni"],
  "Il comma 4 ammette termini oltre i 90 giorni ma mai superiori a 180, esclusi cittadinanza e immigrazione.",
  "art. 2, c. 4", "non possono comunque superare i centottanta giorni")

L("amm-049", "Conclusione del procedimento", 4, "Quali procedimenti sono esclusi dal limite dei 180 giorni dell'art. 2, c. 4?",
  "Quelli per l'acquisto della cittadinanza italiana e quelli sull'immigrazione", ["Quelli tributari", "Quelli degli enti locali", "Quelli relativi ai concorsi pubblici"],
  "Il comma 4 esclude espressamente dal limite i procedimenti di acquisto della cittadinanza e quelli sull'immigrazione.",
  "art. 2, c. 4", "con la sola esclusione dei procedimenti di acquisto della cittadinanza italiana")

L("amm-050", "Conclusione del procedimento", 2, "Da quando decorre il termine di un procedimento ad iniziativa di parte?",
  "Dal ricevimento della domanda", ["Dalla nomina del responsabile del procedimento", "Dalla data di protocollazione interna dell'ufficio", "Dalla prima riunione istruttoria"],
  "L'art. 2, c. 6 fa decorrere i termini dall'inizio d'ufficio o dal ricevimento della domanda, se il procedimento è a istanza di parte.",
  "art. 2, c. 6", "dal ricevimento della domanda, se il procedimento è ad iniziativa di parte")

L("amm-051", "Conclusione del procedimento", 3, "Quante volte e per quanto tempo possono essere sospesi i termini per acquisire informazioni o certificazioni?",
  "Una sola volta, per non più di trenta giorni", ["Due volte, per sessanta giorni ciascuna", "Senza limiti", "Una sola volta, per novanta giorni"],
  "L'art. 2, c. 7 consente una sola sospensione, non superiore a trenta giorni.",
  "art. 2, c. 7", "per una sola volta e per un periodo non superiore a trenta giorni")

L("amm-052", "Conclusione del procedimento", 3, "Quale codice disciplina la tutela contro il silenzio dell'amministrazione?",
  "Il codice del processo amministrativo (D.Lgs. 104/2010)", ["Il codice civile", "Il codice di procedura penale", "Il codice dell'amministrazione digitale"],
  "Il comma 8 rinvia al codice del processo amministrativo; le sentenze che accolgono il ricorso sono trasmesse alla Corte dei conti.",
  "art. 2, c. 8", "è disciplinata dal codice del processo amministrativo")

L("amm-053", "Conclusione del procedimento", 4, "Che cosa costituisce la mancata o tardiva emanazione del provvedimento per il dirigente o funzionario inadempiente?",
  "Elemento di valutazione della performance e di responsabilità disciplinare e amministrativo-contabile", ["Un reato di omissione d'atti d'ufficio in ogni caso", "Nessuna conseguenza", "Causa automatica di licenziamento"],
  "Il comma 9 collega il ritardo alla valutazione della performance e alla responsabilità disciplinare e contabile.",
  "art. 2, c. 9", "costituisce elemento di valutazione della performance individuale")

L("amm-054", "Conclusione del procedimento", 4, "Se l'organo di governo non individua il titolare del potere sostitutivo, a chi è attribuito?",
  "Al dirigente generale o, in mancanza, al dirigente preposto all'ufficio o al funzionario di più elevato livello", ["Al prefetto", "Al sindaco", "Al difensore civico"],
  "Il comma 9-bis stabilisce questa attribuzione automatica in caso di omessa individuazione.",
  "art. 2, c. 9-bis", "il potere sostitutivo si considera attribuito al dirigente generale")

L("amm-055", "Conclusione del procedimento", 4, "Entro quale termine il titolare del potere sostitutivo conclude il procedimento?",
  "Entro un termine pari alla metà di quello originariamente previsto", ["Entro lo stesso termine originario", "Entro il doppio del termine originario", "Entro dieci giorni in ogni caso"],
  "Il comma 9-ter: il sostituto conclude il procedimento entro metà del termine originario, con le strutture competenti o con un commissario.",
  "art. 2, c. 9-ter", "entro un termine pari alla metà di quello originariamente previsto")

L("amm-056", "Conclusione del procedimento", 5, "Entro quale data il titolare del potere sostitutivo comunica all'organo di governo i procedimenti in cui il termine non è stato rispettato?",
  "Entro il 30 gennaio di ogni anno", ["Entro il 31 dicembre", "Entro il 30 giugno", "Entro il 31 marzo"],
  "Il comma 9-quater prevede una comunicazione annuale entro il 30 gennaio.",
  "art. 2, c. 9-quater", "entro il 30 gennaio di ogni anno")

L("amm-057", "Conclusione del procedimento", 3, "Cosa devono indicare i provvedimenti rilasciati in ritardo su istanza di parte?",
  "Il termine previsto e quello effettivamente impiegato", ["Solo il nome del dirigente responsabile", "Le scuse dell'amministrazione", "L'importo del risarcimento dovuto"],
  "Il comma 9-quinquies impone di indicare il termine di legge o regolamento e quello effettivo.",
  "art. 2, c. 9-quinquies", "il termine previsto dalla legge o dai regolamenti e quello effettivamente impiegato")

L("amm-058", "Conclusione del procedimento", 4, "Per il danno ingiusto da inosservanza del termine di conclusione, la PA risponde:",
  "Se l'inosservanza è dolosa o colposa", ["Solo se l'inosservanza è dolosa", "Mai, il ritardo non è risarcibile", "Solo per i procedimenti tributari"],
  "L'art. 2-bis prevede il risarcimento del danno ingiusto da inosservanza dolosa o colposa del termine.",
  "art. 2-bis, c. 1", "inosservanza dolosa o colposa del termine di conclusione del procedimento")

L("amm-059", "Conclusione del procedimento", 5, "L'indennizzo per il mero ritardo (art. 2-bis, c. 1-bis) spetta anche nei concorsi pubblici?",
  "No, i concorsi pubblici sono esclusi", ["Sì, sempre", "Sì, ma solo per i vincitori", "Solo se il concorso dura più di un anno"],
  "Il comma 1-bis esclude dall'indennizzo le ipotesi di silenzio qualificato e i concorsi pubblici.",
  "art. 2-bis, c. 1-bis", "ad esclusione delle ipotesi di silenzio qualificato e dei concorsi pubblici")

L("amm-060", "Motivazione", 2, "Che cosa deve indicare la motivazione del provvedimento?",
  "I presupposti di fatto e le ragioni giuridiche della decisione, in relazione all'istruttoria", ["Solo le norme applicate", "Solo il nome del responsabile", "L'opinione personale del dirigente"],
  "L'art. 3, c. 1 richiede presupposti di fatto e ragioni giuridiche, in relazione alle risultanze dell'istruttoria.",
  "art. 3, c. 1", "La motivazione deve indicare i presupposti di fatto e le ragioni giuridiche")

L("amm-061", "Motivazione", 2, "Per quali atti la motivazione NON è richiesta?",
  "Per gli atti normativi e per quelli a contenuto generale", ["Per i provvedimenti sui concorsi", "Per gli atti relativi al personale", "Per i provvedimenti di diniego"],
  "L'art. 3, c. 2 esclude la motivazione per atti normativi e a contenuto generale.",
  "art. 3, c. 2", "La motivazione non è richiesta per gli atti normativi e per quelli a contenuto generale")

L("amm-062", "Motivazione", 3, "Come si chiama la motivazione che rinvia alle ragioni contenute in un altro atto, da rendere disponibile?",
  "Motivazione per relationem", ["Motivazione postuma", "Motivazione apparente", "Motivazione implicita"],
  "L'art. 3, c. 3 ammette che le ragioni risultino da altro atto richiamato, che deve essere indicato e reso disponibile.",
  "art. 3, c. 3", "Se le ragioni della decisione risultano da altro atto dell'amministrazione richiamato")

L("amm-063", "Motivazione", 2, "Cosa deve indicare ogni atto notificato al destinatario?",
  "Il termine e l'autorità cui è possibile ricorrere", ["Il costo del procedimento", "Il numero di dipendenti dell'ufficio", "L'elenco dei controinteressati"],
  "L'art. 3, c. 4 impone di indicare termine e autorità per il ricorso.",
  "art. 3, c. 4", "devono essere indicati il termine e l'autorità cui è possibile ricorrere")

L("amm-064", "Responsabile del procedimento", 2, "Chi assegna la responsabilità del procedimento?",
  "Il dirigente dell'unità organizzativa, a sé o a un altro dipendente dell'unità", ["Il sindaco", "Il privato interessato", "Il segretario generale in ogni caso"],
  "L'art. 5, c. 1 attribuisce al dirigente l'assegnazione della responsabilità dell'istruttoria.",
  "art. 5, c. 1", "provvede ad assegnare a sé o altro dipendente addetto all'unità")

L("amm-065", "Responsabile del procedimento", 3, "Finché non avviene l'assegnazione, chi è responsabile del procedimento?",
  "Il funzionario preposto all'unità organizzativa competente", ["Nessuno", "Il dipendente più anziano", "L'organo politico"],
  "L'art. 5, c. 2 individua come responsabile il funzionario preposto all'unità organizzativa.",
  "art. 5, c. 2", "è considerato responsabile del singolo procedimento il funzionario preposto")

L("amm-066", "Responsabile del procedimento", 3, "Quale di questi NON è un compito del responsabile del procedimento (art. 6)?",
  "Giudicare i ricorsi contro il provvedimento finale", ["Accertare d'ufficio i fatti", "Curare comunicazioni, pubblicazioni e notificazioni", "Proporre l'indizione della conferenza di servizi"],
  "L'art. 6 elenca compiti istruttori, comunicazioni e proposta o indizione delle conferenze; i ricorsi spettano al giudice o agli organi competenti.",
  "art. 6", "cura le comunicazioni, le pubblicazioni e le notificazioni")

L("amm-067", "Responsabile del procedimento", 4, "L'organo competente all'adozione può discostarsi dalle risultanze istruttorie del responsabile del procedimento?",
  "Sì, ma indicandone la motivazione nel provvedimento finale", ["No, mai", "Sì, liberamente e senza motivare", "Solo con il parere del Consiglio di Stato"],
  "L'art. 6, lett. e) consente di discostarsi solo motivando nel provvedimento finale.",
  "art. 6", "non può discostarsi dalle risultanze dell'istruttoria")

L("amm-068", "Responsabile del procedimento", 2, "Cosa devono fare responsabile del procedimento e titolari degli uffici in caso di conflitto di interessi, anche potenziale?",
  "Astenersi, segnalando la situazione di conflitto", ["Proseguire, ma informando il privato", "Chiedere un parere all'ANAC prima di decidere", "Delegare il provvedimento a un collega dello stesso ufficio senza segnalare"],
  "L'art. 6-bis impone l'obbligo di astensione e di segnalazione di ogni conflitto, anche potenziale.",
  "art. 6-bis", "devono astenersi in caso di conflitto di interessi")

L("amm-069", "Partecipazione", 2, "A chi va comunicato l'avvio del procedimento?",
  "Ai destinatari diretti del provvedimento e a chi per legge deve intervenire", ["Solo al sindaco", "A tutti i cittadini residenti", "Solo agli avvocati delle parti"],
  "L'art. 7 indica i soggetti su cui il provvedimento produce effetti diretti e quelli che per legge devono intervenire.",
  "art. 7", "ai soggetti nei confronti dei quali il provvedimento finale è destinato a produrre effetti diretti")

L("amm-070", "Partecipazione", 3, "La PA può adottare provvedimenti cautelari prima di comunicare l'avvio del procedimento?",
  "Sì, resta salva questa facoltà", ["No, mai", "Solo con l'autorizzazione del giudice", "Solo nei procedimenti tributari"],
  "L'art. 7, c. 2 fa salva la facoltà di adottare provvedimenti cautelari anche prima delle comunicazioni.",
  "art. 7, c. 2", "resta salva la facoltà dell'amministrazione di adottare")

L("amm-071", "Partecipazione", 3, "Come si comunica l'avvio del procedimento se i destinatari sono troppo numerosi?",
  "Con forme di pubblicità idonee stabilite dall'amministrazione", ["Non si comunica affatto", "Solo tramite raccomandata a ciascuno", "Con un decreto del Presidente della Repubblica"],
  "L'art. 8, c. 3 ammette forme di pubblicità idonee quando la comunicazione personale è impossibile o gravosa.",
  "art. 8, c. 3", "mediante forme di pubblicità idonee di volta in volta stabilite")

L("amm-072", "Partecipazione", 4, "Chi può far valere l'omissione di una comunicazione prescritta?",
  "Solo il soggetto nel cui interesse la comunicazione è prevista", ["Chiunque", "Solo il pubblico ministero", "Solo l'amministrazione stessa"],
  "L'art. 8, c. 4 limita la legittimazione al soggetto nel cui interesse la comunicazione è prevista.",
  "art. 8, c. 4", "può esser fatta valere solo dal soggetto nel cui interesse la comunicazione è prevista")

L("amm-073", "Partecipazione", 3, "Chi può intervenire nel procedimento ai sensi dell'art. 9?",
  "I portatori di interessi pubblici o privati e di interessi diffusi costituiti in associazioni o comitati, cui possa derivare un pregiudizio", ["Solo i destinatari del provvedimento", "Solo gli enti pubblici", "Solo chi ha la residenza nel comune"],
  "L'art. 9 apre l'intervento a chiunque possa subire un pregiudizio, compresi gli interessi diffusi organizzati.",
  "art. 9", "nonché i portatori di interessi diffusi costituiti in associazioni o comitati")

L("amm-074", "Partecipazione", 2, "Quali diritti hanno i partecipanti al procedimento (art. 10)?",
  "Prendere visione degli atti e presentare memorie scritte e documenti", ["Adottare il provvedimento finale", "Nominare il responsabile del procedimento", "Sospendere il procedimento a loro scelta"],
  "L'art. 10 riconosce la visione degli atti e la presentazione di memorie e documenti, che la PA deve valutare se pertinenti.",
  "art. 10", "di presentare memorie scritte e documenti")

L("amm-075", "Partecipazione", 4, "Che effetto ha il preavviso di rigetto (art. 10-bis) sui termini del procedimento?",
  "Li sospende: ricominciano dieci giorni dopo le osservazioni o dalla scadenza del termine per presentarle", ["Li interrompe e ricominciano da zero", "Non ha alcun effetto", "Li raddoppia"],
  "Dal 2020 la comunicazione dei motivi ostativi sospende (non interrompe) i termini.",
  "art. 10-bis", "sospende i termini di conclusione dei procedimenti")

L("amm-076", "Partecipazione", 4, "A quali procedimenti NON si applica il preavviso di rigetto?",
  "Alle procedure concorsuali e ai procedimenti previdenziali e assistenziali gestiti dagli enti previdenziali", ["Ai procedimenti a istanza di parte", "Ai procedimenti degli enti locali", "Ai procedimenti di rilascio di autorizzazioni"],
  "L'art. 10-bis esclude le procedure concorsuali e alcuni procedimenti previdenziali e assistenziali.",
  "art. 10-bis", "non si applicano alle procedure concorsuali")

L("amm-077", "Partecipazione", 4, "Dopo l'annullamento giudiziale di un diniego, la PA può addurre motivi ostativi nuovi già emergenti dall'istruttoria?",
  "No, non può addurli per la prima volta", ["Sì, sempre", "Sì, se li comunica entro dieci giorni", "Solo con il consenso del giudice"],
  "L'art. 10-bis vieta di addurre per la prima volta motivi già emergenti dall'istruttoria del provvedimento annullato.",
  "art. 10-bis", "non può addurre per la prima volta motivi ostativi già emergenti")

L("amm-078", "Accordi", 3, "In quale forma devono essere stipulati gli accordi integrativi o sostitutivi del provvedimento?",
  "Per atto scritto, a pena di nullità, salvo che la legge disponga altrimenti", ["Anche oralmente", "Solo per atto notarile", "Con semplice scambio di email"],
  "L'art. 11, c. 2 richiede la forma scritta a pena di nullità; si applicano i principi del codice civile su obbligazioni e contratti.",
  "art. 11, c. 2", "a pena di nullità per atto scritto")

L("amm-079", "Accordi", 4, "Quando può la PA recedere unilateralmente da un accordo ex art. 11?",
  "Per sopravvenuti motivi di pubblico interesse, salvo l'obbligo di indennizzo", ["In qualsiasi momento senza conseguenze", "Mai", "Solo con il consenso del privato"],
  "L'art. 11, c. 4 ammette il recesso per sopravvenuti motivi di pubblico interesse, con indennizzo dei pregiudizi.",
  "art. 11, c. 4", "Per sopravvenuti motivi di pubblico interesse l'amministrazione recede unilateralmente dall'accordo")

L("amm-080", "Accordi", 3, "Cosa deve precedere la stipulazione di un accordo ex art. 11?",
  "Una determinazione dell'organo che sarebbe competente per adottare il provvedimento", ["Un parere del Consiglio di Stato", "Un referendum locale", "L'autorizzazione del prefetto"],
  "Il comma 4-bis, a garanzia di imparzialità e buon andamento, richiede una determinazione dell'organo competente.",
  "art. 11, c. 4-bis", "la stipulazione dell'accordo è preceduta da una determinazione dell'organo")

L("amm-081", "Accordi", 3, "A cosa è subordinata la concessione di sovvenzioni, contributi e vantaggi economici (art. 12)?",
  "Alla predeterminazione dei criteri e delle modalità da parte dell'amministrazione", ["Alla sola richiesta dell'interessato", "Al parere della Corte dei conti", "All'estrazione a sorte dei beneficiari"],
  "L'art. 12 impone di predeterminare criteri e modalità, la cui osservanza deve risultare dai singoli provvedimenti.",
  "art. 12", "sono subordinate alla predeterminazione")

L("amm-082", "Partecipazione", 4, "A quali attività NON si applicano le norme sulla partecipazione (art. 13)?",
  "Agli atti normativi, amministrativi generali, di pianificazione e di programmazione", ["Ai provvedimenti a istanza di parte", "Ai provvedimenti sanzionatori", "Ai provvedimenti di autorizzazione"],
  "L'art. 13 esclude gli atti normativi, generali, di pianificazione e programmazione, oltre ai procedimenti tributari.",
  "art. 13", "diretta alla emanazione di atti normativi, amministrativi generali, di pianificazione e di programmazione")

L("amm-083", "Conferenza di servizi", 3, "Quando è sempre indetta la conferenza di servizi decisoria?",
  "Quando la conclusione positiva richiede più pareri, nulla osta o assensi di diverse amministrazioni", ["Quando lo chiede un qualsiasi cittadino", "Solo per le opere pubbliche statali", "Solo in caso di ricorso al TAR"],
  "L'art. 14, c. 2 rende obbligatoria la conferenza decisoria quando servono più atti di assenso di diverse amministrazioni.",
  "art. 14, c. 2", "La conferenza di servizi decisoria è sempre indetta dall'amministrazione procedente")

L("amm-084", "Conferenza di servizi", 3, "In quale forma si svolge, di regola, la conferenza decisoria?",
  "In forma semplificata e in modalità asincrona", ["In forma simultanea e sincrona", "Per iscritto, presso il Consiglio di Stato", "In assemblea pubblica"],
  "L'art. 14-bis stabilisce la forma semplificata e asincrona, salvo i casi dei commi 6 e 7.",
  "art. 14-bis, c. 1", "si svolge in forma semplificata e in modalità asincrona")

L("amm-085", "Conferenza di servizi", 4, "Nella conferenza semplificata, qual è il termine massimo ordinario per le determinazioni delle amministrazioni coinvolte?",
  "Trenta giorni (sessanta per le amministrazioni preposte a tutele sensibili)", ["Dieci giorni", "Novanta giorni", "Centottanta giorni"],
  "L'art. 14-bis, c. 2, lett. c) fissa un termine non superiore a 30 giorni, 60 per ambiente, paesaggio, beni culturali e salute.",
  "art. 14-bis, c. 2", "il termine perentorio, comunque non superiore a trenta giorni")

L("amm-086", "Conferenza di servizi", 4, "Nella conferenza semplificata, che valore ha la mancata comunicazione della determinazione entro il termine?",
  "Equivale ad assenso senza condizioni", ["Equivale a dissenso", "Blocca la conferenza", "Obbliga a ripetere la conferenza"],
  "L'art. 14-bis, c. 4 equipara il silenzio ad assenso senza condizioni, salvi i casi in cui il diritto UE richiede provvedimenti espressi.",
  "art. 14-bis, c. 4", "equivalgono ad assenso senza condizioni")

L("amm-087", "Conferenza di servizi", 4, "Da chi sono rappresentate le amministrazioni statali in una conferenza simultanea a cui partecipano anche amministrazioni non statali?",
  "Da un unico rappresentante nominato dal Presidente del Consiglio o, per le sole periferiche, dal Prefetto", ["Da un rappresentante per ogni ministero", "Dal Presidente della Repubblica", "Dal Ministro dell'interno"],
  "L'art. 14-ter, c. 4 prevede un rappresentante unico delle amministrazioni statali.",
  "art. 14-ter, c. 4", "le amministrazioni statali sono rappresentate da un unico soggetto")

L("amm-088", "Conferenza di servizi", 4, "Cosa sostituisce la determinazione motivata di conclusione della conferenza?",
  "Tutti gli atti di assenso di competenza delle amministrazioni e dei gestori interessati", ["Solo il parere dell'amministrazione procedente", "Nessun atto, ha valore solo consultivo", "Le sentenze del TAR"],
  "L'art. 14-quater, c. 1: la determinazione sostituisce a ogni effetto tutti gli atti di assenso.",
  "art. 14-quater, c. 1", "sostituisce a ogni effetto tutti gli atti di assenso")

L("amm-089", "Conferenza di servizi", 5, "Entro quanti giorni le amministrazioni dissenzienti preposte a tutele sensibili possono opporsi alla determinazione conclusiva?",
  "Entro 10 giorni, con opposizione al Presidente del Consiglio dei ministri", ["Entro 60 giorni, con ricorso al TAR", "Entro 30 giorni, al Prefetto", "Entro 120 giorni, al Presidente della Repubblica"],
  "L'art. 14-quinquies prevede l'opposizione al Presidente del Consiglio entro 10 giorni dalla comunicazione.",
  "art. 14-quinquies", "entro 10 giorni dalla sua comunicazione")

L("amm-090", "Accordi", 3, "Come devono essere sottoscritti gli accordi fra pubbliche amministrazioni (art. 15)?",
  "Con firma digitale, firma elettronica avanzata o altra firma elettronica qualificata, pena la nullità", ["Con firma autografa davanti a un notaio", "Con semplice email", "Non serve sottoscrizione"],
  "Il comma 2-bis impone la firma digitale o elettronica qualificata/avanzata, a pena di nullità.",
  "art. 15, c. 2-bis", "sono sottoscritti con firma digitale")

L("amm-091", "Attività consultiva", 3, "Entro quanti giorni gli organi consultivi devono rendere i pareri obbligatori?",
  "Venti giorni dal ricevimento della richiesta", ["Dieci giorni", "Trenta giorni", "Novanta giorni"],
  "L'art. 16, c. 1 fissa venti giorni sia per i pareri obbligatori sia, come limite massimo, per quelli facoltativi.",
  "art. 16, c. 1", "entro venti giorni dal ricevimento della richiesta")

L("amm-092", "Attività consultiva", 4, "Se il parere obbligatorio non arriva nel termine, cosa fa l'amministrazione richiedente?",
  "Procede indipendentemente dall'espressione del parere", ["Deve attendere senza limiti", "Deve archiviare il procedimento", "Deve chiedere l'intervento del giudice"],
  "L'art. 16, c. 2 consente di procedere senza parere, salve le esclusioni per ambiente, paesaggio, territorio e salute.",
  "art. 16, c. 2", "procede indipendentemente dall'espressione del parere")

L("amm-093", "Attività consultiva", 4, "La regola per cui si procede senza parere vale anche per le amministrazioni preposte alla tutela ambientale e della salute?",
  "No, per esse non si applica", ["Sì, sempre", "Sì, ma il termine si dimezza", "Solo per i pareri facoltativi"],
  "L'art. 16, c. 3 esclude i pareri delle amministrazioni preposte alla tutela ambientale, paesaggistica, territoriale e della salute.",
  "art. 16, c. 3", "non si applicano in caso di pareri che debbano essere rilasciati da amministrazioni preposte alla tutela ambientale")

L("amm-094", "Attività consultiva", 4, "Se gli organi tecnici non rendono le valutazioni tecniche entro il termine (o entro 90 giorni), cosa deve fare il responsabile del procedimento?",
  "Chiederle ad altri organi o enti pubblici con qualificazione equipollente, o a istituti universitari", ["Procedere senza valutazioni", "Archiviare la pratica", "Nominare un consulente privato a sua scelta"],
  "A differenza dei pareri, per le valutazioni tecniche l'art. 17 impone di rivolgersi ad altri organi qualificati.",
  "art. 17, c. 1", "ovvero ad istituti universitari")

L("amm-095", "Silenzio tra amministrazioni", 4, "Nel silenzio-assenso tra amministrazioni (art. 17-bis), entro quanti giorni va comunicato l'assenso, di regola?",
  "Trenta giorni dal ricevimento dello schema di provvedimento", ["Dieci giorni", "Sessanta giorni", "Centottanta giorni"],
  "Decorsi i trenta giorni (novanta per le amministrazioni preposte a tutele sensibili), l'assenso si intende acquisito.",
  "art. 17-bis, c. 1", "comunicano il proprio assenso, concerto o nulla osta entro trenta giorni")

L("amm-096", "Silenzio tra amministrazioni", 5, "Qual è il termine dell'art. 17-bis per le amministrazioni preposte alla tutela ambientale, dei beni culturali e della salute?",
  "Novanta giorni, salvo termine diverso", ["Trenta giorni", "Sessanta giorni", "Il silenzio-assenso non si applica mai a loro"],
  "L'art. 17-bis, c. 3 estende il meccanismo anche a queste amministrazioni, con termine di novanta giorni.",
  "art. 17-bis, c. 3", "è di novanta giorni dal ricevimento della richiesta")

L("amm-097", "Semplificazione", 2, "Come acquisisce la PA i documenti già in possesso di altre pubbliche amministrazioni?",
  "D'ufficio: all'interessato può chiedere solo gli elementi per trovarli", ["Li chiede sempre al cittadino", "Il cittadino deve presentarli in originale", "Tramite il notaio"],
  "L'art. 18, c. 2 impone l'acquisizione d'ufficio dei documenti detenuti dalla PA.",
  "art. 18, c. 2", "sono acquisiti d'ufficio quando sono in possesso dell'amministrazione procedente")

L("amm-098", "Semplificazione", 3, "Cosa attesta la ricevuta rilasciata alla presentazione di un'istanza o segnalazione (art. 18-bis)?",
  "L'avvenuta presentazione e i termini entro cui la PA deve rispondere o il silenzio vale accoglimento", ["Solo l'identità del richiedente", "L'esito favorevole della domanda", "Il pagamento dei diritti di segreteria"],
  "La ricevuta indica anche i termini e, se contiene gli elementi dell'art. 8, vale come comunicazione di avvio.",
  "art. 18-bis", "una ricevuta, che attesta l'avvenuta presentazione")

L("amm-099", "Semplificazione", 4, "L'istanza produce effetti se la PA non rilascia la ricevuta?",
  "Sì, ferma la responsabilità del soggetto competente", ["No, è come non presentata", "Solo se inviata per PEC", "Solo dopo un sollecito scritto"],
  "L'art. 18-bis precisa che istanze e segnalazioni producono effetti anche senza ricevuta.",
  "art. 18-bis", "producono effetti anche in caso di mancato rilascio della ricevuta")

L("amm-100", "SCIA", 2, "Da quando può iniziare l'attività oggetto di SCIA?",
  "Dalla data di presentazione della segnalazione all'amministrazione competente", ["Dopo 60 giorni di silenzio", "Dopo l'autorizzazione espressa", "Dopo il sopralluogo dei tecnici"],
  "L'art. 19, c. 2 consente l'avvio immediato; la PA controlla dopo.",
  "art. 19, c. 2", "dalla data della presentazione della segnalazione all'amministrazione competente")

L("amm-101", "SCIA", 3, "Se l'attività avviata con SCIA può essere resa conforme alla legge, cosa fa la PA?",
  "Invita il privato a conformarla, fissando un termine non inferiore a trenta giorni", ["La vieta subito in ogni caso", "Archivia senza fare nulla", "Infligge solo una multa"],
  "L'art. 19, c. 3 prevede la conformazione con atto motivato; in difetto, l'attività si intende vietata.",
  "art. 19, c. 3", "con la fissazione di un termine non inferiore a trenta giorni")

L("amm-102", "SCIA", 3, "In materia edilizia, qual è il termine per i controlli sulla SCIA?",
  "Trenta giorni", ["Sessanta giorni", "Novanta giorni", "Dieci giorni"],
  "L'art. 19, c. 6-bis riduce per la SCIA edilizia il termine ordinario di sessanta giorni a trenta.",
  "art. 19, c. 6-bis", "è ridotto a trenta giorni")

L("amm-103", "SCIA", 4, "Qual è la pena per chi attesta falsamente i requisiti nelle dichiarazioni che corredano la SCIA?",
  "Reclusione da uno a tre anni, se il fatto non costituisce più grave reato", ["Solo una sanzione amministrativa", "Reclusione da cinque a dieci anni", "Nessuna pena"],
  "L'art. 19, c. 6 prevede la reclusione da uno a tre anni.",
  "art. 19, c. 6", "è punito con la reclusione da uno a tre anni")

L("amm-104", "SCIA", 5, "Un terzo che si ritiene leso da una SCIA può impugnarla direttamente come provvedimento tacito?",
  "No: può sollecitare le verifiche della PA e, in caso di inerzia, agire contro il silenzio", ["Sì, entro 60 giorni davanti al TAR", "Sì, con ricorso straordinario al Capo dello Stato", "No, non ha alcuna tutela"],
  "L'art. 19, c. 6-ter: la SCIA non è un provvedimento tacito impugnabile; si esperisce solo l'azione dell'art. 31 c.p.a.",
  "art. 19, c. 6-ter", "non costituiscono provvedimenti taciti direttamente impugnabili")

L("amm-105", "SCIA", 3, "Se un'attività richiede più SCIA e comunicazioni, cosa presenta l'interessato?",
  "Un'unica SCIA allo sportello unico", ["Una SCIA per ogni amministrazione", "Una domanda di autorizzazione ordinaria", "Nessuna SCIA, basta una PEC"],
  "L'art. 19-bis prevede la concentrazione dei regimi: un'unica SCIA allo sportello, che la trasmette alle altre amministrazioni.",
  "art. 19-bis, c. 2", "l'interessato presenta un'unica SCIA allo sportello")

L("amm-106", "Silenzio assenso", 4, "In quali casi il silenzio assenso NON si forma, anche se il termine è decorso?",
  "Se la domanda non è stata ricevuta dalla PA competente o manca degli elementi indispensabili", ["Se il dirigente era in ferie", "Se la domanda era in bollo", "Se il richiedente è una società"],
  "L'art. 20, c. 1 indica i soli due casi in cui il silenzio assenso non si forma.",
  "art. 20, c. 1", "Il silenzio assenso non si forma nei soli casi")

L("amm-107", "Silenzio assenso", 4, "Entro quanto la PA, nei procedimenti non telematizzati, deve inviare l'attestazione del silenzio assenso formato?",
  "Entro dieci giorni dalla formazione del silenzio assenso", ["Entro trenta giorni", "Entro sei mesi", "Non è tenuta a inviarla"],
  "Decorso il termine, l'attestazione è sostituita da una dichiarazione del privato ex art. 47 DPR 445/2000.",
  "art. 20, c. 2-bis", "entro dieci giorni dalla data di formazione del silenzio assenso")

L("amm-108", "Silenzio assenso", 3, "In quale di queste materie il silenzio assenso NON si applica?",
  "Pubblica sicurezza", ["Commercio al dettaglio", "Iscrizioni ad albi artigiani", "Occupazione temporanea di suolo per un'insegna"],
  "L'art. 20, c. 4 esclude patrimonio culturale, ambiente, difesa, pubblica sicurezza, immigrazione, asilo, cittadinanza, salute.",
  "art. 20, c. 4", "la difesa nazionale, la pubblica sicurezza, l'immigrazione")

L("amm-109", "Silenzio assenso", 4, "Formato il silenzio assenso, la PA può ancora intervenire?",
  "Sì, in autotutela (revoca o annullamento d'ufficio)", ["No, mai", "Solo con sentenza del giudice", "Solo entro 24 ore"],
  "L'art. 20, c. 3 richiama gli artt. 21-quinquies e 21-nonies.",
  "art. 20, c. 3", "può assumere determinazioni in via di autotutela")

L("amm-110", "Efficacia del provvedimento", 3, "Quando acquista efficacia un provvedimento limitativo della sfera giuridica dei privati?",
  "Con la comunicazione al destinatario", ["Con la firma del dirigente", "Con la pubblicazione sul sito dopo un anno", "Con il pagamento di un'imposta"],
  "L'art. 21-bis lega l'efficacia alla comunicazione; i provvedimenti cautelari e urgenti sono immediatamente efficaci.",
  "art. 21-bis", "acquista efficacia nei confronti di ciascun destinatario con la comunicazione")

L("amm-111", "Efficacia del provvedimento", 4, "Come si chiama il potere della PA di imporre coattivamente l'adempimento degli obblighi, previa diffida?",
  "Esecutorietà", ["Imperatività", "Tipicità", "Inoppugnabilità"],
  "L'art. 21-ter disciplina l'esecutorietà, nei casi e modi stabiliti dalla legge.",
  "art. 21-ter", "possono imporre coattivamente l'adempimento degli obblighi")

L("amm-112", "Efficacia del provvedimento", 4, "Per quanto tempo può essere sospesa l'efficacia di un provvedimento?",
  "Per gravi ragioni e per il tempo strettamente necessario, prorogabile una sola volta", ["Fino a dieci anni", "A tempo indeterminato", "Mai, la sospensione non è prevista"],
  "L'art. 21-quater, c. 2 consente la sospensione con termine esplicito, prorogabile o differibile una sola volta.",
  "art. 21-quater, c. 2", "per gravi ragioni e per il tempo strettamente necessario")

L("amm-113", "Autotutela", 3, "Quale effetto produce la revoca del provvedimento?",
  "Rende il provvedimento inidoneo a produrre ulteriori effetti", ["Elimina gli effetti già prodotti fin dall'origine", "Rende il provvedimento nullo", "Trasforma il provvedimento in un contratto"],
  "La revoca (art. 21-quinquies) opera per il futuro; se crea pregiudizi la PA deve indennizzare.",
  "art. 21-quinquies", "La revoca determina la inidoneità del provvedimento revocato a produrre ulteriori effetti")

L("amm-114", "Autotutela", 4, "Se la revoca incide su rapporti negoziali, come si calcola l'indennizzo?",
  "È parametrato al solo danno emergente", ["Comprende sempre il lucro cessante", "È fisso, pari a mille euro", "Non è dovuto"],
  "L'art. 21-quinquies, c. 1-bis limita l'indennizzo al danno emergente.",
  "art. 21-quinquies, c. 1-bis", "è parametrato al solo danno emergente")

L("amm-115", "Autotutela", 3, "Quando è ammesso il recesso unilaterale della PA dai contratti?",
  "Nei casi previsti dalla legge o dal contratto", ["Sempre, per qualsiasi motivo", "Mai", "Solo con autorizzazione dell'ANAC"],
  "Art. 21-sexies.",
  "art. 21-sexies", "è ammesso nei casi previsti dalla legge o dal contratto")

L("amm-116", "Invalidità del provvedimento", 4, "Un provvedimento vincolato, viziato solo nella forma, è annullabile se il suo contenuto non poteva essere diverso?",
  "No, non è annullabile", ["Sì, sempre", "È nullo", "È inesistente"],
  "L'art. 21-octies, c. 2 esclude l'annullabilità per vizi formali o procedimentali dei provvedimenti vincolati.",
  "art. 21-octies, c. 2", "Non è annullabile il provvedimento adottato in violazione di norme sul procedimento")

L("amm-117", "Autotutela", 3, "Quale istituto consente di sanare un provvedimento annullabile, per ragioni di interesse pubblico ed entro un termine ragionevole?",
  "La convalida", ["La revoca", "La sospensione", "Il ritiro per nullità"],
  "L'art. 21-nonies, c. 2 fa salva la convalida del provvedimento annullabile.",
  "art. 21-nonies, c. 2", "la possibilità di convalida del provvedimento annullabile")

L("amm-118", "Autotutela", 5, "Un'autorizzazione ottenuta con dichiarazioni false, accertate con sentenza penale definitiva, può essere annullata dopo i sei mesi?",
  "Sì, anche dopo la scadenza del termine", ["No, mai", "Solo entro un anno", "Solo se il privato acconsente"],
  "L'art. 21-nonies, c. 2-bis lo consente per false rappresentazioni o dichiarazioni mendaci accertate in giudicato.",
  "art. 21-nonies, c. 2-bis", "possono essere annullati dall'amministrazione anche dopo la scadenza del termine")

L("amm-119", "Accesso ai documenti", 2, "In cosa consiste il diritto di accesso secondo l'art. 22?",
  "Nel prendere visione ed estrarre copia di documenti amministrativi", ["Nel partecipare alle riunioni di giunta", "Nel modificare i documenti amministrativi", "Nell'ottenere un parere legale gratuito"],
  "Art. 22, c. 1, lett. a).",
  "art. 22, c. 1", "il diritto degli interessati di prendere visione e di estrarre copia di documenti amministrativi")

L("amm-120", "Accesso ai documenti", 3, "Le informazioni della PA che non hanno forma di documento amministrativo sono accessibili ex L. 241/1990?",
  "No, salvo quanto previsto per i dati personali dell'interessato", ["Sì, sempre", "Solo per i giornalisti", "Solo se richieste via PEC"],
  "L'art. 22, c. 4: l'accesso riguarda documenti, non informazioni da elaborare.",
  "art. 22, c. 4", "che non abbiano forma di documento amministrativo")

L("amm-121", "Accesso ai documenti", 3, "Fino a quando è esercitabile il diritto di accesso?",
  "Finché la PA ha l'obbligo di detenere i documenti", ["Per un anno dalla formazione del documento", "Solo durante il procedimento", "Per cinque anni"],
  "Art. 22, c. 6.",
  "art. 22, c. 6", "fino a quando la pubblica amministrazione ha l'obbligo di detenere i documenti")

L("amm-122", "Accesso ai documenti", 3, "Nei confronti di chi si esercita il diritto di accesso (art. 23)?",
  "Pubbliche amministrazioni, aziende autonome e speciali, enti pubblici e gestori di pubblici servizi", ["Solo i ministeri", "Solo i comuni", "Qualsiasi impresa privata"],
  "Art. 23; verso le Autorità di garanzia si esercita secondo i rispettivi ordinamenti.",
  "art. 23", "delle aziende autonome e speciali, degli enti pubblici e dei gestori di pubblici servizi")

L("amm-123", "Accesso ai documenti", 3, "Sono ammissibili istanze di accesso finalizzate a un controllo generalizzato sull'operato della PA?",
  "No, non sono ammissibili", ["Sì, sempre", "Solo se firmate da 100 cittadini", "Solo per i consiglieri regionali"],
  "L'art. 24, c. 3 lo esclude per l'accesso documentale (il controllo diffuso è invece lo scopo dell'accesso civico generalizzato del D.Lgs. 33/2013).",
  "art. 24, c. 3", "Non sono ammissibili istanze di accesso preordinate ad un controllo generalizzato")

L("amm-124", "Accesso ai documenti", 4, "L'accesso può essere negato quando basterebbe differirlo?",
  "No: non può essere negato ove sia sufficiente il differimento", ["Sì, a discrezione della PA", "Sì, se il documento è riservato", "Solo nei procedimenti tributari"],
  "Art. 24, c. 4.",
  "art. 24, c. 4", "non può essere negato ove sia sufficiente fare ricorso al potere di differimento")

L("amm-125", "Accesso ai documenti", 4, "In caso di documenti con dati riservati di terzi, quando va comunque garantito l'accesso?",
  "Quando la conoscenza è necessaria per curare o difendere i propri interessi giuridici", ["Mai", "Solo con il consenso scritto del terzo", "Solo se il richiedente è un avvocato"],
  "L'art. 24, c. 7 garantisce l'accesso difensivo, con limiti più stretti per i dati sensibili e giudiziari.",
  "art. 24, c. 7", "la cui conoscenza sia necessaria per curare o per difendere i propri interessi giuridici")

L("amm-126", "Accesso ai documenti", 2, "Quanto costa esaminare i documenti amministrativi?",
  "L'esame è gratuito; per le copie si rimborsa il costo di riproduzione", ["Si paga sempre una tassa fissa", "È gratuito anche il rilascio di copie in bollo", "Si paga un diritto di 50 euro"],
  "Art. 25, c. 1; restano salve le norme sul bollo e i diritti di ricerca e visura.",
  "art. 25, c. 1", "L'esame dei documenti è gratuito")

L("amm-127", "Accesso ai documenti", 3, "La richiesta di accesso documentale deve essere motivata?",
  "Sì, e va rivolta all'amministrazione che ha formato o detiene il documento", ["No, mai", "Solo se riguarda dati personali", "Solo se presentata oralmente"],
  "Art. 25, c. 2 (a differenza dell'accesso civico, che non va motivato).",
  "art. 25, c. 2", "La richiesta di accesso ai documenti deve essere motivata")

L("amm-128", "Accesso ai documenti", 4, "Contro il diniego di accesso di un comune, oltre al TAR, a chi si può chiedere il riesame?",
  "Al difensore civico competente", ["Al prefetto", "Al Garante per la privacy", "Alla Corte dei conti"],
  "Per gli atti di comuni, province e regioni si ricorre al difensore civico; per lo Stato alla Commissione per l'accesso.",
  "art. 25, c. 4", "al difensore civico competente per ambito territoriale")

L("amm-129", "Accesso ai documenti", 4, "Presso quale organo è istituita la Commissione per l'accesso ai documenti amministrativi?",
  "Presso la Presidenza del Consiglio dei Ministri", ["Presso il Ministero dell'interno", "Presso il Consiglio di Stato", "Presso la Camera dei deputati"],
  "Art. 27, c. 1; la Commissione è rinnovata ogni tre anni.",
  "art. 27, c. 1", "È istituita presso la Presidenza del Consiglio dei Ministri la Commissione per l'accesso")

L("amm-130", "Accesso ai documenti", 4, "Ogni quanto è rinnovata la Commissione per l'accesso ai documenti amministrativi?",
  "Ogni tre anni", ["Ogni cinque anni", "Ogni anno", "Ogni sette anni"],
  "Art. 27, c. 3.",
  "art. 27, c. 3", "La Commissione è rinnovata ogni tre anni")

L("amm-131", "Segreto d'ufficio", 2, "Che cosa vieta il segreto d'ufficio all'impiegato pubblico?",
  "Trasmettere a chi non ne ha diritto informazioni su provvedimenti o notizie apprese per le sue funzioni", ["Parlare con i colleghi", "Rilasciare copie nei casi consentiti", "Rispondere alle istanze di accesso"],
  "L'art. 28 ha riscritto l'art. 15 del DPR 3/1957 coordinandolo con il diritto di accesso.",
  "art. 28", "L'impiegato deve mantenere il segreto d'ufficio")

L("amm-132", "Ambito di applicazione", 4, "Le regioni possono prevedere, nei loro procedimenti, garanzie inferiori a quelle dei livelli essenziali della L. 241/1990?",
  "No, possono solo prevedere livelli ulteriori di tutela", ["Sì, liberamente", "Sì, con legge regionale", "Solo le regioni a statuto speciale"],
  "Art. 29, c. 2-quater.",
  "art. 29, c. 2-quater", "non possono stabilire garanzie inferiori")

L("amm-133", "Ambito di applicazione", 3, "Negli atti di notorietà e attestazioni asseverate da testimoni, quanti testimoni servono?",
  "Due", ["Quattro", "Uno", "Tre"],
  "L'art. 30, c. 1 riduce a due il numero dei testimoni.",
  "art. 30, c. 1", "il numero dei testimoni è ridotto a due")


# --- Blocco 3: TUEL (D.Lgs. 267/2000) ---
def T(id, arg, liv, testo, giusta, sbagliate, spieg, art, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, f"D.Lgs. 267/2000 (TUEL), {art}", TUEL, frase)

T("amm-134", "Enti locali", 1, "Quali di questi sono enti locali secondo il TUEL?",
  "Comuni, province, città metropolitane, comunità montane, comunità isolane e unioni di comuni", ["Solo comuni e regioni", "Regioni, prefetture e questure", "Comuni, ASL e camere di commercio"],
  "L'art. 2 elenca gli enti locali; le regioni non sono enti locali ma enti territoriali con potestà legislativa.",
  "art. 2", "si intendono per enti locali i comuni, le province, le città metropolitane, le comunità montane")

T("amm-135", "Enti locali", 1, "Come definisce il comune l'art. 3 del TUEL?",
  "L'ente locale che rappresenta la propria comunità, ne cura gli interessi e ne promuove lo sviluppo", ["Un ufficio periferico dello Stato", "Un organo della regione", "Un'associazione privata di cittadini"],
  "La provincia è invece l'ente intermedio tra comune e regione.",
  "art. 3", "Il comune è l'ente locale che rappresenta la propria comunità")

T("amm-136", "Enti locali", 2, "Quale ente locale il TUEL definisce «intermedio tra comune e regione»?",
  "La provincia", ["La città metropolitana", "L'unione di comuni", "La comunità montana"],
  "Art. 3, c. 3.",
  "art. 3", "La provincia, ente locale intermedio tra comune e regione")

T("amm-137", "Enti locali", 2, "Quali forme di autonomia riconosce il TUEL a comuni e province?",
  "Statutaria, normativa, organizzativa, amministrativa, impositiva e finanziaria", ["Solo amministrativa", "Legislativa e giurisdizionale", "Solo finanziaria"],
  "Art. 3, c. 4; la potestà legislativa spetta invece a Stato e regioni.",
  "art. 3", "hanno autonomia statutaria, normativa, organizzativa e amministrativa")

T("amm-138", "Enti locali", 3, "Che cosa stabilisce lo statuto comunale?",
  "Le norme fondamentali dell'organizzazione dell'ente, tra cui attribuzioni degli organi, garanzie delle minoranze e rappresentanza legale", ["Le aliquote dei tributi ogni anno", "Il bilancio di previsione", "Le pene per i reati commessi nel comune"],
  "Art. 6, c. 2; lo statuto disciplina anche partecipazione popolare, stemma e gonfalone.",
  "art. 6", "stabilisce le norme fondamentali dell'organizzazione dell'ente")

T("amm-139", "Enti locali", 3, "Quali servizi di competenza statale gestisce il comune?",
  "Servizi elettorali, di stato civile, di anagrafe, di leva militare e di statistica", ["Servizi di polizia di Stato", "Giustizia civile di primo grado", "Riscossione delle imposte sui redditi"],
  "Art. 14: le relative funzioni sono esercitate dal sindaco come ufficiale del Governo.",
  "art. 14", "Il comune gestisce i servizi elettorali, di stato civile, di anagrafe, di leva militare e di statistica")

T("amm-140", "Enti locali", 4, "Salvo i casi di fusione, sotto quale soglia di popolazione non si possono istituire nuovi comuni?",
  "10.000 abitanti", ["5.000 abitanti", "1.000 abitanti", "15.000 abitanti"],
  "Art. 15, c. 1.",
  "art. 15", "non possono essere istituiti nuovi comuni con popolazione inferiore ai 10.000 abitanti")

T("amm-141", "Forme associative", 2, "Con quale strumento gli enti locali svolgono in modo coordinato funzioni e servizi determinati, senza creare un nuovo ente?",
  "La convenzione", ["L'unione di comuni", "La fusione", "Il consorzio obbligatorio di bonifica"],
  "L'art. 30 disciplina le convenzioni, che fissano fini, durata, rapporti finanziari e obblighi reciproci.",
  "art. 30", "gli enti locali possono stipulare tra loro apposite convenzioni")

T("amm-142", "Forme associative", 3, "Di quante unioni di comuni può far parte ciascun comune?",
  "Di una sola", ["Di due al massimo", "Di quante vuole", "Di nessuna se ha meno di 5.000 abitanti"],
  "Art. 32, c. 2.",
  "art. 32", "Ogni comune può far parte di una sola unione di comuni")

T("amm-143", "Forme associative", 3, "Che cos'è l'unione di comuni?",
  "Un ente locale costituito da due o più comuni, di norma contermini, per l'esercizio associato di funzioni e servizi", ["Un accordo informale tra sindaci", "Un'azienda speciale del comune capoluogo", "Un ufficio della prefettura"],
  "Art. 32, c. 1.",
  "art. 32", "L'unione di comuni è l'ente locale costituito da due o più comuni")

T("amm-144", "Organi", 2, "Da quanti consiglieri (oltre al sindaco) è composto il consiglio di un comune con più di 100.000 abitanti o capoluogo di provincia?",
  "40", ["60", "30", "24"],
  "Art. 37: 60 oltre il milione, 50 oltre 500.000, 46 oltre 250.000, 40 oltre 100.000 o capoluoghi.",
  "art. 37", "da 40 membri nei comuni con popolazione superiore a 100.000 abitanti")

T("amm-145", "Organi", 3, "Quale presenza minima deve garantire il regolamento per la validità delle sedute del consiglio comunale?",
  "Almeno un terzo dei consiglieri assegnati, senza contare il sindaco", ["La metà più uno", "Due terzi dei consiglieri", "Almeno cinque consiglieri"],
  "Art. 38, c. 2.",
  "art. 38", "almeno un terzo dei consiglieri assegnati per legge all'ente")

T("amm-146", "Organi", 3, "Nei comuni sopra 15.000 abitanti, chi presiede il consiglio comunale?",
  "Un presidente eletto tra i consiglieri nella prima seduta", ["Il sindaco", "Il segretario comunale", "Il prefetto"],
  "Art. 39, c. 1; nei comuni fino a 15.000 abitanti lo statuto può prevedere la figura.",
  "art. 39", "sono presieduti da un presidente eletto tra i consiglieri nella prima seduta")

T("amm-147", "Organi", 4, "Entro quanti giorni il presidente del consiglio deve riunirlo quando lo chiede un quinto dei consiglieri?",
  "Entro venti giorni", ["Entro dieci giorni", "Entro sessanta giorni", "Entro cinque giorni"],
  "Art. 39, c. 2.",
  "art. 39", "in un termine non superiore ai venti giorni, quando lo richiedano un quinto dei consiglieri")

T("amm-148", "Organi", 2, "Chi nomina i componenti della giunta comunale, tra cui il vicesindaco?",
  "Il sindaco", ["Il consiglio comunale con voto segreto", "Il prefetto", "I cittadini con elezione diretta"],
  "Art. 46, c. 2: il sindaco nomina la giunta e ne dà comunicazione al consiglio; può anche revocare gli assessori.",
  "art. 46", "nominano ((, nel rispetto del principio di pari opportunità")

T("amm-149", "Organi", 4, "Qual è il numero massimo di assessori nella giunta comunale?",
  "Un terzo dei consiglieri (computando il sindaco) e comunque non più di dodici", ["La metà dei consiglieri", "Venti in ogni caso", "Cinque in ogni caso"],
  "Art. 47, c. 1.",
  "art. 47", "non deve essere superiore a un terzo, arrotondato aritmeticamente")

T("amm-150", "Organi", 3, "Nei comuni sopra 15.000 abitanti, gli assessori possono essere scelti fuori dal consiglio?",
  "Sì, tra cittadini con i requisiti per essere eletti consiglieri", ["No, devono essere consiglieri", "Solo se iscritti a un albo professionale", "Solo con il consenso del prefetto"],
  "Art. 47, c. 3.",
  "art. 47", "anche al di fuori dei componenti del consiglio")

T("amm-151", "Organi", 3, "Qual è la competenza residuale della giunta comunale?",
  "Compie gli atti di governo non riservati dalla legge al consiglio e non attribuiti al sindaco", ["Approva il bilancio e lo statuto", "Elegge il sindaco", "Adotta tutti gli atti di gestione al posto dei dirigenti"],
  "Art. 48, c. 2: la giunta ha competenza residuale tra gli organi di governo.",
  "art. 48", "che non siano riservati dalla legge al consiglio")

T("amm-152", "Organi", 2, "Chi rappresenta il comune e convoca e presiede la giunta?",
  "Il sindaco", ["Il segretario comunale", "Il presidente del consiglio comunale", "Il dirigente più anziano"],
  "Art. 50, c. 2.",
  "art. 50", "rappresentano l'ente, convocano e presiedono la giunta")

T("amm-153", "Organi", 4, "Il voto contrario del consiglio a una proposta del sindaco comporta le sue dimissioni?",
  "No, servono una mozione di sfiducia approvata a maggioranza assoluta", ["Sì, sempre", "Sì, se la proposta riguardava il bilancio", "Solo se il voto è segreto"],
  "Art. 52, c. 1-2.",
  "art. 52", "non comporta le dimissioni degli stessi")

T("amm-154", "Organi", 4, "Da quanti consiglieri deve essere sottoscritta la mozione di sfiducia al sindaco?",
  "Da almeno due quinti dei consiglieri assegnati", ["Da almeno un decimo", "Da tutti i consiglieri di opposizione", "Dalla metà più uno"],
  "Art. 52, c. 2; viene discussa tra il decimo e il trentesimo giorno dalla presentazione.",
  "art. 52", "sottoscritta da almeno due quinti dei consiglieri assegnati")

T("amm-155", "Organi", 4, "Quando diventano efficaci e irrevocabili le dimissioni del sindaco?",
  "Trascorsi 20 giorni dalla presentazione al consiglio", ["Immediatamente", "Dopo 60 giorni", "Dopo l'accettazione del prefetto"],
  "Art. 53, c. 3.",
  "art. 53", "diventano efficaci ed irrevocabili trascorso il termine di 20 giorni")

T("amm-156", "Organi", 3, "In caso di decesso del sindaco, chi ne svolge le funzioni fino alle nuove elezioni?",
  "Il vicesindaco", ["Il presidente del consiglio comunale", "Il segretario comunale", "Un commissario nominato dal sindaco uscente"],
  "Art. 53, c. 1: la giunta decade e il consiglio è sciolto, ma restano in carica fino all'elezione; le funzioni sono svolte dal vicesindaco.",
  "art. 53", "le funzioni del sindaco e del presidente della provincia sono svolte, rispettivamente, dal vicesindaco")

T("amm-157", "Organi", 3, "In quale veste il sindaco adotta ordinanze contingibili e urgenti per gravi pericoli all'incolumità pubblica e alla sicurezza urbana (art. 54)?",
  "Quale ufficiale del Governo", ["Quale presidente del consiglio comunale", "Quale capo della polizia di Stato", "Quale delegato del presidente della regione"],
  "Art. 54, c. 4.",
  "art. 54", "Il sindaco, quale ufficiale del Governo, adotta con atto motivato provvedimenti")

T("amm-158", "Organi", 4, "Con quale atto vengono sciolti i consigli comunali?",
  "Decreto del Presidente della Repubblica, su proposta del Ministro dell'interno", ["Decreto del prefetto", "Legge regionale", "Sentenza del TAR"],
  "Art. 141, c. 1.",
  "art. 141", "vengono sciolti con decreto del Presidente della Repubblica, su proposta del Ministro dell'interno")

T("amm-159", "Dirigenza locale", 3, "Come sono conferiti gli incarichi dirigenziali negli enti locali?",
  "A tempo determinato, con provvedimento motivato, secondo criteri di competenza professionale", ["A vita, per anzianità", "Per sorteggio", "Con elezione da parte del consiglio"],
  "Art. 109, c. 1; possono essere revocati per inosservanza delle direttive o mancato raggiungimento degli obiettivi.",
  "art. 109", "Gli incarichi dirigenziali sono conferiti a tempo determinato")

T("amm-160", "Dirigenza locale", 4, "Quale quota massima dei posti dirigenziali può essere coperta con contratti a tempo determinato ex art. 110 TUEL?",
  "Il 30 per cento dei posti in dotazione organica (comunque almeno una unità)", ["Il 50 per cento", "Il 10 per cento", "Nessuno"],
  "Art. 110, c. 1; serve una selezione pubblica.",
  "art. 110", "non superiore al 30 per cento dei posti istituiti")

T("amm-161", "Contabilità locale", 3, "Entro quale data gli enti locali presentano il Documento unico di programmazione (DUP)?",
  "Entro il 31 luglio di ogni anno", ["Entro il 31 dicembre", "Entro il 30 aprile", "Entro il 15 settembre"],
  "Art. 151, c. 1; il bilancio di previsione si delibera entro il 31 dicembre, su orizzonte almeno triennale.",
  "art. 151", "presentano il Documento unico di programmazione entro il 31 luglio di ogni anno")

T("amm-162", "Contabilità locale", 3, "Qual è l'unità temporale della gestione finanziaria degli enti locali?",
  "L'anno finanziario, dal 1 gennaio al 31 dicembre", ["Il mandato del sindaco", "Il triennio", "L'anno scolastico"],
  "Art. 162, c. 3: dopo il 31 dicembre non si possono più accertare entrate o impegnare spese dell'esercizio scaduto.",
  "art. 162", "L'unità temporale della gestione è l'anno finanziario")

T("amm-163", "Contabilità locale", 4, "Da cosa può derivare un debito fuori bilancio riconoscibile dal consiglio?",
  "Ad esempio da sentenze esecutive", ["Da qualsiasi spesa decisa a voce dal sindaco", "Dalle multe non pagate dai cittadini", "Dagli stipendi ordinari del personale"],
  "L'art. 194 elenca le fattispecie: sentenze esecutive, disavanzi di aziende, ricapitalizzazioni, espropri, acquisti senza impegno nei limiti dell'utilità.",
  "art. 194", "riconoscono la legittimità dei debiti fuori bilancio derivanti da: a) sentenze esecutive")

T("amm-164", "Contabilità locale", 4, "Quando si ha dissesto finanziario di un ente locale?",
  "Quando non può garantire le funzioni e i servizi indispensabili o non può far fronte a crediti liquidi ed esigibili di terzi", ["Quando chiude l'anno con un piccolo avanzo", "Quando cambia il sindaco", "Quando non approva il DUP"],
  "Art. 244; il risanamento coinvolge l'organo straordinario di liquidazione.",
  "art. 244", "Si ha stato di dissesto finanziario se l'ente non può garantire")

T("amm-165", "Controlli interni", 4, "A cosa serve il controllo di gestione negli enti locali?",
  "A verificare efficacia, efficienza ed economicità dell'azione amministrativa", ["A giudicare i reati dei dipendenti", "A eleggere il collegio dei revisori", "A riscuotere i tributi"],
  "Art. 147, c. 2, lett. a).",
  "art. 147", "attraverso il controllo di gestione, l'efficacia, l'efficienza e l'economicità")


# --- Blocco 4: pubblico impiego, trasparenza, codice di comportamento, documentazione ---
D("amm-166", "Pubblico impiego", 2, "Quale articolo della Costituzione richiama il D.Lgs. 165/2001 tra i suoi fondamenti?",
  "L'art. 97, primo comma", ["L'art. 1", "L'art. 21", "L'art. 139"],
  "L'art. 1 del D.Lgs. 165/2001 disciplina organizzazione e lavoro pubblico nel rispetto dell'art. 97 Cost. (buon andamento e imparzialità).",
  "D.Lgs. 165/2001, art. 1", D165, "nel rispetto dell'articolo 97, comma primo, della Costituzione")

D("amm-167", "Pubblico impiego", 3, "Quali discriminazioni vieta espressamente l'art. 7 del D.Lgs. 165/2001 nell'accesso e nel trattamento sul lavoro?",
  "Quelle legate a genere, età, orientamento sessuale, razza, origine etnica, disabilità, religione o lingua", ["Solo quelle di genere", "Solo quelle legate alla religione", "Nessuna, è materia dei contratti"],
  "Le PA devono garantire pari opportunità, assenza di discriminazioni e benessere organizzativo.",
  "D.Lgs. 165/2001, art. 7", D165, "relativa al genere, all'età, all'orientamento sessuale, alla razza")

D("amm-168", "Pubblico impiego", 3, "Chi assume in via esclusiva le determinazioni sull'organizzazione degli uffici e la gestione dei rapporti di lavoro?",
  "Gli organi preposti alla gestione, con i poteri del privato datore di lavoro", ["Il Parlamento con legge", "I sindacati", "La Corte dei conti"],
  "L'art. 5, c. 2 attribuisce queste determinazioni agli organi di gestione (dirigenti).",
  "D.Lgs. 165/2001, art. 5", D165, "sono assunte in via esclusiva dagli organi preposti alla gestione")

D("amm-169", "Pubblico impiego", 4, "Cosa comporta l'esercizio di fatto, da parte di un dipendente pubblico, di mansioni superiori alla propria qualifica?",
  "Non ha effetto ai fini dell'inquadramento o dell'assegnazione di incarichi di direzione", ["Determina automaticamente la promozione", "Dopo sei mesi dà diritto alla qualifica superiore", "Comporta il licenziamento"],
  "Art. 52, c. 1: nel pubblico impiego le mansioni superiori di fatto non danno diritto all'inquadramento.",
  "D.Lgs. 165/2001, art. 52", D165, "non ha effetto ai fini dell'inquadramento del lavoratore")

D("amm-170", "Pubblico impiego", 4, "Il mancato raggiungimento degli obiettivi da parte del dirigente, accertato dal sistema di valutazione, cosa comporta?",
  "L'impossibilità di rinnovo dello stesso incarico dirigenziale, previa contestazione", ["Nessuna conseguenza", "L'arresto immediato", "La promozione a un altro incarico"],
  "Art. 21 (responsabilità dirigenziale); nei casi più gravi revoca dell'incarico o recesso.",
  "D.Lgs. 165/2001, art. 21", D165, "l'impossibilità di rinnovo dello stesso incarico dirigenziale")

D("amm-171", "Pubblico impiego", 3, "Chi è competente per il procedimento disciplinare che può concludersi con il rimprovero verbale?",
  "Il responsabile della struttura presso cui presta servizio il dipendente", ["L'ufficio per i procedimenti disciplinari", "Il giudice del lavoro", "Il Ministro per la pubblica amministrazione"],
  "Art. 55-bis: per le sanzioni superiori è competente l'ufficio per i procedimenti disciplinari (UPD).",
  "D.Lgs. 165/2001, art. 55-bis", D165, "il procedimento disciplinare è di competenza del responsabile della struttura")

D("amm-172", "Pubblico impiego", 3, "Quale sanzione si applica al dipendente pubblico che attesta falsamente la presenza in servizio alterando i sistemi di rilevazione?",
  "Il licenziamento disciplinare", ["Il rimprovero verbale", "Una multa di quattro ore", "La sospensione per un giorno"],
  "Art. 55-quater, c. 1, lett. a).",
  "D.Lgs. 165/2001, art. 55-quater", D165, "falsa attestazione della presenza in servizio")

D("amm-173", "Pubblico impiego", 4, "La mobilità volontaria verso altra amministrazione (art. 30) richiede sempre l'assenso dell'amministrazione di appartenenza?",
  "No, solo in casi particolari (es. posizioni infungibili, assunti da meno di tre anni, carenze oltre il 20%)", ["Sì, sempre", "No, mai", "Solo per i dirigenti"],
  "Art. 30, c. 1, nel testo vigente.",
  "D.Lgs. 165/2001, art. 30", D165, "di personale assunto da meno di tre anni")

D("amm-174", "Trasparenza", 2, "Come è definita la trasparenza dal D.Lgs. 33/2013?",
  "Accessibilità totale dei dati e documenti detenuti dalle pubbliche amministrazioni", ["Pubblicazione dei soli bilanci", "Riservatezza delle informazioni amministrative", "Possibilità di accesso solo per gli interessati qualificati"],
  "Art. 1, c. 1: anche per favorire forme diffuse di controllo sulle funzioni istituzionali e sull'uso delle risorse pubbliche.",
  "D.Lgs. 33/2013, art. 1", D33, "La trasparenza è intesa come accessibilità totale")

D("amm-175", "Trasparenza", 3, "In che formato vanno pubblicati i dati oggetto di pubblicazione obbligatoria?",
  "In formato di tipo aperto, riutilizzabili citando la fonte", ["Solo in formato cartaceo", "In formato proprietario protetto da password", "Solo come immagine scansionata"],
  "Art. 7 del D.Lgs. 33/2013, con rinvio all'art. 68 del CAD.",
  "D.Lgs. 33/2013, art. 7", D33, "sono pubblicati in formato di tipo aperto")

D("amm-176", "Trasparenza", 3, "Per quanto tempo restano pubblicati, di regola, i dati soggetti a obbligo di pubblicazione?",
  "5 anni dal 1° gennaio dell'anno successivo, e comunque finché gli atti producono effetti", ["1 anno", "10 anni", "Per sempre"],
  "Art. 8, c. 3.",
  "D.Lgs. 33/2013, art. 8", D33, "sono pubblicati per un periodo di 5 anni")

D("amm-177", "Trasparenza", 3, "Chi svolge, di norma, le funzioni di Responsabile per la trasparenza?",
  "Il responsabile per la prevenzione della corruzione", ["Il sindaco", "Il revisore dei conti", "Il presidente dell'OIV"],
  "Art. 43: le due figure coincidono di norma nell'RPCT.",
  "D.Lgs. 33/2013, art. 43", D33, "svolge, di norma, le funzioni di Responsabile per la trasparenza")

D("amm-178", "Trasparenza", 4, "L'accesso civico è sottoposto a limitazioni quanto alla legittimazione soggettiva del richiedente?",
  "No, non è soggetto ad alcuna limitazione e non va motivato", ["Sì, serve un interesse diretto, concreto e attuale", "Sì, solo i residenti possono chiederlo", "Sì, solo i giornalisti"],
  "Art. 5, c. 3, a differenza dell'accesso documentale della L. 241/1990.",
  "D.Lgs. 33/2013, art. 5", D33, "non è sottoposto ad alcuna limitazione quanto al")

D("amm-179", "Codice di comportamento", 2, "Secondo il DPR 62/2013, con quale spirito il dipendente serve la Nazione?",
  "Con disciplina ed onore", ["Con obbedienza al partito di maggioranza", "Con fedeltà al proprio dirigente personale", "Con riservatezza assoluta verso i cittadini"],
  "Art. 3: il dipendente osserva la Costituzione servendo la Nazione con disciplina ed onore (cfr. art. 54 Cost.).",
  "DPR 62/2013, art. 3", P62, "servendo la Nazione con disciplina ed onore")

D("amm-180", "Codice di comportamento", 3, "Il dipendente può accettare un regalo di modico valore come corrispettivo per un atto del proprio ufficio?",
  "No, mai, neanche di modico valore", ["Sì, se inferiore a 150 euro", "Sì, se lo dichiara al dirigente", "Sì, se è un regalo d'uso"],
  "Art. 4, c. 2: i regali come corrispettivo di un atto d'ufficio sono sempre vietati.",
  "DPR 62/2013, art. 4", P62, "neanche di modico valore a titolo di corrispettivo")

D("amm-181", "Codice di comportamento", 3, "All'assegnazione all'ufficio, di quali rapporti con privati il dipendente deve informare il dirigente?",
  "Dei rapporti di collaborazione retribuiti avuti negli ultimi tre anni", ["Di tutte le amicizie personali", "Dei rapporti degli ultimi dieci anni", "Di nessun rapporto"],
  "Art. 6, c. 1.",
  "DPR 62/2013, art. 6", P62, "che lo stesso abbia o abbia avuto negli ultimi tre anni")

D("amm-182", "Codice di comportamento", 3, "Entro quale grado di parentela o affinità scatta l'obbligo di astensione del dipendente (art. 7)?",
  "Affini entro il secondo grado, oltre a parenti, coniuge e conviventi", ["Solo il coniuge", "Fino al sesto grado", "Solo i figli"],
  "Art. 7: anche persone con frequentazione abituale e soggetti con cui ha cause pendenti o grave inimicizia.",
  "DPR 62/2013, art. 7", P62, "ovvero di suoi parenti, affini entro il secondo grado")

D("amm-183", "Codice di comportamento", 2, "Come si fa riconoscere il dipendente in rapporto con il pubblico?",
  "Esponendo in modo visibile il badge o altro supporto identificativo", ["Indossando la divisa", "Mostrando la carta d'identità su richiesta", "Non deve farsi riconoscere"],
  "Art. 12, c. 1 del DPR 62/2013.",
  "DPR 62/2013, art. 12", P62, "si fa riconoscere attraverso l'esposizione in modo visibile del badge")

D("amm-184", "Codice di comportamento", 3, "Nei rapporti privati, cosa vieta al dipendente l'art. 10 del codice di comportamento?",
  "Sfruttare o menzionare la propria posizione per ottenere utilità non dovute", ["Frequentare altri dipendenti pubblici", "Iscriversi a un'associazione", "Usare i social network"],
  "Art. 10 del DPR 62/2013.",
  "DPR 62/2013, art. 10", P62, "non sfrutta, né menziona la posizione che ricopre")

D("amm-185", "Documentazione amministrativa", 2, "Come definisce il DPR 445/2000 il «documento di riconoscimento»?",
  "Ogni documento munito di fotografia del titolare, rilasciato da una PA, che consente l'identificazione", ["Qualsiasi tessera con il nome", "Solo il passaporto", "Solo la carta d'identità cartacea"],
  "Art. 1, lett. c).",
  "DPR 445/2000, art. 1", P445, "ogni documento munito di fotografia del titolare")

D("amm-186", "Documentazione amministrativa", 3, "Quale di questi stati o fatti può essere comprovato con dichiarazione sostitutiva di certificazione (art. 46)?",
  "Il titolo di studio e gli esami sostenuti", ["Lo stato di salute", "La conformità di un impianto elettrico", "Il possesso di un brevetto europeo rilasciato all'estero"],
  "L'art. 46 elenca, tra gli altri, nascita, residenza, cittadinanza, stato di famiglia, titolo di studio ed esami.",
  "DPR 445/2000, art. 46", P445, "titolo di studio, esami sostenuti")

D("amm-187", "Documentazione amministrativa", 3, "La dichiarazione sostitutiva dell'atto di notorietà può riguardare fatti relativi ad altre persone?",
  "Sì, se resa nel proprio interesse e se il dichiarante ne ha diretta conoscenza", ["No, mai", "Solo per i figli minori", "Solo davanti a un notaio"],
  "Art. 47, c. 2.",
  "DPR 445/2000, art. 47", P445, "può riguardare anche stati, qualità personali e fatti relativi ad altri soggetti")

D("amm-188", "Documentazione amministrativa", 3, "Come effettua la PA i controlli sulle dichiarazioni sostitutive?",
  "Con controlli idonei, anche a campione e nei casi di ragionevole dubbio, anche dopo l'erogazione dei benefici", ["Solo con un'ispezione a domicilio", "Non effettua controlli", "Solo su denuncia di terzi"],
  "Art. 71, c. 1.",
  "DPR 445/2000, art. 71", P445, "anche a campione in misura proporzionale al rischio")

D("amm-189", "Documentazione amministrativa", 4, "Oltre alla decadenza dai benefici, cosa comporta una dichiarazione mendace (art. 75, c. 1-bis)?",
  "Il divieto di accesso a contributi e agevolazioni per 2 anni", ["Il divieto di voto per 5 anni", "La perdita della cittadinanza", "Nessun'altra conseguenza"],
  "Art. 75, c. 1-bis; restano fermi gli interventi a favore dei minori.",
  "DPR 445/2000, art. 75", P445, "per un periodo di 2 anni decorrenti")

D("amm-190", "Documentazione amministrativa", 4, "Come sono considerate, ai fini penali, le dichiarazioni sostitutive rese ai sensi degli artt. 46 e 47?",
  "Come fatte a pubblico ufficiale", ["Come dichiarazioni private senza rilievo penale", "Come testimonianze in giudizio", "Come atti notarili"],
  "Art. 76, c. 3; la pena ordinaria è aumentata da un terzo alla metà.",
  "DPR 445/2000, art. 76", P445, "sono considerate come fatte a pubblico ufficiale")

D("amm-191", "Documentazione amministrativa", 4, "Esibire un atto contenente dati non più veri a cosa equivale secondo il DPR 445/2000?",
  "A uso di atto falso", ["A una semplice irregolarità", "A nulla, se in buona fede", "A dichiarazione mendace solo se scritta a mano"],
  "Art. 76, c. 2.",
  "DPR 445/2000, art. 76", P445, "equivale ad uso di atto falso")

D("amm-192", "Documentazione amministrativa", 2, "Le domande di partecipazione ai concorsi pubblici possono essere inviate per via telematica?",
  "Sì, se effettuate secondo l'art. 65 del CAD", ["No, solo a mano", "Solo con raccomandata", "Solo tramite un avvocato"],
  "Art. 38, c. 2 del DPR 445/2000.",
  "DPR 445/2000, art. 38", P445, "ivi comprese le domande per la partecipazione a selezioni e concorsi")

D("amm-193", "Contratti pubblici", 3, "Fino a quale importo i lavori possono essere affidati direttamente, anche senza consultare più operatori (D.Lgs. 36/2023)?",
  "Fino a meno di 150.000 euro", ["Fino a meno di 40.000 euro", "Fino a meno di 1 milione di euro", "Fino alla soglia europea"],
  "Art. 50, c. 1, lett. a); per servizi e forniture il limite è 140.000 euro.",
  "D.Lgs. 36/2023, art. 50", D36, "affidamento diretto per lavori di importo inferiore a 150.000 euro")

D("amm-194", "Contratti pubblici", 3, "Fino a quale importo servizi e forniture possono essere affidati direttamente secondo l'art. 50 del D.Lgs. 36/2023?",
  "Fino a meno di 140.000 euro", ["Fino a meno di 150.000 euro", "Fino a meno di 5.000 euro", "Fino a meno di 500.000 euro"],
  "Art. 50, c. 1, lett. b), compresi i servizi di ingegneria e architettura.",
  "D.Lgs. 36/2023, art. 50", D36, "di importo inferiore a 140.000 euro")

D("amm-195", "Contratti pubblici", 4, "Cosa vieta il principio di rotazione negli affidamenti sotto soglia?",
  "Di affidare al contraente uscente due commesse consecutive nello stesso settore o categoria", ["Di affidare appalti a imprese straniere", "Di affidare più di un appalto all'anno", "Di cambiare il RUP durante la gara"],
  "Art. 49, c. 2 del D.Lgs. 36/2023.",
  "D.Lgs. 36/2023, art. 49", D36, "è vietato l'affidamento o l'aggiudicazione di un appalto al contraente uscente")

D("amm-196", "Contratti pubblici", 3, "Secondo l'art. 5 del D.Lgs. 36/2023, a quali principi si conformano reciprocamente stazioni appaltanti e operatori economici?",
  "Buona fede e tutela dell'affidamento", ["Segretezza e discrezionalità", "Gerarchia e subordinazione", "Gratuità e oralità"],
  "Art. 5, c. 1.",
  "D.Lgs. 36/2023, art. 5", D36, "nel rispetto dei principi di buona fede e di tutela dell'affidamento")

D("amm-197", "Contratti pubblici", 4, "Qual è il criterio generale di aggiudicazione degli appalti nel D.Lgs. 36/2023?",
  "L'offerta economicamente più vantaggiosa", ["Il sorteggio tra i partecipanti", "La sola anzianità dell'impresa", "Il prezzo più alto"],
  "Art. 108, c. 1: individuata sul miglior rapporto qualità/prezzo o sul prezzo/costo.",
  "D.Lgs. 36/2023, art. 108", D36, "sulla base del criterio dell'offerta economicamente più vantaggiosa")

D("amm-198", "Contratti pubblici", 2, "Quale principio, all'art. 3 del D.Lgs. 36/2023, impone di favorire la partecipazione degli operatori economici alle gare?",
  "Il principio dell'accesso al mercato", ["Il principio di tipicità", "Il principio di autotutela", "Il principio di sussidiarietà orizzontale"],
  "Art. 3: nel rispetto di concorrenza, imparzialità, non discriminazione, pubblicità, trasparenza e proporzionalità.",
  "D.Lgs. 36/2023, art. 3", D36, "Principio dell'accesso al mercato")

D("amm-199", "Anticorruzione", 3, "Quale misura prevede la L. 190/2012 negli uffici più esposti al rischio di corruzione?",
  "La rotazione degli incarichi", ["L'abolizione dei dirigenti", "La chiusura degli uffici", "L'assunzione solo di personale esterno"],
  "La L. 190/2012 prevede la rotazione degli incarichi dove è più elevato il rischio di reati di corruzione.",
  "L. 190/2012, art. 1", L190, "rotazione degli incarichi negli uffici preposti allo svolgimento delle attività nel cui ambito è più elevato il rischio")

D("amm-200", "Anticorruzione", 3, "Con quale strumento ogni amministrazione pianifica le misure contro la corruzione, secondo le indicazioni del Piano nazionale anticorruzione?",
  "Il piano triennale per la prevenzione della corruzione", ["Il bilancio consuntivo", "Il regolamento edilizio", "Il documento di valutazione dei rischi per la sicurezza"],
  "La L. 190/2012 prevede il piano triennale (oggi confluito nel PIAO), secondo il PNA dell'ANAC.",
  "L. 190/2012, art. 1", L190, "piano triennale per la prevenzione della corruzione, secondo le indicazioni contenute nel Piano nazionale anticorruzione")

D("amm-201", "Anticorruzione", 4, "I comuni sotto 15.000 abitanti possono definire insieme le attività anticorruzione?",
  "Sì, possono aggregarsi tramite accordi", ["No, ognuno deve fare da sé", "Solo con autorizzazione del prefetto", "Solo se appartengono alla stessa unione montana"],
  "La L. 190/2012 consente ai piccoli comuni di aggregarsi.",
  "L. 190/2012, art. 1", L190, "I comuni con popolazione inferiore a 15.000 abitanti possono aggregarsi")

# --- v2: anticorruzione, incarichi, codice di comportamento (L. 190/2012) ---
D("amm-202", "Anticorruzione", 2, "Quanto dura il Piano nazionale anticorruzione (PNA) e ogni quanto si aggiorna?",
  "Ha durata triennale ed è aggiornato annualmente", ["È annuale e non si aggiorna", "Ha durata quinquennale ed è aggiornato ogni due anni", "Non ha scadenza e si aggiorna solo per legge"],
  "Art. 1, comma 2-bis, L. 190/2012: il Piano ha durata triennale ed è aggiornato annualmente; è atto di indirizzo per i piani delle singole amministrazioni.",
  "L. 190/2012, art. 1, c. 2-bis", L190, "Il Piano ha durata triennale ed è aggiornato annualmente")

D("amm-203", "Anticorruzione", 3, "Entro quale data l'organo di indirizzo adotta ogni anno il piano triennale per la prevenzione della corruzione?",
  "Entro il 31 gennaio", ["Entro il 31 dicembre", "Entro il 30 giugno", "Entro il 15 dicembre"],
  "Art. 1, comma 8: l'organo di indirizzo adotta il Piano su proposta del RPCT entro il 31 gennaio di ogni anno e lo trasmette all'ANAC.",
  "L. 190/2012, art. 1, c. 8", L190, "della corruzione e della trasparenza entro il 31 gennaio di ogni anno")

D("amm-204", "Anticorruzione", 2, "Negli enti locali, quale organo approva il piano triennale per la prevenzione della corruzione?",
  "La giunta", ["Il consiglio comunale", "Il sindaco con proprio decreto", "Il segretario comunale"],
  "Art. 1, comma 8, L. 190/2012: negli enti locali il piano è approvato dalla giunta, su proposta del Responsabile della prevenzione della corruzione e della trasparenza.",
  "L. 190/2012, art. 1, c. 8", L190, "Negli enti locali il piano è approvato dalla giunta")

D("amm-205", "Anticorruzione", 3, "L'elaborazione del piano anticorruzione di un ente può essere affidata a una società di consulenza esterna?",
  "No, non può essere affidata a soggetti estranei all'amministrazione", ["Sì, sempre", "Sì, se il comune ha meno di 15.000 abitanti", "Sì, con il parere favorevole dell'ANAC"],
  "Art. 1, comma 8: l'attività di elaborazione del piano non può essere affidata a soggetti estranei all'amministrazione.",
  "L. 190/2012, art. 1, c. 8", L190, "L'attività di elaborazione del piano non può essere affidata a soggetti estranei all'amministrazione")

D("amm-206", "Anticorruzione", 3, "Negli enti locali, chi è individuato di norma come Responsabile della prevenzione della corruzione e della trasparenza?",
  "Il segretario o il dirigente apicale", ["Il sindaco", "Il presidente del consiglio comunale", "Il revisore dei conti"],
  "Art. 1, comma 7: negli enti locali l'RPCT è individuato, di norma, nel segretario o nel dirigente apicale, salva diversa e motivata determinazione; nelle unioni di comuni può esserci un unico responsabile.",
  "L. 190/2012, art. 1, c. 7", L190, "è individuato, di norma, nel segretario o nel dirigente apicale")

D("amm-207", "Anticorruzione", 3, "Entro quale data l'RPCT trasmette all'organismo indipendente di valutazione e all'organo di indirizzo la relazione sull'attività svolta?",
  "Entro il 15 dicembre di ogni anno", ["Entro il 31 gennaio di ogni anno", "Entro il 30 aprile di ogni anno", "Entro il 31 luglio di ogni anno"],
  "Art. 1, comma 14: entro il 15 dicembre l'RPCT trasmette la relazione con i risultati dell'attività svolta e la pubblica sul sito dell'amministrazione.",
  "L. 190/2012, art. 1, c. 14", L190, "Entro il 15 dicembre di ogni anno, il dirigente individuato ai sensi del comma 7")

D("amm-208", "Anticorruzione", 2, "Che cosa costituisce, per il dipendente, la violazione delle misure di prevenzione previste dal piano anticorruzione?",
  "Un illecito disciplinare", ["Un semplice inadempimento senza conseguenze", "Sempre un reato", "Una causa automatica di decadenza dall'impiego"],
  "Art. 1, comma 14: la violazione, da parte dei dipendenti, delle misure di prevenzione previste dal Piano costituisce illecito disciplinare.",
  "L. 190/2012, art. 1, c. 14", L190, "delle misure di prevenzione previste dal Piano costituisce illecito disciplinare")

D("amm-209", "Anticorruzione", 4, "Se nell'amministrazione è commesso un reato di corruzione accertato con sentenza definitiva, qual è la sanzione disciplinare minima per l'RPCT che non prova di aver vigilato?",
  "La sospensione dal servizio senza retribuzione da un mese a sei mesi", ["Il richiamo verbale", "La multa fino a quattro ore di retribuzione", "Il licenziamento senza preavviso"],
  "Art. 1, comma 13: la sanzione a carico del responsabile non può essere inferiore alla sospensione dal servizio con privazione della retribuzione da un mese a sei mesi.",
  "L. 190/2012, art. 1, c. 13", L190, "non può essere inferiore alla sospensione dal servizio con privazione della retribuzione da un minimo di un mese ad un massimo di sei mesi")

D("amm-210", "Anticorruzione", 4, "Il dipendente che negli ultimi tre anni di servizio ha esercitato poteri autoritativi o negoziali, per quanto tempo dopo la cessazione non può lavorare per i privati destinatari di quei poteri («pantouflage»)?",
  "Per tre anni", ["Per un anno", "Per sei mesi", "Per cinque anni"],
  "Art. 53, comma 16-ter, D.Lgs. 165/2001 (introdotto dalla L. 190/2012): il divieto dura nei tre anni successivi alla cessazione del rapporto di pubblico impiego.",
  "L. 190/2012, art. 1, c. 42 (art. 53, c. 16-ter, D.Lgs. 165/2001)", L190, "nei tre anni successivi alla cessazione del rapporto di pubblico impiego")

D("amm-211", "Anticorruzione", 4, "Che sorte hanno i contratti conclusi con un ex dipendente in violazione del divieto di «pantouflage»?",
  "Sono nulli, e il privato non può contrattare con le PA per tre anni", ["Sono validi ma il dipendente paga una multa", "Sono annullabili solo su richiesta dell'ANAC", "Restano validi se il compenso è restituito"],
  "Art. 53, comma 16-ter, D.Lgs. 165/2001: i contratti e gli incarichi sono nulli e i privati che li hanno conclusi non possono contrattare con le pubbliche amministrazioni per i tre anni successivi.",
  "L. 190/2012, art. 1, c. 42 (art. 53, c. 16-ter, D.Lgs. 165/2001)", L190, "I contratti conclusi e gli incarichi conferiti in violazione di quanto previsto dal presente comma sono nulli")

D("amm-212", "Anticorruzione", 3, "Chi è stato condannato, anche con sentenza non definitiva, per un reato contro la pubblica amministrazione può far parte di una commissione di concorso?",
  "No, nemmeno con compiti di segreteria", ["Sì, se la condanna non è definitiva", "Sì, ma solo come segretario", "Sì, se autorizzato dal dirigente"],
  "Art. 35-bis D.Lgs. 165/2001 (introdotto dalla L. 190/2012): i condannati, anche con sentenza non passata in giudicato, per i reati contro la PA non possono fare parte, anche con compiti di segreteria, di commissioni per l'accesso o la selezione a pubblici impieghi.",
  "L. 190/2012, art. 1, c. 46 (art. 35-bis D.Lgs. 165/2001)", L190, "non possono fare parte, anche con compiti di segreteria, di commissioni per l'accesso o la selezione a pubblici impieghi")

D("amm-213", "Anticorruzione", 2, "Per quali procedimenti la L. 190/2012 chiede in particolare di garantire i livelli essenziali di trasparenza?",
  "Autorizzazioni e concessioni, scelta del contraente, contributi e vantaggi economici, concorsi e progressioni di carriera", ["Solo i procedimenti penali", "Solo i matrimoni e le unioni civili", "Solo le elezioni amministrative"],
  "Art. 1, comma 16: autorizzazione o concessione; scelta del contraente; concessione di sovvenzioni e vantaggi economici; concorsi e prove selettive per l'assunzione del personale e progressioni di carriera.",
  "L. 190/2012, art. 1, c. 16", L190, "concorsi e prove selettive per l'assunzione del personale e progressioni di carriera")

D("amm-214", "Anticorruzione", 3, "Cosa possono prevedere le stazioni appaltanti nei bandi per il mancato rispetto dei protocolli di legalità o dei patti di integrità?",
  "L'esclusione dalla gara", ["Solo una sanzione pecuniaria", "La sospensione del bando", "Nessuna conseguenza: sono impegni morali"],
  "Art. 1, comma 17: le stazioni appaltanti possono prevedere che il mancato rispetto delle clausole dei protocolli di legalità o dei patti di integrità sia causa di esclusione dalla gara.",
  "L. 190/2012, art. 1, c. 17", L190, "nei patti di integrità costituisce causa di esclusione dalla gara")

D("amm-215", "Anticorruzione", 2, "Cosa deve rendere noto ogni amministrazione sul proprio sito, per le istanze e le informazioni dei cittadini (L. 190/2012)?",
  "Almeno un indirizzo di posta elettronica certificata", ["Il numero di cellulare del sindaco", "L'elenco dei dipendenti con l'indirizzo di casa", "Un numero di fax per ogni ufficio"],
  "Art. 1, comma 29: ogni amministrazione rende noto, tramite il sito, almeno un indirizzo PEC a cui il cittadino possa trasmettere istanze e chiedere informazioni sui provvedimenti che lo riguardano.",
  "L. 190/2012, art. 1, c. 29", L190, "almeno un indirizzo di posta elettronica certificata cui il cittadino possa rivolgersi")

D("amm-216", "Anticorruzione", 4, "I magistrati possono partecipare a collegi arbitrali o assumere l'incarico di arbitro unico?",
  "No, pena la decadenza dagli incarichi e la nullità degli atti compiuti", ["Sì, se autorizzati dal capo dell'ufficio", "Sì, solo per gli arbitrati con la PA", "Sì, se l'incarico è gratuito"],
  "Art. 1, comma 18, L. 190/2012: a magistrati ordinari, amministrativi, contabili e militari, avvocati e procuratori dello Stato è vietata la partecipazione a collegi arbitrali, pena la decadenza e la nullità degli atti.",
  "L. 190/2012, art. 1, c. 18", L190, "è vietata, pena la decadenza dagli incarichi e la nullità degli atti compiuti, la partecipazione a collegi arbitrali")

D("amm-217", "Anticorruzione", 3, "Chi verifica che i piani anticorruzione siano coerenti con gli obiettivi dei documenti di programmazione strategico-gestionale?",
  "L'Organismo indipendente di valutazione (OIV)", ["La Corte dei conti", "Il revisore dei conti", "Il prefetto"],
  "Art. 1, comma 8-bis: l'OIV verifica, anche ai fini della validazione della Relazione sulla performance, la coerenza dei piani con gli obiettivi strategico-gestionali e riferisce all'ANAC.",
  "L. 190/2012, art. 1, c. 8-bis", L190, "L'Organismo indipendente di valutazione verifica, anche ai fini della validazione della Relazione sulla performance")

D("amm-218", "Anticorruzione", 3, "Entro quale data l'Autorità nazionale anticorruzione riferisce al Parlamento sull'attività di contrasto della corruzione?",
  "Entro il 31 dicembre di ciascun anno", ["Entro il 31 gennaio di ciascun anno", "Entro il 30 giugno di ciascun anno", "Ogni tre anni, con il nuovo Piano nazionale"],
  "Art. 1, comma 2, lettera g): l'ANAC riferisce al Parlamento presentando una relazione entro il 31 dicembre di ciascun anno.",
  "L. 190/2012, art. 1, c. 2", L190, "presentando una relazione entro il 31 dicembre di ciascun anno")

D("amm-219", "Codice di comportamento", 2, "Con quale atto è approvato il codice di comportamento nazionale dei dipendenti pubblici?",
  "Con decreto del Presidente della Repubblica, previa deliberazione del Consiglio dei ministri", ["Con legge ordinaria del Parlamento", "Con delibera dell'ANAC", "Con decreto del ministro dell'interno"],
  "Art. 54, comma 2, D.Lgs. 165/2001 (testo della L. 190/2012): il codice è approvato con DPR previa deliberazione del Consiglio dei ministri (oggi è il DPR 62/2013).",
  "L. 190/2012, art. 1, c. 44 (art. 54 D.Lgs. 165/2001)", L190, "approvato con decreto del Presidente della Repubblica, previa deliberazione del Consiglio dei ministri")

D("amm-220", "Codice di comportamento", 2, "Quando il dipendente pubblico sottoscrive il codice di comportamento?",
  "All'atto dell'assunzione", ["Alla fine del periodo di prova", "Solo se diventa dirigente", "Ogni anno, con la valutazione della performance"],
  "Art. 54, comma 2, D.Lgs. 165/2001: il codice è pubblicato in Gazzetta Ufficiale e consegnato al dipendente, che lo sottoscrive all'atto dell'assunzione.",
  "L. 190/2012, art. 1, c. 44 (art. 54 D.Lgs. 165/2001)", L190, "consegnato al dipendente, che lo sottoscrive all'atto dell'assunzione")

D("amm-221", "Codice di comportamento", 3, "Che tipo di responsabilità comporta la violazione dei doveri del codice di comportamento?",
  "Responsabilità disciplinare (e, se collegate, anche civile, amministrativa e contabile)", ["Nessuna: il codice è solo etico", "Solo responsabilità penale", "Solo una nota sul fascicolo personale"],
  "Art. 54, comma 3, D.Lgs. 165/2001: la violazione dei doveri del codice, compresi quelli del piano anticorruzione, è fonte di responsabilità disciplinare; violazioni gravi o reiterate portano al licenziamento (art. 55-quater, comma 1).",
  "L. 190/2012, art. 1, c. 44 (art. 54 D.Lgs. 165/2001)", L190, "compresi quelli relativi all'attuazione del Piano di prevenzione della corruzione, è fonte di responsabilità disciplinare")

D("amm-222", "Pubblico impiego", 3, "Entro quanti giorni dall'erogazione del compenso chi conferisce un incarico a un dipendente pubblico deve comunicarlo all'amministrazione di appartenenza?",
  "Entro quindici giorni", ["Entro trenta giorni", "Entro sessanta giorni", "Entro la fine dell'anno"],
  "Art. 53, comma 11, D.Lgs. 165/2001 (testo della L. 190/2012): entro quindici giorni dall'erogazione i soggetti pubblici o privati comunicano l'ammontare dei compensi erogati ai dipendenti pubblici.",
  "L. 190/2012, art. 1, c. 42 (art. 53, c. 11, D.Lgs. 165/2001)", L190, "Entro quindici giorni dall'erogazione del compenso per gli incarichi di cui al comma 6")

# --- v2: trasparenza e accesso civico (D.Lgs. 33/2013) ---
D("amm-223", "Trasparenza", 2, "La richiesta di accesso civico (D.Lgs. 33/2013) deve essere motivata?",
  "No, identifica i dati richiesti ma non richiede motivazione", ["Sì, va sempre spiegato l'interesse", "Sì, se riguarda dati personali", "Sì, se la presenta un'impresa"],
  "Art. 5, comma 3: l'istanza identifica i dati, le informazioni o i documenti richiesti e non richiede motivazione.",
  "D.Lgs. 33/2013, art. 5, c. 3", D33, "L'istanza di accesso civico identifica i dati, le informazioni o i documenti richiesti e non richiede motivazione")

D("amm-224", "Trasparenza", 2, "Quanto costa ottenere dati o documenti con l'accesso civico?",
  "È gratuito, salvo il rimborso del costo di riproduzione su supporti materiali", ["Si paga una marca da bollo da 16 euro", "Si paga un diritto fisso di ricerca", "È gratuito solo per i residenti"],
  "Art. 5, comma 4: il rilascio è gratuito, salvo il rimborso del costo effettivamente sostenuto e documentato per la riproduzione su supporti materiali.",
  "D.Lgs. 33/2013, art. 5, c. 4", D33, "Il rilascio di dati o documenti in formato elettronico o cartaceo è gratuito")

D("amm-225", "Trasparenza", 3, "Entro quanti giorni i controinteressati possono opporsi a una richiesta di accesso civico generalizzato?",
  "Dieci giorni dalla ricezione della comunicazione", ["Cinque giorni", "Trenta giorni", "Sessanta giorni"],
  "Art. 5, comma 5: entro dieci giorni dalla ricezione della comunicazione i controinteressati possono presentare una motivata opposizione; nel frattempo il termine per decidere è sospeso.",
  "D.Lgs. 33/2013, art. 5, c. 5", D33, "Entro dieci giorni dalla ricezione della comunicazione, i controinteressati possono presentare una motivata opposizione")

D("amm-226", "Trasparenza", 2, "Entro quale termine deve concludersi il procedimento di accesso civico?",
  "Trenta giorni dalla presentazione dell'istanza, con provvedimento espresso e motivato", ["Novanta giorni, con silenzio assenso", "Dieci giorni", "Non c'è un termine"],
  "Art. 5, comma 6: il procedimento si conclude con provvedimento espresso e motivato entro trenta giorni dalla presentazione dell'istanza.",
  "D.Lgs. 33/2013, art. 5, c. 6", D33, "deve concludersi con provvedimento espresso e motivato nel termine di trenta giorni")

D("amm-227", "Trasparenza", 3, "Se l'accesso civico è negato o non c'è risposta, a chi si chiede il riesame ed entro quanto deve decidere?",
  "Al Responsabile della prevenzione della corruzione e della trasparenza, che decide entro venti giorni", ["Al sindaco, entro trenta giorni", "Al TAR, entro sessanta giorni", "All'ANAC, entro novanta giorni"],
  "Art. 5, comma 7: il richiedente può presentare richiesta di riesame all'RPCT, che decide con provvedimento motivato entro venti giorni; resta poi il ricorso al TAR.",
  "D.Lgs. 33/2013, art. 5, c. 7", D33, "che decide con provvedimento motivato, entro il termine di venti giorni")

D("amm-228", "Trasparenza", 4, "Nel riesame di un accesso civico negato per tutela dei dati personali, chi deve sentire l'RPCT e in quanto tempo si pronuncia?",
  "Il Garante per la protezione dei dati personali, entro dieci giorni", ["L'ANAC, entro trenta giorni", "Il prefetto, entro quindici giorni", "Il difensore civico, entro venti giorni"],
  "Art. 5, comma 7: se il diniego tutela la protezione dei dati personali, l'RPCT provvede sentito il Garante, che si pronuncia entro dieci giorni.",
  "D.Lgs. 33/2013, art. 5, c. 7", D33, "il quale si pronuncia entro il termine di dieci giorni dalla richiesta")

D("amm-229", "Trasparenza", 3, "Per gli atti di regioni ed enti locali, a chi può ricorrere il richiedente contro il diniego di accesso civico, oltre al TAR?",
  "Al difensore civico competente per territorio", ["Al presidente della Repubblica", "Al prefetto", "Al consiglio comunale"],
  "Art. 5, comma 8: per gli atti di regioni ed enti locali si può ricorrere anche al difensore civico competente per ambito territoriale, che si pronuncia entro trenta giorni.",
  "D.Lgs. 33/2013, art. 5, c. 8", D33, "il richiedente può altresì presentare ricorso al difensore civico competente per ambito territoriale")

D("amm-230", "Trasparenza", 3, "Quale di questi interessi pubblici può giustificare il rifiuto dell'accesso civico generalizzato?",
  "La sicurezza pubblica e l'ordine pubblico", ["Il carico di lavoro dell'ufficio", "L'opportunità politica per la giunta", "Il desiderio di riservatezza del dirigente"],
  "Art. 5-bis, comma 1: l'accesso è rifiutato se serve a evitare un pregiudizio concreto a interessi come sicurezza pubblica e ordine pubblico, sicurezza nazionale, difesa, relazioni internazionali, stabilità finanziaria, indagini sui reati, attività ispettive.",
  "D.Lgs. 33/2013, art. 5-bis, c. 1", D33, "la sicurezza pubblica e l'ordine pubblico")

D("amm-231", "Trasparenza", 3, "Se i limiti all'accesso civico riguardano solo alcune parti di un documento, cosa deve fare l'amministrazione?",
  "Consentire l'accesso alle altre parti", ["Negare l'accesso a tutto il documento", "Chiedere il parere dell'ANAC", "Rinviare la decisione di un anno"],
  "Art. 5-bis, comma 4: se i limiti riguardano soltanto alcuni dati o alcune parti, deve essere consentito l'accesso agli altri dati o alle altre parti.",
  "D.Lgs. 33/2013, art. 5-bis, c. 4", D33, "deve essere consentito l'accesso agli altri dati o alle altre parti")

D("amm-232", "Trasparenza", 4, "Se l'accesso civico è accolto nonostante l'opposizione del controinteressato, quando si trasmettono i documenti al richiedente (salvo indifferibilità)?",
  "Non prima di quindici giorni dalla comunicazione al controinteressato", ["Subito, il giorno stesso", "Dopo sessanta giorni", "Solo dopo una sentenza del TAR"],
  "Art. 5, comma 6: l'amministrazione trasmette i dati non prima di quindici giorni dalla ricezione della comunicazione da parte del controinteressato, che così può reagire.",
  "D.Lgs. 33/2013, art. 5, c. 6", D33, "non prima di quindici giorni dalla ricezione della stessa comunicazione da parte del controinteressato")

D("amm-233", "Trasparenza", 4, "La pubblicazione degli incarichi di consulenza retribuiti affidati a soggetti esterni è:",
  "Condizione per l'efficacia dell'atto e per la liquidazione dei compensi", ["Facoltativa", "Richiesta solo sopra 40.000 euro", "Un semplice obbligo statistico senza effetti"],
  "Art. 15, comma 2: la pubblicazione degli estremi degli atti di conferimento e la comunicazione al Dipartimento della funzione pubblica sono condizioni per l'acquisizione dell'efficacia dell'atto e per la liquidazione dei compensi.",
  "D.Lgs. 33/2013, art. 15, c. 2", D33, "sono condizioni per l'acquisizione dell'efficacia dell'atto e per la liquidazione dei relativi compensi")

D("amm-234", "Trasparenza", 3, "Entro quando e per quanto tempo vanno pubblicati i dati degli incarichi di collaborazione e consulenza?",
  "Entro tre mesi dal conferimento e per i tre anni successivi alla cessazione", ["Entro un anno e per sempre", "Entro trenta giorni e per un anno", "Solo alla fine dell'incarico, per sei mesi"],
  "Art. 15, comma 4: i dati si pubblicano entro tre mesi dal conferimento dell'incarico e per i tre anni successivi alla cessazione.",
  "D.Lgs. 33/2013, art. 15, c. 4", D33, "entro tre mesi dal conferimento dell'incarico e per i tre anni successivi alla cessazione dell'incarico")

D("amm-235", "Trasparenza", 3, "Sopra quale importo gli atti di concessione di contributi e vantaggi economici devono essere pubblicati (art. 26 D.Lgs. 33/2013)?",
  "Sopra i mille euro", ["Sopra i diecimila euro", "Sopra i centomila euro", "Qualunque importo, anche un euro"],
  "Art. 26, comma 2: si pubblicano gli atti di concessione di importo superiore a mille euro; la pubblicazione è condizione legale di efficacia dei provvedimenti oltre i mille euro annui per beneficiario.",
  "D.Lgs. 33/2013, art. 26, c. 2", D33, "di importo superiore a mille euro")

D("amm-236", "Trasparenza", 4, "Quando non si pubblicano i dati identificativi delle persone fisiche che ricevono un contributo pubblico?",
  "Quando rivelerebbero lo stato di salute o la situazione di disagio economico-sociale", ["Mai: si pubblicano sempre", "Quando il contributo è inferiore a 5.000 euro", "Quando il beneficiario lo chiede per iscritto"],
  "Art. 26, comma 4: è esclusa la pubblicazione dei dati identificativi delle persone fisiche se da essi si ricavano informazioni su salute o disagio economico-sociale.",
  "D.Lgs. 33/2013, art. 26, c. 4", D33, "È esclusa la pubblicazione dei dati identificativi delle persone fisiche destinatarie dei provvedimenti")

D("amm-237", "Trasparenza", 3, "Entro quanti giorni dall'adozione vanno pubblicati bilancio preventivo e conto consuntivo?",
  "Trenta giorni", ["Novanta giorni", "Centoventi giorni", "Un anno"],
  "Art. 29, comma 1: le amministrazioni pubblicano documenti e allegati del bilancio preventivo e del conto consuntivo entro trenta giorni dalla loro adozione, anche in forma sintetica e semplificata.",
  "D.Lgs. 33/2013, art. 29, c. 1", D33, "del bilancio preventivo e del conto consuntivo entro trenta giorni dalla loro adozione")

D("amm-238", "Trasparenza", 4, "Che sanzione è prevista per la mancata comunicazione dei dati patrimoniali da parte del titolare di un incarico politico (art. 47 D.Lgs. 33/2013)?",
  "Una sanzione amministrativa da 500 a 10.000 euro", ["La decadenza automatica dalla carica", "La reclusione fino a un anno", "Un semplice richiamo scritto"],
  "Art. 47, comma 1: la mancata o incompleta comunicazione dà luogo a una sanzione amministrativa pecuniaria da 500 a 10.000 euro, pubblicata sul sito dell'ente.",
  "D.Lgs. 33/2013, art. 47, c. 1", D33, "a una sanzione amministrativa pecuniaria da 500 a 10.000 euro")

D("amm-239", "Trasparenza", 3, "Chi irroga le sanzioni per la violazione degli obblighi di trasparenza dell'art. 47 del D.Lgs. 33/2013?",
  "L'Autorità nazionale anticorruzione", ["Il Garante per la privacy", "Il prefetto", "La Corte dei conti"],
  "Art. 47, comma 3: le sanzioni sono irrogate dall'ANAC, che disciplina il procedimento con un proprio regolamento.",
  "D.Lgs. 33/2013, art. 47, c. 3", D33, "sono irrogate dall'Autorità nazionale anticorruzione")

D("amm-240", "Trasparenza", 2, "Quali dati dei titolari di incarichi politici devono pubblicare Stato, regioni ed enti locali (art. 14)?",
  "Atto di nomina con la durata, curriculum, compensi e altre cariche", ["Solo il nome e il partito", "Le cartelle cliniche", "I dati dei conti correnti dei figli"],
  "Art. 14, comma 1: atto di nomina o di proclamazione con la durata dell'incarico, curriculum, compensi, spese per viaggi di servizio, altre cariche e incarichi, dichiarazioni patrimoniali.",
  "D.Lgs. 33/2013, art. 14, c. 1", D33, "l'atto di nomina o di proclamazione, con l'indicazione della durata dell'incarico o del mandato elettivo")

D("amm-241", "Trasparenza", 3, "Cosa costituisce per il dirigente l'inadempimento degli obblighi di pubblicazione o il rifiuto ingiustificato dell'accesso civico?",
  "Elemento di valutazione negativa della responsabilità dirigenziale", ["Un reato di omissione d'atti d'ufficio in ogni caso", "Nulla, se l'ufficio ha poco personale", "Una causa di decadenza automatica dall'incarico"],
  "Art. 46, comma 1: costituiscono elemento di valutazione negativa della responsabilità dirigenziale ed eventuale causa di responsabilità per danno all'immagine, e incidono sulla retribuzione di risultato.",
  "D.Lgs. 33/2013, art. 46, c. 1", D33, "costituiscono elemento di valutazione negativa della responsabilità dirigenziale")

D("amm-242", "Trasparenza", 4, "Se una norma impone di pubblicare un atto che contiene dati personali non pertinenti alla finalità di trasparenza, cosa fa l'amministrazione?",
  "Rende non intelligibili quei dati personali", ["Pubblica l'atto integralmente", "Non pubblica l'atto", "Chiede il consenso agli interessati"],
  "Art. 7-bis, comma 4: le amministrazioni rendono non intelligibili i dati personali non pertinenti o, se sensibili o giudiziari, non indispensabili rispetto alle finalità della pubblicazione.",
  "D.Lgs. 33/2013, art. 7-bis, c. 4", D33, "provvedono a rendere non intelligibili i dati personali non pertinenti")

D("amm-243", "Trasparenza", 4, "Cosa pubblica l'amministrazione sul proprio sito riguardo agli emolumenti dei dirigenti (art. 14, comma 1-ter)?",
  "L'ammontare complessivo degli emolumenti a carico della finanza pubblica per ciascun dirigente", ["Solo lo stipendio medio di tutti i dirigenti", "Le buste paga mensili con i dati bancari", "Nulla, sono dati riservati"],
  "Art. 14, comma 1-ter: ogni dirigente comunica gli emolumenti complessivi percepiti a carico della finanza pubblica e l'amministrazione ne pubblica l'ammontare complessivo per ciascun dirigente.",
  "D.Lgs. 33/2013, art. 14, c. 1-ter", D33, "L'amministrazione pubblica sul proprio sito istituzionale l'ammontare complessivo dei suddetti emolumenti per ciascun dirigente")

D("amm-244", "Trasparenza", 5, "Che conseguenza ha la mancata pubblicazione dei rendiconti dei gruppi consiliari regionali e provinciali?",
  "La riduzione del 50 per cento delle risorse da trasferire nell'anno", ["Lo scioglimento del gruppo", "Una multa di 500 euro a ogni consigliere", "Nessuna conseguenza economica"],
  "Art. 28, comma 2: la mancata pubblicazione dei rendiconti comporta la riduzione del 50 per cento delle risorse da trasferire o assegnare nel corso dell'anno.",
  "D.Lgs. 33/2013, art. 28, c. 2", D33, "La mancata pubblicazione dei rendiconti comporta la riduzione del 50 per cento delle risorse")

# --- v2: codice dei contratti pubblici (D.Lgs. 36/2023, testo vigente) ---
D("amm-245", "Contratti pubblici", 3, "Qual è la soglia di rilevanza europea per gli appalti pubblici di lavori e per le concessioni (D.Lgs. 36/2023)?",
  "5.382.000 euro", ["140.000 euro", "1.000.000 di euro", "10.000.000 di euro"],
  "Art. 14, comma 1, lett. a): 5.382.000 euro per gli appalti pubblici di lavori e per le concessioni. Le soglie sono aggiornate periodicamente dalla Commissione europea.",
  "D.Lgs. 36/2023, art. 14", D36, "euro 5.382.000 per gli appalti pubblici di lavori e per le concessioni")

D("amm-246", "Contratti pubblici", 3, "Qual è la soglia europea per forniture e servizi aggiudicati da stazioni appaltanti sub-centrali, come i comuni?",
  "215.000 euro", ["140.000 euro", "750.000 euro", "5.382.000 euro"],
  "Art. 14, comma 1, lett. c): 215.000 euro per forniture, servizi e concorsi di progettazione delle stazioni appaltanti sub-centrali; 140.000 per le autorità governative centrali.",
  "D.Lgs. 36/2023, art. 14", D36, "euro 215.000 per gli appalti pubblici di forniture, di servizi e per i concorsi pubblici di progettazione")

D("amm-247", "Contratti pubblici", 4, "Qual è la soglia europea per forniture e servizi aggiudicati dalle autorità governative centrali?",
  "140.000 euro", ["215.000 euro", "431.000 euro", "40.000 euro"],
  "Art. 14, comma 1, lett. b): 140.000 euro per le autorità governative centrali indicate nell'allegato I alla direttiva 2014/24/UE.",
  "D.Lgs. 36/2023, art. 14", D36, "euro 140.000 per gli appalti pubblici di forniture, di servizi")

D("amm-248", "Contratti pubblici", 4, "Qual è la soglia europea per gli appalti di servizi sociali e assimilati nei settori ordinari?",
  "750.000 euro", ["215.000 euro", "1.000.000 di euro", "5.382.000 euro"],
  "Art. 14, comma 1, lett. d): 750.000 euro per i servizi sociali e assimilati elencati nell'allegato XIV della direttiva 2014/24/UE.",
  "D.Lgs. 36/2023, art. 14", D36, "euro 750.000 per gli appalti di servizi sociali e assimilati")

D("amm-249", "Contratti pubblici", 2, "Si può dividere artificiosamente un appalto in più parti per restare sotto le soglie europee?",
  "No, salvo ragioni oggettive che lo giustifichino", ["Sì, è sempre consentito", "Sì, se ogni parte è sotto i 40.000 euro", "Sì, con l'autorizzazione del sindaco"],
  "Art. 14: un appalto non può essere frazionato per evitare l'applicazione delle norme del codice, tranne nel caso in cui ragioni oggettive lo giustifichino.",
  "D.Lgs. 36/2023, art. 14", D36, "Un appalto non può essere frazionato per evitare l'applicazione delle norme del codice")

D("amm-250", "Contratti pubblici", 3, "Quando la stazione appaltante nomina il RUP (responsabile unico del progetto)?",
  "Nel primo atto di avvio dell'intervento pubblico", ["Dopo l'aggiudicazione", "Alla stipula del contratto", "Al collaudo"],
  "Art. 15, comma 1: il RUP è nominato nel primo atto di avvio dell'intervento, per programmazione, progettazione, affidamento ed esecuzione.",
  "D.Lgs. 36/2023, art. 15", D36, "Nel primo atto di avvio dell'intervento pubblico da realizzare mediante un contratto")

D("amm-251", "Contratti pubblici", 3, "Tra chi è nominato il RUP nelle pubbliche amministrazioni?",
  "Tra i dipendenti della stazione appaltante, anche a tempo determinato", ["Solo tra liberi professionisti esterni", "Tra i consiglieri comunali", "Tra i dipendenti dell'impresa aggiudicataria"],
  "Art. 15, comma 2: il RUP è nominato tra i dipendenti assunti anche a tempo determinato, preferibilmente dell'unità organizzativa titolare del potere di spesa, con requisiti e competenze adeguate.",
  "D.Lgs. 36/2023, art. 15", D36, "tra i dipendenti assunti anche a tempo determinato della stazione appaltante")

D("amm-252", "Contratti pubblici", 2, "In che forma va stipulato il contratto d'appalto pubblico?",
  "In forma scritta, a pena di nullità, in modalità elettronica", ["Anche solo verbalmente", "Solo con atto notarile cartaceo", "Con una stretta di mano davanti a testimoni"],
  "Art. 18, comma 1: il contratto è stipulato, a pena di nullità, in forma scritta e in modalità elettronica: forma pubblica amministrativa, atto pubblico notarile informatico o scrittura privata.",
  "D.Lgs. 36/2023, art. 18", D36, "Il contratto è stipulato, a pena di nullità, in forma scritta")

D("amm-253", "Contratti pubblici", 4, "Per affidamenti diretti e procedure negoziate, come può essere stipulato il contratto?",
  "Anche mediante scambio di lettere secondo l'uso commerciale, pure via PEC", ["Solo in forma pubblica amministrativa", "Solo con atto notarile", "Con una delibera del consiglio comunale"],
  "Art. 18, comma 1: per procedura negoziata e affidamenti diretti il contratto può essere stipulato mediante corrispondenza secondo l'uso commerciale, anche tramite posta elettronica certificata.",
  "D.Lgs. 36/2023, art. 18", D36, "mediante corrispondenza secondo l'uso commerciale, consistente in un apposito scambio di lettere")

D("amm-254", "Contratti pubblici", 3, "Entro quanto tempo dall'efficacia dell'aggiudicazione si stipula, di regola, il contratto?",
  "Entro sessanta giorni, anche se c'è un contenzioso", ["Entro dieci giorni", "Entro un anno", "Solo dopo la sentenza definitiva su eventuali ricorsi"],
  "Art. 18, comma 2: divenuta efficace l'aggiudicazione, la stipula ha luogo entro i successivi sessanta giorni anche in pendenza di contenzioso, salve le eccezioni previste.",
  "D.Lgs. 36/2023, art. 18", D36, "la stipula del contratto ha luogo entro i successivi sessanta giorni anche in pendenza di contenzioso")

D("amm-255", "Contratti pubblici", 4, "Quanti giorni devono passare, nel testo vigente del D.Lgs. 36/2023, dall'ultima comunicazione dell'aggiudicazione prima di poter stipulare il contratto («stand still»)?",
  "32 giorni", ["35 giorni", "15 giorni", "60 giorni"],
  "Art. 18, comma 3: il contratto non può essere stipulato prima di trentadue giorni dall'invio dell'ultima comunicazione dell'aggiudicazione (prima del correttivo erano 35). Il termine non vale ad esempio sotto le soglie europee.",
  "D.Lgs. 36/2023, art. 18", D36, "Il contratto non può essere stipulato prima di ((trentadue)) giorni dall'invio dell'ultima delle comunicazioni")

D("amm-256", "Contratti pubblici", 2, "Quali programmi adottano le stazioni appaltanti secondo il D.Lgs. 36/2023?",
  "Il programma triennale dei lavori pubblici e il programma triennale degli acquisti di beni e servizi", ["Solo un programma annuale delle spese", "Un programma quinquennale delle opere", "Nessun programma: si decide gara per gara"],
  "Art. 37: le stazioni appaltanti adottano il programma triennale dei lavori pubblici e il programma triennale degli acquisti di beni e servizi, in coerenza con il bilancio.",
  "D.Lgs. 36/2023, art. 37", D36, "adottano il programma triennale dei lavori pubblici e il programma triennale degli acquisti di beni e servizi")

D("amm-257", "Contratti pubblici", 1, "Nella procedura aperta, chi può presentare un'offerta?",
  "Qualsiasi operatore economico interessato", ["Solo gli operatori invitati dalla stazione appaltante", "Solo le imprese con sede nel comune", "Solo chi ha già lavorato con l'ente"],
  "Art. 71: nelle procedure aperte qualsiasi operatore economico interessato può presentare un'offerta in risposta a un avviso di indizione di gara.",
  "D.Lgs. 36/2023, art. 71", D36, "Nelle procedure aperte qualsiasi operatore economico interessato può presentare un'offerta")

D("amm-258", "Contratti pubblici", 4, "Quando si può usare la procedura negoziata senza pubblicazione di un bando di gara?",
  "Solo nei casi previsti dall'articolo 76", ["Sempre, a scelta del RUP", "Per tutti gli appalti di lavori", "Quando l'ente ha fretta di spendere"],
  "Art. 70, comma 2: nei soli casi previsti dall'articolo 76 le stazioni appaltanti possono utilizzare la procedura negoziata senza pubblicazione di un bando.",
  "D.Lgs. 36/2023, art. 70", D36, "Nei soli casi previsti dall'articolo 76 le stazioni appaltanti possono utilizzare la procedura negoziata senza pubblicazione di un bando")

D("amm-259", "Contratti pubblici", 3, "Nel soccorso istruttorio, che termine assegna la stazione appaltante per integrare i documenti mancanti?",
  "Non inferiore a cinque e non superiore a dieci giorni", ["Ventiquattro ore", "Trenta giorni", "Sessanta giorni"],
  "Art. 101, comma 1: la stazione appaltante assegna un termine non inferiore a cinque giorni e non superiore a dieci giorni.",
  "D.Lgs. 36/2023, art. 101", D36, "un termine non inferiore a cinque giorni e non superiore a dieci giorni")

D("amm-260", "Contratti pubblici", 3, "Il soccorso istruttorio permette di integrare l'offerta tecnica o l'offerta economica?",
  "No, l'offerta tecnica e quella economica sono escluse", ["Sì, sempre", "Sì, ma solo l'offerta economica", "Sì, se lo chiede l'operatore entro dieci giorni"],
  "Art. 101: si integrano domanda di partecipazione, DGUE e documenti richiesti, con esclusione della documentazione che compone l'offerta tecnica e l'offerta economica.",
  "D.Lgs. 36/2023, art. 101", D36, "con esclusione della documentazione che compone l'offerta tecnica e l'offerta economica")

D("amm-261", "Contratti pubblici", 3, "A quanto ammonta, di regola, la garanzia provvisoria che accompagna l'offerta?",
  "Al 2 per cento del valore complessivo della procedura", ["Al 10 per cento dell'importo contrattuale", "Al 20 per cento del valore", "A una cifra fissa di 1.000 euro"],
  "Art. 106, comma 1: l'offerta è corredata da una garanzia provvisoria pari al 2 per cento del valore complessivo della procedura.",
  "D.Lgs. 36/2023, art. 106", D36, "garanzia provvisoria pari al 2 per cento del valore complessivo della procedura")

D("amm-262", "Contratti pubblici", 4, "Entro quali limiti la stazione appaltante può modificare, motivando, la garanzia provvisoria?",
  "Ridurla fino all'1 per cento o aumentarla fino al 4 per cento", ["Solo azzerarla", "Ridurla fino allo 0,5 o aumentarla fino al 10 per cento", "Non può modificarla"],
  "Art. 106, comma 1: la stazione appaltante può motivatamente ridurre l'importo sino all'1 per cento oppure incrementarlo sino al 4 per cento.",
  "D.Lgs. 36/2023, art. 106", D36, "ridurre l'importo sino all'1 per cento oppure incrementarlo sino al 4 per cento")

D("amm-263", "Contratti pubblici", 3, "A quanto ammonta la garanzia definitiva richiesta all'appaltatore per sottoscrivere il contratto?",
  "Al 10 per cento dell'importo contrattuale", ["Al 2 per cento del valore della procedura", "Al 50 per cento", "Nessuna: non è prevista"],
  "Art. 117, comma 1: l'appaltatore costituisce una garanzia definitiva, cauzione o fideiussione, pari al 10 per cento dell'importo contrattuale.",
  "D.Lgs. 36/2023, art. 117", D36, "pari al 10 per cento dell'importo contrattuale")

D("amm-264", "Contratti pubblici", 4, "Davanti a un'offerta che appare anormalmente bassa, che termine si dà all'operatore per le spiegazioni?",
  "Non superiore a quindici giorni", ["Non superiore a tre giorni", "Novanta giorni", "Nessuno: l'offerta va esclusa subito"],
  "Art. 110, comma 2: la stazione appaltante chiede per iscritto spiegazioni sul prezzo o sui costi, assegnando un termine non superiore a quindici giorni.",
  "D.Lgs. 36/2023, art. 110", D36, "assegnando a tal fine un termine non superiore a quindici giorni")

D("amm-265", "Contratti pubblici", 2, "Che cos'è il subappalto?",
  "Il contratto con cui l'appaltatore affida a terzi l'esecuzione di parte delle prestazioni", ["La cessione dell'intero contratto a un'altra impresa", "Un contratto tra due stazioni appaltanti", "La revisione dei prezzi dell'appalto"],
  "Art. 119, comma 2: è il contratto con cui l'appaltatore affida a terzi l'esecuzione di parte delle prestazioni, con organizzazione di mezzi e rischi a carico del subappaltatore.",
  "D.Lgs. 36/2023, art. 119", D36, "Il subappalto è il contratto con il quale l'appaltatore affida a terzi l'esecuzione di parte delle prestazioni")

D("amm-266", "Contratti pubblici", 3, "L'appaltatore può cedere a un'altra impresa il contratto d'appalto?",
  "No, la cessione del contratto è nulla (salvi i casi di modifica soggettiva previsti)", ["Sì, liberamente", "Sì, con un preavviso di trenta giorni", "Sì, se l'impresa è della stessa regione"],
  "Art. 119, comma 1: i contratti si eseguono in proprio e, fatto salvo l'art. 120, comma 1, lett. d), la cessione del contratto è nulla.",
  "D.Lgs. 36/2023, art. 119", D36, "la cessione del contratto è nulla")

D("amm-267", "Contratti pubblici", 5, "Nei contratti ad alta intensità di manodopera, entro quale limite la stazione appaltante fissa il tetto al punteggio economico?",
  "30 per cento", ["10 per cento", "50 per cento", "70 per cento"],
  "Art. 108: per i contratti ad alta intensità di manodopera la stazione appaltante stabilisce un tetto massimo per il punteggio economico entro il limite del 30 per cento, per premiare la qualità.",
  "D.Lgs. 36/2023, art. 108", D36, "un tetto massimo per il punteggio economico entro il limite del 30 per cento")

D("amm-268", "Contratti pubblici", 3, "Quale di queste è una causa di esclusione automatica dell'operatore economico dalla gara?",
  "La condanna con sentenza definitiva per uno dei reati indicati dal codice", ["Avere sede in un'altra regione", "Aver presentato l'offerta l'ultimo giorno", "Non aver mai lavorato con quella stazione appaltante"],
  "Art. 94: è causa di esclusione la condanna con sentenza definitiva o decreto penale di condanna irrevocabile per i reati elencati (associazione per delinquere, corruzione, frode, terrorismo…).",
  "D.Lgs. 36/2023, art. 94", D36, "la condanna con sentenza definitiva o decreto penale di condanna divenuto irrevocabile")

D("amm-269", "Contratti pubblici", 3, "Dove vanno trasmessi dati e documenti delle procedure di gara digitali?",
  "Alla Banca dati nazionale dei contratti pubblici", ["Al registro delle imprese", "All'albo pretorio cartaceo", "Al Ministero dell'interno"],
  "Il codice del 2023 digitalizza l'intero ciclo dei contratti: le piattaforme assicurano la pubblicazione e la trasmissione di dati e documenti alla Banca dati nazionale dei contratti pubblici, gestita dall'ANAC.",
  "D.Lgs. 36/2023, art. 22", D36, "la pubblicazione e la trasmissione dei dati e documenti alla Banca dati nazionale dei contratti pubblici")

# --- v2: enti locali — atti, controlli e finanza (D.Lgs. 267/2000, TUEL) ---
D("amm-270", "Enti locali", 2, "Per quanto tempo sono pubblicate all'albo pretorio le deliberazioni del comune?",
  "Quindici giorni consecutivi", ["Sette giorni", "Trenta giorni", "Sessanta giorni"],
  "Art. 124 TUEL: tutte le deliberazioni del comune e della provincia sono pubblicate all'albo pretorio per quindici giorni consecutivi, salvo specifiche disposizioni di legge.",
  "D.Lgs. 267/2000, art. 124", TUEL, "all'albo pretorio, nella sede dell'ente, per quindici giorni consecutivi")

D("amm-271", "Enti locali", 3, "Quando diventa esecutiva una deliberazione non soggetta a controllo?",
  "Dopo il decimo giorno dalla pubblicazione", ["Il giorno stesso dell'adozione", "Dopo trenta giorni dall'adozione", "Dopo il visto del prefetto"],
  "Art. 134, comma 3, TUEL: le deliberazioni non soggette a controllo diventano esecutive dopo il decimo giorno dalla loro pubblicazione.",
  "D.Lgs. 267/2000, art. 134", TUEL, "diventano esecutive dopo il decimo giorno dalla loro pubblicazione")

D("amm-272", "Enti locali", 3, "In caso di urgenza, con quale voto una delibera di consiglio o giunta può essere dichiarata immediatamente eseguibile?",
  "Con il voto della maggioranza dei componenti", ["All'unanimità dei presenti", "Con i due terzi dei consiglieri assegnati", "Con decreto del sindaco, senza voto"],
  "Art. 134, comma 4, TUEL: nel caso di urgenza le deliberazioni possono essere dichiarate immediatamente eseguibili con il voto espresso dalla maggioranza dei componenti.",
  "D.Lgs. 267/2000, art. 134", TUEL, "possono essere dichiarate immediatamente eseguibili con il voto espresso dalla maggioranza dei componenti")

D("amm-273", "Enti locali", 3, "Quali pareri servono su una proposta di deliberazione di giunta o consiglio che non sia mero atto di indirizzo?",
  "Regolarità tecnica del responsabile del servizio e, se ci sono riflessi finanziari, regolarità contabile del responsabile di ragioneria", ["Solo il parere del sindaco", "Il parere del Consiglio di Stato", "Il parere dei revisori su ogni delibera"],
  "Art. 49 TUEL: parere di regolarità tecnica del responsabile del servizio e, se la delibera ha riflessi economico-finanziari o patrimoniali, di regolarità contabile del responsabile di ragioneria.",
  "D.Lgs. 267/2000, art. 49", TUEL, "in ordine alla sola regolarità tecnica, del responsabile del servizio interessato")

D("amm-274", "Enti locali", 4, "Giunta e consiglio possono deliberare in modo diverso da quanto indicano i pareri di regolarità?",
  "Sì, ma devono darne adeguata motivazione nel testo della deliberazione", ["No, i pareri sono sempre vincolanti", "Sì, senza alcuna motivazione", "Solo con il consenso del prefetto"],
  "Art. 49, comma 4, TUEL: se non intendono conformarsi ai pareri, devono darne adeguata motivazione nel testo della deliberazione.",
  "D.Lgs. 267/2000, art. 49", TUEL, "devono darne adeguata motivazione nel testo della deliberazione")

D("amm-275", "Enti locali", 3, "Se l'ente non ha responsabili dei servizi, chi esprime i pareri sulle proposte di deliberazione?",
  "Il segretario dell'ente, in relazione alle sue competenze", ["Il sindaco", "Il presidente del consiglio comunale", "Nessuno: se ne fa a meno"],
  "Art. 49, comma 2, TUEL: in assenza dei responsabili dei servizi il parere è espresso dal segretario dell'ente.",
  "D.Lgs. 267/2000, art. 49", TUEL, "il parere è espresso dal segretario dell'ente, in relazione alle sue competenze")

D("amm-276", "Enti locali", 3, "Con quale maggioranza il consiglio comunale approva lo statuto (alla prima votazione)?",
  "I due terzi dei consiglieri assegnati", ["La maggioranza semplice dei presenti", "La maggioranza assoluta dei votanti", "L'unanimità"],
  "Art. 6, comma 4, TUEL: gli statuti sono deliberati con il voto favorevole dei due terzi dei consiglieri assegnati; se non si raggiunge, si ripete la votazione in successive sedute entro trenta giorni.",
  "D.Lgs. 267/2000, art. 6", TUEL, "con il voto favorevole dei due terzi dei consiglieri assegnati")

D("amm-277", "Enti locali", 2, "Su quali materie possono vertere i referendum comunali previsti dal TUEL?",
  "Solo su materie di esclusiva competenza locale", ["Su qualunque materia, anche le leggi nazionali", "Solo sulle tasse statali", "Sulla politica estera"],
  "Art. 8, comma 4, TUEL: consultazioni e referendum devono riguardare materie di esclusiva competenza locale.",
  "D.Lgs. 267/2000, art. 8", TUEL, "devono riguardare materie di esclusiva competenza locale")

D("amm-278", "Enti locali", 2, "Cosa promuovono i comuni per la partecipazione dei cittadini, secondo l'art. 8 del TUEL?",
  "Le libere forme associative e organismi di partecipazione popolare", ["Solo i partiti politici", "Le società partecipate", "I consorzi di bonifica"],
  "Art. 8, comma 1, TUEL: i comuni, anche su base di quartiere o di frazione, valorizzano le libere forme associative e promuovono organismi di partecipazione popolare.",
  "D.Lgs. 267/2000, art. 8", TUEL, "valorizzano le libere forme associative e promuovono organismi di partecipazione popolare")

D("amm-279", "Organi", 3, "Entro quanti giorni sindaco o assessori delegati rispondono alle interrogazioni dei consiglieri?",
  "Entro 30 giorni", ["Entro 7 giorni", "Entro 90 giorni", "Alla prima seduta utile, senza termine"],
  "Art. 43, comma 3, TUEL: il sindaco o gli assessori delegati rispondono entro 30 giorni alle interrogazioni e alle altre istanze di sindacato ispettivo.",
  "D.Lgs. 267/2000, art. 43", TUEL, "rispondono, entro 30 giorni, alle interrogazioni")

D("amm-280", "Organi", 3, "Che diritto hanno i consiglieri comunali verso gli uffici del comune?",
  "Ottenere tutte le notizie e informazioni utili al mandato, con obbligo di segreto nei casi di legge", ["Solo i documenti già pubblicati", "Nessuno: devono fare accesso come i cittadini", "Solo le informazioni sul bilancio"],
  "Art. 43, comma 2, TUEL: i consiglieri hanno diritto di ottenere dagli uffici tutte le notizie e le informazioni utili all'espletamento del mandato; sono tenuti al segreto nei casi previsti dalla legge.",
  "D.Lgs. 267/2000, art. 43", TUEL, "tutte le notizie e le informazioni in loro possesso, utili all'espletamento del proprio mandato")

D("amm-281", "Contabilità locale", 2, "Entro quale data il consiglio approva il rendiconto della gestione dell'anno precedente?",
  "Entro il 30 aprile", ["Entro il 31 dicembre", "Entro il 31 luglio", "Entro il 31 gennaio"],
  "Art. 227, comma 2, TUEL: il rendiconto è deliberato entro il 30 aprile dell'anno successivo, tenendo conto della relazione dell'organo di revisione.",
  "D.Lgs. 267/2000, art. 227", TUEL, "Il rendiconto della gestione è deliberato entro il 30 aprile dell'anno successivo")

D("amm-282", "Contabilità locale", 3, "Da quali documenti è composto il rendiconto della gestione di un ente locale?",
  "Conto del bilancio, conto economico e stato patrimoniale", ["Solo dal bilancio di previsione", "Dal DUP e dal PEG", "Dalla relazione del sindaco e dal piano delle opere"],
  "Art. 227, comma 1, TUEL: il rendiconto comprende il conto del bilancio, il conto economico e lo stato patrimoniale.",
  "D.Lgs. 267/2000, art. 227", TUEL, "il quale comprende il conto del bilancio, il conto economico e lo stato patrimoniale")

D("amm-283", "Contabilità locale", 4, "Almeno entro quale data di ogni anno il consiglio verifica il permanere degli equilibri di bilancio?",
  "Entro il 31 luglio", ["Entro il 31 marzo", "Entro il 30 novembre", "Solo con il rendiconto, entro il 30 aprile"],
  "Art. 193, comma 2, TUEL: almeno una volta entro il 31 luglio il consiglio dà atto del permanere degli equilibri generali o adotta le misure di riequilibrio.",
  "D.Lgs. 267/2000, art. 193", TUEL, "almeno una volta entro il ((31 luglio)) di ciascun anno")

D("amm-284", "Contabilità locale", 3, "Cosa succede se il bilancio di previsione non è approvato entro il 31 dicembre dell'anno precedente?",
  "L'ente opera in esercizio provvisorio o gestione provvisoria", ["Il comune non può spendere nulla", "Il bilancio dell'anno prima vale per sempre", "Il sindaco decade automaticamente"],
  "Art. 163 TUEL: senza bilancio approvato entro il 31 dicembre, la gestione si svolge secondo le regole dell'esercizio provvisorio o della gestione provvisoria.",
  "D.Lgs. 267/2000, art. 163", TUEL, "Se il bilancio di previsione non è approvato dal Consiglio entro il 31 dicembre dell'anno precedente")

D("amm-285", "Controlli interni", 3, "Da quanti membri è composto il collegio dei revisori dei conti nei comuni più grandi?",
  "Da tre membri", ["Da un solo membro", "Da cinque membri", "Da sette membri"],
  "Art. 234, comma 1, TUEL: i consigli eleggono con voto limitato a due componenti un collegio di revisori composto da tre membri.",
  "D.Lgs. 267/2000, art. 234", TUEL, "un collegio di revisori composto da tre membri")

D("amm-286", "Controlli interni", 3, "Nei comuni con meno di 15.000 abitanti, a chi è affidata la revisione economico-finanziaria?",
  "A un solo revisore", ["A un collegio di cinque revisori", "Al segretario comunale", "Alla Corte dei conti"],
  "Art. 234, comma 3, TUEL: nei comuni sotto 15.000 abitanti, nelle unioni di comuni e nelle comunità montane la revisione è affidata a un solo revisore.",
  "D.Lgs. 267/2000, art. 234", TUEL, "la revisione economico-finanziaria è affidata ad un solo revisore")

D("amm-287", "Controlli interni", 4, "Quanto dura in carica l'organo di revisione contabile di un ente locale?",
  "Tre anni, e non si può svolgere l'incarico più di due volte nello stesso ente", ["Cinque anni, rinnovabili senza limiti", "Un anno, rinnovabile", "Quanto il mandato del sindaco"],
  "Art. 235, comma 1, TUEL: l'organo di revisione dura in carica tre anni e i componenti non possono svolgere l'incarico per più di due volte nello stesso ente.",
  "D.Lgs. 267/2000, art. 235", TUEL, "L'organo di revisione contabile dura in carica tre anni")

D("amm-288", "Enti locali", 3, "Quale di queste è una funzione del segretario comunale secondo l'art. 97 del TUEL?",
  "Rogare, su richiesta dell'ente, i contratti in cui l'ente è parte", ["Approvare il bilancio", "Nominare la giunta", "Presiedere il consiglio comunale"],
  "Art. 97, comma 4, TUEL: il segretario roga i contratti nei quali l'ente è parte e autentica scritture private e atti unilaterali nell'interesse dell'ente.",
  "D.Lgs. 267/2000, art. 97", TUEL, "i contratti nei quali l'ente è parte e autentica")

D("amm-289", "Enti locali", 2, "Che ruolo ha il segretario comunale nelle riunioni di consiglio e giunta?",
  "Partecipa con funzioni consultive, referenti e di assistenza e cura la verbalizzazione", ["Le presiede e vota", "Non vi partecipa mai", "Vi partecipa solo se lo chiede l'opposizione"],
  "Art. 97, comma 4, lett. a), TUEL: il segretario partecipa con funzioni consultive, referenti e di assistenza alle riunioni del consiglio e della giunta e ne cura la verbalizzazione.",
  "D.Lgs. 267/2000, art. 97", TUEL, "partecipa con funzioni consultive, referenti e di assistenza alle riunioni del consiglio e della giunta e ne cura la verbalizzazione")

D("amm-290", "Enti locali", 3, "A chi vengono trasmesse in elenco le deliberazioni della giunta, contestualmente alla pubblicazione all'albo?",
  "Ai capigruppo consiliari", ["Al prefetto", "Alla Corte dei conti", "A tutti i cittadini via email"],
  "Art. 125 TUEL: contestualmente all'affissione all'albo le deliberazioni della giunta sono trasmesse in elenco ai capigruppo consiliari.",
  "D.Lgs. 267/2000, art. 125", TUEL, "le deliberazioni adottate dalla giunta sono trasmesse in elenco ai capigruppo consiliari")

# --- v2: reclutamento e procedimento disciplinare (D.Lgs. 165/2001) ---
D("amm-291", "Pubblico impiego", 2, "Quale principio devono rispettare le procedure di reclutamento nelle pubbliche amministrazioni (art. 35 D.Lgs. 165/2001)?",
  "Adeguata pubblicità della selezione e modalità che garantiscano l'imparzialità", ["Assunzione diretta su segnalazione politica", "Selezione riservata ai residenti nel comune", "Scelta libera del dirigente senza bando"],
  "Art. 35, comma 3, lett. a): adeguata pubblicità della selezione e modalità di svolgimento che garantiscano l'imparzialità e assicurino economicità e celerità.",
  "D.Lgs. 165/2001, art. 35", D165, "adeguata pubblicità della selezione e modalità di svolgimento che garantiscano l'imparzialità")

D("amm-292", "Pubblico impiego", 3, "Chi può far parte delle commissioni di concorso secondo l'art. 35 del D.Lgs. 165/2001?",
  "Esperti di provata competenza, che non siano componenti dell'organo politico, né abbiano cariche politiche o sindacali", ["Gli assessori della giunta", "I rappresentanti sindacali designati dalle confederazioni", "Chiunque scelga il sindaco"],
  "Art. 35, comma 3, lett. e): commissioni composte esclusivamente da esperti di provata competenza (funzionari, docenti, estranei) che non siano componenti dell'organo di direzione politica, non ricoprano cariche politiche e non siano rappresentanti sindacali.",
  "D.Lgs. 165/2001, art. 35", D165, "composizione delle commissioni esclusivamente con esperti di provata competenza nelle materie di concorso")

D("amm-293", "Pubblico impiego", 3, "Per quanto tempo restano vigenti le graduatorie dei concorsi pubblici?",
  "Due anni dalla data di approvazione", ["Sei mesi", "Cinque anni", "Fino al concorso successivo, senza limite"],
  "Art. 35, comma 5-ter: le graduatorie dei concorsi rimangono vigenti per un termine di due anni dalla data di approvazione.",
  "D.Lgs. 165/2001, art. 35", D165, "rimangono vigenti per un termine di due anni dalla data di approvazione")

D("amm-294", "Pubblico impiego", 3, "Quale quota dei posti nelle commissioni di concorso è riservata alle donne, salvo motivata impossibilità?",
  "Almeno un terzo", ["Almeno la metà", "Almeno un quarto", "Nessuna quota"],
  "Art. 57, comma 1, lett. a): le amministrazioni riservano alle donne, salva motivata impossibilità, almeno un terzo dei posti di componente delle commissioni di concorso.",
  "D.Lgs. 165/2001, art. 57", D165, "almeno un terzo dei posti di componente delle commissioni di concorso")

D("amm-295", "Pubblico impiego", 3, "Come si chiama l'organismo delle PA per le pari opportunità, il benessere di chi lavora e contro le discriminazioni?",
  "Comitato unico di garanzia (CUG)", ["Organismo indipendente di valutazione (OIV)", "Ufficio per i procedimenti disciplinari (UPD)", "Ufficio relazioni con il pubblico (URP)"],
  "Art. 57 D.Lgs. 165/2001: le amministrazioni costituiscono il Comitato unico di garanzia per le pari opportunità, la valorizzazione del benessere di chi lavora e contro le discriminazioni.",
  "D.Lgs. 165/2001, art. 57", D165, "Comitato unico di garanzia per le pari opportunità, la valorizzazione del benessere di chi lavora e contro le discriminazioni")

D("amm-296", "Pubblico impiego", 4, "Quale di questi è tra i principi del reclutamento elencati dall'art. 35, comma 3, del D.Lgs. 165/2001?",
  "Il decentramento delle procedure di reclutamento", ["L'assunzione per chiamata diretta", "La riserva totale ai figli dei dipendenti", "L'obbligo di prova orale in dialetto"],
  "Art. 35, comma 3: tra i principi figurano pubblicità, imparzialità, meccanismi oggettivi di verifica, pari opportunità, decentramento delle procedure e commissioni di esperti.",
  "D.Lgs. 165/2001, art. 35", D165, "decentramento delle procedure di reclutamento")

D("amm-297", "Pubblico impiego", 3, "Quale ufficio è competente per le infrazioni punibili con sanzione superiore al rimprovero verbale?",
  "L'ufficio per i procedimenti disciplinari (UPD)", ["Il responsabile della struttura", "Il sindaco", "Il giudice del lavoro"],
  "Art. 55-bis: ogni amministrazione individua l'ufficio per i procedimenti disciplinari competente per le infrazioni punibili con sanzione superiore al rimprovero verbale; il rimprovero verbale spetta al responsabile della struttura.",
  "D.Lgs. 165/2001, art. 55-bis", D165, "individua l'ufficio per i procedimenti disciplinari competente per le infrazioni punibili con sanzione superiore al rimprovero verbale")

D("amm-298", "Pubblico impiego", 4, "Con quale preavviso il dipendente è convocato per l'audizione a sua difesa nel procedimento disciplinare?",
  "Almeno venti giorni", ["Almeno tre giorni", "Almeno sessanta giorni", "Nessun preavviso"],
  "Art. 55-bis, comma 4: l'ufficio contesta per iscritto l'addebito e convoca l'interessato, con un preavviso di almeno venti giorni, per l'audizione in contraddittorio.",
  "D.Lgs. 165/2001, art. 55-bis", D165, "con un preavviso di almeno venti giorni, per l'audizione in contraddittorio a sua difesa")

D("amm-299", "Pubblico impiego", 3, "Durante l'audizione disciplinare, da chi può farsi assistere il dipendente?",
  "Da un procuratore o da un rappresentante sindacale", ["Solo da un familiare", "Da nessuno: deve presentarsi da solo", "Solo da un collega dello stesso ufficio"],
  "Art. 55-bis, comma 4: il dipendente può farsi assistere da un procuratore ovvero da un rappresentante dell'associazione sindacale cui aderisce o conferisce mandato.",
  "D.Lgs. 165/2001, art. 55-bis", D165, "Il dipendente può farsi assistere da un procuratore ovvero da un rappresentante")

D("amm-300", "Pubblico impiego", 4, "Entro quanto tempo dalla contestazione dell'addebito si conclude il procedimento disciplinare?",
  "Entro centoventi giorni", ["Entro trenta giorni", "Entro un anno", "Non c'è un termine"],
  "Art. 55-bis, comma 4: l'ufficio conclude il procedimento, con archiviazione o irrogazione della sanzione, entro centoventi giorni dalla contestazione dell'addebito.",
  "D.Lgs. 165/2001, art. 55-bis", D165, "entro centoventi giorni dalla contestazione dell'addebito")

D("amm-301", "Pubblico impiego", 4, "Quante assenze ingiustificate possono portare al licenziamento disciplinare del dipendente pubblico?",
  "Più di tre giorni, anche non continuativi, nell'arco di un biennio (o più di sette in dieci anni)", ["Un solo giorno", "Più di trenta giorni in un anno", "Nessun numero: l'assenza si punisce solo con la multa"],
  "Art. 55-quater: è causa di licenziamento l'assenza priva di valida giustificazione per più di tre giorni, anche non continuativi, nell'arco di un biennio o per più di sette giorni negli ultimi dieci anni.",
  "D.Lgs. 165/2001, art. 55-quater", D165, "superiore a tre nell'arco di un biennio o comunque per più di sette giorni nel corso degli ultimi dieci anni")
