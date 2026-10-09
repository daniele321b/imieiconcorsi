# Lavoro pubblico e previdenza — fonti: L. 300/1970, D.Lgs. 81/2015, D.Lgs. 81/2008 (Normattiva).
L300 = "norma_L300-1970_Statuto-lavoratori.txt"
D81_15 = "norma_DLgs81-2015_contratti-lavoro.txt"
D81_08 = "norma_DLgs81-2008_sicurezza-lavoro.txt"

D("lav-001", "Contratti di lavoro", 1, "Qual è, secondo il D.Lgs. 81/2015, la forma comune di rapporto di lavoro?",
  "Il contratto di lavoro subordinato a tempo indeterminato", ["Il contratto a tempo determinato", "La collaborazione coordinata e continuativa", "Il contratto di somministrazione"],
  "Art. 1 D.Lgs. 81/2015: il contratto di lavoro subordinato a tempo indeterminato costituisce la forma comune di rapporto di lavoro.",
  "D.Lgs. 81/2015, art. 1", D81_15, "Il contratto di lavoro subordinato a tempo indeterminato costituisce la forma comune di rapporto di lavoro")

D("lav-002", "Contratti di lavoro", 2, "Senza condizioni particolari, quale durata massima può avere un contratto a tempo determinato?",
  "12 mesi", ["6 mesi", "24 mesi", "36 mesi"],
  "Art. 19 D.Lgs. 81/2015: il termine non può superare dodici mesi; fino a ventiquattro solo in presenza delle condizioni previste.",
  "D.Lgs. 81/2015, art. 19", D81_15, "può essere apposto un termine di durata non superiore a dodici mesi")

D("lav-003", "Contratti di lavoro", 3, "Fino a quale durata massima può arrivare un contratto a termine in presenza delle condizioni previste dalla legge?",
  "24 mesi", ["18 mesi", "36 mesi", "48 mesi"],
  "Art. 19 D.Lgs. 81/2015: oltre i dodici mesi, ma comunque non oltre i ventiquattro, solo con le condizioni indicate (es. casi previsti dai contratti collettivi).",
  "D.Lgs. 81/2015, art. 19", D81_15, "ma comunque non eccedente i ventiquattro mesi")

D("lav-004", "Contratti di lavoro", 3, "Il rifiuto di un lavoratore part-time di concordare variazioni dell'orario di lavoro giustifica il licenziamento?",
  "No, non costituisce giustificato motivo di licenziamento", ["Sì, sempre", "Sì, se il contratto collettivo lo prevede", "Solo nei primi sei mesi"],
  "Art. 6 D.Lgs. 81/2015: il rifiuto del lavoratore di concordare variazioni dell'orario non costituisce giustificato motivo di licenziamento.",
  "D.Lgs. 81/2015, art. 6", D81_15, "Il rifiuto del lavoratore di concordare variazioni dell'orario di lavoro non costituisce giustificato motivo di licenziamento")

D("lav-005", "Diritti sindacali", 1, "Secondo lo Statuto dei lavoratori, a chi è garantito il diritto di costituire associazioni sindacali e di svolgere attività sindacale nei luoghi di lavoro?",
  "A tutti i lavoratori", ["Solo ai lavoratori a tempo indeterminato", "Solo ai rappresentanti sindacali", "Solo nelle aziende con più di 15 dipendenti"],
  "Art. 14 L. 300/1970: il diritto è garantito a tutti i lavoratori all'interno dei luoghi di lavoro.",
  "L. 300/1970, art. 14", L300, "è garantito a tutti i lavoratori all'interno dei luoghi di lavoro")

D("lav-006", "Diritti sindacali", 2, "Quante ore annue retribuite di assemblea durante l'orario di lavoro garantisce lo Statuto dei lavoratori?",
  "10 ore", ["5 ore", "12 ore", "20 ore"],
  "Art. 20 L. 300/1970: assemblee durante l'orario di lavoro nei limiti di dieci ore annue retribuite; i contratti collettivi possono migliorare.",
  "L. 300/1970, art. 20", L300, "nei limiti di dieci ore annue, per le quali verrà corrisposta la normale retribuzione")

D("lav-007", "Diritti sindacali", 3, "Quale strumento offre l'art. 28 dello Statuto contro il datore di lavoro che impedisce o limita l'attività sindacale?",
  "Il ricorso per la repressione della condotta antisindacale", ["Il ricorso al TAR", "L'arbitrato obbligatorio", "La denuncia all'Ispettorato del lavoro, unica via possibile"],
  "Art. 28 L. 300/1970: procedimento di repressione della condotta antisindacale davanti al giudice del lavoro.",
  "L. 300/1970, art. 28", L300, "Repressione della condotta antisindacale")

D("lav-008", "Sicurezza sul lavoro", 2, "Quale di queste attività il datore di lavoro NON può delegare, secondo il D.Lgs. 81/2008?",
  "La valutazione di tutti i rischi e l'elaborazione del relativo documento", ["La formazione dei lavoratori", "La gestione delle emergenze", "La sorveglianza sanitaria"],
  "Art. 17 D.Lgs. 81/2008: sono indelegabili la valutazione dei rischi con il DVR (art. 28) e la designazione del responsabile del servizio di prevenzione e protezione.",
  "D.Lgs. 81/2008, art. 17", D81_08, "Il datore di lavoro non può delegare le seguenti attività: a) la valutazione di tutti i rischi")

D("lav-009", "Sicurezza sul lavoro", 2, "Oltre alla valutazione dei rischi, quale altra attività è indelegabile per il datore di lavoro?",
  "La designazione del responsabile del servizio di prevenzione e protezione (RSPP)", ["La nomina del medico competente", "L'acquisto dei dispositivi di protezione", "La tenuta del registro infortuni"],
  "Art. 17 D.Lgs. 81/2008: le due attività non delegabili sono il DVR e la designazione dell'RSPP.",
  "D.Lgs. 81/2008, art. 17", D81_08, "b) la designazione del responsabile del servizio di prevenzione e protezione dai rischi")

D("lav-010", "Sicurezza sul lavoro", 2, "Chi è il rappresentante dei lavoratori per la sicurezza (RLS)?",
  "Una persona eletta o designata per rappresentare i lavoratori sugli aspetti di salute e sicurezza", ["Un medico nominato dall'ASL", "Il dirigente responsabile della sicurezza", "Un ispettore del lavoro"],
  "Art. 2 D.Lgs. 81/2008: l'RLS è eletto o designato per rappresentare i lavoratori per la salute e la sicurezza.",
  "D.Lgs. 81/2008, art. 2", D81_08, "persona eletta o designata per rappresentare i lavoratori per quanto concerne gli aspetti della salute e della sicure")

D("lav-011", "Sicurezza sul lavoro", 3, "Qual è la prima misura generale di tutela della salute e sicurezza elencata dal D.Lgs. 81/2008?",
  "La valutazione di tutti i rischi per la salute e sicurezza", ["L'acquisto dei dispositivi di protezione individuale", "La sorveglianza sanitaria", "L'informazione ai lavoratori"],
  "Art. 15 D.Lgs. 81/2008: la prima misura generale di tutela è la valutazione di tutti i rischi.",
  "D.Lgs. 81/2008, art. 15", D81_08, "a) la valutazione di tutti i rischi per la salute e sicurezza")

D("lav-012", "Sicurezza sul lavoro", 3, "Chi è il «medico competente» secondo il D.Lgs. 81/2008?",
  "Un medico con i titoli previsti che collabora con il datore di lavoro alla valutazione dei rischi e alla sorveglianza sanitaria",
  ["Il medico di base del lavoratore", "Il medico dell'ASL che effettua le ispezioni", "Qualsiasi medico scelto dal lavoratore"],
  "Art. 2 D.Lgs. 81/2008: il medico competente ha titoli e requisiti specifici (art. 38) e collabora con il datore di lavoro.",
  "D.Lgs. 81/2008, art. 2", D81_08, "\"medico competente\": medico in possesso di uno dei titoli e dei requisiti formativi e professionali di cui all'articolo 38")

D("lav-013", "Contratti di lavoro", 5, "Un'azienda propone a un neoassunto un contratto a termine di 18 mesi senza alcuna delle condizioni previste dalla legge. Cosa succede?",
  "Il termine oltre i 12 mesi non è legittimo: senza le condizioni previste il limite è 12 mesi",
  ["È valido, perché il limite generale è 24 mesi", "È valido se il lavoratore firma per accettazione", "Il contratto è nullo e il lavoratore non ha diritto a nulla"],
  "Art. 19 D.Lgs. 81/2015: oltre i dodici mesi servono le condizioni indicate dalla legge; altrimenti il superamento del limite non è consentito.",
  "D.Lgs. 81/2015, art. 19", D81_15, "solo in presenza di almeno una delle seguenti condizioni")


# --- Blocco 2: Statuto dei lavoratori (L. 300/1970) ---
def S(id, arg, liv, testo, giusta, sbagliate, spieg, art, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, f"L. 300/1970, {art}", L300, frase)

S("lav-014", "Statuto dei lavoratori", 1, "Quale diritto riconosce l'art. 1 dello Statuto dei lavoratori?",
  "La libertà di manifestare il proprio pensiero nei luoghi di lavoro", ["Il diritto alle ferie", "Il diritto allo sciopero", "Il diritto alla pensione"],
  "Art. 1: senza distinzione di opinioni politiche, sindacali e di fede religiosa.",
  "art. 1", "hanno diritto, nei luoghi dove prestano la loro opera, di manifestare liberamente il proprio pensiero")

S("lav-015", "Statuto dei lavoratori", 2, "Per quali scopi il datore di lavoro può impiegare guardie particolari giurate?",
  "Solo per la tutela del patrimonio aziendale", ["Per controllare la produttività dei dipendenti", "Per verificare le assenze per malattia", "Per qualsiasi scopo"],
  "Art. 2: non possono vigilare sull'attività lavorativa.",
  "art. 2", "soltanto per scopi di tutela del patrimonio aziendale")

S("lav-016", "Statuto dei lavoratori", 3, "Per quali esigenze possono essere installati impianti da cui derivi un possibile controllo a distanza dei lavoratori?",
  "Esigenze organizzative e produttive, sicurezza del lavoro e tutela del patrimonio aziendale", ["Per misurare la produttività individuale in ogni caso", "Per qualsiasi motivo, se il datore lo comunica", "Mai"],
  "Art. 4, c. 1: serve un accordo sindacale o, in mancanza, l'autorizzazione dell'Ispettorato.",
  "art. 4", "possono essere impiegati esclusivamente per esigenze organizzative e produttive")

S("lav-017", "Statuto dei lavoratori", 4, "In mancanza di accordo sindacale, chi autorizza l'installazione di strumenti di controllo a distanza?",
  "L'Ispettorato nazionale del lavoro", ["Il prefetto", "Il Garante privacy", "Il sindaco"],
  "Art. 4, c. 1.",
  "art. 4", "previa autorizzazione delle sede territoriale dell'Ispettorato nazionale del")

S("lav-018", "Statuto dei lavoratori", 4, "La disciplina sui controlli a distanza si applica agli strumenti usati dal lavoratore per rendere la prestazione (es. PC aziendale)?",
  "No, non si applica a tali strumenti né a quelli di registrazione delle presenze", ["Sì, sempre", "Solo per i dirigenti", "Solo nel settore pubblico"],
  "Art. 4, c. 2; le informazioni sono utilizzabili se il lavoratore è adeguatamente informato.",
  "art. 4", "non si applica agli strumenti utilizzati dal lavoratore per rendere la prestazione lavorativa")

S("lav-019", "Statuto dei lavoratori", 3, "Chi può controllare le assenze per malattia del lavoratore?",
  "Solo i servizi ispettivi degli istituti previdenziali competenti", ["Il datore di lavoro direttamente", "Un medico scelto dal datore", "I colleghi del reparto"],
  "Art. 5: sono vietati gli accertamenti sanitari diretti del datore.",
  "art. 5", "Il controllo delle assenze per infermità può essere effettuato soltanto attraverso i servizi ispettivi")

S("lav-020", "Statuto dei lavoratori", 4, "Quando sono ammesse le visite personali di controllo sul lavoratore?",
  "Solo se indispensabili per tutelare il patrimonio aziendale, all'uscita, con selezione automatica e nel rispetto della dignità", ["Sempre, a discrezione del datore", "Mai", "Solo su richiesta della polizia"],
  "Art. 6 L. 300/1970.",
  "art. 6", "Le visite personali di controllo sul lavoratore sono vietate fuorché")

S("lav-021", "Sanzioni disciplinari", 2, "Cosa deve fare il datore di lavoro prima di adottare un provvedimento disciplinare?",
  "Contestare preventivamente l'addebito e sentire il lavoratore a sua difesa", ["Nulla, può sanzionare subito", "Chiedere il permesso al sindacato", "Informare il prefetto"],
  "Art. 7, c. 2 L. 300/1970.",
  "art. 7", "senza avergli preventivamente contestato l'addebito e senza averlo sentito a sua difesa")

S("lav-022", "Sanzioni disciplinari", 3, "Qual è l'importo massimo della multa disciplinare secondo lo Statuto?",
  "Quattro ore della retribuzione base", ["Un mese di stipendio", "Dieci ore", "Una giornata"],
  "Art. 7, c. 4; la sospensione non può superare dieci giorni.",
  "art. 7", "la multa non può essere disposta per un importo superiore a quattro ore della retribuzione base")

S("lav-023", "Sanzioni disciplinari", 3, "Per quanti giorni al massimo può essere disposta la sospensione dal servizio e dalla retribuzione?",
  "Dieci giorni", ["Trenta giorni", "Cinque giorni", "Tre mesi"],
  "Art. 7, c. 4.",
  "art. 7", "la sospensione dal servizio e dalla retribuzione per più di dieci giorni")

S("lav-024", "Sanzioni disciplinari", 3, "Quanto tempo deve passare dalla contestazione scritta prima di applicare una sanzione più grave del rimprovero verbale?",
  "Cinque giorni", ["Un giorno", "Trenta giorni", "Due mesi"],
  "Art. 7, c. 5.",
  "art. 7", "prima che siano trascorsi cinque giorni dalla contestazione per iscritto")

S("lav-025", "Sanzioni disciplinari", 4, "Dopo quanto tempo non si può più tenere conto di una sanzione disciplinare?",
  "Decorsi due anni dalla sua applicazione", ["Mai, resta per sempre", "Dopo sei mesi", "Dopo cinque anni"],
  "Art. 7, ultimo comma.",
  "art. 7", "decorsi due anni dalla loro applicazione")

S("lav-026", "Statuto dei lavoratori", 2, "Il datore di lavoro può indagare sulle opinioni politiche o religiose di un candidato all'assunzione?",
  "No, è vietato", ["Sì, se il candidato acconsente", "Sì, tramite terzi", "Solo per i dirigenti"],
  "Art. 8 L. 300/1970.",
  "art. 8", "È fatto divieto al datore di lavoro, ai fini dell'assunzione")

S("lav-027", "Statuto dei lavoratori", 2, "Quale diritto hanno i lavoratori studenti che devono sostenere esami?",
  "Permessi giornalieri retribuiti", ["Un mese di ferie aggiuntivo", "Il pagamento delle tasse universitarie", "Nessuno"],
  "Art. 10: hanno anche diritto a turni che agevolino la frequenza e non sono obbligati agli straordinari.",
  "art. 10", "hanno diritto a fruire di permessi giornalieri retribuiti")

S("lav-028", "Diritti sindacali", 3, "Quali atti sono nulli secondo l'art. 15 dello Statuto?",
  "Patti o atti che discriminano il lavoratore per la sua attività sindacale o per motivi politici, religiosi, razziali, di sesso e altri", ["Gli accordi di straordinario", "I contratti part-time", "I trasferimenti motivati da esigenze tecniche"],
  "Art. 15 (atti discriminatori).",
  "art. 15", "È nullo qualsiasi patto od atto diretto a")

S("lav-029", "Diritti sindacali", 3, "Come si chiamano i sindacati costituiti o sostenuti dal datore di lavoro, vietati dall'art. 17?",
  "Sindacati di comodo", ["Sindacati autonomi", "Sindacati confederali", "Rappresentanze unitarie"],
  "Art. 17 L. 300/1970.",
  "art. 17", "Sindacati di comodo")

S("lav-030", "Licenziamento", 3, "In caso di licenziamento discriminatorio dichiarato nullo, cosa ordina il giudice ai sensi dell'art. 18?",
  "La reintegrazione nel posto di lavoro, qualunque sia il numero dei dipendenti", ["Solo un'indennità di due mensilità", "Nulla, il licenziamento resta valido", "Il trasferimento in altra sede"],
  "Art. 18, c. 1 (tutela reale piena).",
  "art. 18", "ordina al datore di lavoro, imprenditore o non imprenditore, la reintegrazione del lavoratore")

S("lav-031", "Licenziamento", 4, "Qual è la misura minima del risarcimento in caso di licenziamento nullo ex art. 18, c. 1-2?",
  "Cinque mensilità della retribuzione globale di fatto", ["Una mensilità", "Ventiquattro mensilità", "Nessun minimo"],
  "Art. 18, c. 2.",
  "art. 18", "non potrà essere inferiore a cinque mensilità")

S("lav-032", "Licenziamento", 4, "In sostituzione della reintegrazione, quale indennità può chiedere il lavoratore?",
  "Quindici mensilità dell'ultima retribuzione globale di fatto", ["Sei mensilità", "Trenta mensilità", "Un anno di contributi"],
  "Art. 18, c. 3: la richiesta va fatta entro trenta giorni e risolve il rapporto.",
  "art. 18", "un'indennità pari a quindici mensilità dell'ultima retribuzione globale di fatto")

S("lav-033", "Licenziamento", 5, "Nelle «altre ipotesi» di mancanza di giusta causa o giustificato motivo soggettivo, quale indennità prevede l'art. 18, c. 5?",
  "Tra dodici e ventiquattro mensilità", ["Tra due e sei mensilità", "Tra trenta e quaranta mensilità", "Sempre la reintegrazione"],
  "Art. 18, c. 5 (tutela indennitaria forte), nel testo successivo alla L. 92/2012.",
  "art. 18", "tra un minimo di dodici e un massimo di ventiquattro mensilità")

S("lav-034", "Licenziamento", 5, "A quali datori di lavoro si applicano, di regola, i commi 4-7 dell'art. 18?",
  "A chi occupa più di quindici dipendenti nell'unità produttiva o nel comune, o più di sessanta in totale", ["A tutti i datori, anche con un solo dipendente", "Solo alle pubbliche amministrazioni", "Solo alle imprese con più di mille dipendenti"],
  "Art. 18, c. 8 (per l'imprenditore agricolo la soglia è cinque).",
  "art. 18", "occupa alle sue dipendenze più di quindici lavoratori")

S("lav-035", "Licenziamento", 4, "Se il datore revoca il licenziamento entro quindici giorni dall'impugnazione, cosa accade?",
  "Il rapporto si intende ripristinato senza soluzione di continuità", ["Il lavoratore deve essere riassunto con nuovo contratto", "Il datore paga comunque 24 mensilità", "Il lavoratore perde l'anzianità"],
  "Art. 18, c. 10.",
  "art. 18", "il rapporto di lavoro si intende ripristinato senza soluzione di continuità")

S("lav-036", "Diritti sindacali", 3, "Nell'ambito di quali associazioni possono essere costituite le rappresentanze sindacali aziendali (RSA), secondo il testo dell'art. 19?",
  "Delle associazioni firmatarie di contratti collettivi applicati nell'unità produttiva", ["Di qualsiasi associazione, anche non sindacale", "Solo delle confederazioni con un milione di iscritti", "Solo dei sindacati dei dirigenti"],
  "Art. 19, come risultante dal referendum del 1995; la Corte costituzionale (sent. 231/2013 e 156/2025) ha esteso la possibilità ad altre associazioni.",
  "art. 19", "delle associazioni sindacali, che siano firmatarie di contratti collettivi di lavoro applicati nell'unità produttiva")

S("lav-037", "Diritti sindacali", 3, "Chi indice le assemblee dei lavoratori nell'unità produttiva?",
  "Le rappresentanze sindacali aziendali", ["Il datore di lavoro", "Il prefetto", "Il medico competente"],
  "Art. 20, c. 2.",
  "art. 20", "sono indette, singolarmente o congiuntamente, dalle rappresentanze sindacali aziendali")

S("lav-038", "Diritti sindacali", 3, "Quando si svolgono i referendum sindacali in azienda (art. 21)?",
  "Fuori dell'orario di lavoro", ["Durante l'orario di lavoro, retribuiti", "Solo di domenica", "Solo con il consenso del datore"],
  "Art. 21 L. 300/1970.",
  "art. 21", "fuori dell'orario di lavoro, di referendum")

S("lav-039", "Diritti sindacali", 4, "Il trasferimento di un dirigente RSA dall'unità produttiva richiede:",
  "Il previo nulla osta dell'associazione sindacale di appartenenza", ["Solo una comunicazione scritta", "L'autorizzazione del prefetto", "Il voto dei colleghi"],
  "Art. 22 L. 300/1970.",
  "art. 22", "può essere disposto solo previo nulla osta delle associazioni sindacali di appartenenza")

S("lav-040", "Diritti sindacali", 4, "Quanti giorni annui minimi di permessi non retribuiti spettano ai dirigenti sindacali aziendali per trattative e congressi?",
  "Otto giorni", ["Due giorni", "Trenta giorni", "Nessuno"],
  "Art. 24 L. 300/1970.",
  "art. 24", "in misura non inferiore a otto giorni all'anno")

S("lav-041", "Diritti sindacali", 3, "In quali unità produttive il datore deve mettere permanentemente a disposizione delle RSA un locale?",
  "In quelle con almeno 200 dipendenti", ["In tutte", "In quelle con almeno 15 dipendenti", "In quelle con almeno 1.000 dipendenti"],
  "Art. 27: nelle unità più piccole le RSA possono usare un locale su richiesta.",
  "art. 27", "nelle unità produttive con almeno 200 dipendenti")

S("lav-042", "Diritti sindacali", 2, "Cosa garantisce l'art. 25 dello Statuto alle RSA?",
  "Il diritto di affissione di comunicati sindacali in appositi spazi", ["Il diritto di firmare i contratti individuali", "Il diritto di gestire le buste paga", "Il diritto di nominare i dirigenti"],
  "Art. 25 L. 300/1970.",
  "art. 25", "hanno diritto di affiggere, su appositi spazi")

S("lav-043", "Diritti sindacali", 4, "Entro quanti giorni il giudice decide sul ricorso per condotta antisindacale (art. 28)?",
  "Nei due giorni successivi, sentite le parti", ["Entro sei mesi", "Entro trenta giorni", "Entro un anno"],
  "Art. 28: il decreto motivato è immediatamente esecutivo.",
  "art. 28", "nei due giorni successivi, convocate le parti")

S("lav-044", "Statuto dei lavoratori", 3, "Il lavoratore eletto al Parlamento può essere collocato in aspettativa?",
  "Sì, aspettativa non retribuita per tutta la durata del mandato, su richiesta", ["No, deve dimettersi", "Sì, con stipendio pieno", "Solo per un anno"],
  "Art. 31 L. 300/1970, applicabile anche ai dipendenti pubblici.",
  "art. 31", "possono, a richiesta, essere collocati in aspettativa non retribuita, per tutta la durata del loro")

S("lav-045", "Statuto dei lavoratori", 3, "Chi gestisce le attività culturali, ricreative e assistenziali promosse in azienda?",
  "Organismi formati a maggioranza da rappresentanti dei lavoratori", ["Solo il datore di lavoro", "Il comune", "L'INPS"],
  "Art. 11 L. 300/1970.",
  "art. 11", "sono gestite da organismi formati a maggioranza dai rappresentanti dei lavoratori")


# --- Blocco 3: D.Lgs. 81/2015 (contratti di lavoro) ---
def C(id, arg, liv, testo, giusta, sbagliate, spieg, art, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, f"D.Lgs. 81/2015, {art}", D81_15, frase)

C("lav-046", "Contratti di lavoro", 4, "A quali collaborazioni si applica la disciplina del lavoro subordinato secondo l'art. 2 del D.Lgs. 81/2015?",
  "A quelle prevalentemente personali, continuative e organizzate dal committente, anche tramite piattaforme digitali", ["A tutte le partite IVA", "Solo ai contratti di appalto", "A nessuna collaborazione"],
  "Art. 2, c. 1 (collaborazioni etero-organizzate).",
  "art. 2", "le cui modalità di esecuzione sono organizzate dal committente")

C("lav-047", "Mansioni", 4, "Secondo l'art. 2103 c.c., come riscritto dal D.Lgs. 81/2015, a quali mansioni può essere adibito il lavoratore?",
  "A quelle di assunzione, a quelle dell'inquadramento superiore acquisito o a mansioni dello stesso livello e categoria legale", ["A qualsiasi mansione, anche inferiore, senza limiti", "Solo a quelle indicate nel contratto iniziale", "Solo a mansioni superiori"],
  "Art. 3 D.Lgs. 81/2015, che ha sostituito l'art. 2103 c.c.",
  "art. 3", "a mansioni riconducibili allo stesso livello e categoria legale di inquadramento")

C("lav-048", "Part-time", 2, "In quale forma va stipulato il contratto di lavoro a tempo parziale?",
  "Per iscritto, ai fini della prova", ["Anche oralmente, senza prova", "Per atto notarile", "Con autorizzazione del sindacato"],
  "Art. 5, c. 1.",
  "art. 5", "Il contratto di lavoro a tempo parziale è stipulato in forma scritta ai fini della prova")

C("lav-049", "Part-time", 3, "Cosa deve indicare il contratto part-time?",
  "La durata della prestazione e la collocazione temporale dell'orario (giorno, settimana, mese, anno)", ["Solo la retribuzione annua", "Solo il nome del responsabile", "Il numero di ferie"],
  "Art. 5, c. 2.",
  "art. 5", "puntuale indicazione della durata della prestazione lavorativa e della collocazione temporale dell'orario")

C("lav-050", "Part-time", 3, "Come si chiamano le prestazioni svolte dal lavoratore part-time oltre l'orario concordato ma entro l'orario normale?",
  "Lavoro supplementare", ["Lavoro straordinario", "Lavoro intermittente", "Lavoro accessorio"],
  "Art. 6, c. 1.",
  "art. 6", "lo svolgimento di prestazioni supplementari")

C("lav-051", "Part-time", 3, "Il rifiuto del lavoratore di trasformare il rapporto da tempo pieno a part-time costituisce giustificato motivo di licenziamento?",
  "No", ["Sì, sempre", "Solo nelle aziende con più di 15 dipendenti", "Solo nel settore pubblico"],
  "Art. 8, c. 1.",
  "art. 8", "non costituisce giustificato motivo di licenziamento")

C("lav-052", "Part-time", 4, "Quali lavoratori hanno diritto alla trasformazione del rapporto in part-time ai sensi dell'art. 8, c. 3?",
  "Quelli affetti da patologie oncologiche o gravi patologie cronico-degenerative ingravescenti", ["Tutti i lavoratori over 50", "Solo i dirigenti", "Solo i neoassunti"],
  "Art. 8, c. 3: vale sia nel settore pubblico sia privato.",
  "art. 8", "affetti da patologie oncologiche")

C("lav-053", "Lavoro intermittente", 3, "Che cos'è il contratto di lavoro intermittente?",
  "Il contratto con cui il lavoratore si mette a disposizione di un datore che ne usa la prestazione in modo discontinuo", ["Un contratto di appalto", "Un tirocinio formativo", "Un contratto di lavoro autonomo occasionale"],
  "Art. 13, c. 1.",
  "art. 13", "si pone a disposizione di un datore di lavoro che ne può utilizzare la prestazione lavorativa in modo discontinuo")

C("lav-054", "Lavoro intermittente", 3, "È ammesso il lavoro intermittente per sostituire lavoratori in sciopero?",
  "No, è vietato", ["Sì, sempre", "Solo per un giorno", "Solo nel settore pubblico"],
  "Art. 14, c. 1, lett. a).",
  "art. 14", "per la sostituzione di lavoratori che esercitano il diritto di sciopero")

C("lav-055", "Contratti a termine", 3, "Come possono essere prorogati e rinnovati i contratti a termine nei primi dodici mesi?",
  "Liberamente; dopo i dodici mesi solo in presenza delle condizioni dell'art. 19", ["Mai", "Solo con autorizzazione dell'Ispettorato", "Solo con il consenso del sindacato"],
  "Art. 21, c. 01; in caso di violazione il contratto si trasforma a tempo indeterminato.",
  "art. 21", "Il contratto può essere prorogato e rinnovato liberamente nei primi dodici mesi")

C("lav-056", "Contratti a termine", 4, "Qual è il limite legale (salvo diversa previsione dei contratti collettivi) dei contratti a termine rispetto ai lavoratori a tempo indeterminato?",
  "Il 20 per cento", ["Il 50 per cento", "Il 10 per cento", "Nessun limite"],
  "Art. 23, c. 1.",
  "art. 23", "in misura superiore al 20 per cento del numero dei lavoratori a tempo indeterminato")

C("lav-057", "Contratti a termine", 4, "Dopo quanti mesi di lavoro a termine nella stessa azienda matura il diritto di precedenza nelle assunzioni a tempo indeterminato?",
  "Più di sei mesi (diritto valido nei dodici mesi successivi)", ["Un mese", "Due anni", "Tre anni"],
  "Art. 24, c. 1.",
  "art. 24", "ha prestato attività lavorativa per un periodo superiore a sei mesi ha diritto di precedenza")

C("lav-058", "Contratti a termine", 4, "Entro quanto va impugnato un contratto a tempo determinato?",
  "Entro centottanta giorni dalla cessazione del singolo contratto", ["Entro sessanta giorni dall'assunzione", "Entro cinque anni", "Entro dieci giorni"],
  "Art. 28, c. 1.",
  "art. 28", "entro centottanta giorni dalla cessazione del singolo contratto")

C("lav-059", "Somministrazione", 3, "Nel contratto di somministrazione, sotto la direzione di chi lavora il lavoratore durante la missione?",
  "Dell'utilizzatore, pur essendo dipendente dell'agenzia", ["Dell'agenzia di somministrazione", "Del centro per l'impiego", "Di nessuno"],
  "Art. 30 D.Lgs. 81/2015.",
  "art. 30", "nell'interesse e sotto la direzione e il controllo dell'utilizzatore")

C("lav-060", "Somministrazione", 4, "Salvo diversa previsione dei contratti collettivi, qual è il limite dei somministrati a tempo indeterminato presso l'utilizzatore?",
  "Il 20 per cento dei lavoratori a tempo indeterminato", ["Il 5 per cento", "Il 50 per cento", "Nessun limite"],
  "Art. 31, c. 1.",
  "art. 31", "non può eccedere il 20 per cento del numero dei lavoratori a tempo indeterminato")

C("lav-061", "Apprendistato", 2, "Che tipo di contratto è l'apprendistato?",
  "Un contratto di lavoro a tempo indeterminato finalizzato alla formazione e all'occupazione dei giovani", ["Un tirocinio non retribuito", "Un contratto a termine di sei mesi", "Una borsa di studio"],
  "Art. 41, c. 1.",
  "art. 41", "L'apprendistato è un contratto di lavoro a tempo indeterminato finalizzato alla formazione")

C("lav-062", "Apprendistato", 3, "Quale di queste NON è una tipologia di apprendistato prevista dal D.Lgs. 81/2015?",
  "Apprendistato di reinserimento per pensionati", ["Apprendistato professionalizzante", "Apprendistato di alta formazione e ricerca", "Apprendistato per la qualifica e il diploma professionale"],
  "Art. 41, c. 2.",
  "art. 41", "b) apprendistato professionalizzante; c) apprendistato di alta formazione e ricerca")

C("lav-063", "Apprendistato", 3, "Quale documento deve contenere, in forma sintetica, il contratto di apprendistato?",
  "Il piano formativo individuale", ["Il DVR", "Il curriculum del datore", "Il codice disciplinare"],
  "Art. 42, c. 1: il contratto è in forma scritta ai fini della prova.",
  "art. 42", "contiene, in forma sintetica, il piano formativo individuale")

C("lav-064", "Apprendistato", 3, "Qual è l'età per l'apprendistato professionalizzante?",
  "Tra i 18 e i 29 anni", ["Tra i 14 e i 16 anni", "Tra i 30 e i 40 anni", "Nessun limite"],
  "Art. 44, c. 1 (dai 17 anni con qualifica professionale).",
  "art. 44", "i soggetti di età compresa tra i 18 e i 29 anni")


# --- Blocco 4: D.Lgs. 81/2008 (salute e sicurezza sul lavoro) ---
def T(id, arg, liv, testo, giusta, sbagliate, spieg, art, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, f"D.Lgs. 81/2008, {art}", D81_08, frase)

T("lav-065", "Sicurezza sul lavoro", 2, "Chi è «lavoratore» ai fini del D.Lgs. 81/2008?",
  "Chi svolge un'attività nell'organizzazione di un datore pubblico o privato, indipendentemente dal contratto, anche senza retribuzione", ["Solo chi ha un contratto a tempo indeterminato", "Solo il dipendente privato", "Solo chi lavora più di 20 ore a settimana"],
  "Art. 2, c. 1, lett. a); sono esclusi gli addetti ai servizi domestici e familiari.",
  "art. 2", "indipendentemente dalla tipologia contrattuale, svolge un'attività lavorativa")

T("lav-066", "Sicurezza sul lavoro", 3, "Chi è il «preposto» secondo il D.Lgs. 81/2008?",
  "Chi sovrintende all'attività lavorativa e garantisce l'attuazione delle direttive, controllandone la corretta esecuzione", ["Il medico competente", "Il rappresentante sindacale", "Il datore di lavoro"],
  "Art. 2, c. 1, lett. e).",
  "art. 2", "sovrintende alla attività lavorativa e garantisce l'attuazione delle direttive ricevute")

T("lav-067", "Sicurezza sul lavoro", 3, "Come definisce il D.Lgs. 81/2008 il «dirigente»?",
  "Chi attua le direttive del datore di lavoro organizzando l'attività lavorativa e vigilando su di essa", ["Chi elegge il RLS", "Chi effettua la sorveglianza sanitaria", "Chi certifica i DPI"],
  "Art. 2, c. 1, lett. d).",
  "art. 2", "attua le direttive del datore di lavoro organizzando l'attività lavorativa e vigilando su di essa")

T("lav-068", "Sicurezza sul lavoro", 3, "Qual è la differenza tra «pericolo» e «rischio»?",
  "Il pericolo è la proprietà intrinseca di un fattore di causare danni; il rischio è la probabilità che il danno si verifichi", ["Sono sinonimi", "Il rischio è sempre più grave del pericolo", "Il pericolo riguarda solo gli incendi"],
  "Art. 2, c. 1, lett. r) e s).",
  "art. 2", "\"pericolo\": proprietà o qualità intrinseca di un determinato fattore avente il potenziale di causare danni")

T("lav-069", "Sicurezza sul lavoro", 3, "Da chi è designato e a chi risponde il responsabile del servizio di prevenzione e protezione (RSPP)?",
  "È designato dal datore di lavoro, a cui risponde", ["È eletto dai lavoratori", "È nominato dall'ASL", "È scelto dal sindacato"],
  "Art. 2, c. 1, lett. f); la sua designazione è indelegabile (art. 17).",
  "art. 2", "designata dal datore di lavoro, a cui risponde")

T("lav-070", "Sicurezza sul lavoro", 2, "Cosa distingue l'«addestramento» dalla «formazione» nel D.Lgs. 81/2008?",
  "L'addestramento insegna l'uso corretto di attrezzature, macchine, dispositivi e procedure", ["L'addestramento è solo teorico", "Non c'è differenza", "L'addestramento riguarda solo i dirigenti"],
  "Art. 2, c. 1, lett. aa)-cc).",
  "art. 2", "\"addestramento\": complesso delle attività dirette a fare apprendere ai lavoratori l'uso corretto di attrezzature")

T("lav-071", "Sicurezza sul lavoro", 3, "Come definisce la «salute» il D.Lgs. 81/2008?",
  "Stato di completo benessere fisico, mentale e sociale, non solo assenza di malattia", ["Assenza di infortuni nell'ultimo anno", "Idoneità alla mansione certificata", "Assenza di malattie croniche"],
  "Art. 2, c. 1, lett. o), che riprende la definizione dell'OMS.",
  "art. 2", "\"salute\": stato di completo benessere fisico, mentale e sociale")

T("lav-072", "Sicurezza sul lavoro", 2, "Chi deve nominare il medico competente, nei casi previsti?",
  "Il datore di lavoro (e i dirigenti secondo le loro attribuzioni)", ["Il RLS", "L'INAIL", "Il lavoratore"],
  "Art. 18, c. 1, lett. a).",
  "art. 18", "nominare il medico competente per l'effettuazione della sorveglianza sanitaria")

T("lav-073", "Sicurezza sul lavoro", 2, "Quale obbligo ha ogni lavoratore secondo l'art. 20 del D.Lgs. 81/2008?",
  "Prendersi cura della propria salute e sicurezza e di quella delle altre persone presenti sul luogo di lavoro", ["Redigere il DVR", "Nominare l'RSPP", "Acquistare i propri DPI"],
  "Art. 20, c. 1.",
  "art. 20", "Ogni lavoratore deve prendersi cura della propria salute e sicurezza")

T("lav-074", "Sicurezza sul lavoro", 3, "La valutazione dei rischi deve considerare anche lo stress lavoro-correlato?",
  "Sì, deve riguardare tutti i rischi, compresi quelli collegati allo stress lavoro-correlato", ["No, solo i rischi fisici", "Solo nelle aziende con più di 100 dipendenti", "Solo su richiesta del sindacato"],
  "Art. 28, c. 1.",
  "art. 28", "quelli collegati allo stress lavoro-correlato")

T("lav-075", "Sicurezza sul lavoro", 3, "Con chi collabora il datore di lavoro per effettuare la valutazione dei rischi?",
  "Con l'RSPP e il medico competente, previa consultazione del RLS", ["Con il sindaco", "Con i vigili del fuoco obbligatoriamente", "Da solo, senza consultare nessuno"],
  "Art. 29, c. 1-2.",
  "art. 29", "in collaborazione con il responsabile del servizio di prevenzione e protezione e il medico competente")

T("lav-076", "Sicurezza sul lavoro", 4, "Quando la valutazione dei rischi va immediatamente rielaborata?",
  "In occasione di modifiche significative del processo produttivo o dell'organizzazione del lavoro (e dopo infortuni significativi)", ["Ogni dieci anni", "Mai", "Solo su ordine del giudice"],
  "Art. 29, c. 3.",
  "art. 29", "La valutazione dei rischi deve essere immediatamente rielaborata")

T("lav-077", "Sicurezza sul lavoro", 4, "Quale titolo di studio minimo serve per svolgere le funzioni di RSPP o addetto al servizio di prevenzione?",
  "Diploma di istruzione secondaria superiore, più un attestato di frequenza a corsi specifici", ["Laurea in medicina", "Licenza media", "Nessuno"],
  "Art. 32, c. 2.",
  "art. 32", "un titolo di studio non inferiore al diploma di istruzione secondaria superiore")

T("lav-078", "Sicurezza sul lavoro", 4, "Nelle aziende con più di 15 lavoratori, quante volte all'anno almeno si tiene la riunione periodica sulla sicurezza?",
  "Almeno una volta all'anno", ["Ogni mese", "Ogni cinque anni", "Mai, è facoltativa"],
  "Art. 35, c. 1: partecipano datore, RSPP, medico competente e RLS.",
  "art. 35", "indice almeno una volta all'anno una riunione")

T("lav-079", "Sicurezza sul lavoro", 2, "Su cosa deve ricevere informazione ogni lavoratore (art. 36)?",
  "Su rischi, procedure di primo soccorso, antincendio ed evacuazione, e sui nominativi degli incaricati", ["Sul bilancio dell'azienda", "Sugli stipendi dei colleghi", "Sui contratti con i fornitori"],
  "Art. 36, c. 1.",
  "art. 36", "sulle procedure che riguardano il primo soccorso, la lotta antincendio, l'evacuazione dei luoghi di lavoro")

T("lav-080", "Sicurezza sul lavoro", 3, "Chi effettua la sorveglianza sanitaria?",
  "Il medico competente", ["Il medico di base del lavoratore", "L'RSPP", "Il preposto"],
  "Art. 41: comprende visita preventiva, periodica e altre visite.",
  "art. 41", "La sorveglianza sanitaria è effettuata dal medico competente")

T("lav-081", "Sicurezza sul lavoro", 4, "A cosa serve la visita medica preventiva nella sorveglianza sanitaria?",
  "A constatare l'assenza di controindicazioni e valutare l'idoneità alla mansione specifica", ["A stabilire lo stipendio", "A verificare le assenze per malattia", "A scegliere il contratto"],
  "Art. 41, c. 2, lett. a); può avvenire anche in fase preassuntiva.",
  "art. 41", "visita medica preventiva, anche in fase preassuntiva")

T("lav-082", "Sicurezza sul lavoro", 3, "Un lavoratore che si allontana dal posto di lavoro per un pericolo grave, immediato e inevitabile può subire conseguenze?",
  "No, non può subire pregiudizio e va protetto da conseguenze dannose", ["Sì, è abbandono del posto", "Sì, una multa", "Solo se non avvisa il preposto per iscritto"],
  "Art. 44, c. 1.",
  "art. 44", "non può subire pregiudizio alcuno e deve essere protetto da qualsiasi conseguenza dannosa")

T("lav-083", "Sicurezza sul lavoro", 3, "In aziende fino a 15 lavoratori, come si individua di norma il RLS?",
  "È eletto direttamente dai lavoratori al loro interno o individuato a livello territoriale/di comparto", ["È nominato dal datore", "È designato dal medico competente", "Non è previsto"],
  "Art. 47, c. 3.",
  "art. 47", "il rappresentante dei lavoratori per la sicurezza è di norma eletto direttamente dai lavoratori al loro interno")

T("lav-084", "Sicurezza sul lavoro", 3, "Quale di queste è un'attribuzione del RLS?",
  "Essere consultato preventivamente sulla valutazione dei rischi", ["Redigere il DVR al posto del datore", "Effettuare le visite mediche", "Firmare i contratti di lavoro"],
  "Art. 50, c. 1, lett. b).",
  "art. 50", "è consultato preventivamente e tempestivamente in ordine alla valutazione dei rischi")

T("lav-085", "Sicurezza sul lavoro", 2, "Cos'è un DPI (dispositivo di protezione individuale)?",
  "Un'attrezzatura indossata dal lavoratore per proteggerlo da rischi per la sicurezza o la salute", ["Un documento di valutazione", "Un piano di evacuazione", "Un estintore fisso"],
  "Art. 74 D.Lgs. 81/2008.",
  "art. 74", "qualsiasi attrezzatura destinata ad essere indossata e tenuta dal lavoratore")

T("lav-086", "Sicurezza sul lavoro", 4, "Per quali rischi il datore di lavoro deve ricorrere ai DPI?",
  "Per i rischi che non possono essere evitati con altri mezzi", ["Per tutti i rischi, prima di ogni altra misura", "Solo per il rischio incendio", "Solo su richiesta del lavoratore"],
  "Art. 77, c. 1, lett. a): le misure collettive hanno priorità.",
  "art. 77", "effettua l'analisi e la valutazione dei rischi che non possono essere evitati con altri mezzi")

T("lav-087", "Sicurezza sul lavoro", 3, "Cos'è un videoterminale secondo il D.Lgs. 81/2008?",
  "Uno schermo alfanumerico o grafico, qualunque sia il procedimento di visualizzazione", ["Solo il computer portatile", "Solo la tastiera", "Un telefono fisso"],
  "Art. 173, c. 1, lett. a).",
  "art. 173", "videoterminale: uno schermo alfanumerico o grafico")

T("lav-088", "Sicurezza sul lavoro", 4, "Quale compito ha il preposto quando rileva comportamenti non conformi dei lavoratori?",
  "Sovrintendere e vigilare, intervenendo per modificarli", ["Nessuno, deve solo segnalarli all'INAIL", "Licenziare subito il lavoratore", "Sospendere la produzione dell'azienda"],
  "Art. 19, c. 1, lett. a), come riscritto nel 2021.",
  "art. 19", "sovrintendere e vigilare sull'osservanza da parte dei singoli lavoratori")


# --- Blocco 5: previdenza e relazioni sindacali (voci Wikipedia, CC BY-SA 4.0) ---
PREV = "Wikipedia_Previdenza-sociale.txt"
INPS = "Wikipedia_Istituto-Nazionale-della-Previdenza-Sociale.txt"
FORN = "Wikipedia_Riforma-delle-pensioni-Fornero.txt"
TFR = "Wikipedia_Trattamento-di-fine-rapporto.txt"
ARAN = "Wikipedia_Agenzia-per-la-rappresentanza-negoziale-delle-pubbliche-amministrazioni.txt"
CCNL = "Wikipedia_Contratto-collettivo-nazionale-di-lavoro.txt"
SCIO = "Wikipedia_Sciopero.txt"
W = lambda voce: f"Wikipedia, «{voce}» (CC BY-SA 4.0)"

D("lav-089", "Previdenza", 2, "Qual è il fine della previdenza sociale?",
  "Tutelare il lavoratore dai rischi derivanti dalla menomazione o perdita della capacità lavorativa per eventi predeterminati", ["Finanziare le imprese in crisi", "Riscuotere le imposte sul reddito", "Gestire le scuole pubbliche"],
  "Voce «Previdenza sociale».",
  W("Previdenza sociale"), PREV, "ha come fine la tutela del lavoratore dai rischi conseguenti alla menomazione o alla perdita della sua capacità lavorativa")

D("lav-090", "Previdenza", 3, "Quale Paese introdusse per primo le assicurazioni sociali obbligatorie contro malattie, infortuni e vecchiaia (1883-1889)?",
  "La Germania di Bismarck", ["Il Regno Unito", "La Francia", "L'Italia"],
  "Voce «Previdenza sociale».",
  W("Previdenza sociale"), PREV, "La Germania la introdusse nel 1883 contro le malattie")

D("lav-091", "Previdenza", 3, "Chi elaborò nel 1942 il piano di sicurezza sociale «dalla culla alla tomba»?",
  "William Beveridge", ["Otto von Bismarck", "Franklin D. Roosevelt", "John Maynard Keynes"],
  "Voce «Previdenza sociale».",
  W("Previdenza sociale"), PREV, "William Beveridge pubblicò il rapporto Social Insurance and Allied Services")

D("lav-092", "Previdenza", 3, "In che anno l'Italia introdusse l'assicurazione obbligatoria contro gli infortuni sul lavoro?",
  "Nel 1898", ["Nel 1948", "Nel 1861", "Nel 1970"],
  "Nello stesso anno nacque la Cassa nazionale di previdenza per l'invalidità e la vecchiaia degli operai (oggi INPS).",
  W("Previdenza sociale"), PREV, "venne introdotta l'assicurazione obbligatoria contro gli infortuni")

D("lav-093", "Previdenza", 4, "Con quale provvedimento del 1919 l'assicurazione per invalidità e vecchiaia divenne obbligatoria in Italia?",
  "Il D.l.lgt. 21 aprile 1919, n. 603", ["La legge 20 maggio 1970, n. 300", "Il D.L. 201/2011", "La legge 335/1995"],
  "Voce «Previdenza sociale».",
  W("Previdenza sociale"), PREV, "D.l.lgt. 21 aprile 1919, n. 603")

D("lav-094", "Previdenza", 3, "Quale legge del 1978 istituì il Servizio sanitario nazionale?",
  "La legge 23 dicembre 1978, n. 833", ["La legge 300/1970", "La legge 241/1990", "La legge 335/1995"],
  "Voce «Previdenza sociale».",
  W("Previdenza sociale"), PREV, "La legge 23 dicembre 1978, n. 833")

D("lav-095", "Previdenza", 3, "Cosa distingue l'assistenza sociale dalla previdenza in senso stretto?",
  "L'assistenza ha vocazione universalistica ed è finanziata integralmente dallo Stato; la previdenza ha base mutualistica nel mondo del lavoro", ["Non c'è alcuna differenza", "La previdenza è finanziata solo dallo Stato", "L'assistenza riguarda solo i lavoratori autonomi"],
  "Voce «Previdenza sociale».",
  W("Previdenza sociale"), PREV, "si contrappone l'assistenza sociale, a vocazione universalistica e solidaristica")

D("lav-096", "Previdenza", 2, "Quale ente gestisce la tutela contro infortuni sul lavoro e malattie professionali?",
  "L'INAIL", ["L'INPS", "L'ISTAT", "L'ARAN"],
  "Voce «Previdenza sociale».",
  W("Previdenza sociale"), PREV, "incentrato sull'INAIL")

D("lav-097", "Previdenza", 1, "Qual è il principale ente previdenziale del sistema pensionistico pubblico italiano?",
  "L'INPS", ["L'INAIL", "La Banca d'Italia", "La Cassa depositi e prestiti"],
  "Voce «Istituto Nazionale della Previdenza Sociale».",
  W("Istituto Nazionale della Previdenza Sociale"), INPS, "è il principale ente previdenziale del sistema pensionistico pubblico italiano")

D("lav-098", "Previdenza", 2, "Sotto la vigilanza di quale Ministero opera l'INPS?",
  "Ministero del lavoro e delle politiche sociali", ["Ministero dell'interno", "Ministero della salute", "Ministero dell'istruzione"],
  "Voce «Istituto Nazionale della Previdenza Sociale».",
  W("Istituto Nazionale della Previdenza Sociale"), INPS, "è sottoposto alla vigilanza del Ministero del lavoro e delle politiche sociali")

D("lav-099", "Previdenza", 3, "Quale banca dati gestisce l'INPS per l'accesso alle prestazioni sociali agevolate?",
  "Quella dell'ISEE (indicatore della situazione economica equivalente)", ["Il casellario giudiziale", "L'anagrafe tributaria", "Il registro delle imprese"],
  "Voce «Istituto Nazionale della Previdenza Sociale».",
  W("Istituto Nazionale della Previdenza Sociale"), INPS, "la gestione della banca dati relativa al calcolo dell'ISEE")

D("lav-100", "Previdenza", 4, "In che anno l'ente assunse la denominazione di Istituto nazionale della previdenza sociale?",
  "Nel 1943", ["Nel 1898", "Nel 1970", "Nel 1995"],
  "In precedenza era l'Istituto nazionale fascista della previdenza sociale (INFPS).",
  W("Istituto Nazionale della Previdenza Sociale"), INPS, "Nel 1943 con l'articolo 3 del Regio Decreto Legge 2 agosto 1943 n.704")

D("lav-101", "Previdenza", 4, "Quale prestazione e quale ammortizzatore nacquero nel 1968?",
  "La pensione sociale e la Cassa integrazione guadagni straordinaria (CIGS)", ["La NASpI e il reddito di cittadinanza", "Il TFR e la quattordicesima", "L'ISEE e l'assegno unico"],
  "Voce «Istituto Nazionale della Previdenza Sociale».",
  W("Istituto Nazionale della Previdenza Sociale"), INPS, "Nel 1968 nasce la pensione sociale e la Cassa Integrazione Guadagni Straordinaria")

D("lav-102", "Previdenza", 4, "Quale legge del 1989 ristrutturò l'INPS separando finanziariamente assistenza e previdenza?",
  "La legge 9 marzo 1989, n. 88", ["La legge 335/1995", "La legge 92/2012", "La legge 146/1990"],
  "Voce «Istituto Nazionale della Previdenza Sociale».",
  W("Istituto Nazionale della Previdenza Sociale"), INPS, "legge 9 marzo 1989, n. 88")

D("lav-103", "Pensioni", 3, "Con quale provvedimento è stata introdotta la riforma Fornero delle pensioni?",
  "Con l'art. 24 del D.L. 6 dicembre 2011, n. 201 («Salva Italia»)", ["Con la L. 335/1995 (riforma Dini)", "Con il D.Lgs. 165/2001", "Con la L. 300/1970"],
  "Voce «Riforma delle pensioni Fornero».",
  W("Riforma delle pensioni Fornero"), FORN, "l'articolo 24 del decreto legge 6 dicembre 2011, n. 201")

D("lav-104", "Pensioni", 3, "Quale riforma del 1995 aveva introdotto il metodo contributivo?",
  "La riforma Dini", ["La riforma Fornero", "La riforma Sacconi", "La riforma Brunetta"],
  "Voce «Riforma delle pensioni Fornero»: la Fornero estese il contributivo pro-rata dal 2012.",
  W("Riforma delle pensioni Fornero"), FORN, "riforma Dini del 1995")

D("lav-105", "Pensioni", 4, "Cosa fece la riforma Fornero con le pensioni di anzianità?",
  "Le ridenominò «anticipate» e abolì il sistema delle quote", ["Le raddoppiò", "Le rese tutte calcolate col retributivo", "Le trasferì all'INAIL"],
  "Voce «Riforma delle pensioni Fornero».",
  W("Riforma delle pensioni Fornero"), FORN, "ridenominate “anticipate” e abolizione delle cosiddette quote")

D("lav-106", "Pensioni", 4, "Da quando la riforma Fornero ha esteso il metodo contributivo pro-rata a chi ne era escluso?",
  "Dal 1° gennaio 2012", ["Dal 1° gennaio 1996", "Dal 1° gennaio 2020", "Dal 1° gennaio 2008"],
  "Voce «Riforma delle pensioni Fornero».",
  W("Riforma delle pensioni Fornero"), FORN, "a decorrere dall'1.1.2012")

D("lav-107", "Pensioni", 3, "Quale articolo della Costituzione riguarda i rapporti tra lavoratori in stato di bisogno ed enti previdenziali?",
  "L'art. 38", ["L'art. 21", "L'art. 81", "L'art. 117"],
  "Voce «Riforma delle pensioni Fornero».",
  W("Riforma delle pensioni Fornero"), FORN, "art. 38 della Costituzione Italiana")

D("lav-108", "TFR", 2, "Che cos'è il TFR?",
  "Una porzione di retribuzione differita, pagata dal datore alla cessazione del rapporto", ["Una pensione integrativa pubblica", "Un'imposta sul lavoro", "Un premio di produzione annuale"],
  "Voce «Trattamento di fine rapporto».",
  W("Trattamento di fine rapporto"), TFR, "è in Italia una porzione di retribuzione al lavoratore subordinato differita alla cessazione del rapporto di lavoro")

D("lav-109", "TFR", 3, "Quale legge ha sostituito l'indennità di anzianità con il TFR, dal 1° giugno 1982?",
  "La legge 29 maggio 1982, n. 297", ["La legge 300/1970", "Il D.Lgs. 252/2005", "La legge 92/2012"],
  "Voce «Trattamento di fine rapporto».",
  W("Trattamento di fine rapporto"), TFR, "La legge n. 297 del 29 maggio 1982")

D("lav-110", "TFR", 4, "Come si calcola la quota annua di TFR secondo l'art. 2120 c.c.?",
  "Retribuzione annua divisa per 13,5", ["Retribuzione mensile per 12", "Il 10% dello stipendio", "Retribuzione annua divisa per 10"],
  "Voce «Trattamento di fine rapporto».",
  W("Trattamento di fine rapporto"), TFR, "divisa per 13,5")

D("lav-111", "TFR", 4, "Come si rivaluta il TFR ogni anno?",
  "Con un tasso dell'1,5% fisso più il 75% dell'aumento dell'indice ISTAT dei prezzi", ["Del 5% fisso", "In base al PIL", "Non si rivaluta"],
  "Voce «Trattamento di fine rapporto».",
  W("Trattamento di fine rapporto"), TFR, "dall'1,5% in misura fissa e dal 75% dell'aumento dell'indice dei prezzi al consumo")

D("lav-112", "TFR", 4, "Quale fondo garantisce il TFR ai lavoratori di imprese insolventi o fallite?",
  "Il Fondo di garanzia gestito dall'INPS", ["Il Fondo di riserva dello Stato", "L'INAIL", "La Cassa depositi e prestiti"],
  "Istituito dall'art. 2 della L. 297/1982.",
  W("Trattamento di fine rapporto"), TFR, "istituisce un Fondo di Garanzia nazionale")

D("lav-113", "TFR", 5, "Quale decreto del 2005 ha regolato la destinazione del TFR ai fondi pensione con il meccanismo del silenzio-assenso?",
  "Il D.Lgs. 5 dicembre 2005, n. 252", ["Il D.Lgs. 81/2008", "La L. 297/1982", "Il D.L. 201/2011"],
  "Voce «Trattamento di fine rapporto».",
  W("Trattamento di fine rapporto"), TFR, "decreto legislativo 5 dicembre 2005 n. 252")

D("lav-114", "TFR", 4, "Quali dipendenti pubblici contrattualizzati hanno il TFR invece del trattamento di fine servizio?",
  "Quelli assunti dopo il 31 dicembre 2000", ["Tutti quelli assunti prima del 1990", "Solo i dirigenti", "Nessuno"],
  "Voce «Trattamento di fine rapporto».",
  W("Trattamento di fine rapporto"), TFR, "assunti dopo la data del 31/12/2000")

D("lav-115", "Contrattazione collettiva", 2, "Chi rappresenta legalmente le pubbliche amministrazioni nella contrattazione collettiva nazionale?",
  "L'ARAN", ["Il CNEL", "L'INPS", "La Corte dei conti"],
  "Voce «Agenzia per la rappresentanza negoziale delle pubbliche amministrazioni».",
  W("Agenzia per la rappresentanza negoziale delle pubbliche amministrazioni"), ARAN, "rappresenta legalmente le pubbliche amministrazioni italiane nella contrattazione collettiva nazionale")

D("lav-116", "Contrattazione collettiva", 3, "Da quale decreto fu istituita l'ARAN?",
  "Dal D.Lgs. 3 febbraio 1993, n. 29", ["Dal D.Lgs. 165/2001", "Dalla L. 300/1970", "Dal D.Lgs. 150/2009"],
  "Poi confermata dai D.Lgs. 165/2001 e 150/2009.",
  W("Agenzia per la rappresentanza negoziale delle pubbliche amministrazioni"), ARAN, "Istituita dall'art. 50 del d.lgs. 3 febbraio 1993, n. 29")

D("lav-117", "Contrattazione collettiva", 4, "A quali atti si attiene l'ARAN nello svolgere la contrattazione?",
  "Agli atti di indirizzo dei Comitati di settore", ["Alle sentenze del TAR", "Alle circolari INPS", "Alle direttive della Banca d'Italia"],
  "Voce «Agenzia per la rappresentanza negoziale delle pubbliche amministrazioni».",
  W("Agenzia per la rappresentanza negoziale delle pubbliche amministrazioni"), ARAN, "si attiene agli atti di indirizzo dei Comitati di settore")

D("lav-118", "Contrattazione collettiva", 3, "Dove sono raccolti e conservati i contratti collettivi nazionali?",
  "Nell'archivio nazionale del CNEL", ["Presso la Corte costituzionale", "Presso le prefetture", "Presso l'Agenzia delle entrate"],
  "Voce «Contratto collettivo nazionale di lavoro».",
  W("Contratto collettivo nazionale di lavoro"), CCNL, "archivio nazionale del Consiglio Nazionale dell'Economia e del Lavoro")

D("lav-119", "Contrattazione collettiva", 4, "Perché i CCNL non hanno efficacia erga omnes secondo il meccanismo dell'art. 39 Cost.?",
  "Perché il riconoscimento giuridico dei sindacati previsto dall'art. 39 non è mai stato attuato", ["Perché l'art. 39 è stato abrogato", "Perché li vieta la Costituzione", "Perché sono atti privati senza valore"],
  "Voce «Contratto collettivo nazionale di lavoro».",
  W("Contratto collettivo nazionale di lavoro"), CCNL, "era subordinata a una forma di riconoscimento giuridico che non è mai stata attivata")

D("lav-120", "Sciopero", 2, "Cos'è lo sciopero?",
  "L'astensione collettiva dal lavoro dei lavoratori subordinati per ottenere migliori condizioni", ["La sospensione del lavoro decisa dal datore", "Il licenziamento collettivo", "Un congedo per motivi familiari"],
  "Voce «Sciopero»; la sospensione decisa dal datore si chiama serrata.",
  W("Sciopero"), SCIO, "Lo sciopero è un'astensione collettiva dal lavoro")

D("lav-121", "Sciopero", 3, "Quale legge disciplina lo sciopero nei servizi pubblici essenziali?",
  "La legge 12 giugno 1990, n. 146", ["La legge 300/1970", "La legge 241/1990", "La legge 92/2012"],
  "Voce «Sciopero».",
  W("Sciopero"), SCIO, "legge n. 146 del 12 giugno 1990")

D("lav-122", "Sciopero", 3, "Come si chiama la sospensione dal lavoro disposta dal datore per fare pressione sui lavoratori?",
  "Serrata", ["Sciopero bianco", "Picchettaggio", "Precettazione"],
  "Voce «Sciopero».",
  W("Sciopero"), SCIO, "Diversa è la serrata")

D("lav-123", "Sciopero", 3, "Cos'è lo «sciopero bianco»?",
  "Applicare alla lettera i regolamenti causando rallentamenti, senza astenersi dal lavoro", ["Astenersi dal lavoro per un'intera settimana", "Scioperare indossando abiti bianchi", "Uno sciopero proclamato dal datore"],
  "Voce «Sciopero».",
  W("Sciopero"), SCIO, "Si parla di sciopero bianco quando i lavoratori anziché astenersi dal lavoro applicano alla lettera i regolamenti")

D("lav-124", "Sciopero", 4, "Qual è l'unico limite esterno che la giurisprudenza riconosce, in termini di danno, al diritto di sciopero?",
  "Il danno alla produttività (impossibilità di riprendere l'attività), non il semplice danno alla produzione", ["Qualsiasi perdita economica del datore", "Il fastidio per gli utenti", "La durata superiore a un giorno"],
  "Voce «Sciopero», che richiama Cass. n. 711/1980.",
  W("Sciopero"), SCIO, "il confine tra legittimità e illegittimità dello sciopero è stato individuato dalla giurisprudenza nel cosiddetto danno alla produttività")

D("lav-125", "Sciopero", 4, "Il mancato rispetto della precettazione costituisce giusta causa di licenziamento?",
  "No, anche se può integrare il reato di interruzione di pubblico servizio", ["Sì, sempre", "Sì, ma solo nel settore privato", "Sì, dopo tre violazioni"],
  "Voce «Sciopero».",
  W("Sciopero"), SCIO, "ma non è \"giusta causa\" di licenziamento")

D("lav-126", "Sciopero", 3, "Che effetto ha lo sciopero sul contratto di lavoro?",
  "Lo sospende temporaneamente: niente prestazione e niente retribuzione", ["Lo risolve", "Lo trasforma a tempo determinato", "Nessun effetto, la retribuzione è dovuta"],
  "Voce «Sciopero».",
  W("Sciopero"), SCIO, "Lo sciopero sospende temporaneamente il contratto di lavoro")


# --- Blocco 6: lavoro pubblico (D.Lgs. 165/2001) ---
D165 = "norma_DLgs165-2001_pubblico-impiego.txt"
def P(id, arg, liv, testo, giusta, sbagliate, spieg, art, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, f"D.Lgs. 165/2001, {art}", D165, frase)

P("lav-127", "Lavoro pubblico", 2, "Da quali norme sono disciplinati i rapporti di lavoro dei dipendenti pubblici «privatizzati»?",
  "Dal codice civile (libro V) e dalle leggi sul lavoro subordinato nell'impresa, salve le diverse disposizioni del D.Lgs. 165/2001", ["Solo dal codice penale", "Dal testo unico del 1957, in via esclusiva", "Dai regolamenti dei singoli ministeri"],
  "Art. 2, c. 2.",
  "art. 2", "sono disciplinati dalle disposizioni del capo I, titolo II, del libro V del codice civile")

P("lav-128", "Lavoro pubblico", 3, "Quale di queste categorie resta in regime di diritto pubblico (art. 3)?",
  "I magistrati, gli avvocati dello Stato, militari e forze di polizia, diplomatici e prefetti", ["Gli impiegati comunali", "Gli infermieri delle ASL", "I dipendenti dei ministeri non dirigenti"],
  "Art. 3, c. 1 D.Lgs. 165/2001.",
  "art. 3", "gli avvocati e procuratori dello Stato, il personale militare e delle Forze di polizia di Stato")

P("lav-129", "Lavoro pubblico", 3, "Con quale strumento le amministrazioni programmano le assunzioni?",
  "Il piano triennale dei fabbisogni di personale", ["Il DUP", "Il conto annuale", "Il piano della performance individuale"],
  "Art. 6, c. 2.",
  "art. 6", "adottano il piano triennale dei fabbisogni di personale")

P("lav-130", "Dirigenza", 3, "In quante fasce si articola la dirigenza statale?",
  "Due fasce", ["Tre fasce", "Una fascia unica", "Cinque fasce"],
  "Art. 15, c. 1 e art. 23.",
  "art. 15", "la dirigenza è articolata nelle due fasce dei ruoli")

P("lav-131", "Dirigenza", 4, "Come si accede alla qualifica di dirigente di seconda fascia nelle amministrazioni statali?",
  "Per corso-concorso della Scuola nazionale dell'amministrazione, per concorso delle singole amministrazioni o concorso unico", ["Per sola anzianità di servizio", "Per nomina politica diretta", "Per sorteggio tra i funzionari"],
  "Art. 28, c. 1 (con quota anche per sviluppo di carriera).",
  "art. 28", "selettivo di formazione bandito dalla Scuola nazionale dell'amministrazione")

P("lav-132", "Dirigenza", 3, "Quale di questi è un compito dei dirigenti (art. 17)?",
  "Dirigere, coordinare e controllare l'attività degli uffici e dei responsabili dei procedimenti", ["Approvare le leggi di spesa", "Nominare i ministri", "Giudicare i ricorsi gerarchici del TAR"],
  "Art. 17, c. 1, lett. d).",
  "art. 17", "dirigono, coordinano e controllano l'attività degli uffici che da essi dipendono")

P("lav-133", "Dirigenza", 4, "A chi formulano proposte ed esprimono pareri i dirigenti degli uffici dirigenziali generali?",
  "Al Ministro, nelle materie di sua competenza", ["Al Presidente della Repubblica", "Ai sindacati", "Al Parlamento"],
  "Art. 16, c. 1, lett. a).",
  "art. 16", "formulano proposte ed esprimono pareri al Ministro")

P("lav-134", "Dirigenza", 4, "Di cosa si tiene conto nel conferire un incarico dirigenziale (art. 19)?",
  "Attitudini e capacità professionali, risultati conseguiti e relativa valutazione, competenze organizzative", ["Solo dell'età anagrafica", "Dell'appartenenza politica", "Del luogo di residenza"],
  "Art. 19, c. 1.",
  "art. 19", "delle attitudini e delle capacità professionali del singolo dirigente")

P("lav-135", "Reclutamento", 3, "Quale di questi è un principio delle procedure di reclutamento (art. 35, c. 3)?",
  "Adeguata pubblicità della selezione e modalità che garantiscano l'imparzialità", ["Scelta discrezionale del sindaco", "Preferenza per i residenti del comune", "Segretezza delle prove"],
  "Art. 35, c. 3, lett. a).",
  "art. 35", "adeguata pubblicità della selezione e modalità di svolgimento che garantiscano l'imparzialità")

P("lav-136", "Reclutamento", 4, "Come devono essere composte le commissioni di concorso secondo l'art. 35, c. 3?",
  "Esclusivamente da esperti di provata competenza, senza componenti degli organi politici o rappresentanti sindacali", ["Da rappresentanti sindacali", "Dai consiglieri comunali", "Da qualsiasi dipendente volontario"],
  "Art. 35, c. 3, lett. e).",
  "art. 35", "composizione delle commissioni esclus")

P("lav-137", "Reclutamento", 3, "Con quali contratti le PA soddisfano il proprio fabbisogno ordinario di personale?",
  "Esclusivamente con contratti a tempo indeterminato, tramite le procedure dell'art. 35", ["Solo con contratti a termine", "Con collaborazioni coordinate", "Con stage gratuiti"],
  "Art. 36, c. 1; il lavoro flessibile è ammesso solo nei limiti previsti.",
  "art. 36", "le pubbliche amministrazioni assumono esclusivamente con contratti di lavoro subordinato a tempo indeterminato")

P("lav-138", "Contrattazione collettiva", 4, "Quali materie sono escluse dalla contrattazione collettiva nel pubblico impiego?",
  "L'organizzazione degli uffici, le prerogative dirigenziali e il conferimento degli incarichi dirigenziali", ["La retribuzione", "Le ferie", "I permessi sindacali"],
  "Art. 40, c. 1.",
  "art. 40", "Sono escluse dalla contrattazione collettiva le materie attinenti all'organizzazione degli uffici")

P("lav-139", "Contrattazione collettiva", 4, "Quale soglia di rappresentatività serve a un sindacato per essere ammesso alla contrattazione nazionale?",
  "Non inferiore al 5 per cento (media tra dato associativo ed elettorale)", ["Il 51 per cento", "L'1 per cento", "Il 20 per cento"],
  "Art. 43, c. 1.",
  "art. 43", "una rappresentatività non inferiore al 5 per cento")

P("lav-140", "Contrattazione collettiva", 4, "Chi emana gli indirizzi per la contrattazione collettiva nazionale prima di ogni rinnovo?",
  "I Comitati di settore", ["Il Parlamento", "La Corte dei conti", "Il CNEL"],
  "Art. 47, c. 1.",
  "art. 47", "Gli indirizzi per la contrattazione collettiva nazionale sono emanati dai Comitati di settore")

P("lav-141", "Contrattazione collettiva", 3, "Chi rappresenta legalmente le PA agli effetti della contrattazione collettiva nazionale secondo l'art. 46?",
  "L'ARAN", ["Il Ministro per la pubblica amministrazione", "Il Presidente del Consiglio", "La Funzione pubblica regionale"],
  "Art. 46, c. 1.",
  "art. 46", "Le pubbliche amministrazioni sono legalmente rappresentate dall'Agenzia per la rappresentanza negoziale")

P("lav-142", "Lavoro pubblico", 3, "Lo Statuto dei lavoratori si applica alle PA anche se hanno pochi dipendenti?",
  "Sì, a prescindere dal numero dei dipendenti", ["No, solo sopra 15 dipendenti", "No, mai", "Solo sopra 60 dipendenti"],
  "Art. 51, c. 2.",
  "art. 51", "si applica alle pubbliche amministrazioni a prescindere dal numero dei dipendenti")

P("lav-143", "Lavoro pubblico", 4, "Quale testo regola ancora le incompatibilità dei dipendenti pubblici, richiamato dall'art. 53?",
  "Il DPR 10 gennaio 1957, n. 3 (artt. 60 e seguenti)", ["Il codice civile del 1942", "La L. 300/1970", "Il D.Lgs. 81/2008"],
  "Art. 53, c. 1.",
  "art. 53", "dagli articoli 60 e seguenti del testo unico approvato con decreto del Presidente della Repubblica 10 gennaio 1957, n. 3")

P("lav-144", "Lavoro pubblico", 3, "Quali doveri costituzionali richiama l'art. 54 tra le finalità del codice di comportamento?",
  "Diligenza, lealtà, imparzialità e servizio esclusivo all'interesse pubblico", ["Obbedienza al partito di governo", "Riservatezza verso i cittadini", "Fedeltà al dirigente"],
  "Art. 54, c. 1.",
  "art. 54", "il rispetto dei doveri costituzionali di diligenza, lealtà, imparzialità e servizio esclusivo")

P("lav-145", "Procedimento disciplinare", 4, "Che natura hanno le norme disciplinari degli artt. 55-55-octies del D.Lgs. 165/2001?",
  "Norme imperative, che prevalgono sui contratti collettivi", ["Norme facoltative", "Raccomandazioni", "Norme regionali"],
  "Art. 55, c. 1.",
  "art. 55", "costituiscono norme imperative")

P("lav-146", "Procedimento disciplinare", 4, "Quale pena prevede l'art. 55-quinquies per il dipendente che attesta falsamente la presenza in servizio?",
  "Reclusione da uno a cinque anni e multa da 400 a 1.600 euro", ["Solo una sanzione disciplinare", "Reclusione fino a sei mesi", "Ammenda di 50 euro"],
  "Art. 55-quinquies, c. 1; la stessa pena si applica al medico che concorre.",
  "art. 55-quinquies", "è punito con la reclusione da uno a cinque anni")

P("lav-147", "Assenze", 4, "Quando l'assenza per malattia va giustificata con certificato di struttura pubblica o medico convenzionato SSN?",
  "Se supera dieci giorni e, in ogni caso, dopo il secondo evento di malattia nell'anno solare", ["Sempre, dal primo giorno", "Mai", "Solo oltre trenta giorni"],
  "Art. 55-septies, c. 1.",
  "art. 55-septies", "Nell'ipotesi di assenza per malattia protratta per un periodo superiore a dieci giorni")

P("lav-148", "Assenze", 3, "A chi è inviato telematicamente il certificato di malattia del dipendente pubblico?",
  "All'INPS, direttamente dal medico o dalla struttura sanitaria", ["Al sindaco", "Al Ministero dell'interno", "Al dirigente via posta ordinaria"],
  "Art. 55-septies, c. 2.",
  "art. 55-septies", "è inviata per via telematica, direttamente dal medico o dalla struttura sanitaria che la rilascia, all'Istituto nazionale della previdenza sociale")

P("lav-149", "Procedimento disciplinare", 5, "Se la violazione degli obblighi del dipendente porta alla condanna della PA al risarcimento, quale sanzione minima si applica?",
  "Sospensione dal servizio con privazione della retribuzione da tre giorni a tre mesi", ["Rimprovero verbale", "Licenziamento immediato", "Nessuna sanzione"],
  "Art. 55-sexies, c. 1.",
  "art. 55-sexies", "da un minimo di tre giorni fino ad un massimo di tre mesi")

P("lav-150", "Controversie", 3, "Quale giudice decide le controversie sui rapporti di lavoro dei dipendenti pubblici contrattualizzati?",
  "Il giudice ordinario in funzione di giudice del lavoro", ["Il TAR", "La Corte dei conti", "Il giudice di pace"],
  "Art. 63, c. 1: incluse quelle su incarichi dirigenziali e indennità di fine rapporto.",
  "art. 63", "Sono devolute al giudice ordinario, in funzione di giudice del lavoro")

P("lav-151", "Controversie", 4, "Quale giudice decide sulle controversie relative alle procedure concorsuali per l'assunzione nelle PA?",
  "Il giudice amministrativo", ["Il giudice del lavoro", "La Corte costituzionale", "Il giudice penale"],
  "Art. 63, c. 4.",
  "art. 63", "Restano devolute alla giurisdizione del giudice amministrativo le controversie in materia di procedure concorsuali")

P("lav-152", "Mobilità", 3, "Come si chiama il passaggio di un dipendente da un'amministrazione a un'altra su sua domanda (art. 30)?",
  "Mobilità volontaria (passaggio diretto di personale)", ["Comando obbligatorio", "Distacco sindacale", "Licenziamento collettivo"],
  "Art. 30, c. 1.",
  "art. 30", "Passaggio diretto di personale tra amministrazioni diverse")

P("lav-153", "Mobilità", 4, "Chi forma e gestisce, per le amministrazioni statali, l'elenco del personale in disponibilità?",
  "Il Dipartimento della funzione pubblica", ["L'INPS", "La Corte dei conti", "Il CNEL"],
  "Art. 34, c. 2.",
  "art. 34", "il Dipartimento della funzione pubblica della Presidenza del Consiglio dei ministri forma e gestisce l'elenco")


# --- Blocco 7: Costituzione (rapporti economici e pubblico impiego) e altre norme ---
COST = "norma_Costituzione.txt"
def K(id, arg, liv, testo, giusta, sbagliate, spieg, art, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, f"Costituzione, {art}", COST, frase)

K("lav-154", "Costituzione e lavoro", 1, "Su cosa è fondata la Repubblica italiana secondo l'art. 1 della Costituzione?",
  "Sul lavoro", ["Sulla proprietà privata", "Sulla religione cattolica", "Sull'iniziativa economica"],
  "Art. 1 Cost.",
  "art. 1", "L'Italia è una Repubblica democratica, fondata sul lavoro")

K("lav-155", "Costituzione e lavoro", 2, "Cosa riconosce l'art. 4 della Costituzione a tutti i cittadini?",
  "Il diritto al lavoro, promuovendo le condizioni che lo rendano effettivo", ["Il diritto a un posto pubblico", "Il diritto a non lavorare mai", "Il diritto a un reddito minimo garantito"],
  "Art. 4 Cost.: prevede anche il dovere di svolgere un'attività che concorra al progresso della società.",
  "art. 4", "La Repubblica riconosce a tutti i cittadini il diritto al lavoro")

K("lav-156", "Costituzione e lavoro", 2, "Secondo l'art. 35 Cost., come tutela la Repubblica il lavoro?",
  "In tutte le sue forme ed applicazioni", ["Solo il lavoro subordinato", "Solo il lavoro pubblico", "Solo il lavoro agricolo"],
  "Art. 35 Cost.: cura anche la formazione professionale e riconosce la libertà di emigrazione.",
  "art. 35", "La Repubblica tutela il lavoro in tutte le sue forme ed applicazioni")

K("lav-157", "Costituzione e lavoro", 2, "Quali caratteristiche deve avere la retribuzione secondo l'art. 36 Cost.?",
  "Proporzionata a quantità e qualità del lavoro e sufficiente ad assicurare un'esistenza libera e dignitosa", ["Uguale per tutti i lavoratori", "Decisa liberamente dal datore senza limiti", "Pari al salario minimo europeo"],
  "Art. 36, c. 1 Cost.",
  "art. 36", "retribuzione proporzionata alla quantità e qualità del suo lavoro")

K("lav-158", "Costituzione e lavoro", 2, "Il lavoratore può rinunciare al riposo settimanale e alle ferie annuali retribuite?",
  "No, non può rinunziarvi", ["Sì, in cambio di denaro", "Sì, con accordo scritto", "Solo se dirigente"],
  "Art. 36, c. 3 Cost.",
  "art. 36", "ferie annuali retribuite, e non può rinunziarvi")

K("lav-159", "Costituzione e lavoro", 3, "Chi stabilisce la durata massima della giornata lavorativa?",
  "La legge", ["Il datore di lavoro", "Il singolo contratto individuale", "Il prefetto"],
  "Art. 36, c. 2 Cost.",
  "art. 36", "La durata massima della giornata lavorativa è stabilita dalla legge")

K("lav-160", "Costituzione e lavoro", 2, "Cosa garantisce l'art. 37 Cost. alla donna lavoratrice?",
  "Gli stessi diritti e, a parità di lavoro, le stesse retribuzioni del lavoratore", ["Una retribuzione ridotta", "L'esclusione dai lavori pubblici", "Il pensionamento obbligatorio a 50 anni"],
  "Art. 37 Cost.",
  "art. 37", "La donna lavoratrice ha gli stessi diritti e, a parità di lavoro, le stesse retribuzioni")

K("lav-161", "Costituzione e lavoro", 3, "Chi stabilisce il limite minimo di età per il lavoro salariato?",
  "La legge", ["I contratti collettivi", "Le famiglie", "Le regioni con regolamento"],
  "Art. 37, c. 2 Cost.",
  "art. 37", "La legge stabilisce il limite minimo di età per il lavoro salariato")

K("lav-162", "Costituzione e lavoro", 3, "Per quali eventi l'art. 38 Cost. garantisce ai lavoratori mezzi adeguati alle esigenze di vita?",
  "Infortunio, malattia, invalidità e vecchiaia, disoccupazione involontaria", ["Solo vecchiaia", "Solo disoccupazione volontaria", "Solo maternità"],
  "Art. 38, c. 2 Cost.",
  "art. 38", "in caso di infortunio, malattia, invalidità e vecchiaia, disoccupazione involontaria")

K("lav-163", "Costituzione e lavoro", 3, "Chi ha diritto al mantenimento e all'assistenza sociale secondo l'art. 38 Cost.?",
  "Ogni cittadino inabile al lavoro e sprovvisto dei mezzi necessari per vivere", ["Ogni lavoratore in pensione", "Solo i dipendenti pubblici", "Solo i minori"],
  "Art. 38, c. 1 Cost.",
  "art. 38", "Ogni cittadino inabile al lavoro e sprovvisto dei mezzi necessari per vivere")

K("lav-164", "Costituzione e lavoro", 2, "L'organizzazione sindacale, secondo l'art. 39 Cost., è:",
  "Libera", ["Obbligatoria per tutti i lavoratori", "Vietata nel pubblico impiego", "Riservata ai dipendenti di grandi imprese"],
  "Art. 39, c. 1 Cost.",
  "art. 39", "L'organizzazione sindacale è libera")

K("lav-165", "Costituzione e lavoro", 4, "Quale requisito prevede l'art. 39 Cost. per la registrazione dei sindacati?",
  "Statuti che sanciscano un ordinamento interno a base democratica", ["Almeno un milione di iscritti", "L'approvazione del Governo", "L'affiliazione a un partito"],
  "Art. 39, c. 3 Cost. (disposizione mai attuata).",
  "art. 39", "un ordinamento interno a base democratica")

K("lav-166", "Costituzione e lavoro", 2, "Come si esercita il diritto di sciopero secondo l'art. 40 Cost.?",
  "Nell'ambito delle leggi che lo regolano", ["Senza alcun limite", "Solo con autorizzazione del prefetto", "Solo nel settore privato"],
  "Art. 40 Cost.",
  "art. 40", "Il diritto di sciopero si esercita nell'ambito delle leggi che lo regolano")

K("lav-167", "Costituzione e lavoro", 3, "Quale diritto riconosce ai lavoratori l'art. 46 Cost.?",
  "Il diritto a collaborare alla gestione delle aziende, nei modi stabiliti dalla legge", ["Il diritto alla proprietà dell'azienda", "Il diritto di nominare l'amministratore delegato", "Il diritto di vendere l'azienda"],
  "Art. 46 Cost.",
  "art. 46", "la Repubblica riconosce il diritto dei lavoratori a collaborare")

K("lav-168", "Costituzione e pubblico impiego", 2, "Come si accede, di regola, agli impieghi nelle pubbliche amministrazioni (art. 97 Cost.)?",
  "Mediante concorso, salvo i casi stabiliti dalla legge", ["Per chiamata diretta", "Per sorteggio", "Per anzianità di iscrizione al collocamento"],
  "Art. 97 Cost.",
  "art. 97", "Agli impieghi nelle pubbliche amministraz")

K("lav-169", "Costituzione e pubblico impiego", 2, "Al servizio di chi sono i pubblici impiegati secondo l'art. 98 Cost.?",
  "Al servizio esclusivo della Nazione", ["Al servizio del Governo in carica", "Al servizio del proprio dirigente", "Al servizio del partito di maggioranza"],
  "Art. 98 Cost.",
  "art. 98", "I pubblici impiegati sono al servizio esclusivo della Nazione")

K("lav-170", "Costituzione e pubblico impiego", 4, "Un pubblico impiegato eletto in Parlamento può ottenere promozioni?",
  "Solo per anzianità", ["Sì, per merito, senza limiti", "No, mai", "Solo con decreto del Presidente della Repubblica"],
  "Art. 98, c. 2 Cost.",
  "art. 98", "non possono conseguire promozioni se non per anzianità")

K("lav-171", "Costituzione e pubblico impiego", 3, "Per quali categorie la legge può limitare il diritto di iscriversi ai partiti politici (art. 98 Cost.)?",
  "Magistrati, militari di carriera in servizio attivo, funzionari e agenti di polizia, diplomatici e consoli all'estero", ["Tutti i dipendenti pubblici", "Gli insegnanti", "I medici del SSN"],
  "Art. 98, c. 3 Cost.",
  "art. 98", "per i magistrati, i militari di carriera in servizio attivo, i funzionari ed agenti di polizia")

K("lav-172", "Costituzione e pubblico impiego", 3, "Cosa garantisce l'art. 51 Cost. a chi è chiamato a funzioni pubbliche elettive?",
  "Il diritto di disporre del tempo necessario e di conservare il posto di lavoro", ["Uno stipendio doppio", "L'esonero dalle tasse", "La promozione automatica"],
  "Art. 51, c. 3 Cost.",
  "art. 51", "Chi è chiamato a funzioni pubbliche elettive ha diritto di")

T("lav-173", "Sicurezza sul lavoro", 2, "A quali settori si applica il D.Lgs. 81/2008?",
  "A tutti i settori di attività, privati e pubblici, e a tutte le tipologie di rischio", ["Solo all'industria", "Solo al settore privato", "Solo ai cantieri edili"],
  "Art. 3, c. 1.",
  "art. 3", "si applica a tutti i settori di attività, privati e pubblici, e a tutte le tipologie di rischio")

T("lav-174", "Sicurezza sul lavoro", 3, "In assenza di disposizioni contrattuali, che pausa spetta a chi lavora al videoterminale?",
  "Quindici minuti ogni centoventi minuti di applicazione continuativa", ["Cinque minuti ogni ora", "Un'ora ogni quattro ore", "Nessuna pausa"],
  "Art. 175, c. 3 D.Lgs. 81/2008.",
  "art. 175", "una pausa di quindici minuti ogni centoventi minuti di applicazione continuativa al videoterminale")

T("lav-175", "Sicurezza sul lavoro", 3, "Che natura ha la prevenzione incendi secondo l'art. 46 del D.Lgs. 81/2008?",
  "Funzione di preminente interesse pubblico, di esclusiva competenza statale", ["Attività facoltativa delle imprese", "Competenza esclusiva dei comuni", "Materia dei contratti collettivi"],
  "Art. 46, c. 1.",
  "art. 46", "La prevenzione incendi è la funzione di preminente interesse pubblico, di esclusiva competenza statuale")

T("lav-176", "Sicurezza sul lavoro", 4, "Il datore di lavoro può svolgere direttamente i compiti del servizio di prevenzione e protezione?",
  "Sì, nelle ipotesi dell'allegato 2, informandone prima il RLS", ["No, mai", "Sì, sempre e senza informare nessuno", "Solo con autorizzazione del prefetto"],
  "Art. 34, c. 1.",
  "art. 34", "il datore di lavoro può svolgere direttamente i compiti propri del servizio di prevenzione e protezione dai rischi")

T("lav-177", "Sicurezza sul lavoro", 4, "Quali obblighi ha il datore che affida lavori a un'impresa appaltatrice all'interno della propria azienda (art. 26)?",
  "Verificarne l'idoneità tecnico-professionale e cooperare e coordinarsi sui rischi da interferenze", ["Nessuno, la sicurezza è tutta dell'appaltatore", "Solo pagare il corrispettivo", "Solo comunicare il nome dell'appaltatore all'INPS"],
  "Art. 26 D.Lgs. 81/2008 (DUVRI).",
  "art. 26", "in caso di affidamento di lavori, servizi e forniture all'impresa appaltatrice")

T("lav-178", "Sicurezza sul lavoro", 4, "Quale sanzione rischia il datore che non effettua la valutazione dei rischi o non nomina l'RSPP?",
  "L'arresto o l'ammenda (sanzione penale contravvenzionale)", ["Solo un richiamo verbale", "Nessuna sanzione", "La chiusura definitiva automatica dell'azienda"],
  "Art. 55, c. 1 D.Lgs. 81/2008.",
  "art. 55", "È punito con l'arresto da tre a sei mesi o con l'ammenda")

T("lav-179", "Sicurezza sul lavoro", 3, "Chi deve designare preventivamente i lavoratori addetti alle emergenze (antincendio, evacuazione, primo soccorso)?",
  "Il datore di lavoro e i dirigenti", ["Il RLS", "I vigili del fuoco", "Il medico di base"],
  "Art. 18, c. 1, lett. b).",
  "art. 18", "designare preventivamente i lavoratori incaricati dell'attuazione delle misure di prevenzione incendi")

T("lav-180", "Sicurezza sul lavoro", 3, "Quali misure prevalgono, secondo le misure generali di tutela, sui dispositivi di protezione individuale?",
  "Le misure di protezione collettiva", ["I DPI vengono sempre prima", "Le sanzioni disciplinari", "Le assicurazioni private"],
  "Art. 15, c. 1, lett. i): priorità delle misure di protezione collettiva rispetto a quelle individuali.",
  "art. 15", "la priorità delle misure di protezione collettiva rispetto alle misure di protezione individuale")

S("lav-181", "Statuto dei lavoratori", 4, "Per le imprese industriali e commerciali, il titolo III dello Statuto (attività sindacale) si applica alle unità produttive con:",
  "Più di quindici dipendenti (più di cinque per le imprese agricole)", ["Qualsiasi numero di dipendenti", "Più di cento dipendenti", "Più di mille dipendenti"],
  "Art. 35 L. 300/1970.",
  "art. 35", "che occupa più di quindici dipendenti")

S("lav-182", "Statuto dei lavoratori", 4, "Lo Statuto si applica ai dipendenti degli enti pubblici economici?",
  "Sì, a quelli che svolgono esclusivamente o prevalentemente attività economica", ["No, mai", "Solo ai dirigenti", "Solo se lo prevede lo statuto dell'ente"],
  "Art. 37 L. 300/1970.",
  "art. 37", "dipendenti da enti pubblici che svolgono esclusivamente o prevalentemente attività economica")

S("lav-183", "Diritti sindacali", 4, "Quanti permessi retribuiti minimi spettano ai dirigenti RSA nelle unità produttive con più di 200 dipendenti?",
  "Otto ore mensili", ["Un'ora l'anno", "Due giorni al mese", "Quaranta ore settimanali"],
  "Art. 23 L. 300/1970.",
  "art. 23", "non potranno essere inferiori a otto ore mensili")

S("lav-184", "Diritti sindacali", 3, "Con quanto preavviso, di regola, il dirigente RSA comunica l'uso dei permessi retribuiti?",
  "24 ore prima, per iscritto, tramite le RSA", ["Una settimana prima", "Un mese prima", "Non serve preavviso"],
  "Art. 23 L. 300/1970.",
  "art. 23", "deve darne comunicazione scritta al datore di lavoro di regola 24 ore prima")

S("lav-185", "Statuto dei lavoratori", 3, "Il datore di lavoro può far controllare l'idoneità fisica del lavoratore?",
  "Sì, ma da enti pubblici e istituti specializzati di diritto pubblico", ["Sì, dal proprio medico di fiducia", "No, mai", "Sì, ma solo dai colleghi"],
  "Art. 5, c. 3 L. 300/1970.",
  "art. 5", "Il datore di lavoro ha facoltà di far controllare la idoneità fisica del lavoratore da parte di enti pubblici")

S("lav-186", "Statuto dei lavoratori", 3, "Chi controlla la qualità del servizio di mensa aziendale secondo l'art. 11?",
  "Le rappresentanze sindacali aziendali", ["L'ASL in via esclusiva", "Il datore di lavoro", "Il comune"],
  "Art. 11 L. 300/1970.",
  "art. 11", "hanno diritto di controllare la qualità del")

S("lav-187", "Statuto dei lavoratori", 3, "Possono gli istituti di patronato operare all'interno dell'azienda?",
  "Sì, su un piano di parità, secondo accordi aziendali", ["No, mai", "Solo con autorizzazione del prefetto", "Solo nel settore pubblico"],
  "Art. 12 L. 300/1970.",
  "art. 12", "hanno diritto di svolgere, su un piano di parità, la loro attività all'interno dell'azienda")

S("lav-188", "Statuto dei lavoratori", 3, "Il lavoratore eletto sindaco o assessore comunale che diritto ha, oltre ai permessi?",
  "Permessi non retribuiti per un minimo di trenta ore mensili", ["Un anno sabbatico retribuito", "Il doppio dello stipendio", "Nessun diritto"],
  "Art. 32 L. 300/1970 (in parte sostituito da leggi successive).",
  "art. 32", "permessi non retribuiti per un minimo di trenta ore mensili")

C("lav-189", "Contratti di lavoro", 3, "Il contratto part-time può essere stipulato anche per un rapporto a tempo determinato?",
  "Sì, l'assunzione a tempo parziale è possibile anche nei contratti a termine", ["No, solo a tempo indeterminato", "Solo per i dirigenti", "Solo nel pubblico impiego"],
  "Art. 4 D.Lgs. 81/2015.",
  "art. 4", "Nel rapporto di lavoro subordinato, anche a tempo determinato, l'assunzione può avvenire a tempo pieno")

C("lav-190", "Contratti di lavoro", 4, "Se il datore non eroga la formazione all'apprendista per sua esclusiva responsabilità, cosa deve versare?",
  "La differenza contributiva rispetto al livello superiore, maggiorata del 100%", ["Nulla", "Una multa fissa di 100 euro", "Il TFR in anticipo"],
  "Art. 47, c. 1 D.Lgs. 81/2015.",
  "art. 47", "maggiorata del 100 per cento")

C("lav-191", "Contratti di lavoro", 4, "Su accordo delle parti, come può essere trasformato un rapporto da tempo pieno a part-time?",
  "Con accordo risultante da atto scritto", ["Con decisione unilaterale del datore", "Oralmente", "Solo con sentenza del giudice"],
  "Art. 8, c. 2.",
  "art. 8", "Su accordo delle parti risultante da atto scritto è ammessa la trasformazione")

C("lav-192", "Contratti di lavoro", 4, "Il lavoro intermittente è vietato presso unità produttive che, nei sei mesi precedenti, hanno effettuato:",
  "Licenziamenti collettivi di lavoratori con le stesse mansioni", ["Assunzioni di apprendisti", "Promozioni interne", "Elezioni della RSU"],
  "Art. 14, c. 1, lett. b).",
  "art. 14", "entro i sei mesi precedenti, a licenziamenti collettivi")

P("lav-193", "Lavoro pubblico", 3, "Quale principio sull'organizzazione degli uffici fissa l'art. 2 del D.Lgs. 165/2001?",
  "Funzionalità rispetto ai compiti e ai programmi, con obiettivi di efficienza, efficacia ed economicità", ["Massimizzazione del numero di dipendenti", "Gerarchia militare", "Rotazione annuale obbligatoria di tutti gli uffici"],
  "Art. 2, c. 1, lett. a).",
  "art. 2", "funzionalità rispetto ai compiti e ai programmi di attività")

P("lav-194", "Lavoro pubblico", 4, "Cosa devono garantire le PA oltre alle pari opportunità, secondo l'art. 7 del D.Lgs. 165/2001?",
  "Un ambiente di lavoro improntato al benessere organizzativo, contrastando la violenza morale o psichica", ["Il lavoro notturno obbligatorio", "Un premio annuale uguale per tutti", "La settimana corta"],
  "Art. 7, c. 1.",
  "art. 7", "un ambiente di lavoro improntato al benessere organizzativo")

P("lav-195", "Dirigenza", 4, "Come si accede alla qualifica di dirigente di prima fascia?",
  "Con i meccanismi dell'art. 28-bis (concorso e incarichi)", ["Per sola anzianità come dirigente di seconda fascia", "Per elezione dei dipendenti", "Per nomina del sindacato"],
  "Art. 23, c. 1 D.Lgs. 165/2001.",
  "art. 23", "L'accesso alla qualifica di dirigente della prima fascia avviene attraverso i meccanismi di accesso previsti dall'articolo 28-bis")

P("lav-196", "Contrattazione collettiva", 4, "Come si calcola la rappresentatività sindacale ai fini dell'art. 43?",
  "Media tra dato associativo (deleghe) e dato elettorale (voti nelle RSU)", ["Solo numero di iscritti nazionali", "Solo voti alle elezioni politiche", "Numero di scioperi proclamati"],
  "Art. 43, c. 1.",
  "art. 43", "considerando a tal fine la media tra il dato associativo e il dato elettorale")

P("lav-197", "Contrattazione collettiva", 4, "Entro quanti giorni il Governo può esprimere valutazioni sugli atti di indirizzo dei comitati di settore regionali e locali?",
  "Venti giorni", ["Cinque giorni", "Sessanta giorni", "Un anno"],
  "Art. 47, c. 2.",
  "art. 47", "nei successivi venti giorni, può esprimere le sue valutazioni")

P("lav-198", "Procedimento disciplinare", 3, "Oltre alla pena, a cosa è obbligato il dipendente che attesta falsamente la presenza in servizio?",
  "A risarcire il danno patrimoniale pari alla retribuzione dei periodi non lavorati, oltre al danno d'immagine", ["A nulla", "A lavorare gratis un mese", "A pagare una tassa di 10 euro"],
  "Art. 55-quinquies, c. 2.",
  "art. 55-quinquies", "è obbligato a risarcire il danno patrimoniale")

P("lav-199", "Lavoro pubblico", 4, "Le disposizioni di legge applicabili solo ai dipendenti pubblici possono essere derogate dai contratti collettivi?",
  "Sì, nelle materie affidate alla contrattazione collettiva e nei limiti previsti", ["No, mai", "Sì, sempre e in ogni materia", "Solo con decreto ministeriale"],
  "Art. 2, c. 2 D.Lgs. 165/2001.",
  "art. 2", "possono essere derogate ((nelle materie affidate alla contrattazione collettiva")

P("lav-200", "Lavoro pubblico", 3, "Cosa prevede l'art. 52 sull'esercizio di fatto di mansioni non corrispondenti alla qualifica?",
  "Non ha effetto ai fini dell'inquadramento né dell'assegnazione di incarichi di direzione", ["Dà diritto all'inquadramento dopo tre mesi", "Comporta la nullità del contratto", "Comporta la perdita del posto"],
  "Art. 52, c. 1.",
  "art. 52", "L'esercizio di fatto di mansioni non corrispondenti alla qualifica di appartenenza non ha effetto")

P("lav-201", "Lavoro pubblico", 4, "In quante aree almeno sono inquadrati i dipendenti pubblici non dirigenti (art. 52, c. 1-bis)?",
  "Almeno tre aree funzionali", ["Una sola area", "Dieci aree", "Due fasce"],
  "Art. 52, c. 1-bis D.Lgs. 165/2001.",
  "art. 52", "sono inquadrati in almeno tre d")
