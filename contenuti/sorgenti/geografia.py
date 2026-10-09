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
