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

# --- Ampliamento a 300: D.Lgs. 81/2015 (contratti) ---
C("lav-202", "Mansioni", 3, "Secondo l'art. 2103 c.c. (riscritto dal D.Lgs. 81/2015), in caso di modifica degli assetti organizzativi che incide sulla sua posizione, il lavoratore può essere assegnato:",
  "a mansioni del livello di inquadramento inferiore, purché nella medesima categoria legale", ["a qualsiasi mansione inferiore, anche di altra categoria", "solo a mansioni superiori", "a mansioni inferiori con riduzione proporzionale della retribuzione"],
  "Il demansionamento è ammesso di un livello, nella stessa categoria legale, conservando livello e trattamento retributivo.", "art. 3", "lo stesso può essere assegnato a mansioni appartenenti al livello di inquadramento inferiore purché rientranti nella medesima categoria legale")
C("lav-203", "Mansioni", 4, "Se il datore non adempie l'obbligo formativo legato al cambio di mansioni, l'atto di assegnazione delle nuove mansioni:",
  "resta valido", ["è nullo", "è annullabile su richiesta del lavoratore entro 60 giorni", "diventa inefficace dopo sei mesi"],
  "L'art. 2103 c.c. precisa che il mancato adempimento dell'obbligo formativo non determina la nullità dell'assegnazione.", "art. 3", "il cui mancato adempimento non determina comunque la nullità dell'atto di assegnazione delle nuove mansioni")
C("lav-204", "Mansioni", 4, "In caso di assegnazione a mansioni inferiori, come va comunicato il mutamento al lavoratore?",
  "Per iscritto, a pena di nullità", ["Anche oralmente", "Con raccomandata entro 30 giorni, a pena di decadenza", "Non serve alcuna comunicazione"],
  "Il lavoratore conserva livello di inquadramento e trattamento retributivo, salvo gli elementi legati a particolari modalità della prestazione precedente.", "art. 3", "il mutamento di mansioni è comunicato per iscritto, a pena di nullità")
C("lav-205", "Mansioni", 3, "Cosa spetta al lavoratore assegnato a mansioni superiori?",
  "Il trattamento corrispondente all'attività svolta", ["Nessuna differenza retributiva", "Una indennità forfettaria fissata dalla legge", "Solo un punteggio per i concorsi interni"],
  "Nel settore privato l'assegnazione diventa poi definitiva dopo il periodo fissato dai contratti collettivi o dalla legge.", "art. 3", "Nel caso di assegnazione a mansioni superiori il lavoratore ha diritto al trattamento corrispondente all'attività svolta")
C("lav-206", "Part-time", 4, "Se il contratto collettivo non disciplina il lavoro supplementare, entro quale misura il datore può richiederlo al lavoratore part-time?",
  "Non oltre il 25 per cento delle ore settimanali concordate", ["Non oltre il 10 per cento", "Non oltre il 50 per cento", "Senza limiti"],
  "Art. 6, comma 2, del D.Lgs. 81/2015.", "art. 6", "in misura non superiore al 25 per cento delle ore di lavoro settimanali concordate")
C("lav-207", "Part-time", 4, "In assenza di disciplina collettiva, con quale maggiorazione è retribuito il lavoro supplementare?",
  "15 per cento della retribuzione oraria globale di fatto", ["25 per cento", "50 per cento", "Nessuna maggiorazione"],
  "Art. 6, comma 2.", "art. 6", "Il lavoro supplementare è retribuito con una maggiorazione del 15 per cento")
C("lav-208", "Part-time", 2, "Rispetto al lavoratore a tempo pieno di pari inquadramento, il lavoratore part-time:",
  "non deve ricevere un trattamento meno favorevole", ["ha diritto a un trattamento più favorevole", "può avere un trattamento inferiore se lo prevede il contratto individuale", "non ha diritto alle ferie"],
  "Art. 7: i diritti sono gli stessi, il trattamento economico è riproporzionato alla prestazione.", "art. 7", "Il lavoratore a tempo parziale non deve ricevere un trattamento meno favorevole rispetto al lavoratore a tempo pieno di pari inquadramento")
C("lav-209", "Part-time", 4, "Come si computano i lavoratori part-time ai fini delle discipline che dipendono dal numero di dipendenti?",
  "In proporzione all'orario svolto, rapportato al tempo pieno", ["Come lavoratori a tempo pieno", "Non si computano", "Ciascuno vale mezza unità"],
  "Art. 9 del D.Lgs. 81/2015.", "art. 9", "i lavoratori a tempo parziale sono computati in proporzione all'orario svolto, rapportato al tempo pieno")
C("lav-210", "Part-time", 5, "Se manca la prova della stipulazione a tempo parziale, su domanda del lavoratore il giudice:",
  "dichiara la sussistenza di un rapporto a tempo pieno", ["dichiara nullo il contratto", "riduce le ore al minimo contrattuale", "applica una sanzione solo amministrativa"],
  "Art. 10, comma 1: restano dovuti retribuzione e contributi per il periodo precedente.", "art. 10", "su domanda del lavoratore è dichiarata la sussistenza fra le parti di un rapporto di lavoro a tempo pieno")
C("lav-211", "Part-time", 5, "Quali disposizioni sul part-time NON si applicano alle pubbliche amministrazioni, secondo l'art. 12?",
  "Gli articoli 6, commi 2 e 6, e 10", ["Tutte le disposizioni della sezione", "Solo l'articolo 5", "Gli articoli 7 e 8"],
  "Le altre norme sul part-time si applicano anche al pubblico impiego, salvo disposizioni speciali.", "art. 12", "con esclusione di quelle contenute negli articoli 6, commi 2 e 6, e 10")
C("lav-212", "Lavoro intermittente", 4, "Con quali lavoratori il contratto intermittente può essere concluso in ogni caso, a prescindere dai contratti collettivi?",
  "Con meno di 24 anni (prestazioni entro i 25) e con più di 55 anni", ["Solo con studenti universitari", "Con meno di 30 anni e più di 60", "Con chiunque sia disoccupato da più di un anno"],
  "Art. 13, comma 2, del D.Lgs. 81/2015.", "art. 13", "può in ogni caso essere concluso con soggetti con meno di 24 anni di età")
C("lav-213", "Lavoro intermittente", 5, "Fuori da turismo, pubblici esercizi e spettacolo, qual è il limite del lavoro intermittente con lo stesso datore?",
  "400 giornate di effettivo lavoro in tre anni solari", ["200 giornate in un anno", "100 giornate in due anni", "Nessun limite"],
  "Superato il limite, il rapporto si trasforma a tempo pieno e indeterminato.", "art. 13", "non superiore a quattrocento giornate di effettivo lavoro nell'arco di tre anni solari")
C("lav-214", "Lavoro intermittente", 4, "Che cosa compensa l'indennità di disponibilità nel lavoro intermittente?",
  "L'impegno del lavoratore a rispondere alla chiamata; è mensile e divisibile in quote orarie", ["Le ore effettivamente lavorate", "Le ferie non godute", "Il trattamento di fine rapporto"],
  "Art. 16: la misura è fissata dai contratti collettivi, non sotto il minimo stabilito con decreto ministeriale.", "art. 16", "La misura dell'indennità mensile di disponibilità, divisibile in quote orarie")
C("lav-215", "Lavoro intermittente", 5, "Cosa può comportare il rifiuto ingiustificato di rispondere alla chiamata da parte del lavoratore intermittente che si è obbligato?",
  "Il licenziamento e la restituzione della quota di indennità successiva al rifiuto", ["Solo un richiamo verbale", "Una multa fino a quattro ore di retribuzione", "Nessuna conseguenza"],
  "Art. 16, comma 5.", "art. 16", "Il rifiuto ingiustificato di rispondere alla chiamata può costituire motivo di licenziamento")
C("lav-216", "Lavoro intermittente", 4, "Come si computa il lavoratore intermittente nell'organico dell'impresa?",
  "In proporzione all'orario effettivamente svolto in ciascun semestre", ["Come un lavoratore a tempo pieno", "Non si computa mai", "In proporzione alle chiamate dell'anno precedente"],
  "Art. 18 del D.Lgs. 81/2015.", "art. 18", "in proporzione all'orario di lavoro effettivamente svolto nell'arco di ciascun semestre")
C("lav-217", "Contratti a termine", 3, "Per quale finalità è sempre vietato assumere a tempo determinato?",
  "Per sostituire lavoratori in sciopero", ["Per sostituire lavoratrici in maternità", "Per attività stagionali", "Per punte di attività"],
  "Art. 20: altri divieti riguardano licenziamenti collettivi recenti, cassa integrazione e mancata valutazione dei rischi.", "art. 20", "per la sostituzione di lavoratori che esercitano il diritto di sciopero")
C("lav-218", "Contratti a termine", 4, "Un datore che non ha effettuato la valutazione dei rischi può stipulare contratti a termine?",
  "No: il termine non è ammesso e il contratto si trasforma a tempo indeterminato", ["Sì, senza conseguenze", "Sì, ma solo fino a sei mesi", "Sì, con una sanzione amministrativa"],
  "Art. 20, comma 1, lett. d) e comma 2.", "art. 20", "da parte di datori di lavoro che non hanno effettuato la valutazione dei rischi")
C("lav-219", "Contratti a termine", 4, "Quante proroghe al massimo sono ammesse per un contratto a tempo determinato nell'arco di 24 mesi?",
  "Quattro", ["Due", "Cinque", "Sei"],
  "Art. 21, comma 1: oltre il limite il contratto si trasforma a tempo indeterminato.", "art. 21", "per un massimo di quattro volte nell'arco di ventiquattro mesi")
C("lav-220", "Contratti a termine", 5, "Se il rapporto a termine prosegue dopo la scadenza, quale maggiorazione spetta per i primi dieci giorni?",
  "20 per cento della retribuzione per ogni giorno", ["10 per cento", "40 per cento", "Nessuna"],
  "Art. 22: dall'undicesimo giorno la maggiorazione sale al 40 per cento.", "art. 22", "pari al 20 per cento fino al decimo giorno successivo e al 40 per cento per ciascun giorno ulteriore")
C("lav-221", "Contratti a termine", 5, "Un contratto a termine di quattro mesi continua oltre la scadenza: da quando si trasforma a tempo indeterminato?",
  "Dopo il trentesimo giorno di prosecuzione", ["Dal giorno successivo alla scadenza", "Dopo il cinquantesimo giorno", "Dopo sei mesi"],
  "Art. 22, comma 2: 30 giorni per i contratti sotto i sei mesi, 50 negli altri casi.", "art. 22", "Qualora il rapporto di lavoro continui oltre il trentesimo giorno in caso di contratto di durata inferiore a sei mesi")
C("lav-222", "Contratti a termine", 3, "Quale trattamento spetta al lavoratore a tempo determinato rispetto ai colleghi a tempo indeterminato comparabili?",
  "Lo stesso trattamento economico e normativo, in proporzione al periodo lavorato", ["Un trattamento ridotto del 20 per cento", "Solo il minimo di legge", "Lo stesso trattamento ma senza ferie"],
  "Art. 25: principio di non discriminazione, salvo obiettiva incompatibilità con la natura del contratto.", "art. 25", "Al lavoratore a tempo determinato spetta il trattamento economico e normativo in atto nell'impresa per i lavoratori con contratto a tempo indeterminato comparabili")
C("lav-223", "Contratti a termine", 5, "Qual è la durata massima dei contratti a tempo determinato con i dirigenti?",
  "Cinque anni", ["Tre anni", "Ventiquattro mesi", "Dieci anni"],
  "Art. 29, comma 2: il dirigente può recedere dopo un triennio a norma dell'art. 2118 c.c.", "art. 29", "i contratti di lavoro a tempo determinato con i dirigenti, che non possono avere una durata superiore a cinque anni")
C("lav-224", "Somministrazione", 4, "Cosa deve fare l'utilizzatore verso i lavoratori somministrati per retribuzioni e contributi?",
  "Ne risponde in solido con il somministratore, salvo rivalsa", ["Nulla: risponde solo l'agenzia", "Paga solo se l'agenzia fallisce", "Paga la metà dei contributi"],
  "Art. 35, comma 2, del D.Lgs. 81/2015.", "art. 35", "L'utilizzatore è obbligato in solido con il somministratore a corrispondere ai lavoratori i trattamenti retributivi")
C("lav-225", "Somministrazione", 3, "Durante la missione, quali condizioni spettano ai lavoratori somministrati?",
  "Condizioni complessivamente non inferiori a quelle dei dipendenti di pari livello dell'utilizzatore", ["Quelle minime fissate dall'agenzia", "Il 70 per cento della retribuzione dei dipendenti", "Le condizioni del contratto nazionale del commercio"],
  "Art. 35, comma 1: parità di trattamento a parità di mansioni.", "art. 35", "a condizioni economiche e normative complessivamente non inferiori a quelle dei dipendenti di pari livello dell'utilizzatore")
C("lav-226", "Somministrazione", 4, "Che cosa accade se il contratto di somministrazione è privo di forma scritta?",
  "È nullo e i lavoratori sono considerati dipendenti dell'utilizzatore", ["È valido ma sanzionabile", "I lavoratori restano dipendenti dell'agenzia", "Si converte in appalto di servizi"],
  "Art. 38, comma 1.", "art. 38", "In mancanza di forma scritta il contratto di somministrazione di lavoro è nullo e i lavoratori sono considerati a tutti gli effetti alle dipendenze dell'utilizzatore")
C("lav-227", "Somministrazione", 3, "Quale di questi elementi deve contenere il contratto di somministrazione?",
  "Gli estremi dell'autorizzazione rilasciata al somministratore", ["Il codice fiscale dei familiari dei lavoratori", "Il parere dell'Ispettorato del lavoro", "Il bilancio dell'utilizzatore"],
  "Art. 33: il contratto è scritto e indica tra l'altro numero dei lavoratori, rischi, durata, mansioni, luogo e orario.", "art. 33", "gli estremi dell'autorizzazione rilasciata al somministratore")
C("lav-228", "Apprendistato", 3, "Qual è la durata minima del contratto di apprendistato, salvo eccezioni?",
  "Sei mesi", ["Tre mesi", "Un anno", "Due anni"],
  "Art. 42, comma 2, del D.Lgs. 81/2015.", "art. 42", "Il contratto di apprendistato ha una durata minima non inferiore a sei mesi")
C("lav-229", "Apprendistato", 4, "Quale età è richiesta per l'apprendistato per la qualifica e il diploma professionale?",
  "Dai 15 anni compiuti fino al compimento dei 25", ["Dai 18 ai 29 anni", "Dai 16 ai 21 anni", "Dai 14 ai 18 anni"],
  "Art. 43, comma 2: la durata non può superare tre anni (quattro per il diploma quadriennale).", "art. 43", "i giovani che hanno compiuto i 15 anni di età e fino al compimento dei 25")
C("lav-230", "Apprendistato", 4, "Per quali finalità può essere usato l'apprendistato di alta formazione e ricerca?",
  "Titoli universitari, dottorati, attività di ricerca e praticantato per le professioni ordinistiche", ["Solo per il diploma di scuola media", "Solo per i corsi di lingua", "Solo per la qualifica di operaio specializzato"],
  "Art. 45: possono essere assunti soggetti tra i 18 e i 29 anni con diploma.", "art. 45", "nonché per il praticantato per l'accesso alle professioni ordinistiche")
C("lav-231", "Apprendistato", 5, "Nell'apprendistato per la qualifica e il diploma professionale, quale fatto costituisce giustificato motivo di licenziamento?",
  "Il mancato raggiungimento degli obiettivi formativi attestato dall'istituzione formativa", ["Il compimento dei 18 anni", "Una singola assenza ingiustificata", "La richiesta di ferie"],
  "Art. 42, comma 3: per il resto, durante l'apprendistato si applicano le sanzioni per il licenziamento illegittimo.", "art. 42", "costituisce giustificato motivo di licenziamento il mancato raggiungimento degli obiettivi formativi")

# --- D.Lgs. 81/2008 (sicurezza) ---
T("lav-232", "Sicurezza sul lavoro", 3, "Su quali argomenti deve vertere, in particolare, la formazione dei lavoratori secondo l'art. 37 del D.Lgs. 81/2008?",
  "Concetti di rischio, danno, prevenzione e protezione, e rischi delle mansioni", ["Solo l'uso dei DPI", "Solo il primo soccorso", "Solo il codice disciplinare"],
  "La formazione deve essere sufficiente e adeguata, anche rispetto alle conoscenze linguistiche.", "art. 37", "concetti di rischio, danno, prevenzione, protezione, organizzazione della prevenzione aziendale")
T("lav-233", "Sicurezza sul lavoro", 4, "Con quale atto sono definiti durata e contenuti minimi della formazione dei lavoratori?",
  "Con accordo in sede di Conferenza Stato-Regioni", ["Con decreto del Presidente della Repubblica", "Con regolamento aziendale", "Con legge regionale"],
  "Art. 37, comma 2, previa consultazione delle parti sociali.", "art. 37", "sono definiti mediante accordo in sede di Conferenza permanente per i rapporti tra lo Stato, le regioni")
T("lav-234", "Sicurezza sul lavoro", 3, "In caso di pericolo grave e immediato che non può essere evitato, il datore di lavoro deve fare in modo che i lavoratori possano:",
  "cessare l'attività o mettersi al sicuro abbandonando immediatamente il luogo di lavoro", ["restare al posto in attesa di istruzioni scritte", "proseguire fino alla fine del turno", "chiamare prima il sindacato"],
  "Art. 43, comma 1, lett. d).", "art. 43", "possano cessare la loro attività, o mettersi al sicuro, abbandonando immediatamente il luogo di lavoro")
T("lav-235", "Sicurezza sul lavoro", 3, "Sentito chi il datore di lavoro prende i provvedimenti in materia di primo soccorso?",
  "Il medico competente, ove nominato", ["Il sindaco", "L'ispettorato del lavoro", "Il RLS, obbligatoriamente"],
  "Art. 45, comma 1: si tiene conto di natura dell'attività e dimensioni dell'azienda.", "art. 45", "sentito il medico competente ove nominato, prende i provvedimenti necessari in materia di primo soccorso")
T("lav-236", "Sicurezza sul lavoro", 4, "Quale decreto ministeriale individua le caratteristiche minime delle attrezzature di primo soccorso?",
  "Il D.M. 15 luglio 2003, n. 388", ["Il D.M. 10 marzo 1998", "Il D.P.R. 547/1955", "Il D.Lgs. 626/1994"],
  "Art. 45, comma 2, del D.Lgs. 81/2008.", "art. 45", "decreto ministeriale 15 luglio 2003, n. 388")
T("lav-237", "Sicurezza sul lavoro", 4, "Dove opera il rappresentante dei lavoratori per la sicurezza territoriale (RLST)?",
  "Nelle aziende del territorio o comparto in cui non è stato eletto o designato il RLS", ["Solo nelle aziende con più di 200 dipendenti", "Solo nelle pubbliche amministrazioni", "Presso l'ispettorato del lavoro"],
  "Art. 48, comma 1.", "art. 48", "nelle quali non sia stato eletto o designato il rappresentante dei lavoratori per la sicurezza")
T("lav-238", "Sicurezza sul lavoro", 4, "Qual è il ruolo degli organismi paritetici nelle controversie su rappresentanza, informazione e formazione?",
  "Sono prima istanza di riferimento", ["Decidono con sentenza", "Non hanno alcun ruolo", "Sostituiscono il giudice del lavoro"],
  "Art. 51, comma 2, salvo quanto previsto dalla contrattazione collettiva.", "art. 51", "sono prima istanza di riferimento in merito a controversie")
T("lav-239", "Sicurezza sul lavoro", 4, "Presso quale ente è costituito il fondo di sostegno alla piccola e media impresa, ai RLST e alla pariteticità?",
  "INAIL", ["INPS", "Ministero della salute", "Camera di commercio"],
  "Art. 52, comma 1, del D.Lgs. 81/2008.", "art. 52", "Presso l'Istituto nazionale per l'assicurazione contro gli infortuni sul lavoro (INAIL) è costituito il fondo")
T("lav-240", "Sicurezza sul lavoro", 3, "La documentazione prevista dal D.Lgs. 81/2008 può essere conservata con sistemi informatici?",
  "Sì, è consentito l'impiego di sistemi di elaborazione automatica dei dati", ["No, solo su carta", "Solo con autorizzazione dell'ASL", "Solo per le aziende con più di 50 dipendenti"],
  "Art. 53: l'accesso deve essere limitato ai soggetti abilitati e le modifiche solo aggiuntive.", "art. 53", "È consentito l'impiego di sistemi di elaborazione automatica dei dati")
T("lav-241", "Sicurezza sul lavoro", 4, "Quale sanzione rischia il lavoratore che viola gli obblighi di sicurezza dell'art. 20, comma 2 (ad es. uso dei DPI)?",
  "Arresto fino a un mese o ammenda da 200 a 600 euro", ["Solo il licenziamento", "Nessuna sanzione penale", "Reclusione da uno a tre anni"],
  "Art. 59: anche i lavoratori sono destinatari di sanzioni.", "art. 59", "con l'arresto fino a un mese o con l'ammenda da 200 a 600 euro")
T("lav-242", "Sicurezza sul lavoro", 3, "A quale allegato del D.Lgs. 81/2008 devono essere conformi i luoghi di lavoro?",
  "Allegato IV", ["Allegato I", "Allegato X", "Allegato XXXIII"],
  "Art. 63, comma 1; i luoghi vanno strutturati tenendo conto, se del caso, dei lavoratori disabili.", "art. 63", "I luoghi di lavoro devono essere conformi ai requisiti indicati nell'allegato IV")
T("lav-243", "Sicurezza sul lavoro", 2, "Come devono essere tenute le vie di circolazione che portano alle uscite di emergenza?",
  "Sgombre, per poterle usare in ogni evenienza", ["Chiuse a chiave fuori orario", "Segnalate ma usabili come deposito temporaneo", "Accessibili solo agli addetti antincendio"],
  "Art. 64, comma 1, lett. b).", "art. 64", "siano sgombre allo scopo di consentirne l'utilizzazione in ogni evenienza")
T("lav-244", "Sicurezza sul lavoro", 3, "Secondo l'art. 65, è consentito destinare al lavoro locali chiusi sotterranei o semisotterranei?",
  "Di regola no, salvo le deroghe previste", ["Sì, sempre", "Solo per uffici", "Solo nei mesi estivi"],
  "L'art. 65 pone il divieto, con deroghe per particolari esigenze tecniche e condizioni di sicurezza.", "art. 65", "È vietato destinare al lavoro locali chiusi sotterranei o semisotterranei")
T("lav-245", "Sicurezza sul lavoro", 3, "Come definisce il D.Lgs. 81/2008 la «zona pericolosa»?",
  "Qualsiasi zona dentro o vicino a un'attrezzatura in cui la presenza di un lavoratore costituisce un rischio", ["Solo le aree con sostanze chimiche", "Le zone esterne al perimetro aziendale", "Le aree dove si fuma"],
  "Art. 69, lett. c); il «lavoratore esposto» è chi si trova in tutto o in parte in tale zona.", "art. 69", "qualsiasi zona all'interno ovvero in prossimità di una attrezzatura di lavoro nella quale la presenza di un lavoratore costituisce un rischio")
T("lav-246", "Sicurezza sul lavoro", 3, "Che cosa si intende per «attrezzatura di lavoro» nel D.Lgs. 81/2008?",
  "Qualsiasi macchina, apparecchio, utensile o impianto destinato a essere usato durante il lavoro", ["Solo le macchine con motore elettrico", "Solo i dispositivi di protezione individuale", "Solo i veicoli aziendali"],
  "Art. 69, lett. a).", "art. 69", "qualsiasi macchina, apparecchio, utensile o impianto")
T("lav-247", "Sicurezza sul lavoro", 4, "Nella scelta delle attrezzature di lavoro, quale fattore NON è tra quelli che il datore deve considerare per legge?",
  "Il prezzo più basso sul mercato", ["Le caratteristiche specifiche del lavoro", "I rischi presenti nell'ambiente di lavoro", "I rischi da interferenze con altre attrezzature"],
  "Art. 71, comma 2: condizioni del lavoro, rischi dell'ambiente, rischi dell'attrezzatura e interferenze.", "art. 71", "i rischi derivanti da interferenze con le altre attrezzature già in uso")
T("lav-248", "Sicurezza sul lavoro", 3, "Chi è il «committente» nei cantieri temporanei o mobili?",
  "Il soggetto per conto del quale l'intera opera viene realizzata", ["L'impresa che esegue i lavori", "Il direttore dei lavori", "Il coordinatore per l'esecuzione"],
  "Art. 89, lett. b); negli appalti pubblici è il titolare del potere decisionale e di spesa.", "art. 89", "il soggetto per conto del quale l'intera opera viene realizzata")
T("lav-249", "Sicurezza sul lavoro", 3, "Cos'è un «cantiere temporaneo o mobile» secondo il D.Lgs. 81/2008?",
  "Qualunque luogo in cui si effettuano lavori edili o di ingegneria civile elencati nell'allegato X", ["Solo i cantieri con più di 10 lavoratori", "Solo i cantieri stradali", "Qualsiasi luogo di lavoro all'aperto"],
  "Art. 89, comma 1, lett. a).", "art. 89", "qualunque luogo in cui si effettuano lavori edili o di ingegneria civile")
T("lav-250", "Sicurezza sul lavoro", 3, "Nella movimentazione manuale dei carichi, qual è il primo obbligo del datore di lavoro?",
  "Evitare la movimentazione manuale, con misure organizzative e mezzi meccanici", ["Fornire cinture lombari a tutti", "Limitare i carichi a 50 kg", "Far firmare una liberatoria ai lavoratori"],
  "Art. 168: se non è evitabile, il datore deve ridurne il rischio, in particolare di patologie dorso-lombari.", "art. 168", "per evitare la necessità di una movimentazione manuale dei carichi da parte dei lavoratori")
T("lav-251", "Sicurezza sul lavoro", 4, "Con quale periodicità sono visitati i videoterminalisti idonei senza prescrizioni e con meno di 50 anni?",
  "Ogni cinque anni", ["Ogni anno", "Ogni due anni", "Ogni dieci anni"],
  "Art. 176, comma 3: la periodicità è biennale per gli idonei con prescrizioni e per chi ha compiuto 50 anni.", "art. 176", "quinquennale negli altri casi")
T("lav-252", "Sicurezza sul lavoro", 5, "A quale normativa si collega il modello di organizzazione e gestione dell'art. 30 del D.Lgs. 81/2008?",
  "Alla responsabilità amministrativa degli enti del D.Lgs. 231/2001, con efficacia esimente", ["Al codice della privacy", "Al codice dei contratti pubblici", "Al testo unico sul pubblico impiego"],
  "Se adottato ed efficacemente attuato, il modello può escludere la responsabilità dell'ente per reati in materia di sicurezza.", "art. 30", "idoneo ad avere efficacia esimente della responsabilità amministrativa delle persone giuridiche")
T("lav-253", "Sicurezza sul lavoro", 4, "Dove deve essere organizzato, prioritariamente, il servizio di prevenzione e protezione?",
  "All'interno dell'azienda o dell'unità produttiva", ["Sempre presso un consulente esterno", "Presso l'ASL competente", "Presso l'INAIL"],
  "Art. 31: in alternativa il datore può incaricare persone o servizi esterni.", "art. 31", "il datore di lavoro organizza il servizio di prevenzione e protezione")
T("lav-254", "Sicurezza sul lavoro", 3, "Gli addetti e i responsabili del servizio di prevenzione e protezione possono subire pregiudizi per l'attività svolta?",
  "No, la legge lo esclude", ["Sì, se il datore non è d'accordo con le loro proposte", "Sì, se sono esterni", "Solo se l'azienda ha meno di 15 dipendenti"],
  "Art. 31, comma 2: devono anche avere mezzi e tempo adeguati.", "art. 31", "Essi non possono subire pregiudizio a causa della attività svolta nell'espletamento del proprio incarico")
T("lav-255", "Sicurezza sul lavoro", 3, "Quale di questi è un compito del servizio di prevenzione e protezione (art. 33)?",
  "Elaborare le procedure di sicurezza per le varie attività aziendali", ["Irrogare sanzioni disciplinari", "Effettuare le visite mediche", "Firmare i contratti di appalto"],
  "Il servizio individua i rischi, propone la formazione e partecipa alla riunione periodica.", "art. 33", "ad elaborare le procedure di sicurezza per le varie attività aziendali")
T("lav-256", "Sicurezza sul lavoro", 4, "Quale di questi titoli consente di svolgere le funzioni di medico competente?",
  "La specializzazione in medicina del lavoro", ["La sola laurea in medicina", "La specializzazione in pediatria", "L'iscrizione all'albo dei medici di base"],
  "Art. 38: valgono anche altri titoli specifici, come la specializzazione in igiene e medicina preventiva o in medicina legale.", "art. 38", "specializzazione in medicina del lavoro o in medicina preventiva dei lavoratori e psicotecnica")
T("lav-257", "Sicurezza sul lavoro", 4, "Se il medico competente giudica il lavoratore inidoneo alla mansione specifica, il datore di lavoro:",
  "lo adibisce, se possibile, a mansioni equivalenti o, in mancanza, inferiori, con il trattamento delle mansioni di provenienza", ["lo licenzia per giusta causa", "lo sospende senza retribuzione", "lo trasferisce ad altra azienda"],
  "Art. 42 del D.Lgs. 81/2008, anche tenendo conto della L. 68/1999.", "art. 42", "a mansioni equivalenti o, in difetto, a mansioni inferiori garantendo il trattamento corrispondente alle mansioni di provenienza")
T("lav-258", "Sicurezza sul lavoro", 4, "Qual è il numero minimo di RLS in un'unità produttiva con 600 lavoratori?",
  "Tre", ["Uno", "Sei", "Due"],
  "Art. 47, comma 7: uno fino a 200 lavoratori, tre da 201 a 1.000, sei oltre i 1.000.", "art. 47", "tre rappresentanti nelle aziende ovvero unità produttive da 201 a 1.000 lavoratori")
T("lav-259", "Sicurezza sul lavoro", 4, "Nelle aziende con più di 15 lavoratori, come si individua il RLS?",
  "È eletto o designato dai lavoratori nell'ambito delle rappresentanze sindacali in azienda", ["Lo nomina il datore di lavoro", "Lo nomina l'ASL", "È sempre il RSPP"],
  "Art. 47, comma 4: se mancano le rappresentanze sindacali, è eletto dai lavoratori al loro interno.", "art. 47", "è eletto o designato dai lavoratori nell'ambito delle rappresentanze sindacali in azienda")
T("lav-260", "Sicurezza sul lavoro", 4, "Nei cantieri con più imprese esecutrici, quando il committente designa il coordinatore per la progettazione?",
  "Contestualmente all'affidamento dell'incarico di progettazione", ["A lavori ultimati", "Solo se lo chiede l'ASL", "Dopo l'apertura del cantiere"],
  "Art. 90, comma 3; il coordinatore per l'esecuzione va designato prima dell'affidamento dei lavori.", "art. 90", "contestualmente all'affidamento dell'incarico di progettazione, designa il coordinatore per la progettazione")
T("lav-261", "Sicurezza sul lavoro", 4, "Quale rischio specifico deve considerare il piano di sicurezza e coordinamento (PSC) nei cantieri con attività di scavo?",
  "Il possibile rinvenimento di ordigni bellici inesplosi", ["Il rischio di furto delle attrezzature", "Il rischio di ritardi nei pagamenti", "Il rischio di contenzioso con i vicini"],
  "Art. 100: il PSC comprende relazione tecnica, prescrizioni e stima dei costi della sicurezza.", "art. 100", "rinvenimento di ordigni bellici inesplosi")
T("lav-262", "Sicurezza sul lavoro", 5, "Qual è il valore limite di esposizione giornaliera al rumore (LEX) fissato dall'art. 189?",
  "87 dB(A)", ["80 dB(A)", "85 dB(A)", "90 dB(A)"],
  "80 dB(A) è il valore inferiore di azione, 85 dB(A) il valore superiore di azione.", "art. 189", "LEX = 87 dB(A)")
T("lav-263", "Sicurezza sul lavoro", 4, "Cosa devono fare i lavoratori autonomi e i componenti dell'impresa familiare secondo l'art. 21?",
  "Usare attrezzature conformi e munirsi di DPI, utilizzandoli correttamente", ["Nominare un RSPP", "Redigere il documento di valutazione dei rischi", "Eleggere un RLS"],
  "Art. 21: se operano in appalto devono anche avere una tessera di riconoscimento con fotografia.", "art. 21", "munirsi di dispositivi di protezione individuale ed utilizzarli")

# --- D.Lgs. 165/2001 (lavoro pubblico) ---
P("lav-264", "Dirigenza", 4, "Quale conseguenza ha il mancato raggiungimento degli obiettivi accertato dal sistema di valutazione per il dirigente?",
  "L'impossibilità di rinnovo dello stesso incarico", ["Il licenziamento automatico", "La riduzione dello stipendio tabellare", "Il trasferimento d'ufficio in altra regione"],
  "Art. 21: nei casi più gravi l'incarico può essere revocato o il rapporto risolto, previa contestazione.", "art. 21", "l'impossibilità di rinnovo dello stesso incarico dirigenziale")
P("lav-265", "Dirigenza", 5, "Quale quota minima della retribuzione complessiva del dirigente deve costituire il trattamento accessorio legato ai risultati?",
  "Il 30 per cento", ["Il 10 per cento", "Il 50 per cento", "Il 5 per cento"],
  "Art. 24, comma 1-bis, al netto della retribuzione individuale di anzianità e degli incarichi aggiuntivi.", "art. 24", "deve costituire almeno il 30 per cento della retribuzione complessiva del dirigente")
P("lav-266", "Mobilità", 4, "Nel passaggio diretto tra amministrazioni, quando serve l'assenso dell'amministrazione di appartenenza?",
  "Per posizioni infungibili, personale assunto da meno di tre anni o se si crea una carenza di organico oltre il 20%", ["Sempre", "Mai", "Solo per i dirigenti"],
  "Art. 30, comma 1, del D.Lgs. 165/2001.", "art. 30", "o di personale assunto da meno di tre anni")
P("lav-267", "Mobilità", 4, "Per motivate esigenze organizzative, per quanto tempo al massimo l'amministrazione di appartenenza può differire il passaggio diretto?",
  "Sessanta giorni dalla ricezione dell'istanza", ["Sei mesi", "Un anno", "Trenta giorni"],
  "Art. 30, comma 1.", "art. 30", "fino ad un massimo di sessanta giorni dalla ricezione dell'istanza")
P("lav-268", "Mobilità", 4, "Prima di avviare le procedure di assunzione, cosa devono comunicare le amministrazioni secondo l'art. 34-bis?",
  "Area, livello e sede di destinazione dei posti, per l'eventuale assegnazione di personale in disponibilità", ["L'elenco dei vincitori", "Il bilancio dell'ente", "I nomi dei commissari"],
  "La mobilità del personale in disponibilità precede il concorso.", "art. 34-bis", "prima di avviare le procedure di assunzione di personale, sono tenute a comunicare")
P("lav-269", "Reclutamento", 3, "Per le qualifiche per cui basta la scuola dell'obbligo, come avviene l'assunzione nelle PA?",
  "Mediante avviamento degli iscritti nelle liste di collocamento", ["Sempre con concorso per esami", "Per chiamata diretta del dirigente", "Per sorteggio"],
  "Art. 35, comma 1, lett. b).", "art. 35", "mediante avviamento degli iscritti nelle liste di collocamento")
P("lav-270", "Reclutamento", 4, "Come avvengono le assunzioni obbligatorie dei disabili (L. 68/1999) nelle PA?",
  "Per chiamata numerica degli iscritti nelle liste di collocamento", ["Per chiamata nominativa del sindaco", "Con concorso riservato obbligatorio", "Con sorteggio tra gli idonei"],
  "Art. 35, comma 2, previa verifica della compatibilità dell'invalidità con le mansioni.", "art. 35", "avvengono per chiamata numerica degli iscritti nelle liste di collocamento")
P("lav-271", "Reclutamento", 4, "Chi è stato condannato, anche con sentenza non definitiva, per reati contro la PA può far parte di una commissione di concorso?",
  "No, nemmeno con compiti di segreteria", ["Sì, se la pena è sospesa", "Sì, come segretario", "Sì, dopo tre anni dalla sentenza"],
  "Art. 35-bis, introdotto dalla legge anticorruzione.", "art. 35-bis", "non possono fare parte, anche con compiti di segreteria, di commissioni per l'accesso o la selezione a pubblici impieghi")
P("lav-272", "Procedimento disciplinare", 4, "Entro quanto il responsabile della struttura segnala all'UPD i fatti di rilevanza disciplinare punibili oltre il rimprovero verbale?",
  "Immediatamente e comunque entro dieci giorni", ["Entro trenta giorni", "Entro sei mesi", "Entro la fine dell'anno"],
  "Art. 55-bis, comma 4.", "art. 55-bis", "segnala immediatamente, e comunque entro dieci giorni")
P("lav-273", "Procedimento disciplinare", 4, "Entro quanto l'UPD deve contestare per iscritto l'addebito dopo la segnalazione?",
  "Non oltre trenta giorni", ["Non oltre dieci giorni", "Non oltre centoventi giorni", "Non oltre un anno"],
  "Art. 55-bis, comma 4: il termine decorre dalla segnalazione o dalla piena conoscenza dei fatti.", "art. 55-bis", "con immediatezza e comunque non oltre trenta giorni decorrenti dal ricevimento della predetta segnalazione")
P("lav-274", "Procedimento disciplinare", 4, "Quante volte il dipendente può chiedere il differimento dell'audizione per grave e oggettivo impedimento?",
  "Una sola volta", ["Due volte", "Senza limiti", "Mai"],
  "Art. 55-bis, comma 4: il termine di conclusione si proroga in misura corrispondente.", "art. 55-bis", "sia differita, per una sola volta")
P("lav-275", "Procedimento disciplinare", 5, "A chi vanno comunicati per via telematica gli atti di avvio e conclusione del procedimento disciplinare?",
  "All'Ispettorato per la funzione pubblica, entro venti giorni", ["Al Prefetto, entro cinque giorni", "All'ANAC, entro sessanta giorni", "Alla Corte dei conti, entro un anno"],
  "Art. 55-bis, comma 4: il nome del dipendente è sostituito da un codice identificativo.", "art. 55-bis", "all'Ispettorato per la funzione pubblica, entro venti giorni dalla loro adozione")
P("lav-276", "Procedimento disciplinare", 4, "Se per gli stessi fatti è in corso un procedimento penale, il procedimento disciplinare di regola:",
  "prosegue e si conclude anche in pendenza del processo penale", ["si sospende sempre", "si estingue", "è assorbito dal processo penale"],
  "Art. 55-ter: la sospensione è possibile solo per infrazioni gravi e accertamenti complessi.", "art. 55-ter", "è proseguito e concluso anche in pendenza del procedimento penale")
P("lav-277", "Procedimento disciplinare", 5, "Quando l'UPD può sospendere il procedimento disciplinare in attesa di quello penale?",
  "Per infrazioni punibili oltre la sospensione di dieci giorni, in casi complessi e senza elementi sufficienti", ["Sempre, su richiesta del dipendente", "Solo per il rimprovero verbale", "Mai"],
  "Art. 55-ter, comma 1.", "art. 55-ter", "Per le infrazioni per le quali è applicabile una sanzione superiore alla sospensione dal servizio con privazione della retribuzione fino a dieci giorni")
P("lav-278", "Licenziamento", 3, "Quale di questi comportamenti comporta comunque il licenziamento disciplinare nel pubblico impiego?",
  "L'ingiustificato rifiuto del trasferimento disposto per motivate esigenze di servizio", ["Un ritardo occasionale di dieci minuti", "La partecipazione a uno sciopero", "L'iscrizione a un sindacato"],
  "Art. 55-quater, comma 1, lett. c).", "art. 55-quater", "ingiustificato rifiuto del trasferimento disposto dall'amministrazione per motivate esigenze di servizio")
P("lav-279", "Licenziamento", 4, "Le falsità documentali commesse per ottenere l'assunzione o una progressione di carriera comportano:",
  "il licenziamento disciplinare", ["solo la revoca della progressione", "una multa", "un rimprovero scritto"],
  "Art. 55-quater, comma 1, lett. d).", "art. 55-quater", "falsità documentali o dichiarative commesse ai fini o in occasione dell'instaurazione del rapporto di lavoro")
P("lav-280", "Licenziamento", 5, "L'insufficiente rendimento porta al licenziamento se rilevato da una valutazione negativa della performance:",
  "per ciascun anno dell'ultimo triennio", ["per un solo anno", "per due mesi consecutivi", "nell'ultimo quinquennio, anche non consecutiva"],
  "Art. 55-quater, comma 1, lett. f-quinquies).", "art. 55-quater", "rilevato dalla costante valutazione negativa della performance del dipendente per ciascun anno dell'ultimo triennio")
P("lav-281", "Licenziamento", 4, "La reiterazione nell'ambiente di lavoro di gravi condotte aggressive, moleste o ingiuriose comporta:",
  "il licenziamento disciplinare", ["solo un richiamo verbale", "il trasferimento ad altro ufficio", "una sospensione di un giorno"],
  "Art. 55-quater, comma 1, lett. e).", "art. 55-quater", "reiterazione nell'ambiente di lavoro di gravi condotte aggressive o moleste o minacciose o ingiuriose")
P("lav-282", "Assenze", 4, "Cosa può fare l'amministrazione in caso di accertata permanente inidoneità psicofisica al servizio del dipendente?",
  "Risolvere il rapporto di lavoro", ["Solo ridurre lo stipendio", "Nulla, il posto è garantito", "Trasferirlo in un altro ente senza il suo consenso"],
  "Art. 55-octies: un regolamento disciplina procedura di verifica e sospensione cautelare.", "art. 55-octies", "l'amministrazione può risolvere il rapporto di lavoro")
P("lav-283", "Procedimento disciplinare", 3, "Chi è competente per il procedimento disciplinare che può concludersi con il rimprovero verbale?",
  "Il responsabile della struttura in cui presta servizio il dipendente", ["L'ufficio per i procedimenti disciplinari", "Il sindaco o il ministro", "Il giudice del lavoro"],
  "Art. 55-bis, comma 1: per il rimprovero verbale si applica la disciplina del contratto collettivo.", "art. 55-bis", "Per le infrazioni di minore gravità, per le quali è prevista l'irrogazione della sanzione del rimprovero verbale")
P("lav-284", "Procedimento disciplinare", 4, "Più amministrazioni possono gestire insieme l'ufficio per i procedimenti disciplinari?",
  "Sì, previa convenzione e senza maggiori oneri", ["No, mai", "Solo i Comuni sotto i 1.000 abitanti", "Solo con autorizzazione del Prefetto"],
  "Art. 55-bis, comma 3.", "art. 55-bis", "Le amministrazioni, previa convenzione, possono prevedere la gestione unificata delle funzioni dell'ufficio competente per i procedimenti disciplinari")
P("lav-285", "Licenziamento", 5, "Quale condanna penale definitiva comporta il licenziamento disciplinare secondo l'art. 55-quater?",
  "Quella per cui è prevista l'interdizione perpetua dai pubblici uffici o l'estinzione del rapporto", ["Qualsiasi condanna, anche per contravvenzione", "Solo la condanna all'ergastolo", "Nessuna: decide il giudice penale"],
  "Art. 55-quater, comma 1, lett. f).", "art. 55-quater", "condanna penale definitiva, in relazione alla quale è prevista l'interdizione perpetua dai pubblici uffici")
P("lav-286", "Licenziamento", 5, "La violazione reiterata degli obblighi della prestazione porta al licenziamento se ha già causato sospensioni per un totale di:",
  "oltre un anno nell'arco di un biennio", ["oltre dieci giorni in un anno", "oltre un mese nell'ultimo quinquennio", "oltre tre mesi in un anno"],
  "Art. 55-quater, comma 1, lett. f-quater).", "art. 55-quater", "della sospensione dal servizio per un periodo complessivo superiore a un anno nell'arco di un biennio")

# --- Costituzione e Statuto dei lavoratori (articoli non ancora usati) ---
K("lav-287", "Costituzione e lavoro", 1, "Come qualifica l'art. 41 della Costituzione l'iniziativa economica privata?",
  "Libera", ["Vietata nei servizi pubblici", "Subordinata all'autorizzazione dello Stato", "Riservata ai cittadini italiani"],
  "Non può però svolgersi in contrasto con l'utilità sociale o recando danno a salute, ambiente, sicurezza, libertà e dignità umana.", "art. 41", "L'iniziativa economica privata è libera")
K("lav-288", "Costituzione e lavoro", 3, "Secondo l'art. 117 della Costituzione, la «tutela e sicurezza del lavoro» è materia di:",
  "legislazione concorrente tra Stato e Regioni", ["legislazione esclusiva dello Stato", "legislazione esclusiva delle Regioni", "competenza dei contratti collettivi"],
  "Nelle materie concorrenti lo Stato fissa i principi fondamentali, le Regioni il resto.", "art. 117", "tutela e sicurezza del lavoro")
K("lav-289", "Costituzione e lavoro", 3, "A chi spetta la legislazione in materia di previdenza sociale, secondo l'art. 117?",
  "Allo Stato, in via esclusiva", ["Alle Regioni, in via esclusiva", "A Stato e Regioni in via concorrente", "All'INPS"],
  "Art. 117, secondo comma, lett. o). La previdenza complementare e integrativa è invece materia concorrente.", "art. 117", "o) previdenza sociale")
K("lav-290", "Costituzione e pubblico impiego", 3, "Per gli atti compiuti in violazione di diritti, i dipendenti pubblici secondo l'art. 28 della Costituzione sono:",
  "direttamente responsabili secondo le leggi penali, civili e amministrative", ["mai responsabili: risponde solo lo Stato", "responsabili solo se dirigenti", "responsabili solo penalmente"],
  "La responsabilità civile si estende allo Stato e agli enti pubblici.", "art. 28", "sono direttamente responsabili, secondo le leggi penali, civili e amministrative, degli atti compiuti in violazione di diritti")
K("lav-291", "Costituzione e pubblico impiego", 2, "Come devono adempiere le funzioni pubbliche i cittadini a cui sono affidate (art. 54)?",
  "Con disciplina ed onore", ["Con discrezionalità politica", "Solo secondo le direttive del partito di maggioranza", "Con riservatezza assoluta"],
  "Prestano giuramento nei casi stabiliti dalla legge.", "art. 54", "hanno il dovere di adempierle con disciplina ed onore")
K("lav-292", "Costituzione e lavoro", 2, "Come definisce la salute l'art. 32 della Costituzione?",
  "Fondamentale diritto dell'individuo e interesse della collettività", ["Diritto riservato ai lavoratori", "Interesse esclusivo dello Stato", "Dovere del cittadino verso il datore"],
  "Su questa base poggia anche la tutela della salute nei luoghi di lavoro.", "art. 32", "La Repubblica tutela la salute come fondamentale diritto dell'individuo e interesse della collettività")
S("lav-293", "Statuto dei lavoratori", 3, "Quale diritto riconosce ai lavoratori l'art. 9 dello Statuto, tramite le loro rappresentanze?",
  "Controllare l'applicazione delle norme per la prevenzione di infortuni e malattie professionali", ["Fissare l'orario di lavoro", "Scegliere i dirigenti", "Decidere le assunzioni"],
  "Possono anche promuovere ricerca e attuazione delle misure di tutela della salute.", "art. 9", "hanno diritto di controllare l'applicazione delle norme per la prevenzione degli infortuni e delle malattie professionali")
S("lav-294", "Statuto dei lavoratori", 4, "Cosa vieta l'art. 16 dello Statuto dei lavoratori?",
  "I trattamenti economici di maggior favore con carattere discriminatorio", ["Gli aumenti di merito", "I premi di produzione", "Gli straordinari"],
  "Il datore può essere condannato a versare al fondo adeguamento pensioni l'importo indebitamente corrisposto, per un massimo di un anno.", "art. 16", "È vietata la concessione di trattamenti economici di maggior favore aventi carattere discriminatorio")
S("lav-295", "Diritti sindacali", 3, "Secondo l'art. 26 dello Statuto, i lavoratori possono raccogliere contributi sindacali sul luogo di lavoro?",
  "Sì, senza pregiudicare il normale svolgimento dell'attività aziendale", ["No, mai", "Solo fuori dall'orario e fuori dall'azienda", "Solo con autorizzazione scritta del datore"],
  "Possono anche fare proselitismo; i commi sulla trattenuta in busta paga sono stati abrogati dal referendum del 1995.", "art. 26", "I lavoratori hanno diritto di raccogliere contributi e di svolgere opera di proselitismo")
S("lav-296", "Diritti sindacali", 4, "A chi spettano i permessi retribuiti dell'art. 30 dello Statuto?",
  "Ai componenti degli organi direttivi provinciali e nazionali delle associazioni sindacali", ["A tutti gli iscritti al sindacato", "Solo ai delegati RLS", "Ai lavoratori studenti"],
  "I permessi servono a partecipare alle riunioni degli organi, secondo i contratti di lavoro.", "art. 30", "I componenti degli organi direttivi, provinciali e nazionali")
S("lav-297", "Statuto dei lavoratori", 4, "Quale clausola deve contenere un appalto di opere pubbliche secondo l'art. 36 dello Statuto?",
  "L'obbligo di applicare condizioni non inferiori ai contratti collettivi di categoria e zona", ["L'obbligo di assumere solo residenti", "Il divieto di iscrizione ai sindacati", "L'obbligo di lavorare anche nei festivi"],
  "Vale anche per i benefici concessi dallo Stato agli imprenditori.", "art. 36", "condizioni non inferiori a quelle risultanti dai contratti collettivi di lavoro della categoria e della zona")
S("lav-298", "Statuto dei lavoratori", 3, "Il lavoratore eletto al Parlamento europeo può chiedere l'aspettativa ai sensi dell'art. 31 dello Statuto?",
  "Sì, aspettativa non retribuita per la durata del mandato", ["No, solo per il Parlamento nazionale", "Sì, ma retribuita dal datore", "Solo se il datore è pubblico"],
  "L'art. 31 vale per Parlamento nazionale ed europeo, assemblee regionali e altre funzioni pubbliche elettive.", "art. 31", "del Parlamento europeo o di assemblee regionali")
C("lav-299", "Contratti a termine", 4, "Senza nessuna delle condizioni dell'art. 19, comma 1, un contratto a termine può essere prorogato oltre i primi dodici mesi?",
  "No: oltre i 12 mesi serve una delle condizioni, altrimenti diventa a tempo indeterminato", ["Sì, liberamente fino a 36 mesi", "Sì, con il solo consenso del lavoratore", "Sì, se il datore paga una maggiorazione"],
  "Art. 21, comma 01; i contratti per attività stagionali fanno eccezione.", "art. 21", "Il contratto può essere prorogato e rinnovato liberamente nei primi dodici mesi")
C("lav-300", "Somministrazione", 4, "La somministrazione di lavoro è vietata presso unità produttive in cui, nei sei mesi precedenti, vi sono stati:",
  "licenziamenti collettivi per le stesse mansioni", ["nuove assunzioni a tempo indeterminato", "promozioni del personale", "cambi del contratto collettivo"],
  "Art. 32, comma 1, lett. b), con eccezioni per sostituzione di assenti o durata iniziale fino a tre mesi.", "art. 32", "presso unità produttive nelle quali si è proceduto, entro i sei mesi precedenti, a licenziamenti collettivi")
C("lav-301", "Somministrazione", 5, "Se la somministrazione avviene oltre i limiti di legge, cosa può chiedere il lavoratore?",
  "La costituzione di un rapporto alle dipendenze dell'utilizzatore dall'inizio della somministrazione", ["Solo un'indennità di 6 mensilità", "Il trasferimento a un'altra agenzia", "Nulla: risponde solo l'agenzia"],
  "Art. 38, comma 2: la domanda può essere rivolta anche solo all'utilizzatore.", "art. 38", "il lavoratore può chiedere, anche soltanto nei confronti dell'utilizzatore, la costituzione di un rapporto di lavoro alle dipendenze di quest'ultimo")
