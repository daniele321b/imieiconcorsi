# Storia — fonti: voci di Wikipedia in italiano (CC BY-SA 4.0), usate solo per i fatti.
SI = "Wikipedia_Storia-d-Italia.txt"
RIS = "Wikipedia_Risorgimento.txt"
G1 = "Wikipedia_Prima-guerra-mondiale.txt"
FAS = "Wikipedia_Fascismo.txt"
G2 = "Wikipedia_Seconda-guerra-mondiale.txt"
REP = "Wikipedia_Storia-dell-Italia-repubblicana.txt"
GF = "Wikipedia_Guerra-fredda.txt"
UE = "Wikipedia_Storia-dell-Unione-europea.txt"
W = lambda voce: f"Wikipedia, «{voce}» (CC BY-SA 4.0)"

D("sto-001", "Medioevo", 1, "In che anno cadde l'Impero romano d'Occidente?",
  "476", ["410", "800", "1054"],
  "La caduta dell'Impero romano d'Occidente è fissata convenzionalmente al 476; seguirono Ostrogoti, Bizantini e Longobardi.",
  W("Storia d'Italia"), SI, "Dopo la caduta dell'Impero romano d'Occidente (476)")

D("sto-002", "Medioevo", 2, "Da quale papa e in che anno fu incoronato Carlo Magno?",
  "Da papa Leone III, nell'anno 800", ["Da papa Gregorio VII, nel 1077", "Da papa Gregorio Magno, nel 590", "Da papa Urbano II, nel 1095"],
  "Carlo Magno fu incoronato imperatore da papa Leone III nell'anno 800.",
  W("Storia d'Italia"), SI, "da parte di Papa Leone III nell'anno 800")

D("sto-003", "Età moderna", 3, "Quale trattato del 1454 chiuse la guerra tra Venezia e Milano e aprì la «politica dell'equilibrio»?",
  "La pace di Lodi", ["La pace di Cateau-Cambrésis", "Il trattato di Campoformio", "La pace di Westfalia"],
  "La pace di Lodi (9 aprile 1454) avviò l'equilibrio tra gli Stati italiani, poi difeso da Lorenzo il Magnifico.",
  W("Storia d'Italia"), SI, "La Pace di Lodi, firmata nella città lombarda il 9 aprile 1454")

D("sto-004", "Età moderna", 2, "Quale signore fiorentino del Quattrocento è legato alla «politica dell'equilibrio» tra gli Stati italiani?",
  "Lorenzo il Magnifico", ["Cosimo I de' Medici", "Ludovico il Moro", "Francesco Sforza"],
  "Nella seconda metà del Quattrocento Lorenzo il Magnifico fu il garante della politica dell'equilibrio.",
  W("Storia d'Italia"), SI, "Lorenzo il Magnifico, attuando la sua famosa politica dell'equilibrio")

D("sto-005", "Risorgimento", 2, "In che anno Carlo Alberto promulgò lo Statuto albertino?",
  "1848", ["1821", "1861", "1831"],
  "Il 4 marzo 1848 Carlo Alberto promulgò lo Statuto, che divenne poi la carta fondamentale del Regno d'Italia.",
  W("Risorgimento"), RIS, "il 4 marzo Carlo Alberto promulgò lo Statuto albertino")

D("sto-006", "Risorgimento", 1, "Quando fu proclamato il Regno d'Italia?",
  "Il 17 marzo 1861", ["Il 20 settembre 1870", "Il 2 giugno 1946", "Il 4 marzo 1848"],
  "La proclamazione del 17 marzo 1861 sancì la nascita dello Stato unitario.",
  W("Risorgimento"), RIS, "La proclamazione del Regno d'Italia del 17 marzo 1861")

D("sto-007", "Risorgimento", 2, "Con quale evento l'esercito italiano entrò a Roma il 20 settembre 1870?",
  "La breccia di Porta Pia", ["La spedizione dei Mille", "La battaglia di Solferino", "Il plebiscito di Napoli"],
  "La breccia di Porta Pia (20 settembre 1870) chiuse il processo risorgimentale; Roma divenne poi capitale.",
  W("Risorgimento"), RIS, "la breccia di Porta Pia da parte dell'esercito italiano (20 settembre 1870)")

D("sto-008", "Prima guerra mondiale", 2, "Quale evento del 28 giugno 1914 fece scoppiare la Prima guerra mondiale?",
  "L'assassinio dell'arciduca Francesco Ferdinando a Sarajevo", ["L'invasione del Belgio", "Lo sbarco degli Stati Uniti in Francia", "La rivoluzione russa"],
  "L'attentato di Sarajevo all'erede al trono austro-ungarico fu la causa scatenante del conflitto.",
  W("Prima guerra mondiale"), G1, "avvenuto il 28 giugno 1914 a Sarajevo")

D("sto-009", "Prima guerra mondiale", 3, "Con quale accordo segreto del 1915 l'Italia si impegnò a entrare in guerra a fianco dell'Intesa?",
  "Il Patto di Londra", ["La Triplice alleanza", "Il trattato di Versailles", "Il patto Gentiloni"],
  "Con il patto di Londra l'Italia si impegnava a entrare in guerra entro un mese, in cambio di concessioni territoriali.",
  W("Prima guerra mondiale"), G1, "la firma del patto di Londra")

D("sto-010", "Prima guerra mondiale", 2, "A quale Stato l'Italia dichiarò guerra il 24 maggio 1915?",
  "All'Austria-Ungheria", ["Alla Germania", "All'Impero ottomano", "Alla Francia"],
  "Il 24 maggio 1915 l'Italia dichiarò guerra all'Austria-Ungheria, ma inizialmente non alla Germania.",
  W("Prima guerra mondiale"), G1, "il 24 maggio fu dichiarata guerra all'Austria-Ungheria")

D("sto-011", "Prima guerra mondiale", 2, "Quale battaglia vittoriosa del 1918 portò l'Austria-Ungheria a chiedere l'armistizio?",
  "Vittorio Veneto", ["Caporetto", "Isonzo", "Piave del 1917"],
  "Dopo la vittoria italiana a Vittorio Veneto l'Austria-Ungheria chiese l'armistizio, firmato a Villa Giusti.",
  W("Prima guerra mondiale"), G1, "a seguito del successo italiano nella battaglia di Vittorio Veneto")

D("sto-012", "Prima guerra mondiale", 3, "Quale trattato firmato il 28 giugno 1919 stabilì la pace tra la Germania e le potenze alleate?",
  "Il trattato di Versailles", ["Il trattato di Saint-Germain", "Il trattato di Rapallo", "Il trattato di Brest-Litovsk"],
  "Il trattato di Versailles fu firmato il 28 giugno 1919; Saint-Germain riguardò l'Austria.",
  W("Prima guerra mondiale"), G1, "il 28 giugno 1919 venne firmato il trattato di Versailles")

D("sto-013", "Fascismo", 1, "In che data avvenne la marcia su Roma?",
  "28 ottobre 1922", ["3 gennaio 1925", "10 giugno 1924", "25 luglio 1943"],
  "Il 28 ottobre 1922 il fascismo marciò su Roma e Vittorio Emanuele III affidò il governo a Mussolini.",
  W("Fascismo"), FAS, "il 28 ottobre 1922 il Fascismo marciò su Roma")

D("sto-014", "Fascismo", 3, "Con il discorso del 3 gennaio 1925 Mussolini si assunse la responsabilità politica di quale delitto?",
  "Il delitto Matteotti", ["Il delitto Rosselli", "L'omicidio di Gramsci", "L'attentato di via Rasella"],
  "Con il discorso del 3 gennaio 1925 Mussolini si assunse la responsabilità del delitto Matteotti, avviando la dittatura.",
  W("Fascismo"), FAS, "del 3 gennaio 1925, con il quale si assunse la responsabilità politica del delitto Matteotti")

D("sto-015", "Fascismo", 2, "In che anno furono firmati i Patti Lateranensi tra Stato italiano e Chiesa?",
  "1929", ["1919", "1938", "1948"],
  "I Patti Lateranensi del 1929 chiusero la «questione romana».",
  W("Storia d'Italia"), SI, "con i Patti Lateranensi del 1929")

D("sto-016", "Fascismo", 4, "Cosa avvenne il 25 luglio 1943?",
  "Il Gran Consiglio del fascismo sfiduciò Mussolini, che fu poi arrestato", ["L'Italia firmò l'armistizio con gli Alleati", "Nacque la Repubblica sociale italiana", "Gli Alleati sbarcarono in Sicilia"],
  "Il 25 luglio 1943 l'ordine del giorno Grandi, con l'appoggio del Re, portò alla caduta di Mussolini.",
  W("Fascismo"), FAS, "Il 25 luglio 1943, per iniziativa di alcuni gerarchi (Grandi, Bottai e Ciano)")

D("sto-017", "Seconda guerra mondiale", 1, "Con quale evento iniziò la Seconda guerra mondiale?",
  "L'attacco della Germania alla Polonia, il 1° settembre 1939", ["L'attacco giapponese a Pearl Harbor", "L'annessione dell'Austria", "L'invasione dell'Unione Sovietica"],
  "Il conflitto iniziò il 1° settembre 1939 con l'attacco tedesco alla Polonia.",
  W("Seconda guerra mondiale"), G2, "con l'attacco della Germania nazista alla Polonia")

D("sto-018", "Seconda guerra mondiale", 2, "Quando l'Italia entrò nella Seconda guerra mondiale?",
  "Il 10 giugno 1940", ["Il 1° settembre 1939", "L'8 settembre 1943", "Il 22 giugno 1941"],
  "Il 10 giugno 1940 l'Italia entrò in guerra come alleata della Germania contro Francia e Regno Unito.",
  W("Storia d'Italia"), SI, "Il 10 giugno 1940 l'Italia entrò nella seconda guerra mondiale")

D("sto-019", "Seconda guerra mondiale", 3, "Come si chiama l'armistizio firmato il 3 settembre 1943 tra Italia e Alleati?",
  "Armistizio di Cassibile", ["Armistizio di Villa Giusti", "Armistizio di Compiègne", "Pace di Parigi"],
  "L'armistizio di Cassibile fu firmato il 3 settembre e reso noto l'8 settembre 1943.",
  W("Seconda guerra mondiale"), G2, "alla stipula dell'armistizio di Cassibile il 3 settembre")

D("sto-020", "Seconda guerra mondiale", 2, "Quando terminò la Seconda guerra mondiale in Europa?",
  "L'8 maggio 1945, con la resa tedesca", ["Il 25 aprile 1945", "Il 2 settembre 1945", "Il 6 giugno 1944"],
  "In Europa la guerra finì l'8 maggio 1945; in Asia il 2 settembre, con la resa del Giappone.",
  W("Seconda guerra mondiale"), G2, "nel teatro europeo, l'8 maggio 1945, con la resa tedesca")

D("sto-021", "Seconda guerra mondiale", 2, "Su quali città gli Stati Uniti sganciarono le bombe atomiche nel 1945?",
  "Hiroshima e Nagasaki", ["Tokyo e Osaka", "Kyoto e Kobe", "Hiroshima e Okinawa"],
  "La resa del Giappone seguì i bombardamenti atomici di Hiroshima e Nagasaki.",
  W("Seconda guerra mondiale"), G2, "dopo i bombardamenti atomici di Hiroshima e Nagasaki")

D("sto-022", "Repubblica", 1, "Con quale voto gli italiani scelsero la Repubblica?",
  "Il referendum istituzionale del 2 e 3 giugno 1946", ["Le elezioni politiche del 1948", "Un voto dell'Assemblea Costituente", "Il plebiscito del 1861"],
  "Nel referendum del 2-3 giugno 1946, il primo a cui votarono le donne, gli italiani scelsero la Repubblica.",
  W("Storia d'Italia"), SI, "Col referendum istituzionale del 2 e 3 giugno 1946")

D("sto-023", "Repubblica", 2, "Il referendum del 1946 fu la prima consultazione nazionale in cui votarono:",
  "anche le donne", ["anche i diciottenni", "anche gli italiani all'estero", "anche i militari in servizio"],
  "Nel referendum istituzionale del 1946 per la prima volta votarono anche le donne italiane.",
  W("Storia d'Italia"), SI, "per la prima volta anche le donne italiane ebbero il diritto al voto")

D("sto-024", "Repubblica", 3, "Chi fu il primo Presidente della Repubblica Italiana, con piene funzioni dal 1° gennaio 1948?",
  "Enrico De Nicola", ["Luigi Einaudi", "Alcide De Gasperi", "Giovanni Gronchi"],
  "Enrico De Nicola, già Capo provvisorio dello Stato, assunse le piene funzioni di Presidente il 1° gennaio 1948. Luigi Einaudi fu il primo eletto secondo la Costituzione.",
  W("Storia dell'Italia repubblicana"), REP, "e piene funzioni di Presidente della Repubblica Italiana il 1o gennaio 1948")

D("sto-025", "Repubblica", 3, "Quale inchiesta giudiziaria del 1992 segnò la fine della cosiddetta «prima repubblica»?",
  "Mani pulite", ["Piazza Fontana", "P2", "Calciopoli"],
  "Nel 1992 le indagini della magistratura di Milano, note come Mani pulite, travolsero il sistema dei partiti.",
  W("Storia dell'Italia repubblicana"), REP, "L'inchiesta \"Mani pulite\" e la fine della prima repubblica")

D("sto-026", "Repubblica", 4, "Quale periodo della storia repubblicana va convenzionalmente dal 1963 al 1981 ed è segnato dal terrorismo?",
  "Il centro-sinistra e gli anni di piombo", ["Il centrismo", "Il boom economico", "La seconda repubblica"],
  "La voce colloca nel 1963-1981 il centro-sinistra e gli anni di piombo.",
  W("Storia dell'Italia repubblicana"), REP, "Il centro-sinistra e gli anni di piombo (1963-1981)")

D("sto-027", "Guerra fredda", 2, "Con quali eventi si chiude convenzionalmente la Guerra fredda?",
  "La caduta del Muro di Berlino (1989) e la dissoluzione dell'URSS (1991)", ["La crisi dei missili di Cuba (1962)", "La fine della guerra di Corea (1953)", "La nascita della NATO (1949)"],
  "La Guerra fredda termina con la caduta del Muro (1989) e la dissoluzione dell'Unione Sovietica (1991).",
  W("Guerra fredda"), GF, "terminato con la caduta del Muro di Berlino (1989) e con la conseguente dissoluzione dell'Unione Sovietica (1991)")

D("sto-028", "Guerra fredda", 3, "Con quale alleanza l'URSS rispose nel 1955 alla nascita della NATO?",
  "Il Patto di Varsavia", ["Il Comecon", "Il Cominform", "Il Patto di Monaco"],
  "La NATO nasce nel 1949; nel 1955 l'URSS risponde con il Patto di Varsavia.",
  W("Guerra fredda"), GF, "con il Patto di Varsavia nel 1955")

D("sto-029", "Integrazione europea", 2, "Quali comunità istituirono i Trattati di Roma del 1957?",
  "La CEE e l'EURATOM", ["La CECA e la NATO", "L'Unione europea e l'euro", "Il Consiglio d'Europa e la CEDU"],
  "I Trattati di Roma del 1957 istituirono la Comunità economica europea e l'EURATOM.",
  W("Storia dell'Unione europea"), UE, "I Trattati di Roma, istitutivi della CEE (Comunità economica europea) e dell'EURATOM")

D("sto-030", "Integrazione europea", 3, "Quale fu la prima comunità europea, nata dal piano Schuman e ideata da Jean Monnet?",
  "La CECA (Comunità europea del carbone e dell'acciaio)", ["La CEE", "L'EURATOM", "L'EFTA"],
  "La CECA, prevista dal piano Schuman e ideata da Jean Monnet, fu la prima comunità; il trattato fu ratificato nel 1951.",
  W("Storia dell'Unione europea"), UE, "Ideata da Jean Monnet, la CECA")


# --- Blocco 2: dall'Italia antica all'Impero (voce «Storia d'Italia») ---
def S(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, "Wikipedia, «Storia d'Italia» (CC BY-SA 4.0)", SI, frase)

S("sto-031", "Età antica", 2, "Quale editto del 313 garantì la libertà di culto nell'Impero romano?",
  "L'editto di Milano", ["L'editto di Tessalonica", "L'editto di Caracalla", "L'editto di Nantes"],
  "L'editto di Tessalonica (380) impose invece la religione del vescovo di Roma.",
  "la promulgazione dell'editto di Milano (313), che garantiva la libertà di culto")

S("sto-032", "Medioevo", 2, "Quale popolo guidato da Alboino invase l'Italia nel 568?",
  "I Longobardi", ["Gli Ostrogoti", "I Visigoti", "I Franchi"],
  "Dopo il 476 l'Italia fu invasa da Ostrogoti (492), Bizantini (535) e Longobardi (568).",
  "dai Longobardi di Alboino (568)")

S("sto-033", "Medioevo", 3, "Chi guidava gli Ostrogoti che invasero l'Italia nel 492?",
  "Teodorico", ["Alarico", "Odoacre", "Attila"],
  "Voce «Storia d'Italia».",
  "dagli Ostrogoti di Teodorico (492)")

S("sto-034", "Medioevo", 3, "Quale sovrano unì nel Medioevo la corona di Sicilia e il diadema imperiale?",
  "Federico II di Svevia", ["Carlo Magno", "Ruggero II", "Ottone I"],
  "Voce «Storia d'Italia».",
  "pervennero entrambi a Federico II di Svevia")

S("sto-035", "Medioevo", 2, "Quale popolo unificò il Mezzogiorno nel regno di Sicilia?",
  "I Normanni", ["I Longobardi", "Gli Arabi", "Gli Angioini"],
  "Voce «Storia d'Italia».",
  "il Mezzogiorno veniva unificato nel regno di Sicilia dai Normanni")

S("sto-036", "Età antica", 1, "Secondo la tradizione, in che anno fu fondata Roma?",
  "Nel 753 a.C.", ["Nel 509 a.C.", "Nel 476 d.C.", "Nel 27 a.C."],
  "Secondo la tradizione Roma fu fondata il 21 aprile 753 a.C. da Romolo sul Palatino.",
  "fu fondata il 21 aprile del 753 a.C. da Romolo sul colle Palatino")

S("sto-037", "Età antica", 2, "Quanti re governarono Roma secondo la tradizione, fino al 509 a.C.?",
  "Sette", ["Cinque", "Dodici", "Tre"],
  "Voce «Storia d'Italia».",
  "da sette re")

S("sto-038", "Età antica", 3, "Quale re di Roma istituì i primi collegi sacerdotali, come quello delle Vestali?",
  "Numa Pompilio", ["Romolo", "Tullo Ostilio", "Tarquinio il Superbo"],
  "Voce «Storia d'Italia».",
  "Numa Pompilio, istituì i primi collegi sacerdotali")

S("sto-039", "Età antica", 3, "A quale re di Roma la tradizione attribuisce la fondazione del porto di Ostia?",
  "Anco Marzio", ["Servio Tullio", "Numa Pompilio", "Tarquinio Prisco"],
  "Voce «Storia d'Italia».",
  "Anco Marzio, costruì il primo ponte di legno sul Tevere")

S("sto-040", "Età antica", 3, "Chi fu l'ultimo re di Roma, espulso nel 510 a.C.?",
  "Tarquinio il Superbo", ["Tarquinio Prisco", "Servio Tullio", "Anco Marzio"],
  "Voce «Storia d'Italia».",
  "Ultimo monarca a governare Roma fu Tarquinio il Superbo")

S("sto-041", "Età antica", 3, "A quale re etrusco la tradizione attribuisce l'ordinamento centuriato?",
  "Servio Tullio", ["Tarquinio il Superbo", "Romolo", "Numa Pompilio"],
  "Voce «Storia d'Italia».",
  "Servio Tullio, fu, secondo la leggenda, l'ideatore dell'ordinamento centuriato")

S("sto-042", "Età antica", 3, "In che anno furono redatte le leggi delle XII tavole?",
  "Nel 450 a.C.", ["Nel 753 a.C.", "Nel 133 a.C.", "Nel 27 a.C."],
  "Voce «Storia d'Italia».",
  "nel 450 a.C. da parte dei decemviri, delle")

S("sto-043", "Età antica", 3, "Quale magistratura nacque dopo la secessione della plebe sul Monte Sacro (494 a.C.)?",
  "Il tribunato della plebe", ["La dittatura", "La censura", "Il consolato"],
  "Voce «Storia d'Italia».",
  "con l'istituzione della magistratura del tribunato della plebe")

S("sto-044", "Età antica", 3, "In quale celebre episodio i Sanniti inflissero una disfatta umiliante ai Romani?",
  "Le Forche Caudine", ["Canne", "Zama", "Azio"],
  "Avvenne durante la seconda guerra sannitica.",
  "celebre quella delle Forche Caudine")

S("sto-045", "Età antica", 3, "Quale re d'Epiro venne in aiuto di Taranto contro Roma?",
  "Pirro", ["Annibale", "Filippo V", "Mitridate"],
  "Fu sconfitto a Maleventum nel 275 a.C.",
  "re d'Epiro Pirro")

S("sto-046", "Età antica", 2, "Quali territori annesse Roma dopo la prima guerra punica (241 a.C.)?",
  "Sicilia, Sardegna e Corsica", ["Spagna e Africa", "Grecia e Macedonia", "Gallia e Britannia"],
  "Voce «Storia d'Italia».",
  "annettendo Sicilia, Sardegna e Corsica")

S("sto-047", "Età antica", 2, "In quale battaglia del 216 a.C. Annibale sconfisse duramente i Romani?",
  "Canne", ["Zama", "Azio", "Farsalo"],
  "Voce «Storia d'Italia».",
  "nella battaglia di Canne (216")

S("sto-048", "Età antica", 2, "Chi sconfisse Annibale a Zama?",
  "Publio Cornelio Scipione", ["Quinto Fabio Massimo", "Marco Attilio Regolo", "Gaio Mario"],
  "Voce «Storia d'Italia».",
  "sconfisse Annibale, nel frattempo tornato a Cartagine, nella battaglia di Zama")

S("sto-049", "Età antica", 3, "Perché Quinto Fabio Massimo era detto «il temporeggiatore»?",
  "Perché evitava lo scontro diretto con Annibale per far riorganizzare Roma", ["Perché arrivava sempre in ritardo", "Perché governò per pochi giorni", "Perché rinviò le elezioni"],
  "Voce «Storia d'Italia».",
  "Quinto Fabio Massimo, detto il temporeggiatore")

S("sto-050", "Età antica", 4, "Quale politico romano si oppose all'ellenizzazione dei costumi in nome del mos maiorum?",
  "Catone il Censore", ["Cicerone", "Scipione l'Africano", "Tiberio Gracco"],
  "Voce «Storia d'Italia».",
  "Marco Porcio Catone detto il Censore")

S("sto-051", "Età antica", 3, "Cosa prevedeva la riforma dei fratelli Gracchi?",
  "Limitare l'occupazione delle terre pubbliche e redistribuire le eccedenze ai contadini", ["Abolire la schiavitù", "Estendere il voto alle donne", "Trasferire la capitale"],
  "Voce «Storia d'Italia».",
  "la limitazione dell'occupazione delle terre dello Stato a 125 ettari")

S("sto-052", "Età antica", 4, "Cosa ottennero gli alleati italici dopo la guerra sociale (91-88 a.C.)?",
  "La cittadinanza romana", ["L'indipendenza", "Il diritto di battere moneta", "L'esenzione dalle tasse"],
  "Voce «Storia d'Italia».",
  "Gli italici si videro comunque riconosciuta la cittadinanza romana")

S("sto-053", "Età antica", 2, "Chi guidò la terza guerra servile, scoppiata a Capua nel 73 a.C.?",
  "Spartaco", ["Giugurta", "Vercingetorige", "Catilina"],
  "La rivolta fu schiacciata da Crasso nel 71 a.C.",
  "condotta dallo schiavo e gladiatore Spartaco")

S("sto-054", "Età antica", 3, "Chi formò il primo triumvirato?",
  "Cesare, Crasso e Pompeo", ["Ottaviano, Antonio e Lepido", "Mario, Silla e Cinna", "Bruto, Cassio e Cicerone"],
  "Voce «Storia d'Italia».",
  "Cesare, Crasso e Pompeo, si spartivano le sfere d'influenza")

S("sto-055", "Età antica", 2, "Quale fiume attraversò Cesare nel 49 a.C. dando inizio alla guerra civile?",
  "Il Rubicone", ["Il Tevere", "Il Po", "L'Arno"],
  "«Alea iacta est».",
  "Cesare attraversò con le sue truppe il Rubicone")

S("sto-056", "Età antica", 2, "Quando fu ucciso Giulio Cesare?",
  "Alle idi di marzo del 44 a.C.", ["Nel 31 a.C. ad Azio", "Nel 27 a.C.", "Nel 49 a.C."],
  "Voce «Storia d'Italia».",
  "ucciso alle idi di marzo nel 44 a.C.")

S("sto-057", "Età antica", 2, "Quale battaglia del 31 a.C. decretò il trionfo di Ottaviano su Marco Antonio?",
  "Azio", ["Filippi", "Farsalo", "Munda"],
  "Voce «Storia d'Italia».",
  "terminò con la Battaglia di Azio nel 31 a.C.")

S("sto-058", "Età antica", 3, "In quante regioni Augusto divise l'Italia nel 7 d.C.?",
  "Undici", ["Venti", "Sette", "Quattordici"],
  "Roma città fu invece divisa in 14 regioni.",
  "Augusto, divise l'Italia in undici regioni")

S("sto-059", "Età antica", 3, "Quale dinastia imperiale comprese Tiberio, Caligola, Claudio e Nerone?",
  "La dinastia Giulio-Claudia", ["La dinastia Flavia", "La dinastia degli Antonini", "La dinastia dei Severi"],
  "Voce «Storia d'Italia».",
  "nel corso di mezzo secolo si succedettero Tiberio, Caligola, Claudio e Nerone")

S("sto-060", "Età antica", 3, "Sotto quale imperatore fu conquistata la Britannia, a partire dal 43?",
  "Claudio", ["Nerone", "Traiano", "Augusto"],
  "Voce «Storia d'Italia».",
  "riorganizzò la burocrazia e conquistò la Britannia")

S("sto-061", "Età antica", 3, "Come è ricordato il 69 d.C.?",
  "L'anno dei quattro imperatori", ["L'anno della fondazione di Costantinopoli", "L'anno dell'eruzione del Vesuvio", "L'anno della morte di Augusto"],
  "Galba, Otone, Vitellio e Vespasiano.",
  "noto come anno dei quattro imperatori")

S("sto-062", "Età antica", 2, "Quale evento distrusse Pompei ed Ercolano nel 79 d.C.?",
  "L'eruzione del Vesuvio", ["Un terremoto in Sicilia", "Un'invasione barbarica", "Un incendio appiccato da Nerone"],
  "Avvenne sotto l'imperatore Tito.",
  "nel 79 l'eruzione del Vesuvio distrusse Pompei ed Ercolano")

S("sto-063", "Età antica", 3, "Quale dinastia fece costruire il Colosseo (anfiteatro Flavio)?",
  "La dinastia Flavia (Vespasiano)", ["La dinastia Giulio-Claudia", "La dinastia dei Severi", "La dinastia Costantiniana"],
  "Voce «Storia d'Italia».",
  "realizzare numerose opere pubbliche, come il Colosseo")

S("sto-064", "Età antica", 3, "Sotto quale imperatore l'Impero romano raggiunse la massima estensione (117)?",
  "Traiano", ["Adriano", "Augusto", "Costantino"],
  "Voce «Storia d'Italia».",
  "l'Impero raggiunse la sua massima estensione (117)")

S("sto-065", "Età antica", 4, "Come si chiamava il sistema di successione degli imperatori introdotto da Nerva?",
  "Principato adottivo", ["Tetrarchia", "Dominato", "Monarchia ereditaria"],
  "Voce «Storia d'Italia».",
  "principato adottivo")

S("sto-066", "Età antica", 4, "Quale imperatore avviò nel 284 la fase del «Dominato»?",
  "Diocleziano", ["Costantino", "Augusto", "Marco Aurelio"],
  "Voce «Storia d'Italia».",
  "l'imperatore Diocleziano, incominciò una nuova fase, il Dominato")

S("sto-067", "Età antica", 3, "Quale popolo di lingua non indoeuropea sviluppò dal IX secolo a.C. una raffinata civiltà nell'Italia centrale tirrenica?",
  "Gli Etruschi", ["I Sanniti", "I Liguri", "I Veneti"],
  "Voce «Storia d'Italia».",
  "Le origini di questo popolo di lingua non indoeuropea")

S("sto-068", "Età antica", 3, "Quale civiltà sviluppò in Sardegna l'elemento etnico degli antichi Sardi?",
  "La civiltà nuragica", ["La civiltà villanoviana", "La civiltà etrusca", "La civiltà micenea"],
  "Voce «Storia d'Italia».",
  "avevano dato vita alla civiltà nuragica")

S("sto-069", "Età antica", 3, "Come chiamarono gli storici romani l'Italia meridionale colonizzata dai Greci?",
  "Magna Grecia", ["Gallia Cisalpina", "Italia annonaria", "Ellade minore"],
  "Voce «Storia d'Italia».",
  "con l'appellativo di Magna Grecia")

S("sto-070", "Età antica", 4, "Quali coloni fondarono Siracusa?",
  "I Corinzi", ["Gli Spartani", "Gli Eubei", "Gli Ateniesi"],
  "Gli Spartani fondarono Taranto, gli Eubei Cuma e Napoli.",
  "i Corinzi Siracusa")

# --- Blocco 3: dal tardo Impero al Rinascimento (voce «Storia d'Italia») ---
S("sto-071", "Età antica", 3, "Quale imperatore concesse nel 212 la cittadinanza romana a tutti gli abitanti dell'Impero?",
  "Caracalla", ["Augusto", "Costantino", "Adriano"],
  "Voce «Storia d'Italia».",
  "Nel 212 Caracalla concesse la cittadinanza")

S("sto-072", "Età antica", 3, "Quale imperatore istituì la Tetrarchia?",
  "Diocleziano", ["Costantino", "Teodosio", "Settimio Severo"],
  "Due Augusti e due Cesari che amministravano gruppi distinti di province.",
  "La crisi del III secolo venne frenata dall'imperatore Diocleziano")

S("sto-073", "Età antica", 2, "Quale città fondò Costantino nel 330 come seconda capitale?",
  "Costantinopoli, sull'antico sito di Bisanzio", ["Ravenna", "Milano", "Treviri"],
  "Voce «Storia d'Italia».",
  "da lui ridenominata Costantinopoli (330)")

S("sto-074", "Età antica", 3, "Sotto quale imperatore il cristianesimo divenne religione ufficiale dell'Impero (380)?",
  "Teodosio I", ["Costantino", "Giuliano", "Nerone"],
  "Voce «Storia d'Italia».",
  "sotto il regno di Teodosio I")

S("sto-075", "Età antica", 3, "In che anno l'Impero si divise definitivamente in Occidente e Oriente, alla morte di Teodosio?",
  "Nel 395", ["Nel 476", "Nel 313", "Nel 1054"],
  "Voce «Storia d'Italia».",
  "Nel 395, alla morte di Teodosio, l'Impero si trovò definitivamente suddiviso")

S("sto-076", "Età antica", 2, "Quale popolo saccheggiò Roma nel 410, guidato da Alarico?",
  "I Visigoti", ["I Vandali", "Gli Unni", "I Longobardi"],
  "Voce «Storia d'Italia».",
  "il sacco di Roma del 410 per opera dei Visigoti di Alarico I")

S("sto-077", "Età antica", 3, "Quale invasione del 452 provocò la fuga delle popolazioni nella laguna e la nascita di Venezia?",
  "Quella degli Unni di Attila", ["Quella dei Vandali di Genserico", "Quella degli Ostrogoti", "Quella dei Franchi"],
  "Voce «Storia d'Italia».",
  "Nel 452 gli Unni di Attila invasero il nord Italia")

S("sto-078", "Età antica", 2, "Chi depose nel 476 l'ultimo imperatore d'Occidente, Romolo Augusto?",
  "Odoacre", ["Teodorico", "Alarico", "Attila"],
  "Odoacre non si proclamò imperatore ma re d'Italia.",
  "capeggiata da Odoacre che")

S("sto-079", "Medioevo", 4, "Quale filosofo fu condannato a morte nel 524 durante le persecuzioni di Teodorico?",
  "Severino Boezio", ["Cassiodoro", "Sant'Agostino", "Tommaso d'Aquino"],
  "Voce «Storia d'Italia».",
  "il filosofo Severino Boezio, condannato a morte nel 524")

S("sto-080", "Medioevo", 3, "Quale imperatore d'Oriente avviò nel 535 la guerra gotica per riconquistare l'Italia?",
  "Giustiniano", ["Costantino", "Teodosio", "Eraclio"],
  "Con i generali Belisario e Narsete.",
  "il nuovo e ambizioso imperatore d'Oriente Giustiniano")

S("sto-081", "Medioevo", 3, "Chi fondò nel 529 l'abbazia di Montecassino?",
  "San Benedetto da Norcia", ["San Francesco d'Assisi", "San Romualdo", "Papa Gregorio Magno"],
  "Voce «Storia d'Italia».",
  "Nel 529 san Benedetto da Norcia fonda l'Abbazia di Montecassino")

S("sto-082", "Medioevo", 3, "Quale città divenne stabilmente capitale del regno longobardo?",
  "Pavia", ["Milano", "Ravenna", "Benevento"],
  "Voce «Storia d'Italia».",
  "Pavia divenne stabilmente capitale del regno Longobardo")

S("sto-083", "Medioevo", 3, "Come si chiama la prima raccolta di leggi scritte longobarde (643)?",
  "Editto di Rotari", ["Codice di Giustiniano", "Capitolare di Quierzy", "Constitutio de feudis"],
  "Voce «Storia d'Italia».",
  "Editto di Rotari, 643")

S("sto-084", "Medioevo", 4, "Quale regina avviò la conversione dei Longobardi al cattolicesimo?",
  "Teodolinda", ["Adelaide", "Matilde di Canossa", "Galla Placidia"],
  "Voce «Storia d'Italia».",
  "per opera della regina Teodolinda")

S("sto-085", "Medioevo", 4, "Quale atto del 728 è considerato l'origine del potere temporale dei papi?",
  "La Donazione di Sutri", ["La Donazione di Costantino", "Il Concordato di Worms", "La Prammatica Sanzione"],
  "Con essa il re longobardo Liutprando cedette alcuni castelli al papa.",
  "ricordato come la Donazione di Sutri")

S("sto-086", "Medioevo", 3, "Quale re dei Franchi sconfisse Astolfo e donò al papa le terre dell'esarcato di Ravenna?",
  "Pipino il Breve", ["Carlo Magno", "Clodoveo", "Carlo Martello"],
  "Nacque così lo Stato della Chiesa.",
  "il re dei Franchi Pipino il Breve")

S("sto-087", "Medioevo", 3, "In che anno Carlo Magno sconfisse definitivamente i Longobardi di Desiderio?",
  "Nel 774", ["Nel 800", "Nel 568", "Nel 962"],
  "Assunse il titolo di Re dei Franchi e dei Longobardi.",
  "si concluse nel 774 con la vittoria di Carlo")

S("sto-088", "Medioevo", 3, "Dove sbarcarono per la prima volta gli Arabi in Sicilia, nell'827?",
  "A Mazara del Vallo", ["A Palermo", "A Siracusa", "A Messina"],
  "Voce «Storia d'Italia».",
  "anno del loro primo sbarco a Mazara del Vallo")

S("sto-089", "Medioevo", 4, "Quale battaglia del 915 fermò definitivamente l'espansione saracena nella penisola?",
  "La battaglia del Garigliano", ["La battaglia di Ostia", "La battaglia di Lepanto", "La battaglia di Legnano"],
  "Voce «Storia d'Italia».",
  "battaglia del Garigliano del 915")

S("sto-090", "Medioevo", 3, "Quale imperatore tedesco si cinse della corona italiana nel 951, sposando Adelaide?",
  "Ottone I", ["Federico Barbarossa", "Enrico IV", "Carlo Magno"],
  "Voce «Storia d'Italia».",
  "si cinse della corona italiana nel 951")

S("sto-091", "Medioevo", 3, "Quali documenti (960-963) contengono le prime frasi ufficiali in volgare italiano?",
  "I Placiti cassinesi", ["Il Cantico delle creature", "L'Editto di Rotari", "Le Costituzioni di Melfi"],
  "Voce «Storia d'Italia».",
  "risalgono i Placiti cassinesi")

S("sto-092", "Medioevo", 2, "Quali sono le quattro repubbliche marinare più note, i cui stemmi compaiono nella bandiera della Marina?",
  "Amalfi, Genova, Pisa e Venezia", ["Genova, Napoli, Bari e Venezia", "Ancona, Gaeta, Noli e Ragusa", "Pisa, Livorno, Trieste e Venezia"],
  "Voce «Storia d'Italia».",
  "Amalfi, Genova, Pisa e Venezia")

S("sto-093", "Medioevo", 3, "Quale papa bandì la prima crociata?",
  "Urbano II", ["Gregorio VII", "Innocenzo III", "Bonifacio VIII"],
  "La prima crociata conquistò Gerusalemme nel 1099.",
  "Papa Urbano II (1088-1099)")

S("sto-094", "Medioevo", 3, "Con quale accordo del 1122 si chiuse la lotta per le investiture?",
  "Il concordato di Worms", ["La pace di Costanza", "La pace di Lodi", "Il trattato di Verdun"],
  "Voce «Storia d'Italia».",
  "Nel 1122 si arrivò al compromesso di Worms")

S("sto-095", "Medioevo", 3, "Quale imperatore subì l'«umiliazione di Canossa»?",
  "Enrico IV", ["Federico II", "Ottone III", "Enrico VII"],
  "Voce «Storia d'Italia».",
  "Umiliazione di Canossa dell'imperatore Enrico IV")

S("sto-096", "Medioevo", 2, "In che anno nacque l'Università di Bologna secondo la voce di Wikipedia?",
  "Nel 1088", ["Nel 1222", "Nel 962", "Nel 1303"],
  "Voce «Storia d'Italia».",
  "1088 segue la nascita quella di Bologna")

S("sto-097", "Medioevo", 3, "Chi riunì nel 1130 i possedimenti normanni creando il Regno di Sicilia?",
  "Ruggero II", ["Roberto il Guiscardo", "Federico II", "Tancredi di Lecce"],
  "Voce «Storia d'Italia».",
  "Nel 1130 Ruggero II riuscì a riunire nelle sue mani tutti i possedimenti normanni")

S("sto-098", "Medioevo", 3, "Quale magistrato forestiero fu introdotto nei comuni per porre fine alle lotte interne?",
  "Il podestà", ["Il console", "Il doge", "Il gonfaloniere"],
  "Voce «Storia d'Italia».",
  "il podestà, scelto tra i forestieri")

S("sto-099", "Medioevo", 2, "In quale battaglia la Lega Lombarda sconfisse Federico Barbarossa nel 1176?",
  "Legnano", ["Montaperti", "Benevento", "Campaldino"],
  "Con la pace di Costanza (1183) l'imperatore riconobbe l'autonomia dei comuni.",
  "battaglia di Legnano (1176)")

S("sto-100", "Medioevo", 3, "Oltre a Roma, quale città è citata nell'inno nazionale italiano?",
  "Legnano", ["Milano", "Torino", "Firenze"],
  "Voce «Storia d'Italia».",
  "Legnano è l'unica città, oltre a Roma, a essere citata")

S("sto-101", "Medioevo", 2, "Chi è l'autore del Decameron?",
  "Giovanni Boccaccio", ["Dante Alighieri", "Francesco Petrarca", "Guido Cavalcanti"],
  "Voce «Storia d'Italia».",
  "Giovanni Boccaccio, autore del Decameron")

S("sto-102", "Medioevo", 4, "Quale re di Francia si scontrò con Bonifacio VIII, fino allo «schiaffo di Anagni» (1303)?",
  "Filippo IV il Bello", ["Luigi IX", "Carlo VIII", "Francesco I"],
  "Voce «Storia d'Italia».",
  "Filippo IV il Bello, re di Francia")

S("sto-103", "Medioevo", 3, "Dove fu trasferita la sede papale nel 1305 da Clemente V?",
  "Ad Avignone", ["A Parigi", "A Viterbo", "A Lione"],
  "La «cattività avignonese» terminò nel 1377 con Gregorio XI.",
  "Clemente V spostò la sede papale in Francia, ad Avignone")

S("sto-104", "Medioevo", 4, "Quale concilio pose fine allo Scisma d'Occidente?",
  "Il Concilio di Costanza (1414)", ["Il Concilio di Trento", "Il Concilio di Pisa", "Il Concilio di Nicea"],
  "Voce «Storia d'Italia».",
  "col Concilio di Costanza (1414)")

S("sto-105", "Medioevo", 4, "Chi guidò la breve repubblica romana del 1347-1354?",
  "Cola di Rienzo", ["Arnaldo da Brescia", "Stefano Porcari", "Girolamo Savonarola"],
  "Voce «Storia d'Italia».",
  "guidata da Cola di Rienzo")

S("sto-106", "Medioevo", 3, "Quale rivolta scoppiò a Palermo nel 1282 contro gli Angioini?",
  "I Vespri siciliani", ["La congiura dei Pazzi", "Il tumulto dei Ciompi", "La rivolta di Masaniello"],
  "Si conclusero con la pace di Caltabellotta (1302).",
  "dando così inizio ai Vespri siciliani")

S("sto-107", "Medioevo", 4, "Quale signore di Milano ottenne nel 1395 il titolo ereditario di duca?",
  "Gian Galeazzo Visconti", ["Ludovico il Moro", "Francesco Sforza", "Giovanni Visconti"],
  "Voce «Storia d'Italia».",
  "Gian Galeazzo Visconti cercò con ogni sforzo")

S("sto-108", "Età moderna", 3, "In che anno Cosimo de' Medici affermò il proprio controllo su Firenze?",
  "Nel 1434", ["Nel 1492", "Nel 1378", "Nel 1569"],
  "Voce «Storia d'Italia».",
  "Nel 1434, Cosimo de' Medici seppe abilmente sfruttare tali divisioni")

S("sto-109", "Medioevo", 4, "Chi istituì il Ducato di Savoia nel 1416?",
  "Amedeo VIII, designato duca dall'imperatore Sigismondo", ["Umberto Biancamano", "Emanuele Filiberto", "Carlo Alberto"],
  "Voce «Storia d'Italia».",
  "Amedeo VIII, fu designato duca dall'imperatore Sigismondo nel 1416")

S("sto-110", "Età moderna", 4, "Quale città pugliese fu conquistata dai Turchi nel 1480?",
  "Otranto", ["Bari", "Brindisi", "Taranto"],
  "Fu riconquistata dagli Aragonesi dopo tredici mesi.",
  "la città di Otranto fu conquistata dai turchi")

# --- Blocco 4: età moderna e napoleonica (voce «Storia d'Italia») ---
S("sto-111", "Età moderna", 3, "Quale re di Francia scese in Italia nel 1494, avviando le guerre d'Italia?",
  "Carlo VIII", ["Luigi XII", "Francesco I", "Enrico II"],
  "Il 1494 segna la fine della politica dell'equilibrio.",
  "re di Francia Carlo VIII")

S("sto-112", "Età moderna", 3, "In quale battaglia del 1495 la lega antifrancese costrinse Carlo VIII a ritirarsi?",
  "Fornovo", ["Marignano", "Pavia", "Agnadello"],
  "Voce «Storia d'Italia».",
  "Battaglia di Fornovo")

S("sto-113", "Età moderna", 4, "Quale episodio celebre avvenne durante il conflitto franco-spagnolo per Napoli all'inizio del Cinquecento?",
  "La disfida di Barletta", ["Il sacco di Roma", "I Vespri siciliani", "La congiura dei Pazzi"],
  "Voce «Storia d'Italia».",
  "avvenne la disfida di Barletta")

S("sto-114", "Età moderna", 4, "Contro quale Stato fu stipulata nel 1508 la Lega di Cambrai?",
  "La Repubblica di Venezia", ["Il Regno di Francia", "Lo Stato della Chiesa", "Il Ducato di Milano"],
  "Promossa da papa Giulio II.",
  "contro la Repubblica di Venezia")

S("sto-115", "Età moderna", 3, "In quale battaglia del 1525 fu fatto prigioniero il re di Francia Francesco I?",
  "Pavia", ["Marignano", "Fornovo", "Lepanto"],
  "Voce «Storia d'Italia».",
  "di Pavia, durante la quale lo stesso Francesco I fu")

S("sto-116", "Età moderna", 2, "Chi saccheggiò Roma nel maggio 1527?",
  "I Lanzichenecchi, soldati imperiali", ["I Turchi", "I Francesi", "Gli Spagnoli di Filippo II"],
  "Voce «Storia d'Italia».",
  "sacco di Roma del maggio 1527 per opera dei Lanzichenecchi")

S("sto-117", "Età moderna", 3, "Quale pace del 1559 pose fine alle guerre d'Italia tra Francia e Spagna?",
  "La pace di Cateau-Cambrésis", ["La pace di Lodi", "La pace di Westfalia", "La pace di Utrecht"],
  "Sancì l'egemonia spagnola su Milano, Napoli, Sicilia e Sardegna.",
  "la pace di Cateau-Cambrésis")

S("sto-118", "Età moderna", 3, "In che anno i Savoia trasferirono la capitale da Chambéry a Torino?",
  "Nel 1563", ["Nel 1416", "Nel 1720", "Nel 1861"],
  "Voce «Storia d'Italia».",
  "spostando nello stesso anno la capitale del ducato da Chambery a Torino")

S("sto-119", "Età moderna", 2, "In quale battaglia del 1571 la Lega Santa sconfisse la flotta ottomana?",
  "Lepanto", ["Prevesa", "Capo Passero", "Famagosta"],
  "Voce «Storia d'Italia».",
  "Battaglia di Lepanto con la conseguente sconfitta della flotta ottomana")

S("sto-120", "Età moderna", 4, "Quale comandante veneziano difese Famagosta e fu torturato dagli Ottomani?",
  "Marcantonio Bragadin", ["Sebastiano Venier", "Francesco Morosini", "Andrea Doria"],
  "Voce «Storia d'Italia».",
  "Marcantonio Bragadin che rifiutò la resa")

S("sto-121", "Età moderna", 2, "Chi guidò la rivolta popolare scoppiata a Napoli nel 1647 contro le gabelle spagnole?",
  "Masaniello", ["Gennaro Annese", "Tommaso Campanella", "Pietro Micca"],
  "Voce «Storia d'Italia».",
  "quella del 1647 del pescatore Masaniello")

S("sto-122", "Età moderna", 3, "Quale trattato del 1713 segnò il passaggio dell'egemonia in Italia dalla Spagna all'Austria?",
  "Il trattato di Utrecht", ["Il trattato di Aquisgrana", "Il trattato di Campoformio", "Il trattato di Cateau-Cambrésis"],
  "Voce «Storia d'Italia».",
  "Pace di Utrecht (1713)")

S("sto-123", "Età moderna", 3, "Quale eroe piemontese si sacrificò durante l'assedio di Torino del 1706?",
  "Pietro Micca", ["Balilla", "Ciro Menotti", "Masaniello"],
  "Voce «Storia d'Italia».",
  "il sacrificio di Pietro Micca")

S("sto-124", "Età moderna", 4, "Con il trattato dell'Aia del 1720 i Savoia scambiarono la Sicilia con quale isola, diventando re di essa?",
  "La Sardegna", ["La Corsica", "Malta", "L'Elba"],
  "Voce «Storia d'Italia».",
  "da Re di Sicilia a Re di Sardegna")

S("sto-125", "Età moderna", 4, "Quale ragazzo genovese diede inizio, con un sasso, alla rivolta contro gli Austriaci nel 1746?",
  "Balilla", ["Pietro Micca", "Goffredo Mameli", "Masaniello"],
  "Voce «Storia d'Italia».",
  "un ragazzino, Balilla, che lanciò un sasso")

S("sto-126", "Età moderna", 3, "A quale Stato Genova cedette la Corsica nel 1768?",
  "Alla Francia", ["Al Regno di Sardegna", "All'Inghilterra", "Alla Spagna"],
  "Con il trattato di Versailles.",
  "la Repubblica di Genova cedette la Corsica alla Francia")

S("sto-127", "Età moderna", 2, "Chi scrisse nel 1763-1764 il trattato «Dei delitti e delle pene»?",
  "Cesare Beccaria", ["Pietro Verri", "Gaetano Filangieri", "Ludovico Muratori"],
  "Proponeva l'abolizione della tortura e della pena di morte.",
  "Cesare Beccaria pubblica nel 1763 il trattato Dei delitti e delle pene")

S("sto-128", "Età moderna", 2, "Quale scienziato italiano inventò la pila elettrica?",
  "Alessandro Volta", ["Luigi Galvani", "Lazzaro Spallanzani", "Evangelista Torricelli"],
  "Voce «Storia d'Italia».",
  "Alessandro Volta inventa la pila elettrica")

S("sto-129", "Età moderna", 4, "Chi fu la prima donna autrice di un libro di matematica e titolare di una cattedra universitaria di matematica?",
  "Maria Gaetana Agnesi", ["Laura Bassi", "Elena Cornaro Piscopia", "Maria Montessori"],
  "Voce «Storia d'Italia».",
  "Maria Gaetana Agnesi, fu la prima donna autrice di un libro di matematica")

S("sto-130", "Età napoleonica", 3, "Con quale trattato del 1797 la Repubblica di Venezia fu ceduta all'Austria?",
  "Il trattato di Campoformio", ["Il trattato di Presburgo", "Il trattato di Utrecht", "Il congresso di Vienna"],
  "Voce «Storia d'Italia».",
  "Trattato di Campoformio con il quale la Repubblica di Venezia fu annessa allo Stato austriaco")

S("sto-131", "Età napoleonica", 3, "Quale repubblica, riconosciuta a Campoformio, comprendeva Lombardia ed Emilia-Romagna?",
  "La Repubblica Cisalpina", ["La Repubblica Partenopea", "La Repubblica Romana", "La Repubblica Ligure"],
  "Nel 1802 divenne Repubblica Italiana e nel 1805 Regno d'Italia.",
  "Repubblica Cisalpina, la quale comprendeva Lombardia, Emilia-Romagna")

S("sto-132", "Età napoleonica", 4, "A chi Napoleone affidò il Regno di Napoli nel 1808?",
  "A Gioacchino Murat", ["A Giuseppe Bonaparte", "A Eugenio di Beauharnais", "A Elisa Bonaparte"],
  "Prima lo aveva retto il fratello Giuseppe (1806-1808).",
  "consegnandolo nel 1808 a Gioacchino")

S("sto-133", "Età napoleonica", 4, "Chi era il viceré del Regno d'Italia napoleonico?",
  "Eugenio di Beauharnais, figliastro di Napoleone", ["Gioacchino Murat", "Giuseppe Bonaparte", "Francesco Melzi d'Eril"],
  "Voce «Storia d'Italia».",
  "il figliastro Eugenio di")

S("sto-134", "Età napoleonica", 2, "Dove fu esiliato Napoleone dopo l'abdicazione del 1814?",
  "All'Isola d'Elba", ["A Sant'Elena", "In Corsica", "A Malta"],
  "Dopo i Cento giorni sarebbe stato esiliato a Sant'Elena.",
  "venne mandato in esilio all'Isola d'Elba")

S("sto-135", "Età napoleonica", 4, "Quale istituto napoleonico era al vertice di ogni dipartimento del Regno d'Italia?",
  "La prefettura", ["Il podestà", "Il consiglio comunale", "La questura"],
  "Nel Regno di Napoli l'equivalente era l'intendenza.",
  "nell'istituto della prefettura")

# --- Blocco 5: Risorgimento, Grande guerra, fascismo ---
D("sto-136", "Risorgimento", 3, "Dopo quale evento la storiografia fa iniziare di solito il Risorgimento come movimento?",
  "Il Congresso di Vienna (1815)", ["La Rivoluzione francese", "La pace di Utrecht", "La spedizione dei Mille"],
  "Voce «Risorgimento».",
  "Wikipedia, «Risorgimento» (CC BY-SA 4.0)", RIS, "subito dopo il Congresso di Vienna (1815)")

D("sto-137", "Risorgimento", 3, "Quando fu proclamata ufficialmente Roma capitale d'Italia?",
  "Il 3 febbraio 1871", ["Il 20 settembre 1870", "Il 17 marzo 1861", "Il 2 giugno 1946"],
  "Il Parlamento lo aveva già stabilito il 27 marzo 1861.",
  "Wikipedia, «Risorgimento» (CC BY-SA 4.0)", RIS, "proclamazione ufficiale a capitale d'Italia il 3 febbraio 1871")

D("sto-138", "Risorgimento", 2, "Quali città insorsero nel marzo 1848 con le «Cinque giornate» e la rivolta del 22 marzo?",
  "Milano e Venezia", ["Torino e Genova", "Napoli e Palermo", "Roma e Firenze"],
  "Voce «Risorgimento».",
  "Wikipedia, «Risorgimento» (CC BY-SA 4.0)", RIS, "Cinque giornate di Milano e di Venezia il 22 marzo")

D("sto-139", "Risorgimento", 3, "In quali battaglie fu sconfitto Carlo Alberto nella prima guerra d'indipendenza?",
  "Custoza e Novara", ["Magenta e Solferino", "Calatafimi e Volturno", "Lissa e Custoza (1866)"],
  "Dopo Novara abdicò in favore di Vittorio Emanuele II.",
  "Wikipedia, «Risorgimento» (CC BY-SA 4.0)", RIS, "nella battaglia di Custoza e nella Battaglia di Novara")

D("sto-140", "Risorgimento", 4, "Quale attentato a Napoleone III aprì la fase decisiva del 1859-1860?",
  "L'attentato di Felice Orsini", ["L'attentato di Gaetano Bresci", "L'attentato di Agesilao Milano", "L'attentato di Guglielmo Oberdan"],
  "Voce «Risorgimento».",
  "Wikipedia, «Risorgimento» (CC BY-SA 4.0)", RIS, "iniziò con l'attentato di Felice Orsini contro Napoleone III")

D("sto-141", "Risorgimento", 2, "Quali battaglie vinsero Franco-Piemontesi nella seconda guerra d'indipendenza (1859)?",
  "Magenta e Solferino e San Martino", ["Custoza e Novara", "Caporetto e Vittorio Veneto", "Calatafimi e Volturno"],
  "Voce «Risorgimento».",
  "Wikipedia, «Risorgimento» (CC BY-SA 4.0)", RIS, "(Battaglia di Magenta, Battaglia di Solferino e San Martino)")

D("sto-142", "Risorgimento", 3, "Con quale armistizio del 1859 Napoleone III interruppe la guerra, lasciando al Piemonte solo la Lombardia?",
  "Villafranca", ["Campoformio", "Cormons", "Vignale"],
  "Voce «Risorgimento».",
  "Wikipedia, «Risorgimento» (CC BY-SA 4.0)", RIS, "preliminari di pace di Villafranca")

D("sto-143", "Risorgimento", 2, "Da dove salpò Garibaldi con i Mille e dove sbarcò?",
  "Da Quarto (Liguria), sbarcando a Marsala l'11 maggio 1860", ["Da Genova, sbarcando a Napoli", "Da Livorno, sbarcando a Palermo", "Da La Spezia, sbarcando a Messina"],
  "Voce «Risorgimento».",
  "Wikipedia, «Risorgimento» (CC BY-SA 4.0)", RIS, "salpato da Quarto in Liguria e sbarcato a Marsala l'11 maggio 1860")

D("sto-144", "Risorgimento", 3, "Qual fu la prima battaglia vinta dai garibaldini contro i borbonici, il 15 maggio 1860?",
  "Calatafimi", ["Volturno", "Milazzo", "Aspromonte"],
  "Voce «Risorgimento».",
  "Wikipedia, «Risorgimento» (CC BY-SA 4.0)", RIS, "vinse la prima battaglia contro i borbonici a Calatafimi")

D("sto-145", "Risorgimento", 4, "Con quale battaglia del 1° ottobre 1860 Garibaldi sottrasse definitivamente il Sud ai Borbone?",
  "Battaglia del Volturno", ["Battaglia di Calatafimi", "Battaglia di Gaeta", "Battaglia di Mentana"],
  "Voce «Risorgimento».",
  "Wikipedia, «Risorgimento» (CC BY-SA 4.0)", RIS, "Battaglia del Volturno il 1o ottobre 1860")

D("sto-146", "Risorgimento", 4, "In quale battaglia navale del 1866 fu sconfitta la Marina italiana?",
  "Lissa", ["Lepanto", "Capo Passero", "Capo Matapan"],
  "Voce «Risorgimento».",
  "Wikipedia, «Risorgimento» (CC BY-SA 4.0)", RIS, "dalla sconfitta della Marina a Lissa il 20 luglio")

D("sto-147", "Risorgimento", 4, "Quale vittoria prussiana del 1866 determinò l'esito della terza guerra d'indipendenza?",
  "Sadowa", ["Sedan", "Waterloo", "Lipsia"],
  "Voce «Risorgimento».",
  "Wikipedia, «Risorgimento» (CC BY-SA 4.0)", RIS, "quella di Sadowa del 3 luglio 1866")

D("sto-148", "Prima guerra mondiale", 2, "Tra quali date si combatté la Prima guerra mondiale?",
  "Dal 28 luglio 1914 all'11 novembre 1918", ["Dal 1° settembre 1939 all'8 maggio 1945", "Dal 24 maggio 1915 al 4 novembre 1918 per tutti", "Dal 1912 al 1913"],
  "Per l'Italia la guerra iniziò il 24 maggio 1915.",
  "Wikipedia, «Prima guerra mondiale» (CC BY-SA 4.0)", G1, "tra il 28 luglio 1914 e l'11 novembre 1918")

D("sto-149", "Prima guerra mondiale", 3, "Lungo quale fiume si combatterono le principali offensive italiane del 1915-1917?",
  "L'Isonzo", ["Il Po", "Il Tevere", "L'Adige"],
  "Voce «Prima guerra mondiale».",
  "Wikipedia, «Prima guerra mondiale» (CC BY-SA 4.0)", G1, "attestate lungo il corso del fiume Isonzo")

D("sto-150", "Prima guerra mondiale", 2, "Su quale fiume ripiegò l'esercito italiano dopo la disfatta di Caporetto?",
  "Il Piave", ["L'Isonzo", "Il Tagliamento", "Il Brenta"],
  "Voce «Prima guerra mondiale».",
  "Wikipedia, «Prima guerra mondiale» (CC BY-SA 4.0)", G1, "ordinò all'intero esercito di ripiegare sul fiume Piave")

D("sto-151", "Prima guerra mondiale", 3, "Quale presidente americano mantenne la neutralità degli Stati Uniti fino al 1917?",
  "Thomas Woodrow Wilson", ["Theodore Roosevelt", "Franklin D. Roosevelt", "Herbert Hoover"],
  "L'affondamento del Lusitania e la guerra sottomarina tedesca portarono gli USA in guerra.",
  "Wikipedia, «Prima guerra mondiale» (CC BY-SA 4.0)", G1, "il presidente Thomas Woodrow Wilson si era attenuto alla sua politica di neutralità")

D("sto-152", "Prima guerra mondiale", 3, "Intorno a quale piazzaforte i Tedeschi lanciarono nel 1916 una grande battaglia di logoramento?",
  "Verdun", ["Ypres", "Tannenberg", "Gallipoli"],
  "Voce «Prima guerra mondiale».",
  "Wikipedia, «Prima guerra mondiale» (CC BY-SA 4.0)", G1, "battaglia di logoramento attorno alla piazzaforte di Verdun")

D("sto-153", "Prima guerra mondiale", 4, "Con quale trattato la Russia rivoluzionaria uscì dalla guerra nel 1918?",
  "Trattato di Brest-Litovsk", ["Trattato di Versailles", "Trattato di Rapallo", "Trattato di Saint-Germain"],
  "Voce «Prima guerra mondiale».",
  "Wikipedia, «Prima guerra mondiale» (CC BY-SA 4.0)", G1, "Trattato di Brest-Litovsk")

D("sto-154", "Prima guerra mondiale", 3, "Quale presidente del Consiglio guidava l'Italia quando dichiarò guerra all'Austria-Ungheria nel 1915?",
  "Antonio Salandra", ["Giovanni Giolitti", "Vittorio Emanuele Orlando", "Francesco Crispi"],
  "Voce «Prima guerra mondiale».",
  "Wikipedia, «Prima guerra mondiale» (CC BY-SA 4.0)", G1, "con cui Antonio Salandra sperava")

D("sto-155", "Prima guerra mondiale", 3, "Che tipo di guerra caratterizzò soprattutto il primo conflitto mondiale?",
  "Una logorante guerra di trincea", ["Una guerra lampo di movimento", "Una guerra solo navale", "Una guerra solo aerea"],
  "Voce «Prima guerra mondiale».",
  "Wikipedia, «Prima guerra mondiale» (CC BY-SA 4.0)", G1, "logorante guerra di trincea")

D("sto-156", "Fascismo", 2, "Quale movimento fondò Mussolini nel 1919 con reduci, arditi e futuristi?",
  "I Fasci italiani di combattimento", ["Il Partito Popolare", "Il Partito Nazionale Fascista", "L'Associazione nazionalista"],
  "Il Partito Nazionale Fascista nacque nel 1921.",
  "Wikipedia, «Fascismo» (CC BY-SA 4.0)", FAS, "fondarono i Fasci italiani di combattimento")

D("sto-157", "Fascismo", 3, "Come si chiamò la protesta dei deputati di opposizione che abbandonarono il Parlamento dopo il delitto Matteotti?",
  "Secessione dell'Aventino", ["Marcia su Roma", "Biennio rosso", "Patto di Palazzo Vidoni"],
  "Voce «Fascismo».",
  "Wikipedia, «Fascismo» (CC BY-SA 4.0)", FAS, "la Secessione dell'Aventino")

D("sto-158", "Fascismo", 4, "In che anno il Gran Consiglio del Fascismo fu costituzionalizzato?",
  "Nel 1928", ["Nel 1922", "Nel 1943", "Nel 1919"],
  "Voce «Fascismo».",
  "Wikipedia, «Fascismo» (CC BY-SA 4.0)", FAS, "costituzionalizzazione del Gran Consiglio del Fascismo, nel 1928")

D("sto-159", "Fascismo", 3, "Quale Stato si costituì nel Nord Italia dopo l'8 settembre 1943, riconosciuto solo dall'Asse?",
  "La Repubblica Sociale Italiana", ["Il Regno del Sud", "La Repubblica di Salò democratica", "Il Territorio Libero di Trieste"],
  "Voce «Fascismo».",
  "Wikipedia, «Fascismo» (CC BY-SA 4.0)", FAS, "si costituì la Repubblica Sociale Italiana")

D("sto-160", "Fascismo", 4, "Formalmente, a quale istituzione restò subordinato il regime fascista?",
  "Alla monarchia sabauda e allo Statuto del Regno", ["Al Papa", "Alla Società delle Nazioni", "Al Parlamento eletto a suffragio universale"],
  "Voce «Fascismo».",
  "Wikipedia, «Fascismo» (CC BY-SA 4.0)", FAS, "si mantenne formalmente subordinato alla monarchia sabauda e fedele allo Statuto del Regno")

# --- Blocco 6: Seconda guerra mondiale, Repubblica, Guerra fredda, integrazione europea ---
UE = "Wikipedia_Storia-dell-Unione-europea.txt"
W = lambda voce: f"Wikipedia, «{voce}» (CC BY-SA 4.0)"

D("sto-161", "Seconda guerra mondiale", 3, "Come si chiamò l'invasione tedesca dell'Unione Sovietica nel 1941?",
  "Operazione Barbarossa", ["Operazione Overlord", "Operazione Leone marino", "Operazione Torch"],
  "Hitler ruppe così il patto Molotov-Ribbentrop.",
  W("Seconda guerra mondiale"), G2, "di rompere il patto Molotov-Ribbentrop e di scatenare un attacco generale contro l'Unione Sovietica")

D("sto-162", "Seconda guerra mondiale", 2, "Quale attacco giapponese portò gli Stati Uniti in guerra nel dicembre 1941?",
  "L'attacco di Pearl Harbor", ["Lo sbarco a Okinawa", "La battaglia delle Midway", "L'invasione delle Filippine"],
  "Voce «Seconda guerra mondiale».",
  W("Seconda guerra mondiale"), G2, "Attacco di Pearl Harbor")

D("sto-163", "Seconda guerra mondiale", 2, "Quando iniziò lo sbarco in Normandia (operazione Overlord)?",
  "Il 6 giugno 1944", ["L'8 settembre 1943", "Il 25 aprile 1945", "Il 10 luglio 1943"],
  "Voce «Seconda guerra mondiale».",
  W("Seconda guerra mondiale"), G2, "il 6 giugno 1944 prese il via l'invasione anfibia della Francia")

D("sto-164", "Seconda guerra mondiale", 3, "Quale località egiziana fu teatro delle battaglie decisive tra Asse e britannici nel 1942?",
  "El Alamein", ["Tobruk", "Il Cairo", "Alessandria"],
  "Era l'ultimo ostacolo geografico prima del Cairo.",
  W("Seconda guerra mondiale"), G2, "fino alla località di El Alamein")

D("sto-165", "Seconda guerra mondiale", 3, "Quando fu fondata l'ONU, al termine della Conferenza di San Francisco?",
  "Il 26 giugno 1945", ["Il 1° settembre 1939", "Il 10 dicembre 1948", "Il 4 aprile 1949"],
  "Voce «Seconda guerra mondiale».",
  W("Seconda guerra mondiale"), G2, "al termine della Conferenza di San Francisco il 26 giugno")

D("sto-166", "Seconda guerra mondiale", 2, "Come si chiamavano i due schieramenti della Seconda guerra mondiale?",
  "Potenze dell'Asse e Alleati", ["Triplice alleanza e Triplice intesa", "NATO e Patto di Varsavia", "Imperi centrali e Intesa"],
  "Voce «Seconda guerra mondiale».",
  W("Seconda guerra mondiale"), G2, "le cosiddette potenze dell'Asse e gli Alleati")

D("sto-167", "Seconda guerra mondiale", 3, "Quale paese aderì al Patto tripartito nel 1941 ma, dopo un colpo di Stato a Belgrado, fu invaso dalla Germania?",
  "La Jugoslavia", ["La Grecia", "La Bulgaria", "L'Ungheria"],
  "Voce «Seconda guerra mondiale».",
  W("Seconda guerra mondiale"), G2, "siglò l'adesione del paese al Patto tripartito")

D("sto-168", "Repubblica", 3, "Dove andò in esilio Umberto II dopo il referendum del 1946?",
  "In Portogallo", ["In Svizzera", "In Spagna", "In Francia"],
  "Il governo De Gasperi dichiarò decaduta la monarchia nella notte tra il 12 e il 13 giugno.",
  W("Storia dell'Italia repubblicana"), REP, "Umberto II partì per l'esilio in Portogallo")

D("sto-169", "Repubblica", 3, "Chi assunse temporaneamente le funzioni di capo dello Stato nel giugno 1946?",
  "Alcide De Gasperi", ["Enrico De Nicola", "Luigi Einaudi", "Palmiro Togliatti"],
  "Voce «Storia dell'Italia repubblicana».",
  W("Storia dell'Italia repubblicana"), REP, "Lo stesso De Gasperi assunse temporaneamente anche la carica di capo dello Stato")

D("sto-170", "Repubblica", 2, "Quale programma statunitense finanziò la ricostruzione europea nel dopoguerra?",
  "Il Piano Marshall", ["Il Piano Schuman", "Il New Deal", "La Dottrina Monroe"],
  "Voce «Storia dell'Italia repubblicana».",
  W("Storia dell'Italia repubblicana"), REP, "aiuti economici previsti dal Piano Marshall")

D("sto-171", "Repubblica", 2, "In che anno l'Italia aderì alla NATO?",
  "Nel 1949", ["Nel 1946", "Nel 1955", "Nel 1957"],
  "Voce «Storia dell'Italia repubblicana».",
  W("Storia dell'Italia repubblicana"), REP, "nel 1949 l'Italia aderì alla NATO")

D("sto-172", "Repubblica", 3, "In che anno l'Italia fu ammessa alle Nazioni Unite?",
  "Nel 1955", ["Nel 1945", "Nel 1949", "Nel 1960"],
  "Voce «Storia dell'Italia repubblicana».",
  W("Storia dell'Italia repubblicana"), REP, "Nel 1955 venne ammessa invece alle Nazioni Unite")

D("sto-173", "Repubblica", 3, "Quale ente fu istituito per ridurre il divario tra Nord e Sud nel dopoguerra?",
  "La Cassa per il Mezzogiorno", ["L'IRI", "L'ENI", "La Cassa depositi e prestiti"],
  "Voce «Storia dell'Italia repubblicana».",
  W("Storia dell'Italia repubblicana"), REP, "l'istituzione della Cassa per il Mezzogiorno")

D("sto-174", "Repubblica", 3, "In che anno fu introdotta in Italia la legge sul divorzio?",
  "Nel 1970", ["Nel 1946", "Nel 1978", "Nel 1981"],
  "Approvata da una maggioranza trasversale, esclusi DC e MSI.",
  W("Storia dell'Italia repubblicana"), REP, "introdotta anche la legge sul divorzio")

D("sto-175", "Repubblica", 2, "Come fu chiamato lo scandalo delle tangenti scoperto dall'inchiesta «Mani pulite»?",
  "Tangentopoli", ["Calciopoli", "Scandalo Lockheed", "P2"],
  "Voce «Storia dell'Italia repubblicana».",
  W("Storia dell'Italia repubblicana"), REP, "Tangentopoli")

D("sto-176", "Repubblica", 3, "Quale periodo di forte crescita del PIL italiano è noto come «miracolo economico»?",
  "Il boom tra la fine degli anni Cinquanta e i primi anni Sessanta", ["Gli anni Venti", "Gli anni Novanta", "Il periodo 2001-2008"],
  "Voce «Storia dell'Italia repubblicana».",
  W("Storia dell'Italia repubblicana"), REP, "Durante il cosiddetto \"miracolo economico\" il prodotto interno lordo")

D("sto-177", "Guerra fredda", 2, "Perché la Guerra fredda è detta «fredda»?",
  "Perché non vi furono combattimenti diretti su larga scala tra le superpotenze", ["Perché si combatté in Siberia", "Perché durò solo d'inverno", "Perché fu combattuta solo in mare"],
  "Voce «Guerra fredda».",
  W("Guerra fredda"), GF, "Viene utilizzato l'aggettivo \"fredda\" poiché non vi furono combattimenti diretti su larga scala")

D("sto-178", "Guerra fredda", 3, "Quale crisi del 1962 portò il mondo vicino a un conflitto nucleare?",
  "La crisi dei missili di Cuba", ["La crisi di Suez", "Il blocco di Berlino", "La guerra di Corea"],
  "Voce «Guerra fredda».",
  W("Guerra fredda"), GF, "soprattutto la crisi dei missili di Cuba")

D("sto-179", "Guerra fredda", 3, "Quale diplomatico americano inviò nel 1946 il «lungo telegramma» che ispirò la politica di contenimento?",
  "George Frost Kennan", ["Henry Kissinger", "George Marshall", "Dean Acheson"],
  "Voce «Guerra fredda».",
  W("Guerra fredda"), GF, "dal diplomatico George Frost Kennan")

D("sto-180", "Guerra fredda", 2, "Quali eventi segnarono la fine della Guerra fredda?",
  "La caduta del Muro di Berlino (1989) e la dissoluzione dell'URSS (1991)", ["La crisi di Cuba e la guerra del Vietnam", "La nascita della NATO e del Patto di Varsavia", "La fine della guerra di Corea"],
  "Voce «Guerra fredda».",
  W("Guerra fredda"), GF, "terminato con la caduta del Muro di Berlino (1989)")

D("sto-181", "Guerra fredda", 3, "Quale processo di riduzione delle tensioni tra i blocchi si avviò dagli anni Settanta?",
  "La distensione", ["Il containment", "La perestrojka", "Il riarmo"],
  "Voce «Guerra fredda».",
  W("Guerra fredda"), GF, "intraprendere un processo di \"disten")

D("sto-182", "Integrazione europea", 2, "Chi sono gli autori del Manifesto di Ventotene?",
  "Altiero Spinelli, Ernesto Rossi ed Eugenio Colorni", ["Alcide De Gasperi e Robert Schuman", "Jean Monnet e Konrad Adenauer", "Carlo Rosselli e Piero Gobetti"],
  "Voce «Storia dell'Unione europea».",
  W("Storia dell'Unione europea"), UE, "di cui sono autori Altiero Spinelli, Ernesto Rossi, Eugenio Colorni")

D("sto-183", "Integrazione europea", 3, "Quale ministro francese propose il piano da cui nacque la CECA?",
  "Robert Schuman", ["Charles de Gaulle", "Jean Monnet", "François Mitterrand"],
  "La CECA fu ideata da Jean Monnet; il piano prende il nome da Schuman.",
  W("Storia dell'Unione europea"), UE, "piano Schuman, dal nome del ministro degli esteri francese Robert Schuman")

D("sto-184", "Integrazione europea", 3, "Perché la Costituzione europea non entrò mai in vigore?",
  "Per il voto contrario nei referendum, a partire da quello francese", ["Perché non fu mai firmata", "Perché la bocciò la Corte di giustizia", "Perché l'Italia non la ratificò"],
  "Fu poi sostituita dal Trattato di Lisbona.",
  W("Storia dell'Unione europea"), UE, "il 54,7% dell'elettorato francese ha scelto di non s")

D("sto-185", "Integrazione europea", 4, "Quale atto degli anni Ottanta rilanciò il processo di integrazione europea verso il mercato unico?",
  "L'Atto unico europeo", ["Il Trattato di Nizza", "Il Trattato di Amsterdam", "Il Piano Werner"],
  "Voce «Storia dell'Unione europea».",
  W("Storia dell'Unione europea"), UE, "L'atto unico europeo")

D("sto-186", "Integrazione europea", 4, "Quale premier britannico, eletto nel 1979, chiese di contribuire meno al bilancio comunitario?",
  "Margaret Thatcher", ["Tony Blair", "Harold Wilson", "John Major"],
  "Voce «Storia dell'Unione europea».",
  W("Storia dell'Unione europea"), UE, "il governo conservatore di Margaret Thatcher, eletto nel 1979")

# --- Blocco 7: Italia liberale e giolittiana (voce «Storia d'Italia») ---
S("sto-187", "Italia liberale", 3, "Quale questione tenne banco nei primi anni dopo l'Unità, insieme al brigantaggio?",
  "La questione meridionale", ["La questione d'Oriente", "La questione sociale inglese", "La questione balcanica"],
  "Il brigantaggio fu intenso soprattutto tra il 1861 e il 1865.",
  "fu la questione meridionale e il brigantaggio delle regioni meridionali")

S("sto-188", "Italia liberale", 3, "Da quali ceti era composta principalmente la Destra storica?",
  "Dall'alta borghesia e dai proprietari terrieri", ["Dagli operai industriali", "Dal clero", "Dai braccianti agricoli"],
  "Voce «Storia d'Italia».",
  "composta principalmente dall'alta borghesia e dai proprietari terrieri")

S("sto-189", "Italia liberale", 3, "Chi guidò la Sinistra storica, al governo dal 1876?",
  "Agostino Depretis", ["Marco Minghetti", "Francesco Crispi", "Giovanni Giolitti"],
  "Voce «Storia d'Italia».",
  "guidata da Agostino Depretis")

S("sto-190", "Italia liberale", 3, "Chi successe a Vittorio Emanuele II sul trono d'Italia?",
  "Umberto I", ["Vittorio Emanuele III", "Carlo Alberto", "Umberto II"],
  "Voce «Storia d'Italia».",
  "sul trono gli successe Umberto I")

S("sto-191", "Italia liberale", 3, "Quale obiettivo abbandonò la Sinistra storica rispetto alla Destra?",
  "Il pareggio di bilancio", ["L'unità nazionale", "La monarchia", "La conquista di Roma"],
  "Avviò invece politiche di democratizzazione e ammodernamento.",
  "La Sinistra abbandonò l'obiettivo del pareggio")

S("sto-192", "Italia liberale", 2, "In quale battaglia del 1896 l'Italia subì una pesante sconfitta in Etiopia?",
  "Adua", ["Dogali", "Caporetto", "El Alamein"],
  "Fu uno dei pochi successi della resistenza africana al colonialismo europeo.",
  "pesante sconfitta nella battaglia di Adua")

S("sto-193", "Italia liberale", 3, "Quale riforma elettorale è tra i provvedimenti più importanti di Giolitti?",
  "Il suffragio universale maschile", ["Il voto alle donne", "Il sistema proporzionale puro", "L'abolizione del Senato"],
  "Giolitti promosse anche la legislazione sociale e la nazionalizzazione delle ferrovie.",
  "il suffragio universale maschile, la nazionalizzazione delle ferrovie")

S("sto-194", "Italia liberale", 3, "Quali territori occupò l'Italia dopo la guerra italo-turca (1911-1912)?",
  "La Libia e il Dodecaneso", ["L'Eritrea e la Somalia", "L'Albania e la Dalmazia", "Rodi e Creta soltanto"],
  "Voce «Storia d'Italia».",
  "dopo la guerra italo-turca, furono occupate Libia e Dodecaneso")

S("sto-195", "Prima guerra mondiale", 4, "Cosa prometteva all'Italia il Patto di Londra del 1915, in caso di vittoria?",
  "Trentino, Alto Adige, Venezia Giulia, Istria e Dalmazia settentrionale (Fiume esclusa)", ["Fiume e tutta la Dalmazia", "La Corsica e Nizza", "La Libia e la Tunisia"],
  "Voce «Storia d'Italia».",
  "il Trentino, l'Alto Adige, la Venezia Giulia, l'Istria, con l'esclusione di Fiume")

S("sto-196", "Fascismo", 3, "Quale espressione della propaganda nazionalista indicava l'insoddisfazione per i risultati della pace del 1919?",
  "Vittoria mutilata", ["Pace senza vittoria", "Vittoria di Pirro", "Pace cartaginese"],
  "Voce «Storia d'Italia».",
  "propaganda nazionalista della \"vittoria mutilata\"")

S("sto-197", "Fascismo", 3, "Come si chiamò l'intesa politico-militare tra Italia e Germania del 1936?",
  "Asse Roma-Berlino", ["Patto d'acciaio", "Patto anticomintern", "Triplice alleanza"],
  "Voce «Storia d'Italia».",
  "la formazione dell'asse Roma-Berlino del 1936")

S("sto-198", "Fascismo", 4, "Come è ricordato il periodo di agitazioni sindacali e operaie del 1919-1920 in Italia?",
  "Biennio rosso", ["Autunno caldo", "Anni di piombo", "Settimana rossa"],
  "Voce «Storia d'Italia».",
  "che caratterizzarono il biennio rosso italiano")

S("sto-199", "Repubblica", 2, "Quando entrò in vigore l'attuale Costituzione italiana?",
  "Il 1° gennaio 1948", ["Il 2 giugno 1946", "Il 25 aprile 1945", "Il 22 dicembre 1947"],
  "Fu approvata il 22 dicembre 1947 e promulgata il 27 dicembre.",
  "quando entrò in vigore l'attuale Costituzione")

S("sto-200", "Repubblica", 3, "Chi successe a Enrico De Nicola come Presidente della Repubblica?",
  "Luigi Einaudi", ["Giovanni Gronchi", "Antonio Segni", "Alcide De Gasperi"],
  "Voce «Storia d'Italia».",
  "sostituito in seguito dall'economista Luigi Einaudi")

S("sto-201", "Repubblica", 3, "Quali due esponenti DC erano definiti i «cavalli di razza» del partito?",
  "Aldo Moro e Amintore Fanfani", ["Alcide De Gasperi e Giulio Andreotti", "Mariano Rumor e Emilio Colombo", "Ciriaco De Mita e Arnaldo Forlani"],
  "Voce «Storia d'Italia».",
  "Aldo Moro e Amintore Fanfani, definiti")

S("sto-202", "Repubblica", 3, "Di quale gruppo di grandi economie l'Italia fu tra i fondatori nel 1975?",
  "Il G6 (poi G7)", ["L'OPEC", "Il Patto di Varsavia", "Il Commonwealth"],
  "Voce «Storia d'Italia».",
  "tra le nazioni fondanti del G6 (poi G7, G8 e nuovamente G7) nel 1975")

# --- Ampliamento a 300: Risorgimento, guerre mondiali, fascismo, Repubblica, Guerra fredda, Europa ---
def RI(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Risorgimento"), RIS, frase)
def P1(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Prima guerra mondiale"), G1, frase)
def FA(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Fascismo"), FAS, frase)
def P2(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Seconda guerra mondiale"), G2, frase)
def RE(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Storia dell'Italia repubblicana"), REP, frase)
def GFR(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Guerra fredda"), GF, frase)
def EU(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Storia dell'Unione europea"), UE, frase)

RI("sto-203", "Risorgimento", 4, "Quale evento del 15 giugno 1820 è indicato da alcuni storici come inizio del Risorgimento?",
  "I moti siciliani", ["Le Cinque giornate di Milano", "La spedizione dei Mille", "Il Congresso di Vienna"],
  "Altri fanno partire il Risorgimento dalla prima guerra d'indipendenza (1848-1849).", "ai moti siciliani del 15 giugno 1820")
RI("sto-204", "Risorgimento", 4, "Quale proclama del 1815 è considerato da alcuni storici l'inizio del Risorgimento?",
  "Il proclama di Rimini", ["Il proclama di Moncalieri", "Il proclama di Teano", "Il proclama di Torino"],
  "Per questi storici il Risorgimento va dal proclama di Rimini (1815) alla breccia di Porta Pia (1870).", "fra il proclama di Rimini (1815) e la breccia di Porta Pia")
RI("sto-205", "Risorgimento", 3, "Da quale organizzazione derivavano società segrete come la Carboneria?",
  "Dalla massoneria", ["Dall'ordine dei Gesuiti", "Dai partiti politici inglesi", "Dalle corporazioni medievali"],
  "Furono i laboratori in cui la classe dirigente patriottica pianificò i moti.", "Questi circoli iniziatici, derivati dalla massoneria")
RI("sto-206", "Risorgimento", 3, "Quando Leopoldo II concesse lo Statuto in Toscana?",
  "Il 17 febbraio 1848", ["Il 4 marzo 1848", "Il 14 marzo 1848", "Il 17 marzo 1861"],
  "Seguirono lo Statuto albertino (4 marzo) e lo statuto dello Stato Pontificio (14 marzo).", "Leopoldo II di Toscana concesse lo Statuto il 17 febbraio")
RI("sto-207", "Risorgimento", 3, "Quanto durò la Repubblica Romana del 1849?",
  "Da febbraio a luglio 1849", ["Due anni", "Dieci giorni", "Dal 1849 al 1870"],
  "Durante la Repubblica Pio IX fuggì da Roma; Napoleone III la represse.", "Dal febbraio al luglio 1849 si svolse la vicenda della Repubblica Romana")
RI("sto-208", "Risorgimento", 3, "Chi guidò la spedizione di Sapri del 1857, finita con la morte sua e dei compagni?",
  "Carlo Pisacane", ["Giuseppe Garibaldi", "Felice Orsini", "Ciro Menotti"],
  "Era ispirata al credo mazziniano di «dare l'esempio».", "conclusasi con la morte di Carlo Pisacane e dei suoi 23 compagni")
RI("sto-209", "Risorgimento", 3, "Da chi furono sconfitti i garibaldini nella battaglia di Mentana del 1867?",
  "Dalle truppe francesi", ["Dall'esercito austriaco", "Dall'esercito italiano", "Dai borbonici"],
  "Nel 1862 Garibaldi era stato fermato in Aspromonte dall'esercito italiano.", "sconfitto dalle truppe francesi nella battaglia di Mentana")
RI("sto-210", "Risorgimento", 4, "Dove fu fermato Garibaldi dall'esercito italiano nel 1862, nel tentativo di marciare su Roma?",
  "In Aspromonte", ["A Mentana", "A Teano", "A Bezzecca"],
  "L'esercito fu inviato dal governo Rattazzi.", "'Aspromonte dall'esercito italiano inviato da Urbano Rattazzi")
RI("sto-211", "Risorgimento", 3, "In che anno il Veneto fu incorporato nel Regno d'Italia?",
  "Nel 1866", ["Nel 1859", "Nel 1861", "Nel 1870"],
  "Dopo la terza guerra d'indipendenza; Roma fu presa nel 1870.", "Il Risorgimento continuò con l'incorporazione del Veneto nel 1866")
RI("sto-212", "Risorgimento", 3, "Cosa fece Vittorio Emanuele II dello Statuto albertino, diversamente dagli altri sovrani italiani dopo il 1849?",
  "Non lo ritirò", ["Lo abolì", "Lo sostituì con una costituzione repubblicana", "Lo sospese fino al 1861"],
  "Gli altri sovrani revocarono le costituzioni concesse nel 1848.", "non ritirò lo Statuto Albertino concesso dal padre")
RI("sto-213", "Risorgimento", 3, "Quale papa, eletto il 16 giugno 1846, fu inizialmente ritenuto un «liberale»?",
  "Pio IX", ["Gregorio XVI", "Leone XIII", "Pio VII"],
  "Su di lui puntò il movimento neoguelfo.", "1846 di papa Pio IX, ritenuto un \"liberale\"")
RI("sto-214", "Risorgimento", 4, "Quali patrioti erano unitaristi repubblicani e federalisti contrari alla monarchia?",
  "Nicolò Tommaseo e Carlo Cattaneo", ["Cavour e D'Azeglio", "Gioberti e Rosmini", "Vittorio Emanuele II e La Marmora"],
  "I cattolici neoguelfi come Gioberti e Rosmini puntavano invece su una confederazione guidata dal papa.", "federalisti radicali contrari alla monarchia come Nicolò Tommaseo e Carlo Cattaneo")
RI("sto-215", "Risorgimento", 3, "Quali pensatori cattolici auspicavano una soluzione neoguelfa?",
  "Vincenzo Gioberti e Antonio Rosmini", ["Mazzini e Garibaldi", "Cattaneo e Ferrari", "Cavour e Ricasoli"],
  "Il neoguelfismo immaginava un'Italia federata sotto la guida del papa.", "vi furono cattolici come Vincenzo Gioberti, Antonio Rosmini")
RI("sto-216", "Risorgimento", 4, "Che cosa indica la storiografia con «quarta guerra d'indipendenza»?",
  "La Prima guerra mondiale, che portò all'annessione delle terre irredente", ["La guerra di Crimea", "La guerra del 1866", "La guerra di Libia"],
  "Così il compimento dell'unità si estende fino al primo Novecento.", "creando quindi il concetto di quarta guerra di indipendenza")
RI("sto-217", "Risorgimento", 2, "Da quanti volontari era formata, all'incirca, la spedizione dei Mille?",
  "Poco più di un migliaio", ["Circa 10.000", "Circa 300", "Circa 50.000"],
  "Garibaldi partì da Quarto nel maggio 1860.", "Essa era formata da poco più di un migliaio di volontari")
RI("sto-218", "Risorgimento", 4, "In quale località fu arrestato Garibaldi dopo Mentana, prima di essere riportato a Caprera?",
  "Figline Valdarno", ["Aspromonte", "Teano", "Varignano"],
  "Lo fece arrestare il governo Menabrea.", "fece arrestare Garibaldi a Figline Valdarno")

P1("sto-219", "Prima guerra mondiale", 2, "Chi uccise l'arciduca Francesco Ferdinando a Sarajevo nel 1914?",
  "Gavrilo Princip, studente bosniaco della Giovane Bosnia", ["Un ufficiale austriaco", "Un anarchico italiano", "Un agente russo"],
  "L'attentato del 28 giugno 1914 innescò il conflitto.", "Gavrilo Princip, studente bosniaco facente parte della")
P1("sto-220", "Prima guerra mondiale", 3, "Quando l'Italia ruppe la Triplice alleanza, prima di entrare in guerra?",
  "Il 3 maggio 1915", ["Il 24 maggio 1915", "Il 26 aprile 1915", "Il 4 novembre 1918"],
  "Il 24 maggio dichiarò guerra all'Austria-Ungheria, non alla Germania.", "Il 3 maggio successivo fu rotta la Triplice alleanza")
P1("sto-221", "Prima guerra mondiale", 2, "Chi era il capo di stato maggiore dell'esercito italiano all'entrata in guerra nel 1915?",
  "Luigi Cadorna", ["Armando Diaz", "Pietro Badoglio", "Vittorio Emanuele III"],
  "Dopo Caporetto fu sostituito da Armando Diaz.", "capo di stato maggiore Luigi Cadorna")
P1("sto-222", "Prima guerra mondiale", 3, "Quale battaglia del settembre 1914 fermò l'avanzata tedesca in Francia, spegnendo le speranze di una guerra breve?",
  "La prima battaglia della Marna", ["Verdun", "La Somme", "Ypres"],
  "Da allora il conflitto degenerò in una logorante guerra di trincea.", "nel corso della prima battaglia della Marna nel settembre 1914")
P1("sto-223", "Prima guerra mondiale", 3, "Quale transatlantico affondato dai tedeschi contribuì a orientare l'opinione pubblica americana contro la Germania?",
  "Il Lusitania", ["Il Titanic", "La Bismarck", "Il Britannic"],
  "Wilson restò comunque neutrale fino al 1917.", "a partire dall'affondamento del RMS Lusitania")
P1("sto-224", "Prima guerra mondiale", 4, "Come si chiama il telegramma con cui la Germania cercò di spingere il Messico ad attaccare gli Stati Uniti?",
  "Il telegramma Zimmermann", ["Il telegramma di Ems", "Il lungo telegramma", "Il telegramma di Kruger"],
  "Contribuì alla decisione di Wilson di entrare in guerra.", "il caso del \"telegramma Zimmermann\"")
P1("sto-225", "Prima guerra mondiale", 3, "Quando gli Stati Uniti dichiararono guerra alla Germania?",
  "Il 6 aprile 1917", ["Il 7 dicembre 1917", "Il 4 agosto 1914", "L'11 novembre 1918"],
  "Wilson aveva presentato la proposta al Congresso il 4 aprile.", "il 6 aprile gli Stati Uniti dichiararono guerra alla Germania")
P1("sto-226", "Prima guerra mondiale", 4, "Con quale trattato del 1919 fu regolata la pace con l'Austria?",
  "Il trattato di Saint-Germain-en-Laye", ["Il trattato del Trianon", "Il trattato di Neuilly", "Il trattato di Sèvres"],
  "Il Trianon riguardò l'Ungheria, Neuilly la Bulgaria, Sèvres l'Impero ottomano.", "il 10 settembre dal trattato di Saint-Germain-en-Laye con l'Austria")
P1("sto-227", "Prima guerra mondiale", 4, "Con quale trattato del 1920 fu regolata la pace con l'Ungheria?",
  "Il trattato del Trianon", ["Il trattato di Saint-Germain", "Il trattato di Versailles", "Il trattato di Rapallo"],
  "Fu firmato il 4 giugno 1920.", "il 4 giugno 1920 dal trattato del Trianon con l'Ungheria")
P1("sto-228", "Prima guerra mondiale", 2, "In quale città aveva sede la Società delle Nazioni?",
  "Ginevra", ["New York", "Parigi", "Londra"],
  "Fu istituita dopo la Prima guerra mondiale.", "La sede della Società delle Nazioni a")
P1("sto-229", "Prima guerra mondiale", 3, "Come è conosciuta in Italia l'offensiva austro-ungarica del maggio 1916 sugli Altipiani?",
  "Strafexpedition («spedizione punitiva»)", ["Disfatta di Caporetto", "Battaglia del solstizio", "Offensiva Brusilov"],
  "Iniziò il 15 maggio 1916 tra la valle dell'Adige e la Valsugana.", "in Italia conosciuta come Strafexpedition, \"spedizione punitiva\"")
P1("sto-230", "Prima guerra mondiale", 4, "Quale politico britannico sostenne con vigore l'attacco ai Dardanelli (campagna di Gallipoli)?",
  "Winston Churchill, primo lord dell'Ammiragliato", ["David Lloyd George", "Herbert Asquith", "Lord Kitchener soltanto"],
  "L'operazione fallì con pesanti perdite.", "con il vigoroso appoggio del primo lord dell'Ammiragliato Winston Churchill")
P1("sto-231", "Prima guerra mondiale", 3, "In quale battaglia del 1915 i tedeschi usarono per la prima volta su vasta scala gas venefici (cloro)?",
  "Nella seconda battaglia di Ypres", ["Nella battaglia della Marna", "A Verdun", "A Caporetto"],
  "Iniziò così la «guerra dei gas».", "prese avvio la seconda battaglia di Ypres: impiegando per la prima volta e su vasta scala gas venefici")
P1("sto-232", "Prima guerra mondiale", 4, "Quale generale tedesco fu richiamato dalla pensione e vinse a Tannenberg contro i russi?",
  "Paul von Hindenburg", ["Erich von Falkenhayn", "Helmuth von Moltke", "Maximilian von Prittwitz"],
  "Sostituì Prittwitz al comando sul fronte orientale.", "dal generale in pensione Paul von Hindenburg")
P1("sto-233", "Prima guerra mondiale", 3, "Quale generale francese ebbe il comando unificato degli Alleati sul fronte occidentale nel 1918?",
  "Ferdinand Foch", ["Philippe Pétain", "Joseph Joffre", "Robert Nivelle"],
  "Predispose la serie di attacchi dell'offensiva dei cento giorni.", "nella persona del generale francese Ferdinand Foch")
P1("sto-234", "Prima guerra mondiale", 4, "Chi guidò la Turchia verso la repubblica dopo la Prima guerra mondiale?",
  "Mustafa Kemal", ["Ismail Enver", "Mehmed VI", "Talat Pascià"],
  "Nel 1923 il sultanato fu abolito.", "sotto la guida di Mustafa Kemal le forze turche")
P1("sto-235", "Prima guerra mondiale", 2, "Come era definita inizialmente la Prima guerra mondiale dai contemporanei?",
  "«Guerra europea»", ["«Guerra lampo»", "«Guerra fredda»", "«Guerra dei trent'anni»"],
  "Prese poi il nome di guerra mondiale o Grande guerra.", "Inizialmente definita \"guerra europea\" dai contemporanei")

FA("sto-236", "Fascismo", 3, "Quale legge elettorale con un grande premio di maggioranza favorì il «listone» fascista nelle elezioni del 1924?",
  "La legge Acerbo", ["La legge Rocco", "La legge Casati", "La legge Coppino"],
  "Le elezioni furono segnate da brogli e violenze, denunciati da Matteotti.", "Grazie poi alla legge Acerbo")
FA("sto-237", "Fascismo", 3, "Quanti deputati fascisti furono eletti nelle elezioni del 1921?",
  "35", ["Nessuno", "120", "300"],
  "Nel 1919 i Fasci non avevano ottenuto alcun seggio.", "Nelle successive elezioni del 1921 vennero invece eletti 35 deputati")
FA("sto-238", "Fascismo", 4, "Con chi Mussolini elaborò nel 1932 una sintesi dottrinaria del fascismo?",
  "Giovanni Gentile", ["Benedetto Croce", "Gabriele D'Annunzio", "Alfredo Rocco"],
  "Secondo Mussolini il fascismo non nacque da una dottrina preesistente ma dall'azione.", "L'ideologia fascista, di cui Gentile e Mussolini elaborarono una sintesi dottrinaria nel 1932")
FA("sto-239", "Fascismo", 3, "Come si chiamava il primo programma del movimento fascista (1919)?",
  "Programma di San Sepolcro", ["Manifesto di Verona", "Carta del lavoro", "Programma di Erfurt"],
  "Il Manifesto di Verona è invece del periodo della RSI.", "Programma di San Sepolcro")
FA("sto-240", "Fascismo", 3, "In quale anno, secondo la voce, il fascismo si costituì in dittatura?",
  "Nel 1925", ["Nel 1922", "Nel 1929", "Nel 1936"],
  "Raggiunse il potere nel 1922 con la marcia su Roma.", "e si costituì in dittatura nel 1925")
FA("sto-241", "Fascismo", 3, "Come si presentava il fascismo rispetto a capitalismo liberale e comunismo marxista?",
  "Come una «terza via» alternativa a entrambi", ["Come una variante del liberalismo", "Come un movimento comunista", "Come un partito monarchico liberale"],
  "Si fondava su una visione interclassista e corporativa.", "Il fascismo descrive se stesso come una terza via alternativa a capitalismo liberale e comunismo marxista")
FA("sto-242", "Fascismo", 3, "Quale politica economica di autosufficienza esaltò il fascismo?",
  "L'autarchia", ["Il libero scambio", "Il keynesismo", "La pianificazione sovietica"],
  "Si accompagnò a un nazionalismo anche linguistico.", "l'esaltazione dell'autarchia in economia")
FA("sto-243", "Fascismo", 3, "Cosa subirono le minoranze linguistiche durante il fascismo?",
  "Una politica di italianizzazione forzata", ["Il riconoscimento dell'autonomia", "Il bilinguismo obbligatorio", "La tutela costituzionale"],
  "Rientrava nel nazionalismo anche linguistico del regime.", "si perseguì una politica di italianizzazione forzata")
FA("sto-244", "Fascismo", 2, "In quale periodo il governo Mussolini varò la normativa antiebraica (leggi razziali)?",
  "Nell'autunno 1938", ["Nel 1922", "Nel 1929", "Nel 1943"],
  "In parte a imitazione di quanto avveniva in Germania.", "Nell'autunno 1938")
FA("sto-245", "Fascismo", 4, "Quali gerarchi promossero l'ordine del giorno del 25 luglio 1943 al Gran Consiglio?",
  "Grandi, Bottai e Ciano", ["Farinacci, Starace e Balbo", "Badoglio, Ciano e Graziani", "Gentile, Rocco e Volpe"],
  "Chiedeva al Re di riprendere il potere e portò all'arresto di Mussolini.", "per iniziativa di alcuni gerarchi (Grandi, Bottai e Ciano)")
FA("sto-246", "Fascismo", 2, "Come si chiama il ricorso alla violenza come metodo di lotta politica tipico del primo fascismo?",
  "Squadrismo", ["Arditismo", "Brigantaggio", "Terrorismo rosso"],
  "Caratterizzò il fascismo fin dall'inizio, insieme all'ostilità alla democrazia.", "per il ricorso alla violenza come metodo di lotta politica (squadrismo)")
FA("sto-247", "Fascismo", 4, "Secondo le stime di Gaetano Salvemini, quante vittime causarono le violenze del biennio 1921-22?",
  "Circa tremila", ["Circa trenta", "Circa trecentomila", "Nessuna"],
  "Le violenze colpivano soprattutto sindacati e partiti socialisti.", "circa tremila nel solo biennio 1921-22")
FA("sto-248", "Fascismo", 3, "Quali governi formarono la coalizione del primo governo Mussolini?",
  "Fascisti con nazionalisti, liberali e popolari", ["Solo fascisti", "Fascisti e socialisti", "Fascisti e comunisti"],
  "Dopo il delitto Matteotti il regime assunse connotazioni dittatoriali.", "un governo di coalizione composto da nazionalisti, liberali e popolari")

P2("sto-249", "Seconda guerra mondiale", 3, "Quando fu firmato il patto Molotov-Ribbentrop tra Germania e URSS?",
  "Il 24 agosto 1939", ["Il 1° settembre 1939", "Il 22 giugno 1941", "Il 23 giugno 1940"],
  "Un protocollo segreto prevedeva la spartizione della Polonia.", "il 24 agosto 1939 il ministro degli esteri sovietico")
P2("sto-250", "Seconda guerra mondiale", 4, "Quale durata prevedeva il patto di non aggressione Molotov-Ribbentrop?",
  "Dieci anni", ["Un anno", "Cinque anni", "Venticinque anni"],
  "Fu violato dalla Germania con l'operazione Barbarossa nel 1941.", "un patto di non aggressione tra le due nazioni della durata di dieci anni")
P2("sto-251", "Seconda guerra mondiale", 3, "Come si chiamò l'invasione tedesca di Danimarca e Norvegia del 9 aprile 1940?",
  "Operazione Weserübung", ["Operazione Barbarossa", "Operazione Leone marino", "Fall Gelb"],
  "Interruppe la «strana guerra».", "(operazione Weserübung)")
P2("sto-252", "Seconda guerra mondiale", 3, "In quale battaglia navale del marzo 1941 la flotta italiana perse tre incrociatori pesanti?",
  "Capo Matapan", ["Lissa", "Taranto", "Midway"],
  "La sortita avvenne nelle acque a sud di Creta.", "nel corso della battaglia di Capo Matapan gli italiani persero tre incrociatori pesanti")
P2("sto-253", "Seconda guerra mondiale", 4, "Quale depressione naturale rendeva El Alamein l'ultimo ostacolo geografico prima del Cairo?",
  "La depressione di Qattara", ["La depressione del Mar Morto", "Il deserto del Sinai", "Il delta del Nilo"],
  "El Alamein era stretta tra il mare a nord e la depressione a sud.", "intransitabile depressione di Qattara")
P2("sto-254", "Seconda guerra mondiale", 3, "Dove sbarcarono gli anglo-statunitensi il 22 gennaio 1944 per aggirare la linea Gustav?",
  "Tra Anzio e Nettuno", ["A Salerno", "In Normandia", "A Gela"],
  "L'obiettivo era aprire la strada verso Roma.", "sbarcarono alle spalle dei tedeschi lungo la costa tra Anzio e Nettuno")
P2("sto-255", "Seconda guerra mondiale", 2, "Quale antica abbazia fu completamente distrutta dai bombardamenti alleati nel 1944?",
  "Montecassino", ["San Galgano", "Subiaco", "Pomposa"],
  "Si trovava lungo la linea Gustav.", "l'antica abbazia di Montecassino finì")
P2("sto-256", "Seconda guerra mondiale", 3, "Tra quali città si estendeva la Linea Gotica?",
  "Da Massa a Pesaro", ["Da Gaeta a Ortona", "Da Genova a Venezia", "Da Roma a Pescara"],
  "Vi ripiegarono i tedeschi dopo la liberazione di Roma.", "Linea Gotica, estesa da Massa a Pesaro")
P2("sto-257", "Seconda guerra mondiale", 3, "Quando fu liberata Firenze?",
  "Il 13 agosto 1944", ["Il 4 giugno 1944", "Il 25 aprile 1945", "Il 18 luglio 1944"],
  "Ancona era stata liberata il 18 luglio.", "Firenze il 13 agosto")
P2("sto-258", "Seconda guerra mondiale", 4, "Dove avvenne il 25 aprile 1945 il primo incontro tra truppe sovietiche e statunitensi?",
  "A Torgau, sul fiume Elba", ["A Berlino", "A Vienna", "A Praga"],
  "Lo stesso giorno in Italia si celebra la Liberazione.", "a Torgau, sul fiume Elba, il 25 aprile")
P2("sto-259", "Seconda guerra mondiale", 3, "Quando fu liberata Bologna?",
  "Il 21 aprile 1945", ["Il 25 aprile 1945", "Il 4 giugno 1944", "Il 1° maggio 1945"],
  "Gli Alleati valicarono poi il Po.", "su Bologna, liberata il 21 aprile")
P2("sto-260", "Seconda guerra mondiale", 3, "Come si chiamava il programma statunitense per la bomba atomica, coordinato da Oppenheimer?",
  "Progetto Manhattan", ["Progetto Apollo", "Operazione Overlord", "Progetto Trinity Bay"],
  "Vi collaborarono centinaia di scienziati statunitensi e britannici.", "sotto il nome in codice di \"Progetto Manhattan\"")
P2("sto-261", "Seconda guerra mondiale", 4, "Quando fu testato con successo il primo prototipo di bomba atomica?",
  "Il 16 luglio 1945, ad Alamogordo", ["Il 6 agosto 1945, a Hiroshima", "Il 2 settembre 1945, nel Pacifico", "Nel 1949, in Kazakistan"],
  "Il prototipo era chiamato «The Gadget».", "venne testato con successo il 16 luglio 1945 nel poligono di Alamogordo")
P2("sto-262", "Seconda guerra mondiale", 4, "Quale confine orientale fu fissato per la Germania alla conferenza di Potsdam del luglio 1945?",
  "La linea Oder-Neiße", ["La linea Curzon", "La linea Maginot", "Il fiume Reno"],
  "Slesia e Pomerania passarono alla Polonia.", "la frontiera orientale fu arretrata alla linea Oder-Neiße")
P2("sto-263", "Seconda guerra mondiale", 2, "Chi sostituì Mussolini alla guida del governo dopo il 25 luglio 1943?",
  "Il maresciallo Pietro Badoglio", ["Dino Grandi", "Vittorio Emanuele III", "Ivanoe Bonomi"],
  "Il nuovo governo dichiarò inizialmente di voler continuare la guerra.", "rimpiazzato alla guida del governo dal maresciallo Pietro")
P2("sto-264", "Seconda guerra mondiale", 2, "Quando si arrese il Giappone, chiudendo la guerra in Asia?",
  "Il 2 settembre 1945", ["L'8 maggio 1945", "Il 6 agosto 1945", "Il 7 dicembre 1945"],
  "Dopo i bombardamenti atomici di Hiroshima e Nagasaki.", "in quello asiatico, il successivo 2 settembre")
P2("sto-265", "Seconda guerra mondiale", 2, "Quanti morti causò, secondo le stime, la Seconda guerra mondiale?",
  "Tra 55 e 60 milioni", ["Circa 5 milioni", "Circa 15 milioni", "Oltre 200 milioni"],
  "È il conflitto più sanguinoso della storia.", "55 e i 60 milioni di individui")
P2("sto-266", "Seconda guerra mondiale", 3, "Quali città liberò l'operazione sovietica «Stella» nel febbraio 1943?",
  "Kursk e Char'kov", ["Leningrado e Mosca", "Berlino e Varsavia", "Kiev e Minsk"],
  "Costrinse i tedeschi a sgombrare il Caucaso.", "l'operazione Stella portò le colonne corazzate sovietiche a liberare Kursk e Char'kov")

RE("sto-267", "Repubblica", 3, "In che data nacque ufficialmente la Repubblica Italiana, con la proclamazione dei risultati definitivi del referendum?",
  "Il 18 giugno 1946", ["Il 2 giugno 1946", "Il 1° gennaio 1948", "Il 25 aprile 1945"],
  "La Corte di cassazione respinse i ricorsi e completò lo scrutinio.", "La Repubblica Italiana nacque ufficialmente il 18 giugno 1946")
RE("sto-268", "Repubblica", 3, "Come si chiama il provvedimento del 22 giugno 1946 per la riconciliazione nazionale?",
  "Amnistia Togliatti", ["Legge Scelba", "Decreto De Gasperi", "Lodo Moro"],
  "Prese il nome dal guardasigilli che l'aveva concepita.", "fu emanata poi la cosiddetta amnistia Togliatti")
RE("sto-269", "Repubblica", 3, "Quale ministro delle Finanze realizzò un riassetto fiscale negli anni del centrismo?",
  "Ezio Vanoni", ["Luigi Einaudi", "Ugo La Malfa", "Giulio Andreotti"],
  "Nello stesso periodo nacque la Cassa per il Mezzogiorno.", "operato dal ministro delle Finanze Ezio Vanoni")
RE("sto-270", "Repubblica", 3, "Quale ente nacque nel 1964 dopo la nazionalizzazione dell'energia elettrica?",
  "L'Enel", ["L'ENI", "L'IRI", "L'Agip"],
  "La nazionalizzazione fu osteggiata dal PLI e da Edison e SADE.", "che nel 1964 porterà alla nascita dell'Enel")
RE("sto-271", "Repubblica", 3, "Fino a quale età fu estesa la scuola dell'obbligo dal primo centro-sinistra?",
  "14 anni", ["11 anni", "16 anni", "18 anni"],
  "Fu uno degli atti di rilievo del governo di centro-sinistra.", "l'estensione della scuola dell'obbligo fino ai 14 anni")
RE("sto-272", "Repubblica", 3, "Quale ministro volle lo Statuto dei lavoratori, approvato il 20 maggio 1970?",
  "Giacomo Brodolini", ["Carlo Donat-Cattin", "Pietro Nenni", "Amintore Fanfani"],
  "Nello stesso periodo furono approvate le norme sui referendum.", "lo statuto dei lavoratori voluto dal ministro Giacomo Brodolini")
RE("sto-273", "Repubblica", 3, "Con quale legge del 1970 furono istituite le Regioni a statuto ordinario?",
  "La legge del 16 maggio 1970", ["La legge del 1° gennaio 1948", "La legge del 1963", "La legge del 2001"],
  "Fu una delle riforme in risposta al Sessantotto.", "l'istituzione delle Regioni con legge del 16 maggio 1970")
RE("sto-274", "Repubblica", 2, "Quando avvenne la strage di piazza Fontana a Milano?",
  "Il 12 dicembre 1969", ["Il 2 agosto 1980", "Il 16 marzo 1978", "Il 28 maggio 1974"],
  "Uccise diciassette persone; le indagini puntarono inizialmente sugli anarchici.", "Il 12 dicembre 1969 la strage di piazza Fontana")
RE("sto-275", "Repubblica", 3, "Come è ricordata l'ondata di scioperi del 1969 che coinvolse circa 1,5 milioni di lavoratori?",
  "Autunno caldo", ["Biennio rosso", "Maggio francese", "Marcia dei quarantamila"],
  "Portò al rinnovo del contratto collettivo nazionale.", "sfociarono nell'\"autunno caldo\" del 1969")
RE("sto-276", "Repubblica", 3, "Quale disastro del 9 ottobre 1963 distrusse Longarone causando circa duemila morti?",
  "Il disastro del Vajont", ["L'alluvione di Firenze", "Il terremoto del Belice", "Il disastro di Seveso"],
  "Fu attribuito alla sottovalutazione del rischio idrogeologico.", "il 9 ottobre si verificò il disastro del Vajont, che distrusse Longarone")
RE("sto-277", "Repubblica", 3, "Quale linea politica promosse Berlinguer per legittimare il PCI come forza di governo?",
  "L'eurocomunismo", ["Il centrismo", "Il compromesso di Yalta", "Il pentapartito"],
  "Affermava l'autonomia da Mosca e la fedeltà alla NATO.", "Berlinguer promosse l'eurocomunismo")
RE("sto-278", "Repubblica", 2, "Chi fu Presidente della Repubblica dal 1978 al 1985?",
  "Sandro Pertini", ["Giovanni Leone", "Francesco Cossiga", "Giuseppe Saragat"],
  "Fu eletto con il sostegno decisivo di Craxi.", "Sandro Pertini, Presidente della")
RE("sto-279", "Repubblica", 2, "Chi furono le vittime principali della strage di Capaci del 1992?",
  "Il giudice Giovanni Falcone, la moglie e tre agenti di scorta", ["Paolo Borsellino e la scorta", "Aldo Moro e la scorta", "Carlo Alberto dalla Chiesa"],
  "Pochi mesi dopo la strage di via D'Amelio uccise Borsellino.", "in cui persero la vita il magistrato antimafia Giovanni Falcone")
RE("sto-280", "Repubblica", 3, "Chi guidò nel 1993 il primo governo presieduto da un tecnico non parlamentare?",
  "Carlo Azeglio Ciampi", ["Giuliano Amato", "Lamberto Dini", "Mario Monti"],
  "Traghettò il sistema politico verso la Seconda Repubblica.", "da un tecnico indipendente, Carlo Azeglio Ciampi")
RE("sto-281", "Repubblica", 3, "In quale miniera belga morirono nel 1956 numerosi minatori italiani?",
  "Marcinelle", ["Charleroi Nord", "Liegi", "Anversa"],
  "Il disastro mise in luce le condizioni dell'emigrazione italiana.", "il disastro di Marcinelle in una miniera del Belgio nel 1956")
RE("sto-282", "Repubblica", 3, "Quale presidente della Repubblica, della sinistra DC, era amico di Enrico Mattei?",
  "Giovanni Gronchi", ["Luigi Einaudi", "Antonio Segni", "Giovanni Leone"],
  "Guardava con favore all'apertura ai socialisti.", "il nuovo presidente della Repubblica Giovanni Gronchi")
RE("sto-283", "Repubblica", 3, "Con quale trattato del 1951 l'Italia aderì alla CECA?",
  "Il Trattato di Parigi", ["I Trattati di Roma", "Il Trattato di Maastricht", "Il Patto Atlantico"],
  "La CECA fu il primo embrione dell'integrazione europea.", "nel 1951 l'Italia aderì al Trattato di Parigi che istituiva la CECA")
RE("sto-284", "Repubblica", 4, "Come fu chiamato il governo monocolore DC di Giovanni Leone del 1963?",
  "«Governo balneare»", ["«Governo delle convergenze parallele»", "«Governo della non sfiducia»", "«Governo dei tecnici»"],
  "Durante il suo breve mandato avvenne il disastro del Vajont.", "il cosiddetto \"governo balneare\"")
RE("sto-285", "Repubblica", 3, "Come fu chiamato il terzo governo Andreotti sostenuto dall'astensione di quasi tutti i partiti?",
  "Governo della non sfiducia", ["Governo balneare", "Governo di unità nazionale del CLN", "Pentapartito"],
  "Aprì la stagione della «solidarietà nazionale» tra DC e PCI.", "La complessità del risultato impose la nascita di un \"governo della non sfiducia\"")
RE("sto-286", "Repubblica", 3, "Quale ministro dell'Interno represse con fermezza le proteste sindacali dei primi anni Cinquanta?",
  "Mario Scelba", ["Paolo Emilio Taviani", "Francesco Cossiga", "Amintore Fanfani"],
  "Celebre la repressione alle Fonderie Riunite di Modena nel 1950.", "vennero fermamente represse dal ministro dell'Interno Mario Scelba")

GFR("sto-287", "Guerra fredda", 2, "Quale fu il primo satellite artificiale, lanciato dall'URSS nel 1957?",
  "Lo Sputnik 1", ["L'Apollo 11", "L'Explorer 1", "La Vostok 1"],
  "Avviò la corsa allo spazio tra le due superpotenze.", "lanciarono il primo satellite artificiale, lo Sputnik 1")
GFR("sto-288", "Guerra fredda", 3, "Come si concluse la rivoluzione ungherese del 1956?",
  "I carri armati sovietici riconquistarono Budapest e Nagy fu giustiziato", ["Con l'uscita dell'Ungheria dal Patto di Varsavia", "Con l'intervento della NATO", "Con libere elezioni"],
  "Gli eventi provocarono una frattura nei partiti comunisti occidentali.", "il 4 novembre Budapest venne")
GFR("sto-289", "Guerra fredda", 2, "Quale paese invase l'URSS nel 1968 per fermare la Primavera di Praga?",
  "La Cecoslovacchia", ["L'Ungheria", "La Polonia", "La Jugoslavia"],
  "Fu una delle crisi più gravi del blocco orientale.", "invase la Cecoslovacchia per fermare la Primavera")
GFR("sto-290", "Guerra fredda", 2, "Come si chiamavano le riforme di Michail Gorbačëv?",
  "Glasnost («trasparenza») e perestrojka («riorganizzazione»)", ["Destalinizzazione e disgelo", "Grande balzo in avanti", "NEP e collettivizzazione"],
  "Furono introdotte dalla metà degli anni Ottanta.", "glasnost (\"trasparenza\") e perestrojka (\"riorganizzazione\")")
GFR("sto-291", "Guerra fredda", 3, "Quale evento del 1979 pose fine alla fase di distensione?",
  "L'invasione sovietica dell'Afghanistan", ["La crisi di Suez", "La costruzione del Muro di Berlino", "La guerra di Corea"],
  "Seguì una fase di forte tensione con gli Stati Uniti di Reagan.", "La distensione finì con l'invasione sovietica dell'Afghanistan del 1979")
GFR("sto-292", "Guerra fredda", 3, "Quale trattato sul controllo degli armamenti firmarono Nixon e Brežnev nel 1972?",
  "Il SALT I", ["Il trattato INF", "Il START II", "Il trattato di non proliferazione"],
  "Fu il primo patto di limitazione globale tra le superpotenze.", "SALT I, il primo patto di limitazione globale firmato dalle due superpotenze")
GFR("sto-293", "Guerra fredda", 2, "Chi vinse la guerra civile cinese nel 1949?",
  "Mao Zedong", ["Chiang Kai-shek", "Sun Yat-sen", "Deng Xiaoping"],
  "Chiang Kai-shek si rifugiò con il suo governo a Taiwan.", "l'Esercito Popolare di Liberazione di Mao Zedong")
GFR("sto-294", "Guerra fredda", 4, "Quale strategia elaborò l'amministrazione Kennedy per ridurre il rischio di guerra nucleare totale?",
  "La «risposta flessibile»", ["La «rappresaglia massiccia»", "Il «roll back»", "Lo «scudo spaziale»"],
  "Sostituiva la dottrina della rappresaglia massiccia.", "elaborò la strategia della \"risposta flessibile\"")
GFR("sto-295", "Guerra fredda", 2, "Quando si dissolse formalmente l'Unione Sovietica?",
  "Nel dicembre 1991", ["Nel novembre 1989", "Nel 1985", "Nel 1995"],
  "La caduta della cortina di ferro era avvenuta nel 1989.", "alla dissoluzione formale dell'Unione Sovietica nel dicembre 1991")

EU("sto-296", "Integrazione europea", 4, "Con quale trattato del 1948 si fa iniziare il processo di integrazione europea, secondo la voce?",
  "Il Trattato di Bruxelles", ["Il Trattato di Roma", "Il Trattato di Parigi", "Il Trattato di Maastricht"],
  "Seguirono molti altri trattati e referendum.", "iniziato nel 1948 con il Trattato di Bruxelles")
EU("sto-297", "Integrazione europea", 3, "Quale ministro degli esteri belga studiò il progetto di mercato comune confluito nei Trattati di Roma?",
  "Paul-Henri Spaak", ["Robert Schuman", "Jean Monnet", "Konrad Adenauer"],
  "La sua proposta si unì a quella di Monnet sull'energia.", "ministro degli esteri belga Paul-Henri Spaak su un mercato comune")
EU("sto-298", "Integrazione europea", 4, "Quale paese respinse il Trattato di Maastricht con un referendum nel 1992, approvandolo l'anno dopo?",
  "La Danimarca", ["La Francia", "L'Irlanda", "Il Regno Unito"],
  "Il secondo referendum fu positivo.", "lo approvò l'anno dopo in un nuovo referendum")
EU("sto-299", "Integrazione europea", 3, "Quale spazio economico fu formato nel 1992 dall'UE e dall'EFTA?",
  "Lo Spazio economico europeo (SEE)", ["L'area Schengen", "L'Eurozona", "Il Consiglio d'Europa"],
  "L'EFTA è l'Associazione europea di libero scambio.", "Spazio economico europeo (SEE) nel 1992")
EU("sto-300", "Integrazione europea", 4, "Quale maggioranza serviva all'assemblea comune dei Trattati di Roma per censurare le decisioni della Commissione?",
  "I due terzi", ["La maggioranza semplice", "L'unanimità", "Tre quinti"],
  "L'assemblea è l'antenata del Parlamento europeo.", "maggioranza fissata in 2/3")
