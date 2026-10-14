# Informatica — fonti: voci Wikipedia (CC BY-SA 4.0), Appunti di L. Ghio (CC BY-SA 4.0), D.Lgs. 82/2005 CAD (Normattiva).
SO = "Wikipedia_Sistema-operativo.txt"
RETE = "Wikipedia_Rete-informatica.txt"
GR = "Ghio_Appunti-reti-calcolatori.txt"
GC = "Ghio_Appunti-calcolatori-elettronici.txt"
CAD = "norma_DLgs82-2005_CAD.txt"
W = lambda voce: f"Wikipedia, «{voce}» (CC BY-SA 4.0)"
GRF = "L. Ghio, Appunti di Reti di calcolatori (CC BY-SA 4.0)"
GCF = "L. Ghio, Appunti di Calcolatori elettronici (CC BY-SA 4.0)"

D("inf-001", "Sistemi operativi", 1, "Quale di questi è un sistema operativo per dispositivi mobili?",
  "Android", ["Excel", "Firefox", "HTML"],
  "Tra i sistemi operativi per smartphone e tablet ci sono iOS e Android; Excel è un'applicazione, Firefox un browser, HTML un linguaggio di markup.",
  W("Sistema operativo"), SO, "vi sono iOS, Android")

D("inf-002", "Sistemi operativi", 2, "Quale componente del sistema operativo gestisce l'organizzazione dei file sui dischi?",
  "Il file system", ["Lo spooler di stampa", "Il BIOS", "Il browser"],
  "Il sistema operativo è composto da kernel, scheduler, file system, gestore della memoria, gestore delle periferiche, interfaccia utente e spooler.",
  W("Sistema operativo"), SO, "kernel, scheduler, file system, gestore della memoria, gestore delle periferiche")

D("inf-003", "Sistemi operativi", 2, "Come si chiama la capacità di un sistema operativo di eseguire più processi in parallelo?",
  "Multitasking", ["Multiutenza", "Virtualizzazione", "Compilazione"],
  "Un sistema multitasking può svolgere più compiti parallelamente attraverso una politica di scheduling.",
  W("Sistema operativo"), SO, "multitasking o multithreading, se in grado di svolgere più compiti")

D("inf-004", "Sistemi operativi", 1, "Quale di questi NON è un sistema operativo per computer?",
  "Microsoft Word", ["Microsoft Windows", "macOS", "Linux"],
  "Windows, macOS e le distribuzioni Linux sono sistemi operativi per computer; Word è un programma di videoscrittura.",
  W("Sistema operativo"), SO, "Microsoft Windows, MacOS, le distribuzioni Linux")

D("inf-005", "Reti", 2, "Quale sigla indica una rete locale, ad esempio quella di un ufficio?",
  "LAN", ["WAN", "GAN", "VPN"],
  "LAN (Local Area Network) è la rete locale; WAN e GAN coprono aree geografiche più ampie. Dalla loro interconnessione nasce Internet.",
  W("Rete informatica"), RETE, "Esempi di rete informatica sono le reti LAN, WLAN, WAN e GAN")

D("inf-006", "Reti", 2, "A cosa serve il DNS (Domain Name System)?",
  "A convertire i nomi di dominio in indirizzi IP e viceversa", ["A cifrare le email", "Ad assegnare la posta certificata", "A misurare la velocità della connessione"],
  "Il DNS risolve i nomi (es. www.esempio.it) negli indirizzi IP dei server, tramite un database distribuito.",
  GRF, GR, "serve per risolvere (convertire) i nomi in indirizzi IP e viceversa")

D("inf-007", "Reti", 3, "Quanti bit ha un indirizzo IPv4?",
  "32", ["16", "64", "128"],
  "IPv4 gestisce indirizzi a 32 bit (es. 192.168.1.10); IPv6 usa indirizzi a 128 bit.",
  GRF, GR, "gestione di indirizzi a 32 bit (IPv4)")

D("inf-008", "Reti", 3, "A quale livello appartengono i protocolli TCP e UDP?",
  "Al livello di trasporto", ["Al livello fisico", "Al livello applicazione", "Al livello di collegamento"],
  "TCP e UDP sono protocolli del livello trasporto; IP lavora al livello rete.",
  GRF, GR, "Livello Trasporto: Protocolli TCP-UDP")

D("inf-009", "Hardware", 2, "Che cosa significa che la memoria ROM è «non volatile»?",
  "Che il contenuto non si cancella quando manca l'alimentazione", ["Che si può riscrivere all'infinito", "Che è più veloce della RAM", "Che si trova all'esterno del computer"],
  "La ROM mantiene i dati senza alimentazione; la RAM invece è volatile.",
  GCF, GC, "La memoria ROM è non volatile: il contenuto non viene cancellato all'assenza dell'alimentazione")

D("inf-010", "Hardware", 3, "A cosa serve la memoria cache in un calcolatore?",
  "A tenere vicino al processore i dati usati più spesso, per velocizzare l'accesso", ["A conservare i file in modo permanente", "A collegare il computer alla rete", "A stampare più velocemente"],
  "La cache è una memoria piccola e veloce tra processore e memoria principale, che migliora le prestazioni.",
  GCF, GC, "Le memorie cache")

D("inf-011", "PA digitale", 2, "Cosa significa la sigla SPID?",
  "Sistema pubblico di identità digitale", ["Servizio postale integrato digitale", "Sistema protetto di identificazione documentale", "Servizio pubblico di informazione dati"],
  "Lo SPID, insieme a carta d'identità elettronica e carta nazionale dei servizi, consente di identificarsi online con la PA.",
  "D.Lgs. 82/2005 (CAD)", CAD, "il sistema pubblico di identità digitale (SPID)")

D("inf-012", "PA digitale", 3, "Che cos'è il «domicilio digitale» secondo il CAD?",
  "Un indirizzo elettronico eletto presso un servizio di PEC o di recapito certificato qualificato", ["La residenza anagrafica registrata online", "L'indirizzo del sito web personale", "La casella email fornita dal comune"],
  "Il CAD definisce il domicilio digitale come indirizzo elettronico presso un servizio di posta elettronica certificata o di recapito certificato qualificato.",
  "D.Lgs. 82/2005 (CAD), art. 1", CAD, "domicilio digitale: un indirizzo elettronico eletto presso un servizio di posta elettronica certificata")

D("inf-013", "PA digitale", 3, "Su cosa si basa la firma digitale?",
  "Su un sistema di chiavi crittografiche, una pubblica e una privata", ["Su una password scelta dall'utente", "Sulla scansione della firma autografa", "Su un codice inviato via SMS"],
  "Il CAD definisce la firma digitale come firma qualificata basata su un sistema di chiavi crittografiche, una pubblica e una privata, correlate tra loro.",
  "D.Lgs. 82/2005 (CAD), art. 1", CAD, "basata su un su un sistema di chiavi crittografiche, una pubblica e una priva")

D("inf-014", "PA digitale", 4, "Quando un documento informatico soddisfa il requisito della forma scritta con l'efficacia della scrittura privata (art. 2702 c.c.)?",
  "Quando vi è apposta una firma digitale (o altra firma qualificata/avanzata nei casi previsti)", ["Quando è salvato in PDF", "Quando è inviato per email ordinaria", "Quando è stampato e scansionato"],
  "Art. 20 CAD: il documento informatico soddisfa la forma scritta e ha l'efficacia dell'art. 2702 c.c. quando vi è apposta una firma digitale o le altre firme previste.",
  "D.Lgs. 82/2005 (CAD), art. 20", CAD, "Il documento informatico soddisfa il requisito della forma scritta e ha l'efficacia prevista dall'articolo 2702 del Codice civile quando vi è apposta una firma digital")

D("inf-015", "PA digitale", 2, "Cos'è la carta d'identità elettronica (CIE) secondo il CAD?",
  "Il documento d'identità su supporto informatico, con elementi per l'identificazione fisica del titolare", ["Una tessera per i servizi sanitari", "Una copia scansionata della carta cartacea", "Un'app per pagare la PA"],
  "Il CAD definisce la CIE come documento d'identità rilasciato su supporto informatico e munito di elementi per l'identificazione fisica del titolare.",
  "D.Lgs. 82/2005 (CAD), art. 1", CAD, "carta d'identità elettronica: il documento d'identità munito di elementi per l'identificazione fisica del titolare")

D("inf-016", "PA digitale", 3, "Cosa può attestare la posta elettronica certificata (PEC)?",
  "L'invio e l'avvenuta consegna di un messaggio", ["Solo la lettura del messaggio da parte del destinatario", "L'identità di chi apre il messaggio", "Il contenuto del messaggio senza bisogno di firme"],
  "Il CAD definisce la PEC come sistema di comunicazione in grado di attestare l'invio e l'avvenuta consegna di un messaggio, con ricevute opponibili ai terzi.",
  "D.Lgs. 82/2005 (CAD), art. 1", CAD, "posta elettronica certificata: sistema di comunicazione in grado di attestare l'")


# --- Blocco 2: hardware, memorie, codifica dell'informazione (voci di Wikipedia, CC BY-SA 4.0) ---
def I(id, arg, liv, testo, giusta, sbagliate, spieg, voce, file, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W(voce), f"Wikipedia_{file}.txt", frase)

I("inf-017", "Hardware", 1, "Che cos'è l'hardware?", "L'insieme delle parti fisiche e tangibili di un computer", ["L'insieme dei programmi installati", "Il sistema operativo", "La rete Internet"],
  "Il software è invece la parte intangibile.", "Hardware", "Hardware", "è l'insieme di tutte le parti tangibili")
I("inf-018", "Hardware", 1, "Qual è il componente principale di un computer, che collega tra loro tutte le altre componenti?", "La scheda madre", ["La scheda audio", "Il monitor", "L'alimentatore"],
  "Sulla scheda madre si trovano processore, RAM, ROM con il BIOS.", "Hardware", "Hardware", "La scheda madre (in inglese motherboard) è il componente principale di un computer")
I("inf-019", "Hardware", 2, "In quale tipo di memoria si trova il BIOS?", "ROM", ["RAM", "Cache", "Disco rigido"],
  "Sulla scheda madre sono alloggiate le unità di memoria ROM che contengono il BIOS.", "Hardware", "Hardware", "l'insieme di unità di memoria ROM che contengono il BIOS")
I("inf-020", "Hardware", 2, "Che cos'è una scheda d'espansione?", "Una scheda non compresa di serie che, installata, aggiunge funzionalità al computer", ["La scheda madre", "Un modulo di memoria ROM", "Un programma di installazione"],
  "Esempi: scheda video, scheda audio, scheda di rete.", "Hardware", "Hardware", "La scheda d'espansione è una qualsiasi scheda elettronica che non è compresa di serie nel computer")
I("inf-021", "Hardware", 1, "Cosa significa la sigla CPU?", "Central Processing Unit", ["Computer Personal Unit", "Central Program Utility", "Control Power Unit"],
  "È l'unità di elaborazione centrale, il processore.", "CPU", "CPU", "dall'inglese central processing unit")
I("inf-022", "Hardware", 2, "Quali sono i due blocchi fondamentali riuniti nella CPU?", "L'ALU e l'unità di controllo", ["La RAM e la ROM", "Il disco e la cache", "La tastiera e il monitor"],
  "L'ALU esegue le operazioni aritmetico-logiche; l'unità di controllo coordina.", "CPU", "CPU", "l'ALU e l'unità di controllo")
I("inf-023", "Hardware", 3, "A quale italiano si deve l'implementazione dell'Intel 4004, il primo microprocessore commerciale (1971)?", "Federico Faggin", ["Guglielmo Marconi", "Adriano Olivetti", "Enrico Fermi"],
  "Voce «CPU».", "CPU", "CPU", "la cui implementazione si deve all'italiano Federico Faggin")
I("inf-024", "Hardware", 1, "La RAM è una memoria:", "Volatile, ad accesso casuale", ["Non volatile, a sola lettura", "Sequenziale, come un nastro", "Permanente, come un disco"],
  "Il contenuto si perde allo spegnimento.", "Random Access Memory", "RAM", "è un tipo di memoria volatile caratterizzata dal permettere l'accesso diretto a qualunque indirizzo di memoria con gli stessi tempi")
I("inf-025", "Hardware", 1, "Cosa succede alle modifiche a un documento non salvate quando si spegne il computer?", "Si perdono, perché si trovano nella RAM", ["Restano nella RAM", "Vengono salvate automaticamente nel BIOS", "Restano nella CPU"],
  "Vanno salvate su disco o altra memoria non volatile.", "Random Access Memory", "RAM", "se non opportunamente salvate sul disco rigido o su altra memoria non volatile, verranno perse")
I("inf-026", "Hardware", 2, "In quale memoria vengono caricati i programmi che la CPU deve eseguire?", "Nella RAM", ["Nella ROM", "Nel BIOS", "Nella stampante"],
  "La RAM è la memoria primaria dei computer.", "Random Access Memory", "RAM", "Nella memoria RAM vengono copiati (caricati) i programmi che la CPU deve eseguire")
I("inf-027", "Codifica", 1, "Quanti bit compongono un byte?", "8", ["2", "10", "16"],
  "Definizione stabilita dal 1964.", "Byte", "Byte", "Dal 1964 il byte si definisce come formato da 8 bit")
I("inf-028", "Codifica", 2, "Quanti valori diversi può assumere un byte?", "256", ["8", "255", "1.024"],
  "2⁸ = 256 (da 0 a 255).", "Byte", "Byte", "256 possibili valori")
I("inf-029", "Codifica", 2, "Qual è il simbolo del byte come unità di misura?", "B (maiuscola)", ["b (minuscola)", "By", "bt"],
  "La b minuscola indica generalmente il bit.", "Byte", "Byte", "Il simbolo utilizzato per il byte come unità di misura della quantità di informazione è B")
I("inf-030", "Codifica", 4, "Chi coniò il termine «byte» nel 1956?", "Werner Buchholz", ["Alan Turing", "John von Neumann", "Claude Shannon"],
  "All'inizio del progetto IBM Stretch.", "Byte", "Byte", "Il termine byte è stato coniato da Werner Buchholz nel luglio 1956")
I("inf-031", "Codifica", 1, "In quale base è il sistema numerico binario?", "2", ["10", "8", "16"],
  "Usa solo le cifre 0 e 1.", "Sistema numerico binario", "Sistema-numerico-binario", "Il sistema numerico binario è un sistema numerico posizionale in base 2")
I("inf-032", "Codifica", 2, "Quanto vale in decimale il numero binario 1001?", "9", ["1001", "17", "5"],
  "1·8 + 0·4 + 0·2 + 1·1 = 9.", "Sistema numerico binario", "Sistema-numerico-binario", "si considera moltiplicata per")
I("inf-033", "Codifica", 2, "Quanto vale in decimale il numero binario 1111?", "15", ["4", "16", "1.111"],
  "8 + 4 + 2 + 1 = 15.", "Sistema numerico binario", "Sistema-numerico-binario", "si considera moltiplicata per")
I("inf-034", "Codifica", 3, "Come si scrive in binario il numero decimale 10?", "1010", ["1100", "0110", "1001"],
  "8 + 2 = 10.", "Sistema numerico binario", "Sistema-numerico-binario", "si considera moltiplicata per")
I("inf-035", "Codifica", 2, "Perché i computer usano il sistema binario?", "Perché i circuiti digitali gestiscono facilmente due soli valori, due livelli di tensione", ["Perché è più compatto del decimale", "Per una convenzione commerciale", "Perché i numeri binari occupano meno memoria"],
  "0 e 1 corrispondono anche a falso e vero della logica booleana.", "Sistema numerico binario", "Sistema-numerico-binario", "rappresentati fisicamente da due diversi livelli di tensione elettrica")
I("inf-036", "Hardware", 2, "Attraverso quale software il sistema operativo controlla una periferica?", "Il driver", ["Il compilatore", "Il browser", "Il firewall"],
  "Driver e controller di periferica.", "Periferica", "Periferica", "è controllata dal sistema operativo (SO) attraverso un driver")
I("inf-037", "Hardware", 2, "Come si chiama la capacità di una periferica di funzionare appena collegata, senza installazioni manuali?", "Plug and play", ["Autorun", "Backup", "Streaming"],
  "Tipica delle periferiche USB.", "Periferica", "Periferica", "(plug and play)")
I("inf-038", "Hardware", 3, "Con quale meccanismo il sistema operativo gestisce tipicamente le periferiche?", "Interrupt", ["Phishing", "Overclock", "Defrag"],
  "La periferica segnala alla CPU che richiede attenzione.", "Periferica", "Periferica", "La gestione delle periferiche da parte del sistema operativo è operata tipicamente attraverso il meccanismo dell'interrupt")
I("inf-039", "Hardware", 1, "Quale di queste è una periferica di input?", "La tastiera", ["La stampante", "Il monitor", "Gli altoparlanti"],
  "Ogni periferica può essere di input, di output o di input/output.", "Periferica", "Periferica", "Ogni periferica può essere di input/output")
I("inf-040", "Hardware", 1, "Cosa significa la sigla USB?", "Universal Serial Bus", ["Unique System Board", "Universal Storage Box", "User Service Bridge"],
  "È uno standard di comunicazione seriale.", "Universal Serial Bus", "USB", "acronimo di Universal Serial Bus")
I("inf-041", "Hardware", 2, "Come si chiama il connettore USB reversibile più recente, diffuso dal 2014?", "USB-C", ["USB Tipo-A", "USB Tipo-B", "Mini-USB"],
  "È anche più veloce.", "Universal Serial Bus", "USB", "Dal 2014 nei nuovi dispositivi è utilizzata anche una versione più veloce: la USB-C")
I("inf-042", "Hardware", 1, "Qual è la caratteristica principale di una memoria di massa?", "È non volatile: conserva i dati anche a computer spento", ["È più veloce della RAM", "Si cancella allo spegnimento", "Contiene solo il BIOS"],
  "Esempi: dischi, DVD, chiavette USB.", "Memoria di massa", "Memoria-di-massa", "La caratteristica principale della memoria di massa è la")
I("inf-043", "Hardware", 3, "Perché i computer non usano solo memoria di massa al posto della RAM?", "Perché la memoria di massa è molto più lenta nell'accesso ai dati", ["Perché costa di più della RAM", "Perché è volatile", "Perché non può contenere programmi"],
  "La memoria di massa costa meno ma è più lenta.", "Memoria di massa", "Memoria-di-massa", "La ragione risiede nella velocità di accesso ai dati")
I("inf-044", "Hardware", 3, "Quali furono le prime memorie di massa?", "Le unità a nastro magnetico", ["Le chiavette USB", "I DVD", "I dischi a stato solido"],
  "Diffuse dalla seconda metà del XX secolo.", "Memoria di massa", "Memoria-di-massa", "Le prime memorie di massa, furono delle unità a nastro magnetico")
I("inf-045", "Software", 1, "Che cos'è il software?", "L'insieme delle componenti intangibili di elaborazione (programmi)", ["La parte fisica del computer", "Il cavo di rete", "La scheda madre"],
  "È contrapposto all'hardware.", "Software", "Software", "l'insieme delle componenti intangibili di elaborazione")
I("inf-046", "Software", 4, "Chi usò per primo, nel 1957, il termine «software» nel senso moderno?", "John Wilder Tukey", ["Alan Turing", "Bill Gates", "Charles Babbage"],
  "Statistico statunitense.", "Software", "Software", "è stato utilizzato per la prima volta nel 1957 da John Wilder Tukey")
I("inf-047", "Hardware", 3, "Nell'architettura di von Neumann, con «memoria» si intende:", "La memoria principale, dove si caricano programmi e dati", ["Il disco rigido", "La memoria cache della scheda video", "Le periferiche di input"],
  "La memoria secondaria è trattata come un dispositivo di I/O.", "Memoria di massa", "Memoria-di-massa", "Nell'architettura di von Neumann, quando ci si riferisce alla memoria, s'intende la memoria principale")


# --- Blocco 3: Internet, web, posta elettronica, reti, cloud ---
I("inf-048", "Internet", 1, "Che cos'è Internet?", "L'interconnessione globale tra reti di computer", ["Un singolo grande server", "Un browser", "Il sito web di un'azienda"],
  "Da «interconnected networks».", "Internet", "Internet", "è un'architettura di sistema che permette l'interconnessione tra diverse reti di computer a livello globale")
I("inf-049", "Internet", 2, "Quale suite di protocolli costituisce la «lingua comune» di Internet?", "TCP/IP", ["HTML/CSS", "USB", "PDF"],
  "Prende il nome dai due protocolli principali, TCP e IP.", "Internet", "Internet", "chiamata \"TCP/IP\" dal nome dei due protocolli principali")
I("inf-050", "Internet", 3, "Quale progetto è considerato il precursore di Internet (1969)?", "ARPANET", ["World Wide Web", "Ethernet", "Minitel"],
  "Finanziato dalla DARPA statunitense.", "Internet", "Internet", "Il progenitore e precursore della rete Internet è considerato il progetto ARPANET")
I("inf-051", "Internet", 2, "Web e Internet sono la stessa cosa?", "No: il Web è uno dei servizi di Internet", ["Sì, sono sinonimi", "No: Internet è un servizio del Web", "Sì, ma solo in Europa"],
  "Il WWW si basa sul protocollo HTTP ed è nato nel 1991.", "World Wide Web", "World-Wide-Web", "è uno dei principali servizi di Internet")
I("inf-052", "Internet", 2, "Chi pubblicò il primo sito web, il 6 agosto 1991?", "Tim Berners-Lee", ["Bill Gates", "Steve Jobs", "Vint Cerf"],
  "L'idea nacque al CERN di Ginevra nel 1989.", "World Wide Web", "World-Wide-Web", "giorno in cui l'informatico inglese Tim Berners-Lee pubblicò il primo sito web")
I("inf-053", "Internet", 2, "In quale centro di ricerca nacque l'idea del World Wide Web?", "Il CERN di Ginevra", ["Il MIT di Boston", "La NASA", "Lo Xerox PARC"],
  "L'idea risale al 1989.", "World Wide Web", "World-Wide-Web", "presso il CERN (Conseil Européen pour la Recherche Nucléaire) di Ginevra")
I("inf-054", "Internet", 2, "Come si chiamano i collegamenti che uniscono tra loro i contenuti del Web?", "Collegamenti ipertestuali (link)", ["Cookie", "Driver", "Pacchetti"],
  "Il Web è un grande ipertesto.", "World Wide Web", "World-Wide-Web", "interrelati tramite collegamenti ipertestuali (link)")
I("inf-055", "Internet", 1, "Che cos'è l'HTTP?", "Il protocollo per il trasferimento di ipertesti sul Web", ["Un linguaggio di programmazione", "Un tipo di virus", "Un formato di immagine"],
  "HyperText Transfer Protocol.", "Hypertext Transfer Protocol", "Hypertext-Transfer-Protocol", "è un protocollo applicativo usato come principale sistema per la trasmissione d'informazioni su internet")
I("inf-056", "Internet", 3, "Su quale porta TCP resta generalmente in ascolto un server HTTP?", "80", ["21", "25", "8"],
  "HTTPS usa invece la porta 443.", "Hypertext Transfer Protocol", "Hypertext-Transfer-Protocol", "Un server HTTP generalmente resta in ascolto delle richieste dei client sulla porta TCP 80")
I("inf-057", "Internet", 2, "Cosa indica il codice di stato HTTP 404?", "La risorsa richiesta non è stata trovata", ["Accesso consentito", "Errore interno del server", "Reindirizzamento permanente"],
  "Di solito l'indirizzo è sbagliato o il contenuto è stato rimosso.", "Hypertext Transfer Protocol", "Hypertext-Transfer-Protocol", "404 Not Found")
I("inf-058", "Internet", 2, "Con quale architettura lavora il protocollo HTTP?", "Client/server", ["Peer-to-peer obbligatorio", "Mainframe", "Ad anello"],
  "Il client invia la richiesta, il server restituisce la risposta.", "Hypertext Transfer Protocol", "Hypertext-Transfer-Protocol", "L'HTTP è un protocollo che lavora con un'architettura di tipo client/server")
I("inf-059", "Internet", 1, "Che cos'è un browser?", "Un'applicazione per navigare e visualizzare risorse sul Web", ["Un motore di ricerca", "Un sistema operativo", "Un antivirus"],
  "Esempi: Chrome, Firefox, Edge, Safari.", "Browser", "Browser", "è un'applicazione usata principalmente per l'acquisizione, la presentazione e la navigazione di risorse sul Web")
I("inf-060", "Internet", 1, "Quale di questi è un browser?", "Mozilla Firefox", ["Microsoft Word", "Linux", "Excel"],
  "Voce «Browser».", "Browser", "Browser", "Tra i browser più utilizzati vi sono Google Chrome, Mozilla Firefox")
I("inf-061", "Internet", 3, "Qual è stato il primo browser a raggiungere una grande popolarità internazionale?", "Mosaic", ["Internet Explorer", "Google Chrome", "Opera"],
  "Sviluppato dall'NCSA, poi seguito da Netscape Navigator.", "Browser", "Browser", "Il primo browser a raggiungere un'apprezzabile popolarità internazionale fu Mosaic")
I("inf-062", "Internet", 1, "Che cos'è un URL?", "L'indirizzo che identifica una risorsa sulla rete", ["Un tipo di cavo", "Un programma di posta", "Un formato di file compresso"],
  "Uniform Resource Locator, es. https://www.esempio.it/pagina.", "Uniform Resource Locator", "Uniform-Resource-Locator", "è una sequenza di caratteri che identifica univocamente l'indirizzo di una risorsa su una rete di computer")
I("inf-063", "Internet", 3, "Quale sistema traduce il nome di un URL nell'indirizzo IP del server?", "Il DNS", ["L'HTML", "Il DHCP", "L'USB"],
  "Domain Name System.", "Uniform Resource Locator", "Uniform-Resource-Locator", "La risoluzione dell'URL in indirizzo IP, necessario per l'instradamento con il protocollo IP avviene tramite DNS")
I("inf-064", "Internet", 3, "Perché è rischioso inserire username e password direttamente in un URL?", "Perché le credenziali viaggiano in chiaro e la tecnica si presta al phishing", ["Perché l'URL diventa troppo lungo", "Perché il browser le cancella", "Perché il DNS non funziona"],
  "Voce «Uniform Resource Locator».", "Uniform Resource Locator", "Uniform-Resource-Locator", "L'autenticazione in URL è però estremamente rischiosa")
I("inf-065", "Posta elettronica", 1, "Qual è la forma di un indirizzo di posta elettronica?", "nomeutente@dominio", ["www.nomeutente.it", "nomeutente://dominio", "dominio#nomeutente"],
  "Il dominio è un nome DNS.", "Posta elettronica", "Posta-elettronica", "Questi hanno la forma nomeutente@dominio")
I("inf-066", "Posta elettronica", 2, "Chi ideò la posta elettronica nel 1971?", "Ray Tomlinson", ["Tim Berners-Lee", "Steve Wozniak", "Linus Torvalds"],
  "Fu implementata su ARPANET.", "Posta elettronica", "Posta-elettronica", "La posta elettronica è stata ideata nel 1971 da Ray Tomlinson")
I("inf-067", "Posta elettronica", 2, "Quali sono i principali protocolli usati per la posta elettronica su Internet?", "SMTP, POP e IMAP", ["HTTP, FTP e SSH", "USB, HDMI e VGA", "TCP, UDP e ICMP"],
  "SMTP per l'invio, POP e IMAP per la ricezione.", "Posta elettronica", "Posta-elettronica", "Su Internet i protocolli usati sono principalmente SMTP, POP e IMAP")
I("inf-068", "Posta elettronica", 2, "In un'email, cosa contiene il campo «Ccn»?", "I destinatari in copia nascosta, invisibili agli altri", ["I destinatari principali", "Il mittente", "Gli allegati"],
  "Il campo «Cc» contiene i destinatari in copia conoscenza, visibili.", "Posta elettronica", "Posta-elettronica", "Ccn: contiene gli indirizzi di posta elettronica dei destinatari in copia conoscenza nascosta")
I("inf-069", "Posta elettronica", 2, "Perché la posta elettronica è un servizio «asincrono»?", "Perché mittente e destinatario non devono essere collegati contemporaneamente", ["Perché i messaggi arrivano in ordine casuale", "Perché richiede una videochiamata", "Perché funziona solo di notte"],
  "Il messaggio resta nella casella finché non viene letto.", "Posta elettronica", "Posta-elettronica", "La modalità di accesso al servizio è quindi asincrona")
I("inf-070", "Posta elettronica", 3, "La consegna di una normale email è garantita?", "No, la consegna non è garantita", ["Sì, sempre", "Sì, con valore legale", "Solo se c'è un allegato"],
  "Per avere valore legale si usa la PEC.", "Posta elettronica", "Posta-elettronica", "La consegna al destinatario dei messaggi inviati non è garantita")
I("inf-071", "Reti", 1, "Che cos'è un indirizzo IP?", "Un numero che identifica un dispositivo in una rete che usa il protocollo Internet", ["Il nome di un sito web", "La password del Wi-Fi", "Il numero di serie del computer"],
  "È simile a un indirizzo postale.", "Indirizzo IP", "Indirizzo-IP", "un indirizzo IP è un numero che identifica univocamente un nodo in una rete di computer")
I("inf-072", "Reti", 3, "Da quanti bit è composto un indirizzo IPv6?", "128", ["32", "64", "256"],
  "IPv4 usa invece 32 bit.", "Indirizzo IP", "Indirizzo-IP", "L'indirizzo IPv6 (Internet Protocol versione 6) è costituito da 128 bit")
I("inf-073", "Reti", 3, "Quali sono le due parti di un indirizzo IP?", "Indicatore di rete (Net_ID) e indicatore di host (Host_ID)", ["Nome e cognome", "Protocollo e porta", "Dominio e sottodominio"],
  "Il Net_ID serve all'instradamento tra reti.", "Indirizzo IP", "Indirizzo-IP", "L'indirizzo IP si compone di due parti: indicatore di rete (Net_ID) e indicatore di host (Host_ID)")
I("inf-074", "Reti", 1, "Che cos'è il Wi-Fi?", "Una tecnologia per reti locali senza fili", ["Un tipo di cavo di rete", "Un sistema operativo", "Un protocollo di posta"],
  "Basato sugli standard IEEE 802.11.", "Wi-Fi", "Wi-Fi", "Wi-Fi è un insieme di tecnologie per reti locali senza fili (WLAN)")
I("inf-075", "Reti", 2, "Come si chiama il dispositivo che permette ai dispositivi Wi-Fi di collegarsi a una rete?", "Access point", ["Stampante", "Scanner", "Webcam"],
  "Detto anche punto di accesso wireless.", "Wi-Fi", "Wi-Fi", "punto di accesso wireless (access point)")
I("inf-076", "Cloud", 1, "Che cos'è il cloud computing?", "L'erogazione di servizi (archiviazione, elaborazione) via Internet su richiesta", ["Un computer senza schermo", "Un tipo di virus", "Un formato di file"],
  "Le risorse sono in remoto, presso il fornitore.", "Cloud computing", "Cloud-computing", "indica un paradigma di erogazione di servizi offerti su richiesta da un fornitore a un utente finale attraverso la rete internet")
I("inf-077", "Cloud", 2, "Cosa significa SaaS?", "Software as a Service: software usato via Internet", ["Storage and archive System", "Security as a Service", "Server and access Switch"],
  "Esempi: posta web, suite per ufficio online.", "Cloud computing", "Cloud-computing", "SaaS (software as a service)")
I("inf-078", "Cloud", 3, "Cosa significa PaaS nel cloud computing?", "Platform as a Service: una piattaforma software eseguita in remoto", ["Password as a Service", "Printer and access Service", "Personal area System"],
  "Fornisce servizi, programmi, librerie per sviluppare.", "Cloud computing", "Cloud-computing", "PaaS (platform as a service)")


# --- Blocco 4: sicurezza informatica, software libero, produttività ---
I("inf-079", "Sicurezza", 2, "Quali sono i tre obiettivi della sicurezza informatica secondo la triade CIA?", "Riservatezza, integrità e disponibilità", ["Velocità, costo e capacità", "Backup, antivirus e firewall", "Hardware, software e rete"],
  "Confidentiality, Integrity, Availability.", "Sicurezza informatica", "Sicurezza-informatica", "la tutela della riservatezza, dell'integrità e della disponibilità delle informazioni")
I("inf-080", "Sicurezza", 2, "Cosa garantisce la «riservatezza» delle informazioni?", "Che siano accessibili solo ai soggetti autorizzati", ["Che non vengano mai cancellate", "Che siano sempre raggiungibili", "Che siano pubbliche"],
  "Strumenti: crittografia e controlli di accesso.", "Sicurezza informatica", "Sicurezza-informatica", "La riservatezza consiste nel garantire che le informazioni siano accessibili esclusivamente ai soggetti autorizzati")
I("inf-081", "Sicurezza", 3, "Cosa garantisce l'«integrità» dei dati?", "Che non vengano modificati o distrutti in modo non autorizzato", ["Che siano cifrati", "Che siano accessibili sempre", "Che siano duplicati"],
  "Si usano funzioni di hash, firme digitali e controlli delle modifiche.", "Sicurezza informatica", "Sicurezza-informatica", "L'integrità consiste nel garantire che i dati non vengano modificati, alterati o distrutti in modo non autorizzato")
I("inf-082", "Sicurezza", 3, "Quali misure aumentano la «disponibilità» di un sistema?", "Aggiornamenti, patch, backup e ridondanza delle risorse", ["Usare una sola password per tutto", "Spegnere il server di notte", "Disattivare il firewall"],
  "Si riducono i single point of failure.", "Sicurezza informatica", "Sicurezza-informatica", "l'installazione delle patch di sicurezza, il backup, la ridondanza delle risorse")
I("inf-083", "Sicurezza", 1, "Che cos'è il malware?", "Un software malevolo che danneggia o disturba l'utente", ["Un programma antivirus", "Un componente hardware difettoso", "Un tipo di cavo"],
  "Da malicious software.", "Malware", "Malware", "abbreviazione dell'inglese malicious software")
I("inf-084", "Sicurezza", 2, "Quale tipo di malware cifra i dati della vittima e chiede un riscatto?", "Ransomware", ["Adware", "Keylogger", "Worm"],
  "Esempio: CryptoLocker.", "Malware", "Malware", "oppure può criptare i dati del computer della vittima, estorcendo denaro per la decriptazione")
I("inf-085", "Sicurezza", 2, "Che cosa fa un keylogger?", "Registra ciò che l'utente digita sulla tastiera", ["Blocca le pubblicità", "Fa il backup dei file", "Cifra il disco"],
  "Rende possibile il furto di password e dati.", "Malware", "Malware", "I Keylogger sono dei programmi in grado di registrare tutto ciò che un utente digita su una tastiera")
I("inf-086", "Sicurezza", 3, "Chi coniò il termine «malware» nel 1990?", "Yisrael Radai", ["Fred Cohen", "Kevin Mitnick", "John McAfee"],
  "Prima si parlava di virus per computer.", "Malware", "Malware", "Termine coniato nel 1990 da Yisrael Radai")
I("inf-087", "Sicurezza", 1, "Che cos'è il phishing?", "Una truffa in cui ci si finge un ente affidabile per ottenere dati personali o password", ["Un antivirus gratuito", "Un sistema di backup", "Un protocollo di rete"],
  "Avviene soprattutto via email, ma anche via SMS.", "Phishing", "Phishing", "Il phishing è un tipo di truffa effettuata su Internet")
I("inf-088", "Sicurezza", 2, "Su quale tecnica si basa il phishing?", "Ingegneria sociale", ["Overclock", "Compressione dei dati", "Crittografia asimmetrica"],
  "Sfrutta la fiducia della vittima con messaggi che imitano quelli legittimi.", "Phishing", "Phishing", "sfrutta una tecnica di ingegneria sociale")
I("inf-089", "Sicurezza", 3, "Come si chiama il phishing mirato verso una specifica persona o azienda?", "Spear phishing", ["Vishing", "Spam", "Pharming"],
  "Gli attaccanti raccolgono informazioni sull'obiettivo.", "Phishing", "Phishing", "Un attacco mirato verso un individuo o una compagnia è stato denominato spear phishing")
I("inf-090", "Sicurezza", 3, "Come si chiama il phishing effettuato tramite telefonate?", "Vishing", ["Smishing", "Spear phishing", "Spoofing"],
  "Da voice phishing.", "Phishing", "Phishing", "Il vishing (voice phishing)")
I("inf-091", "Sicurezza", 1, "Che cos'è un firewall?", "Un componente hardware o software di difesa perimetrale della rete", ["Un programma di videoscrittura", "Un tipo di memoria", "Un browser sicuro"],
  "Il nome deriva dal muro tagliafuoco.", "Firewall", "Firewall", "è un componente hardware e/o software di difesa perimetrale di una rete")
I("inf-092", "Sicurezza", 2, "A cosa serve la crittografia?", "A rendere un messaggio incomprensibile a chi non è autorizzato a leggerlo", ["A comprimere i file", "A velocizzare la rete", "A stampare documenti"],
  "Garantisce la riservatezza.", "Crittografia", "Crittografia", "dei metodi per rendere un messaggio non comprensibile/intelligibile a persone non autorizzate a leggerlo")
I("inf-093", "Sicurezza", 3, "Nella crittografia simmetrica:", "Si usa un'unica chiave per cifrare e decifrare", ["Si usano due chiavi diverse", "Non si usano chiavi", "La chiave è sempre pubblica"],
  "Nella crittografia asimmetrica si usano chiavi diverse (pubblica e privata).", "Crittografia", "Crittografia", "con cui si faceva uso di un'unica chiave sia per proteggere il messaggio che per renderlo nuovamente leggibile")
I("inf-094", "Sicurezza", 3, "Nella crittografia asimmetrica:", "Si usano chiavi diverse per cifrare e per decifrare", ["Si usa la stessa chiave", "Il messaggio non è cifrato", "Serve una password condivisa a voce"],
  "Chi vuole ricevere un messaggio segreto diffonde la chiave pubblica.", "Crittografia", "Crittografia", "utilizza chiavi diverse per cifrare e per decifrare un messaggio")
I("inf-095", "Sicurezza", 2, "A quale personaggio storico si attribuisce un celebre cifrario a sostituzione?", "Giulio Cesare", ["Napoleone", "Carlo Magno", "Cristoforo Colombo"],
  "Il cifrario di Cesare.", "Crittografia", "Crittografia", "a Gaio Giulio Cesare si attribuisce l'uso del cosiddetto cifrario di Cesare")
I("inf-096", "Sicurezza", 1, "Che cos'è un backup?", "Una copia di riserva dei dati per poterli ripristinare", ["Un virus", "Un aggiornamento del sistema operativo", "Un tipo di firewall"],
  "Protegge anche dai ransomware.", "Backup", "Backup", "una o più copie di riserva dei dati")
I("inf-097", "Sicurezza", 3, "Cosa prevede la regola del backup «3-2-1»?", "Tre copie dei dati, su due tipi di supporto, di cui una offline", ["Tre backup al giorno per due settimane", "Tre password, due utenti, un amministratore", "Tre dischi, due server, un cloud"],
  "Voce «Backup».", "Backup", "Backup", "che prevede tre (3) copie dei dati su due (2) tipi diversi di unità archiviazione")
I("inf-098", "Sicurezza", 2, "Quali tipi di backup si distinguono in base ai dati copiati?", "Completo, differenziale e incrementale", ["Rapido, lento e medio", "Locale, nazionale e globale", "Testuale, grafico e audio"],
  "Il backup incrementale copia solo le modifiche dall'ultimo backup.", "Backup", "Backup", "tipo di backup (completo, differenziale, incrementale)")
I("inf-099", "Software", 2, "Cosa caratterizza il software libero?", "La licenza ne consente studio, uso, modifica e redistribuzione", ["È sempre gratuito ma non modificabile", "È prodotto solo da aziende", "Non ha licenza"],
  "Si contrappone al software proprietario.", "Software libero", "Software-libero", "che ne concede lo studio, l'utilizzo, la modifica e la redistribuzione")
I("inf-100", "Software", 3, "Chi fondò nel 1983 il progetto GNU?", "Richard Stallman", ["Linus Torvalds", "Bill Gates", "Steve Jobs"],
  "Obiettivo: un sistema operativo completamente libero.", "Software libero", "Software-libero", "fondò il progetto GNU")
I("inf-101", "Software", 4, "Quante sono le «libertà fondamentali» del software libero secondo la Free Software Foundation?", "Quattro", ["Due", "Tre", "Cinque"],
  "Eseguire, studiare/modificare, ridistribuire, migliorare e diffondere.", "Software libero", "Software-libero", "garantisce quattro «libertà fondamentali»")
I("inf-102", "Produttività", 1, "Che cos'è un foglio elettronico (foglio di calcolo)?", "Un software per eseguire calcoli su dati organizzati in celle", ["Un programma di posta", "Un sistema operativo", "Un tipo di stampante"],
  "Esempi: Microsoft Excel, LibreOffice Calc.", "Foglio elettronico", "Foglio-elettronico", "è un software di produttività personale che consente di operare in maniera efficiente su una più o meno grande mole di dati")
I("inf-103", "Produttività", 2, "Con quale simbolo deve iniziare una formula in una cella di un foglio di calcolo?", "=", ["#", "$", "@"],
  "Ad esempio =A1+B1.", "Foglio elettronico", "Foglio-elettronico", "la prima cosa da scrivere nella cella è il simbolo =")
I("inf-104", "Produttività", 3, "In un foglio di calcolo, cosa indica il simbolo $ in un riferimento come $A$1?", "Un riferimento assoluto, che non cambia copiando la formula", ["Una valuta", "Un errore", "Una cella vuota"],
  "Senza $ i riferimenti sono relativi.", "Foglio elettronico", "Foglio-elettronico", "per avere un riferimento assoluto, la lettera o il numero che lo indicano nella formula devono essere preceduti dal carattere")
I("inf-105", "Produttività", 3, "Qual è stato il primo foglio elettronico, ideato da Dan Bricklin?", "VisiCalc", ["Lotus 1-2-3", "Excel", "Calc"],
  "Trasformò il personal computer in strumento di lavoro.", "Foglio elettronico", "Foglio-elettronico", "il primo foglio elettronico")
I("inf-106", "Produttività", 2, "Cosa significa WYSIWYG nei programmi di videoscrittura?", "What You See Is What You Get: ciò che vedi è ciò che ottieni", ["Un formato di file", "Un comando di stampa", "Un linguaggio di programmazione"],
  "L'interfaccia grafica mostra il testo come sarà stampato.", "Videoscrittura", "Videoscrittura", "I programmi What You See Is What You Get utilizzano infatti interfacce grafiche")


# --- Blocco 5: algoritmi, programmazione, basi di dati, IA, GDPR, PEC ---
I("inf-107", "Programmazione", 1, "Che cos'è un algoritmo?", "Una sequenza finita di istruzioni che risolve una classe di problemi", ["Un linguaggio di programmazione", "Un componente hardware", "Un tipo di file"],
  "Deve essere finito, deterministico, non ambiguo e generale.", "Algoritmo", "Algoritmo", "è la specificazione di una sequenza finita di operazioni")
I("inf-108", "Programmazione", 2, "Quale proprietà NON è richiesta a un algoritmo?", "Essere scritto in un linguaggio specifico", ["Essere finito", "Essere non ambiguo", "Essere deterministico"],
  "Un algoritmo può essere descritto anche con diagrammi di flusso o pseudocodice.", "Algoritmo", "Algoritmo", "finito: è costituito da un numero finito di istruzioni e deve sempre terminare")
I("inf-109", "Programmazione", 3, "Da quale matematico deriva il termine «algoritmo»?", "Al-Khwarizmi", ["Euclide", "Fibonacci", "Al-Biruni"],
  "Matematico persiano del IX secolo.", "Algoritmo", "Algoritmo", "Il termine deriva dalla trascrizione latina del nome del matematico persiano al-Khwarizmi")
I("inf-110", "Programmazione", 2, "Con quali strumenti si può descrivere un algoritmo prima di programmarlo?", "Diagramma di flusso o pseudocodice", ["Foglio elettronico o email", "Firewall o antivirus", "BIOS o driver"],
  "Poi viene tradotto in un linguaggio di programmazione.", "Algoritmo", "Algoritmo", "un algoritmo può essere descritto attraverso l'uso di un diagramma di flusso o ricorrendo a uno pseudocodice")
I("inf-111", "Programmazione", 3, "Quando un problema si dice «calcolabile»?", "Quando è risolvibile mediante un algoritmo", ["Quando ha una soluzione numerica", "Quando si risolve con una calcolatrice", "Quando ha infinite soluzioni"],
  "L'algoritmo è alla base della teoria della calcolabilità.", "Algoritmo", "Algoritmo", "un problema è calcolabile quando è risolvibile mediante un algoritmo")
I("inf-112", "Programmazione", 1, "Che cos'è un linguaggio di programmazione?", "Un sistema di notazione per scrivere programmi per computer", ["Una lingua straniera", "Un sistema operativo", "Un protocollo di rete"],
  "È definito da sintassi e semantica.", "Linguaggio di programmazione", "Linguaggio-di-programmazione", "Un linguaggio di programmazione è un sistema di notazione per la scrittura di programmi per computer")
I("inf-113", "Programmazione", 3, "Chi è considerata autrice del primo linguaggio di programmazione, per la macchina di Babbage?", "Ada Lovelace", ["Grace Hopper", "Marie Curie", "Hedy Lamarr"],
  "Voce «Linguaggio di programmazione».", "Linguaggio di programmazione", "Linguaggio-di-programmazione", "il linguaggio meccanico adoperato da Ada Lovelace per la programmazione della macchina di Charles Babbage")
I("inf-114", "Programmazione", 2, "Che cos'è l'assembly?", "Una rappresentazione simbolica del linguaggio macchina", ["Un linguaggio ad altissimo livello", "Un database", "Un browser"],
  "È un linguaggio a basso livello.", "Linguaggio di programmazione", "Linguaggio-di-programmazione", "l'assembly, che costituisce una rappresentazione simbolica del linguaggio macchina")
I("inf-115", "Programmazione", 3, "Quale fu uno dei primi linguaggi ad alto livello, creato nel 1957 da John Backus?", "Fortran", ["Java", "Python", "HTML"],
  "Da esso derivò il BASIC (1964).", "Linguaggio di programmazione", "Linguaggio-di-programmazione", "il Fortran, creato nel 1957 da John Backus")
I("inf-116", "Programmazione", 2, "Come si classificano i linguaggi in base alla vicinanza al linguaggio macchina o a quello umano?", "A basso livello e ad alto livello", ["Compressi e non compressi", "Pubblici e privati", "Grafici e sonori"],
  "Si distinguono anche linguaggi compilati e interpretati.", "Linguaggio di programmazione", "Linguaggio-di-programmazione", "essi vengono classificati in linguaggi a basso livello e ad alto livello")
I("inf-117", "Programmazione", 3, "In che anno nacque il linguaggio Java?", "1995", ["1972", "1985", "2005"],
  "Linguaggio orientato agli oggetti.", "Linguaggio di programmazione", "Linguaggio-di-programmazione", "successivamente Java, classe 1995")
I("inf-118", "Basi di dati", 1, "Che cos'è una base di dati (database)?", "Una collezione organizzata di dati in forma elettronica", ["Un programma di videoscrittura", "Un tipo di processore", "Una rete wireless"],
  "Si gestisce con un DBMS.", "Base di dati", "Base-di-dati", "è una collezione organizzata di dati in forma elettronica")
I("inf-119", "Basi di dati", 2, "Cosa indica la sigla DBMS?", "Il sistema software per gestire una base di dati", ["Un tipo di disco", "Un protocollo di posta", "Un linguaggio di markup"],
  "Database Management System.", "Base di dati", "Base-di-dati", "database management system: ovvero il sistema software necessario all'interfacciamento con la base di dati")
I("inf-120", "Basi di dati", 3, "Chi ideò il modello relazionale delle basi di dati?", "Edgar F. Codd", ["Charles Bachman", "Larry Ellison", "Donald Knuth"],
  "Ricercatore IBM.", "Base di dati", "Base-di-dati", "Edgar F. Codd lavorava nella sede californiana di IBM")
I("inf-121", "Basi di dati", 2, "Come si rappresentano i dati nel modello relazionale?", "Mediante tabelle e relazioni tra esse", ["Mediante un unico file di testo", "Mediante grafici a torta", "Mediante cartelle e sottocartelle"],
  "È il modello attualmente più diffuso.", "Base di dati", "Base-di-dati", "rappresentabile mediante tabelle e relazioni tra esse")
I("inf-122", "Basi di dati", 3, "Nel modello relazionale, cos'è la chiave di un record?", "Un identificatore univoco della riga", ["La password del database", "Il nome della tabella", "Un campo sempre vuoto"],
  "Serve a collegare le tabelle.", "Base di dati", "Base-di-dati", "per ogni record viene definita una chiave, ovvero un identificatore univoco della tupla")
I("inf-123", "Basi di dati", 1, "Che cos'è SQL?", "Un linguaggio standard per database relazionali", ["Un sistema operativo", "Un formato di immagine", "Un protocollo di rete"],
  "Structured Query Language.", "Structured Query Language", "Structured-Query-Language", "è un linguaggio standardizzato per database basati sul modello relazionale")
I("inf-124", "Basi di dati", 2, "In SQL, quale clausola serve a definire criteri di ricerca?", "WHERE", ["FROM", "INSERT", "ORDER"],
  "Esempio: SELECT * FROM utenti WHERE eta > 30.", "Structured Query Language", "Structured-Query-Language", "L'unico operatore condizionale di SQL è WHERE")
I("inf-125", "Basi di dati", 2, "Quale comando SQL inserisce una nuova riga in una tabella?", "INSERT", ["SELECT", "DROP", "WHERE"],
  "SELECT serve per interrogare.", "Structured Query Language", "Structured-Query-Language", "il comando INSERT opera inserendo in tabella una sola riga per volta")
I("inf-126", "Basi di dati", 3, "Quale sottoinsieme di SQL serve a creare e modificare lo schema del database?", "DDL (Data Definition Language)", ["DML (Data Manipulation Language)", "DQL (Data Query Language)", "HTML"],
  "DML per gestire i dati, DQL per interrogarli, DCL per i permessi.", "Structured Query Language", "Structured-Query-Language", "DDL = Data Definition Language")
I("inf-127", "Basi di dati", 4, "Dove e quando nacque SQL?", "Nei laboratori IBM nel 1974", ["Al CERN nel 1989", "Alla Microsoft nel 1985", "Al MIT nel 1960"],
  "Inizialmente si chiamava SEQUEL.", "Structured Query Language", "Structured-Query-Language", "Il SQL nasce nel 1974 ad opera di Donald Chamberlin, nei laboratori dell'IBM")
I("inf-128", "Intelligenza artificiale", 1, "Che cosa si intende per intelligenza artificiale?", "La capacità di un sistema artificiale di simulare capacità tipiche dell'intelletto umano", ["Un nuovo tipo di processore", "Un programma antivirus", "La rete Internet"],
  "Esempi: riconoscimento vocale, traduzione, visione artificiale.", "Intelligenza artificiale", "Intelligenza-artificiale", "è il termine ombrello che indica l'insieme delle capacità il cui svolgimento richiederebbe normalmente un intelletto naturale")
I("inf-129", "Intelligenza artificiale", 3, "In che anno l'intelligenza artificiale fu istituita come campo accademico, con la conferenza di Dartmouth?", "1956", ["1946", "1969", "1991"],
  "Le radici risalgono al lavoro di Alan Turing.", "Intelligenza artificiale", "Intelligenza-artificiale", "la disciplina venne istituita formalmente come campo accademico nel 1956")
I("inf-130", "Intelligenza artificiale", 3, "Quale regolamento europeo disciplina l'intelligenza artificiale?", "Il Regolamento UE 2024/1689 (AI Act)", ["Il Regolamento UE 2016/679 (GDPR)", "Il Regolamento eIDAS 910/2014", "La Direttiva NIS2"],
  "Definisce i sistemi di IA come sistemi automatizzati con un certo grado di autonomia.", "Intelligenza artificiale", "Intelligenza-artificiale", "Il Regolamento UE 2024/1689 (AI Act)")
I("inf-131", "Intelligenza artificiale", 2, "Quale di questi è un paradigma di apprendimento dell'IA?", "Machine learning", ["Overclocking", "Defragmentazione", "Phishing"],
  "Altri: deep learning, reinforcement learning, apprendimento supervisionato.", "Intelligenza artificiale", "Intelligenza-artificiale", "Tra i paradigmi di apprendimento più diffusi figurano il machine learning")
I("inf-132", "Privacy", 2, "Qual è il numero ufficiale del GDPR, il Regolamento generale sulla protezione dei dati?", "Regolamento (UE) 2016/679", ["Direttiva 95/46/CE", "D.Lgs. 196/2003", "Regolamento (UE) 2024/1689"],
  "Operativo dal 25 maggio 2018.", "Regolamento generale sulla protezione dei dati", "Regolamento-generale-sulla-protezione-dei-dati", "ufficialmente regolamento (UE) n. 2016/679")
I("inf-133", "Privacy", 2, "Da quando è operativo il GDPR?", "Dal 25 maggio 2018", ["Dal 1° gennaio 2016", "Dal 30 giugno 2003", "Dal 24 maggio 2020"],
  "Entrato in vigore il 24 maggio 2016.", "Regolamento generale sulla protezione dei dati", "Regolamento-generale-sulla-protezione-dei-dati", "operativo a partire dal 25 maggio 2018")
I("inf-134", "Privacy", 3, "Entro quanto tempo il titolare deve notificare un data breach all'autorità?", "72 ore da quando ne viene a conoscenza", ["24 ore", "30 giorni", "Una settimana"],
  "GDPR, art. 33.", "Regolamento generale sulla protezione dei dati", "Regolamento-generale-sulla-protezione-dei-dati", "entro 72 ore dal momento in cui ne viene a conoscenza")
I("inf-135", "Privacy", 3, "Quale diritto consente all'interessato di ricevere i propri dati in formato strutturato e leggibile da dispositivo automatico?", "Il diritto alla portabilità", ["Il diritto di accesso civico", "Il diritto all'oblio", "Il diritto di rettifica"],
  "GDPR, art. 20.", "Regolamento generale sulla protezione dei dati", "Regolamento-generale-sulla-protezione-dei-dati", "Il diritto alla portabilità è sancito dall'articolo 20")
I("inf-136", "Privacy", 2, "Come si chiama la figura del «responsabile della protezione dei dati» prevista dal GDPR?", "DPO (Data Protection Officer)", ["CEO", "CIO", "RUP"],
  "Obbligatoria, ad esempio, per le autorità pubbliche.", "Regolamento generale sulla protezione dei dati", "Regolamento-generale-sulla-protezione-dei-dati", "Responsabile per la protezione dei dati (\"DPO\", Data Protection Officer)")
I("inf-137", "Privacy", 2, "Un indirizzo IP può essere un dato personale secondo la definizione richiamata dal GDPR?", "Sì, come nomi, foto, email e dati bancari", ["No, mai", "Solo se pubblico", "Solo per le aziende"],
  "Il dato personale è qualunque informazione relativa a una persona identificata o identificabile.", "Regolamento generale sulla protezione dei dati", "Regolamento-generale-sulla-protezione-dei-dati", "informazioni mediche o indirizzi IP di computer")
I("inf-138", "PA digitale", 2, "In quale registro pubblico sono iscritti gli indirizzi PEC dei soggetti obbligati ad averla?", "INI-PEC", ["SPID", "ANPR", "IPA-MAIL"],
  "Indice nazionale degli indirizzi PEC.", "Posta elettronica certificata", "Posta-elettronica-certificata", "L'indirizzo PEC dei soggetti obbligati ad averla è iscritto nel registro pubblico INI-PEC")
I("inf-139", "PA digitale", 2, "Quale ricevuta fornisce al mittente il gestore PEC del destinatario?", "La ricevuta di avvenuta consegna", ["La ricevuta fiscale", "La conferma di lettura", "Il protocollo informatico"],
  "Indica il momento della consegna nella casella del destinatario.", "Posta elettronica certificata", "Posta-elettronica-certificata", "fornirà al mittente una ricevuta di avvenuta consegna")
I("inf-140", "PA digitale", 3, "Quale ente vigila sui gestori PEC e ne pubblica l'elenco?", "L'Agenzia per l'Italia digitale (AgID)", ["Il Garante privacy", "L'ANAC", "La Consob"],
  "Voce «Posta elettronica certificata».", "Posta elettronica certificata", "Posta-elettronica-certificata", "è demandata all'Agenzia per l'Italia digitale")
I("inf-141", "PA digitale", 2, "A cosa serve SPID?", "Ad accedere con un'unica identità digitale ai servizi online della PA e dei privati aderenti", ["A inviare PEC", "A firmare digitalmente i documenti", "A pagare le tasse in contanti"],
  "Sistema Pubblico di Identità Digitale.", "SPID", "SPID", "è il sistema unico di accesso con identità digitale ai servizi online della pubblica amministrazione italiana")
I("inf-142", "PA digitale", 3, "Quale regolamento europeo ha consentito il riconoscimento di SPID a livello UE?", "Il regolamento eIDAS n. 910/2014", ["Il GDPR 2016/679", "L'AI Act 2024/1689", "La direttiva NIS2"],
  "Permette l'accesso ai servizi delle PA di tutta l'Unione.", "SPID", "SPID", "come previsto dal Regolamento europeo eIDAS n. 910/2014")


# --- Blocco 6: Codice dell'amministrazione digitale e Codice privacy (testi di legge) ---
PRIV = "norma_DLgs196-2003_privacy.txt"
def C(id, liv, testo, giusta, sbagliate, spieg, art, frase):
    D(id, "PA digitale", liv, testo, giusta, sbagliate, spieg, f"D.Lgs. 82/2005 (CAD), art. {art}", CAD, frase)

C("inf-143", 2, "Secondo il CAD, che cos'è il «documento informatico»?", "Il documento elettronico che contiene la rappresentazione informatica di atti, fatti o dati giuridicamente rilevanti",
  ["Qualsiasi file salvato su un computer", "La scansione di un documento cartaceo non firmato", "Un documento stampato da un computer"],
  "Il documento analogico è invece la rappresentazione non informatica.", "1", "documento informatico: il documento elettronico che contiene la rappresentazione informatica di atti, fatti o dati giuridicamente rilevanti")
C("inf-144", 2, "Secondo il CAD, cos'è il «documento analogico»?", "La rappresentazione non informatica di atti, fatti o dati giuridicamente rilevanti",
  ["Un documento firmato digitalmente", "Un file PDF", "Una copia informatica"],
  "Art. 1, lett. p-bis).", "1", "documento analogico: la rappresentazione non informatica di atti, fatti o dati giuridicamente rilevanti")
C("inf-145", 3, "Secondo il CAD, cos'è il «duplicato informatico»?", "Il documento ottenuto memorizzando la medesima sequenza di valori binari del documento originario",
  ["Una fotocopia del documento", "Una copia con diversa sequenza di valori binari", "La stampa di un documento informatico"],
  "La copia informatica di documento informatico ha invece una diversa sequenza di valori binari.", "1", "duplicato informatico: il documento informatico ottenuto mediante la memorizzazione")
C("inf-146", 3, "Secondo il CAD, cos'è un «formato aperto»?", "Un formato di dati reso pubblico, documentato e neutro rispetto agli strumenti tecnologici",
  ["Un formato utilizzabile solo con software a pagamento", "Un file non protetto da password", "Un formato compresso"],
  "Art. 1, lett. l-bis).", "1", "formato aperto: un formato di dati reso pubblico, documentato esaustivamente e neutro")
C("inf-147", 4, "Quale caratteristica NON è propria dei «dati di tipo aperto» secondo il CAD?", "Possono essere usati solo per finalità non commerciali",
  ["Sono disponibili con licenza che ne permette l'uso a chiunque", "Sono in formato aperto e adatti all'uso automatico", "Sono gratuiti o a costi marginali"],
  "L'uso è consentito a chiunque, anche per finalità commerciali.", "1", "anche per finalità commerciali, in formato disaggregato")
C("inf-148", 2, "Cosa definisce il CAD come «identità digitale»?", "La rappresentazione informatica della corrispondenza tra un utente e i suoi attributi identificativi",
  ["La password della posta elettronica", "Il codice fiscale", "La firma autografa scansionata"],
  "Art. 1, lett. u-quater).", "1", "identità digitale: la rappresentazione informatica della corrispondenza tra un utente e i suoi attributi identificativi")
C("inf-149", 3, "Secondo il CAD, cos'è l'«interoperabilità»?", "La capacità di un sistema informativo con interfacce pubbliche e aperte di interagire automaticamente con altri sistemi",
  ["La possibilità di lavorare da casa", "L'obbligo di usare un solo fornitore", "La compatibilità tra stampanti"],
  "Art. 1, lett. dd).", "1", "interoperabilità: caratteristica di un sistema informativo, le cui interfacce sono pubbliche e aperte")
C("inf-150", 2, "Cos'è la carta nazionale dei servizi (CNS) secondo il CAD?", "Il documento su supporto informatico per accedere per via telematica ai servizi della PA",
  ["Una carta di credito della PA", "La tessera elettorale", "Un abbonamento ai trasporti"],
  "Art. 1, lett. d).", "1", "carta nazionale dei servizi: il documento rilasciato su supporto informatico per consentire l'accesso per via telematica")
C("inf-151", 2, "Chi ha diritto di usare le soluzioni e gli strumenti del CAD nei rapporti con la PA?", "Chiunque", ["Solo i cittadini maggiorenni", "Solo le imprese", "Solo i dipendenti pubblici"],
  "Art. 3: diritto all'uso delle tecnologie.", "3", "Chiunque ha il diritto di usare")
C("inf-152", 3, "Chi ha l'obbligo di dotarsi di un domicilio digitale secondo il CAD?", "PA, professionisti iscritti in albi ed elenchi e imprese iscritte nel registro delle imprese",
  ["Tutti i cittadini maggiorenni", "Solo i dipendenti pubblici", "Solo le grandi imprese"],
  "Per gli altri è una facoltà.", "3-bis", "i professionisti tenuti all'iscrizione in albi ed elenchi e i soggetti tenuti all'iscrizione nel registro delle imprese hanno l'obbligo di dotarsi di un domicilio digitale")
C("inf-153", 2, "Le pubbliche amministrazioni devono accettare pagamenti elettronici?", "Sì, tramite la piattaforma prevista dal CAD (pagoPA)", ["No, solo contanti", "Solo per importi superiori a 1.000 euro", "Solo dalle imprese"],
  "Art. 5 CAD.", "5", "sono obbligati ad accettare, tramite la piattaforma di cui al comma 2, i pagamenti spettanti a qualsiasi titolo attraverso sistemi di pagamento elettronico")
C("inf-154", 3, "Come si chiama la figura che, presso l'AgID, riceve le segnalazioni di violazioni del CAD da parte delle PA?", "Difensore civico per il digitale",
  ["Garante della privacy", "Responsabile del procedimento", "Responsabile della transizione digitale"],
  "Le segnalazioni si presentano in un'area del sito AgID.", "17", "Chiunque può presentare al difensore civico per il digitale")
C("inf-155", 3, "A chi ciascuna PA affida la transizione alla modalità operativa digitale?", "A un unico ufficio dirigenziale generale (Responsabile per la transizione digitale)",
  ["A un consulente esterno", "Al sindaco", "Al Garante privacy"],
  "Art. 17 CAD.", "17", "ciascuna pubblica amministrazione affida a un unico ufficio dirigenziale generale")
C("inf-156", 2, "Come formano le PA gli originali dei propri documenti?", "Con mezzi informatici", ["Su carta, con firma autografa", "Indifferentemente", "Solo tramite PEC"],
  "Art. 40 CAD.", "40", "Le pubbliche amministrazioni formano gli originali dei propri documenti")
C("inf-157", 3, "Dove la PA raccoglie atti, documenti e dati di un procedimento?", "In un fascicolo informatico", ["In un registro cartaceo", "Nella casella email del funzionario", "Nel sito istituzionale"],
  "Art. 41 CAD.", "41", "raccoglie in un fascicolo informatico gli atti, i documenti e i dati del procedimento")
C("inf-158", 3, "Una copia cartacea di un documento informatico firmato digitalmente ha la stessa efficacia dell'originale se:", "La conformità all'originale è attestata da un pubblico ufficiale autorizzato",
  ["È stampata a colori", "Riporta la data di stampa", "È firmata a mano da chiunque"],
  "Art. 23 CAD.", "23", "se la loro conformità all'originale in tutte le sue componenti è attestata da un pubblico ufficiale a ciò autorizzato")
C("inf-159", 3, "Le istanze presentate per via telematica alla PA sono valide anche quando l'istante è identificato con:", "SPID, carta d'identità elettronica o carta nazionale dei servizi",
  ["Un indirizzo email qualsiasi", "Il numero di telefono", "Una foto del documento"],
  "Art. 65 CAD.", "65", "quando l'istante o il dichiarante è identificato attraverso il sistema pubblico di identità digitale (SPID), la carta di identità elettronica o la carta nazionale dei servizi")
C("inf-160", 2, "Chi ha istituito il sistema SPID secondo il CAD?", "L'Agenzia per l'Italia digitale (AgID)", ["Il Ministero dell'interno", "L'INPS", "La Banca d'Italia"],
  "Art. 64, comma 2-bis.", "64", "è istituito, a cura dell'Agenzia per l'Italia digitale, il sistema pubblico per la gestione dell'identità digitale")
C("inf-161", 3, "Presso quale ministero è istituita l'Anagrafe nazionale della popolazione residente (ANPR)?", "Ministero dell'interno", ["Ministero della giustizia", "Ministero dell'economia", "Presidenza del Consiglio"],
  "Art. 62 CAD.", "62", "È istituita presso il Ministero dell'interno l'ANPR")
C("inf-162", 3, "Tra le soluzioni che la PA deve valutare prima di acquistare software, quale compare espressamente nel CAD?", "Software libero o a codice sorgente aperto",
  ["Software pirata", "Solo software proprietario", "Solo software sviluppato all'estero"],
  "Art. 68: valutazione comparativa tecnica ed economica.", "68", "c) software libero o a codice sorgente aperto")
C("inf-163", 4, "Cosa devono fare le PA titolari di programmi realizzati su loro specifiche?", "Rendere disponibile il codice sorgente sotto licenza aperta ad altre PA",
  ["Brevettarli", "Venderli all'estero", "Distruggerne il codice"],
  "Art. 69: riuso delle soluzioni.", "69", "hanno l'obbligo di rendere disponibile il relativo codice sorgente")
C("inf-164", 3, "Chi adotta le Linee guida con le regole tecniche per l'attuazione del CAD?", "L'AgID", ["Il Parlamento", "Il Garante privacy", "La Corte dei conti"],
  "Art. 71 CAD.", "71", "adotta Linee guida contenenti le regole tecniche e di indirizzo per l'attuazione del presente Codice")
C("inf-165", 3, "Qual è il nome dell'Indice nazionale dei domicili digitali delle imprese e dei professionisti?", "INI-PEC", ["ANPR", "IPA", "SPID"],
  "Art. 6-bis CAD.", "6-bis", "Indice nazionale dei domicili digitali (INI-PEC)")
D("inf-166", "Privacy", 3, "Qual è in Italia l'autorità di controllo prevista dal GDPR?", "Il Garante per la protezione dei dati personali", ["L'AgID", "L'ANAC", "L'AGCOM"],
  "Codice privacy, art. 2-bis.", "D.Lgs. 196/2003, art. 2-bis", PRIV, "L'Autorità di controllo di cui all'articolo 51 del regolamento è individuata nel Garante per la protezione dei dati personali")
D("inf-167", "Privacy", 4, "Da quanti componenti è costituito il Collegio del Garante privacy?", "Quattro, eletti due dalla Camera e due dal Senato", ["Cinque, nominati dal Governo", "Tre, nominati dal Presidente della Repubblica", "Sette, eletti dal Parlamento in seduta comune"],
  "Codice privacy, art. 153.", "D.Lgs. 196/2003, art. 153", PRIV, "Il Collegio è costituito da quattro componenti, eletti due dalla Camera dei deputati e due dal Senato")
D("inf-168", "Privacy", 4, "Per i minori di quale età il consenso ai servizi della società dell'informazione deve essere prestato da chi esercita la responsabilità genitoriale?", "Meno di 14 anni", ["Meno di 16 anni", "Meno di 18 anni", "Meno di 12 anni"],
  "Codice privacy, art. 2-quinquies.", "D.Lgs. 196/2003, art. 2-quinquies", PRIV, "è lecito a condizione che sia prestato da chi esercita la responsabilità genitoriale")
D("inf-169", "PA digitale", 3, "Secondo il CAD, cos'è la «copia per immagine su supporto informatico di documento analogico»?", "Un documento informatico con contenuto e forma identici a quelli del documento cartaceo da cui è tratto",
  ["Una fotografia qualsiasi del documento", "Un documento con lo stesso contenuto ma forma diversa", "Una stampa del documento informatico"],
  "La copia informatica di documento analogico ha invece solo il contenuto identico.", "D.Lgs. 82/2005 (CAD), art. 1", CAD, "copia per immagine su supporto informatico di documento analogico: il documento informatico avente contenuto e forma identici")
D("inf-170", "PA digitale", 3, "Le copie informatiche di atti originariamente cartacei, rilasciate da pubblici ufficiali nelle forme previste, sostituiscono l'originale?", "Sì, la loro esibizione sostituisce quella dell'originale",
  ["No, mai", "Solo se stampate", "Solo per atti privati"],
  "Art. 22 CAD.", "D.Lgs. 82/2005 (CAD), art. 22", CAD, "La loro esibizione e produzione sostituisce quella dell'originale")


# --- Blocco 7: protocolli di rete, architettura dei calcolatori, sistemi operativi (Ghio; Wikipedia) ---
def R(id, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, "Reti", liv, testo, giusta, sbagliate, spieg, GRF, GR, frase)
def H(id, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, "Hardware", liv, testo, giusta, sbagliate, spieg, GCF, GC, frase)

R("inf-171", 3, "A cosa serve il protocollo ARP?", "A conoscere l'indirizzo MAC di una destinazione partendo dal suo indirizzo IP", ["Ad assegnare indirizzi IP", "A tradurre nomi di dominio", "A cifrare i pacchetti"],
  "Il mittente invia una ARP request in broadcast.", "Il protocollo ARP serve per venire a sapere l'indirizzo MAC della destinazione partendo dal suo indirizzo IP")
R("inf-172", 2, "Quale protocollo assegna automaticamente a un host l'indirizzo IP e altri parametri di rete?", "DHCP", ["DNS", "ARP", "FTP"],
  "Dynamic Host Configuration Protocol.", "permette a un host di ottenere dinamicamente dal server DHCP vari parametri di configurazione, tra cui il proprio indirizzo IP")
R("inf-173", 3, "A cosa serve il NAT (Network Address Translation)?", "A collegare più host a Internet usando un unico indirizzo IP pubblico", ["A cifrare il traffico", "A risolvere i nomi di dominio", "A bloccare i virus"],
  "Gli host hanno indirizzi privati; il router ha l'indirizzo pubblico.", "è un modo per connettere ad Internet più host utilizzando un unico indirizzo IP")
R("inf-174", 3, "Cosa fa un hub con il segnale ricevuto da un nodo?", "Lo replica su tutte le altre interfacce", ["Lo invia solo al destinatario", "Lo cifra", "Lo scarta"],
  "Lo switch invece inoltra in base alla destinazione.", "il segnale elettrico proveniente da un nodo viene replicato su tutte le altre interfacce")
R("inf-175", 3, "Quale caratteristica ha il protocollo UDP?", "È non connesso e privo di controllo di flusso e congestione", ["Garantisce la consegna ordinata", "Apre la connessione con il three-way handshake", "Cifra i dati"],
  "Ha basso overhead e ritardi bassi: adatto a streaming e voce.", "Il protocollo UDP è privo dei controlli di flusso e di congestione")
R("inf-176", 3, "Con quale procedura il TCP apre una connessione?", "Three-way handshake (SYN, SYN-ACK, ACK)", ["Broadcast ARP", "DHCP discover", "Ping ICMP"],
  "Tre messaggi tra client e server.", "il TCP usa un three-way handshake")
R("inf-177", 2, "Come si chiama il router che un host usa per uscire dalla propria rete logica?", "Default gateway", ["Server DNS", "Proxy di stampa", "Access point"],
  "La consegna tra reti logiche diverse è affidata al router.", "L'host deve quindi conoscere almeno un default gateway, che è il router per uscire dalla rete logica")
R("inf-178", 2, "Quale di questi indirizzi IPv4 NON è valido?", "192.168.1.300", ["192.168.1.30", "10.0.0.1", "8.8.8.8"],
  "Ogni numero dell'indirizzo è compreso tra 0 e 255.", "ogni numero è compreso tra 0 e 255")
R("inf-179", 3, "Quale protocollo fornisce funzioni di controllo e segnalazione degli errori sul livello IP (usato anche dal ping)?", "ICMP", ["SMTP", "HTTP", "DHCP"],
  "Internet Control Message Protocol.", "L'Internet Control Message Protocol (ICMP) fornisce delle funzionalità di controllo sul livello IP")
R("inf-180", 2, "Qual è il livello più basso del modello OSI, che trasporta fisicamente i bit?", "Il livello fisico", ["Il livello di rete", "Il livello di trasporto", "Il livello applicazione"],
  "Livello 1.", "Il livello fisico (physical) è lo strato deputato al trasporto fisico dei bit")
R("inf-181", 2, "Cosa identifica l'indirizzo MAC?", "La scheda di rete", ["Il sito web", "L'utente", "Il sistema operativo"],
  "È un indirizzo di livello 2.", "L'indirizzo MAC permette di identificare la scheda")
R("inf-182", 4, "Un indirizzo IP con tutti 0 nel campo host cosa identifica?", "L'intera rete", ["Il router", "Il broadcast", "Un host qualsiasi"],
  "Con tutti 1 nel campo host si identifica invece il broadcast.", "indirizzi con tutti 0 nel campo host identificano l'intera rete")
H("inf-183", 3, "Quale registro della CPU contiene l'indirizzo della prossima istruzione da leggere?", "Il Program Counter (PC)", ["L'Instruction Register", "L'accumulatore", "Il registro di stato"],
  "Usato nella fase di fetch.", "il Program Counter (PC) contiene l'indirizzo di memoria della nuova istruzione da leggere")
H("inf-184", 2, "Che cos'è l'«instruction set» di un processore?", "L'insieme delle operazioni che il processore è in grado di eseguire", ["L'elenco dei programmi installati", "La memoria cache", "Il manuale d'uso"],
  "A ogni operazione corrisponde un'istruzione (es. ADD).", "L'instruction set è l'insieme delle operazioni che il processore è in grado di eseguire")
H("inf-185", 3, "Cosa caratterizza i processori RISC rispetto ai CISC?", "Completano un'istruzione in un colpo di clock, con un set di istruzioni più semplice", ["Hanno istruzioni più complesse e lente", "Non usano la memoria", "Funzionano solo in parallelo a un CISC"],
  "I CISC richiedono più colpi di clock per istruzione.", "completano un'istruzione in un solo colpo di clock")
H("inf-186", 4, "Quale tecnica usano i processori RISC per eseguire in parallelo le fasi di più istruzioni?", "La pipeline", ["Il DMA", "La memoria virtuale", "Il multitasking"],
  "Fasi standard: fetch, decode, operate, write.", "I processori con architettura RISC fanno uso delle pipeline")
H("inf-187", 3, "Cosa contengono le celle di una memoria RAM dinamica (DRAM)?", "Condensatori collegati tramite transistor", ["Flip-flop", "Dischi magnetici", "Fusibili"],
  "La SRAM usa invece flip-flop.", "Le celle di una memoria RAM dinamica contengono dei condensatori")
H("inf-188", 3, "Cosa indica un «hit» in una memoria cache?", "Che il dato richiesto è stato trovato in cache", ["Che la cache è piena", "Un errore di lettura", "Che il dato va letto dal disco"],
  "In caso di miss si accede alla memoria principale.", "h è la percentuale di accessi che avvengono con successo (hit) in cache")
H("inf-189", 2, "Cosa fa il processore nella fase di «fetch»?", "Legge dalla memoria la prossima istruzione", ["Esegue l'istruzione", "Scrive il risultato su disco", "Spegne le periferiche"],
  "Seguono le fasi di decodifica ed esecuzione.", "Durante la fase di fetch il processore legge una di queste istruzioni dalla memoria")
H("inf-190", 4, "Con quale rappresentazione i processori come l'8086 eseguono il calcolo binario degli interi con segno?", "Complemento a 2", ["Virgola mobile", "Codice Gray", "Esadecimale"],
  "Supporta anche il formato BCD.", "L'8086 supporta istruzioni per il calcolo binario (in complemento a 2)")
I("inf-191", "Sistemi operativi", 1, "Qual è il compito principale di un sistema operativo?", "Gestire le risorse hardware e software e fornire servizi ai programmi applicativi", ["Navigare in Internet", "Scrivere documenti", "Proteggere solo dai virus"],
  "Esempi: Windows, macOS, Linux.", "Sistema operativo", "Sistema-operativo", "che gestisce le risorse hardware e software della macchina")
I("inf-192", "Sistemi operativi", 2, "Un sistema operativo «monotasking»:", "Esegue un solo processo alla volta", ["Esegue più processi in parallelo", "Funziona solo in rete", "Non ha file system"],
  "Il multitasking esegue più compiti con una politica di scheduling.", "Sistema operativo", "Sistema-operativo", "monotasking, se in grado di eseguire un solo compito")
I("inf-193", "Sistemi operativi", 2, "Quale celebre sistema operativo a riga di comando di Microsoft era alla base di Windows 95/98?", "MS-DOS", ["Unix", "OS/2", "CP/M"],
  "Ne esiste una versione libera, FreeDOS.", "Sistema operativo", "Sistema-operativo", "L'esemplare più famoso è senz'altro l'MS-DOS di Microsoft")
I("inf-194", "Sistemi operativi", 2, "Come si chiama l'interprete di comandi che fa da interfaccia tra utente e sistema operativo?", "Shell", ["Kernel", "BIOS", "Driver"],
  "Può interpretare anche un semplice linguaggio di scripting.", "Sistema operativo", "Sistema-operativo", "un interprete di comandi che funzioni anche da interfaccia utente ovvero da Shell")
I("inf-195", "Sistemi operativi", 4, "Un kernel che integra al suo interno gestione della memoria, scheduler, file system e driver si dice:", "Monolitico", ["Microkernel", "Esokernel", "Distribuito"],
  "Il microkernel delega molte funzioni a moduli esterni.", "Sistema operativo", "Sistema-operativo", "Un kernel tradizionale, ovvero monolitico")
I("inf-196", "Reti", 2, "Come si chiama una rete che si estende all'interno di una città?", "MAN (Metropolitan Area Network)", ["LAN", "WAN", "PAN"],
  "La LAN è locale, la WAN geografica.", "Rete informatica", "Rete-informatica", "si parla di rete metropolitana o MAN (Metropolitan Area Network) se la rete si estende all'interno di una città")
I("inf-197", "Reti", 2, "Come si chiama una rete che copre un'area geografica molto estesa?", "WAN (Wide Area Network)", ["LAN", "MAN", "WLAN"],
  "Internet è l'interconnessione globale di reti.", "Rete informatica", "Rete-informatica", "si parla di rete geografica o WAN (Wide Area Network)")
I("inf-198", "Reti", 2, "In un'architettura peer-to-peer:", "Tutti i dispositivi hanno le stesse capacità e possono inviare e ricevere dati", ["Un server centrale serve tutti i client", "Solo un nodo può trasmettere", "Non serve alcuna rete"],
  "Si contrappone all'architettura client-server.", "Rete informatica", "Rete-informatica", "In questa architettura tutti i dispositivi connessi alla rete hanno le stesse capacità")
I("inf-199", "Reti", 3, "Cosa rappresenta la topologia di una rete?", "Il modello geometrico delle connessioni tra i nodi", ["La velocità della rete", "Il costo dei cavi", "Il numero di utenti connessi"],
  "Esempi: a stella, ad anello, a bus, a maglia.", "Rete informatica", "Rete-informatica", "La topologia di rete è il modello geometrico (grafo)")
I("inf-200", "Reti", 2, "In un'architettura client-server, chi fornisce il servizio?", "Il server, su richiesta del client", ["Il client, su richiesta del server", "Tutti i nodi allo stesso modo", "Il router"],
  "Esempio: browser (client) e server web.", "Rete informatica", "Rete-informatica", "Spesso le reti informatiche sono organizzate sotto un'architettura client-server")

# --- Ampliamento a 300: sicurezza, reti, architettura, CAD, GDPR, servizi digitali ---
I("inf-201", "Sicurezza", 3, "Quale celebre malware fu usato per sabotare e distruggere attrezzature industriali specifiche?",
  "Stuxnet", ["ILOVEYOU", "WannaCry", "Melissa"],
  "È citato come esempio di malware usato per sabotaggio, non per guadagno diretto.", "Malware", "Malware", "Un esempio di sabotaggio è stato Stuxnet")
I("inf-202", "Sicurezza", 3, "Come si chiamano i computer infettati usati all'insaputa del proprietario per inviare spam o attacchi DoS?",
  "Computer zombie", ["Honeypot", "Server proxy", "Thin client"],
  "Insieme formano reti di macchine controllate da remoto.", "Malware", "Malware", "Computer zombie per l'invio di email di Spam")
I("inf-203", "Sicurezza", 3, "Qual è il canale di diffusione del malware più usato dai criminali?",
  "Internet, soprattutto tramite e-mail e World Wide Web", ["I CD-ROM", "Le reti telefoniche analogiche", "Le stampanti di rete"],
  "Per questo servono firewall e antivirus su ogni computer collegato.", "Malware", "Malware", "Il canale di diffusione più usato dai criminali è Internet: principalmente tramite e-mail e World Wide Web")
I("inf-204", "Sicurezza", 4, "Un software che danneggia un sistema per un difetto involontario è un malware?",
  "No: il malware è caratterizzato dall'intento malevolo", ["Sì, sempre", "Sì, se è un software libero", "Solo se si diffonde via rete"],
  "Il malware agisce contro le necessità dell'utente in modo intenzionale.", "Malware", "Malware", "Un malware è caratterizzato dal suo intento malevolo")
I("inf-205", "Sicurezza", 3, "Nella sicurezza informatica, cosa si intende per «vulnerabilità»?",
  "Una debolezza di un sistema che può essere sfruttata da una minaccia", ["Un attacco già avvenuto", "Una copia di backup danneggiata", "Un software antivirus scaduto"],
  "Può riguardare hardware, software, configurazione o procedure; viene sfruttata anche tramite exploit.", "Sicurezza informatica", "Sicurezza-informatica", "Una vulnerabilità è una debolezza presente in un sistema informatico")
I("inf-206", "Sicurezza", 3, "In funzione di quali due fattori si esprime generalmente il rischio informatico?",
  "Impatto e probabilità dell'evento", ["Costo e durata", "Velocità e banda", "Numero di utenti e di server"],
  "Il rischio è la possibilità che una minaccia sfrutti una vulnerabilità.", "Sicurezza informatica", "Sicurezza-informatica", "l'impatto, cioè l'entità del danno che deriverebbe dall'evento, e la probabilità che l'evento si verifichi")
I("inf-207", "Sicurezza", 4, "Quale standard definisce i requisiti di un sistema di gestione della sicurezza delle informazioni?",
  "ISO/IEC 27001", ["ISO 9001", "IEEE 802.11", "ISO/IEC 42001"],
  "Prevede un processo di gestione del rischio; la ISO/IEC 42001 riguarda invece l'IA.", "Sicurezza informatica", "Sicurezza-informatica", "Lo standard ISO/IEC 27001 definisce i requisiti di un sistema di gestione della sicurezza delle informazioni")
I("inf-208", "Sicurezza", 4, "Cosa indica l'acronimo SPOF nella progettazione dei sistemi?",
  "Single point of failure: un componente il cui guasto blocca l'intero sistema", ["Un protocollo di posta sicura", "Un tipo di firewall", "Un formato di backup"],
  "Per evitarlo si usano ridondanza e architetture adeguate.", "Sicurezza informatica", "Sicurezza-informatica", "single point of failure (SPOF)")
I("inf-209", "Sicurezza", 3, "Quale configurazione dei dischi aumenta la tolleranza ai guasti dei dispositivi di archiviazione?",
  "RAID", ["FAT32", "BIOS", "DHCP"],
  "È un esempio di ridondanza a favore della disponibilità.", "Sicurezza informatica", "Sicurezza-informatica", "Un esempio è rappresentato dalle configurazioni RAID")
I("inf-210", "Sicurezza", 3, "Cosa si intende per «resilienza» di un sistema informatico?",
  "La capacità di continuare a fornire i servizi o ripristinarli rapidamente dopo un guasto", ["La velocità di calcolo", "La capacità di cifrare i dati", "Il numero di utenti collegabili"],
  "È strettamente legata alla disponibilità.", "Sicurezza informatica", "Sicurezza-informatica", "il concetto di resilienza")
I("inf-211", "Sicurezza", 3, "Quali strumenti tutelano l'integrità dei dati?",
  "Funzioni di hash (es. SHA), firme digitali e controllo delle modifiche", ["Solo il backup su nastro", "Solo la password del Wi-Fi", "La compressione ZIP"],
  "L'integrità garantisce che i dati non siano alterati in modo non autorizzato.", "Sicurezza informatica", "Sicurezza-informatica", "meccanismi basati sulle funzioni di hash, come gli algoritmi della famiglia SHA")
I("inf-212", "Sicurezza", 3, "Qual è il significato originario della parola «firewall»?",
  "Muro tagliafuoco", ["Porta blindata", "Cavo schermato", "Antenna di rete"],
  "Indicava un muro destinato a confinare un incendio all'interno di un edificio.", "Firewall", "Firewall", "muro tagliafuoco")
I("inf-213", "Sicurezza", 4, "Come si chiamava la prima generazione di firewall, che filtrava i pacchetti in base all'intestazione?",
  "Packet filter (stateless) firewall", ["Application gateway", "Next generation firewall", "Proxy inverso"],
  "Il primo esemplare fu sviluppato nel 1988 dalla Digital Equipment Corporation.", "Firewall", "Firewall", "La prima generazione fu quella dei packet filter firewall o stateless firewall")
I("inf-214", "Sicurezza", 4, "Cosa introdusse la seconda generazione di firewall (stateful)?",
  "La possibilità di salvare e monitorare lo stato di una connessione", ["Il filtro antispam", "La cifratura dei dischi", "Il controllo parentale"],
  "Il primo stateful firewall fu sviluppato tra il 1989 e il 1990 ai Bell Laboratories.", "Firewall", "Firewall", "la possibilità di salvare e monitorare lo stato di una connessione")
I("inf-215", "Sicurezza", 4, "Fino a quale livello del modello OSI proteggono gli application firewall (proxy firewall)?",
  "Fino al livello applicativo (livello 7)", ["Solo il livello fisico", "Fino al livello di rete (3)", "Fino al livello di trasporto (4)"],
  "Riescono a individuare minacce dentro il traffico web.", "Firewall", "Firewall", "fino al livello applicativo (livello 7) del modello OSI")
I("inf-216", "Sicurezza", 3, "Contro quale minaccia un backup può risultare particolarmente utile?",
  "I ransomware", ["Lo spam", "Il phishing vocale", "I cookie di terze parti"],
  "Con una copia di riserva si possono ripristinare i dati cifrati dal ransomware.", "Backup", "Backup", "Un backup può anche risultare utile per proteggersi dai ransomware")
I("inf-217", "Sicurezza", 3, "A quale processo appartiene il backup nella sicurezza informatica?",
  "Al disaster recovery", ["Al phishing", "Al load balancing", "Al routing"],
  "Crea ridondanza delle informazioni per poterle ripristinare.", "Backup", "Backup", "si indica un processo di disaster recovery")
I("inf-218", "Sicurezza", 4, "Come si chiama, nei programmi di backup, la singola esecuzione programmata o manuale di un backup?",
  "Job", ["Thread", "Ticket", "Token"],
  "Indica una determinata sessione di backup in un dato momento.", "Backup", "Backup", "utilizzano spesso il termine job")
I("inf-219", "Cloud", 3, "Cosa si intende per «multicloud»?",
  "L'uso di servizi cloud acquisiti da almeno due provider distinti e autonomi", ["Un cloud con più data center dello stesso fornitore", "Un cloud solo privato", "Un cloud senza connessione Internet"],
  "Ad esempio un'organizzazione che usa sia Microsoft sia Amazon o Google.", "Cloud computing", "Cloud-computing", "i servizi sono acquisiti dall'organizzazione utilizzatrice da almeno due provider distinti e autonomi")
I("inf-220", "Cloud", 3, "Cosa caratterizza il «cloud ibrido»?",
  "È una soluzione mista di cloud pubblico e privato", ["È solo pubblico", "Funziona solo offline", "È riservato alle PA"],
  "Può comprendere anche un datacenter on premise.", "Cloud computing", "Cloud-computing", "cloud ibrido ⇒ soluzione mista di pubblico e privato")
I("inf-221", "Cloud", 4, "Quale direttiva UE definisce il cloud come servizio che consente l'amministrazione su richiesta di un pool scalabile ed elastico di risorse?",
  "La direttiva NIS2 (UE 2022/2555)", ["Il GDPR", "La direttiva e-Privacy", "Il regolamento eIDAS"],
  "Precisa anche che un datacenter non è necessariamente cloud.", "Cloud computing", "Cloud-computing", "La direttiva UE 2022/2555 NIS2 definisce")
I("inf-222", "Sicurezza", 4, "Quale macchina cifrante tedesca della Seconda guerra mondiale fu forzata già nel 1932 dai crittografi polacchi?",
  "Enigma", ["Purple", "Lorenz", "Magic"],
  "Anche gli inglesi decifrarono più volte i messaggi tedeschi.", "Crittografia", "Crittografia", "La Germania nazista considerava inattaccabile la sua macchina Enigma")
I("inf-223", "Sicurezza", 4, "Quale cifrario, perfezionato da Gilbert Vernam nel 1918, usa chiavi casuali lunghe quanto il messaggio?",
  "Il cifrario di Vernam (one-time pad)", ["Il cifrario di Cesare", "L'RSA", "L'AES"],
  "Claude Shannon dimostrò nel 1949 che è l'unico metodo totalmente sicuro.", "Crittografia", "Crittografia", "chiavi segrete casuali lunghe almeno quanto il messaggio")
I("inf-224", "Sicurezza", 3, "Come si chiama lo studio volto a rompere un meccanismo crittografico?",
  "Crittoanalisi", ["Steganografia", "Compressione", "Hashing"],
  "Insieme alla crittografia forma la crittologia.", "Crittografia", "Crittografia", "è detto invece crittoanalisi")
I("inf-225", "Sicurezza", 4, "Chi è considerato il padre della teoria dell'informazione?",
  "Claude Shannon", ["Alan Turing", "John von Neumann", "Tim Berners-Lee"],
  "Nel 1949 pubblicò un lavoro sulla teoria della comunicazione nei sistemi crittografici.", "Crittografia", "Crittografia", "Claude Shannon, padre della teoria dell'informazione")
I("inf-226", "Software", 3, "Quale sistema operativo, sviluppato da AT&T, circolava liberamente nelle università americane fino al 1984?",
  "Unix", ["MS-DOS", "Linux", "macOS"],
  "Dopo il frazionamento di AT&T la società ricominciò a venderlo.", "Software libero", "Software-libero", "Unix, quindi, era il software libero utilizzato nelle università americane")
I("inf-227", "Software", 4, "Quale legge statunitense del 1980 estese la tutela del diritto d'autore al software?",
  "Il Software Copyright Act", ["Il Bayh-Dole Act", "Il Digital Millennium Copyright Act", "Il Patriot Act"],
  "Da allora copia, modifica e distribuzione dei programmi divennero facoltà esclusive dell'autore: nacque il software proprietario.", "Software libero", "Software-libero", "nel 1980, viene emessa la US Software Copyright Act")
I("inf-228", "Posta elettronica", 3, "Per quanto tempo i gestori PEC conservano la traccia informatica delle ricevute, con lo stesso valore legale?",
  "Trenta mesi", ["Sei mesi", "Dieci anni", "Un anno"],
  "Serve in caso di smarrimento delle ricevute.", "Posta elettronica certificata", "Posta-elettronica-certificata", "per un periodo di trenta mesi")
I("inf-229", "Posta elettronica", 4, "Quale decreto del Presidente della Repubblica fissa le regole della PEC?",
  "Il D.P.R. n. 68/2005", ["Il D.P.R. n. 445/2000", "Il D.P.R. n. 62/2013", "Il D.P.R. n. 600/1973"],
  "Le regole tecniche sono allegate al D.M. 2 novembre 2005.", "Posta elettronica certificata", "Posta-elettronica-certificata", "Decreto del presidente della Repubblica n. 68/2005")
I("inf-230", "Posta elettronica", 4, "Con quale protocollo è trasmessa la PEC dal 2024, con autenticazione a due fattori?",
  "REM", ["SMTP semplice", "FTP", "POP3"],
  "Il protocollo REM qualifica l'identità di mittente e destinatario con SPID o CIE.", "Posta elettronica certificata", "Posta-elettronica-certificata", "è trasmessa col protocollo REM")
I("inf-231", "Posta elettronica", 3, "Cosa riceve il mittente dal proprio gestore PEC al momento dell'invio?",
  "Una ricevuta con valore legale dell'avvenuta (o mancata) trasmissione", ["Una copia cartacea del messaggio", "La conferma di lettura del destinatario", "Una fattura elettronica"],
  "Il gestore del destinatario invia poi la ricevuta di avvenuta consegna.", "Posta elettronica certificata", "Posta-elettronica-certificata", "una ricevuta che costituirà valore legale dell'avvenuta (o mancata) trasmissione del messaggio")
I("inf-232", "PA digitale", 4, "Su proposta di quale deputato iniziarono nel 2013 i lavori del sistema SPID?",
  "Stefano Quintarelli", ["Alessio Butti", "Diego Piacentini", "Paola Pisano"],
  "Divenne poi presidente del comitato di indirizzo dell'AgID.", "SPID", "SPID", "su proposta del deputato Stefano Quintarelli")
I("inf-233", "PA digitale", 4, "Quali furono i primi tre gestori di identità SPID accreditati da AgID nel dicembre 2015?",
  "InfoCert, Poste Italiane e Telecom Italia Trust Technologies", ["Aruba, Sielte e Namirial", "Register.it, Lepida e Intesa", "TIM, Vodafone e Wind"],
  "Aruba e Sielte furono accreditati nel 2016, Namirial e Register.it nel 2017.", "SPID", "SPID", "InfoCert S.p.A., Poste Italiane S.p.A. e Telecom Italia Trust Technologies S.r.l.")
I("inf-234", "PA digitale", 4, "Per quali servizi possono usare lo SPID i minori tra 5 e 14 anni, secondo le linee guida AgID del 2022?",
  "Solo per i servizi scolastici", ["Per tutti i servizi", "Solo per i servizi sanitari", "Non possono usarlo"],
  "Gli over 14 possono accedere a tutti i servizi che li riguardano.", "SPID", "SPID", "dai 5 anni fino ai 14 può essere utilizzato solo per l'accesso ai servizi scolastici")
I("inf-235", "PA digitale", 3, "Con quale decreto fu attuato per la prima volta il sistema SPID?",
  "Il DPCM 24 ottobre 2014", ["Il D.Lgs. 82/2005", "La L. 241/1990", "Il D.P.R. 68/2005"],
  "Fu pubblicato in Gazzetta Ufficiale il 9 dicembre 2014.", "SPID", "SPID", "decreto del Presidente del Consiglio dei Ministri del 24 ottobre 2014")
I("inf-236", "Reti", 3, "Su quale famiglia di standard si basa il Wi-Fi?",
  "IEEE 802.11", ["IEEE 802.3", "Bluetooth", "ISO 9660"],
  "La prima versione del protocollo 802.11 è del 1997.", "Wi-Fi", "Wi-Fi", "rappresenta il marchio commerciale utilizzato per indicare la famiglia di protocolli IEEE 802.11")
I("inf-237", "Reti", 4, "Quale velocità massima consentiva lo standard 802.11b del 1999?",
  "11 Mbit/s", ["2 Mbit/s", "54 Mbit/s", "1 Gbit/s"],
  "La prima versione 802.11 del 1997 arrivava a 2 Mbit/s.", "Wi-Fi", "Wi-Fi", "velocità di collegamento fino a 11 Mbit/s")
I("inf-238", "Reti", 3, "«Wi-Fi» è l'acronimo ufficiale di «Wireless Fidelity»?",
  "No, è un marchio commerciale senza significato tecnico", ["Sì, è l'acronimo ufficiale", "Significa «Wide Field»", "Significa «Wireless Firewall»"],
  "Il nome fu coniato dalla società Interbrand per la Wi-Fi Alliance.", "Wi-Fi", "Wi-Fi", "il termine Wi-Fi non ha alcun significato")
I("inf-239", "Reti", 3, "Qual è la portata indicativa di un access point Wi-Fi all'interno di un edificio?",
  "Circa 20 metri", ["Circa 2 metri", "Circa 500 metri", "Circa 5 chilometri"],
  "All'esterno può coprire un raggio di circa 100 metri.", "Wi-Fi", "Wi-Fi", "può avere una portata di circa 20 metri")
I("inf-240", "Hardware", 3, "Qual è la tensione di alimentazione prevista dallo standard USB di base?",
  "5 volt", ["12 volt", "220 volt", "1,5 volt"],
  "Con USB Power Delivery si possono richiedere tensioni maggiori.", "USB", "USB", "La tensione di alimentazione prevista dallo standard di base è 5 volt")
I("inf-241", "Hardware", 3, "Cosa significa che con USB si può fare «hot swap»?",
  "Che si possono collegare e scollegare periferiche senza riavviare il computer", ["Che i cavi si scaldano", "Che i dati vengono cifrati", "Che serve un driver per ogni porta"],
  "Migliora la funzionalità plug and play.", "USB", "USB", "senza dover riavviare il computer (hot swap)")
I("inf-242", "Hardware", 4, "Quale fu il primo prodotto di largo consumo con USB, nel 1998?",
  "L'iMac G3 di Apple", ["L'IBM PC", "Il Commodore 64", "Il Nintendo 64"],
  "Apple rimosse le porte legacy, spingendo la diffusione dello standard.", "USB", "USB", "Nel 1998 l'iMac G3 è stato il primo prodotto mainstream con USB")
I("inf-243", "Hardware", 4, "Quando è stata introdotta la specifica USB 1.0?",
  "Nel gennaio 1996", ["Nel 1989", "Nel 2000", "Nel 2008"],
  "USB 2.0 è dell'aprile 2000, USB 3.0 del novembre 2008.", "USB", "USB", "La specifica USB 1.0 è stata introdotta nel gennaio 1996")
I("inf-244", "Intelligenza artificiale", 3, "Quale architettura, introdotta nel 2017, ha dato un forte impulso all'IA generativa?",
  "Transformer", ["Von Neumann", "RISC", "Client-server"],
  "Dal 2012 le GPU avevano già permesso al deep learning di superare le tecniche precedenti.", "Intelligenza artificiale", "Intelligenza-artificiale", "con l'introduzione dell'architettura Transformer")
I("inf-245", "Intelligenza artificiale", 3, "Come si chiamano i periodi storici di riduzione dei finanziamenti alla ricerca sull'IA?",
  "Inverni dell'IA", ["Bolle dell'IA", "Ere glaciali digitali", "Crisi del silicio"],
  "Il settore ha conosciuto molti alti e bassi dal 1956.", "Intelligenza artificiale", "Intelligenza-artificiale", "inverni dell'IA")
I("inf-246", "Intelligenza artificiale", 3, "Come si chiama l'ipotetica IA capace di eguagliare o superare le capacità cognitive umane in ogni ambito?",
  "IA generale (AGI)", ["IA debole", "IA ristretta", "Sistema esperto"],
  "Tutti i sistemi oggi esistenti sono IA debole, specializzata in compiti specifici.", "Intelligenza artificiale", "Intelligenza-artificiale", "l'IA generale (AGI)")
I("inf-247", "Intelligenza artificiale", 4, "Quale standard internazionale disciplina la certificazione dei sistemi di gestione dell'IA?",
  "ISO/IEC 42001:2023", ["ISO/IEC 27001", "ISO 14001", "IEEE 754"],
  "Riguarda gli AI Management Systems (AIMS).", "Intelligenza artificiale", "Intelligenza-artificiale", "Lo standard internazionale ISO/IEC 42001:2023")
I("inf-248", "Internet", 3, "Quali erano i quattro nodi originari di ARPANET nel 1969?",
  "UCLA, SRI di Stanford, UC Santa Barbara e Università dello Utah", ["MIT, Harvard, Yale e Princeton", "CERN, MIT, IBM e Bell Labs", "Quattro basi militari"],
  "L'ampiezza di banda era di 50 kbps.", "Internet", "Internet", "collegando quattro nodi: l'Università della California di Los Angeles")
I("inf-249", "Internet", 4, "Quale agenzia statunitense finanziò il progetto ARPANET?",
  "La DARPA, dipendente dal Dipartimento della Difesa", ["La NASA", "La NSA", "Il CERN"],
  "L'agenzia si occupava di progetti di ricerca avanzata per la difesa.", "Internet", "Internet", "Defence Advanced Research Projects Agency")
I("inf-250", "Internet", 4, "Quale nome diedero Licklider e Clark nel 1962 alla rete di computer mondiale da loro teorizzata?",
  "Intergalactic Computer Network", ["World Wide Web", "Usenet", "Ethernet"],
  "Erano ricercatori del MIT.", "Internet", "Internet", "Intergalactic Computer Network")
I("inf-251", "Internet", 4, "Quale legge statunitense del 1991 aprì Internet allo sfruttamento commerciale privato?",
  "L'High performance computing act", ["Il Telecommunications Act", "Il Patriot Act", "Il Digital Millennium Copyright Act"],
  "Fino ad allora la rete era di proprietà statale e destinata al mondo scientifico.", "Internet", "Internet", "High performance computing act")
I("inf-252", "Privacy", 3, "Quale direttiva europea è stata sostituita dal GDPR?",
  "La direttiva 95/46/CE", ["La direttiva 2002/58/CE", "La direttiva NIS2", "La direttiva 2019/790"],
  "In Italia il GDPR ha abrogato le norme incompatibili del Codice privacy.", "Regolamento generale sulla protezione dei dati", "Regolamento-generale-sulla-protezione-dei-dati", "Direttiva 95/46/CE")
I("inf-253", "Privacy", 3, "Fino a quale percentuale del volume d'affari globale possono arrivare le sanzioni del GDPR?",
  "Il 4%", ["Lo 0,5%", "Il 10%", "Il 25%"],
  "Il regime prevede una disciplina severa con sanzioni rilevanti.", "Regolamento generale sulla protezione dei dati", "Regolamento-generale-sulla-protezione-dei-dati", "possono raggiungere il 4% del volume globale di affari")
I("inf-254", "Privacy", 3, "Cosa si intende per «privacy by default»?",
  "Che le misure di tutela della privacy siano attuate per impostazione predefinita", ["Che i dati siano pubblici per impostazione predefinita", "Che il consenso sia sempre presunto", "Che la privacy valga solo su richiesta"],
  "La «privacy by design» richiede invece che i requisiti privacy entrino nella progettazione.", "Regolamento generale sulla protezione dei dati", "Regolamento-generale-sulla-protezione-dei-dati", "la privacy by default (le misure privacy devono essere attuate per impostazione predefinita)")
I("inf-255", "Privacy", 4, "Quale principio del GDPR (art. 24) indica il dovere del titolare di dar conto delle misure adottate?",
  "Accountability (responsabilizzazione)", ["Trasparenza passiva", "Interoperabilità", "Minimizzazione della pena"],
  "Il titolare deve poter dimostrare la conformità del trattamento.", "Regolamento generale sulla protezione dei dati", "Regolamento-generale-sulla-protezione-dei-dati", "il concetto di accountability")
I("inf-256", "Privacy", 4, "Con quale decreto l'Italia ha adeguato il Codice privacy al GDPR?",
  "Il D.Lgs. 10 agosto 2018, n. 101", ["Il D.Lgs. 82/2005", "La L. 675/1996", "Il D.Lgs. 33/2013"],
  "La prima legge italiana sulla privacy era la L. 675/1996.", "Regolamento generale sulla protezione dei dati", "Regolamento-generale-sulla-protezione-dei-dati", "decreto legislativo n. 101 del 10 agosto 2018")
I("inf-257", "Privacy", 4, "Quale saggio del 1890 di Warren e Brandeis definì la privacy come «the right to be let alone»?",
  "The Right to Privacy", ["Nineteen Eighty-Four", "On Liberty", "The Data Protection Act"],
  "Fu pubblicato sulla Harvard Law Review.", "Regolamento generale sulla protezione dei dati", "Regolamento-generale-sulla-protezione-dei-dati", "The Right to Privacy rappresenta la pietra angolare")

R("inf-258", 3, "A cosa serve il campo TTL (Time To Live) nell'intestazione di un pacchetto IP?",
  "È un contatore di hop decrementato a ogni router: a zero il pacchetto viene scartato", ["Indica l'ora di invio del pacchetto", "Indica la priorità del traffico", "Contiene la password di rete"],
  "Evita che i pacchetti vaghino all'infinito; lo sfrutta il comando traceroute.", "è un contatore di hop")
R("inf-259", 4, "Nell'intestazione IPv4, cosa protegge il campo checksum?",
  "Solo l'intestazione", ["L'intero pacchetto", "Solo il payload", "Nulla, è facoltativo"],
  "Gli errori nel payload sono gestiti dai livelli superiori.", "checksum: protegge solo l'intestazione")
R("inf-260", 3, "Quale apparato interconnette reti a livello 3 e implementa IP?",
  "Il router", ["L'hub", "Il repeater", "Il bridge"],
  "Hub e repeater lavorano al livello 1, bridge e switch al livello 2, il gateway al livello 7.", "router: interconnette reti di livello 3, e implementa IP")
R("inf-261", 3, "A quale livello lavorano bridge e switch?",
  "Al livello 2 (collegamento)", ["Al livello 1 (fisico)", "Al livello 3 (rete)", "Al livello 7 (applicazione)"],
  "Devono gestire gli indirizzi MAC.", "bridge o switch1 : interconnette reti di livello 2")
R("inf-262", 4, "Che effetto ha collegare due domini di collisione con un repeater?",
  "Si crea un unico dominio di collisione", ["Si separano le collisioni", "Si raddoppia la banda", "Si filtra il traffico per indirizzo MAC"],
  "Il repeater si limita a rigenerare e trasmettere i bit.", "L'interconnessione di due domini di collisione crea un unico dominio di collisione")
R("inf-263", 3, "A quale livello del modello OSI appartiene il protocollo IP?",
  "Al livello di rete", ["Al livello di collegamento", "Al livello di trasporto", "Al livello di presentazione"],
  "IP è un servizio non connesso di tipo datagram.", "L'Internet Protocol (IP) è il livello di rete di TCP/IP")
R("inf-264", 3, "Che tipo di servizio offre il protocollo IP?",
  "Non connesso, basato su datagrammi", ["Connesso e affidabile", "Circuito dedicato", "Solo broadcast"],
  "Affidabilità e controllo di flusso sono demandati al livello di trasporto (TCP).", "è un servizio non connesso")
R("inf-265", 4, "Chi effettua il riassemblaggio dei pacchetti IP frammentati?",
  "La destinazione finale", ["Ogni router lungo il percorso", "Il primo router", "Il server DNS"],
  "I router effettuano solo la frammentazione.", "il riassemblaggio è delegato alla destinazione")
R("inf-266", 3, "Cosa fa il subnetting?",
  "Crea reti logiche più piccole usando parte del campo host come campo subnet", ["Unisce più reti in un'unica rete fisica", "Cifra gli indirizzi IP", "Assegna indirizzi MAC"],
  "La subnet mask indica quali bit appartengono al prefisso di rete.", "una parte del campo host diventa il campo subnet")
R("inf-267", 3, "Come è fatto il doppino usato nelle reti?",
  "Da due fili di rame intrecciati per ridurre le interferenze", ["Da una fibra di vetro", "Da un filo centrale schermato da una maglia", "Da due cavi coassiali paralleli"],
  "La versione UTP non ha schermature; il cavo coassiale ha invece un filo centrale schermato.", "Il doppino è costituito da due fili di rame intrecciati")
R("inf-268", 4, "Quale categoria di doppino supporta reti locali fino a 1 Gb/s?",
  "La categoria 5e", ["La categoria 3", "La categoria 1", "La categoria 4"],
  "La categoria 5 arriva a 100 Mb/s.", "5e. reti locali fino a 1 Gb/s")
R("inf-269", 3, "A cosa serve il protocollo POP3?",
  "Al recupero della posta elettronica dal server", ["All'invio della posta tra server", "Alla risoluzione dei nomi", "Al trasferimento di pagine web"],
  "IMAP migliora POP3, che è stateless.", "serve per il recupero della posta elettronica dal server di posta")
R("inf-270", 4, "Quale funzione del DNS consente di associare più indirizzi IP allo stesso nome per bilanciare il carico?",
  "Load distribution", ["Host aliasing", "Mail server aliasing", "Reverse lookup"],
  "Il DNS è un database distribuito.", "load distribution: allo stesso nome possono essere associati più indirizzi IP")
R("inf-271", 4, "In una topologia a stella attiva, qual è il principale svantaggio?",
  "La vulnerabilità ai guasti del centro stella", ["La complessità di controllo", "L'assenza di un nodo centrale", "La comunicazione sempre broadcast"],
  "Tutte le informazioni passano attraverso il centro stella.", "Svantaggio vulnerabilità ai guasti del centro stella")

H("inf-272", 3, "In quali tre bus è diviso il bus esterno tra processore e memoria?",
  "Bus dati, bus indirizzi e bus di controllo", ["Bus video, bus audio e bus rete", "Bus USB, bus PCI e bus SATA", "Bus seriale, parallelo e misto"],
  "Il registro MAR passa alla memoria l'indirizzo della cella da leggere.", "bus dati, bus indirizzi e bus di controllo")
H("inf-273", 3, "Come vengono cancellate le memorie EPROM per essere riprogrammate?",
  "Con raggi ultravioletti", ["Elettricamente byte per byte", "Con un campo magnetico", "Non possono essere riprogrammate"],
  "Le EEPROM invece si riprogrammano senza raggi ultravioletti.", "la cancellazione avviene grazie a raggi ultra-violetti")
H("inf-274", 4, "Che caratteristica hanno le operazioni di scrittura nelle memorie flash?",
  "Avvengono a blocchi, e il blocco va cancellato prima di essere riscritto", ["Avvengono bit per bit senza cancellazione", "Richiedono raggi ultravioletti", "Sono impossibili"],
  "Sono la base di chiavette USB e SSD.", "Le memorie flash richiedono delle operazioni di scrittura a blocchi")
H("inf-275", 4, "Quanti transistor richiede ogni cella di una RAM statica (SRAM)?",
  "Sei", ["Uno", "Due", "Otto"],
  "Una RAM dinamica usa un condensatore e un transistor per bit, ed è più densa.", "Ogni cella di una memoria RAM statica richiede 6 transistor")
H("inf-276", 3, "Cosa si intende per «località dei riferimenti» delle memorie?",
  "Che i programmi accedono per un certo tempo solo a zone limitate della memoria", ["Che la memoria è sempre vicina al processore", "Che i dati sono salvati in locale e non nel cloud", "Che ogni cella ha un indirizzo univoco"],
  "Su questo principio si basano cache e memoria virtuale.", "Le memorie sono caratterizzate dalla località dei riferimenti")
H("inf-277", 4, "Nella politica di cache «write-through»:",
  "il processore scrive contemporaneamente in memoria e in cache", ["si scrive solo in cache", "si scrive solo in memoria", "si scrive su disco"],
  "Nel write-back i dati modificati vanno in memoria solo prima che la linea venga sovrascritta.", "write-through: il processore scrive parallelamente sia in memoria sia in cache")
H("inf-278", 3, "Come si chiamano i blocchi in cui è suddivisa la memoria virtuale?",
  "Pagine", ["Settori", "Cluster", "Tracce"],
  "Sono grandi da 1 KB a 64 KB.", "La memoria virtuale è suddivisa in blocchi detti pagine")
H("inf-279", 4, "Quale componente hardware converte gli indirizzi logici del processore in indirizzi fisici nella memoria virtuale?",
  "La MMU (Memory Management Unit)", ["L'ALU", "Il DMA Controller", "Il Program Counter"],
  "Il processore vede un'unica memoria grande quanto la memoria complessiva.", "detto Memory Management Unit (MMU)")
H("inf-280", 4, "A cosa serve il DMA Controller?",
  "A trasferire grandi quantità di dati tra periferica e memoria senza passare dal processore", ["A gestire la cache di primo livello", "A eseguire calcoli in virgola mobile", "A generare il clock"],
  "Il DMA Controller può diventare bus master, con arbitraggio del bus.", "in grado di gestire il trasferimento di grosse moli di dati tra una periferica e la memoria")
H("inf-281", 3, "Cos'è il «polling» nella gestione dell'input/output?",
  "Il processore controlla ripetutamente se la periferica è pronta", ["La periferica interrompe il processore", "Il trasferimento diretto in memoria", "La compressione dei dati"],
  "Svantaggio: il processore resta impegnato nel ciclo di attesa.", "Il processore campiona (= polling) il segnale di ready")
H("inf-282", 4, "Con quale rappresentazione l'8086 memorizza un numero su 2 byte?",
  "Little endian: il byte meno significativo precede quello più significativo", ["Big endian", "In BCD", "In complemento a 1"],
  "Ogni istruzione in codice macchina occupa da 1 a 6 byte.", "con la rappresentazione little endian")
H("inf-283", 4, "Che cos'è un'unità di controllo «cablata» (hardwired)?",
  "Un circuito sequenziale che genera i segnali di controllo con flip-flop e rete combinatoria", ["Un'unità programmata con microistruzioni in memoria", "Un cavo che collega CPU e RAM", "Un controller di rete"],
  "L'alternativa è l'unità di controllo microprogrammata.", "L'unità di controllo cablata (o hardwired) è un circuito sequenziale")
H("inf-284", 3, "Quali sono le due capacità principali di un processore?",
  "Elaborare istruzioni (fetch ed esecuzione) e interagire con l'esterno tramite le periferiche", ["Stampare e scansionare", "Memorizzare file e navigare", "Alimentare e raffreddare il computer"],
  "Reagisce alle richieste di interrupt provenienti dall'esterno.", "Il processore è un dispositivo capace di")

C("inf-285", 3, "A quale finalità sono rivolte le iniziative di «alfabetizzazione informatica dei cittadini» previste dal CAD?",
  "Diffondere la cultura digitale, con attenzione ai minori e alle categorie a rischio di esclusione", ["Insegnare la programmazione ai dipendenti pubblici", "Vendere computer a prezzo agevolato", "Certificare le competenze dei professionisti"],
  "Lo Stato può avvalersi anche del servizio radiotelevisivo.", "8", "promuovono iniziative volte a favorire la diffusione della cultura digitale tra i cittadini")
C("inf-286", 3, "Cosa favoriscono le PA secondo l'art. 9 del CAD (partecipazione democratica elettronica)?",
  "L'uso delle nuove tecnologie per una maggiore partecipazione dei cittadini al processo democratico", ["Il voto elettronico obbligatorio", "La chiusura degli sportelli fisici", "La pubblicazione dei dati sanitari"],
  "Anche con consultazioni telematiche preventive sugli schemi di atti.", "9", "per promuovere una maggiore partecipazione dei cittadini, anche residenti all'estero, al processo democratico")
C("inf-287", 3, "Quale ente è preposto alla realizzazione degli obiettivi dell'Agenda Digitale Italiana?",
  "L'Agenzia per l'Italia digitale (AgID)", ["Il Garante privacy", "L'ANAC", "La Consip"],
  "Opera in coerenza con l'Agenda digitale europea.", "14-bis", "L'Agenzia per l'Italia Digitale (AgID) è preposta alla realizzazione degli obiettivi dell'Agenda Digitale Italiana")
C("inf-288", 3, "Secondo il CAD, a quanti soggetti deve riferirsi la firma digitale?",
  "A un solo soggetto, in maniera univoca", ["A tutti i dipendenti dell'ufficio", "A due soggetti, firmatario e testimone", "A nessuno in particolare"],
  "Si riferisce anche al documento o all'insieme di documenti cui è apposta.", "24", "La firma digitale deve riferirsi in maniera univoca ad un solo soggetto")
C("inf-289", 3, "Cosa sostituisce l'apposizione della firma digitale?",
  "Sigilli, punzoni, timbri, contrassegni e marchi di qualsiasi genere", ["Solo la firma autografa", "Il protocollo informatico", "La marca da bollo"],
  "Art. 24, comma 2, del CAD.", "24", "integra e sostituisce l'apposizione di sigilli, punzoni, timbri, contrassegni e marchi")
C("inf-290", 4, "Quale certificato serve per generare una firma digitale valida?",
  "Un certificato qualificato non scaduto, né revocato o sospeso", ["Un certificato di residenza", "Un certificato SSL di un sito web", "Qualsiasi certificato autofirmato"],
  "Art. 24, comma 3, del CAD.", "24", "deve adoperarsi un certificato qualificato che, al momento della sottoscrizione, non risulti scaduto di validità")
C("inf-291", 3, "Quale obbligo ha il titolare di un certificato di firma digitale?",
  "Custodire il dispositivo di firma e utilizzarlo personalmente", ["Prestarlo ai colleghi in caso di urgenza", "Rinnovarlo ogni mese", "Depositarne copia in Comune"],
  "Deve anche adottare misure idonee a evitare danno ad altri.", "32", "è altresì tenuto ad utilizzare personalmente il dispositivo di firma")
C("inf-292", 4, "Se un documento informatico è conservato per legge da una PA, cosa accade all'obbligo di conservazione di cittadini e imprese?",
  "Cessa: possono chiederne accesso in ogni momento alla PA", ["Raddoppia", "Resta invariato", "Passa al notaio"],
  "Art. 43, comma 1-bis, del CAD.", "43", "cessa l'obbligo di conservazione a carico dei cittadini e delle imprese")
C("inf-293", 3, "Come avvengono le comunicazioni di documenti tra pubbliche amministrazioni secondo il CAD?",
  "Tramite posta elettronica o cooperazione applicativa", ["Solo tramite raccomandata", "Solo via fax", "Tramite consegna a mano"],
  "Sono valide una volta verificata la provenienza; la violazione comporta responsabilità dirigenziale e disciplinare.", "47", "avvengono mediante l'utilizzo della posta elettronica o in cooperazione applicativa")
C("inf-294", 4, "Quali dati pubblicati dalle PA senza una licenza espressa si intendono rilasciati come dati di tipo aperto?",
  "I dati e documenti pubblicati, salvo quelli personali", ["Nessuno", "Solo i dati di bilancio", "Tutti, compresi i dati personali"],
  "È il principio «open by default» dell'art. 52 del CAD.", "52", "si intendono rilasciati come dati di tipo aperto")
C("inf-295", 3, "Quali principi devono rispettare i siti Internet delle pubbliche amministrazioni secondo l'art. 53 del CAD?",
  "Accessibilità, usabilità e reperibilità, anche per le persone disabili", ["Solo l'estetica grafica", "La presenza di pubblicità", "L'uso esclusivo della lingua inglese"],
  "Anche completezza di informazione, chiarezza di linguaggio e affidabilità.", "53", "rispettano i principi di accessibilità, nonché di elevata usabilità e reperibilità")
C("inf-296", 4, "Dove è attivato il punto di accesso telematico unico ai servizi delle PA (art. 64-bis CAD)?",
  "Presso la Presidenza del Consiglio dei ministri", ["Presso ogni Comune", "Presso l'INPS", "Presso le Camere di commercio"],
  "È il punto di accesso a cui fa riferimento il diritto a servizi online semplici e integrati.", "64-bis", "tramite il punto di accesso telematico attivato presso la Presidenza del Consiglio dei ministri")
C("inf-297", 4, "Che cos'è il Sistema pubblico di connettività e cooperazione (SPC)?",
  "L'insieme di infrastrutture e regole tecniche che assicura l'interoperabilità tra i sistemi informativi delle PA", ["Il portale dei concorsi pubblici", "La rete Wi-Fi gratuita dei Comuni", "Il registro delle PEC"],
  "Art. 73 del CAD.", "73", "quale insieme di infrastrutture tecnologiche e di regole tecniche che assicura l'interoperabilità")
C("inf-298", 3, "Cosa individuano le Linee guida previste dall'art. 51 del CAD?",
  "Le soluzioni tecniche per garantire protezione, disponibilità, integrità e riservatezza dei dati e continuità operativa", ["Gli orari degli uffici", "Le tariffe dei servizi online", "I modelli di firma autografa"],
  "AgID attua anche il Piano nazionale per la sicurezza cibernetica.", "51", "sono individuate le soluzioni tecniche idonee a garantire la protezione, la disponibilità")
C("inf-299", 3, "A cosa sono finalizzate le politiche di formazione informatica dei dipendenti pubblici (art. 13 CAD)?",
  "Alla conoscenza e all'uso delle tecnologie dell'informazione, anche sull'accessibilità e le tecnologie assistive", ["Solo all'uso dei social network", "Alla riparazione dei computer", "Alla programmazione di videogiochi"],
  "Per i dirigenti riguardano anche competenze manageriali e di informatica giuridica.", "13", "finalizzate alla conoscenza e all'uso delle tecnologie dell'informazione e della comunicazione")
C("inf-300", 4, "Quale piattaforma è realizzata presso l'AgID per la consultazione pubblica sui provvedimenti dell'agenda digitale?",
  "La Piattaforma nazionale per la governance della trasformazione digitale", ["La piattaforma pagoPA", "L'app IO", "Il portale INI-PEC"],
  "Raccoglie suggerimenti e proposte dai portatori di interesse.", "18", "È realizzata presso l'AgID una piattaforma per la consultazione pubblica")

# ── Verso 350: quadro europeo delle competenze digitali (DigComp 2.2, traduzione AgID/Dipartimento
#    per la trasformazione digitale), IA, software libero, backup, Codice privacy, calcolatori.
DIG = "AgID_DigComp-2.2-italiano.txt"
FDIG = "DigComp 2.2, Il Quadro delle Competenze Digitali per i Cittadini (JRC, trad. italiana)"
WIA, WSL, WBK = "Wikipedia_Intelligenza-artificiale.txt", "Wikipedia_Software-libero.txt", "Wikipedia_Backup.txt"
P196 = "norma_DLgs196-2003_privacy.txt"

D("inf-301", "Competenze digitali", 2, "Quante competenze compongono la competenza digitale secondo il quadro europeo DigComp?",
  "21 competenze", ["5 competenze", "12 competenze", "50 competenze"],
  "Il DigComp definisce la competenza digitale come una combinazione di 21 competenze raggruppate in cinque aree.",
  FDIG, DIG, "combinazione di 21 competenze")

D("inf-302", "Competenze digitali", 2, "In quante aree principali sono raggruppate le competenze del DigComp?",
  "Cinque", ["Tre", "Otto", "Dieci"],
  "Le 21 competenze del DigComp sono raggruppate in cinque aree principali.",
  FDIG, DIG, "raggruppate in cinque aree principali")

D("inf-303", "Competenze digitali", 3, "Quale tra queste è una delle cinque aree del DigComp?",
  "Sicurezza", ["Contabilità digitale", "Hardware", "Programmazione avanzata"],
  "Dal 2016 le cinque aree sono: alfabetizzazione su informazione e dati; comunicazione e collaborazione; creazione di contenuti digitali; sicurezza; risolvere problemi.",
  FDIG, DIG, "Dal 2016, le cinque aree sono")

D("inf-304", "Competenze digitali", 3, "In che anno è uscito il primo quadro di riferimento DigComp?",
  "Nel 2013", ["Nel 2006", "Nel 2020", "Nel 1999"],
  "Il lavoro sulle competenze digitali iniziò nel 2010; nel 2013 è uscito il primo quadro di riferimento DigComp.",
  FDIG, DIG, "Nel 2013 è uscito il primo quadro di riferimento DigComp")

D("inf-305", "Competenze digitali", 3, "Quanti livelli di padronanza prevede il DigComp?",
  "Otto", ["Tre", "Cinque", "Dieci"],
  "Il DigComp prevede otto livelli di padronanza, ispirati alla struttura e al vocabolario dell'EQF e alla tassonomia di Bloom.",
  FDIG, DIG, "Gli otto livelli di padronanza si ispirano alla struttura e al")

D("inf-306", "Competenze digitali", 4, "Quale servizio della Commissione europea ha elaborato il DigComp?",
  "Il Joint Research Centre (JRC)", ["L'ENISA", "Eurostat", "La Banca centrale europea"],
  "Il DigComp 2.2 è un rapporto Science for Policy del Joint Research Centre, il servizio della Commissione europea per la scienza e la conoscenza.",
  FDIG, DIG, "rapporto Science for Policy del Joint Research Centre (JRC)")

D("inf-307", "Competenze digitali", 4, "Cosa aggiunge principalmente l'aggiornamento DigComp 2.2?",
  "Più di 250 nuovi esempi di conoscenze, abilità e attitudini", ["Una sesta area di competenza", "Un esame di certificazione obbligatorio", "Nuovi livelli di padronanza"],
  "Il DigComp 2.2 fornisce più di 250 nuovi esempi di conoscenze, abilità e attitudini, anche su temi emergenti come l'IA; non cambia aree né livelli.",
  FDIG, DIG, "fornisce più di 250 nuovi esempi")

D("inf-308", "Competenze digitali", 3, "In quale area del DigComp rientra la competenza «Netiquette»?",
  "Comunicazione e collaborazione", ["Sicurezza", "Risolvere problemi", "Creazione di contenuti digitali"],
  "La 2.5 Netiquette fa parte dell'area 2, Comunicazione e collaborazione, insieme ad esempio alla 2.6 Gestire l'identità digitale.",
  FDIG, DIG, "2.5. Netiquette")

D("inf-309", "Competenze digitali", 4, "In quale area del DigComp rientra la competenza «Proteggere l'ambiente»?",
  "Sicurezza", ["Comunicazione e collaborazione", "Alfabetizzazione su informazione e dati", "Creazione di contenuti digitali"],
  "L'area 4, Sicurezza, comprende: proteggere i dispositivi, i dati personali e la privacy, la salute e il benessere, l'ambiente (4.4).",
  FDIG, DIG, "4.4. Proteggere l'ambiente")

D("inf-310", "Competenze digitali", 3, "In quale area del DigComp rientra la competenza «Copyright e licenze»?",
  "Creazione di contenuti digitali", ["Sicurezza", "Risolvere problemi", "Comunicazione e collaborazione"],
  "L'area 3, Creazione di contenuti digitali, comprende sviluppare, integrare e rielaborare contenuti, copyright e licenze (3.3) e programmazione (3.4).",
  FDIG, DIG, "3.3. Copyright e licenze")

D("inf-311", "Competenze digitali", 3, "Come si chiamano gli effetti per cui alcuni algoritmi rafforzano i punti di vista già esistenti di un utente?",
  "Camere d'eco e bolle di filtraggio", ["Phishing e spoofing", "Cache e buffer", "Firewall e proxy"],
  "Il DigComp ricorda che alcuni algoritmi di IA possono rafforzare i punti di vista esistenti creando «camere d'eco» o «bolle di filtraggio».",
  FDIG, DIG, "\"bolle di filtraggio\" (filter bubbles)")

D("inf-312", "Competenze digitali", 3, "Perché è utile cercare online il proprio nome e cognome, secondo il DigComp?",
  "Per controllare la propria «impronta digitale» negli ambienti online", ["Per aumentare la velocità della connessione", "Per aggiornare il sistema operativo", "Per cancellare i cookie"],
  "Tra le abilità: effettuare una ricerca sul proprio nome per controllare la propria impronta digitale online, ad esempio post o immagini problematici.",
  FDIG, DIG, "al fine di controllare la propria \"impronta digitale\"")

D("inf-313", "Sicurezza", 2, "Cosa si usa, insieme alle credenziali, nell'autenticazione a due fattori?",
  "Una password temporanea OTP o un codice aggiuntivo", ["Una seconda password uguale alla prima", "Il proprio indirizzo email", "Nessun altro elemento"],
  "L'autenticazione a due fattori usa, ad esempio, una password temporanea OTP o un codice aggiuntivo assieme alle credenziali di accesso.",
  FDIG, DIG, "attivare l'autenticazione a due fattori quando disponibile")

D("inf-314", "Sicurezza", 2, "Cosa si intende per cyberbullismo?",
  "Bullismo perpetrato con l'uso di tecnologie digitali", ["Un attacco informatico a una banca", "Un virus che cancella i file", "La pubblicità ingannevole online"],
  "Il cyberbullismo è il bullismo perpetrato con tecnologie digitali: un comportamento ripetuto volto a spaventare, irritare o svergognare le persone prese di mira.",
  FDIG, DIG, "si riferisce al bullismo perpetrato con l'uso di tecnologie digitali")

D("inf-315", "Privacy", 3, "Quali funzionalità permettono di limitare il tracciamento delle proprie attività su Internet?",
  "La navigazione privata e la cancellazione dei cookie", ["L'aumento della risoluzione dello schermo", "La deframmentazione del disco", "L'uso di caratteri maiuscoli nelle password"],
  "Esistono modi per limitare il tracciamento online, come la navigazione privata, la cancellazione dei cookie e il consenso personalizzato per i cookie.",
  FDIG, DIG, "navigazione privata e cancellazione dei cookie")

D("inf-316", "Competenze digitali", 4, "Come si chiamano, in inglese, le misure tecniche che bloccano o limitano l'accesso a contenuti digitali protetti?",
  "TPM (Technical Protection Measures)", ["VPN", "API", "DNS"],
  "Esistono meccanismi per limitare l'accesso ai contenuti digitali, come password, blocchi geografici e misure di protezione tecniche (TPM).",
  FDIG, DIG, "misure di protezione tecniche, in inglese TPM")

D("inf-317", "Basi di dati", 3, "Cosa sono gli archivi di dati aperti (open data)?",
  "Archivi in cui chiunque può ottenere dati, ad esempio per risolvere problemi", ["Database accessibili solo alla polizia", "Archivi di password", "Backup di sistema crittografati"],
  "Il DigComp ricorda che esistono archivi di dati aperti in cui chiunque può ottenere dati utili, ad esempio per attività di risoluzione dei problemi.",
  FDIG, DIG, "esistono archivi di dati aperti in cui chiunque può ottenere dati")

D("inf-318", "Intelligenza artificiale", 3, "Cosa ha fatto esplodere l'interesse per il deep learning dopo il 2012?",
  "L'uso delle GPU per addestrare reti neurali", ["L'invenzione del transistor", "La nascita del World Wide Web", "L'abbandono delle reti neurali"],
  "Interesse e investimenti sono cresciuti dopo il 2012, quando l'uso delle GPU per addestrare reti neurali ha permesso al deep learning di superare le tecniche precedenti.",
  W("Intelligenza artificiale"), WIA, "quando l'impiego delle unità di elaborazione grafica (GPU) per addestrare reti neurali")

D("inf-319", "Intelligenza artificiale", 3, "Quale tipo di IA rappresenta oggi la totalità dei sistemi esistenti?",
  "L'IA debole (o ristretta), specializzata in compiti specifici", ["L'IA generale (AGI)", "La superintelligenza", "L'IA cosciente"],
  "L'IA debole o ristretta, specializzata in compiti specifici, rappresenta il 100% dei sistemi oggi esistenti; l'AGI è ipotetica.",
  W("Intelligenza artificiale"), WIA, "IA debole (o ristretta), che rappresenta il 100% dei sistemi AI oggi esistenti")

D("inf-320", "Intelligenza artificiale", 4, "Chi creò nel 1943 quello che è ritenuto il primo lavoro sull'intelligenza artificiale, un modello di neuroni artificiali?",
  "McCulloch e Pitts", ["Turing e Church", "Minsky e McCarthy", "Newell e Simon"],
  "Nel 1943 McCulloch e Pitts crearono il primo lavoro sull'IA: un modello di neuroni artificiali «accesi» o «spenti».",
  W("Intelligenza artificiale"), WIA, "Nel 1943 McCulloch e Pitts crearono ciò che viene ritenuto il primo lavoro")

D("inf-321", "Intelligenza artificiale", 4, "Come si chiamava la prima rete neurale artificiale, creata nel 1950 da Minsky ed Edmonds?",
  "SNARC", ["ENIAC", "Logic Theorist", "Perceptron"],
  "Nel 1950 Marvin Minsky e Dean Edmonds, studenti di Harvard, crearono la prima rete neurale artificiale, chiamata SNARC.",
  W("Intelligenza artificiale"), WIA, "crearono la prima rete neurale artificiale, conosciuta con il nome di \"SNARC\"")

D("inf-322", "Intelligenza artificiale", 4, "Quale programma di Newell e Simon, presentato a Dartmouth nel 1956, sapeva dimostrare teoremi?",
  "Logic Theorist", ["ELIZA", "Deep Blue", "SHRDLU"],
  "A Dartmouth Allen Newell e Herbert Simon presentarono il Logic Theorist, capace di dimostrare teoremi partendo dai principi della matematica.",
  W("Intelligenza artificiale"), WIA, "conosciuto con il nome di \"Logic Theorist\"")

D("inf-323", "Intelligenza artificiale", 3, "Chi introdusse l'espressione «intelligenza artificiale»?",
  "John McCarthy, al convegno di Dartmouth del 1956", ["Alan Turing, nel 1936", "Claude Shannon, nel 1948", "Marvin Minsky, nel 1969"],
  "Nel convegno di Dartmouth del 1956 McCarthy introdusse l'espressione «intelligenza artificiale».",
  W("Intelligenza artificiale"), WIA, "McCarthy introdusse l'espressione \"intelligenza artificiale\"")

D("inf-324", "Intelligenza artificiale", 4, "In quale articolo del 1936 Alan Turing discusse la calcolabilità e introdusse la «macchina di Turing»?",
  "On Computable Numbers", ["Computing Machinery and Intelligence", "A Mathematical Theory of Communication", "Perceptrons"],
  "Nel 1936 Alan Turing, nell'articolo On Computable Numbers, discusse calcolabilità, computabilità e il concetto di macchina di Turing.",
  W("Intelligenza artificiale"), WIA, "Nel 1936 Alan Turing nel suo articolo On Computable Numbers")

D("inf-325", "Intelligenza artificiale", 3, "Come definisce l'intelligenza artificiale il Parlamento europeo?",
  "La capacità di un sistema di mostrare capacità umane come ragionamento, apprendimento, pianificazione e creatività", ["Un qualsiasi programma per computer", "Un robot con sembianze umane", "Una rete di computer collegati a Internet"],
  "Il Parlamento europeo definisce l'IA come la possibilità per un sistema di mostrare capacità tipicamente umane: ragionamento, apprendimento, pianificazione e creatività.",
  W("Intelligenza artificiale"), WIA, "quali il ragionamento, l'apprendimento, la pianificazione e la creatività")

D("inf-326", "Intelligenza artificiale", 3, "Quale uso improprio si fa spesso, nel linguaggio comune, del termine «intelligenza artificiale»?",
  "Lo si usa per indicare la sola IA generativa", ["Lo si usa per indicare i robot industriali", "Lo si usa per indicare Internet", "Lo si usa per indicare i videogiochi"],
  "Nel linguaggio comune «intelligenza artificiale» indica spesso la sola IA generativa, che crea testi, immagini, audio o video: è solo uno dei sottocampi.",
  W("Intelligenza artificiale"), WIA, "viene spesso usato in modo improprio per indicare la sola intelligenza artificiale generativa")

D("inf-327", "Intelligenza artificiale", 4, "Quale programma di Newell e Simon fu ideato per imitare i processi umani di risoluzione dei problemi?",
  "General Problem Solver (GPS)", ["Logic Theorist", "SNARC", "Geometry Theorem Prover"],
  "Dopo il Logic Theorist, Newell e Simon crearono il General Problem Solver (GPS), ideato per imitare la risoluzione dei problemi umana (euristica mezzi-fini).",
  W("Intelligenza artificiale"), WIA, "General Problem Solver, o GPS")

D("inf-328", "Intelligenza artificiale", 4, "Quale celebre scienziato, nel 2014, segnalò i rischi potenziali dell'IA per l'umanità?",
  "Stephen Hawking", ["Albert Einstein", "Tim Berners-Lee", "Alan Turing"],
  "Numerosi scienziati e filosofi, tra cui nel 2014 Stephen Hawking, hanno segnalato i rischi potenziali dell'IA.",
  W("Intelligenza artificiale"), WIA, "nel 2014, Stephen Hawking")

D("inf-329", "Software", 3, "Quale licenza ideò Richard Stallman nel 1989?",
  "La GNU General Public License (GPL), una licenza copyleft", ["La licenza MIT", "La licenza Creative Commons", "La licenza Apache"],
  "Nel 1989 Richard Stallman ideò la GNU General Public License, una licenza copyleft.",
  W("Software libero"), WSL, "Nel 1989, Richard Stallman, ideò anche la GNU General Public License (GNU-GPL), una licenza Copyleft")

D("inf-330", "Software", 4, "Cosa impone il copyleft a chi modifica un software distribuito con licenza GPL?",
  "Di distribuire le modifiche con la stessa licenza del software di partenza", ["Di pagare una royalty all'autore", "Di non pubblicare mai il codice sorgente", "Di cambiare il nome del programma"],
  "La GPL incentiva la condivisione del codice imponendo a chi modifica di farlo con la stessa licenza del software di partenza.",
  W("Software libero"), WSL, "l'obbligo verso coloro che modificano di farlo con la stessa licenza del software di partenza")

D("inf-331", "Software", 3, "Cosa significa l'acronimo ricorsivo GNU?",
  "GNU's Not Unix", ["General Network Utility", "Global Numeric Unit", "GNU New Unix"],
  "Nel 1983 Stallman fondò il progetto GNU (GNU's Not Unix) per creare un sistema operativo completamente libero.",
  W("Software libero"), WSL, "(GNU's Not Unix)")

D("inf-332", "Software", 5, "Quale atto normativo statunitense permise di privatizzare con la proprietà intellettuale i risultati della ricerca accademica?",
  "Il Bayh-Dole Act", ["Il Patriot Act", "Il Digital Millennium Copyright Act", "Lo Sherman Act"],
  "Negli anni Ottanta il Bayh-Dole Act mise in discussione la libera circolazione delle idee accademiche, permettendo di proteggere con proprietà intellettuale i risultati delle ricerche.",
  W("Software libero"), WSL, "Bayh-Dole Act")

D("inf-333", "Sicurezza", 3, "Oltre a quella manuale o periodica, quale altra programmazione del backup è possibile?",
  "«Su evento», ad esempio all'installazione di un nuovo software", ["Solo alla fine dell'anno", "Solo quando il disco è pieno", "Solo su richiesta del produttore"],
  "Il backup può essere manuale, automatico periodico, oppure «su evento», ad esempio all'installazione di nuovo software o al superamento di una soglia di allarme.",
  W("Backup"), WBK, "Un'altra possibilità di programmazione è \"su evento\"")

D("inf-334", "Sicurezza", 3, "Basta eseguire un backup per essere al sicuro?",
  "No: bisogna verificare che il job sia completo e privo di errori, e conservarlo bene", ["Sì, sempre", "Sì, se fatto su chiavetta USB", "Sì, se il file è compresso"],
  "Eseguire un backup non basta: occorre accertare che il job sia corretto, completo e privo di errori, perché il ripristino sia efficace; conta anche la conservazione.",
  W("Backup"), WBK, "occorre accertare che il job ottenuto sia corretto")

D("inf-335", "Sicurezza", 4, "Cosa si salva con il backup di un apparato di rete come un router o un firewall?",
  "La configurazione, cioè il file delle impostazioni", ["Solo i documenti degli utenti", "Il firmware del produttore", "Le password di tutti i siti visitati"],
  "Per gli apparati il backup si applica anche alla configurazione (il file delle impostazioni e personalizzazioni), ad esempio di router, firewall o switch.",
  W("Backup"), WBK, "Per gli apparati il backup si applica pure alla configurazione")

D("inf-336", "Sicurezza", 4, "Come funziona il backup continuo offerto dai servizi online o dai backup appliance?",
  "Tramite agent che individuano i file nuovi e ne fanno subito la copia", ["Con una copia manuale settimanale", "Stampando i documenti", "Spegnendo il computer ogni sera"],
  "Il backup continuo usa agent, software che individuano con criteri i file nuovi da archiviare e ne eseguono subito la copia di sicurezza.",
  W("Backup"), WBK, "attraverso gli agent")

D("inf-337", "Privacy", 4, "Per quanto tempo il fornitore conserva i dati di traffico telefonico per finalità di accertamento dei reati?",
  "Ventiquattro mesi dalla comunicazione", ["Sei mesi", "Dieci anni", "Tre giorni"],
  "Art. 132 D.Lgs. 196/2003: i dati di traffico telefonico sono conservati per ventiquattro mesi; quelli di traffico telematico, esclusi i contenuti, per dodici mesi.",
  "D.Lgs. 196/2003, art. 132", P196, "conservati dal fornitore per ventiquattro mesi dalla data della comunicazione")

D("inf-338", "Privacy", 4, "Per quanto tempo il fornitore conserva i dati di traffico telematico (esclusi i contenuti) a fini di repressione dei reati?",
  "Dodici mesi", ["Ventiquattro mesi", "Trenta giorni", "Cinque anni"],
  "Art. 132 D.Lgs. 196/2003: i dati di traffico telematico, esclusi i contenuti delle comunicazioni, sono conservati dal fornitore per dodici mesi.",
  "D.Lgs. 196/2003, art. 132", P196, "sono conservati dal fornitore per dodici mesi dalla data della comunicazione")

D("inf-339", "Privacy", 4, "Chi elegge i componenti del Collegio del Garante per la protezione dei dati personali?",
  "Due la Camera dei deputati e due il Senato, con voto limitato", ["Il Presidente della Repubblica", "Il Governo", "Il Consiglio di Stato"],
  "Art. 153 D.Lgs. 196/2003: il Collegio è costituito da quattro componenti, eletti due dalla Camera e due dal Senato con voto limitato.",
  "D.Lgs. 196/2003, art. 153", P196, "eletti due dalla Camera dei deputati e due dal Senato della Repubblica con voto limitato")

D("inf-340", "Privacy", 4, "Se l'interessato ha già proposto reclamo al Garante, può poi rivolgersi al giudice per lo stesso oggetto e tra le stesse parti?",
  "No: il reclamo al Garante rende improponibile l'ulteriore domanda al giudice", ["Sì, sempre", "Sì, ma solo dopo un anno", "Sì, se il Garante non risponde entro una settimana"],
  "Art. 140-bis D.Lgs. 196/2003: reclamo al Garante e ricorso al giudice sono alternativi; presentato il reclamo, è improponibile la domanda al giudice tra le stesse parti e per lo stesso oggetto.",
  "D.Lgs. 196/2003, art. 140-bis", P196, "La presentazione del reclamo al Garante rende improponibile un'ulteriore domanda dinanzi all'autorità giudiziaria")

D("inf-341", "Privacy", 5, "Da quali atti può essere costituita la base giuridica dei trattamenti per compiti di interesse pubblico?",
  "Da una norma di legge, di regolamento o da atti amministrativi generali", ["Solo dal consenso dell'interessato", "Da un contratto privato", "Da una circolare interna"],
  "Art. 2-ter D.Lgs. 196/2003: la base giuridica per i trattamenti di interesse pubblico è una norma di legge o di regolamento o un atto amministrativo generale.",
  "D.Lgs. 196/2003, art. 2-ter", P196, "da una norma di legge o ((...)) di regolamento ((o da atti amministrativi generali))")

D("inf-342", "Privacy", 4, "Le chiamate pubblicitarie automatizzate, senza operatore, sono consentite?",
  "Solo con il consenso del contraente o utente", ["Sempre", "Mai", "Solo di notte"],
  "Art. 130 D.Lgs. 196/2003: l'uso di sistemi automatizzati di chiamata senza operatore per pubblicità o vendita diretta è consentito con il consenso del contraente o utente.",
  "D.Lgs. 196/2003, art. 130", P196, "è consentito con il consenso del contraente o utente")

D("inf-343", "Privacy", 4, "Cosa possono fare titolare e responsabile del trattamento secondo l'art. 2-quaterdecies del Codice privacy?",
  "Attribuire specifici compiti a persone fisiche espressamente designate sotto la loro autorità", ["Delegare tutto al Garante", "Rinunciare alla responsabilità", "Trasferire i dati senza limiti"],
  "Art. 2-quaterdecies: titolare o responsabile possono attribuire compiti connessi al trattamento a persone fisiche espressamente designate che operano sotto la loro autorità.",
  "D.Lgs. 196/2003, art. 2-quaterdecies", P196, "siano attribuiti a persone fisiche, espressamente designate, che operano sotto la loro autorità")

D("inf-344", "Privacy", 5, "Con quale pena è punito il trattamento illecito di dati dell'art. 167, c. 1 del Codice privacy?",
  "Reclusione da sei mesi a un anno e sei mesi", ["Solo una multa", "Reclusione da cinque a dieci anni", "Nessuna pena: è solo un illecito civile"],
  "Art. 167, c. 1: chi, per profitto o per arrecare danno, viola le norme indicate e arreca nocumento all'interessato è punito con la reclusione da sei mesi a un anno e sei mesi.",
  "D.Lgs. 196/2003, art. 167", P196, "è punito con la reclusione da sei mesi a un anno e sei mesi")

D("inf-345", "Hardware", 3, "In cosa si differenzia l'architettura Harvard da quella di Von Neumann?",
  "Separa la memoria dei dati da quella del codice (istruzioni)", ["Non usa memoria", "Usa solo memorie ottiche", "Ha un solo registro"],
  "L'architettura Harvard si differenzia da quella di Von Neumann per la separazione della memoria dati e della memoria codice, con cache separate.",
  GCF, GC, "L'architettura Harvard si differenzia dall'architettura di Von Neumann per la separazione della memoria dati e della memoria codice")

D("inf-346", "Hardware", 4, "Nel RAID 0, come vengono distribuiti i dati?",
  "Su strisce (strip) suddivise tra più dischi, con letture e scritture in parallelo", ["Duplicati identici su due dischi", "Su un solo disco con parità", "Solo su nastro"],
  "Nel RAID 0 i dati sono distribuiti su strisce, ciascuna su un disco: la banda in lettura/scrittura aumenta perché le operazioni avvengono in parallelo.",
  GCF, GC, "Nel RAID 0, i dati vengono distribuiti su strisce (strip)")

D("inf-347", "Hardware", 4, "Nella modalità Memory-Mapped-IO, come comunica il processore con le periferiche?",
  "Come con le celle di memoria: periferiche e memoria condividono un unico spazio di indirizzamento", ["Con un bus separato per ogni periferica", "Solo tramite interrupt", "Via rete Wi-Fi"],
  "In Memory-Mapped-IO periferiche e memoria sono mappate in un unico spazio di indirizzamento; in Isolated-IO gli spazi sono distinti.",
  GCF, GC, "le periferiche e la memoria sono mappate in un unico spazio di indirizzamento")

D("inf-348", "Hardware", 3, "Cosa caratterizza i processori superscalari, diffusi dagli anni Novanta?",
  "Completano più di un'istruzione a ogni colpo di clock", ["Hanno un solo transistor", "Funzionano senza clock", "Eseguono un'istruzione ogni dieci colpi di clock"],
  "CISC: più colpi di clock per istruzione; RISC: un'istruzione per colpo; superscalari: più di un'istruzione per colpo; multicore: più processori integrati.",
  GCF, GC, "a ogni colpo di clock completano più di un'istruzione")

D("inf-349", "Hardware", 4, "Che organizzazione hanno i dischi ottici quanto alla velocità di rotazione?",
  "Constant Linear Velocity: velocità lineare costante, angolare variabile", ["Velocità angolare costante come i dischi fissi", "Nessuna rotazione", "Rotazione casuale"],
  "I dischi ottici hanno organizzazione CLV: il motore ruota a velocità lineare costante ma a velocità angolari diverse secondo la posizione del laser.",
  GCF, GC, "I dischi ottici hanno un'organizzazione Constant Linear Velocity (CLV)")

D("inf-350", "Hardware", 3, "Che vantaggio hanno le EEPROM rispetto alle EPROM?",
  "Si riprogrammano senza raggi ultravioletti", ["Sono volatili", "Sono più veloci delle RAM", "Non si possono mai riscrivere"],
  "Le memorie EEPROM possono essere riprogrammate senza raggi ultravioletti, ma la programmazione è lenta e sono costose.",
  GCF, GC, "Le memorie EEPROM possono essere riprogrammate senza raggi ultra-violetti")
