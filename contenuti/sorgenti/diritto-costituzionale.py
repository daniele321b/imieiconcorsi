# Diritto costituzionale — fonte: Costituzione della Repubblica Italiana (testo vigente, Normattiva).
# D(id, argomento, livello, testo, giusta, [sbagliate], spiegazione, fonte, file, frase_prova)
C = "norma_Costituzione.txt"

D("cost-001", "Principi fondamentali", 1, "Secondo l'art. 1 della Costituzione, a chi appartiene la sovranità?",
  "Al popolo", ["Al Parlamento", "Al Presidente della Repubblica", "Allo Stato"],
  "L'art. 1 afferma che la sovranità appartiene al popolo, che la esercita nelle forme e nei limiti della Costituzione.",
  "Costituzione, art. 1", C, "La sovranità appartiene al popolo, che la esercita nelle forme e nei limiti della Costituzione")

D("cost-002", "Principi fondamentali", 1, "L'Italia, secondo l'art. 1 della Costituzione, è una Repubblica democratica fondata:",
  "sul lavoro", ["sulla famiglia", "sulla libertà", "sulla solidarietà"],
  "Il primo comma dell'art. 1 recita: «L'Italia è una Repubblica democratica, fondata sul lavoro».",
  "Costituzione, art. 1", C, "L'Italia è una Repubblica democratica, fondata sul lavoro")

D("cost-003", "Principi fondamentali", 2, "Il principio di eguaglianza sostanziale, che impegna la Repubblica a rimuovere gli ostacoli di ordine economico e sociale, è previsto:",
  "dal secondo comma dell'art. 3", ["dal primo comma dell'art. 3", "dall'art. 2", "dall'art. 4"],
  "Il primo comma dell'art. 3 sancisce l'eguaglianza formale; il secondo comma l'eguaglianza sostanziale, con il compito di rimuovere gli ostacoli che la limitano.",
  "Costituzione, art. 3", C, "È compito della Repubblica rimuovere gli ostacoli di ordine economico e sociale")

D("cost-004", "Principi fondamentali", 2, "Come descrive l'art. 12 della Costituzione la bandiera della Repubblica?",
  "Tricolore verde, bianco e rosso, a tre bande verticali di eguali dimensioni",
  ["Tricolore verde, bianco e rosso, a tre bande orizzontali", "Tricolore rosso, bianco e verde, a bande verticali di larghezza diversa", "La Costituzione non descrive la bandiera"],
  "L'art. 12 fissa colori, ordine e forma: bande verticali di eguali dimensioni.",
  "Costituzione, art. 12", C, "a tre bande verticali di eguali dimensioni")

D("cost-005", "Principi fondamentali", 2, "Secondo l'art. 7 della Costituzione, i rapporti tra Stato e Chiesa cattolica sono regolati:",
  "dai Patti Lateranensi", ["dal Concordato di Worms", "da una legge costituzionale del 1948", "dallo Statuto Albertino"],
  "L'art. 7 dichiara Stato e Chiesa indipendenti e sovrani, ciascuno nel proprio ordine, e rinvia ai Patti Lateranensi.",
  "Costituzione, art. 7", C, "I loro rapporti sono regolati dai Patti Lateranensi")

D("cost-006", "Principi fondamentali", 3, "Dopo la riforma costituzionale del 2022, l'art. 9 tutela anche:",
  "l'ambiente, la biodiversità e gli ecosistemi, anche nell'interesse delle future generazioni",
  ["il diritto alla connessione a internet", "la parità di genere nelle cariche elettive", "il diritto allo sport"],
  "La legge costituzionale 1/2022 ha aggiunto all'art. 9 la tutela di ambiente, biodiversità ed ecosistemi.",
  "Costituzione, art. 9", C, "Tutela l'ambiente, la biodiversità e gli ecosistemi, anche nell'interesse delle future generazioni")

D("cost-007", "Principi fondamentali", 1, "Che cosa afferma l'art. 11 della Costituzione a proposito della guerra?",
  "L'Italia ripudia la guerra come strumento di offesa alla libertà degli altri popoli",
  ["L'Italia può dichiarare guerra solo con referendum", "L'Italia ammette la guerra solo se decisa dall'ONU", "L'Italia rinuncia a dotarsi di forze armate"],
  "L'art. 11 ripudia la guerra come strumento di offesa e come mezzo di risoluzione delle controversie internazionali.",
  "Costituzione, art. 11", C, "L'Italia ripudia la guerra come strumento di offesa alla libertà degli altri popoli")

D("cost-008", "Diritti e libertà", 3, "In caso di fermo da parte dell'autorità di pubblica sicurezza, entro quanto tempo il provvedimento va comunicato all'autorità giudiziaria?",
  "Entro 48 ore", ["Entro 24 ore", "Entro 72 ore", "Entro 5 giorni"],
  "Art. 13: i provvedimenti provvisori vanno comunicati entro 48 ore all'autorità giudiziaria; se questa non li convalida nelle successive 48 ore, si intendono revocati.",
  "Costituzione, art. 13", C, "devono essere comunicati entro quarantotto ore all'autorità giudiziaria")

D("cost-009", "Diritti e libertà", 2, "Secondo l'art. 21 della Costituzione, la stampa:",
  "non può essere soggetta ad autorizzazioni o censure", ["è soggetta ad autorizzazione del Ministero dell'interno", "può essere censurata dal Governo in caso di necessità", "è sottoposta al controllo preventivo del Garante"],
  "L'art. 21 tutela la libertà di manifestazione del pensiero e vieta autorizzazioni o censure sulla stampa.",
  "Costituzione, art. 21", C, "La stampa non può essere soggetta ad autorizzazioni o censure")

D("cost-010", "Diritti e libertà", 1, "Che cosa stabilisce l'art. 27 della Costituzione sulla pena di morte?",
  "Non è ammessa", ["È ammessa solo in tempo di guerra", "È ammessa per i reati più gravi", "È ammessa solo con referendum"],
  "L'art. 27 afferma che la responsabilità penale è personale e che non è ammessa la pena di morte.",
  "Costituzione, art. 27", C, "Non è ammessa la pena di morte")

D("cost-011", "Diritti e libertà", 2, "Secondo l'art. 27, l'imputato è considerato:",
  "non colpevole sino alla condanna definitiva", ["colpevole fino a prova contraria", "non colpevole fino alla sentenza di primo grado", "innocente solo se assolto in appello"],
  "La presunzione di non colpevolezza dura fino alla condanna definitiva.",
  "Costituzione, art. 27", C, "L'imputato non è considerato colpevole sino alla condanna definitiva")

D("cost-012", "Rapporti economici", 2, "Secondo l'art. 36, il lavoratore può rinunciare alle ferie annuali retribuite?",
  "No, non può rinunciarvi", ["Sì, se lo concorda con il datore di lavoro", "Sì, in cambio di un compenso", "Solo nei contratti a termine"],
  "L'art. 36 riconosce il diritto al riposo settimanale e a ferie annuali retribuite, a cui il lavoratore non può rinunziare.",
  "Costituzione, art. 36", C, "e a ferie annuali retribuite, e non può rinunziarvi")

D("cost-013", "Rapporti politici", 1, "Secondo l'art. 48, il voto è:",
  "personale ed eguale, libero e segreto", ["personale, palese e obbligatorio", "libero ma delegabile", "segreto solo per le elezioni politiche"],
  "L'art. 48 definisce le caratteristiche del voto e lo qualifica come dovere civico.",
  "Costituzione, art. 48", C, "Il voto è personale ed eguale, libero e segreto")

D("cost-014", "Parlamento", 2, "Quanti sono i deputati dopo la riduzione del numero dei parlamentari?",
  "400", ["630", "315", "600"],
  "L'art. 56, modificato dalla legge costituzionale 1/2020, fissa il numero dei deputati a quattrocento, di cui otto eletti nella circoscrizione Estero.",
  "Costituzione, art. 56", C, "Il numero dei deputati è di ((quattrocento))")

D("cost-015", "Parlamento", 2, "Quanti senatori sono eletti a suffragio universale e diretto?",
  "200", ["315", "100", "400"],
  "L'art. 57, dopo la riforma del 2020, fissa i senatori elettivi a duecento, di cui quattro eletti nella circoscrizione Estero.",
  "Costituzione, art. 57", C, "Il numero dei senatori elettivi è di ((duecento))")

D("cost-016", "Parlamento", 2, "Qual è l'età minima per essere eletti deputati?",
  "25 anni", ["18 anni", "21 anni", "40 anni"],
  "Art. 56: sono eleggibili a deputati gli elettori che nel giorno delle elezioni hanno compiuto i venticinque anni di età.",
  "Costituzione, art. 56", C, "i venticinque anni di età")

D("cost-017", "Parlamento", 3, "Qual è l'età minima per essere eletti senatori?",
  "40 anni", ["25 anni", "30 anni", "50 anni"],
  "Art. 58: sono eleggibili a senatori gli elettori che hanno compiuto il quarantesimo anno.",
  "Costituzione, art. 58", C, "che hanno compiuto il quarantesimo anno")

D("cost-018", "Parlamento", 1, "Quanto dura la legislatura di ciascuna Camera?",
  "Cinque anni", ["Quattro anni", "Sei anni", "Sette anni"],
  "Art. 60: la Camera dei deputati e il Senato della Repubblica sono eletti per cinque anni.",
  "Costituzione, art. 60", C, "sono eletti per cinque anni")

D("cost-019", "Parlamento", 4, "Quanti senatori a vita può nominare, al massimo, il Presidente della Repubblica?",
  "In tutto non più di cinque in carica contemporaneamente", ["Cinque per ogni mandato presidenziale", "Tre", "Nessuno: sono senatori a vita solo gli ex Presidenti"],
  "Art. 59, come modificato nel 2020: il numero complessivo dei senatori in carica nominati dal Presidente non può in alcun caso essere superiore a cinque.",
  "Costituzione, art. 59", C, "non può in alcun caso essere superiore a cinque")

D("cost-020", "Parlamento", 3, "Che cosa significa che ogni membro del Parlamento esercita le sue funzioni «senza vincolo di mandato»?",
  "Non è obbligato a seguire istruzioni di elettori o partiti", ["Non può essere rieletto", "Non può cambiare gruppo parlamentare", "Non ha un'indennità fissata dalla legge"],
  "L'art. 67 stabilisce che ogni parlamentare rappresenta la Nazione ed esercita le sue funzioni senza vincolo di mandato.",
  "Costituzione, art. 67", C, "esercita le sue funzioni senza vincolo di mandato")

D("cost-021", "Formazione delle leggi", 2, "Quante firme di elettori servono per presentare una proposta di legge di iniziativa popolare?",
  "Almeno 50.000", ["Almeno 500.000", "Almeno 100.000", "Almeno 5.000"],
  "Art. 71: il popolo esercita l'iniziativa delle leggi mediante la proposta di un progetto redatto in articoli da parte di almeno cinquantamila elettori.",
  "Costituzione, art. 71", C, "da parte di almeno cinquantamila elettori")

D("cost-022", "Formazione delle leggi", 3, "Chi può chiedere un referendum abrogativo?",
  "500.000 elettori o cinque Consigli regionali", ["50.000 elettori o tre Consigli regionali", "Un quinto dei parlamentari", "Il Presidente della Repubblica"],
  "L'art. 75 attribuisce la richiesta a cinquecentomila elettori o a cinque Consigli regionali.",
  "Costituzione, art. 75", C, "quando lo richiedono cinquecentomila elettori o cinque Consigli regionali")

D("cost-023", "Formazione delle leggi", 4, "Per quale di queste leggi NON è ammesso il referendum abrogativo?",
  "Le leggi tributarie e di bilancio", ["Le leggi sulla caccia", "Le leggi elettorali", "Le leggi sul divorzio"],
  "L'art. 75 esclude il referendum per leggi tributarie e di bilancio, di amnistia e di indulto, e di autorizzazione a ratificare trattati internazionali.",
  "Costituzione, art. 75", C, "Non è ammesso il referendum per le leggi tributarie e di bilancio")

D("cost-024", "Formazione delle leggi", 4, "Quando è approvata la proposta sottoposta a referendum abrogativo?",
  "Se partecipa la maggioranza degli aventi diritto e si raggiunge la maggioranza dei voti validi",
  ["Se si raggiunge la maggioranza dei voti validi, qualunque sia l'affluenza", "Se votano almeno due terzi degli aventi diritto", "Se partecipa almeno un terzo degli elettori"],
  "Art. 75: la proposta è approvata se ha partecipato alla votazione la maggioranza degli aventi diritto e se è raggiunta la maggioranza dei voti validamente espressi.",
  "Costituzione, art. 75", C, "se ha partecipato alla votazione la maggioranza degli aventi diritto")

D("cost-025", "Fonti del diritto", 2, "Entro quanti giorni dalla pubblicazione il decreto-legge deve essere convertito in legge?",
  "60 giorni", ["30 giorni", "90 giorni", "45 giorni"],
  "Art. 77: i decreti perdono efficacia sin dall'inizio se non sono convertiti in legge entro sessanta giorni dalla loro pubblicazione.",
  "Costituzione, art. 77", C, "entro sessanta giorni dalla loro pubblicazione")

D("cost-026", "Fonti del diritto", 4, "Con quale maggioranza sono approvate le leggi di amnistia e di indulto?",
  "Due terzi dei componenti di ciascuna Camera, in ogni articolo e nella votazione finale",
  ["Maggioranza semplice dei presenti", "Maggioranza assoluta dei componenti in seduta comune", "Tre quinti dei componenti di ciascuna Camera"],
  "L'art. 79 richiede la maggioranza dei due terzi dei componenti di ciascuna Camera, in ogni suo articolo e nella votazione finale.",
  "Costituzione, art. 79", C, "maggioranza dei due terzi dei componenti di ciascuna Camera")

D("cost-027", "Presidente della Repubblica", 2, "Chi elegge il Presidente della Repubblica?",
  "Il Parlamento in seduta comune, integrato dai delegati regionali", ["I cittadini con voto diretto", "Il Senato su proposta del Governo", "I Consigli regionali"],
  "Art. 83: il Presidente è eletto dal Parlamento in seduta comune dei suoi membri, con tre delegati per ogni Regione (uno per la Valle d'Aosta).",
  "Costituzione, art. 83", C, "Il Presidente della Repubblica è eletto dal Parlamento in seduta comune dei suoi membri")

D("cost-028", "Presidente della Repubblica", 3, "Dopo quale scrutinio per eleggere il Presidente della Repubblica basta la maggioranza assoluta?",
  "Dopo il terzo scrutinio", ["Dopo il secondo scrutinio", "Dopo il quarto scrutinio", "Fin dal primo scrutinio"],
  "Art. 83: nei primi tre scrutini serve la maggioranza di due terzi dell'assemblea; dopo il terzo è sufficiente la maggioranza assoluta.",
  "Costituzione, art. 83", C, "Dopo il terzo scrutinio è sufficiente la maggioranza assoluta")

D("cost-029", "Presidente della Repubblica", 1, "Qual è l'età minima per essere eletti Presidente della Repubblica?",
  "50 anni", ["40 anni", "45 anni", "35 anni"],
  "Art. 84: può essere eletto ogni cittadino che abbia compiuto cinquanta anni d'età e goda dei diritti civili e politici.",
  "Costituzione, art. 84", C, "abbia compiuto cinquanta anni d'età")

D("cost-030", "Presidente della Repubblica", 1, "Per quanti anni è eletto il Presidente della Repubblica?",
  "Sette", ["Cinque", "Sei", "Nove"],
  "Art. 85: il Presidente della Repubblica è eletto per sette anni.",
  "Costituzione, art. 85", C, "Il Presidente della Repubblica è eletto per sette anni")

D("cost-031", "Presidente della Repubblica", 2, "Chi esercita le funzioni del Presidente della Repubblica se questi non può adempierle?",
  "Il Presidente del Senato", ["Il Presidente della Camera", "Il Presidente del Consiglio dei ministri", "Il Presidente della Corte costituzionale"],
  "Art. 86: le funzioni sono esercitate dal Presidente del Senato in ogni caso in cui il Presidente della Repubblica non possa adempierle.",
  "Costituzione, art. 86", C, "sono esercitate dal Presidente del Senato")

D("cost-032", "Presidente della Repubblica", 3, "In quale periodo il Presidente della Repubblica non può sciogliere le Camere (il cosiddetto «semestre bianco»)?",
  "Negli ultimi sei mesi del suo mandato", ["Nei primi sei mesi del suo mandato", "Nei sei mesi successivi alle elezioni", "Durante lo stato di guerra"],
  "L'art. 88 vieta lo scioglimento negli ultimi sei mesi del mandato, salvo che coincidano in tutto o in parte con gli ultimi sei mesi della legislatura.",
  "Costituzione, art. 88", C, "Non può esercitare tale facoltà negli ultimi sei mesi del suo mandato")

D("cost-033", "Presidente della Repubblica", 3, "Per quali atti compiuti nell'esercizio delle sue funzioni il Presidente della Repubblica è responsabile?",
  "Solo per alto tradimento o attentato alla Costituzione", ["Per tutti i reati comuni", "Per nessun atto, in nessun caso", "Solo per gli atti non controfirmati"],
  "L'art. 90 esclude la responsabilità del Presidente per gli atti nell'esercizio delle funzioni, tranne alto tradimento e attentato alla Costituzione.",
  "Costituzione, art. 90", C, "tranne che per alto tradimento o per attentato alla Costituzione")

D("cost-034", "Governo", 2, "Entro quanto tempo dalla sua formazione il Governo deve presentarsi alle Camere per ottenere la fiducia?",
  "Entro dieci giorni", ["Entro trenta giorni", "Entro cinque giorni", "Entro sessanta giorni"],
  "Art. 94: entro dieci giorni dalla sua formazione il Governo si presenta alle Camere per ottenerne la fiducia.",
  "Costituzione, art. 94", C, "Entro dieci giorni dalla sua formazione il Governo si presenta alle Camere")

D("cost-035", "Governo", 4, "Da quanti componenti della Camera deve essere firmata la mozione di sfiducia?",
  "Almeno un decimo", ["Almeno un quinto", "Almeno un terzo", "La maggioranza assoluta"],
  "Art. 94: la mozione di sfiducia deve essere firmata da almeno un decimo dei componenti della Camera e non può essere messa in discussione prima di tre giorni dalla presentazione.",
  "Costituzione, art. 94", C, "almeno un decimo dei componenti della Camera")

D("cost-036", "Magistratura", 3, "Chi presiede il Consiglio superiore della magistratura?",
  "Il Presidente della Repubblica", ["Il Ministro della giustizia", "Il Primo presidente della Corte di cassazione", "Il Presidente della Corte costituzionale"],
  "Art. 104: il CSM è presieduto dal Presidente della Repubblica; ne fanno parte di diritto il primo presidente e il procuratore generale della Cassazione.",
  "Costituzione, art. 104", C, "Il Consiglio superiore della magistratura è presieduto dal Presidente della Repubblica")

D("cost-037", "Ordinamento della Repubblica", 2, "Quali enti costituiscono la Repubblica secondo l'art. 114 della Costituzione?",
  "Comuni, Province, Città metropolitane, Regioni e Stato", ["Solo lo Stato e le Regioni", "Stato, Regioni e Comuni", "Stato, Regioni, Province e Comunità montane"],
  "L'art. 114, riscritto nel 2001, elenca gli enti che costituiscono la Repubblica, partendo dai Comuni.",
  "Costituzione, art. 114", C, "La Repubblica è costituita dai Comuni, dalle Province, dalle Città metropolitane, dalle Regioni e dallo Stato")

D("cost-038", "Corte costituzionale", 2, "Per quanti anni sono nominati i giudici della Corte costituzionale?",
  "Nove anni", ["Sette anni", "Dodici anni", "Cinque anni"],
  "Art. 135: i giudici sono nominati per nove anni, decorrenti dal giorno del giuramento, e non possono essere nuovamente nominati.",
  "Costituzione, art. 135", C, "I giudici della Corte costituzionale sono nominati per nove anni")

D("cost-039", "Corte costituzionale", 4, "Da quando una norma di legge dichiarata incostituzionale cessa di avere efficacia?",
  "Dal giorno successivo alla pubblicazione della decisione", ["Dal giorno della sentenza", "Dopo sessanta giorni dalla pubblicazione", "Dall'abrogazione da parte del Parlamento"],
  "Art. 136: la norma cessa di avere efficacia dal giorno successivo alla pubblicazione della decisione della Corte.",
  "Costituzione, art. 136", C, "cessa di avere efficacia dal giorno successivo alla pubblicazione della decisione")

D("cost-040", "Revisione costituzionale", 5, "Una legge di revisione costituzionale approvata in seconda votazione da ciascuna Camera con la maggioranza dei due terzi dei componenti:",
  "non può essere sottoposta a referendum", ["deve essere sempre sottoposta a referendum", "può essere sottoposta a referendum su richiesta di 50.000 elettori", "entra in vigore solo dopo il parere della Corte costituzionale"],
  "Art. 138: il referendum non si fa se la legge è stata approvata nella seconda votazione da ciascuna Camera a maggioranza di due terzi dei suoi componenti.",
  "Costituzione, art. 138", C, "Non si fa luogo a referendum se la legge è stata approvata nella seconda votazione")

D("cost-041", "Revisione costituzionale", 3, "Quale elemento, secondo l'art. 139, non può essere oggetto di revisione costituzionale?",
  "La forma repubblicana", ["Il numero dei parlamentari", "La durata del mandato presidenziale", "L'elenco delle Regioni"],
  "L'art. 139 è il limite espresso alla revisione: la forma repubblicana non può essere oggetto di revisione costituzionale.",
  "Costituzione, art. 139", C, "La forma repubblicana non può essere oggetto di revisione costituzionale")

D("cost-042", "Revisione costituzionale", 5, "Chi può chiedere il referendum su una legge costituzionale approvata con maggioranza inferiore ai due terzi?",
  "Un quinto dei membri di una Camera, 500.000 elettori o cinque Consigli regionali",
  ["Solo il Presidente della Repubblica", "Un decimo dei membri di ciascuna Camera", "Un milione di elettori"],
  "Art. 138: il referendum può essere chiesto entro tre mesi dalla pubblicazione da un quinto dei membri di una Camera o da cinquecentomila elettori o da cinque Consigli regionali.",
  "Costituzione, art. 138", C, "ne facciano domanda un quinto dei membri di una Camera o cinquecentomila elettori o cinque Consigli regionali")

D("cost-043", "Storia costituzionale", 1, "Quando è entrata in vigore la Costituzione?",
  "Il 1° gennaio 1948", ["Il 2 giugno 1946", "Il 27 dicembre 1947", "Il 25 aprile 1945"],
  "La disposizione transitoria XVIII fissa l'entrata in vigore al 1° gennaio 1948; la promulgazione era avvenuta il 27 dicembre 1947.",
  "Costituzione, disp. trans. XVIII", C, "ed entra in vigore il 1° gennaio 1948")

D("cost-044", "Principi fondamentali", 5, "Un comune vuole introdurre una «lingua ufficiale locale» che sostituisca l'italiano negli atti. Quale principio costituzionale lo esclude, pur tutelando le minoranze?",
  "L'art. 6 tutela le minoranze linguistiche con apposite norme, ma resta nell'unità della Repubblica (art. 5)",
  ["L'art. 21 sulla libertà di stampa", "L'art. 33 sulla libertà di insegnamento", "Nessuno: i comuni sono liberi di scegliere la lingua"],
  "L'art. 6 affida alla Repubblica la tutela delle minoranze linguistiche con apposite norme; l'art. 5 afferma la Repubblica una e indivisibile. Non è il singolo comune a stabilire la lingua degli atti.",
  "Costituzione, artt. 5 e 6", C, "La Repubblica tutela con apposite norme le minoranze linguistiche")

# ===== Blocco 2 (ottobre 2026): ampliamento a 200 domande =====
def K(id, arg, liv, testo, giusta, sbagliate, spieg, art, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, f"Costituzione, {art}", C, frase)

K("cost-045", "Principi fondamentali", 2, "Secondo l'art. 2, quali doveri la Repubblica richiede di adempiere?",
  "I doveri inderogabili di solidarietà politica, economica e sociale", ["I doveri di fedeltà al Governo", "I doveri fiscali verso lo Stato", "I doveri di difesa armata"],
  "L'art. 2 riconosce i diritti inviolabili e richiede i doveri inderogabili di solidarietà.", "art. 2", "richiede l'adempimento dei doveri inderogabili di solidarietà politica, economica e sociale")
K("cost-046", "Principi fondamentali", 2, "L'art. 4 riconosce a tutti i cittadini il diritto:",
  "al lavoro", ["alla proprietà", "all'abitazione", "al reddito minimo"],
  "La Repubblica riconosce il diritto al lavoro e promuove le condizioni che lo rendano effettivo.", "art. 4", "riconosce a tutti i cittadini il diritto al lavoro")
K("cost-047", "Principi fondamentali", 2, "Secondo l'art. 5, la Repubblica è:",
  "una e indivisibile, e riconosce e promuove le autonomie locali", ["federale", "una e centralizzata, senza autonomie", "divisa in Stati regionali sovrani"],
  "L'art. 5 unisce unità della Repubblica e valorizzazione delle autonomie locali e del decentramento.", "art. 5", "La Repubblica, una e indivisibile, riconosce e promuove le autonomie locali")
K("cost-048", "Principi fondamentali", 3, "Le modificazioni dei Patti Lateranensi accettate da Stato e Chiesa richiedono una revisione costituzionale?",
  "No, non richiedono procedimento di revisione costituzionale", ["Sì, sempre", "Sì, con referendum", "Solo se riguardano l'insegnamento"],
  "L'art. 7 esclude la revisione costituzionale per modifiche dei Patti accettate dalle due parti.", "art. 7", "non richiedono procedimento di revisione costituzionale")
K("cost-049", "Principi fondamentali", 3, "Come sono regolati i rapporti tra lo Stato e le confessioni religiose diverse dalla cattolica?",
  "Per legge sulla base di intese con le relative rappresentanze", ["Con i Patti Lateranensi", "Con trattati internazionali", "Con decreto del Ministro dell'interno"],
  "Art. 8: le confessioni acattoliche si organizzano con propri statuti e i rapporti con lo Stato sono regolati per legge sulla base di intese.", "art. 8", "sono regolati per legge sulla base di intese con le relative rappresentanze")
K("cost-050", "Principi fondamentali", 3, "Dopo la riforma del 2022, l'art. 9 affida alla legge dello Stato la disciplina della tutela:",
  "degli animali", ["delle lingue regionali", "dei dati personali", "dei consumatori"],
  "La L. cost. 1/2022 ha aggiunto che la legge dello Stato disciplina modi e forme di tutela degli animali.", "art. 9", "La legge dello Stato disciplina i modi e le forme di tutela degli animali")
K("cost-051", "Principi fondamentali", 3, "Lo straniero a cui nel suo paese è impedito l'esercizio delle libertà democratiche ha diritto:",
  "d'asilo nel territorio della Repubblica, alle condizioni di legge", ["alla cittadinanza italiana automatica", "a un permesso di lavoro illimitato", "solo a un soggiorno di transito"],
  "Art. 10: diritto d'asilo secondo le condizioni stabilite dalla legge.", "art. 10", "ha diritto d'asilo nel territorio della Repubblica")
K("cost-052", "Principi fondamentali", 4, "È ammessa l'estradizione dello straniero per reati politici?",
  "No, salvo che per i delitti di genocidio", ["Sì, sempre", "Sì, se lo chiede l'ONU", "Solo per i cittadini UE"],
  "L'art. 10 la esclude per reati politici; la L. cost. 1/1967 ha previsto che il divieto non si applica ai delitti di genocidio.", "art. 10", "Non è ammessa l'estradizione dello straniero per reati politici")
K("cost-053", "Principi fondamentali", 3, "A quali condizioni l'art. 11 consente limitazioni di sovranità?",
  "In condizioni di parità con gli altri Stati, per un ordinamento che assicuri la pace e la giustizia", ["Su richiesta di qualunque Stato alleato", "Solo in caso di guerra", "Mai"],
  "L'art. 11 è la base costituzionale della partecipazione all'ONU e all'Unione europea.", "art. 11", "consente, in condizioni di parità con gli altri Stati, alle limitazioni di sovranità")
K("cost-054", "Diritti e libertà", 2, "Il domicilio, secondo l'art. 14, è:",
  "inviolabile", ["sempre ispezionabile dalla polizia", "tutelato solo se di proprietà", "inviolabile solo di notte"],
  "Ispezioni, perquisizioni e sequestri sono ammessi solo nei casi e modi stabiliti dalla legge.", "art. 14", "Il domicilio è inviolabile")
K("cost-055", "Diritti e libertà", 2, "Chi può limitare la libertà e la segretezza della corrispondenza?",
  "Solo l'autorità giudiziaria con atto motivato", ["La polizia senza autorizzazione", "Il sindaco", "Il datore di lavoro"],
  "Art. 15: la limitazione può avvenire soltanto per atto motivato dell'autorità giudiziaria.", "art. 15", "La loro limitazione può avvenire soltanto per atto motivato dell'autorità giudiziaria")
K("cost-056", "Diritti e libertà", 3, "La libertà di circolazione può essere limitata per ragioni politiche?",
  "No, nessuna restrizione può essere determinata da ragioni politiche", ["Sì, con decreto del Governo", "Sì, in periodo elettorale", "Solo per i dipendenti pubblici"],
  "Art. 16: limiti solo in via generale per sanità o sicurezza.", "art. 16", "Nessuna restrizione può essere determinata da ragioni politiche")
K("cost-057", "Diritti e libertà", 3, "Per una riunione in luogo pubblico, cosa prevede l'art. 17?",
  "Deve essere dato preavviso alle autorità", ["Serve l'autorizzazione del prefetto", "Non serve nulla", "Serve il permesso del sindaco"],
  "Per le riunioni in luogo aperto al pubblico non serve preavviso; per quelle in luogo pubblico sì, e possono essere vietate solo per comprovati motivi di sicurezza o incolumità.", "art. 17", "Delle riunioni in luogo pubblico deve essere dato preavviso alle autorità")
K("cost-058", "Diritti e libertà", 2, "Per le riunioni in luogo aperto al pubblico è richiesto il preavviso?",
  "No, non è richiesto", ["Sì, sempre", "Sì, almeno tre giorni prima", "Solo oltre cento partecipanti"],
  "Art. 17: il preavviso serve solo per le riunioni in luogo pubblico.", "art. 17", "Per le riunioni, anche in luogo aperto al pubblico, non è richiesto preavviso")
K("cost-059", "Diritti e libertà", 3, "Quali associazioni sono vietate dall'art. 18?",
  "Le associazioni segrete e quelle con scopi politici perseguiti mediante organizzazioni di carattere militare", ["Tutte le associazioni non registrate", "Le associazioni religiose", "I sindacati non riconosciuti"],
  "La libertà di associazione non richiede autorizzazione, ma sono proibite associazioni segrete e paramilitari.", "art. 18", "Sono proibite le associazioni segrete")
K("cost-060", "Diritti e libertà", 2, "Quale limite pone l'art. 19 alla libertà di culto?",
  "Che non si tratti di riti contrari al buon costume", ["Che si svolga solo in luoghi autorizzati", "Che sia una religione riconosciuta", "Nessun limite"],
  "Art. 19: tutti possono professare la propria fede, purché non con riti contrari al buon costume.", "art. 19", "purché non si tratti di riti contrari al buon costume")
K("cost-061", "Diritti e libertà", 4, "In caso di sequestro urgente di stampa periodica da parte della polizia giudiziaria, entro quanto deve essere fatta denuncia all'autorità giudiziaria?",
  "Immediatamente, e non oltre 24 ore", ["Entro 48 ore", "Entro 5 giorni", "Entro un mese"],
  "Art. 21: denuncia entro 24 ore; senza convalida nelle 24 ore successive il sequestro è revocato.", "art. 21", "immediatamente, e non mai oltre ventiquattro ore")
K("cost-062", "Diritti e libertà", 2, "Per motivi politici, si può essere privati della cittadinanza?",
  "No: nessuno può essere privato per motivi politici della capacità giuridica, della cittadinanza, del nome", ["Sì, con decreto del Presidente della Repubblica", "Sì, con sentenza penale", "Solo in tempo di guerra"],
  "L'art. 22 vieta queste privazioni per motivi politici.", "art. 22", "Nessuno può essere privato, per motivi politici, della capacità giuridica, della cittadinanza, del nome")
K("cost-063", "Diritti e libertà", 3, "Quale principio fissa l'art. 23 («Nessuna prestazione personale o patrimoniale può essere imposta se non in base alla legge»)?",
  "La riserva di legge per le prestazioni imposte", ["Il principio di progressività", "La libertà d'impresa", "Il principio di sussidiarietà"],
  "Tributi e altre prestazioni imposte richiedono una base legislativa.", "art. 23", "Nessuna prestazione personale o patrimoniale può essere imposta se non in base alla legge")
K("cost-064", "Diritti e libertà", 2, "Secondo l'art. 24, la difesa è:",
  "diritto inviolabile in ogni stato e grado del procedimento", ["un diritto solo nel processo penale", "un servizio a pagamento", "garantita solo in appello"],
  "L'art. 24 garantisce anche ai non abbienti i mezzi per agire e difendersi.", "art. 24", "La difesa è diritto inviolabile in ogni stato e grado del procedimento")
K("cost-065", "Diritti e libertà", 3, "Il principio del «giudice naturale precostituito per legge» è sancito:",
  "dall'art. 25", ["dall'art. 101", "dall'art. 111", "dall'art. 13"],
  "L'art. 25 afferma che nessuno può essere distolto dal giudice naturale precostituito per legge.", "art. 25", "Nessuno può essere distolto dal giudice naturale precostituito per legge")
K("cost-066", "Diritti e libertà", 3, "L'irretroattività della legge penale è garantita dall'art. 25, secondo cui nessuno può essere punito:",
  "se non in forza di una legge entrata in vigore prima del fatto commesso", ["se non con sentenza di Cassazione", "senza il parere della Corte costituzionale", "se non dopo tre gradi di giudizio"],
  "È il principio di legalità e irretroattività della norma penale.", "art. 25", "Nessuno può essere punito se non in forza di una legge che sia entrata in vigore prima del fatto commesso")
K("cost-067", "Diritti e libertà", 4, "Quando è consentita l'estradizione del cittadino italiano?",
  "Solo ove espressamente prevista dalle convenzioni internazionali, mai per reati politici", ["Sempre, se lo chiede un altro Stato", "Mai", "Solo con referendum"],
  "Art. 26; anche qui il divieto per reati politici non si applica al genocidio.", "art. 26", "L'estradizione del cittadino può essere consentita soltanto ove sia espressamente prevista dalle convenzioni internazionali")
K("cost-068", "Diritti e libertà", 2, "A cosa devono tendere le pene secondo l'art. 27?",
  "Alla rieducazione del condannato", ["All'esclusione sociale", "Al risarcimento dello Stato", "Alla sola punizione"],
  "Le pene non possono essere contrarie al senso di umanità e devono tendere alla rieducazione.", "art. 27", "devono tendere alla rieducazione del condannato")
K("cost-069", "Diritti e libertà", 4, "Per gli atti compiuti in violazione di diritti, i dipendenti pubblici sono:",
  "direttamente responsabili, e la responsabilità civile si estende allo Stato e agli enti pubblici", ["mai responsabili personalmente", "responsabili solo disciplinarmente", "responsabili solo se dirigenti"],
  "Art. 28: responsabilità diretta del dipendente con estensione della responsabilità civile all'ente.", "art. 28", "In tali casi la responsabilità civile si estende allo Stato e agli enti pubblici")
K("cost-070", "Rapporti etico-sociali", 2, "Come definisce la famiglia l'art. 29?",
  "Società naturale fondata sul matrimonio", ["Istituzione di diritto pubblico", "Nucleo di persone conviventi", "Unione registrata presso il Comune"],
  "Il matrimonio è ordinato sull'eguaglianza morale e giuridica dei coniugi.", "art. 29", "la famiglia come società naturale fondata sul matrimonio")
K("cost-071", "Rapporti etico-sociali", 2, "Secondo l'art. 30, mantenere, istruire ed educare i figli è:",
  "dovere e diritto dei genitori, anche se i figli sono nati fuori del matrimonio", ["compito esclusivo dello Stato", "dovere solo del padre", "dovere solo per i figli nati nel matrimonio"],
  "L'art. 30 non distingue tra figli nati nel e fuori del matrimonio quanto a questo dovere.", "art. 30", "È dovere e diritto dei genitori mantenere, istruire ed educare i figli")
K("cost-072", "Rapporti etico-sociali", 2, "Come qualifica la salute l'art. 32?",
  "Fondamentale diritto dell'individuo e interesse della collettività", ["Servizio a pagamento", "Competenza esclusiva delle Regioni", "Diritto solo dei lavoratori"],
  "La Repubblica garantisce anche cure gratuite agli indigenti.", "art. 32", "La Repubblica tutela la salute come fondamentale diritto dell'individuo e interesse della collettività")
K("cost-073", "Rapporti etico-sociali", 3, "Si può essere obbligati a un trattamento sanitario?",
  "Solo per disposizione di legge, nel rispetto della persona umana", ["Mai", "Sì, su decisione del medico", "Sì, su ordinanza del sindaco senza limiti"],
  "Art. 32: trattamenti obbligatori solo per legge e mai in violazione del rispetto della persona.", "art. 32", "Nessuno può essere obbligato a un determinato trattamento sanitario se non per disposizione di legge")
K("cost-074", "Rapporti etico-sociali", 2, "Secondo l'art. 33, privati ed enti possono istituire scuole?",
  "Sì, senza oneri per lo Stato", ["No, solo lo Stato", "Sì, con finanziamento statale obbligatorio", "Solo scuole religiose"],
  "Art. 33: diritto di istituire scuole ed istituti di educazione senza oneri per lo Stato.", "art. 33", "Enti e privati hanno il diritto di istituire scuole ed istituti di educazione, senza oneri per lo Stato")
K("cost-075", "Rapporti etico-sociali", 3, "Quale valore dell'attività sportiva riconosce l'art. 33 dopo la riforma del 2023?",
  "Il valore educativo, sociale e di promozione del benessere psicofisico", ["Solo il valore economico", "Il valore agonistico olimpico", "Nessuno: lo sport non è in Costituzione"],
  "La L. cost. 1/2023 ha aggiunto il riconoscimento dell'attività sportiva in tutte le sue forme.", "art. 33", "La Repubblica riconosce il valore educativo, sociale e di promozione del benessere psicofisico dell'attività sportiva")
K("cost-076", "Rapporti etico-sociali", 2, "Per quanti anni almeno l'istruzione inferiore è obbligatoria e gratuita secondo l'art. 34?",
  "Otto", ["Cinque", "Dieci", "Dodici"],
  "Art. 34: istruzione inferiore impartita per almeno otto anni, obbligatoria e gratuita.", "art. 34", "L'istruzione inferiore, impartita per almeno otto anni, è obbligatoria e gratuita")
K("cost-077", "Rapporti etico-sociali", 3, "Chi ha diritto di raggiungere i gradi più alti degli studi secondo l'art. 34?",
  "I capaci e meritevoli, anche se privi di mezzi", ["Solo chi può pagare le tasse universitarie", "Solo i figli dei dipendenti pubblici", "Tutti, senza alcun requisito"],
  "Il diritto è reso effettivo con borse di studio e assegni attribuiti per concorso.", "art. 34", "I capaci e meritevoli, anche se privi di mezzi, hanno diritto di raggiungere i gradi più alti degli studi")
K("cost-078", "Rapporti economici", 2, "Secondo l'art. 36, la retribuzione del lavoratore deve essere:",
  "proporzionata alla quantità e qualità del lavoro e sufficiente per un'esistenza libera e dignitosa", ["uguale per tutti", "fissata dal Governo", "libera, senza limiti costituzionali"],
  "L'art. 36 fissa i criteri di proporzionalità e sufficienza.", "art. 36", "proporzionata alla quantità e qualità del suo lavoro")
K("cost-079", "Rapporti economici", 2, "Chi stabilisce la durata massima della giornata lavorativa?",
  "La legge", ["Il datore di lavoro", "Il contratto individuale", "Il sindacato"],
  "Art. 36: la durata massima della giornata lavorativa è stabilita dalla legge.", "art. 36", "La durata massima della giornata lavorativa è stabilita dalla legge")
K("cost-080", "Rapporti economici", 2, "A parità di lavoro, la donna lavoratrice ha diritto:",
  "alle stesse retribuzioni del lavoratore", ["a una retribuzione ridotta", "a una retribuzione maggiore", "solo al minimo contrattuale"],
  "Art. 37: stessi diritti e stesse retribuzioni a parità di lavoro.", "art. 37", "La donna lavoratrice ha gli stessi diritti e, a parità di lavoro, le stesse retribuzioni che spettano al lavoratore")
K("cost-081", "Rapporti economici", 3, "Secondo l'art. 38, chi ha diritto al mantenimento e all'assistenza sociale?",
  "Ogni cittadino inabile al lavoro e sprovvisto dei mezzi necessari per vivere", ["Ogni disoccupato", "Solo i pensionati", "Solo i dipendenti pubblici"],
  "L'art. 38 fonda assistenza e previdenza sociale.", "art. 38", "Ogni cittadino inabile al lavoro e sprovvisto dei mezzi necessari per vivere ha diritto al mantenimento e all'assistenza sociale")
K("cost-082", "Rapporti economici", 4, "Quale condizione pone l'art. 39 per la registrazione dei sindacati?",
  "Che gli statuti sanciscano un ordinamento interno a base democratica", ["Un numero minimo di iscritti", "L'autorizzazione del Ministro del lavoro", "L'adesione a una confederazione"],
  "La norma sulla registrazione (art. 39) non è mai stata attuata, ma prevede questa condizione.", "art. 39", "È condizione per la registrazione che gli statuti dei sindacati sanciscano un ordinamento interno a base democratica")
K("cost-083", "Rapporti economici", 1, "Dove si esercita il diritto di sciopero secondo l'art. 40?",
  "Nell'ambito delle leggi che lo regolano", ["Solo nel settore privato", "Solo con autorizzazione del prefetto", "Senza alcun limite"],
  "Art. 40: il diritto di sciopero si esercita nell'ambito delle leggi che lo regolano.", "art. 40", "Il diritto di sciopero si esercita nell'ambito delle leggi che lo regolano")
K("cost-084", "Rapporti economici", 3, "Dopo la riforma del 2022, l'iniziativa economica privata non può svolgersi in modo da recare danno anche:",
  "alla salute e all'ambiente", ["al bilancio dello Stato", "alle imprese concorrenti", "al turismo"],
  "La L. cost. 1/2022 ha aggiunto salute e ambiente ai limiti dell'art. 41.", "art. 41", "in modo da recare danno ((alla salute, all'ambiente,))")
K("cost-085", "Rapporti economici", 3, "Quando la proprietà privata può essere espropriata?",
  "Nei casi previsti dalla legge, salvo indennizzo, per motivi d'interesse generale", ["Mai", "Su decisione del sindaco senza indennizzo", "Solo in tempo di guerra"],
  "Art. 42: espropriazione per interesse generale, con indennizzo.", "art. 42", "e salvo indennizzo, espropriata per motivi d'interesse generale")
K("cost-086", "Rapporti economici", 2, "Come tratta il risparmio l'art. 47?",
  "La Repubblica lo incoraggia e tutela in tutte le sue forme", ["Lo tassa in modo speciale", "Lo vieta oltre una soglia", "Non se ne occupa"],
  "L'art. 47 disciplina anche l'esercizio del credito.", "art. 47", "La Repubblica incoraggia e tutela il risparmio in tutte le sue forme")
K("cost-087", "Rapporti politici", 2, "In quali casi il diritto di voto può essere limitato?",
  "Per incapacità civile, sentenza penale irrevocabile o indegnità morale indicata dalla legge", ["Per mancato pagamento delle tasse", "Per mancata iscrizione a un partito", "Per opinioni politiche"],
  "L'art. 48 elenca tassativamente i casi di limitazione.", "art. 48", "Il diritto di voto non può essere limitato se non per incapacità civile")
K("cost-088", "Rapporti politici", 2, "Secondo l'art. 49, i partiti concorrono a determinare la politica nazionale:",
  "con metodo democratico", ["con il controllo dello Stato", "con il finanziamento obbligatorio pubblico", "solo durante le elezioni"],
  "Tutti i cittadini possono associarsi liberamente in partiti.", "art. 49", "per concorrere con metodo democratico a determinare la politica nazionale")
K("cost-089", "Rapporti politici", 2, "A chi possono essere rivolte le petizioni dei cittadini secondo l'art. 50?",
  "Alle Camere", ["Al Presidente della Repubblica", "Alla Corte costituzionale", "Al Consiglio di Stato"],
  "Le petizioni chiedono provvedimenti legislativi o espongono comuni necessità.", "art. 50", "Tutti i cittadini possono rivolgere petizioni alle Camere")
K("cost-090", "Rapporti politici", 3, "Chi è chiamato a funzioni pubbliche elettive, secondo l'art. 51, ha diritto:",
  "di disporre del tempo necessario e di conservare il posto di lavoro", ["a un'indennità doppia", "alla promozione automatica", "a non pagare le tasse"],
  "Art. 51, ultimo comma.", "art. 51", "ha diritto di disporre del tempo necessario al loro adempimento e di conservare il suo posto di lavoro")
K("cost-091", "Rapporti politici", 2, "Come definisce l'art. 52 la difesa della Patria?",
  "Sacro dovere del cittadino", ["Facoltà riservata ai militari", "Obbligo solo maschile", "Compito esclusivo della NATO"],
  "L'ordinamento delle Forze armate si informa allo spirito democratico della Repubblica.", "art. 52", "La difesa della Patria è sacro dovere del cittadino")
K("cost-092", "Rapporti politici", 2, "Secondo l'art. 53, il sistema tributario è informato a criteri di:",
  "progressività", ["proporzionalità fissa", "regressività", "uguaglianza dell'importo"],
  "Tutti concorrono alle spese pubbliche in ragione della capacità contributiva.", "art. 53", "Il sistema tributario è informato a criteri di progressività")
K("cost-093", "Rapporti politici", 3, "Come devono adempiere le funzioni pubbliche i cittadini a cui sono affidate (art. 54)?",
  "Con disciplina ed onore, prestando giuramento nei casi stabiliti dalla legge", ["Con imparzialità politica assoluta e senza giuramento", "Solo su delega del Governo", "Secondo le indicazioni del partito"],
  "L'art. 54 impone anche a tutti i cittadini la fedeltà alla Repubblica.", "art. 54", "hanno il dovere di adempierle con disciplina ed onore")
K("cost-094", "Parlamento", 1, "Da quali Camere si compone il Parlamento?",
  "Camera dei deputati e Senato della Repubblica", ["Camera e Consiglio di Stato", "Senato e Consiglio regionale", "Camera alta e Camera dei comuni"],
  "Art. 55: bicameralismo paritario.", "art. 55", "Il Parlamento si compone della Camera dei deputati e del Senato della Repubblica")
K("cost-095", "Parlamento", 3, "Quanti deputati sono eletti nella circoscrizione Estero?",
  "Otto", ["Dodici", "Quattro", "Sei"],
  "Art. 56: 400 deputati, otto dei quali eletti all'estero; al Senato i senatori eletti all'estero sono quattro.", "art. 56", "((otto)) dei quali eletti nella circoscrizione Estero")
K("cost-096", "Parlamento", 3, "Su quale base è eletto il Senato della Repubblica?",
  "Su base regionale, salvi i seggi della circoscrizione Estero", ["Su base nazionale unica", "Su base provinciale", "Su base comunale"],
  "Lo stabilisce l'art. 57 della Costituzione.", "art. 57", "Il Senato della Repubblica è eletto a base regionale")
K("cost-097", "Parlamento", 4, "Quanti senatori ha almeno ciascuna Regione (escluse Molise e Valle d'Aosta)?",
  "Tre", ["Cinque", "Sette", "Due"],
  "Art. 57: nessuna Regione o Provincia autonoma può avere meno di tre senatori; il Molise ne ha due, la Valle d'Aosta uno.", "art. 57", "il Molise ne ha due, la Valle d'Aosta uno")
K("cost-098", "Parlamento", 3, "Chi è senatore di diritto e a vita, salvo rinunzia?",
  "Chi è stato Presidente della Repubblica", ["Chi è stato Presidente del Consiglio", "Chi è stato presidente della Corte costituzionale", "Chi è stato Presidente del Senato"],
  "Art. 59, primo comma.", "art. 59", "È senatore di diritto e a vita, salvo rinunzia, chi è stato Presidente della Repubblica")
K("cost-099", "Parlamento", 4, "In quale caso può essere prorogata la durata delle Camere?",
  "Solo per legge e soltanto in caso di guerra", ["Con decreto del Presidente della Repubblica", "Per accordo tra i partiti", "Mai"],
  "Art. 60, secondo comma.", "art. 60", "non può essere prorogata se non per legge e soltanto in caso di guerra")
K("cost-100", "Parlamento", 3, "Entro quanti giorni dalla fine delle precedenti hanno luogo le elezioni delle nuove Camere?",
  "Settanta", ["Sessanta", "Novanta", "Trenta"],
  "Art. 61: elezioni entro settanta giorni; prima riunione non oltre il ventesimo giorno dalle elezioni.", "art. 61", "Le elezioni delle nuove Camere hanno luogo entro settanta giorni dalla fine delle precedenti")
K("cost-101", "Parlamento", 4, "Quando si riuniscono di diritto le Camere?",
  "Il primo giorno non festivo di febbraio e di ottobre", ["Il 2 giugno di ogni anno", "Il primo lunedì di gennaio e luglio", "Solo su convocazione del Governo"],
  "Art. 62: riunioni di diritto; convocazione straordinaria su iniziativa del Presidente della Camera, del Presidente della Repubblica o di un terzo dei componenti.", "art. 62", "Le Camere si riuniscono di diritto il primo giorno non festivo di febbraio e di ottobre")
K("cost-102", "Parlamento", 3, "Quando il Parlamento si riunisce in seduta comune, chi lo presiede?",
  "Il Presidente e l'Ufficio di presidenza della Camera dei deputati", ["Il Presidente del Senato", "Il Presidente della Repubblica", "Il più anziano dei parlamentari"],
  "Art. 63, secondo comma.", "art. 63", "il Presidente e l'Ufficio di presidenza sono quelli della Camera dei deputati")
K("cost-103", "Parlamento", 3, "Con quale maggioranza ciascuna Camera adotta il proprio regolamento?",
  "Maggioranza assoluta dei suoi componenti", ["Maggioranza semplice dei presenti", "Due terzi dei componenti", "Unanimità"],
  "Art. 64, primo comma.", "art. 64", "Ciascuna Camera adotta il proprio regolamento a maggioranza assoluta dei suoi componenti")
K("cost-104", "Parlamento", 4, "Quando sono valide le deliberazioni delle Camere?",
  "Se è presente la maggioranza dei componenti e sono adottate a maggioranza dei presenti, salvo maggioranze speciali", ["Se votano almeno due terzi dei componenti", "Sempre, qualunque sia il numero dei presenti", "Solo se presente il Governo"],
  "Art. 64, terzo comma: numero legale e maggioranza.", "art. 64", "non sono valide se non è presente la maggioranza dei loro componenti")
K("cost-105", "Parlamento", 2, "Si può essere contemporaneamente deputato e senatore?",
  "No, nessuno può appartenere contemporaneamente alle due Camere", ["Sì, sempre", "Sì, per non più di un anno", "Solo i senatori a vita"],
  "Art. 65, secondo comma.", "art. 65", "Nessuno può appartenere contemporaneamente alle due Camere")
K("cost-106", "Parlamento", 3, "Chi giudica dei titoli di ammissione dei componenti di ciascuna Camera?",
  "La Camera stessa", ["La Corte costituzionale", "La Corte di cassazione", "Il Presidente della Repubblica"],
  "Art. 66: verifica dei poteri interna a ciascuna Camera.", "art. 66", "Ciascuna Camera giudica dei titoli di ammissione dei suoi componenti")
K("cost-107", "Parlamento", 4, "Per quali condotte i parlamentari non possono essere chiamati a rispondere?",
  "Per le opinioni espresse e i voti dati nell'esercizio delle loro funzioni", ["Per qualsiasi reato commesso durante il mandato", "Per i reati commessi prima dell'elezione", "Per le violazioni stradali"],
  "Art. 68: insindacabilità; per arresti, perquisizioni e intercettazioni serve l'autorizzazione della Camera di appartenenza.", "art. 68", "non possono essere chiamati a rispondere delle opinioni espresse e dei voti dati nell'esercizio delle loro funzioni")
K("cost-108", "Parlamento", 5, "Un parlamentare viene sorpreso a commettere un delitto per il quale è previsto l'arresto obbligatorio in flagranza. Serve l'autorizzazione della Camera per arrestarlo?",
  "No: in questo caso l'arresto è possibile senza autorizzazione", ["Sì, sempre", "Sì, ma basta quella del Presidente della Camera", "No, ma serve quella del Presidente della Repubblica"],
  "L'art. 68 esclude l'autorizzazione per l'esecuzione di una sentenza irrevocabile e per la flagranza di delitti con arresto obbligatorio.", "art. 68", "ovvero se sia colto nell'atto di commettere un delitto per il quale è previsto l'arresto obbligatorio in flagranza")
K("cost-109", "Formazione delle leggi", 2, "A chi appartiene l'iniziativa delle leggi?",
  "Al Governo, a ciascun membro delle Camere, agli organi ed enti previsti da legge costituzionale e al popolo", ["Solo al Governo", "Solo ai parlamentari", "Solo al Presidente della Repubblica"],
  "Art. 71: tra gli altri enti ci sono CNEL e Consigli regionali.", "art. 71", "L'iniziativa delle leggi appartiene al Governo, a ciascun membro delle Camere")
K("cost-110", "Formazione delle leggi", 4, "Per quali disegni di legge è sempre obbligatoria la procedura normale di esame e approvazione diretta da parte della Camera?",
  "In materia costituzionale ed elettorale, di delegazione legislativa, di ratifica dei trattati, di approvazione di bilanci", ["Per tutti i decreti-legge", "Per le leggi regionali", "Per le leggi di spesa inferiore a un milione"],
  "Art. 72, ultimo comma: riserva d'assemblea.", "art. 72", "La procedura normale di esame e di approvazione diretta da parte della Camera è sempre adottata per i disegni di legge in materia costituzionale ed elettorale")
K("cost-111", "Formazione delle leggi", 2, "Entro quanto tempo dall'approvazione le leggi sono promulgate dal Presidente della Repubblica?",
  "Entro un mese", ["Entro sessanta giorni", "Entro una settimana", "Entro tre mesi"],
  "Art. 73: termine più breve se le Camere ne dichiarano l'urgenza a maggioranza assoluta.", "art. 73", "Le leggi sono promulgate dal Presidente della Repubblica entro un mese dall'approvazione")
K("cost-112", "Formazione delle leggi", 1, "Quando entrano in vigore, di regola, le leggi?",
  "Il quindicesimo giorno successivo alla pubblicazione", ["Il giorno stesso della pubblicazione", "Dopo trenta giorni", "Il primo gennaio successivo"],
  "Art. 73: salvo che le leggi stabiliscano un termine diverso (vacatio legis).", "art. 73", "entrano in vigore il quindicesimo giorno successivo alla loro pubblicazione")
K("cost-113", "Formazione delle leggi", 3, "Il Presidente della Repubblica può rifiutarsi di promulgare una legge?",
  "Può chiedere una nuova deliberazione con messaggio motivato; se le Camere la riapprovano, deve promulgarla", ["Sì, definitivamente", "No, mai", "Sì, se la Corte costituzionale è d'accordo"],
  "Art. 74: rinvio presidenziale.", "art. 74", "Se le Camere approvano nuovamente la legge, questa deve essere promulgata")
K("cost-114", "Formazione delle leggi", 3, "Chi ha diritto di partecipare al referendum abrogativo?",
  "Tutti i cittadini chiamati ad eleggere la Camera dei deputati", ["Solo gli iscritti ai partiti", "I cittadini con più di 25 anni", "Solo i firmatari della richiesta"],
  "Art. 75, terzo comma.", "art. 75", "Hanno diritto di partecipare al referendum tutti i cittadini chiamati ad eleggere la Camera dei deputati")
K("cost-115", "Fonti del diritto", 3, "Quali limiti deve contenere la legge delega al Governo?",
  "Principi e criteri direttivi, tempo limitato e oggetti definiti", ["Solo il termine", "Nessuno", "Solo l'indicazione della materia"],
  "Art. 76: limiti del decreto legislativo delegato.", "art. 76", "se non con determinazione di principi e criteri direttivi e soltanto per tempo limitato e per oggetti definiti")
K("cost-116", "Fonti del diritto", 4, "Un decreto-legge presentato quando le Camere sono sciolte: cosa prevede l'art. 77?",
  "Le Camere sono appositamente convocate e si riuniscono entro cinque giorni", ["Il decreto decade subito", "Lo converte il Presidente della Repubblica", "Si attendono le nuove Camere"],
  "Il decreto va presentato il giorno stesso alle Camere, anche se sciolte.", "art. 77", "anche se sciolte, sono appositamente convocate e si riuniscono entro cinque giorni")
K("cost-117", "Fonti del diritto", 4, "Cosa accade ai rapporti giuridici sorti sulla base di un decreto-legge non convertito?",
  "Le Camere possono regolarli con legge", ["Restano validi automaticamente", "Sono sempre nulli senza rimedio", "Li regola il Governo con un nuovo decreto"],
  "Il decreto perde efficacia ex tunc, ma la legge può regolare i rapporti sorti.", "art. 77", "Le Camere possono tuttavia regolare con legge i rapporti giuridici sorti sulla base dei decreti non convertiti")
K("cost-118", "Fonti del diritto", 2, "Chi delibera lo stato di guerra?",
  "Le Camere", ["Il Governo", "Il Presidente della Repubblica da solo", "Il Consiglio supremo di difesa"],
  "Art. 78: le Camere deliberano e conferiscono al Governo i poteri necessari; il Presidente lo dichiara (art. 87).", "art. 78", "Le Camere deliberano lo stato di guerra")
K("cost-119", "Fonti del diritto", 4, "A quali reati non possono applicarsi amnistia e indulto?",
  "Ai reati commessi dopo la presentazione del disegno di legge", ["Ai reati contro la PA", "Ai reati commessi da minorenni", "A nessun reato: si applicano a tutti"],
  "Art. 79, ultimo periodo.", "art. 79", "non possono applicarsi ai reati commessi successivamente alla presentazione del disegno di legge")
K("cost-120", "Fonti del diritto", 3, "Quali trattati internazionali richiedono una legge di autorizzazione alla ratifica?",
  "Quelli politici, che prevedono arbitrati, variazioni del territorio, oneri finanziari o modifiche di leggi", ["Tutti i trattati, senza eccezioni", "Solo quelli con Stati extra UE", "Nessuno: ratifica sempre il Governo"],
  "Lo stabilisce l'art. 80 della Costituzione.", "art. 80", "Le Camere autorizzano con legge la ratifica dei trattati internazionali che sono di natura politica")
K("cost-121", "Bilancio", 4, "Per quanto tempo al massimo può essere concesso l'esercizio provvisorio del bilancio?",
  "Per periodi non superiori complessivamente a quattro mesi", ["Sei mesi", "Un anno", "Due mesi"],
  "Art. 81: solo per legge e per non più di quattro mesi complessivi.", "art. 81", "per periodi non superiori complessivamente a quattro mesi")
K("cost-122", "Bilancio", 4, "Quando è consentito il ricorso all'indebitamento secondo l'art. 81?",
  "Solo per considerare gli effetti del ciclo economico e, con autorizzazione a maggioranza assoluta, per eventi eccezionali", ["Sempre, se lo decide il Governo", "Mai", "Solo per le Regioni"],
  "Riforma del 2012 (equilibrio di bilancio).", "art. 81", "Il ricorso all'indebitamento è consentito solo al fine di considerare gli effetti del ciclo economico")
K("cost-123", "Parlamento", 3, "Con quali poteri procede una commissione parlamentare d'inchiesta?",
  "Con gli stessi poteri e le stesse limitazioni dell'autorità giudiziaria", ["Con poteri illimitati", "Solo con poteri consultivi", "Con i poteri del Governo"],
  "Lo stabilisce l'art. 82 della Costituzione.", "art. 82", "procede alle indagini e agli esami con gli stessi poteri e le stesse limitazioni dell'autorità giudiziaria")

K("cost-124", "Presidente della Repubblica", 3, "Quanti delegati per Regione partecipano all'elezione del Presidente della Repubblica?",
  "Tre per Regione, uno solo per la Valle d'Aosta", ["Due per Regione", "Cinque per Regione", "Uno per Regione"],
  "Art. 83: delegati eletti dal Consiglio regionale garantendo la rappresentanza delle minoranze.", "art. 83", "La Valle d'Aosta ha un solo delegato")
K("cost-125", "Presidente della Repubblica", 2, "Con quale tipo di votazione è eletto il Presidente della Repubblica?",
  "Scrutinio segreto", ["Voto palese per appello nominale", "Alzata di mano", "Voto elettronico pubblico"],
  "Art. 83: scrutinio segreto, maggioranza di due terzi nei primi tre scrutini.", "art. 83", "ha luogo per scrutinio segreto a maggioranza di due terzi della assemblea")
K("cost-126", "Presidente della Repubblica", 3, "L'ufficio di Presidente della Repubblica è compatibile con altre cariche?",
  "No, è incompatibile con qualsiasi altra carica", ["Sì, con quella di senatore", "Sì, con quella di sindaco", "Solo con incarichi universitari"],
  "Art. 84, secondo comma.", "art. 84", "L'ufficio di Presidente della Repubblica è incompatibile con qualsiasi altra carica")
K("cost-127", "Presidente della Repubblica", 4, "Chi convoca il Parlamento in seduta comune per eleggere il nuovo Presidente della Repubblica, trenta giorni prima della scadenza?",
  "Il Presidente della Camera dei deputati", ["Il Presidente del Senato", "Il Presidente del Consiglio", "Il Presidente uscente"],
  "Art. 85, secondo comma.", "art. 85", "Trenta giorni prima che scada il termine, il Presidente della Camera dei deputati convoca in seduta comune il Parlamento")
K("cost-128", "Presidente della Repubblica", 5, "Il mandato presidenziale scade quando mancano meno di tre mesi alla cessazione delle Camere. Quando si elegge il nuovo Presidente?",
  "Entro quindici giorni dalla riunione delle Camere nuove, con proroga dei poteri del Presidente in carica", ["Subito, dalle Camere uscenti", "Dopo un anno", "Lo nomina il Presidente del Senato"],
  "Art. 85, terzo comma.", "art. 85", "la elezione ha luogo entro quindici giorni dalla riunione delle Camere nuove")
K("cost-129", "Presidente della Repubblica", 4, "In caso di morte o dimissioni del Presidente della Repubblica, entro quanti giorni il Presidente della Camera indice l'elezione del successore?",
  "Quindici", ["Trenta", "Sessanta", "Sette"],
  "Art. 86, secondo comma.", "art. 86", "il Presidente della Camera dei deputati indice la elezione del nuovo Presidente della Repubblica entro quindici giorni")
K("cost-130", "Presidente della Repubblica", 2, "Chi ha il comando delle Forze armate?",
  "Il Presidente della Repubblica", ["Il Ministro della difesa", "Il Presidente del Consiglio", "Il Capo di Stato maggiore della difesa"],
  "Art. 87: il Presidente ha il comando delle Forze armate e presiede il Consiglio supremo di difesa.", "art. 87", "Ha il comando delle Forze armate, presiede il Consiglio supremo di difesa")
K("cost-131", "Presidente della Repubblica", 2, "Quale di questi poteri spetta al Presidente della Repubblica?",
  "Concedere la grazia e commutare le pene", ["Approvare il bilancio dello Stato", "Nominare i giudici ordinari", "Votare la fiducia al Governo"],
  "Art. 87, tra le attribuzioni presidenziali.", "art. 87", "Può concedere grazia e commutare le pene")
K("cost-132", "Presidente della Repubblica", 3, "Prima di sciogliere le Camere, il Presidente della Repubblica deve:",
  "sentire i loro Presidenti", ["ottenere il parere della Corte costituzionale", "indire un referendum", "avere il voto del Consiglio dei ministri"],
  "Art. 88: può sciogliere le Camere o una sola di esse, sentiti i loro Presidenti.", "art. 88", "Il Presidente della Repubblica può, sentiti i loro Presidenti, sciogliere le Camere")
K("cost-133", "Presidente della Repubblica", 3, "Quando è valido un atto del Presidente della Repubblica?",
  "Solo se è controfirmato dai ministri proponenti, che ne assumono la responsabilità", ["Sempre, con la sola firma presidenziale", "Solo se approvato dalle Camere", "Solo con il visto della Corte dei conti"],
  "Art. 89: controfirma ministeriale.", "art. 89", "Nessun atto del Presidente della Repubblica è valido se non è controfirmato dai ministri proponenti")
K("cost-134", "Presidente della Repubblica", 4, "Da chi è messo in stato di accusa il Presidente della Repubblica per alto tradimento o attentato alla Costituzione?",
  "Dal Parlamento in seduta comune, a maggioranza assoluta dei membri", ["Dalla Corte di cassazione", "Dal Senato a maggioranza semplice", "Dal Governo"],
  "Art. 90; il giudizio spetta poi alla Corte costituzionale integrata.", "art. 90", "è messo in stato di accusa dal Parlamento in seduta comune, a maggioranza assoluta dei suoi membri")
K("cost-135", "Presidente della Repubblica", 2, "Dinanzi a chi presta giuramento il Presidente della Repubblica?",
  "Dinanzi al Parlamento in seduta comune", ["Dinanzi alla Corte costituzionale", "Nelle mani del Presidente del Senato", "Dinanzi al Consiglio dei ministri"],
  "Lo stabilisce l'art. 91 della Costituzione.", "art. 91", "dinanzi al Parlamento in seduta comune")
K("cost-136", "Governo", 1, "Da chi è composto il Governo?",
  "Dal Presidente del Consiglio e dai ministri", ["Solo dai ministri", "Dal Presidente della Repubblica e dai ministri", "Dai sottosegretari"],
  "Art. 92: insieme costituiscono il Consiglio dei ministri.", "art. 92", "Il Governo della Repubblica è composto del Presidente del Consiglio e dei ministri")
K("cost-137", "Governo", 2, "Chi nomina i ministri?",
  "Il Presidente della Repubblica, su proposta del Presidente del Consiglio", ["Il Parlamento", "Il Presidente del Consiglio da solo", "I partiti di maggioranza"],
  "Art. 92, secondo comma.", "art. 92", "Il Presidente della Repubblica nomina il Presidente del Consiglio dei ministri e, su proposta di questo, i ministri")
K("cost-138", "Governo", 2, "Nelle mani di chi giurano il Presidente del Consiglio e i ministri?",
  "Del Presidente della Repubblica", ["Del Presidente della Camera", "Del Presidente della Corte costituzionale", "Del Parlamento in seduta comune"],
  "Lo stabilisce l'art. 93 della Costituzione.", "art. 93", "prestano giuramento nelle mani del Presidente della Repubblica")
K("cost-139", "Governo", 3, "Come accordano o revocano la fiducia le Camere?",
  "Con mozione motivata e votata per appello nominale", ["Con voto segreto", "Con decreto del Presidente", "Per acclamazione"],
  "Art. 94, secondo comma.", "art. 94", "mediante mozione motivata e votata per appello nominale")
K("cost-140", "Governo", 4, "Se una Camera vota contro una proposta del Governo, il Governo deve dimettersi?",
  "No, non c'è obbligo di dimissioni", ["Sì, sempre", "Sì, se il voto è al Senato", "Sì, entro dieci giorni"],
  "Art. 94: il voto contrario su una proposta del Governo non importa obbligo di dimissioni (diverso dalla mozione di sfiducia).", "art. 94", "non importa obbligo di dimissioni")
K("cost-141", "Governo", 3, "Chi dirige la politica generale del Governo e ne è responsabile?",
  "Il Presidente del Consiglio dei ministri", ["Il Presidente della Repubblica", "Il Ministro dell'economia", "Il Consiglio di Stato"],
  "Art. 95: mantiene l'unità di indirizzo politico e amministrativo.", "art. 95", "Il Presidente del Consiglio dei ministri dirige la politica generale del Governo e ne è responsabile")
K("cost-142", "Governo", 4, "Per quali atti i ministri sono responsabili individualmente?",
  "Per gli atti dei loro dicasteri", ["Per tutti gli atti del Consiglio dei ministri", "Per nessun atto", "Solo per i decreti-legge"],
  "Art. 95: responsabilità collegiale per gli atti del Consiglio, individuale per quelli del proprio ministero.", "art. 95", "individualmente degli atti dei loro dicasteri")
K("cost-143", "Governo", 5, "Un ministro commette un reato nell'esercizio delle sue funzioni. Quale giudice è competente?",
  "La giurisdizione ordinaria, previa autorizzazione della Camera competente", ["La Corte costituzionale", "Un tribunale speciale ministeriale senza autorizzazione", "Il Senato in funzione di giudice"],
  "Art. 96 come riformato nel 1989.", "art. 96", "sono sottoposti, per i reati commessi nell'esercizio delle loro funzioni, alla giurisdizione ordinaria")
K("cost-144", "Pubblica amministrazione", 1, "Secondo l'art. 97, come si accede agli impieghi nelle pubbliche amministrazioni?",
  "Mediante concorso, salvo i casi stabiliti dalla legge", ["Per chiamata diretta", "Per sorteggio", "Per nomina politica"],
  "È il fondamento costituzionale dei concorsi pubblici.", "art. 97", "Agli impieghi nelle pubbliche amministrazioni si accede mediante concorso")
K("cost-145", "Pubblica amministrazione", 2, "Quali principi devono assicurare i pubblici uffici secondo l'art. 97?",
  "Buon andamento e imparzialità dell'amministrazione", ["Efficienza e profitto", "Riservatezza e segretezza", "Gerarchia e obbedienza"],
  "Art. 97, secondo comma.", "art. 97", "siano assicurati il buon andamento e l'imparzialità dell'amministrazione")
K("cost-146", "Pubblica amministrazione", 2, "Secondo l'art. 98, i pubblici impiegati sono al servizio:",
  "esclusivo della Nazione", ["del Governo in carica", "del partito di maggioranza", "dell'ente che li paga"],
  "Art. 98, primo comma.", "art. 98", "I pubblici impiegati sono al servizio esclusivo della Nazione")
K("cost-147", "Pubblica amministrazione", 4, "Per quali categorie la legge può limitare l'iscrizione ai partiti politici?",
  "Magistrati, militari di carriera in servizio, funzionari e agenti di polizia, diplomatici e consoli all'estero", ["Tutti i dipendenti pubblici", "Gli insegnanti", "I medici del servizio sanitario"],
  "Art. 98, terzo comma.", "art. 98", "limitazioni al diritto d'iscriversi ai partiti politici per i magistrati")
K("cost-148", "Organi ausiliari", 3, "Quale organo ausiliario è composto da esperti e rappresentanti delle categorie produttive?",
  "Il CNEL (Consiglio nazionale dell'economia e del lavoro)", ["Il Consiglio di Stato", "La Corte dei conti", "Il CSM"],
  "Art. 99: il CNEL è consulente di Camere e Governo e ha iniziativa legislativa.", "art. 99", "Il Consiglio nazionale dell'economia e del lavoro è composto")
K("cost-149", "Organi ausiliari", 2, "Come definisce il Consiglio di Stato l'art. 100?",
  "Organo di consulenza giuridico-amministrativa e di tutela della giustizia nell'amministrazione", ["Organo di controllo contabile", "Organo legislativo", "Organo di governo delle Regioni"],
  "Art. 100, primo comma.", "art. 100", "Il Consiglio di Stato è organo di consulenza giuridico-amministrativa")
K("cost-150", "Organi ausiliari", 3, "Quale controllo esercita la Corte dei conti sugli atti del Governo?",
  "Il controllo preventivo di legittimità", ["Il controllo di merito politico", "Il controllo di costituzionalità", "Nessun controllo"],
  "Art. 100: oltre al controllo successivo sulla gestione del bilancio.", "art. 100", "La Corte dei conti esercita il controllo preventivo di legittimità sugli atti del Governo")
K("cost-151", "Magistratura", 1, "In nome di chi è amministrata la giustizia?",
  "In nome del popolo", ["In nome del Presidente della Repubblica", "In nome dello Stato", "In nome della legge"],
  "Art. 101: i giudici sono soggetti soltanto alla legge.", "art. 101", "La giustizia è amministrata in nome del popolo")
K("cost-152", "Magistratura", 3, "Possono essere istituiti giudici straordinari o speciali?",
  "No; si possono istituire solo sezioni specializzate presso gli organi giudiziari ordinari", ["Sì, con decreto del Governo", "Sì, in tempo di pace", "Sì, per i reati politici"],
  "Lo stabilisce l'art. 102 della Costituzione.", "art. 102", "Non possono essere istituiti giudici straordinari o giudici speciali")
K("cost-153", "Magistratura", 3, "A tutela di quali situazioni hanno giurisdizione il Consiglio di Stato e gli altri organi di giustizia amministrativa?",
  "Degli interessi legittimi e, nelle materie indicate dalla legge, anche dei diritti soggettivi", ["Solo dei diritti soggettivi", "Solo dei reati dei pubblici ufficiali", "Delle controversie tra privati"],
  "Lo stabilisce l'art. 103 della Costituzione.", "art. 103", "degli interessi legittimi e, in particolari materie indicate dalla legge, anche dei diritti soggettivi")
K("cost-154", "Magistratura", 4, "In tempo di pace, su quali reati hanno giurisdizione i tribunali militari?",
  "Solo sui reati militari commessi da appartenenti alle Forze armate", ["Su tutti i reati commessi da militari", "Sui reati contro lo Stato", "Su nessun reato"],
  "Art. 103, ultimo comma.", "art. 103", "In tempo di pace hanno giurisdizione soltanto per i reati militari commessi da appartenenti alle Forze armate")
K("cost-155", "Magistratura", 4, "Come sono eletti i membri elettivi del CSM?",
  "Due terzi dai magistrati ordinari, un terzo dal Parlamento in seduta comune", ["Tutti dal Parlamento", "Metà dal Governo, metà dai magistrati", "Tutti dai magistrati"],
  "Art. 104: i membri di nomina parlamentare sono professori di diritto e avvocati con quindici anni di esercizio.", "art. 104", "sono eletti per due terzi da tutti i magistrati ordinari")
K("cost-156", "Magistratura", 3, "Quanto durano in carica i membri elettivi del CSM?",
  "Quattro anni, e non sono immediatamente rieleggibili", ["Sei anni, rieleggibili", "Nove anni", "Due anni"],
  "Lo stabilisce l'art. 104 della Costituzione.", "art. 104", "I membri elettivi del Consiglio durano in carica quattro anni e non sono immediatamente rieleggibili")
K("cost-157", "Magistratura", 3, "Come avvengono le nomine dei magistrati?",
  "Per concorso", ["Per elezione popolare", "Per nomina ministeriale", "Per cooptazione"],
  "Art. 106; sono ammesse nomine di magistrati onorari per le funzioni di giudici singoli.", "art. 106", "Le nomine dei magistrati hanno luogo per concorso")
K("cost-158", "Magistratura", 3, "Cosa significa che i magistrati sono «inamovibili»?",
  "Non possono essere trasferiti o sospesi se non per decisione del CSM con le garanzie previste o con il loro consenso", ["Non possono mai cambiare sede", "Non possono essere giudicati", "Restano in carica a vita senza limiti di età"],
  "Art. 107; il Ministro della giustizia può promuovere l'azione disciplinare.", "art. 107", "I magistrati sono inamovibili")
K("cost-159", "Magistratura", 2, "Chi dispone direttamente della polizia giudiziaria?",
  "L'autorità giudiziaria", ["Il Ministro dell'interno", "Il prefetto", "Il questore"],
  "Lo stabilisce l'art. 109 della Costituzione.", "art. 109", "L'autorità giudiziaria dispone direttamente della polizia giudiziaria")
K("cost-160", "Magistratura", 3, "Quali caratteristiche deve avere il giudice nel giusto processo (art. 111)?",
  "Terzo e imparziale", ["Elettivo e politico", "Nominato dalle parti", "Unico per tutto il processo"],
  "Ogni processo si svolge nel contraddittorio tra le parti, in condizioni di parità.", "art. 111", "davanti a giudice terzo e imparziale")
K("cost-161", "Magistratura", 4, "Contro le sentenze e i provvedimenti sulla libertà personale è sempre ammesso:",
  "ricorso in Cassazione per violazione di legge", ["ricorso alla Corte costituzionale", "ricorso al Presidente della Repubblica", "appello al Consiglio di Stato"],
  "Art. 111, con deroga solo per le sentenze dei tribunali militari in tempo di guerra.", "art. 111", "è sempre ammesso ricorso in Cassazione per violazione di legge")
K("cost-162", "Magistratura", 2, "Cosa stabilisce l'art. 112 sul pubblico ministero?",
  "Ha l'obbligo di esercitare l'azione penale", ["Può scegliere liberamente se agire", "Dipende dal Ministro della giustizia", "Esercita l'azione solo su querela"],
  "È il principio di obbligatorietà dell'azione penale.", "art. 112", "Il pubblico ministero ha l'obbligo di esercitare l'azione penale")
K("cost-163", "Magistratura", 3, "Contro gli atti della pubblica amministrazione la tutela giurisdizionale:",
  "è sempre ammessa e non può essere esclusa o limitata per determinate categorie di atti", ["è ammessa solo per gli atti dei ministeri", "è esclusa per gli atti politici dei Comuni", "richiede l'autorizzazione del prefetto"],
  "Lo stabilisce l'art. 113 della Costituzione.", "art. 113", "Tale tutela giurisdizionale non può essere esclusa o limitata")
K("cost-164", "Regioni ed enti locali", 1, "Qual è la capitale della Repubblica secondo la Costituzione?",
  "Roma", ["Torino", "Firenze", "Nessuna: non è indicata"],
  "Art. 114: Roma è la capitale; la legge dello Stato ne disciplina l'ordinamento.", "art. 114", "Roma è la capitale della Repubblica")
K("cost-165", "Regioni ed enti locali", 2, "Quali sono le Regioni a statuto speciale?",
  "Friuli Venezia Giulia, Sardegna, Sicilia, Trentino-Alto Adige/Südtirol, Valle d'Aosta", ["Sicilia, Sardegna, Calabria, Valle d'Aosta, Veneto", "Lombardia, Veneto, Sicilia, Sardegna, Trentino", "Solo Sicilia e Sardegna"],
  "Art. 116: statuti speciali adottati con legge costituzionale.", "art. 116", "dispongono di forme e condizioni particolari di autonomia")
K("cost-166", "Regioni ed enti locali", 3, "Da quali Province autonome è costituita la Regione Trentino-Alto Adige/Südtirol?",
  "Trento e Bolzano", ["Trento e Belluno", "Bolzano e Sondrio", "Trento e Verona"],
  "Art. 116, secondo comma.", "art. 116", "è costituita dalle Province autonome di Trento e di Bolzano")
K("cost-167", "Regioni ed enti locali", 3, "Quale di queste materie è di legislazione esclusiva dello Stato?",
  "Moneta e tutela del risparmio", ["Tutela della salute", "Governo del territorio", "Protezione civile"],
  "Art. 117, secondo comma, lett. e). Salute, governo del territorio e protezione civile sono materie concorrenti.", "art. 117", "e) moneta, tutela del risparmio e mercati finanziari")
K("cost-168", "Regioni ed enti locali", 3, "Quale di queste materie è di legislazione concorrente tra Stato e Regioni?",
  "Tutela della salute", ["Difesa e Forze armate", "Immigrazione", "Ordinamento civile e penale"],
  "Art. 117, terzo comma: nelle materie concorrenti lo Stato fissa i principi fondamentali.", "art. 117", "ricerca scientifica e tecnologica e sostegno all'innovazione per i settori produttivi; tutela della salute")
K("cost-169", "Regioni ed enti locali", 4, "A chi spetta la potestà legislativa nelle materie non espressamente riservate allo Stato?",
  "Alle Regioni (competenza residuale)", ["Allo Stato", "Ai Comuni", "All'Unione europea"],
  "Art. 117, quarto comma.", "art. 117", "Spetta alle Regioni la potestà legislativa in riferimento ad ogni materia non espressamente riservata alla legislazione dello Stato")
K("cost-170", "Regioni ed enti locali", 4, "Nelle materie di legislazione concorrente, cosa spetta allo Stato?",
  "La determinazione dei principi fondamentali", ["Tutta la disciplina di dettaglio", "Nulla", "Solo i regolamenti"],
  "Art. 117, terzo comma.", "art. 117", "salvo che per la determinazione dei principi fondamentali, riservata alla legislazione dello Stato")
K("cost-171", "Regioni ed enti locali", 3, "Con quali principi le funzioni amministrative sono attribuite ai diversi livelli di governo (art. 118)?",
  "Sussidiarietà, differenziazione e adeguatezza", ["Gerarchia, competenza e territorialità", "Efficienza, efficacia ed economicità", "Legalità, imparzialità e buon andamento"],
  "Le funzioni spettano ai Comuni, salvo conferimento ad enti più ampi per l'esercizio unitario.", "art. 118", "sulla base dei principi di sussidiarietà, differenziazione ed adeguatezza")
K("cost-172", "Regioni ed enti locali", 4, "Cosa prevede l'ultimo comma dell'art. 118 sull'iniziativa dei cittadini?",
  "Gli enti favoriscono l'autonoma iniziativa dei cittadini per attività di interesse generale (sussidiarietà orizzontale)", ["La vieta senza autorizzazione", "La riserva alle associazioni registrate", "La affida ai partiti"],
  "Art. 118, quarto comma.", "art. 118", "favoriscono l'autonoma iniziativa dei cittadini, singoli e associati")
K("cost-173", "Regioni ed enti locali", 4, "Per quali spese Comuni, Province, Città metropolitane e Regioni possono indebitarsi?",
  "Solo per finanziare spese di investimento", ["Per qualsiasi spesa", "Solo per pagare stipendi", "Mai"],
  "Art. 119: con piani di ammortamento e senza garanzia dello Stato.", "art. 119", "Possono ricorrere all'indebitamento solo per finanziare spese di investimento")
K("cost-174", "Regioni ed enti locali", 3, "Quale riconoscimento è stato aggiunto all'art. 119 nel 2022?",
  "Le peculiarità delle Isole e la rimozione degli svantaggi dell'insularità", ["La tutela delle montagne", "Il federalismo fiscale integrale", "L'abolizione delle Province"],
  "L. cost. 2/2022.", "art. 119", "La Repubblica riconosce le peculiarità delle Isole")
K("cost-175", "Regioni ed enti locali", 3, "Una Regione può istituire dazi sul transito di merci tra Regioni?",
  "No, l'art. 120 lo vieta", ["Sì, con legge regionale", "Sì, con il consenso del Governo", "Solo le Regioni speciali"],
  "Art. 120: vietati anche provvedimenti che ostacolino la libera circolazione.", "art. 120", "La Regione non può istituire dazi di importazione o esportazione o transito tra le Regioni")
K("cost-176", "Regioni ed enti locali", 2, "Quali sono gli organi della Regione?",
  "Il Consiglio regionale, la Giunta e il suo presidente", ["Il Consiglio regionale e il prefetto", "La Giunta e il commissario di Governo", "Il Presidente e la Corte dei conti regionale"],
  "Lo stabilisce l'art. 121 della Costituzione.", "art. 121", "Sono organi della Regione: il Consiglio regionale, la Giunta e il suo presidente")
K("cost-177", "Regioni ed enti locali", 3, "Come è eletto, di regola, il Presidente della Giunta regionale?",
  "A suffragio universale e diretto, salvo diversa previsione dello statuto", ["Dal Consiglio regionale", "Dal Governo", "Dai sindaci della Regione"],
  "Lo stabilisce l'art. 122 della Costituzione.", "art. 122", "è eletto a suffragio universale e diretto")
K("cost-178", "Regioni ed enti locali", 4, "Come è approvato lo statuto di una Regione ordinaria?",
  "Con legge regionale a maggioranza assoluta, con due deliberazioni a distanza di almeno due mesi", ["Con legge dello Stato", "Con legge costituzionale", "Con decreto del Presidente della Repubblica"],
  "Lo stabilisce l'art. 123 della Costituzione.", "art. 123", "con due deliberazioni successive adottate ad intervallo non minore di due mesi")
K("cost-179", "Regioni ed enti locali", 4, "Entro quanti giorni il Governo può impugnare una legge regionale davanti alla Corte costituzionale?",
  "Sessanta giorni dalla pubblicazione", ["Trenta giorni", "Novanta giorni", "Un anno"],
  "Lo stabilisce l'art. 127 della Costituzione.", "art. 127", "dinanzi alla Corte costituzionale entro sessanta giorni dalla sua pubblicazione")
K("cost-180", "Regioni ed enti locali", 4, "Con quale maggioranza il Consiglio regionale approva la sfiducia al Presidente della Giunta?",
  "Maggioranza assoluta dei componenti, con mozione firmata da almeno un quinto", ["Maggioranza semplice", "Due terzi", "Unanimità"],
  "Art. 126: l'approvazione comporta dimissioni della Giunta e scioglimento del Consiglio.", "art. 126", "sottoscritta da almeno un quinto dei suoi componenti e approvata per appello nominale a maggioranza assoluta")
K("cost-181", "Regioni ed enti locali", 5, "Quale minimo di abitanti serve per creare una nuova Regione secondo l'art. 132?",
  "Un milione", ["Cinquecentomila", "Due milioni", "Trecentomila"],
  "Serve legge costituzionale, richiesta di Consigli comunali e referendum delle popolazioni interessate.", "art. 132", "creazione di nuove Regioni con un minimo di un milione d'abitanti")
K("cost-182", "Regioni ed enti locali", 4, "Chi può istituire nuovi Comuni nel proprio territorio?",
  "La Regione, con sue leggi, sentite le popolazioni interessate", ["Lo Stato con decreto", "La Provincia", "Il prefetto"],
  "Art. 133, secondo comma.", "art. 133", "può con sue leggi istituire nel proprio territorio nuovi Comuni")
K("cost-183", "Corte costituzionale", 2, "Su cosa giudica la Corte costituzionale?",
  "Legittimità delle leggi, conflitti di attribuzione e accuse contro il Presidente della Repubblica", ["Ricorsi contro le multe", "Elezioni comunali", "Controversie di lavoro privato"],
  "Lo stabilisce l'art. 134 della Costituzione.", "art. 134", "La Corte costituzionale giudica: sulle controversie relative alla legittimità costituzionale delle leggi")
K("cost-184", "Corte costituzionale", 3, "Chi nomina i giudici della Corte costituzionale?",
  "Un terzo il Presidente della Repubblica, un terzo il Parlamento in seduta comune, un terzo le supreme magistrature", ["Tutti il Parlamento", "Tutti il Presidente della Repubblica", "Metà Governo, metà CSM"],
  "Art. 135, primo comma.", "art. 135", "nominati per un terzo dal Presidente della Repubblica")
K("cost-185", "Corte costituzionale", 4, "Dopo quanti anni di esercizio un avvocato può essere scelto come giudice costituzionale?",
  "Venti", ["Quindici", "Dieci", "Trenta"],
  "Art. 135: magistrati delle giurisdizioni superiori, professori ordinari di diritto e avvocati dopo venti anni.", "art. 135", "gli avvocati dopo venti anni di esercizio")
K("cost-186", "Corte costituzionale", 3, "Quanto dura in carica il Presidente della Corte costituzionale?",
  "Tre anni, ed è rieleggibile", ["Nove anni", "Un anno", "Sette anni"],
  "Art. 135: eletto dalla Corte tra i suoi componenti.", "art. 135", "il Presidente, che rimane in carica per un triennio, ed è rieleggibile")
K("cost-187", "Corte costituzionale", 5, "Quanti membri si aggiungono ai giudici ordinari della Corte nei giudizi d'accusa contro il Presidente della Repubblica?",
  "Sedici, tratti a sorte da un elenco compilato dal Parlamento", ["Cinque, nominati dal Senato", "Nessuno", "Dieci, designati dal CSM"],
  "Art. 135, ultimo comma.", "art. 135", "sedici membri tratti a sorte")
K("cost-188", "Corte costituzionale", 3, "Contro le decisioni della Corte costituzionale è ammessa impugnazione?",
  "No, non è ammessa alcuna impugnazione", ["Sì, alla Corte di cassazione", "Sì, alla Corte europea dei diritti dell'uomo", "Sì, con referendum"],
  "Art. 137, ultimo comma.", "art. 137", "Contro le decisioni della Corte costituzionale non è ammessa alcuna impugnazione")
K("cost-189", "Revisione costituzionale", 4, "Una legge costituzionale sottoposta a referendum quando non è promulgata?",
  "Se non è approvata dalla maggioranza dei voti validi", ["Se non vota la maggioranza degli aventi diritto", "Mai: è sempre promulgata", "Se non è approvata dai due terzi dei votanti"],
  "Art. 138: per il referendum costituzionale non c'è quorum di partecipazione.", "art. 138", "La legge sottoposta a referendum non è promulgata, se non è approvata dalla maggioranza dei voti validi")
K("cost-190", "Revisione costituzionale", 4, "Entro quanto tempo dalla pubblicazione si può chiedere il referendum su una legge costituzionale?",
  "Tre mesi", ["Sessanta giorni", "Un anno", "Sei mesi"],
  "Art. 138, secondo comma.", "art. 138", "entro tre mesi dalla loro pubblicazione")
K("cost-191", "Disposizioni transitorie", 3, "Cosa vieta la XII disposizione transitoria e finale?",
  "La riorganizzazione, sotto qualsiasi forma, del disciolto partito fascista", ["Il ritorno dei Savoia in Italia", "I titoli nobiliari", "Le leggi razziali"],
  "XII disposizione transitoria e finale.", "disp. trans. XII", "È vietata la riorganizzazione, sotto qualsiasi forma, del disciolto partito fascista")
K("cost-192", "Disposizioni transitorie", 2, "I titoli nobiliari sono riconosciuti dalla Costituzione?",
  "No, non sono riconosciuti", ["Sì, tutti", "Sì, solo quelli anteriori al 1861", "Sì, se registrati presso la Consulta araldica"],
  "XIV disposizione: i predicati anteriori al 28 ottobre 1922 valgono come parte del nome.", "disp. trans. XIV", "I titoli nobiliari non sono riconosciuti")
K("cost-193", "Disposizioni transitorie", 3, "Con l'entrata in vigore della Costituzione, chi assunse il titolo di Presidente della Repubblica?",
  "Il Capo provvisorio dello Stato", ["Il Presidente dell'Assemblea Costituente", "Il Presidente del Consiglio", "Il Re"],
  "I disposizione transitoria: il Capo provvisorio dello Stato (Enrico De Nicola) ne assume le attribuzioni e il titolo.", "disp. trans. I", "il Capo provvisorio dello Stato esercita le attribuzioni di Presidente della Repubblica e ne assume il titolo")
K("cost-194", "Disposizioni transitorie", 4, "Dove fu depositato il testo della Costituzione durante tutto il 1948, perché ogni cittadino potesse leggerlo?",
  "Nella sala comunale di ciascun Comune", ["In ogni scuola", "Nelle prefetture", "Nelle parrocchie"],
  "XVIII disposizione transitoria e finale.", "disp. trans. XVIII", "è depositato nella sala comunale di ciascun Comune della Repubblica")
K("cost-195", "Storia costituzionale", 2, "In che data fu promulgata la Costituzione?",
  "Il 27 dicembre 1947", ["Il 1° gennaio 1948", "Il 2 giugno 1946", "Il 22 dicembre 1948"],
  "La Costituzione fu data a Roma il 27 dicembre 1947 ed entrò in vigore il 1° gennaio 1948.", "disp. trans. XVIII", "Data a Roma, addì 27 dicembre 1947")
K("cost-196", "Principi fondamentali", 5, "Una legge regionale prevede che per accedere a un concorso regionale serva la residenza da dieci anni nella Regione. Con quale principio costituzionale contrasta più direttamente?",
  "Il divieto per le Regioni di limitare il diritto al lavoro in qualunque parte del territorio nazionale (art. 120)", ["Il principio di progressività tributaria", "La libertà di stampa", "Il diritto di sciopero"],
  "L'art. 120 vieta alla Regione di limitare l'esercizio del diritto al lavoro in qualunque parte del territorio nazionale; rilevano anche artt. 3 e 51.", "art. 120", "né limitare l'esercizio del diritto al lavoro in qualunque parte del territorio nazionale")
K("cost-197", "Parlamento", 5, "Un disegno di legge è assegnato a una commissione in sede deliberante. Chi può chiedere che torni all'esame dell'Assemblea?",
  "Il Governo, un decimo dei componenti della Camera o un quinto della commissione", ["Solo il Presidente della Repubblica", "Solo il Presidente della Camera", "Nessuno: la commissione decide in via definitiva"],
  "Art. 72, terzo comma.", "art. 72", "se il Governo o un decimo dei componenti della Camera o un quinto della commissione richiedono")
K("cost-198", "Formazione delle leggi", 5, "Le Camere dichiarano l'urgenza di una legge a maggioranza assoluta dei componenti. Cosa cambia per la promulgazione?",
  "La legge è promulgata nel termine stabilito dalla legge stessa", ["Non serve più la promulgazione", "La promulga il Presidente del Senato", "Entra in vigore senza pubblicazione"],
  "Art. 73, secondo comma.", "art. 73", "ne dichiarano l'urgenza, la legge è promulgata nel termine da essa stabilito")
K("cost-199", "Diritti e libertà", 5, "Il questore dispone una perquisizione domiciliare d'urgenza nei casi previsti dalla legge. Quali garanzie costituzionali si applicano?",
  "Quelle previste per la libertà personale: comunicazione e convalida dell'autorità giudiziaria nei termini di 48 ore", ["Nessuna, perché è un atto di polizia", "Solo l'autorizzazione del sindaco", "Solo la notifica al proprietario entro un mese"],
  "L'art. 14 rinvia alle garanzie prescritte per la libertà personale (art. 13).", "art. 14", "secondo le garanzie prescritte per la tutela della libertà personale")
K("cost-200", "Rapporti politici", 4, "A quale scopo la Repubblica, secondo l'art. 51, adotta appositi provvedimenti?",
  "Per promuovere le pari opportunità tra donne e uomini", ["Per garantire posti riservati ai partiti", "Per favorire i cittadini residenti", "Per limitare l'accesso ai pubblici uffici"],
  "Comma aggiunto dalla L. cost. 1/2003.", "art. 51", "la Repubblica promuove con appositi provvedimenti le pari opportunità tra donne e uomini")
