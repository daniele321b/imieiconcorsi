# Geografia — fonti: voci di Wikipedia (CC BY-SA 4.0) e Annuario statistico ISTAT 2025 (CC BY), usate solo per i fatti.
GI = "Wikipedia_Geografia-dell-Italia.txt"
REG = "Wikipedia_Regioni-d-Italia.txt"
UE = "Wikipedia_Unione-europea.txt"
POP = "ISTAT_Annuario2025_cap3_Popolazione.txt"
W = lambda voce: f"Wikipedia, «{voce}» (CC BY-SA 4.0)"

D("geo-001", "Italia fisica", 1, "Qual è il punto più elevato d'Italia?",
  "Il Monte Bianco", ["Il Monte Rosa", "Il Gran Paradiso", "Il Cervino"],
  "Il Monte Bianco, in Valle d'Aosta, è il punto più alto del Paese (oltre 4.800 m).",
  W("Geografia dell'Italia"), GI, "Punto più elevato: Monte Bianco (AO)")

D("geo-002", "Italia fisica", 1, "Qual è il fiume più lungo d'Italia?",
  "Il Po", ["Il Tevere", "L'Adige", "L'Arno"],
  "Il Po (652 km) nasce dal Monviso, attraversa la Pianura Padana e sfocia con un delta nell'Adriatico.",
  W("Geografia dell'Italia"), GI, "Il più lungo fiume italiano è il Po (652 km)")

D("geo-003", "Italia fisica", 2, "Da quale monte nasce il Po?",
  "Dal Monviso", ["Dal Monte Bianco", "Dal Monte Fumaiolo", "Dal Gran Sasso"],
  "Il Po sgorga dal Monviso, nelle Alpi Cozie; il Tevere invece nasce dal Monte Fumaiolo.",
  W("Geografia dell'Italia"), GI, "che sgorga dal Monviso")

D("geo-004", "Italia fisica", 3, "Qual è il terzo fiume più lungo d'Italia, che nasce dal Monte Fumaiolo?",
  "Il Tevere", ["L'Arno", "Il Volturno", "Il Piave"],
  "Il Tevere (405 km) è il terzo per lunghezza e il secondo per ampiezza del bacino idrografico.",
  W("Geografia dell'Italia"), GI, "Il terzo fiume più lungo in Italia è il Tevere (405 km)")

D("geo-005", "Italia fisica", 1, "Qual è il lago più vasto d'Italia?",
  "Il Lago di Garda", ["Il Lago Maggiore", "Il Lago di Como", "Il Lago Trasimeno"],
  "Il Lago di Garda è il più esteso dei laghi italiani, di origine glaciale.",
  W("Geografia dell'Italia"), GI, "il Lago di Garda (il più vasto d'Italia)")

D("geo-006", "Italia fisica", 2, "Qual è il vulcano attivo più alto d'Europa?",
  "L'Etna", ["Il Vesuvio", "Lo Stromboli", "Vulcano"],
  "L'Etna, vicino a Catania, con circa 3.343 m è il vulcano più alto d'Europa.",
  W("Geografia dell'Italia"), GI, "l'Etna vicino a Catania che con i suoi 3.343 m è il vulcano più alto d'Europa")

D("geo-007", "Italia fisica", 2, "Quali sono le due isole più grandi del Mediterraneo, entrambe italiane?",
  "Sicilia e Sardegna", ["Sicilia e Corsica", "Sardegna e Creta", "Sicilia e Cipro"],
  "L'Italia insulare comprende le due maggiori isole del Mediterraneo, la Sardegna e la Sicilia.",
  W("Geografia dell'Italia"), GI, "le due maggiori isole del Mediterraneo, la Sardegna e la Sicilia")

D("geo-008", "Italia fisica", 3, "Qual è la superficie della Repubblica italiana, in cifra tonda?",
  "Circa 302.000 km²", ["Circa 250.000 km²", "Circa 360.000 km²", "Circa 210.000 km²"],
  "La superficie della Repubblica italiana è di 302.073 km².",
  W("Geografia dell'Italia"), GI, "della Repubblica italiana (302 073 km2)")

D("geo-009", "Confini", 2, "Con quali Stati confina l'Italia via terra (esclusi i microstati)?",
  "Francia, Svizzera, Austria e Slovenia", ["Francia, Svizzera, Germania e Slovenia", "Francia, Austria, Croazia e Slovenia", "Svizzera, Austria, Ungheria e Slovenia"],
  "L'Italia confina a ovest con la Francia, a nord con Svizzera e Austria, a est con la Slovenia.",
  W("Geografia dell'Italia"), GI, "confinando ad ovest con la Francia, a nord con la Svizzera e l'Austria e ad est con la Slovenia")

D("geo-010", "Confini", 2, "Quali microstati sono enclavi interamente comprese nel territorio italiano?",
  "San Marino e Città del Vaticano", ["Monaco e San Marino", "Liechtenstein e Città del Vaticano", "Andorra e San Marino"],
  "San Marino e Città del Vaticano sono enclavi interamente circondate dall'Italia.",
  W("Geografia dell'Italia"), GI, "i microstati San Marino e Città del Vaticano sono enclavi")

D("geo-011", "Confini", 3, "Qual è il comune più a nord d'Italia?",
  "Predoi", ["Bardonecchia", "Sesto", "Livigno"],
  "Comuni estremi: Predoi a nord, Lampedusa e Linosa a sud, Otranto a est, Bardonecchia a ovest.",
  W("Geografia dell'Italia"), GI, "Predoi, il comune più a nord")

D("geo-012", "Confini", 3, "Qual è il comune più a est d'Italia?",
  "Otranto", ["Lecce", "Trieste", "Santa Maria di Leuca"],
  "Otranto, in Puglia, è il comune più orientale; Bardonecchia il più occidentale.",
  W("Geografia dell'Italia"), GI, "Otranto, il comune più a est")

D("geo-013", "Confini", 2, "Qual è il comune più a sud d'Italia?",
  "Lampedusa e Linosa", ["Pantelleria", "Pachino", "Portopalo di Capo Passero"],
  "Il comune più meridionale è Lampedusa e Linosa, nelle isole Pelagie.",
  W("Geografia dell'Italia"), GI, "Lampedusa e Linosa, il comune più a sud")

D("geo-014", "Regioni", 1, "Quante sono le regioni italiane e quante di queste sono a statuto speciale?",
  "20 regioni, di cui 5 a statuto speciale", ["20 regioni, di cui 3 a statuto speciale", "21 regioni, di cui 5 a statuto speciale", "19 regioni, di cui 6 a statuto speciale"],
  "Le regioni sono 20: 15 a statuto ordinario e 5 a statuto speciale.",
  W("Regioni d'Italia"), REG, "Sono 20, di cui 15 a statuto ordinario e 5 a statuto speciale")

D("geo-015", "Regioni", 3, "Come compariva il Molise nel testo originario dell'art. 131 della Costituzione?",
  "Insieme all'Abruzzo, nella regione «Abruzzi e Molise»", ["Come regione autonoma", "Insieme alla Campania", "Non compariva: è stato creato dalle Province"],
  "L'art. 131 nel testo originario elencava «Abruzzi e Molise»; il Molise è diventato regione autonoma nel 1963.",
  W("Regioni d'Italia"), REG, "Abruzzi e Molise")

D("geo-016", "Popolazione", 2, "Quanti residenti contava l'Italia al 1° gennaio 2025, secondo l'ISTAT (dati provvisori)?",
  "Circa 58,9 milioni", ["Circa 61,5 milioni", "Circa 55 milioni", "Circa 64 milioni"],
  "ISTAT, Annuario 2025: 58.934.177 residenti al 1° gennaio 2025, circa 37 mila in meno rispetto all'anno prima.",
  "ISTAT, Annuario statistico italiano 2025, cap. 3 (CC BY)", POP, "la popolazione residente in Italia è pari a 58.934.177 individui")

D("geo-017", "Popolazione", 3, "Rispetto all'anno precedente, come è cambiata la popolazione residente al 1° gennaio 2025?",
  "È diminuita di circa 37 mila persone", ["È aumentata di circa 100 mila persone", "È rimasta identica", "È diminuita di oltre un milione"],
  "Secondo l'ISTAT la popolazione è calata di circa 37 mila unità rispetto alla stessa data del 2024.",
  "ISTAT, Annuario statistico italiano 2025, cap. 3 (CC BY)", POP, "circa 37 mila unità in meno")

D("geo-018", "Unione europea", 1, "Quanti Stati membri ha l'Unione europea?",
  "27", ["25", "28", "30"],
  "Dopo l'uscita del Regno Unito l'Unione europea comprende 27 Stati membri.",
  W("Unione europea"), UE, "che comprende 27 Stati membri")

D("geo-019", "Unione europea", 2, "Quante sono le lingue ufficiali dell'Unione europea?",
  "24", ["27", "12", "3"],
  "L'Unione europea ha 24 lingue ufficiali.",
  W("Unione europea"), UE, "Lingua ufficiale 24 lingue")

D("geo-020", "Unione europea", 3, "In quale città ha sede la Banca centrale europea?",
  "Francoforte sul Meno", ["Bruxelles", "Lussemburgo", "Strasburgo"],
  "La BCE ha sede a Francoforte sul Meno; Commissione e Consiglio a Bruxelles; il Parlamento a Strasburgo; la Corte di giustizia a Lussemburgo.",
  W("Unione europea"), UE, "Francoforte sul Meno")

D("geo-021", "Unione europea", 3, "Con quale trattato l'Unione europea ha assunto la struttura attuale?",
  "Il trattato di Lisbona del 2007", ["Il trattato di Maastricht del 1992", "I Trattati di Roma del 1957", "Il trattato di Nizza del 2001"],
  "Nata come CEE nel 1957 e trasformata a Maastricht (1992), l'Unione ha la struttura attuale dal trattato di Lisbona del 2007.",
  W("Unione europea"), UE, "Lisbona del 2007")


# --- Blocco 2: Alpi, Appennini, Po ---
ALPI = "Wikipedia_Alpi.txt"
APP = "Wikipedia_Appennini.txt"
PO = "Wikipedia_Po.txt"

D("geo-022", "Montagne", 1, "Qual è la catena montuosa più importante d'Europa, che racchiude a nord la regione italiana?",
  "Le Alpi", ["Gli Appennini", "I Pirenei", "I Carpazi"],
  "Voce «Alpi».",
  W("Alpi"), ALPI, "Le Alpi sono la catena montuosa più importante d'Europa")

D("geo-023", "Montagne", 2, "Qual è la montagna più alta delle Alpi?",
  "Il Monte Bianco", ["Il Monte Rosa", "Il Cervino", "Il Gran Paradiso"],
  "Si trova al confine tra Italia e Francia.",
  W("Alpi"), ALPI, "La montagna più alta è il Monte Bianco, posto al confine tra Italia e Francia")

D("geo-024", "Montagne", 3, "Per quanti chilometri circa si estende l'arco alpino?",
  "Circa 1300 km", ["Circa 300 km", "Circa 3000 km", "Circa 600 km"],
  "Voce «Alpi».",
  W("Alpi"), ALPI, "L'intero sistema montuoso si distende per circa 1300 km")

D("geo-025", "Montagne", 3, "Quale valico segna convenzionalmente il limite occidentale delle Alpi (e il punto d'unione con gli Appennini)?",
  "La Bocchetta di Altare o colle di Cadibona", ["Il passo del Brennero", "Il passo dello Stelvio", "Il colle del Moncenisio"],
  "Voce «Alpi».",
  W("Alpi"), ALPI, "il limite occidentale delle Alpi è la Bocchetta di Altare o colle di Cadibona")

D("geo-026", "Montagne", 3, "In quali tre grandi parti la «Partizione delle Alpi» divide la catena?",
  "Alpi Occidentali, Centrali e Orientali", ["Alpi Alte, Medie e Basse", "Alpi Italiane, Francesi e Svizzere", "Prealpi, Alpi e Dolomiti"],
  "Voce «Alpi».",
  W("Alpi"), ALPI, "Alpi Occidentali, Alpi Centrali e Alpi Orientali")

D("geo-027", "Montagne", 4, "Quale passo separa le Alpi Centrali dalle Alpi Orientali secondo la Partizione delle Alpi?",
  "Il passo del Brennero", ["Il colle di Cadibona", "Il col Ferret", "Il passo di Vrata"],
  "Le Centrali vanno dal col Ferret al Brennero.",
  W("Alpi"), ALPI, "le Alpi Centrali dal col Ferret al passo del Brennero")

D("geo-028", "Montagne", 3, "A quale grande parte delle Alpi appartengono le Dolomiti?",
  "Alle Alpi Orientali", ["Alle Alpi Occidentali", "Alle Alpi Centrali", "Agli Appennini"],
  "Voce «Alpi».",
  W("Alpi"), ALPI, "Alpi Orientali: Alpi Noriche, Dolomiti")

D("geo-029", "Montagne", 3, "A quale grande parte delle Alpi appartengono le Alpi Marittime e le Cozie?",
  "Alle Alpi Occidentali", ["Alle Alpi Centrali", "Alle Alpi Orientali", "Alle Prealpi"],
  "Voce «Alpi».",
  W("Alpi"), ALPI, "Alpi Occidentali: Alpi Marittime, Alpi Cozie")

D("geo-030", "Montagne", 2, "Come si chiama la celebre mummia dell'età del rame ritrovata sulle Alpi (uomo di Similaun)?",
  "Ötzi", ["Lucy", "Tutankhamon", "Uomo di Neanderthal"],
  "Voce «Alpi».",
  W("Alpi"), ALPI, "l'uomo di Similaun (detto anche \"Ötzi\")")

D("geo-031", "Montagne", 3, "In che anno fu istituito nelle Alpi svizzere il primo parco nazionale d'Europa?",
  "Nel 1914", ["Nel 1872", "Nel 1922", "Nel 1960"],
  "Voce «Alpi».",
  W("Alpi"), ALPI, "istituito nelle Alpi svizzere nel 1914")

D("geo-032", "Montagne", 2, "Per quanti chilometri circa si estendono gli Appennini (senza l'Appennino siculo)?",
  "Circa 1200 km", ["Circa 600 km", "Circa 2500 km", "Circa 400 km"],
  "Comprendendo l'Appennino siculo si arriva a 1400 km.",
  W("Appennini"), APP, "Gli Appennini sono il sistema montuoso lungo circa 1200 km")

D("geo-033", "Montagne", 1, "Come sono spesso chiamati gli Appennini?",
  "La «spina dorsale» della penisola italiana", ["Il «tetto d'Europa»", "Le «montagne bianche»", "Il «muro del Nord»"],
  "Voce «Appennini».",
  W("Appennini"), APP, "spina dorsale della penisola italiana")

D("geo-034", "Montagne", 2, "Qual è la cima più alta degli Appennini?",
  "Il Corno Grande, nel Gran Sasso", ["Il Monte Vettore", "La Maiella (Monte Amaro)", "Il Monte Cimone"],
  "Raggiunge 2912 m in Abruzzo.",
  W("Appennini"), APP, "La cima più alta è il Corno Grande, nel massiccio del Gran Sasso")

D("geo-035", "Montagne", 3, "Qual è l'unico ghiacciaio degli Appennini, il più meridionale d'Europa?",
  "Il Calderone, sul Gran Sasso", ["Il ghiacciaio del Pollino", "Il ghiacciaio della Marmolada", "Il ghiacciaio del Terminillo"],
  "Voce «Appennini».",
  W("Appennini"), APP, "È presente un solo ghiacciaio, quello del Calderone")

D("geo-036", "Montagne", 3, "Quali rilievi appenninici sono costituiti da rocce granitiche?",
  "La Sila e l'Aspromonte", ["Le Alpi Apuane e i Sibillini", "Il Gran Sasso e la Maiella", "Il Pollino e gli Alburni"],
  "Il resto degli Appennini è formato in prevalenza da calcari e argille.",
  W("Appennini"), APP, "solamente la Sila e l'Aspromonte sono costituiti da rocce granitiche")

D("geo-037", "Montagne", 3, "Quale vetta appenninica appartiene alla Repubblica di San Marino?",
  "Il Monte Titano", ["Il Monte Carpegna", "Il Monte Fumaiolo", "Il Monte Falterona"],
  "Voce «Appennini».",
  W("Appennini"), APP, "con l'eccezione del Monte Titano, appartenente alla Repubblica di San Marino")

D("geo-038", "Montagne", 4, "Dov'è più stretta la catena appenninica (circa 30 km)?",
  "All'istmo di Catanzaro, tra i golfi di Sant'Eufemia e di Squillace", ["Tra Ancona e Piombino", "Tra Roma e Pescara", "Tra Napoli e Bari"],
  "Anche tra Genova Voltri e Gavi la larghezza è di circa 30 km.",
  W("Appennini"), APP, "Golfo di Sant'Eufemia sul Tirreno e il Golfo di Squillace sullo Ionio")

D("geo-039", "Montagne", 3, "Quali linee difensive tedesche della Seconda guerra mondiale sfruttavano gli Appennini?",
  "Linea Gustav e Linea Gotica", ["Linea Maginot e Linea Sigfrido", "Linea Mannerheim", "Vallo Atlantico"],
  "Voce «Appennini».",
  W("Appennini"), APP, "la linea Gustav e la linea Barbara")

D("geo-040", "Montagne", 3, "Quali vulcani sono ancora attivi nell'Antiappennino campano?",
  "Il Vesuvio e i Campi Flegrei", ["I Colli Albani", "L'Amiata", "Il Vulture"],
  "I vulcani dei Colli Albani sono invece spenti.",
  W("Appennini"), APP, "ancora attivi il Vesuvio e i Campi Flegrei")

D("geo-041", "Fiumi", 2, "Quanto è lungo il Po?",
  "652 km", ["405 km", "1000 km", "241 km"],
  "È il fiume più lungo interamente compreso nel territorio italiano.",
  W("Po"), PO, "La sua lunghezza, 652 km")

D("geo-042", "Fiumi", 3, "Dove nasce il Po?",
  "Sul Monviso, al Pian del Re (Piemonte)", ["Sul Monte Rosa", "Sul Monte Fumaiolo", "Sul Gran Paradiso"],
  "Voce «Po».",
  W("Po"), PO, "Ha origine in Piemonte, sul Monviso, al Pian del Re")

D("geo-043", "Fiumi", 3, "Quale capoluogo di regione è attraversato dal Po?",
  "Torino", ["Milano", "Bologna", "Venezia"],
  "Bagna anche i capoluoghi di provincia Piacenza e Cremona.",
  W("Po"), PO, "bagna direttamente un capoluogo di regione (Torino)")

D("geo-044", "Fiumi", 3, "In quale mare sfocia il Po e in che modo?",
  "Nell'Adriatico, con un vasto delta", ["Nel Tirreno, con un estuario", "Nel Ligure, con una sola foce", "Nello Ionio, con un delta"],
  "Voce «Po».",
  W("Po"), PO, "sfociare nel mare Adriatico in un vasto delta")

D("geo-045", "Fiumi", 4, "Quante province attraversa il Po?",
  "Tredici", ["Cinque", "Venti", "Otto"],
  "Da Cuneo a Rovigo.",
  W("Po"), PO, "Attraversa tredici province")

D("geo-046", "Fiumi", 4, "Con quale nome letterario è indicato il Po, derivato dalla mitologia greca?",
  "Eridano", ["Padania", "Bodinkòs", "Spinetico"],
  "In latino era Padus.",
  W("Po"), PO, "in italiano letterario Eridano")

D("geo-047", "Fiumi", 3, "Quale regione è separata dalla Lombardia, per lunghi tratti, dal corso del Po?",
  "L'Emilia-Romagna", ["Il Piemonte", "La Liguria", "Il Trentino"],
  "Il Po segna anche il confine tra Emilia-Romagna e Veneto.",
  W("Po"), PO, "segna per lunghi tratti il confine tra Lombardia e Emilia-Romagna")


# --- Blocco 3: fiumi, laghi, isole, parchi, città metropolitane ---
FIU = "Wikipedia_Fiumi-d-Italia.txt"
LAG = "Wikipedia_Laghi-d-Italia.txt"
ISO = "Wikipedia_Isole-dell-Italia.txt"
PAR = "Wikipedia_Parchi-nazionali-d-Italia.txt"
CM = "Wikipedia_Città-metropolitane-d-Italia.txt"

D("geo-048", "Fiumi", 3, "Perché i fiumi italiani sono generalmente più brevi di quelli delle altre regioni europee?",
  "Perché l'Italia è in parte una penisola, divisa dagli Appennini in due versanti", ["Perché piove pochissimo", "Perché sono tutti artificiali", "Perché nascono tutti dalle Alpi"],
  "Voce «Fiumi d'Italia».",
  W("Fiumi d'Italia"), FIU, "lungo la quale si eleva la catena degli Appennini che divide le acque in due versanti opposti")

D("geo-049", "Fiumi", 4, "Qual è l'asta fluviale più lunga d'Italia, considerando anche il Tanaro e il Negrone?",
  "Negrone-Tanaro-Po, con 712 km", ["Adige-Po, con 1000 km", "Tevere-Aniene, con 500 km", "Ticino-Po, con 900 km"],
  "Voce «Fiumi d'Italia».",
  W("Fiumi d'Italia"), FIU, "l'asta fluviale più lunga d'Italia è il Negrone-Tanaro-Po, con 712 km")

D("geo-050", "Fiumi", 4, "Qual è il fiume più lungo tra quelli che scorrono almeno in parte in Italia?",
  "La Drava", ["Il Po", "Il Danubio", "Il Rodano"],
  "La Drava misura 749 km.",
  W("Fiumi d'Italia"), FIU, "è invece la Drava, con i suoi 749 km")

D("geo-051", "Fiumi", 3, "Quando sono soggetti a piene i fiumi alpini?",
  "In primavera ed estate, per lo scioglimento dei ghiacciai", ["Solo in inverno", "In autunno, per le piogge", "Mai, hanno portata costante"],
  "I fiumi appenninici hanno invece piene improvvise in primavera e autunno.",
  W("Fiumi d'Italia"), FIU, "soggetti a piene nella stagione primaverile ed estiva")

D("geo-052", "Fiumi", 3, "Che regime hanno, in generale, i fiumi sardi e siciliani?",
  "Torrentizio: pieni d'inverno e quasi secchi d'estate", ["Glaciale, con piene estive", "Costante tutto l'anno", "Carsico, con portata uniforme"],
  "Fanno eccezione Tirso, Flumendosa, Coghinas e Simeto.",
  W("Fiumi d'Italia"), FIU, "I fiumi Sardi e Siciliani sono di carattere torrentizio")

D("geo-053", "Fiumi", 2, "Qual è il secondo fiume d'Italia per lunghezza?",
  "L'Adige", ["Il Tevere", "L'Arno", "Il Piave"],
  "È lungo circa 410 km e nasce presso il Passo di Resia.",
  W("Fiumi d'Italia"), FIU, "l'Adige, lungo circa 410 km, è il secondo fiume d'Italia per lunghezza")

D("geo-054", "Fiumi", 3, "Dove nasce l'Adige?",
  "Presso il Passo di Resia", ["Sul Monviso", "Al Passo del Brennero", "Sulla Marmolada"],
  "Voce «Fiumi d'Italia».",
  W("Fiumi d'Italia"), FIU, "Nasce presso il Passo di Resia")

D("geo-055", "Fiumi", 4, "Quale fiume nasce dai laghi di Caldonazzo e Levico, in Valsugana?",
  "Il Brenta", ["Il Piave", "Il Sile", "L'Adige"],
  "Voce «Fiumi d'Italia».",
  W("Fiumi d'Italia"), FIU, "il Brenta nasce nell'alta Valsugana dai laghi di Caldonazzo e di Levico")

D("geo-056", "Fiumi", 4, "Quale fiume veneto è un tipico fiume di risorgiva, con la maggiore sorgente italiana?",
  "Il Sile", ["Il Brenta", "Il Tagliamento", "La Livenza"],
  "Voce «Fiumi d'Italia».",
  W("Fiumi d'Italia"), FIU, "il Sile, tipico fiume di risorgiva")

D("geo-057", "Fiumi", 3, "Da quale montagna nasce il Piave?",
  "Dal Monte Peralba, nelle Alpi Carniche", ["Dal Monte Bianco", "Dalla Marmolada", "Dal Monte Grappa"],
  "Voce «Fiumi d'Italia».",
  W("Fiumi d'Italia"), FIU, "il Piave nasce dalle Alpi Carniche (Monte Peralba)")

D("geo-058", "Fiumi", 3, "Dove nasce l'Isonzo?",
  "Nelle Alpi Giulie, in Slovenia", ["Nelle Dolomiti", "Nelle Alpi Carniche, in Italia", "Nel Carso triestino"],
  "Sfocia presso Monfalcone.",
  W("Fiumi d'Italia"), FIU, "l'Isonzo nasce dalle Alpi Giulie in Slovenia")

D("geo-059", "Fiumi", 4, "Quale grande alluvione del Po colpì il Polesine nel 1951?",
  "L'alluvione del Polesine del novembre 1951", ["L'alluvione di Firenze", "L'alluvione del Vajont", "L'alluvione di Sarno"],
  "Il tratto finale del Po scorre in argini pensili.",
  W("Fiumi d'Italia"), FIU, "l'alluvione che avvenne in Polesine nel novembre del 1951")

D("geo-060", "Laghi", 1, "Qual è il lago più esteso d'Italia?",
  "Il lago di Garda (Benaco)", ["Il lago Maggiore", "Il lago di Como", "Il lago Trasimeno"],
  "Misura 370 km².",
  W("Laghi d'Italia"), LAG, "Il lago di Garda o Benaco è il più esteso lago d'Italia")

D("geo-061", "Laghi", 2, "Qual è il lago più profondo d'Italia?",
  "Il lago di Como (Lario)", ["Il lago di Garda", "Il lago Maggiore", "Il lago di Bolsena"],
  "Raggiunge 418 m di profondità.",
  W("Laghi d'Italia"), LAG, "è il più profondo fra i laghi italiani (418 m)")

D("geo-062", "Laghi", 2, "Con quale altro nome è noto il lago Maggiore?",
  "Verbano", ["Lario", "Benaco", "Sebino"],
  "Lario è il lago di Como, Benaco il Garda, Sebino il lago d'Iseo.",
  W("Laghi d'Italia"), LAG, "Il lago Maggiore è chiamato anche Verbano")

D("geo-063", "Laghi", 3, "Quale fiume è immissario ed emissario del lago di Como?",
  "L'Adda", ["Il Ticino", "L'Oglio", "Il Mincio"],
  "Voce «Laghi d'Italia».",
  W("Laghi d'Italia"), LAG, "Immissario ed emissario del Lario è il fiume Adda")

D("geo-064", "Laghi", 3, "Quale isola, la più estesa dei laghi italiani, sorge nel lago d'Iseo?",
  "Monte Isola", ["Isola Bella", "Isola Maggiore", "Isola Comacina"],
  "Voce «Laghi d'Italia».",
  W("Laghi d'Italia"), LAG, "l'isola più estesa dei laghi italiani: Monte Isola")

D("geo-065", "Laghi", 3, "Quali isole sorgono nel lago Maggiore?",
  "Le isole Borromee (Madre, Bella, dei Pescatori)", ["Le isole Eolie", "Le isole Tremiti", "Le isole Egadi"],
  "Voce «Laghi d'Italia».",
  W("Laghi d'Italia"), LAG, "emergono le isole Borromee")

D("geo-066", "Laghi", 3, "Qual è il più grande lago appenninico?",
  "Il Trasimeno", ["Il lago di Bolsena", "Il lago di Bracciano", "Il lago di Scanno"],
  "Con 128 km² è il quarto lago d'Italia ed è di origine tettonica.",
  W("Laghi d'Italia"), LAG, "Dei laghi appenninici, il Trasimeno è il più grande")

D("geo-067", "Laghi", 4, "Chi prosciugò il lago del Fucino, in Abruzzo?",
  "Alessandro Torlonia", ["I Borbone", "Mussolini", "Napoleone"],
  "Voce «Laghi d'Italia».",
  W("Laghi d'Italia"), LAG, "fu prosciugato da Alessandro Torlonia")

D("geo-068", "Laghi", 3, "Di che origine sono i grandi laghi prealpini?",
  "Morenica (glaciale)", ["Vulcanica", "Tettonica", "Artificiale"],
  "Voce «Laghi d'Italia».",
  W("Laghi d'Italia"), LAG, "I laghi prealpini, di origine morenica")

D("geo-069", "Laghi", 4, "Quali sono i laghi costieri più estesi della penisola, a nord del Gargano?",
  "I laghi di Lesina e di Varano", ["I laghi di Fogliano e Sabaudia", "I laghi Alimini", "Il lago di Ganzirri"],
  "Voce «Laghi d'Italia».",
  W("Laghi d'Italia"), LAG, "Il lago di Lesina, il lago di Varano")

D("geo-070", "Isole", 2, "Quante isole conta all'incirca il patrimonio insulare italiano?",
  "Oltre 800, di cui solo un'ottantina abitate", ["Circa 50", "Circa 5.000", "Esattamente 100"],
  "Voce «Isole dell'Italia».",
  W("Isole dell'Italia"), ISO, "Il patrimonio insulare italiano consta di oltre 800 isole")

D("geo-071", "Isole", 3, "A quale arcipelago appartengono Alicudi e Filicudi?",
  "Alle Isole Eolie", ["Alle Isole Egadi", "Alle Isole Pelagie", "Alle Isole Tremiti"],
  "Voce «Isole dell'Italia».",
  W("Isole dell'Italia"), ISO, "Isole Eolie o Isole Lipari Isola Alicudi")

D("geo-072", "Isole", 3, "A quale arcipelago appartengono Favignana, Levanzo e Marettimo?",
  "Alle Isole Egadi", ["Alle Isole Eolie", "Alle Isole Pelagie", "All'arcipelago della Maddalena"],
  "Voce «Isole dell'Italia».",
  W("Isole dell'Italia"), ISO, "Isole Egadi Isola di Favignana")

D("geo-073", "Parchi", 3, "Quanti sono i parchi nazionali iscritti nell'Elenco ufficiale delle aree protette?",
  "Ventisei (uno non ancora operativo)", ["Dieci", "Cinquanta", "Cento"],
  "Coprono circa il 5,3% del territorio nazionale.",
  W("Parchi nazionali d'Italia"), PAR, "sono ventisei (di cui uno istituito ma non operativo)")

D("geo-074", "Parchi", 4, "A chi spetta la competenza sui parchi nazionali, anche nelle regioni a statuto speciale, secondo la Corte costituzionale?",
  "Esclusivamente allo Stato", ["Alle regioni", "Ai comuni", "All'Unione europea"],
  "Sentenza n. 12 del 2009.",
  W("Parchi nazionali d'Italia"), PAR, "la competenza in materia di parchi nazionali spetta esclusivamente allo Stato")

D("geo-075", "Parchi", 3, "Quale parco nazionale siciliano è stato istituito nel 2016?",
  "Il Parco nazionale dell'Isola di Pantelleria", ["Il Parco dell'Etna", "Il Parco delle Madonie", "Il Parco dei Nebrodi"],
  "Voce «Parchi nazionali d'Italia».",
  W("Parchi nazionali d'Italia"), PAR, "il Parco nazionale dell'Isola di Pantelleria")

D("geo-076", "Città metropolitane", 2, "Quante sono le città metropolitane in Italia?",
  "Quindici", ["Dieci", "Venti", "Ventisette"],
  "Sono subentrate alle province con la L. 56/2014.",
  W("Città metropolitane d'Italia"), CM, "Le città metropolitane d'Italia sono quindici")

D("geo-077", "Città metropolitane", 3, "Quale legge del 2014 ha disposto il subentro delle città metropolitane alle province?",
  "La legge 7 aprile 2014, n. 56 (legge Delrio)", ["La legge 142/1990", "Il D.Lgs. 267/2000", "La legge costituzionale 3/2001"],
  "Erano state previste per la prima volta dalla L. 142/1990.",
  W("Città metropolitane d'Italia"), CM, "la legge 7 aprile 2014, n. 56")


# --- Blocco 4: geografia generale (Mediterraneo, continenti, oceani, coordinate, fusi orari, Europa) ---
MED = "Wikipedia_Mar-Mediterraneo.txt"
CON = "Wikipedia_Continente.txt"
OCE = "Wikipedia_Oceano.txt"
COO = "Wikipedia_Coordinate-geografiche.txt"
FUS = "Wikipedia_Fuso-orario.txt"
EUR = "Wikipedia_Europa.txt"

D("geo-078", "Mediterraneo", 2, "Attraverso quale stretto il Mediterraneo comunica con l'Oceano Atlantico?",
  "Lo stretto di Gibilterra", ["Lo stretto del Bosforo", "Lo stretto di Messina", "Il canale di Suez"],
  "Il Bosforo lo collega al Mar Nero, il canale di Suez al Mar Rosso.",
  W("Mar Mediterraneo"), MED, "connesso a ovest tramite lo stretto di Gibilterra")

D("geo-079", "Mediterraneo", 2, "Quale opera artificiale collega il Mediterraneo al Mar Rosso?",
  "Il canale di Suez", ["Il canale di Panama", "Il canale di Corinto", "Lo stretto dei Dardanelli"],
  "Voce «Mar Mediterraneo».",
  W("Mar Mediterraneo"), MED, "il canale di Suez, artificiale, lo collega a sud-est al Mar Rosso")

D("geo-080", "Mediterraneo", 3, "Qual è la superficie approssimativa del Mar Mediterraneo?",
  "Circa 2,5 milioni di km²", ["Circa 250.000 km²", "Circa 25 milioni di km²", "Circa 500.000 km²"],
  "Voce «Mar Mediterraneo».",
  W("Mar Mediterraneo"), MED, "La sua superficie approssimativa è di 2,51 milioni di km²")

D("geo-081", "Mediterraneo", 3, "Dove si trova il punto più profondo del Mediterraneo (oltre 5.000 m)?",
  "Presso le coste del Peloponneso", ["Nel Tirreno meridionale", "Al largo di Malta", "Nel Golfo del Leone"],
  "Voce «Mar Mediterraneo».",
  W("Mar Mediterraneo"), MED, "quella massima di 5270 m presso le coste del Peloponneso")

D("geo-082", "Mediterraneo", 1, "Cosa significa la parola latina «mediterraneus»?",
  "«In mezzo alle terre»", ["«Mare profondo»", "«Mare del sole»", "«Mare dei Romani»"],
  "I Romani lo chiamavano Mare nostrum.",
  W("Mar Mediterraneo"), MED, "che significa 'in mezzo alle terre'")

D("geo-083", "Mediterraneo", 2, "Come chiamavano i Romani il Mediterraneo?",
  "Mare nostrum", ["Mare magnum", "Pontus Euxinus", "Mare internum soltanto"],
  "Voce «Mar Mediterraneo».",
  W("Mar Mediterraneo"), MED, "Gli antichi Romani lo chiamavano, ad esempio, Mare nostrum")

D("geo-084", "Mediterraneo", 3, "Attraverso quali stretti il Mediterraneo comunica con il Mar Nero?",
  "Dardanelli e Bosforo, attraverso il Mar di Marmara", ["Gibilterra e Messina", "Otranto e Bonifacio", "Kerč e Hormuz"],
  "Voce «Mar Mediterraneo».",
  W("Mar Mediterraneo"), MED, "gli stretti dei Dardanelli e del Bosforo è collegato al Mar Nero")

D("geo-085", "Continenti", 2, "Quanti continenti prevede il modello più seguito in Italia?",
  "Sei: Africa, Asia, Europa, America, Oceania, Antartide", ["Cinque, senza l'Antartide", "Sette, con due Americhe", "Quattro"],
  "È anche il criterio del geoschema delle Nazioni Unite.",
  W("Continente"), CON, "Modello più seguito in Italia: sei continenti")

D("geo-086", "Continenti", 3, "Quale continente manca nel modello a cinque continenti dei cerchi olimpici?",
  "L'Antartide", ["L'Oceania", "L'Africa", "L'America"],
  "Si considerano solo i continenti abitati.",
  W("Continente"), CON, "In esso non si include l'Antartide")

D("geo-087", "Continenti", 3, "A quale continente appartiene la Groenlandia, pur essendo politicamente legata alla Danimarca?",
  "All'America", ["All'Europa", "All'Asia", "All'Antartide"],
  "L'appartenenza politica non conta ai fini del continente.",
  W("Continente"), CON, "la Groenlandia è parte integrante del continente americano")

D("geo-088", "Continenti", 2, "Da quale verbo latino deriva la parola «continente»?",
  "Continere, «tenere insieme»", ["Contendere, «lottare»", "Continuare, «proseguire»", "Contemnere, «disprezzare»"],
  "Voce «Continente».",
  W("Continente"), CON, "dal latino continere, \"tenere insieme\"")

D("geo-089", "Continenti", 2, "A quale continente si considera appartenente il Madagascar?",
  "All'Africa", ["All'Asia", "All'Oceania", "All'Europa"],
  "Le isole si attribuiscono generalmente al continente più vicino.",
  W("Continente"), CON, "il Madagascar e le Seychelles si considerano parte dell'Africa")

D("geo-090", "Oceani", 1, "Quale percentuale circa della superficie terrestre è coperta dall'oceano?",
  "Circa il 70%", ["Circa il 30%", "Circa il 50%", "Circa il 90%"],
  "Voce «Oceano».",
  W("Oceano"), OCE, "circa il 70% della superficie totale")

D("geo-091", "Oceani", 2, "Quanti oceani si identificano per consuetudine in Italia?",
  "Tre: Pacifico, Atlantico e Indiano", ["Cinque", "Quattro, con l'Artico", "Sette"],
  "Il Mar Glaciale Artico è considerato un mare dipendente dall'Atlantico.",
  W("Oceano"), OCE, "è dunque consuetudine identificare tre oceani")

D("geo-092", "Oceani", 1, "Qual è l'oceano più esteso?",
  "L'Oceano Pacifico", ["L'Oceano Atlantico", "L'Oceano Indiano", "Il Mar Glaciale Artico"],
  "Circa 179 milioni di km².",
  W("Oceano"), OCE, "Oceano Pacifico, 179000000 km²")

D("geo-093", "Oceani", 3, "Come è considerato il «Mar Glaciale Artico» nella geografia italiana?",
  "Un mare dipendente dall'Oceano Atlantico", ["Un oceano autonomo", "Un lago salato", "Parte del Pacifico"],
  "Nei paesi anglosassoni si parla invece di Oceano Artico.",
  W("Oceano"), OCE, "è considerato nella letteratura geografica italiana un mare dipendente dall'Oceano Atlantico")

D("geo-094", "Cartografia", 2, "Quali sono le coordinate geografiche di un punto?",
  "Latitudine, longitudine e altitudine", ["Solo latitudine e longitudine", "Nord, sud, est, ovest", "Altezza, larghezza e profondità"],
  "Voce «Coordinate geografiche».",
  W("Coordinate geografiche"), COO, "Esse sono la latitudine, la longitudine e l'altitudine")

D("geo-095", "Cartografia", 2, "Cos'è la latitudine?",
  "La distanza angolare di un punto dall'equatore", ["La distanza dal meridiano di Greenwich", "L'altezza sul livello del mare", "La distanza dal polo nord in km"],
  "La longitudine è invece la distanza angolare da un meridiano di riferimento.",
  W("Coordinate geografiche"), COO, "La latitudine è la distanza angolare di un punto dall'equatore")

D("geo-096", "Cartografia", 2, "Quale meridiano è convenzionalmente il riferimento zero della longitudine dal 1884?",
  "Il meridiano di Greenwich", ["Il meridiano di Parigi", "Il meridiano di Roma (Monte Mario)", "Il meridiano di Washington"],
  "Fu deciso alla International Meridian Conference di Washington.",
  W("Coordinate geografiche"), COO, "Dal 1884 il meridiano fondamentale di riferimento è convenzionalmente fissato a Greenwich")

D("geo-097", "Cartografia", 3, "A chi è attribuita l'invenzione di un sistema di coordinate geografiche?",
  "A Eratostene di Cirene", ["A Tolomeo", "A Galileo Galilei", "A Mercatore"],
  "Tolomeo fu il primo ad adottare il sistema di latitudine e longitudine.",
  W("Coordinate geografiche"), COO, "è generalmente attribuita a Eratostene di Cirene")

D("geo-098", "Cartografia", 3, "Le latitudini dell'emisfero sud, in gradi decimali, si indicano con:",
  "Valori negativi", ["Valori superiori a 90", "La lettera E", "Valori sempre positivi"],
  "Anche le longitudini a ovest di Greenwich sono negative.",
  W("Coordinate geografiche"), COO, "avremo valori negativi per latitudini nell'emisfero sud")

D("geo-099", "Fusi orari", 2, "Quanti gradi di longitudine copre idealmente un fuso orario?",
  "15°", ["10°", "30°", "24°"],
  "360° diviso 24 ore.",
  W("Fuso orario"), FUS, "ciascuna delle quali copriva 15° di longitudine")

D("geo-100", "Fusi orari", 2, "Rispetto all'UTC, in quale fuso si trova Roma (ora solare)?",
  "UTC+1", ["UTC", "UTC+2", "UTC-1"],
  "Voce «Fuso orario».",
  W("Fuso orario"), FUS, "Roma: UTC+1")

D("geo-101", "Fusi orari", 3, "Se a Roma (UTC+1) sono le 13:00, che ora è a Los Angeles (UTC-8), in ora solare?",
  "Le 4:00", ["Le 21:00", "Le 5:00", "Le 22:00"],
  "La differenza è di 9 ore: 13 − 9 = 4. Con UTC 12:00 a Los Angeles sono le 04:00.",
  W("Fuso orario"), FUS, "Los Angeles: UTC-8")

D("geo-102", "Fusi orari", 3, "Quanti fusi orari esistono oggi, per ragioni anche politiche?",
  "39", ["24", "12", "48"],
  "In origine erano 24 zone di 15°.",
  W("Fuso orario"), FUS, "si crearono 39 fusi orari, tuttora in uso")

D("geo-103", "Europa", 2, "Quali sono le principali penisole europee?",
  "Italiana, balcanica, iberica e finno-scandinava", ["Arabica, indiana e coreana", "Malese e indocinese", "Kamčatka e Alaska"],
  "Voce «Europa».",
  W("Europa"), EUR, "la penisola italiana, quella balcanica, quella iberica e quella finno-scandinava")

D("geo-104", "Europa", 2, "Qual è il continente più piccolo della Terra?",
  "L'Oceania", ["L'Europa", "L'Antartide", "L'Africa"],
  "L'Europa (circa 10 milioni di km²) è di poco più grande.",
  W("Europa"), EUR, "l'Oceania, il continente più piccolo della Terra")

D("geo-105", "Europa", 3, "Lungo quale catena montuosa corre convenzionalmente il confine tra Europa e Asia?",
  "Gli Urali", ["Le Alpi", "I Carpazi", "L'Himalaya"],
  "Il confine segue poi il fiume Ural e la depressione del Kuma-Manyč o il Caucaso, secondo le convenzioni.",
  W("Europa"), EUR, "lungo gli Urali e attraverso l'istmo ponto-caspico")


# --- Blocco 5: continenti e luoghi notevoli d'Italia ---
AFR = "Wikipedia_Africa.txt"
ASI = "Wikipedia_Asia.txt"
AME = "Wikipedia_America.txt"
OCN = "Wikipedia_Oceania.txt"
ANT = "Wikipedia_Antartide.txt"
ETN = "Wikipedia_Etna.txt"
VES = "Wikipedia_Vesuvio.txt"
STR = "Wikipedia_Stretto-di-Messina.txt"
PP = "Wikipedia_Pianura-Padana.txt"

D("geo-106", "Continenti", 2, "Qual è il continente più vasto e più popolato del mondo?",
  "L'Asia", ["L'Africa", "L'America", "L'Europa"],
  "Ha circa un terzo delle terre emerse e circa 4,8 miliardi di abitanti.",
  W("Asia"), ASI, "È il continente più vasto al mondo")

D("geo-107", "Continenti", 3, "Quale posto occupa l'Africa tra i continenti per superficie e per popolazione?",
  "Terzo per superficie e secondo per popolazione", ["Primo per entrambi", "Secondo per superficie e terzo per popolazione", "Quarto per entrambi"],
  "Voce «Africa».",
  W("Africa"), AFR, "il terzo per superficie e secondo per popolazione")

D("geo-108", "Continenti", 2, "Quale stretto separa l'Africa dall'Europa?",
  "Lo stretto di Gibilterra", ["Lo stretto di Messina", "Il Bosforo", "Lo stretto di Bab el-Mandeb"],
  "Voce «Africa».",
  W("Africa"), AFR, "È separata dall'Europa dallo Stretto di Gibilterra")

D("geo-109", "Continenti", 3, "Quali linee notevoli attraversano l'Africa?",
  "L'Equatore e i tropici del Cancro e del Capricorno", ["Solo il tropico del Cancro", "Il circolo polare artico", "Il meridiano del cambiamento di data"],
  "Gran parte del territorio ricade nella zona torrida.",
  W("Africa"), AFR, "L'Africa è attraversata dall'Equatore e dai tropici del Cancro e del Capricorno")

D("geo-110", "Continenti", 3, "Quali continenti formano il cosiddetto «Continente Antico»?",
  "Europa, Asia e Africa", ["America e Oceania", "Europa e America", "Asia e Oceania"],
  "Voce «Africa».",
  W("Africa"), AFR, "Insieme all'Europa e all'Asia, forma il cosiddetto Continente Antico")

D("geo-111", "Continenti", 3, "Secondo un'ipotesi etimologica fenicia, cosa significherebbe «Asia»?",
  "«Oriente» (le terre dove sorge il Sole)", ["«Occidente»", "«Terra fertile»", "«Grande montagna»"],
  "«Europa» deriverebbe invece da ereb, «occidente».",
  W("Asia"), ASI, "derivante da una voce semitica significante \"oriente\"")

D("geo-112", "Continenti", 2, "Con quale altro nome è chiamata l'America?",
  "Nuovo Mondo (Continente Nuovo)", ["Continente Antico", "Continente Nuovissimo", "Terra Australis"],
  "L'Oceania è detta invece Continente Nuovissimo.",
  W("America"), AME, "chiamata anche Continente Nuovo o Nuovo Mondo")

D("geo-113", "Continenti", 3, "Quali catene montuose dominano il lato occidentale dell'America?",
  "Le Montagne Rocciose e le Ande", ["Gli Appalachi e l'Himalaya", "Gli Urali e il Caucaso", "Le Alpi e i Pirenei"],
  "Voce «America».",
  W("America"), AME, "catene montuose delle Montagne Rocciose e delle Ande")

D("geo-114", "Continenti", 3, "Quali sono i paesi più popolosi dell'America?",
  "Stati Uniti, Brasile e Messico", ["Canada, Argentina e Cile", "Perù, Colombia e Cuba", "Venezuela, Bolivia e Uruguay"],
  "Voce «America».",
  W("America"), AME, "i paesi più popolosi sono gli Stati Uniti d'America, il Brasile e il Messico")

D("geo-115", "Continenti", 3, "Quale istmo separa, secondo la letteratura anglosassone, America del Nord e del Sud?",
  "L'istmo di Panama", ["L'istmo di Suez", "L'istmo di Corinto", "Lo stretto di Bering"],
  "Voce «America».",
  W("America"), AME, "separati dall'istmo di Panama")

D("geo-116", "Continenti", 3, "In quali grandi regioni insulari si suddivide tradizionalmente l'Oceania?",
  "Melanesia, Micronesia e Polinesia", ["Indonesia, Malesia e Filippine", "Antille e Bahamas", "Australia e Antartide"],
  "Voce «Oceania».",
  W("Oceania"), OCN, "Melanesia (inclusa la Nuova Guinea) Micronesia e Polinesia")

D("geo-117", "Continenti", 3, "Perché l'Oceania è detta «Continente Nuovissimo»?",
  "Perché, Antartide a parte, fu l'ultimo a essere scoperto dagli europei e popolato dall'uomo", ["Perché è emerso da poco dal mare", "Perché è il più giovane geologicamente", "Perché è stato colonizzato dopo il 1900"],
  "Voce «Oceania».",
  W("Oceania"), OCN, "fu l'ultimo a essere scoperto dagli europei")

D("geo-118", "Continenti", 2, "Quale percentuale del territorio antartico è coperta dai ghiacci?",
  "Circa il 98%", ["Circa il 50%", "Circa il 75%", "Il 100%"],
  "È il continente più freddo del pianeta.",
  W("Antartide"), ANT, "L'Antartide ha dunque il 98% del territorio coperto dai ghiacci")

D("geo-119", "Continenti", 3, "Cosa stabilisce il Trattato Antartico del 1959?",
  "Che l'Antartide sia usata solo per scopi pacifici e scientifici, senza attività militari né sfruttamento economico", ["La spartizione del continente tra sette Stati", "L'estrazione di minerali da parte dell'ONU", "La costruzione di basi militari NATO"],
  "Voce «Antartide».",
  W("Antartide"), ANT, "esclusivamente per scopi pacifici e scientifici")

D("geo-120", "Continenti", 3, "Quale posto occupa l'Antartide tra i continenti per estensione?",
  "Quarto, dopo Asia, America e Africa", ["Primo", "Ultimo", "Secondo, dopo l'Asia"],
  "Misura circa 14 milioni di km².",
  W("Antartide"), ANT, "è il quarto continente più vasto della Terra dopo Asia, America e Africa")

D("geo-121", "Continenti", 4, "Cosa significa l'aggettivo greco da cui deriva «Antartide»?",
  "«Opposto all'Artico»", ["«Terra dei ghiacci»", "«Sotto le stelle»", "«Fine del mondo»"],
  "Voce «Antartide».",
  W("Antartide"), ANT, "\"opposto all'Artico\"")

D("geo-122", "Vulcani", 2, "Con quale altro nome è noto l'Etna?",
  "Mongibello", ["Stromboli", "Vulture", "Somma"],
  "È il più alto vulcano attivo della placca euroasiatica.",
  W("Etna"), ETN, "L'Etna o Mongibello")

D("geo-123", "Vulcani", 3, "In quale anno l'UNESCO ha inserito l'Etna nel Patrimonio dell'umanità?",
  "Nel 2013", ["Nel 1997", "Nel 2020", "Nel 2005"],
  "Voce «Etna».",
  W("Etna"), ETN, "Il 21 giugno 2013, la XXXVII sessione del Comitato UNESCO ha inserito l'Etna")

D("geo-124", "Vulcani", 3, "Nel territorio di quale città metropolitana si trova l'Etna?",
  "Catania", ["Messina", "Palermo", "Siracusa"],
  "Voce «Etna».",
  W("Etna"), ETN, "entro il territorio della città metropolitana di Catania")

D("geo-125", "Vulcani", 3, "Quale vulcano più antico si è fuso con il Vesuvio, formando la caldera in cui si è sviluppato il cono attuale?",
  "Il Monte Somma", ["I Campi Flegrei", "Il Monte Nuovo", "L'Epomeo"],
  "Voce «Vesuvio».",
  W("Vesuvio"), VES, "la fusione con un vulcano più antico, il Monte Somma")

D("geo-126", "Vulcani", 2, "Su quale golfo domina il Vesuvio?",
  "Il golfo di Napoli", ["Il golfo di Salerno", "Il golfo di Gaeta", "Il golfo di Taranto"],
  "Voce «Vesuvio».",
  W("Vesuvio"), VES, "in posizione dominante rispetto al golfo di Napoli")

D("geo-127", "Vulcani", 3, "Perché il Vesuvio è considerato uno dei vulcani più pericolosi al mondo?",
  "Per l'elevata popolazione delle zone circostanti e le sue caratteristiche esplosive", ["Perché erutta ogni anno", "Perché è il più alto d'Europa", "Perché è sottomarino"],
  "Circa 700.000 residenti sono potenzialmente in pericolo.",
  W("Vesuvio"), VES, "a causa dell'elevata popolazione delle zone circostanti e delle sue caratteristiche esplosive")

D("geo-128", "Mari e stretti", 2, "Quali mari collega lo stretto di Messina?",
  "Il Tirreno a nord e lo Ionio a sud", ["L'Adriatico e lo Ionio", "Il Tirreno e il Ligure", "Lo Ionio e il Mediterraneo orientale soltanto"],
  "Voce «Stretto di Messina».",
  W("Stretto di Messina"), STR, "Collega il mar Tirreno, che si trova a nord, con il mar Ionio")

D("geo-129", "Mari e stretti", 3, "Qual è la larghezza minima dello stretto di Messina?",
  "Circa 3,14 km", ["Circa 30 km", "Circa 800 m", "Circa 12 km"],
  "Tra Villa San Giovanni e Messina.",
  W("Stretto di Messina"), STR, "la larghezza minima è di circa 3,14 km")

D("geo-130", "Mari e stretti", 3, "Con quale nome mitologico era noto anticamente lo stretto di Messina?",
  "Stretto di Scilla e Cariddi", ["Colonne d'Ercole", "Mare di Ulisse", "Stretto delle Sirene"],
  "Voce «Stretto di Messina».",
  W("Stretto di Messina"), STR, "Stretto di Scilla e Cariddi")

D("geo-131", "Pianure", 2, "Qual è la più grande pianura dell'Europa meridionale?",
  "La Pianura Padana", ["Il Tavoliere delle Puglie", "La Maremma", "L'Agro Pontino"],
  "Ha una superficie di circa 47.820 km².",
  W("Pianura Padana"), PP, "è una delle più grandi pianure europee e la più grande dell'Europa meridionale")

D("geo-132", "Pianure", 3, "Di che tipo è la Pianura Padana?",
  "Alluvionale", ["Vulcanica", "Carsica", "Glaciale costiera"],
  "Si è formata dai depositi del Po e dei suoi affluenti.",
  W("Pianura Padana"), PP, "La Pianura Padana è una pianura alluvionale")

D("geo-133", "Pianure", 3, "Da dove deriva l'aggettivo «padano»?",
  "Dal latino Padus, nome del Po", ["Da Padova", "Dal greco «pados», pianura", "Da Parma e Piacenza"],
  "Voce «Pianura Padana».",
  W("Pianura Padana"), PP, "derivante dall'idronimo Padus, cioè il nome del Po")


# --- Blocco 6: Italia fisica e regioni (voci «Geografia dell'Italia» e «Regioni d'Italia») ---
def G(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Geografia dell'Italia"), GI, frase)

def R(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Regioni d'Italia"), REG, frase)

G("geo-134", "Italia fisica", 2, "In quali tre parti si suddivide geograficamente l'Italia?",
  "Continentale, peninsulare e insulare", ["Alpina, padana e appenninica", "Nord, centro e sud soltanto", "Tirrenica, adriatica e ionica"],
  "Il confine tra continentale e peninsulare è la linea La Spezia-Rimini.",
  "l'Italia continentale, tra le Alpi e l'istmo La Spezia-Rimini")

G("geo-135", "Italia fisica", 3, "Quali isole italiane appartengono geograficamente al continente africano?",
  "Lampedusa e Lampione", ["Pantelleria e Linosa", "Malta e Gozo", "Ustica e Favignana"],
  "Fanno parte delle Pelagie.",
  "Lampedusa e Lampione, appartengono geograficamente al continente africano")

G("geo-136", "Italia fisica", 3, "Quale comune italiano costituisce un'exclave in territorio svizzero?",
  "Campione d'Italia", ["Livigno", "Como", "Domodossola"],
  "Si trova nel Canton Ticino.",
  "il comune di Campione d'Italia costituisce una exclave")

G("geo-137", "Italia fisica", 2, "Qual è la zona altimetrica prevalente in Italia?",
  "La collina (circa il 41,6% del territorio)", ["La montagna", "La pianura", "Le zone sotto il livello del mare"],
  "Le montagne sono il 35,2%, le pianure il 23,2%.",
  "L'Italia presenta una prevalenza di zone collinari (il 41,6% del territorio)")

G("geo-138", "Italia fisica", 4, "Dove si trova il punto meno elevato d'Italia, sotto il livello del mare?",
  "Le Contane (Ferrara)", ["Il delta del Po a Rovigo", "Le paludi pontine", "La laguna di Venezia"],
  "Circa −3,44 m.",
  "Punto meno elevato: le Contane (FE)")

G("geo-139", "Italia fisica", 4, "Qual è il comune italiano più lontano dal mare?",
  "Madesimo (SO)", ["Livigno (SO)", "Aosta", "Bormio (SO)"],
  "Dista 294 km dal Mar Ligure.",
  "il comune italiano più lontano dal mare è Madesimo (SO)")

G("geo-140", "Italia fisica", 3, "Con quale Stato l'Italia ha il confine terrestre più lungo?",
  "La Svizzera (744 km)", ["La Francia", "L'Austria", "La Slovenia"],
  "Francia 515 km, Austria 430 km, Slovenia 232 km.",
  "Svizzera 744 km")

G("geo-141", "Italia fisica", 3, "Quanto misura il canale di Sicilia tra la Sicilia e la penisola tunisina?",
  "Circa 140 km", ["Circa 14 km", "Circa 500 km", "Circa 70 km"],
  "Voce «Geografia dell'Italia».",
  "intercorrono solo 140 km: tanti ne misura il canale di Sicilia")

G("geo-142", "Italia fisica", 3, "Quanto dista la penisola salentina dalla costa albanese nel punto più stretto (canale d'Otranto)?",
  "Circa 70 km", ["Circa 7 km", "Circa 200 km", "Circa 140 km"],
  "Voce «Geografia dell'Italia».",
  "nel punto più stretto del canale d'Otranto, 70 km")

G("geo-143", "Italia fisica", 3, "Quale località è il punto più a nord d'Italia?",
  "La Testa Gemella Occidentale, nel massiccio della Vetta d'Italia", ["Il Brennero", "Il Monte Bianco", "Il passo dello Stelvio"],
  "Fino al 1997 si considerava tale la Vetta d'Italia.",
  "a settentrione la Testa Gemella Occidentale")

G("geo-144", "Italia fisica", 3, "Quale punto è l'estremo occidentale d'Italia?",
  "La Rocca Bernauda nelle Alpi Cozie", ["Capo Teulada", "Il Monte Bianco", "Ventimiglia"],
  "Il comune più a ovest è Bardonecchia.",
  "a occidente la Rocca Bernauda nelle Alpi Cozie")

G("geo-145", "Italia fisica", 4, "Quale località rivendica, tra le altre, il titolo di centro geografico d'Italia?",
  "Narni", ["Firenze", "Roma", "Bologna"],
  "Lo rivendicano anche Orvieto, Rieti e Spoleto; secondo l'IGM non è determinabile univocamente.",
  "Narni (TR)")

G("geo-146", "Italia fisica", 3, "Qual è la vetta più alta della Sardegna?",
  "Punta La Marmora, nel Gennargentu", ["Monte Limbara", "Monte Arci", "Punta Corrasi"],
  "Raggiunge 1.834 m.",
  "Punta La Marmora, di 1.834 metri")

G("geo-147", "Italia fisica", 3, "Qual è la seconda pianura italiana per estensione?",
  "Il Tavoliere delle Puglie", ["La Maremma", "Il Campidano", "La Piana di Catania"],
  "È una pianura di sollevamento.",
  "La seconda pianura italiana per estensione è il Tavoliere delle Puglie")

G("geo-148", "Italia fisica", 3, "Di che origine è la Pianura campana?",
  "Vulcanica", ["Alluvionale", "Di sollevamento", "Glaciale"],
  "Le ceneri dei vulcani hanno riempito le valli.",
  "ad esempio la Pianura campana, sono di origine vulcanica")

G("geo-149", "Italia fisica", 3, "Quale percentuale del territorio nazionale è costituita da pianure?",
  "Circa il 23%", ["Circa il 50%", "Circa il 10%", "Circa il 40%"],
  "La Pianura Padana ne costituisce più di due terzi.",
  "Le pianure costituiscono solamente il 23,2% del territorio nazionale")

G("geo-150", "Italia fisica", 3, "Di che origine sono le colline delle Langhe, del Monferrato e del Chianti?",
  "Sedimentaria (sollevamento del fondo marino)", ["Vulcanica", "Morenica", "Carsica"],
  "Le colline della Brianza sono invece moreniche, i Colli Euganei vulcanici.",
  "Le Langhe, il Monferrato, il Chianti e le Murge sono colline sedimentarie")

G("geo-151", "Italia fisica", 3, "Di che origine sono i Colli Euganei?",
  "Vulcanica", ["Morenica", "Sedimentaria", "Alluvionale"],
  "Voce «Geografia dell'Italia».",
  "I Colli Euganei e numerose altre formazioni in Toscana, Lazio, Campania sono di origine vulcanica")

G("geo-152", "Italia fisica", 3, "Quale mare bagna le coste orientali della penisola dal Friuli-Venezia Giulia a Santa Maria di Leuca?",
  "Il mar Adriatico", ["Il mar Ionio", "Il mar Tirreno", "Il mar Ligure"],
  "Voce «Geografia dell'Italia».",
  "Il Mar Adriatico bagna le coste orientali della penisola")

G("geo-153", "Italia fisica", 3, "Quale braccio di mare separa la Sardegna dalla Corsica?",
  "Le Bocche di Bonifacio", ["Il canale di Piombino", "Il canale di Corsica", "Lo stretto di Messina"],
  "Il canale di Piombino separa l'Elba dalla Toscana.",
  "tra la Sardegna e la Corsica le Bocche di Bonifacio")

G("geo-154", "Italia fisica", 2, "Tra quali placche si trova l'Italia, che spiega l'elevata sismicità?",
  "Placca africana e placca eurasiatica", ["Placca pacifica e nordamericana", "Placca indiana e araba", "Placca sudamericana e africana"],
  "Voce «Geografia dell'Italia».",
  "Stretta tra due placche, la placca africana e la placca eurasiatica")

G("geo-155", "Italia fisica", 4, "Come si chiama il grande vulcano sottomarino a nord della Sicilia, tra i più estesi d'Europa?",
  "Marsili", ["Empedocle", "Ferdinandea", "Palinuro"],
  "Voce «Geografia dell'Italia».",
  "gigantesco vulcano sottomarino Marsili")

G("geo-156", "Italia fisica", 3, "Quali laghi del Lazio occupano crateri di vulcani spenti?",
  "Bolsena, Vico e Bracciano", ["Trasimeno e Scanno", "Garda e Iseo", "Lesina e Varano"],
  "Voce «Geografia dell'Italia».",
  "laghi vulcanici (Lago di Bolsena, Lago di Vico, Lago di")

G("geo-157", "Italia fisica", 3, "Quali sono le lagune più importanti dell'Adriatico settentrionale?",
  "Venezia, Grado e Marano", ["Orbetello e Lesina", "Cagliari e Oristano", "Comacchio e Varano"],
  "La laguna di Orbetello è invece sulla costa toscana.",
  "la Laguna di Venezia")

R("geo-158", "Regioni", 3, "Qual è il capoluogo dell'Abruzzo?",
  "L'Aquila", ["Pescara", "Chieti", "Teramo"],
  "Voce «Regioni d'Italia».",
  "Abruzzo L'Aquila")

R("geo-159", "Regioni", 2, "Qual è il capoluogo della Basilicata?",
  "Potenza", ["Matera", "Melfi", "Lagonegro"],
  "Voce «Regioni d'Italia».",
  "Basilicata Potenza")

R("geo-160", "Regioni", 2, "Qual è il capoluogo della Calabria?",
  "Catanzaro", ["Reggio Calabria", "Cosenza", "Crotone"],
  "Voce «Regioni d'Italia».",
  "Calabria Catanzaro")

R("geo-161", "Regioni", 2, "Qual è il capoluogo del Molise?",
  "Campobasso", ["Isernia", "Termoli", "Venafro"],
  "Voce «Regioni d'Italia».",
  "Molise Campobasso")

R("geo-162", "Regioni", 2, "Qual è il capoluogo delle Marche?",
  "Ancona", ["Pesaro", "Macerata", "Ascoli Piceno"],
  "Voce «Regioni d'Italia».",
  "Marche Ancona")

R("geo-163", "Regioni", 3, "Qual è la regione italiana più popolosa?",
  "La Lombardia", ["Il Lazio", "La Campania", "La Sicilia"],
  "Supera i 10 milioni di abitanti (dati al 1° gennaio 2025).",
  "Milano 10 033 918")

R("geo-164", "Regioni", 3, "Qual è la regione meno popolosa d'Italia?",
  "La Valle d'Aosta", ["Il Molise", "La Basilicata", "L'Umbria"],
  "Circa 122 mila abitanti al 1° gennaio 2025.",
  "Valle d'Aosta Aosta 122 532")

R("geo-165", "Regioni", 3, "Quale fu la prima regione autonoma a essere costituita, nel 1947?",
  "La Sicilia", ["La Sardegna", "La Valle d'Aosta", "Il Trentino-Alto Adige"],
  "Seguirono Sardegna, Trentino-Alto Adige e Valle d'Aosta nel 1948.",
  "Le prime regioni a essere costituite furono le regioni autonome Sicilia")

R("geo-166", "Regioni", 3, "In che anno la regione «Abruzzi e Molise» fu divisa in due regioni?",
  "Nel 1963", ["Nel 1948", "Nel 1970", "Nel 2001"],
  "Così le regioni diventarono 20.",
  "Nel 1963 la regione Abruzzi e Molise venne scorporata")

R("geo-167", "Regioni", 3, "Quando si tennero le prime elezioni regionali per le regioni a statuto ordinario?",
  "Nel 1970", ["Nel 1948", "Nel 1963", "Nel 1995"],
  "Voce «Regioni d'Italia».",
  "Le prime elezioni regionali per gli organi delle regioni a statuto ordinario si tennero nel 1970")

R("geo-168", "Regioni", 4, "In quale regione il presidente è eletto dal consiglio regionale e non direttamente?",
  "Valle d'Aosta", ["Lombardia", "Sicilia", "Toscana"],
  "In Trentino-Alto Adige la presidenza ruota tra i presidenti delle due province autonome.",
  "eccettuate la Valle d'Aosta (dove il presidente è eletto dal consiglio regionale)")

R("geo-169", "Regioni", 4, "Quale regione ha il PIL pro capite più alto (dati ISTAT 2022)?",
  "L'Alto Adige (provincia di Bolzano)", ["La Lombardia", "Il Lazio", "L'Emilia-Romagna"],
  "La Lombardia ha invece il PIL totale più alto.",
  "L'Alto Adige capeggia la classifica del PIL pro capite")

R("geo-170", "Regioni", 4, "Quale legge del 1865 disciplinò gli enti locali del Regno d'Italia (province, circondari, mandamenti, comuni)?",
  "La legge Ricasoli (L. 20 marzo 1865, n. 2248)", ["La legge Crispi del 1890", "La legge Tatarella", "La legge Delrio"],
  "Voce «Regioni d'Italia».",
  "La Legge 20 marzo 1865, n. 2248 (\"Legge Ricasoli\")")


# --- Blocco 7: dati ISTAT (Annuario statistico 2025, CC BY) e Unione europea ---
TER = "ISTAT_Annuario2025_cap1_Territorio.txt"
IST = "ISTAT, Annuario statistico italiano 2025 (CC BY 4.0)"

D("geo-171", "Popolazione", 3, "Quanti Comuni c'erano in Italia al 31 dicembre 2024 secondo l'ISTAT?",
  "7.896", ["8.101", "6.500", "9.200"],
  "Erano 8.101 nel 2001: le fusioni ne hanno ridotto il numero.",
  IST, TER, "sono presenti 7.896 Comuni al 31 dicembre 2024")

D("geo-172", "Popolazione", 3, "Che quota dei Comuni italiani ha meno di 5 mila abitanti (fine 2024)?",
  "Circa il 70% (69,9%)", ["Circa il 20%", "Circa il 50%", "Circa il 90%"],
  "Annuario statistico italiano 2025.",
  IST, TER, "il 69,9 per cento del totale ha meno di 5 mila abitanti")

D("geo-173", "Popolazione", 4, "Quanti Comuni italiani superano i 250 mila abitanti (fine 2024)?",
  "Undici", ["Cinque", "Ventuno", "Trentacinque"],
  "Ospitano il 14,7% dei residenti.",
  IST, TER, "A contare oltre 250 mila abitanti sono solo undici Comuni")

D("geo-174", "Popolazione", 3, "Quali regioni hanno più Comuni?",
  "Lombardia e Piemonte", ["Sicilia e Sardegna", "Lazio e Campania", "Veneto ed Emilia-Romagna"],
  "Rispettivamente 1.502 e 1.180 Comuni.",
  IST, TER, "Le regioni con il maggior numero di Comuni sono la Lombardia e il Piemonte")

D("geo-175", "Popolazione", 3, "Quali regioni hanno meno Comuni?",
  "Valle d'Aosta e Umbria", ["Molise e Basilicata", "Liguria e Marche", "Friuli-Venezia Giulia e Trentino-Alto Adige"],
  "74 e 92 Comuni.",
  IST, TER, "le regioni con meno Comuni sono la Valle d'Aosta (74) e l'Umbria (92)")

D("geo-176", "Popolazione", 3, "Dove vive quasi la metà della popolazione italiana (2024)?",
  "Nelle aree di pianura", ["In montagna", "In collina", "Sulle isole minori"],
  "Il 38,6% vive in collina e il 12,1% in montagna.",
  IST, TER, "Nel 2024 quasi la metà della popolazione vive nelle aree di pianura")

D("geo-177", "Popolazione", 4, "Quale ecoregione italiana è la più popolata?",
  "Quella padana", ["Quella tirrenica meridionale", "Quella alpina", "Quella adriatica"],
  "Oltre 19 milioni di abitanti.",
  IST, TER, "la sezione con la popolazione più numerosa è quella padana")

D("geo-178", "Popolazione", 4, "Quanti sistemi locali del lavoro individua l'ISTAT in Italia?",
  "515", ["107", "20", "7.896"],
  "Annuario statistico italiano 2025.",
  IST, TER, "Nel nostro Paese sono presenti 515 sistemi locali del lavoro")

D("geo-179", "Popolazione", 4, "Quante sono le Unità territoriali sovracomunali (province, città metropolitane e simili)?",
  "107", ["20", "110", "80"],
  "Annuario statistico italiano 2025.",
  IST, TER, "dalle 107 Unità territoriali sovracomunali e dalle 20 regioni italiane")

D("geo-180", "Popolazione", 3, "Quale quota della popolazione italiana risiede nelle Aree interne?",
  "Circa il 22,7%", ["Circa il 5%", "Circa il 50%", "Circa il 70%"],
  "Le Aree interne occupano la maggior parte della superficie di Isole e Sud.",
  IST, TER, "Nelle Aree interne risiede il 22,7 per cento della popolazione")

D("geo-181", "Popolazione", 3, "Qual era la quota di stranieri residenti in Italia al 1° gennaio 2025 (stime ISTAT)?",
  "Il 9,2% della popolazione", ["Il 2%", "Il 20%", "Il 15%"],
  "Circa 5,4 milioni di persone.",
  IST, POP, "rappresenta il 9,2 per cento della popolazione totale")

D("geo-182", "Popolazione", 3, "Quale fu il numero medio di figli per donna nel 2024 (stima ISTAT)?",
  "1,18", ["2,1", "1,5", "0,9"],
  "È inferiore anche al precedente minimo storico del 1995 (1,19).",
  IST, POP, "Il numero medio di figli per donna è pari, nel 2024, a 1,18")

D("geo-183", "Popolazione", 3, "Quale era l'età media della popolazione italiana al 1° gennaio 2025 (stima)?",
  "46,8 anni", ["38 anni", "52 anni", "41,2 anni"],
  "In aumento di circa tre mesi rispetto all'anno precedente.",
  IST, POP, "l'età media della popolazione, stimata pari a 46,8 anni")

D("geo-184", "Popolazione", 3, "Quale quota della popolazione aveva 65 anni e più al 1° gennaio 2025?",
  "Il 24,7%", ["Il 10%", "Il 35%", "Il 50%"],
  "Continua l'invecchiamento della popolazione.",
  IST, POP, "La popolazione di 65 anni e più rappresenta il 24,7 per cento")

D("geo-185", "Popolazione", 3, "Quale era la speranza di vita alla nascita delle donne nel 2024 (stima ISTAT)?",
  "85,5 anni", ["79 anni", "90 anni", "81,4 anni"],
  "Per gli uomini era 81,4 anni.",
  IST, POP, "81,4 anni per gli uomini e in 85,5 anni per le donne")

D("geo-186", "Popolazione", 4, "Come fu il saldo naturale (nati meno morti) in Italia nel 2024?",
  "Negativo, circa −281 mila", ["Positivo, circa +100 mila", "Nullo", "Positivo, circa +243 mila"],
  "Il saldo migratorio positivo (+243 mila) lo compensa quasi del tutto.",
  IST, POP, "un saldo naturale negativo (-280.665 unità")

D("geo-187", "Popolazione", 4, "Da quando la popolazione residente in Italia diminuisce senza interruzioni?",
  "Dal 2014", ["Dal 1990", "Dal 2020", "Dal 2001"],
  "Annuario statistico italiano 2025.",
  IST, POP, "in atto senza interruzioni dal 2014")

D("geo-188", "Popolazione", 4, "Qual è l'unica ripartizione territoriale con popolazione in crescita nel 2024?",
  "Il Nord", ["Il Centro", "Il Sud", "Le Isole"],
  "Nel Mezzogiorno il calo è più intenso.",
  IST, POP, "è l'unica ripartizione a registrare una variazione positiva")

D("geo-189", "Unione europea", 2, "Qual è il motto dell'Unione europea?",
  "«Unita nella diversità»", ["«Libertà, uguaglianza, fraternità»", "«E pluribus unum»", "«Dio salvi l'Europa»"],
  "Voce «Unione europea».",
  W("Unione europea"), UE, "Unita nella diversità")

D("geo-190", "Unione europea", 2, "Qual è l'inno dell'Unione europea?",
  "L'Inno alla gioia di Beethoven", ["La Marsigliese", "Il Canto degli Italiani", "Va' pensiero di Verdi"],
  "Voce «Unione europea».",
  W("Unione europea"), UE, "Inno alla gioia")

D("geo-191", "Unione europea", 2, "Cosa raffigura la bandiera europea?",
  "Un cerchio di dodici stelle dorate in campo blu", ["Ventisette stelle gialle", "Una croce bianca su fondo rosso", "Un cerchio di stelle blu su fondo bianco"],
  "Il dodici simboleggia la completezza; non corrisponde al numero degli Stati.",
  W("Unione europea"), UE, "un cerchio di dodici stelle dorate in campo blu")

D("geo-192", "Unione europea", 2, "Quale giorno si celebra la Festa dell'Europa?",
  "Il 9 maggio", ["Il 25 marzo", "Il 1° gennaio", "Il 2 giugno"],
  "Ricorda la dichiarazione Schuman del 1950.",
  W("Unione europea"), UE, "Festa dell'Unione 9 maggio")

D("geo-193", "Unione europea", 3, "In quale città ha sede principale il Parlamento europeo?",
  "Strasburgo", ["Bruxelles", "Lussemburgo", "Francoforte"],
  "Bruxelles ospita la Commissione, Lussemburgo la Corte di giustizia.",
  W("Unione europea"), UE, "Strasburgo: Storia Parlamento europeo")

D("geo-194", "Unione europea", 3, "Quale Stato è uscito dall'Unione europea, dopo esserne stato membro dal 1973 al 2020?",
  "Il Regno Unito", ["La Norvegia", "La Svizzera", "La Groenlandia"],
  "Voce «Unione europea».",
  W("Unione europea"), UE, "Regno Unito (1973-2020)")

D("geo-195", "Unione europea", 3, "In che anno l'Unione europea ha ricevuto il premio Nobel per la pace?",
  "Nel 2012", ["Nel 1957", "Nel 1992", "Nel 2002"],
  "Per il contributo a pace, riconciliazione, democrazia e diritti umani.",
  W("Unione europea"), UE, "Il 12 ottobre 2012 è stata insignita del premio Nobel per la pace")

D("geo-196", "Unione europea", 3, "Con quale trattato del 25 marzo 1957 nacque la Comunità economica europea?",
  "Il trattato di Roma", ["Il trattato di Parigi", "Il trattato di Maastricht", "Il trattato di Lisbona"],
  "Voce «Unione europea».",
  W("Unione europea"), UE, "Nata come Comunità economica europea con il trattato di Roma del 25 marzo 1957")

D("geo-197", "Unione europea", 3, "Quale accordo ha creato uno spazio «senza frontiere interne» tra molti Stati europei?",
  "L'accordo di Schengen", ["Il trattato di Nizza", "L'Atto unico europeo", "Il Patto di stabilità"],
  "Voce «Unione europea».",
  W("Unione europea"), UE, "grazie all'accordo di Schengen")

D("geo-198", "Unione europea", 3, "Quale istituzione governa la politica monetaria dell'eurozona?",
  "La Banca centrale europea (BCE)", ["La Commissione europea", "Il Consiglio europeo", "La Banca europea per gli investimenti"],
  "Voce «Unione europea».",
  W("Unione europea"), UE, "con una politica monetaria comune governata dalla Banca centrale europea (BCE)")

D("geo-199", "Unione europea", 3, "Qual è la popolazione approssimativa dell'Unione europea?",
  "Circa 450 milioni di abitanti", ["Circa 150 milioni", "Circa 800 milioni", "Circa 1 miliardo"],
  "Voce «Unione europea».",
  W("Unione europea"), UE, "La sua popolazione ammonta a circa 450 milioni di abitanti")

D("geo-200", "Unione europea", 4, "Quali Stati aderirono all'UE nel 1995?",
  "Austria, Finlandia e Svezia", ["Spagna e Portogallo", "Polonia e Ungheria", "Croazia e Slovenia"],
  "La Norvegia rifiutò di nuovo l'adesione.",
  W("Unione europea"), UE, "Nel 1995, Austria, Finlandia e Svezia hanno aderito all'UE")

D("geo-201", "Unione europea", 4, "In quale anno è stato introdotto l'euro come moneta circolante?",
  "Nel 2002", ["Nel 1999", "Nel 1992", "Nel 2007"],
  "Sostituì dodici valute nazionali.",
  W("Unione europea"), UE, "L'euro è stato introdotto nel 2002")

# --- Ampliamento a 300: Unione europea, regioni, ambiente ISTAT, continenti, Italia fisica ---
def U(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Unione europea"), UE, frase)

AMB = "ISTAT_Annuario2025_cap2_Ambiente-clima-energia.txt"
def A(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, IST, AMB, frase)

U("geo-202", "Unione europea", 2, "Quali sei Stati fondarono la Comunità economica europea con i Trattati di Roma del 1957?",
  "Belgio, Francia, Germania occidentale, Italia, Lussemburgo e Paesi Bassi", ["Francia, Germania, Italia, Spagna, Regno Unito e Belgio", "Italia, Francia, Austria, Svizzera, Belgio e Olanda", "Germania, Francia, Danimarca, Irlanda, Italia e Belgio"],
  "Gli stessi sei Stati avevano già creato la CECA nel 1951.", "firmato da Belgio, Francia, Italia, Lussemburgo, Paesi Bassi e Germania occidentale")
U("geo-203", "Unione europea", 3, "Quale comunità europea fu istituita insieme alla CEE con i Trattati di Roma?",
  "L'Euratom (Comunità europea dell'energia atomica)", ["La CECA", "Il Consiglio d'Europa", "L'EFTA"],
  "Entrambi i trattati sono entrati in vigore nel 1958.", "Comunità europea dell'energia atomica (Euratom)")
U("geo-204", "Unione europea", 3, "In che anno sei nazioni crearono la Comunità europea del carbone e dell'acciaio (CECA)?",
  "Nel 1951", ["Nel 1957", "Nel 1946", "Nel 1965"],
  "Era considerata «un primo passo nella federazione dell'Europa».", "nel 1951, deluse dalla mancanza di progressi in seno al Consiglio d'Europa, sei nazioni")
U("geo-205", "Unione europea", 2, "Quale documento sull'unità europea fu redatto nel 1941 da Altiero Spinelli, Ernesto Rossi ed Eugenio Colorni?",
  "Il Manifesto di Ventotene", ["La Dichiarazione Schuman", "Il Trattato di Parigi", "Il Manifesto di Bruxelles"],
  "Fu scritto al confino sull'isola di Ventotene e pubblicato nel 1944.", "Manifesto di Ventotene")
U("geo-206", "Unione europea", 3, "Quale statista italiano è tra i padri fondatori dell'Unione europea?",
  "Alcide De Gasperi", ["Giovanni Giolitti", "Aldo Moro", "Enrico Mattei"],
  "Con lui sono ricordati Jean Monnet e Robert Schuman (Francia) e Paul-Henri Spaak (Belgio).", "Alcide De Gasperi dall'Italia")
U("geo-207", "Unione europea", 3, "Quali Stati entrarono nelle Comunità europee nel 1973?",
  "Danimarca, Irlanda e Regno Unito", ["Spagna, Portogallo e Grecia", "Austria, Finlandia e Svezia", "Norvegia, Islanda e Svizzera"],
  "La Norvegia negoziò l'ingresso ma gli elettori lo respinsero con un referendum.", "Nel 1973, le Comunità furono ampliate per includere la Danimarca")
U("geo-208", "Unione europea", 4, "Quale territorio lasciò le Comunità europee nel 1985 dopo un referendum, per una disputa sui diritti di pesca?",
  "La Groenlandia", ["Le Isole Far Oer", "L'Islanda", "La Norvegia"],
  "La Groenlandia è una provincia autonoma della Danimarca.", "compresa la Groenlandia che, nel 1985, lasciò le Comunità")
U("geo-209", "Unione europea", 3, "In che anno si tennero le prime elezioni dirette del Parlamento europeo a suffragio universale?",
  "Nel 1979", ["Nel 1957", "Nel 1993", "Nel 1969"],
  "Prima i membri erano designati dai parlamenti nazionali.", "Nel 1979 furono proclamate le prime elezioni dirette democratiche del parlamento europeo")
U("geo-210", "Unione europea", 3, "Quando entrarono nella Comunità europea Spagna e Portogallo?",
  "Nel 1986", ["Nel 1981", "Nel 1995", "Nel 1973"],
  "La Grecia era entrata nel 1981.", "Nel 1981 si unì alla Comunità europea anche la Grecia e, nel 1986, Spagna e Portogallo")
U("geo-211", "Unione europea", 3, "Quando entrò in vigore il Trattato di Maastricht, che istituì formalmente l'Unione europea?",
  "Il 1° novembre 1993", ["Il 25 marzo 1957", "Il 1° dicembre 2009", "Il 1° gennaio 2002"],
  "I suoi principali artefici furono Helmut Kohl e François Mitterrand.", "entrò in vigore il 1o novembre 1993")
U("geo-212", "Unione europea", 4, "Come si chiamano i criteri che un Paese deve soddisfare per aderire all'UE, concordati nel 1993?",
  "Criteri di Copenaghen", ["Criteri di Maastricht", "Parametri di Schengen", "Criteri di Lisbona"],
  "Richiedono democrazia stabile, economia di mercato funzionante e accettazione degli obblighi di adesione.", "criteri di Copenaghen")
U("geo-213", "Unione europea", 3, "Quale fu il più grande allargamento dell'UE, con l'ingresso di dieci Paesi tra cui Polonia e Ungheria?",
  "Quello del 2004", ["Quello del 1995", "Quello del 2007", "Quello del 2013"],
  "Entrarono Cipro, Estonia, Lettonia, Lituania, Malta, Polonia, Repubblica Ceca, Slovacchia, Slovenia e Ungheria.", "Nel 2004 l'UE ha visto il suo più grande allargamento")
U("geo-214", "Unione europea", 4, "Quali Paesi bocciarono con referendum la Costituzione europea nel 2005?",
  "Francia e Paesi Bassi", ["Irlanda e Danimarca", "Regno Unito e Svezia", "Italia e Spagna"],
  "Il trattato costituzionale non entrò in vigore; molte novità furono riprese dal Trattato di Lisbona.", "anche il risultato del referendum tenuto nei Paesi Bassi fu contrario")
U("geo-215", "Unione europea", 4, "Quando entrò in vigore il Trattato di Lisbona?",
  "Il 1° dicembre 2009", ["Il 13 dicembre 2007", "Il 1° novembre 1993", "Il 1° gennaio 2002"],
  "Fu firmato il 13 dicembre 2007; l'Irlanda lo approvò con un secondo referendum nel 2009.", "entrato in vigore il 1o dicembre 2009")
U("geo-216", "Unione europea", 3, "Quale articolo del Trattato di Lisbona disciplina il recesso di uno Stato dall'Unione?",
  "L'articolo 50", ["L'articolo 7", "L'articolo 1", "L'articolo 352"],
  "È stato invocato solo dal Regno Unito (Brexit).", "conosciute come articolo 50")
U("geo-217", "Unione europea", 3, "Quale Stato è entrato nell'UE nel 2013, portandola a 28 membri?",
  "La Croazia", ["La Slovenia", "La Romania", "La Serbia"],
  "La Croazia ha poi adottato l'euro nel 2023.", "Nel 2013 continuò l'allargamento con l'adesione della Croazia")
U("geo-218", "Unione europea", 2, "In che anno Romania e Bulgaria sono entrate nell'Unione europea?",
  "Nel 2007", ["Nel 2004", "Nel 2013", "Nel 1995"],
  "Nello stesso anno la Slovenia adottò l'euro.", "Il 2007 è anche l'anno dell'adesione di Romania e Bulgaria")
U("geo-219", "Unione europea", 4, "Dove si trovano le zone più basse dell'Unione europea, a 7 metri sotto il livello del mare?",
  "Nel Lammefjorden (Danimarca) e nello Zuidplaspolder (Paesi Bassi)", ["Nel delta del Po", "Nella laguna di Venezia", "Nella Camargue, in Francia"],
  "Il punto più alto dell'Unione è il Monte Bianco.", "le zone più basse sono il Lammefjorden in Danimarca e lo Zuidplaspolder nei Paesi Bassi")
U("geo-220", "Unione europea", 4, "Come sono classificati territori come le Canarie, le Azzorre e la Guyana francese, che fanno parte dell'UE pur essendo fuori dall'Europa?",
  "Regioni ultraperiferiche", ["Paesi e territori d'oltremare", "Protettorati europei", "Territori associati"],
  "Groenlandia e Nuova Caledonia sono invece paesi e territori d'oltremare, non parte dell'UE.", "tali territori vengono classificati come regioni ultraperiferiche")
U("geo-221", "Unione europea", 4, "Quale isola dell'UE è la più grande per superficie?",
  "L'Irlanda", ["La Sicilia", "La Sardegna", "Cipro"],
  "Seguono Sicilia e Sardegna.", "1 Irlanda Irlanda Europa 70 273")

R("geo-222", "Regioni", 2, "Qual è il capoluogo della regione Friuli-Venezia Giulia?",
  "Trieste", ["Udine", "Gorizia", "Pordenone"],
  "Il Friuli-Venezia Giulia è una regione a statuto speciale dal 1963.", "Friuli-Venezia 6 Trieste")
R("geo-223", "Regioni", 1, "Qual è il capoluogo della Puglia?",
  "Bari", ["Lecce", "Foggia", "Taranto"],
  "La Puglia comprende anche la provincia di Barletta-Andria-Trani.", "Puglia Bari 3 877 395")
R("geo-224", "Regioni", 1, "Qual è il capoluogo dell'Umbria?",
  "Perugia", ["Terni", "Assisi", "Spoleto"],
  "L'Umbria ha solo due province: Perugia e Terni.", "Umbria Perugia 851 473")
R("geo-225", "Regioni", 1, "Qual è il capoluogo della Liguria?",
  "Genova", ["La Spezia", "Savona", "Imperia"],
  "Le province liguri sono Genova, Imperia, La Spezia e Savona.", "Liguria Genova 1 510 143")
R("geo-226", "Regioni", 3, "Qual è la regione italiana più estesa per superficie?",
  "La Sicilia", ["Il Piemonte", "La Sardegna", "La Lombardia"],
  "La Sicilia (circa 25.800 km²) supera di poco il Piemonte (circa 25.400 km²).", "Sicilia Palermo 4 787 390 25 824,33")
R("geo-227", "Regioni", 2, "Qual è la regione italiana più piccola per superficie?",
  "La Valle d'Aosta", ["Il Molise", "La Liguria", "L'Umbria"],
  "Ha circa 3.260 km² ed è anche la meno popolosa.", "Valle d'Aosta Aosta 122 532 3 258,61")
R("geo-228", "Regioni", 4, "Come è attribuita la presidenza della regione Trentino-Alto Adige?",
  "A rotazione tra i presidenti delle Province autonome di Trento e di Bolzano", ["Per elezione diretta dei cittadini", "Per nomina del Governo", "Al sindaco di Trento"],
  "Nelle altre regioni il presidente è eletto insieme al consiglio, tranne in Valle d'Aosta.", "è ricoperta a rotazione dal Presidente della Provincia di Trento e dal Presidente della Provincia di Bolzano")
R("geo-229", "Regioni", 4, "Quale legge disciplina dal 1995 le elezioni regionali, salvo le leggi elettorali proprie delle regioni?",
  "La legge Tatarella", ["La legge Ricasoli", "La legge Bassanini", "La legge Delrio"],
  "Le riforme costituzionali del 1999 e del 2001 consentono alle regioni di darsi una propria legge elettorale.", "dal 1995 normate dalla legge Tatarella")
R("geo-230", "Regioni", 4, "Chi raggruppò nel 1870 le province in «compartimenti» a fini statistici, precursori delle regioni?",
  "Pietro Maestri", ["Camillo Cavour", "Bettino Ricasoli", "Francesco Crispi"],
  "Il termine «regione» comparve al posto di «compartimento» nell'Annuario statistico del 1912.", "furono stilati nel 1870 da Pietro Maestri a fini statistici e didattici")
R("geo-231", "Regioni", 3, "Ogni quanti anni si tengono di norma le elezioni regionali?",
  "Ogni cinque anni", ["Ogni quattro anni", "Ogni sei anni", "Ogni tre anni"],
  "Rinnovano il consiglio regionale e il presidente della giunta.", "che di norma si tengono ogni cinque anni")

A("geo-232", "Ambiente", 3, "Quale quota della produzione lorda di energia elettrica italiana veniva da fonti rinnovabili nel 2023 (ISTAT)?",
  "Il 44 per cento", ["Il 20 per cento", "Il 70 per cento", "Il 10 per cento"],
  "Era il 35,4 per cento nel 2022, anno di forte calo dell'idroelettrico.", "dal 35,4 al 44 per cento della produzione lorda totale")
A("geo-233", "Ambiente", 3, "Quale fonte rinnovabile ha dato il contributo maggiore alla produzione elettrica italiana nel 2023?",
  "L'idroelettrica", ["L'eolica", "La geotermica", "Le bioenergie"],
  "Idroelettrico 15,3%, fotovoltaico 11,6%, eolico 8,9%, bioenergie 6,1%, geotermico 2,2%.", "L'apporto maggiore viene garantito dalla fonte idroelettrica")
A("geo-234", "Ambiente", 3, "In quale regione italiana si produce energia geotermica?",
  "Solo in Toscana", ["In Sicilia e Campania", "In tutte le regioni vulcaniche", "Solo in Trentino-Alto Adige"],
  "L'idroelettrico prevale nelle regioni montuose, l'eolico nel Mezzogiorno, il fotovoltaico al Centro.", "l'energia geotermica viene prodotta solo in Toscana")
A("geo-235", "Ambiente", 4, "Quale regione aveva nel 2023 la quota più alta di energia elettrica da fonti rinnovabili?",
  "La Valle d'Aosta (98,4%)", ["La Lombardia", "L'Emilia-Romagna", "La Liguria"],
  "Seguono Basilicata, Trentino-Alto Adige e Marche; ultime Emilia-Romagna e Liguria.", "la Valle d'Aosta (98,4 per cento)")
A("geo-236", "Ambiente", 4, "Qual era la dipendenza energetica dell'Italia dall'estero nel 2023?",
  "Il 74,8 per cento", ["Il 30 per cento", "Il 50 per cento", "Il 95 per cento"],
  "La media dell'UE era il 58,3 per cento.", "la dipendenza energetica dall'estero è infatti del 74,8 per cento")
A("geo-237", "Ambiente", 3, "Qual era la percentuale di raccolta differenziata dei rifiuti urbani in Italia nel 2023?",
  "Il 66,6 per cento", ["Il 45 per cento", "Il 30 per cento", "L'85 per cento"],
  "Supera il target UE del 65 per cento.", "La raccolta differenziata è al 66,6 per cento")
A("geo-238", "Ambiente", 4, "Quanti rifiuti urbani pro capite sono stati prodotti in Italia nel 2023?",
  "Circa 496 kg per abitante", ["Circa 200 kg", "Circa 900 kg", "Circa 1.500 kg"],
  "In tutto 29,3 milioni di tonnellate.", "496,2 kg per abitante")
A("geo-239", "Ambiente", 3, "Quale quota del territorio terrestre italiano era coperta da aree tutelate nel 2023?",
  "Il 21,7 per cento", ["Il 5 per cento", "Il 40 per cento", "Il 60 per cento"],
  "Le aree marine tutelate erano l'11,6 per cento.", "le aree tutelate terrestri coprono il 21,7 per cento del territorio")
A("geo-240", "Ambiente", 4, "Qual è stata la temperatura media annua nei capoluoghi di regione nel 2023, tra gli anni più caldi dal 1971?",
  "16,6 °C", ["12,1 °C", "20,4 °C", "14,0 °C"],
  "È di 1,7 °C sopra il valore climatico 1981-2010.", "con una temperatura media annua di 16,6°C")
A("geo-241", "Ambiente", 3, "Quale quota delle famiglie aveva un impianto di condizionamento nel 2024?",
  "Il 56 per cento", ["Il 15 per cento", "L'85 per cento", "Il 30 per cento"],
  "Era il 29,4 per cento nel 2013: la presenza è quasi raddoppiata.", "dal 29,4 per cento nel 2013 al 56 per cento nel 2024")
A("geo-242", "Ambiente", 3, "Qual è stata nel 2024 la preoccupazione ambientale più sentita dagli italiani?",
  "I cambiamenti climatici", ["Il rumore", "L'inquinamento elettromagnetico", "La perdita di biodiversità"],
  "Indicata dal 58,1 per cento.", "i cambiamenti climatici sono la preoccupazione ambientale più sentita")
A("geo-243", "Ambiente", 4, "Quanti terremoti di magnitudo pari o superiore a 4,0 si sono registrati in Italia nel 2024?",
  "15", ["150", "2", "45"],
  "Erano 10 nel 2023.", "Sono stati 15 i terremoti di magnitudo superiore o uguale a 4,0")

D("geo-244", "Europa", 3, "Secondo il mito greco, in quale animale si trasformò Zeus per rapire la principessa Europa?",
  "In un toro bianco", ["In un'aquila", "In un cigno", "In un cavallo alato"],
  "La condusse fino a Creta; il loro figlio Minosse ne divenne re.", W("Europa"), EUR, "si trasformò in uno splendido toro bianco")
D("geo-245", "Europa", 3, "Quale istmo separa la parte continentale da quella peninsulare dell'Europa?",
  "L'istmo ponto-baltico, da Odessa a Danzica", ["L'istmo di Corinto", "L'istmo di Suez", "L'istmo di Panama"],
  "È una linea di circa 1200 km tra Mar Nero e Baltico.", W("Europa"), EUR, "separate dall'istmo ponto-baltico")
D("geo-246", "Europa", 3, "Quale corrente oceanica rende il clima europeo più mite di altre aree alla stessa latitudine?",
  "La corrente del Golfo", ["La corrente di Humboldt", "La corrente del Labrador", "La corrente delle Canarie"],
  "È soprannominata «il riscaldamento centralizzato d'Europa».", W("Europa"), EUR, "a causa dell'influenza della corrente del Golfo")
D("geo-247", "Europa", 3, "Quali isole europee rientrano tra le venti più grandi della Terra?",
  "Gran Bretagna, Islanda e Irlanda", ["Sicilia, Sardegna e Corsica", "Creta, Cipro e Malta", "Islanda, Sicilia e Creta"],
  "Sono rispettivamente la nona, la diciottesima e la ventesima.", W("Europa"), EUR, "la Gran Bretagna, l'Islanda e l'Irlanda")
D("geo-248", "Europa", 3, "In Europa, il clima diventa più freddo anche spostandosi:",
  "da ovest verso est, per la crescente distanza dal mare", ["da est verso ovest", "da nord verso sud", "solo in altitudine"],
  "L'influenza oceanica si riduce verso l'interno del continente.", W("Europa"), EUR, "diventa più fredda anche andando da ovest verso est")
D("geo-249", "Europa", 4, "Quali mari e stretti segnano il confine meridionale tra Europa e Asia?",
  "Mar Nero, Bosforo, Mar di Marmara e Dardanelli", ["Mar Caspio e Mar d'Aral", "Mar Rosso e canale di Suez", "Mar Egeo e Mar Ionio"],
  "Sono universalmente riconosciuti come confine.", W("Europa"), EUR, "Il mar Nero, lo stretto del Bosforo, il Mar di Marmara e lo stretto dei Dardanelli")
D("geo-250", "Europa", 4, "Secondo la convenzione del confine sullo spartiacque del Caucaso, qual è la vetta più alta d'Europa?",
  "Il Monte Elbrus", ["Il Monte Bianco", "Il Monte Rosa", "Il Cervino"],
  "Con la convenzione di von Strahlenberg la vetta più alta è invece il Monte Bianco.", W("Europa"), EUR, "la vetta massima si identifica con il Monte Elbrus")
D("geo-251", "Europa", 3, "Quale caratteristica rende l'Europa unica tra i continenti per il popolamento?",
  "L'assenza di zone inabitabili come deserti o calotte glaciali", ["La presenza dei fiumi più lunghi", "Il clima tropicale", "L'assenza di montagne"],
  "Per questo è il secondo continente per densità di popolazione.", W("Europa"), EUR, "l'assenza di zone inabitabili come deserti o calotte glaciali")
D("geo-252", "Europa", 4, "Quali catene montuose si trovano tra Norvegia e Svezia, solcate a nord da profondi fiordi?",
  "Le Alpi Scandinave", ["I Carpazi", "I Monti Grampiani", "I Sudeti"],
  "Arrivano a 2452 m.", W("Europa"), EUR, "delle Alpi Scandinave, tra Norvegia e Svezia")
D("geo-253", "Europa", 4, "Quale grande pianura dell'Europa orientale si estende verso est dal Bassopiano germanico?",
  "Il Bassopiano sarmatico", ["La Puszta", "Il Tavoliere", "La pianura di Aquitania"],
  "Nella grande pianura ungherese si estende invece la Puszta.", W("Europa"), EUR, "il vastissimo Bassopiano sarmatico")

D("geo-254", "Continenti", 2, "Qual è il deserto più vasto del mondo, che si estende nel nord dell'Africa?",
  "Il Sahara", ["Il Kalahari", "Il Gobi", "Il Namib"],
  "Misura circa 9 milioni di km²; a sud sfuma nel Sahel.", W("Africa"), AFR, "si estende il Sahara, il più vasto deserto del mondo")
D("geo-255", "Continenti", 2, "Qual è la montagna più alta dell'Africa?",
  "Il Kilimangiaro, in Tanzania", ["Il Monte Kenya", "Il Ruwenzori", "L'Atlante"],
  "È un vulcano spento con ghiacci perenni in cima.", W("Africa"), AFR, "Il punto più alto: Kilimangiaro, Tanzania")
D("geo-256", "Continenti", 3, "Qual è lo Stato più grande dell'Africa per superficie?",
  "L'Algeria", ["L'Egitto", "La Nigeria", "Il Sudan"],
  "Il più piccolo sono le Seychelles; sulla terraferma il Gambia.", W("Africa"), AFR, "Lo Stato più grande del continente è l'Algeria")
D("geo-257", "Continenti", 3, "Qual è l'unica grande isola dell'Africa, la quarta del mondo per estensione?",
  "Il Madagascar", ["Zanzibar", "Sant'Elena", "Le Canarie"],
  "Gli altri arcipelaghi africani sono formati da isole piccole.", W("Africa"), AFR, "L'unica isola di grandi dimensioni è il Madagascar")
D("geo-258", "Continenti", 3, "Lungo quale fiume africano si trovano le celebri Cascate Vittoria?",
  "Lo Zambesi", ["Il Nilo", "Il Congo", "Il Niger"],
  "Lo Zambesi sfocia nell'Oceano Indiano.", W("Africa"), AFR, "Lo Zambesi è celebre anche per le Cascate Vittoria")
D("geo-259", "Continenti", 4, "Dove si trova il punto più basso dell'Africa?",
  "Nel lago Assal, a Gibuti", ["Nel Mar Morto", "Nella depressione di Qattara", "Nel lago Vittoria"],
  "Si trova a circa 155 m sotto il livello del mare.", W("Africa"), AFR, "Il punto più basso: Lago Assal, Gibuti")
D("geo-260", "Continenti", 4, "Qual è il punto più meridionale dell'Africa?",
  "Capo Agulhas, in Sudafrica", ["Capo di Buona Speranza", "Capo Verde", "Ras Hafun"],
  "È anche il punto africano più vicino all'Antartide.", W("Africa"), AFR, "Il punto più a Sud: Capo Agulhas, Sudafrica")
D("geo-261", "Continenti", 3, "Quale stretto separa l'Asia dall'America settentrionale?",
  "Lo stretto di Bering", ["Lo stretto di Malacca", "Lo stretto di Magellano", "Lo stretto di Hormuz"],
  "È largo circa 92 km.", W("Asia"), ASI, "è separata dall'America settentrionale dallo stretto di Bering")
D("geo-262", "Continenti", 3, "Quale massiccio montuoso asiatico è chiamato il «tetto del mondo»?",
  "Il Pamir", ["L'Himalaya", "Il Caucaso", "Gli Urali"],
  "Dal Pamir si diramano grandi catene verso est e sud.", W("Asia"), ASI, "si annodano nel Pamir, il \"tetto del mondo\"")
D("geo-263", "Continenti", 4, "Qual è il più vasto arcipelago della Terra?",
  "L'Arcipelago Malese", ["Le Filippine", "Il Giappone", "La Polinesia"],
  "Fa parte della regione orientale dell'Asia.", W("Asia"), ASI, "l'Arcipelago Malese, il più vasto arcipelago della Terra")
D("geo-264", "Continenti", 4, "Quale continente ha l'altitudine media più elevata (oltre 1000 m), escludendo l'Antartide coperta dai ghiacci?",
  "L'Asia", ["L'Africa", "L'America", "L'Europa"],
  "È anche il continente più vasto e più popolato.", W("Asia"), ASI, "L'Asia è il continente con la maggiore altitudine media")
D("geo-265", "Continenti", 2, "Da quale esploratore prende il nome l'America?",
  "Amerigo Vespucci", ["Cristoforo Colombo", "Giovanni Caboto", "Ferdinando Magellano"],
  "Il cartografo Martin Waldseemüller usò il nome latinizzato Americus.", W("America"), AME, "L'America prende il nome dall'esploratore fiorentino Amerigo Vespucci")
D("geo-266", "Continenti", 3, "Attraverso quale lingua di terra giunsero in America, dall'Asia, le prime popolazioni circa 13.000 anni fa?",
  "La Beringia", ["L'istmo di Panama", "La Groenlandia", "Le Aleutine"],
  "La Beringia univa allora i due continenti.", W("America"), AME, "attraverso la Beringia")
D("geo-267", "Continenti", 4, "Che quota delle terre emerse costituisce l'America?",
  "Circa il 23,4%", ["Circa il 5%", "Circa il 40%", "Circa il 60%"],
  "È l'8,5% della superficie totale della Terra.", W("America"), AME, "il 23,4% delle terre emerse")
D("geo-268", "Continenti", 4, "Chi propose nel 1831 la divisione dell'Oceania in Polinesia, Micronesia, Malesia e Melanesia?",
  "Jules Dumont d'Urville", ["James Cook", "Abel Tasman", "Charles Darwin"],
  "La propose alla Società geografica di Parigi.", W("Oceania"), OCN, "l'ammiraglio francese Jules Dumont d'Urville")
D("geo-269", "Continenti", 3, "Quante isole, all'incirca, fanno parte dell'Oceania?",
  "Circa 30.000", ["Circa 300", "Circa 3.000", "Circa 300.000"],
  "Il nome deriva dal ruolo dell'oceano nell'unirle.", W("Oceania"), OCN, "le sue circa 30 000 isole")
D("geo-270", "Continenti", 3, "Chi guidò la prima spedizione a raggiungere il polo sud geografico, il 14 dicembre 1911?",
  "Roald Amundsen", ["Robert Falcon Scott", "Ernest Shackleton", "James Cook"],
  "Circa un mese dopo arrivò anche la spedizione di Scott.", W("Antartide"), ANT, "una spedizione guidata dall'esploratore polare norvegese Roald Amundsen")
D("geo-271", "Continenti", 3, "Qual è lo spessore medio della calotta glaciale antartica?",
  "Circa 2.000 metri", ["Circa 200 metri", "Circa 20 metri", "Circa 10.000 metri"],
  "Copre il 98% del continente.", W("Antartide"), ANT, "avente uno spessore medio di circa 2 000 metri")
D("geo-272", "Continenti", 4, "A quale anno si fa risalire il primo avvistamento confermato del continente antartico?",
  "Al 1820", ["Al 1492", "Al 1773", "Al 1911"],
  "Si attribuisce alla spedizione russa di Bellingshausen e Lazarev.", W("Antartide"), ANT, "si fa risalire al 1820")
D("geo-273", "Continenti", 4, "Quale navigatore attraversò per primo il Circolo polare antartico, nel 1773?",
  "James Cook", ["Roald Amundsen", "Ferdinando Magellano", "Vasco da Gama"],
  "Arrivò a circa 121 km dalla costa prima di dover invertire la rotta.", W("Antartide"), ANT, "le navi del capitano James Cook")

D("geo-274", "Mediterraneo", 3, "Quale battaglia del 480 a.C. salvò la Grecia dall'occupazione persiana?",
  "La battaglia di Salamina", ["La battaglia di Lepanto", "La battaglia del Mare Sardo", "La battaglia di Azio"],
  "I Greci si opposero alle mire di Serse.", W("Mar Mediterraneo"), MED, "nel 480 a.C., li oppose alle mire di Serse nella battaglia di Salamina")
D("geo-275", "Mediterraneo", 3, "Quali città sono le Repubbliche marinare più note?",
  "Amalfi, Pisa, Genova e Venezia", ["Napoli, Palermo, Bari e Ancona", "Trieste, Livorno, Gaeta e Ragusa", "Roma, Ostia, Pisa e Genova"],
  "Contrastarono l'espansione islamica nel Mediterraneo.", W("Mar Mediterraneo"), MED, "Amalfi, Pisa, Genova e Venezia le più note")
D("geo-276", "Mediterraneo", 4, "Quale tratto di mare divide il Mediterraneo occidentale da quello orientale?",
  "Il canale di Sicilia", ["Lo stretto di Messina", "Lo stretto di Otranto", "Le Bocche di Bonifacio"],
  "L'occidentale ha ampie piane abissali; l'orientale è dominato dalla dorsale Mediterranea.", W("Mar Mediterraneo"), MED, "il Mediterraneo occidentale, delimitato dal canale di Sicilia")
D("geo-277", "Mediterraneo", 4, "Quali sono i due bacini principali del Mediterraneo occidentale?",
  "Il bacino algero-provenzale e il bacino tirrenico", ["Il bacino ionico e quello levantino", "Il bacino adriatico e quello egeo", "Il bacino del Mar Nero e quello di Marmara"],
  "Il bacino tirrenico è la parte più profonda del Mediterraneo occidentale.", W("Mar Mediterraneo"), MED, "quello algero-provenzale e il bacino tirrenico")
D("geo-278", "Oceani", 3, "Qual è la superficie dell'Oceano Pacifico secondo la convenzione italiana?",
  "Circa 179 milioni di km²", ["Circa 74 milioni di km²", "Circa 106 milioni di km²", "Circa 14 milioni di km²"],
  "Atlantico circa 106 milioni, Indiano circa 74 milioni di km².", W("Oceano"), OCE, "Oceano Pacifico, 179000000 km2")
D("geo-279", "Oceani", 4, "Chi propose nel 1928 di considerare anche un Oceano Artico, portando gli oceani a quattro?",
  "L'Organizzazione Idrografica Internazionale", ["La Società geografica italiana", "Le Nazioni Unite", "L'UNESCO"],
  "La convenzione è seguita soprattutto nei paesi di lingua inglese.", W("Oceano"), OCE, "seguendo la proposta del 1928 dell'Organizzazione Idrografica Internazionale")
D("geo-280", "Oceani", 3, "Come si chiamano i mari minori compresi all'interno degli oceani, come il Mediterraneo e il Mar Rosso?",
  "Mari dipendenti", ["Mari chiusi", "Mari interni", "Bacini abissali"],
  "Il Mar Glaciale Artico è considerato in Italia un mare dipendente dall'Atlantico.", W("Oceano"), OCE, "dette \"mari dipendenti\"")
D("geo-281", "Oceani", 4, "Quando si affermò la tripartizione in Oceano Atlantico, Pacifico e Indiano?",
  "Risale alle grandi scoperte, si diffuse nel Settecento e trionfò dall'Ottocento", ["Nell'antichità greca", "Solo nel Novecento", "Nel Medioevo"],
  "Fu favorita dalla scolarizzazione di massa.", W("Oceano"), OCE, "La tripartizione in Oceano Atlantico, Oceano Pacifico e Oceano Indiano risale all'epoca delle grandi scoperte geografiche")

D("geo-282", "Vulcani", 3, "Quale tipo di vulcano è l'Etna?",
  "Uno stratovulcano sovrapposto a un vulcano a scudo", ["Un vulcano sottomarino", "Una caldera spenta", "Un vulcano di fango"],
  "È il più alto vulcano attivo della placca euroasiatica.", W("Etna"), ETN, "Il vulcano è classificato tra quelli definiti a scudo a cui è sovrapposto uno stratovulcano")
D("geo-283", "Vulcani", 4, "Quali fiumi delimitano la regione etnea?",
  "L'Alcantara e il Simeto", ["Il Platani e il Salso", "Il Belice e l'Imera", "Il Tevere e l'Aniene"],
  "La regione etnea ha una superficie di 1570 km².", W("Etna"), ETN, "delimitata dal corso dell'Alcantara e da quello del Simeto")
D("geo-284", "Vulcani", 4, "Quale meridiano attraversa l'Etna, prendendone il nome?",
  "Il 15° meridiano est", ["Il meridiano di Greenwich", "Il 12° meridiano est", "Il 10° meridiano est"],
  "È il meridiano di riferimento del fuso orario dell'Europa centrale.", W("Etna"), ETN, "è attraversato dal 15o meridiano est")
D("geo-285", "Vulcani", 4, "Come si chiama la grande depressione sul versante est dell'Etna?",
  "La Valle del Bove", ["La Bocca Nuova", "La Voragine", "La Grotta del Gelo"],
  "Voragine e Bocca Nuova sono crateri sommitali.", W("Etna"), ETN, "Il versante est è dominato dalla Valle del Bove")
D("geo-286", "Vulcani", 4, "Cosa sono le «sciare» sull'Etna?",
  "Terreni di scorie vulcaniche incoerenti", ["Boschi di castagno", "Laghi craterici", "Sorgenti termali"],
  "Predominano sul versante occidentale e nord.", W("Etna"), ETN, "termine siciliano locale che indica terreno di scorie vulcaniche incoerenti")
D("geo-287", "Pianure", 3, "Quale superficie ha all'incirca la Pianura Padana?",
  "Circa 47.800 km²", ["Circa 4.800 km²", "Circa 150.000 km²", "Circa 12.000 km²"],
  "È la più grande pianura dell'Europa meridionale.", W("Pianura Padana"), PP, "Con una superficie di circa 47820 km2")
D("geo-288", "Pianure", 3, "Cosa sono i fontanili o risorgive della Pianura Padana?",
  "Punti in cui l'acqua della falda riaffiora in superficie", ["Pozzi artificiali per l'irrigazione", "Laghi di origine glaciale", "Canali di bonifica"],
  "Segnano il passaggio tra alta e bassa pianura.", W("Pianura Padana"), PP, "dando origine ai fontanili o risorgive")
D("geo-289", "Pianure", 4, "Come si chiamano le coltivazioni a prato rese possibili dalle acque a temperatura costante delle risorgive?",
  "Marcite", ["Risaie", "Terrazzamenti", "Polder"],
  "Le acque delle risorgive hanno una temperatura tra 9 e 12 °C.", W("Pianura Padana"), PP, "particolari coltivazioni a prato chiamate marcite")
D("geo-290", "Pianure", 3, "Come è detta anche l'alta pianura padana, dal suolo permeabile di sabbie e ghiaie?",
  "Pianura asciutta", ["Pianura irrigua", "Bassopiano", "Pianura alluvionale bassa"],
  "La bassa pianura è detta invece pianura irrigua.", W("Pianura Padana"), PP, "L'alta pianura, detta anche pianura asciutta")
D("geo-291", "Mari e stretti", 3, "Tra quali comuni si misura la larghezza minima dello stretto di Messina?",
  "Villa San Giovanni e Messina", ["Reggio Calabria e Taormina", "Scilla e Milazzo", "Messina e Tropea"],
  "La distanza è di circa 3,14 km.", W("Stretto di Messina"), STR, "tra i comuni di Villa San Giovanni e di Messina")
D("geo-292", "Mari e stretti", 4, "Cosa sono i «piloni dello Stretto»?",
  "Le strutture di sostegno del vecchio elettrodotto aereo che sovrappassava lo stretto", ["I piloni del ponte sullo Stretto", "Due fari medievali", "Antiche torri di avvistamento"],
  "L'elettrodotto del 1957 fu sostituito nel 1992 da cavi sottomarini.", W("Stretto di Messina"), STR, "note come piloni dello Stretto")
D("geo-293", "Mari e stretti", 4, "Con quale denominazione geopolitica medievale era noto lo stretto di Messina?",
  "Faro di Messina", ["Fretum Gaditanum", "Bocca di Scilla", "Canale di Calabria"],
  "In epoca romana era il Fretum Siculum.", W("Stretto di Messina"), STR, "come Faro di Messina")

D("geo-294", "Isole", 3, "A quale arcipelago appartengono Ponza e Ventotene?",
  "Alle Isole Ponziane (o Pontine)", ["Alle Isole Eolie", "All'Arcipelago Toscano", "Alle Isole Tremiti"],
  "Sono nel Mar Tirreno, al largo del Lazio.", W("Isole dell'Italia"), ISO, "Isole Ponziane o Isole Pontine Isola di Ponza Isola di Ventotene")
D("geo-295", "Isole", 2, "A quale arcipelago appartengono l'Elba, il Giglio e Montecristo?",
  "All'Arcipelago Toscano", ["Alle Isole Ponziane", "All'Arcipelago di La Maddalena", "Alle Isole Egadi"],
  "Comprende anche Gorgona, Capraia, Pianosa e Giannutri.", W("Isole dell'Italia"), ISO, "Arcipelago Toscano Isola di Gorgona")
D("geo-296", "Isole", 3, "A quale arcipelago appartengono Lampedusa e Linosa?",
  "Alle Isole Pelagie", ["Alle Isole Egadi", "Alle Isole Eolie", "Alle Isole Maltesi"],
  "Si trovano nel canale di Sicilia.", W("Isole dell'Italia"), ISO, "Isole Pelagie Isola di Lampedusa")
D("geo-297", "Isole", 3, "In quale arcipelago si trova l'isola di Caprera?",
  "Nell'Arcipelago di La Maddalena", ["Nell'Arcipelago Toscano", "Nelle Isole Eolie", "Nelle Isole Flegree"],
  "Si trova nel Mar Tirreno, a nord-est della Sardegna.", W("Isole dell'Italia"), ISO, "Arcipelago di La Maddalena La Maddalena Caprera")
D("geo-298", "Isole", 3, "Quale isola è il centro storico di Siracusa?",
  "Ortigia", ["Mozia", "Ustica", "Pantelleria"],
  "Si trova nel Mar Ionio.", W("Isole dell'Italia"), ISO, "Isola di Ortigia (centro storico di Siracusa)")
D("geo-299", "Isole", 3, "Quali isole fanno parte delle Isole Flegree, nel golfo di Napoli?",
  "Ischia, Procida e Vivara", ["Capri e Li Galli", "Ponza e Palmarola", "Elba e Pianosa"],
  "Capri fa parte dell'Arcipelago Campano ma non delle Flegree.", W("Isole dell'Italia"), ISO, "Isole Flegree Isola d'Ischia")
D("geo-300", "Isole", 4, "Quale superficie complessiva hanno le isole italiane?",
  "Oltre 50.000 km²", ["Circa 5.000 km²", "Oltre 150.000 km²", "Circa 20.000 km²"],
  "Sicilia e Sardegna da sole superano i 49.000 km².", W("Isole dell'Italia"), ISO, "la loro superficie complessiva supera i 50.000 km2")
D("geo-301", "Unione europea", 4, "Con quante entità indipendenti confina l'Unione europea?",
  "21", ["7", "40", "12"],
  "Le frontiere esterne misurano 14.647 km; la costa dell'UE è la seconda al mondo per lunghezza dopo il Canada.", W("Unione europea"), UE, "L'Unione europea confina con 21 entità indipendenti")
