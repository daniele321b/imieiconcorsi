# Logica — fonti: MatematicaC3, «Logica» (CC BY 3.0) e voce Wikipedia «Sillogismo» (CC BY-SA 4.0), solo per definizioni e regole.
LOG = "MatematicaC3_Logica.txt"
SIL = "Wikipedia_Sillogismo.txt"
M = "MatematicaC3, Logica (CC BY 3.0)"
WS = "Wikipedia, «Sillogismo» (CC BY-SA 4.0)"

D("log-001", "Connettivi", 1, "Quando è vera la congiunzione «p e q»?",
  "Solo quando p e q sono entrambe vere", ["Quando almeno una delle due è vera", "Quando sono entrambe false", "Quando p è vera, qualunque sia q"],
  "La congiunzione è vera solo se le due proposizioni sono contestualmente vere; basta una falsa perché sia falsa.",
  M, LOG, "è falsa quando anche una sola delle due proposizioni è falsa")

D("log-002", "Connettivi", 2, "Quando è falsa la disgiunzione inclusiva «p o q»?",
  "Solo se entrambe le proposizioni sono false", ["Se almeno una è falsa", "Se entrambe sono vere", "Mai"],
  "La disgiunzione inclusiva è vera quando almeno una delle due è vera ed è falsa solo se entrambe sono false.",
  M, LOG, "è falsa solo se entrambe le proposizioni sono false")

D("log-003", "Connettivi", 3, "Quando è vera la disgiunzione esclusiva «o p o q»?",
  "Quando soltanto una delle due è vera", ["Quando sono entrambe vere", "Quando sono entrambe false", "Quando almeno una è vera"],
  "La disgiunzione esclusiva (aut) è vera solo se una delle due è vera; è falsa se sono entrambe vere o entrambe false. Esempio: «oggi il Milan vince o pareggia».",
  M, LOG, "è vera quando soltanto una delle due proposizioni è vera")

D("log-004", "Connettivi", 2, "Nella frase «100 è minore di 1 o maggiore di 10», la «o» è usata in senso:",
  "inclusivo, e la frase è vera", ["esclusivo, e la frase è falsa", "inclusivo, e la frase è falsa", "esclusivo, e la frase è vera"],
  "È una disgiunzione inclusiva ed è vera perché una delle due affermazioni è vera: 100 è maggiore di 10.",
  M, LOG, "«100 è minore di 1 o maggiore di 10» è vera perché è vera una delle due affermazioni")

D("log-005", "Implicazione", 2, "Nell'implicazione «se p allora q», come si chiamano p e q?",
  "p è l'antecedente (ipotesi), q il conseguente (tesi)", ["p è la tesi, q l'ipotesi", "p e q sono entrambe premesse", "p è il termine medio, q la conclusione"],
  "Nella scrittura p ⇒ q, p è l'antecedente o ipotesi e q il conseguente o tesi.",
  M, LOG, "La proposizione p è detta antecedente, (o ipotesi) e la proposizione q è detta conseguente (o tesi)")

D("log-006", "Implicazione", 3, "Se vale «p implica q», allora:",
  "p è condizione sufficiente per q e q è condizione necessaria per p", ["p è condizione necessaria per q", "q è condizione sufficiente per p", "p e q sono sempre equivalenti"],
  "Da p ⇒ q: p è sufficiente per q, q è necessaria per p.",
  M, LOG, "condizione sufficiente per q, mentre la proposizione q viene detta condizione necessaria per p")

D("log-007", "Implicazione", 4, "«Studiare è condizione necessaria per essere promossi, ma non sufficiente». Quale affermazione è sicuramente vera?",
  "Chi non ha studiato non è stato promosso", ["Chi ha studiato è stato promosso", "Chi è stato bocciato non ha studiato", "Studiare e essere promossi sono la stessa cosa"],
  "Se q (studiare) è necessaria per p (promozione), vale p ⇒ q e quindi anche ¬q ⇒ ¬p: senza studio, niente promozione.",
  M, LOG, "studiare è condizione necessaria per essere promossi ma non è sufficiente")

D("log-008", "Implicazione", 4, "Data l'implicazione «se p allora q», quale altra implicazione ha sempre gli stessi valori di verità?",
  "Se non q allora non p", ["Se q allora p", "Se non p allora non q", "Se p allora non q"],
  "La contronominale ¬q ⇒ ¬p è equivalente a p ⇒ q; l'inversa (q ⇒ p) e la contraria (¬p ⇒ ¬q) no.",
  M, LOG, "da p ⇒ q si può dedurre ¬q ⇒ ¬p")

D("log-009", "Tautologie", 2, "Come si chiama una proposizione sempre vera, qualunque sia il valore di verità dei suoi elementi?",
  "Tautologia", ["Contraddizione", "Implicazione", "Sillogismo"],
  "Esempio di tautologia: «Quest'anno la Juve vince il campionato oppure non lo vince».",
  M, LOG, "è detta tautologia")

D("log-010", "Tautologie", 2, "Come si chiama una proposizione sempre falsa, come «un numero è multiplo di 2 ed è dispari»?",
  "Contraddizione", ["Tautologia", "Disgiunzione", "Negazione"],
  "Una proposizione sempre falsa, qualunque sia la verità dei suoi elementi, è una contraddizione.",
  M, LOG, "Un esempio banale di contraddizione è l'affermazione \"un numero è multiplo di 2 ed è dispari\"")

D("log-011", "Leggi di De Morgan", 3, "Secondo le leggi di De Morgan, la negazione di «p e q» equivale a:",
  "non p o non q", ["non p e non q", "p o q", "non (p o q)"],
  "Leggi di De Morgan: ¬(p ∧ q) = ¬p ∨ ¬q e ¬(p ∨ q) = ¬p ∧ ¬q.",
  M, LOG, "¬(p ∧ q) = ¬p ∨ ¬q")

D("log-012", "Leggi di De Morgan", 4, "Qual è la negazione di «Marco parla inglese o francese»?",
  "Marco non parla né inglese né francese", ["Marco non parla inglese o non parla francese", "Marco parla inglese e francese", "Marco parla solo una delle due lingue"],
  "Per De Morgan ¬(p ∨ q) = ¬p ∧ ¬q: non parla inglese E non parla francese.",
  M, LOG, "¬(p ∨ q) = ¬p ∧ ¬q")

D("log-013", "Quantificatori", 3, "Qual è la negazione di «Tutti i gatti fanno le fusa»?",
  "C'è almeno un gatto che non fa le fusa", ["Nessun gatto fa le fusa", "Tutti i gatti non fanno le fusa", "Alcuni gatti fanno le fusa"],
  "La negazione di un enunciato universale è un enunciato esistenziale: «esiste almeno un… che non…».",
  M, LOG, "\"C'è almeno un gatto che non fa le fusa\"")

D("log-014", "Quantificatori", 2, "Quale simbolo indica il quantificatore universale «per ogni»?",
  "∀", ["∃", "¬", "∨"],
  "∀ si legge «per ogni»; ∃ «esiste»; ¬ è la negazione; ∨ la disgiunzione.",
  M, LOG, "il simbolo ∀ (che si legge \"per ogni\") per indicare il quantificatore universale")

D("log-015", "Sillogismo", 2, "Nel sillogismo «Tutti gli uomini sono mortali; tutti i greci sono uomini; quindi tutti i greci sono mortali», qual è il termine medio?",
  "uomini", ["mortali", "greci", "tutti"],
  "Il termine medio compare in entrambe le premesse e non nella conclusione: qui è «uomini».",
  WS, SIL, "termine medio, che è il termine che si trova in entrambe le premesse")

D("log-016", "Sillogismo", 4, "Quante sono le forme valide del sillogismo categorico, sulle 256 combinazioni possibili?",
  "19", ["4", "64", "256"],
  "Le combinazioni sono 256, ma le forme valide solo 19, tra cui le quattro «perfette» della prima figura (Barbara, Celarent, Darii, Ferio).",
  WS, SIL, "Le forme valide, però, sono soltanto 19")

D("log-017", "Sillogismo", 5, "Premesse false possono portare a una conclusione vera?",
  "Sì: «tutti i pesci sono uomini; Socrate è un pesce; quindi Socrate è un uomo»", ["No, mai", "Solo se il sillogismo non è valido", "Solo con premesse particolari"],
  "La validità riguarda la forma: da premesse false si può ricavare una conclusione vera, come nell'esempio di Socrate.",
  WS, SIL, "\"tutti i pesci sono uomini\" (premessa maggiore)")


# --- Blocco 2: regole di inferenza, condizioni, opposizioni, fallacie (voci di Wikipedia, CC BY-SA 4.0) ---
W = lambda voce: f"Wikipedia, «{voce}» (CC BY-SA 4.0)"
MP = "Wikipedia_Modus-ponens.txt"
MT = "Wikipedia_Modus-tollens.txt"
CNS = "Wikipedia_Condizione-necessaria-e-sufficiente.txt"
QO = "Wikipedia_Quadrato-delle-opposizioni.txt"
FAL = "Wikipedia_Fallacia.txt"
PM = "Wikipedia_Paradosso-del-mentitore.txt"
VEN = "Wikipedia_Diagramma-di-Venn.txt"
INS = "Wikipedia_Insieme.txt"
CAS = "Wikipedia_Principio-dei-cassetti.txt"

D("log-018", "Inferenza", 2, "«Se piove, la strada è bagnata. Piove.» Cosa si può concludere?",
  "La strada è bagnata", ["Non piove", "La strada non è bagnata", "Nulla"],
  "È il modus ponens: da «p implica q» e «p» segue «q».",
  W("Modus ponens"), MP, "Se p implica q è una proposizione vera, e anche la premessa p è vera, allora la conseguenza q è vera")

D("log-019", "Inferenza", 3, "«Se piove, la strada è bagnata. La strada non è bagnata.» Cosa si può concludere?",
  "Non piove", ["Piove", "La strada è asciutta perché c'è il sole", "Nulla"],
  "È il modus tollens: da «p implica q» e «non q» segue «non p».",
  W("Modus tollens"), MT, "il modo che toglie la verità di una proposizione togliendo quella di un'altra")

D("log-020", "Inferenza", 4, "«Se studio, passo l'esame. Ho passato l'esame. Quindi ho studiato.» Il ragionamento è:",
  "Non valido: è la fallacia dell'affermazione del conseguente", ["Valido per modus ponens", "Valido per modus tollens", "Valido perché le premesse sono vere"],
  "Il conseguente può essere vero anche se l'antecedente è falso.",
  W("Fallacia"), FAL, "Fallacia dell'affermazione del conseguente")

D("log-021", "Inferenza", 4, "«Se è italiano, è europeo. Non è italiano. Quindi non è europeo.» Il ragionamento è:",
  "Non valido: è la negazione dell'antecedente", ["Valido per modus tollens", "Valido per modus ponens", "Un sillogismo valido"],
  "Si può essere europei senza essere italiani.",
  W("Fallacia"), FAL, "In questo caso ci troviamo di fronte a una negazione dell'antecedente")

D("log-022", "Inferenza", 3, "Cosa significa letteralmente «modus ponens»?",
  "«Modo che afferma»", ["«Modo che toglie»", "«Modo del dubbio»", "«Modo della prova»"],
  "Voce «Modus ponens».",
  W("Modus ponens"), MP, "(\"modo che afferma\"")

D("log-023", "Condizioni", 3, "Quando una condizione Q è «necessaria» per P?",
  "Quando P implica Q", ["Quando Q implica P", "Quando P e Q sono sempre false", "Quando Q è vera solo a volte"],
  "Esempio: respirare è necessario per vivere, ma non sufficiente.",
  W("Condizione necessaria e sufficiente"), CNS, "una condizione Q è necessaria per una proposizione P se P implica Q")

D("log-024", "Condizioni", 3, "Quando una condizione Q è «sufficiente» per P?",
  "Quando Q implica P", ["Quando P implica Q", "Quando Q è falsa", "Quando P è falsa"],
  "Esempio: essere divisibile per 6 è sufficiente per essere pari, ma non necessario.",
  W("Condizione necessaria e sufficiente"), CNS, "una condizione Q è sufficiente per una proposizione P se Q implica P")

D("log-025", "Condizioni", 3, "Essere divisibile per 6, per un numero, rispetto all'essere pari, è condizione:",
  "Sufficiente ma non necessaria", ["Necessaria ma non sufficiente", "Necessaria e sufficiente", "Né necessaria né sufficiente"],
  "Esistono numeri pari non divisibili per 6 (es. 4).",
  W("Condizione necessaria e sufficiente"), CNS, "la divisibilità per 6 di un numero è sufficiente affinché il numero sia pari, ma non è necessaria")

D("log-026", "Condizioni", 3, "Per un numero primo maggiore di 2, essere dispari è condizione:",
  "Necessaria ma non sufficiente", ["Sufficiente ma non necessaria", "Necessaria e sufficiente", "Né necessaria né sufficiente"],
  "Tutti i primi maggiori di 2 sono dispari, ma non tutti i dispari sono primi (es. 9).",
  W("Condizione necessaria e sufficiente"), CNS, "è necessario che un numero primo maggiore di 2 sia dispari")

D("log-027", "Condizioni", 4, "«Solo se hai il biglietto puoi entrare». Quale affermazione è sicuramente vera?",
  "Se sei entrato, hai il biglietto", ["Se hai il biglietto, entri sicuramente", "Se non sei entrato, non hai il biglietto", "Chi ha il biglietto deve entrare"],
  "«Solo se» indica la condizione necessaria: entrare implica avere il biglietto.",
  W("Condizione necessaria e sufficiente"), CNS, "\"ogni volta che Q è vera, anche P è vera\"")

D("log-028", "Opposizioni", 2, "Qual è la proposizione di tipo «A» nel quadrato aristotelico?",
  "L'universale affermativa («ogni S è P»)", ["L'universale negativa", "La particolare affermativa", "La particolare negativa"],
  "E = universale negativa, I = particolare affermativa, O = particolare negativa.",
  W("Quadrato delle opposizioni"), QO, "l'universale affermativa (universalis affirmativa)")

D("log-029", "Opposizioni", 3, "Quale tipo di proposizione è «alcuni S non sono P»?",
  "O, particolare negativa", ["A, universale affermativa", "E, universale negativa", "I, particolare affermativa"],
  "Voce «Quadrato delle opposizioni».",
  W("Quadrato delle opposizioni"), QO, "la particolare negativa (particularis negativa)")

D("log-030", "Opposizioni", 3, "Qual è la contraddittoria di «ogni uomo è bianco»?",
  "«Qualche uomo non è bianco»", ["«Nessun uomo è bianco»", "«Qualche uomo è bianco»", "«Ogni uomo è nero»"],
  "Tra contraddittorie una è sempre vera e l'altra falsa.",
  W("Quadrato delle opposizioni"), QO, "Esempi di contraddizioni sono 'ogni uomo è bianco' e 'qualche uomo non è bianco'")

D("log-031", "Opposizioni", 4, "«Ogni uomo è bianco» e «nessun uomo è bianco» sono proposizioni:",
  "Contrarie: non possono essere entrambe vere", ["Contraddittorie", "Subalterne", "Equivalenti"],
  "Possono però essere entrambe false.",
  W("Quadrato delle opposizioni"), QO, "sono tali che entrambe non possono, allo stesso tempo, essere vere")

D("log-032", "Fallacie", 3, "Come si chiama l'argomento che attacca chi sostiene una tesi invece della tesi stessa?",
  "Argumentum ad hominem", ["Petitio principii", "Ad verecundiam", "Modus tollens"],
  "Voce «Fallacia».",
  W("Fallacia"), FAL, "Argumentum ad hominem")

D("log-033", "Fallacie", 4, "Come si chiama la fallacia in cui la conclusione è già contenuta nella premessa?",
  "Petitio principii", ["Ad hominem", "Falso dilemma", "Ad verecundiam"],
  "Voce «Fallacia».",
  W("Fallacia"), FAL, "premessa è già contenuta la conclusione")

D("log-034", "Fallacie", 4, "La domanda «Hai smesso di rapinare banche?» è un esempio di:",
  "Domanda complessa (multipla)", ["Modus ponens", "Sillogismo valido", "Tautologia"],
  "Dà per scontato qualcosa non dimostrato.",
  W("Fallacia"), FAL, "Esempio: Hai smesso di rapinare banche?")

D("log-035", "Paradossi", 3, "Quale celebre paradosso nasce dalla frase «questa frase è falsa»?",
  "Il paradosso del mentitore", ["Il paradosso di Zenone", "Il paradosso del barbiere", "Il paradosso del sorite"],
  "È attribuito al megarico Eubulide; una versione è legata a Epimenide.",
  W("Paradosso del mentitore"), PM, "data una proposizione autonegante come \"Questa frase è falsa\"")

D("log-036", "Paradossi", 4, "A quale filosofo è tradizionalmente attribuita l'ideazione del paradosso del mentitore («io sto mentendo»)?",
  "Eubulide di Mileto", ["Zenone di Elea", "Aristotele", "Socrate"],
  "Voce «Paradosso del mentitore».",
  W("Paradosso del mentitore"), PM, "Eubulide di Mileto")

D("log-037", "Insiemi", 1, "Cos'è l'intersezione di due insiemi A e B?",
  "L'insieme degli elementi che appartengono sia ad A sia a B", ["L'insieme degli elementi di A o di B", "L'insieme degli elementi di A non in B", "L'insieme vuoto"],
  "L'unione è invece l'insieme degli elementi di A o di B.",
  W("Insieme"), INS, "è data dall'insieme formato da tutti gli elementi che appartengono sia")

D("log-038", "Insiemi", 1, "Come si chiama l'insieme che non contiene alcun elemento?",
  "Insieme vuoto", ["Insieme universo", "Insieme unitario", "Insieme complementare"],
  "Si indica con ∅ o { }.",
  W("Insieme"), INS, "Insieme vuoto è l'insieme che non contiene nessun elemento")

D("log-039", "Insiemi", 2, "Quando A è sottoinsieme di B?",
  "Quando tutti gli elementi di A appartengono anche a B", ["Quando A e B non hanno elementi in comune", "Quando A ha più elementi di B", "Quando B è vuoto"],
  "Voce «Insieme».",
  W("Insieme"), INS, "quando tutti gli elementi di A")

D("log-040", "Insiemi", 3, "A = {1, 2, 3, 4}, B = {3, 4, 5}. Quanto vale A ∩ B?",
  "{3, 4}", ["{1, 2, 3, 4, 5}", "{1, 2}", "{5}"],
  "Intersezione: elementi comuni.",
  W("Insieme"), INS, "L'intersezione di due insiemi")

D("log-041", "Insiemi", 3, "A = {1, 2, 3, 4}, B = {3, 4, 5}. Quanto vale A ∪ B?",
  "{1, 2, 3, 4, 5}", ["{3, 4}", "{1, 2}", "{1, 2, 5}"],
  "Unione: tutti gli elementi di A o di B.",
  W("Insieme"), INS, "Le principali operazioni tra insiemi sono")

D("log-042", "Insiemi", 3, "In una classe di 30 studenti, 18 studiano inglese, 15 francese e 7 entrambe. Quanti non studiano nessuna delle due lingue?",
  "4", ["0", "7", "12"],
  "Inglese o francese = 18 + 15 − 7 = 26; 30 − 26 = 4. Il diagramma di Venn aiuta a visualizzarlo.",
  W("Diagramma di Venn"), VEN, "mostra tutte le possibili relazioni logiche tra una collezione finita di insiemi")

D("log-043", "Insiemi", 4, "Su 100 dipendenti, 60 usano l'auto, 50 il treno e 25 entrambi. Quanti usano solo il treno?",
  "25", ["50", "35", "15"],
  "Solo treno = 50 − 25 = 25.",
  W("Diagramma di Venn"), VEN, "un diagramma di Venn (detto anche diagramma di Eulero-Venn)")

D("log-044", "Insiemi", 2, "Chi propose nel 1880 il diagramma che porta il suo nome per rappresentare relazioni tra insiemi?",
  "John Venn", ["Leonhard Euler da solo", "George Boole", "Gottlob Frege"],
  "Voce «Diagramma di Venn».",
  W("Diagramma di Venn"), VEN, "proposto nel 1880 dal matematico inglese John Venn")

D("log-045", "Combinatoria", 3, "In un cassetto ci sono calzini neri e bianchi mescolati al buio. Quanti calzini bisogna prendere, come minimo, per essere sicuri di averne due dello stesso colore?",
  "3", ["2", "4", "5"],
  "Principio dei cassetti: con 2 colori («cassetti»), 3 calzini garantiscono una coppia.",
  W("Principio dei cassetti"), CAS, "se n+k oggetti sono messi in n cassetti, allora almeno un cassetto deve contenere più di un oggetto")

D("log-046", "Combinatoria", 3, "In un gruppo di 13 persone, cosa si può dire con certezza?",
  "Almeno due sono nate nello stesso mese", ["Almeno due sono nate lo stesso giorno", "Tutte sono nate in mesi diversi", "Nessuna conclusione"],
  "13 persone in 12 mesi: per il principio dei cassetti almeno un mese ne contiene due.",
  W("Principio dei cassetti"), CAS, "allora almeno un cassetto deve contenere più di un oggetto")

D("log-047", "Combinatoria", 4, "A chi si attribuisce la prima formulazione esplicita del principio dei cassetti (1834)?",
  "Dirichlet", ["Pascal", "Fermat", "Gauss"],
  "In russo è noto come principio di Dirichlet.",
  W("Principio dei cassetti"), CAS, "esplicitato per la prima volta da Dirichlet nel 1834")


# --- Blocco 3: serie numeriche, combinatoria, probabilità, numeri primi, medie ---
# I calcoli sono verificati a parte; la frase di prova riporta la regola applicata.
PA = "Wikipedia_Progressione-aritmetica.txt"
PG = "Wikipedia_Progressione-geometrica.txt"
FIB = "Wikipedia_Successione-di-Fibonacci.txt"
FAT = "Wikipedia_Fattoriale.txt"
CC = "Wikipedia_Calcolo-combinatorio.txt"
PRO = "Wikipedia_Probabilità.txt"
PRI = "Wikipedia_Numero-primo.txt"
MED = "Wikipedia_Media-statistica.txt"
DED = "Wikipedia_Deduzione.txt"
IND = "Wikipedia_Induzione.txt"
R_PA = "la differenza tra ciascun termine (o elemento) della successione e il suo precedente sia una costante"
R_PG = "il rapporto tra un elemento ed il suo precedente sia sempre costante"
R_FIB = "ciascun numero è la somma dei due precedenti"
R_FAT = "il prodotto dei numeri interi positivi minori o uguali a tale numero"
R_PERM = "Una permutazione di un insieme di oggetti è una presentazione ordinata"
R_COMB = "combinazione semplice una presentazione di elementi di un insieme nella quale non ha importanza l'ordine dei componenti"
R_DISP = "se l'ordinamento è importante"
R_RIP = "se si possono avere più ripetizioni di uno stesso oggetto"
R_PRO = "il rapporto tra casi favorevoli e casi possibili"
R_INC = "la probabilità del verificarsi di uno di due eventi incompatibili"
R_PRI = "un numero intero positivo che abbia esattamente due divisori distinti"
R_MED = "con il termine media si intende comunemente la media aritmetica"
R_POND = "media aritmetica ponderata (o media pesata) viene calcolata sommando i valori in analisi"

def S(id, liv, testo, giusta, sbagliate, spieg, voce, file, frase, arg="Serie numeriche"):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W(voce), file, frase)

S("log-048", 1, "Completa la serie: 2, 5, 8, 11, ...", "14", ["13", "15", "16"],
  "Progressione aritmetica di ragione 3.", "Progressione aritmetica", PA, R_PA)
S("log-049", 2, "Completa la serie: 100, 93, 86, 79, ...", "72", ["73", "71", "69"],
  "Progressione aritmetica di ragione −7.", "Progressione aritmetica", PA, R_PA)
S("log-050", 1, "Completa la serie: 3, 6, 12, 24, ...", "48", ["36", "30", "42"],
  "Progressione geometrica di ragione 2.", "Progressione geometrica", PG, R_PG)
S("log-051", 2, "Completa la serie: 81, 27, 9, 3, ...", "1", ["0", "2", "1/3"],
  "Progressione geometrica di ragione 1/3.", "Progressione geometrica", PG, R_PG)
S("log-052", 2, "Completa la serie: 2, 6, 18, 54, ...", "162", ["108", "72", "216"],
  "Ogni termine è il triplo del precedente.", "Progressione geometrica", PG, R_PG)
S("log-053", 2, "Completa la serie: 64, 32, 16, 8, ...", "4", ["2", "6", "0"],
  "Progressione geometrica di ragione 1/2.", "Progressione geometrica", PG, R_PG)
S("log-054", 3, "In una progressione aritmetica il primo termine è 4 e la ragione è 5. Quanto vale il decimo termine?",
  "49", ["50", "54", "45"], "a₁₀ = a₁ + 9·d = 4 + 45 = 49.", "Progressione aritmetica", PA, "Tale costante viene detta ragione della progressione")
S("log-055", 3, "Quanto vale la somma dei numeri interi da 1 a 100?", "5050", ["5000", "10100", "4950"],
  "Somma di una progressione aritmetica: n·(a₁ + aₙ)/2 = 100·101/2 = 5050.", "Progressione aritmetica", PA, "La somma dei numeri di una progressione aritmetica finita si chiama serie aritmetica")
S("log-056", 3, "Completa la serie: 1, 4, 9, 16, 25, ...", "36", ["30", "35", "49"],
  "Sono i quadrati; le differenze 3, 5, 7, 9 formano una progressione aritmetica di ragione 2, quindi la successiva è 11.", "Progressione aritmetica", PA, R_PA)
S("log-057", 3, "Completa la serie: 1, 2, 4, 7, 11, 16, ...", "22", ["21", "20", "23"],
  "Le differenze crescono di 1 (1, 2, 3, 4, 5): la successiva è 6.", "Progressione aritmetica", PA, R_PA)
S("log-058", 4, "Completa la serie: 1, 3, 2, 4, 3, 5, ...", "4", ["6", "2", "5"],
  "Due progressioni alternate: 1, 2, 3, 4… (posti dispari) e 3, 4, 5… (posti pari). Il settimo termine è 4.", "Progressione aritmetica", PA, R_PA)
S("log-059", 2, "Completa la serie: 1, 1, 2, 3, 5, 8, 13, ...", "21", ["18", "20", "26"],
  "È la successione di Fibonacci: ogni termine è la somma dei due precedenti.", "Successione di Fibonacci", FIB, R_FIB)
S("log-060", 3, "Completa la serie: 2, 3, 5, 8, 13, ...", "21", ["18", "19", "26"],
  "Ogni termine è la somma dei due precedenti (8 + 13).", "Successione di Fibonacci", FIB, R_FIB)
S("log-061", 3, "Completa la serie: 4, 7, 11, 18, 29, ...", "47", ["40", "36", "58"],
  "Ogni termine è la somma dei due precedenti (18 + 29), come nella successione di Fibonacci.", "Successione di Fibonacci", FIB, R_FIB)
S("log-062", 2, "In quale opera Leonardo Fibonacci presentò nel 1202 il problema da cui nasce la sua successione?",
  "Liber abbaci", ["Ars conjectandi", "Elementi", "Summa de arithmetica"],
  "Voce «Successione di Fibonacci».", "Successione di Fibonacci", FIB, "Nel 1202 il matematico pisano Leonardo Fibonacci pubblicò il Liber abbaci")
S("log-063", 2, "Completa la serie: 5, 10, 20, 40, ...", "80", ["60", "50", "45"],
  "Progressione geometrica di ragione 2.", "Progressione geometrica", PG, R_PG)
S("log-064", 3, "Completa la serie: 3, 5, 9, 17, 33, ...", "65", ["49", "66", "57"],
  "Le differenze raddoppiano (2, 4, 8, 16): la successiva è 32, quindi 33 + 32 = 65.", "Progressione geometrica", PG, R_PG)
S("log-065", 2, "Come si chiama la costante che si somma a ogni termine di una progressione aritmetica per ottenere il successivo?",
  "Ragione", ["Base", "Modulo", "Esponente"], "Voce «Progressione aritmetica».", "Progressione aritmetica", PA, "Tale costante viene detta ragione della progressione")

S("log-066", 1, "Quanto vale 5! (5 fattoriale)?", "120", ["25", "60", "720"],
  "5! = 5·4·3·2·1 = 120.", "Fattoriale", FAT, R_FAT, "Calcolo combinatorio")
S("log-067", 2, "Quanto vale 0! per convenzione?", "1", ["0", "Non è definito", "Infinito"],
  "Per la convenzione del prodotto vuoto 0! = 1.", "Fattoriale", FAT, "per la convenzione del prodotto vuoto si definisce inoltre", "Calcolo combinatorio")
S("log-068", 3, "Quanto vale 6! / 4!?", "30", ["2", "24", "720"],
  "6!/4! = 6·5 = 30.", "Fattoriale", FAT, R_FAT, "Calcolo combinatorio")
S("log-069", 4, "Chi introdusse nel 1807 la notazione n! con il punto esclamativo?",
  "Christian Kramp", ["Leonhard Euler", "Blaise Pascal", "Antoine Arbogast"],
  "Il nome «fattoriale» si deve invece ad Arbogast (1800).", "Fattoriale", FAT, "La notazione con il punto esclamativo è stata introdotta nel 1807 da Christian Kramp", "Calcolo combinatorio")
S("log-070", 2, "Quanti anagrammi (anche senza significato) si possono formare con le lettere della parola MONTE?",
  "120", ["25", "60", "5"], "5 lettere distinte: 5! = 120 permutazioni.", "Calcolo combinatorio", CC, "In quanti modi possibili si può anagrammare la parola", "Calcolo combinatorio")
S("log-071", 2, "In quanti modi diversi si possono sedere 4 persone su 4 sedie in fila?",
  "24", ["16", "4", "12"], "Permutazioni di 4 elementi: 4! = 24.", "Calcolo combinatorio", CC, R_PERM, "Calcolo combinatorio")
S("log-072", 3, "In una gara con 8 atleti, quanti sono i possibili podi (oro, argento, bronzo) diversi?",
  "336", ["56", "24", "512"], "L'ordine conta, senza ripetizioni: 8·7·6 = 336 disposizioni.", "Calcolo combinatorio", CC, R_DISP, "Calcolo combinatorio")
S("log-073", 3, "Quante coppie diverse si possono formare scegliendo 2 persone da un gruppo di 5?",
  "10", ["20", "25", "5"], "Combinazioni: (5·4)/2 = 10, perché l'ordine non conta.", "Calcolo combinatorio", CC, R_COMB, "Calcolo combinatorio")
S("log-074", 3, "In una riunione di 10 persone ciascuno stringe la mano a tutti gli altri una volta. Quante strette di mano ci sono?",
  "45", ["90", "100", "50"], "Combinazioni di 10 elementi a 2 a 2: 10·9/2 = 45.", "Calcolo combinatorio", CC, R_COMB, "Calcolo combinatorio")
S("log-075", 3, "In quanti modi si possono scegliere 3 libri da uno scaffale di 6 libri diversi, senza contare l'ordine?",
  "20", ["120", "18", "216"], "Combinazioni: 6·5·4/(3·2·1) = 20.", "Calcolo combinatorio", CC, R_COMB, "Calcolo combinatorio")
S("log-076", 2, "Quanti codici PIN di 4 cifre (da 0 a 9, ripetizioni ammesse) esistono?",
  "10.000", ["5.040", "40", "9.999"], "Disposizioni con ripetizione: 10⁴ = 10.000.", "Calcolo combinatorio", CC, R_RIP, "Calcolo combinatorio")
S("log-077", 3, "Quante sequenze diverse di 3 lanci di moneta (testa/croce) sono possibili?",
  "8", ["6", "3", "9"], "Disposizioni con ripetizione di 2 esiti su 3 posti: 2³ = 8.", "Calcolo combinatorio", CC, R_RIP, "Calcolo combinatorio")
S("log-078", 3, "Quale differenza c'è tra una disposizione e una combinazione?",
  "Nella disposizione conta l'ordine, nella combinazione no", ["Nella combinazione conta l'ordine, nella disposizione no", "Sono sinonimi", "La combinazione ammette sempre ripetizioni"],
  "Voce «Calcolo combinatorio».", "Calcolo combinatorio", CC, R_COMB, "Calcolo combinatorio")
S("log-079", 4, "Un menù offre 3 primi, 4 secondi e 2 dolci. Quanti pasti diversi (un primo, un secondo, un dolce) si possono comporre?",
  "24", ["9", "12", "36"], "Principio di moltiplicazione: 3·4·2 = 24.", "Calcolo combinatorio", CC, "il primo elemento della configurazione può essere scelto in", "Calcolo combinatorio")

S("log-080", 1, "Qual è la probabilità di ottenere 6 lanciando un dado regolare?", "1/6", ["1/3", "1/2", "6"],
  "Un caso favorevole su sei possibili.", "Probabilità", PRO, R_PRO, "Probabilità")
S("log-081", 1, "Qual è la probabilità di ottenere un numero pari lanciando un dado regolare?", "1/2", ["1/6", "1/3", "2/3"],
  "Tre casi favorevoli (2, 4, 6) su sei.", "Probabilità", PRO, R_PRO, "Probabilità")
S("log-082", 2, "Un'urna contiene 3 palline rosse e 7 bianche. Qual è la probabilità di estrarre una rossa?", "3/10", ["3/7", "7/10", "1/3"],
  "3 casi favorevoli su 10 possibili.", "Probabilità", PRO, R_PRO, "Probabilità")
S("log-083", 2, "Da un mazzo di 40 carte napoletane, qual è la probabilità di estrarre un asso?", "1/10", ["1/40", "1/4", "4/10"],
  "4 assi su 40 carte: 4/40 = 1/10.", "Probabilità", PRO, R_PRO, "Probabilità")
S("log-084", 3, "Lanciando due monete, qual è la probabilità di ottenere due teste?", "1/4", ["1/2", "1/3", "2/3"],
  "Casi possibili TT, TC, CT, CC: uno solo è favorevole.", "Probabilità", PRO, R_PRO, "Probabilità")
S("log-085", 3, "Lanciando due dadi, qual è la probabilità che la somma sia 7?", "1/6", ["1/12", "7/36", "1/36"],
  "6 coppie favorevoli (1-6, 2-5, 3-4, 4-3, 5-2, 6-1) su 36.", "Probabilità", PRO, R_PRO, "Probabilità")
S("log-086", 3, "Lanciando due dadi, qual è la probabilità che la somma sia 12?", "1/36", ["1/12", "1/6", "2/36"],
  "Solo la coppia 6-6 su 36 casi possibili.", "Probabilità", PRO, R_PRO, "Probabilità")
S("log-087", 2, "Qual è la probabilità di NON ottenere 6 lanciando un dado?", "5/6", ["1/6", "1/2", "6/5"],
  "Cinque casi favorevoli su sei.", "Probabilità", PRO, R_PRO, "Probabilità")
S("log-088", 2, "Ottenere 1 come somma lanciando due dadi è un esempio di evento:", "Impossibile", ["Certo", "Probabile", "Indipendente"],
  "La somma minima con due dadi è 2.", "Probabilità", PRO, "evento impossibile (ottenere 1 come somma dal lancio di due dadi)", "Probabilità")
S("log-089", 2, "Che probabilità ha un evento certo?", "1", ["0", "1/2", "100"],
  "La probabilità va da 0 (evento impossibile) a 1 (evento certo).", "Probabilità", PRO, "detti evento certo", "Probabilità")
S("log-090", 3, "Lanciando un dado, qual è la probabilità di ottenere 1 oppure 2?", "1/3", ["1/6", "1/36", "1/2"],
  "Eventi incompatibili: le probabilità si sommano, 1/6 + 1/6 = 1/3.", "Probabilità", PRO, R_INC, "Probabilità")
S("log-091", 4, "Lanciando due volte un dado, qual è la probabilità di ottenere 6 entrambe le volte?", "1/36", ["1/12", "1/6", "2/6"],
  "Eventi indipendenti: le probabilità si moltiplicano, 1/6 · 1/6.", "Probabilità", PRO, "vengono definiti indipendenti stocasticamente", "Probabilità")
S("log-092", 3, "A chi viene attribuita la nascita del concetto moderno di probabilità?", "Pascal e Fermat", ["Galileo e Cardano", "Newton e Leibniz", "Euclide e Pitagora"],
  "Dalla loro corrispondenza del 1654.", "Probabilità", PRO, "La nascita del concetto moderno di probabilità viene attribuita a Pascal e Fermat", "Probabilità")

S("log-093", 1, "Qual è l'unico numero primo pari?", "2", ["0", "4", "Nessuno"],
  "Tutti gli altri pari sono divisibili per 2.", "Numero primo", PRI, "L'unico numero primo pari è 2", "Numeri")
S("log-094", 2, "Quale di questi numeri è primo?", "59", ["51", "57", "91"],
  "51 = 3·17, 57 = 3·19, 91 = 7·13.", "Numero primo", PRI, R_PRI, "Numeri")
S("log-095", 2, "Quanti sono i numeri primi minori di 20?", "8", ["7", "9", "10"],
  "2, 3, 5, 7, 11, 13, 17, 19.", "Numero primo", PRI, "La successione dei numeri primi comincia con 2, 3, 5, 7, 11, 13, 17, 19", "Numeri")
S("log-096", 2, "Il numero 1 è primo?", "No: un primo deve essere maggiore di 1 e avere esattamente due divisori", ["Sì, è il primo numero primo", "Sì, perché è divisibile solo per sé stesso", "Dipende dalla convenzione"],
  "Voce «Numero primo».", "Numero primo", PRI, "un numero naturale maggiore di 1 che sia divisibile solamente per 1 e per sé stesso", "Numeri")
S("log-097", 3, "Quanti sono i numeri primi?", "Infiniti", ["100", "Circa un milione", "Un numero finito ancora sconosciuto"],
  "Già dimostrato da Euclide.", "Numero primo", PRI, "I primi sono inoltre infiniti", "Numeri")
S("log-098", 2, "Qual è la media aritmetica di 4, 8, 6, 10, 2?", "6", ["5", "7", "30"],
  "(4 + 8 + 6 + 10 + 2) / 5 = 30 / 5 = 6.", "Media (statistica)", MED, R_MED, "Numeri")
S("log-099", 3, "Uno studente ha preso 26, 28, 27 e 29 in quattro esami. Quanto deve prendere nel quinto per avere media 27?",
  "25", ["27", "26", "24"], "Totale necessario 27·5 = 135; 135 − 110 = 25.", "Media (statistica)", MED, R_MED, "Numeri")
S("log-100", 4, "Un esame da 6 crediti con voto 30 e uno da 12 crediti con voto 24: qual è la media ponderata sui crediti?",
  "26", ["27", "25", "28"], "(30·6 + 24·12) / 18 = 468 / 18 = 26.", "Media (statistica)", MED, R_POND, "Numeri")


# --- Blocco 4: connettivi, sillogismi, principi logici, quesiti dei Giochi di Archimede ---
LP = "Wikipedia_Logica-proposizionale.txt"
ES = "MatematicaC3_Esercizi-logica.txt"
PNC = "Wikipedia_Principio-di-non-contraddizione.txt"
TND = "Wikipedia_Tertium-non-datur.txt"
ABD = "Wikipedia_Abduzione.txt"
MH = "Wikipedia_Problema-di-Monty-Hall.txt"
HAN = "Wikipedia_Torre-di-Hanoi.txt"
PERF = "Wikipedia_Numero-perfetto.txt"
PAR = "Wikipedia_Paradosso.txt"
ME = "MatematicaC3, Esercizi di logica (CC BY 3.0)"

D("log-101", "Connettivi", 2, "Perché la negazione si dice operatore «unario»?",
  "Perché agisce su un'unica proposizione", ["Perché ha un solo valore di verità", "Perché è sempre vera", "Perché lega due proposizioni"],
  "Congiunzione e disgiunzione legano invece due proposizioni.", M, LOG, "è un operatore che, a differenza dei precedenti, non lega più proposizioni ma agisce su un'unica proposizione")
D("log-102", "Implicazione", 3, "Quando è vera la doppia implicazione «p se e solo se q»?",
  "Quando p e q hanno lo stesso valore di verità", ["Solo quando p e q sono entrambe vere", "Quando almeno una è vera", "Quando hanno valori opposti"],
  "v(x↔y) = V se e solo se v(x) = v(y).", W("Logica proposizionale"), LP, "v(x↔y) = V se e solo se v(x) = v(y)")
D("log-103", "Implicazione", 3, "In quale unico caso l'implicazione «se p allora q» è falsa?",
  "Quando p è vera e q è falsa", ["Quando p è falsa e q è vera", "Quando entrambe sono false", "Quando entrambe sono vere"],
  "È vera se l'antecedente è falso oppure il conseguente è vero.", W("Logica proposizionale"), LP, "v(x→y) = V se e solo se v(x) = F oppure v(y) = V")
D("log-104", "Implicazione", 3, "Data l'implicazione «se p allora q», come si chiama l'implicazione «se q allora p»?",
  "Inversa", ["Contraria", "Contronominale", "Equivalente"],
  "La contraria è «se non p allora non q», la contronominale «se non q allora non p».", M, LOG, "l'implicazione q ⇒ p si dice inversa di p ⇒ q")
D("log-105", "Implicazione", 3, "Data l'implicazione «se p allora q», come si chiama «se non p allora non q»?",
  "Contraria", ["Inversa", "Contronominale", "Doppia implicazione"],
  "Voce del manuale MatematicaC3.", M, LOG, "l'implicazione ¬p ⇒ ¬q si dice contraria di p ⇒ q")
D("log-106", "Implicazione", 3, "Come si chiama anche la contronominale di un'implicazione?",
  "Controinversa", ["Contraria", "Inversa", "Reciproca"],
  "La contronominale di «p ⇒ q» è «¬q ⇒ ¬p».", M, LOG, "si dice contronominale (o controinversa) di p ⇒ q")
D("log-107", "Inferenza", 2, "«Se un numero è multiplo di 10 allora è pari. Il numero n non è pari.» Quindi:",
  "n non è multiplo di 10", ["n è multiplo di 10", "n è dispari e multiplo di 5", "Non si può concludere nulla"],
  "Modus tollens.", ME, ES, "Se un numero è multiplo di 10 allora è pari")
D("log-108", "Quantificatori", 2, "Quale numero è un controesempio all'affermazione «tutti i multipli di 3 sono dispari»?",
  "6", ["9", "15", "21"], "6 è multiplo di 3 ed è pari: basta un controesempio per smentire un'affermazione universale.",
  ME, ES, "Dimostra con un controesempio che non è vera l'affermazione")
D("log-109", "Quantificatori", 3, "Qual è la negazione di «Ogni volta che ho preso l'ombrello non è piovuto»?",
  "Almeno una volta sono uscito con l'ombrello ed è piovuto", ["Quando esco senza ombrello piove sempre", "Tutti i giorni in cui non piove esco con l'ombrello", "Tutti i giorni che è piovuto ho preso l'ombrello"],
  "La negazione di «per ogni… non» è «esiste almeno un caso in cui…».", ME, ES, "Almeno una volta sono uscito con l'ombrello ed è piovuto")
D("log-110", "Quantificatori", 2, "Qual è la negazione di «Tutti hanno portato i soldi per la gita»?",
  "Almeno uno non ha portato i soldi per la gita", ["Nessuno ha portato i soldi per la gita", "Tutti non hanno portato i soldi", "Alcuni hanno portato i soldi"],
  "La negazione di un universale affermativo è un particolare negativo.", ME, ES, "Tutti hanno portato i soldi per la gita")
D("log-111", "Quantificatori", 4, "Qual è la negazione di «In ogni scuola c'è almeno una classe in cui sono tutti promossi»?",
  "C'è almeno una scuola che ha almeno un bocciato in ogni classe", ["In ogni scuola c'è almeno una classe in cui sono tutti bocciati", "In ogni scuola c'è almeno un bocciato in tutte le classi", "C'è almeno una scuola in cui c'è una classe con almeno un bocciato"],
  "Si scambiano i quantificatori («ogni» ↔ «almeno uno») e si nega il predicato. Quesito dei Giochi di Archimede 1999.", ME, ES, "In ogni scuola c'è almeno una classe in cui sono tutti promossi")
D("log-112", "Implicazione", 2, "p = «Mario è cittadino romano», q = «Mario è cittadino italiano». Quale implicazione è sempre vera?",
  "p ⇒ q", ["q ⇒ p", "p ⇔ q", "q ⇒ ¬p"], "Ogni cittadino romano è italiano, ma non viceversa.", ME, ES, "Mario è cittadino romano")
D("log-113", "Connettivi", 3, "p = «18 è divisibile per 3», q = «18 è un numero dispari». Quale proposizione è vera?",
  "p ∧ ¬q", ["p ∧ q", "¬p", "¬p ∧ ¬q"], "p è vera e q è falsa, quindi ¬q è vera.", ME, ES, "18 è numero dispari")
D("log-114", "Connettivi", 4, "A quale proposizione equivale (¬p ∧ q) ∨ (p ∧ ¬q)?",
  "Alla disgiunzione esclusiva «o p o q»", ["Alla congiunzione «p e q»", "Alla doppia implicazione «p se e solo se q»", "Alla tautologia «p o non p»"],
  "È vera quando esattamente una delle due è vera.", ME, ES, "è equivalente alla proposizione p Y q")
D("log-115", "Proposizioni", 2, "Quale di queste frasi è una proposizione logica?",
  "«12 è un numero dispari»", ["«Per favore, fate silenzio»", "«Lucia è una bella ragazza»", "«I matematici sono intelligenti»"],
  "Una proposizione deve poter essere oggettivamente vera o falsa: «12 è dispari» è falsa, ma è una proposizione.", ME, ES, "Quali delle seguenti frasi sono proposizioni logiche?")
D("log-116", "Problemi logici", 4, "Quattro amiche: Carla dice «Non sono né la più giovane né la più anziana», Liliana «Non sono la più giovane», Milena «Sono la più giovane», Anna «Sono la più anziana». Solo una mente. Chi è la più giovane?",
  "Milena", ["Carla", "Liliana", "Anna"], "Quesito dei Giochi d'autunno 2010; soluzione riportata nel testo.", ME, ES, "Io non sono né la più giovane né la più anziana")
D("log-117", "Problemi logici", 4, "Paolo dice di non essere il capitano; Andrea dice che il capitano è Gabriele; Gabriele dice che il capitano è uno degli altri due. Uno solo dice il vero. Chi è il capitano?",
  "Paolo", ["Andrea", "Gabriele", "Non si può stabilire"],
  "Se fosse Paolo, solo Gabriele direbbe il vero: è l'unico caso coerente. Giochi di Archimede 2011.", ME, ES, "Paolo dice di non essere il capitano")
D("log-118", "Problemi logici", 5, "Il colpevole mente sempre, gli altri dicono il vero. Anna: «Il colpevole è un maschio». Cecilia: «È stata Anna oppure Enrico». Enrico: «Se Bruno è colpevole allora Anna è innocente». Chi è il colpevole?",
  "Anna", ["Bruno", "Cecilia", "Enrico"], "Giochi di Archimede 2010; soluzione riportata nel testo.", ME, ES, "Il colpevole è un maschio")
D("log-119", "Problemi logici", 4, "È falso che «su Papilla sono tutti grassi e sporchi». Quale affermazione è sicuramente vera?",
  "Se tutti gli abitanti sono sporchi, almeno uno di loro è magro", ["Almeno un abitante è magro e pulito", "Tutti gli abitanti sono magri e puliti", "Almeno un abitante è magro"],
  "Almeno un abitante è magro oppure pulito: se sono tutti sporchi, deve esserci un magro.", ME, ES, "su Papilla sono tutti grassi e sporchi")
D("log-120", "Problemi logici", 5, "«Se il pomeriggio gioco a tennis, la sera ho fame; se la sera ho fame, mangio troppo.» Quale conclusione NON si può trarre?",
  "Se la sera non ho fame, allora non mangio troppo", ["Se gioco a tennis, la sera mangio troppo", "Se la sera non ho fame, non ho giocato a tennis", "Se la sera non mangio troppo, non ho giocato a tennis"],
  "Sarebbe la negazione dell'antecedente: si può mangiare troppo anche senza fame.", ME, ES, "Se il pomeriggio ho giocato a tennis, la sera ho fame")
D("log-121", "Problemi logici", 5, "Su un'isola i cavalieri dicono sempre il vero, i furfanti mentono sempre, i paggi alternano verità e menzogna. Una ragazza dice «Io sono furfante». Che cosa è sicuramente?",
  "Paggio", ["Cavaliere", "Furfante", "Non si può stabilire"],
  "Un cavaliere non lo direbbe (sarebbe falso) e nemmeno un furfante (sarebbe vero): resta il paggio.", ME, ES, "i cavalieri, che dicono sempre la verità, i furfanti, che mentono sempre")
D("log-122", "Problemi logici", 5, "Quattro amici giocano con 20 carte (re, regine, fanti, assi, dieci). Anna: «Ho un poker»; Bea: «Ho cinque carte di cuori»; Caio: «Ho cinque carte rosse»; Dino: «Ho un full». Una sola affermazione è falsa: chi mente?",
  "Bea", ["Anna", "Caio", "Dino"], "Giochi di Archimede 2009; soluzione riportata nel testo.", ME, ES, "Io ho tutte e cinque le carte di cuori")
D("log-123", "Principi logici", 2, "Che cosa afferma il principio di non contraddizione?",
  "Una proposizione e la sua negazione non possono essere entrambe vere", ["Ogni proposizione è vera", "Una proposizione può essere vera e falsa insieme", "Esiste sempre una terza possibilità"],
  "In simboli ¬(A ∧ ¬A).", W("Principio di non contraddizione"), PNC, "il principio di non-contraddizione afferma la falsità di ogni proposizione implicante che una certa proposizione A e la sua negazione")
D("log-124", "Principi logici", 4, "Con quale espressione latina si indica che da una contraddizione segue qualsiasi affermazione?",
  "Ex falso sequitur quodlibet", ["Tertium non datur", "Petitio principii", "Modus ponens"],
  "Nella logica moderna è il «principio di esplosione».", W("Principio di non contraddizione"), PNC, "ex falso sequitur quodlibet")
D("log-125", "Principi logici", 3, "Che cosa significa «tertium non datur»?",
  "Non esiste una terza possibilità oltre al vero e al falso", ["Il terzo termine del sillogismo non è dato", "Tre premesse non bastano", "La terza ipotesi è sempre vera"],
  "È il principio del terzo escluso.", W("Tertium non datur"), TND, "principio logico del terzo escluso")
D("log-126", "Ragionamento", 3, "Che cos'è l'abduzione secondo Aristotele?",
  "Un sillogismo con premessa maggiore certa e premessa minore solo probabile", ["Un ragionamento dal particolare all'universale", "Un sillogismo con premesse entrambe certe", "Un paradosso"],
  "La conclusione è quindi solo probabile.", W("Abduzione"), ABD, "un sillogismo in cui la premessa maggiore è certa mentre quella minore è solamente probabile")
D("log-127", "Ragionamento", 2, "Il metodo deduttivo procede:",
  "Da premesse generali a conclusioni particolari", ["Da casi particolari a una legge universale", "Per tentativi ed errori", "Dalla conclusione alle premesse"],
  "Esempio: «tutti gli uomini sono mortali» → «Socrate è mortale».", W("Deduzione"), DED, "fa derivare una certa conclusione da premesse più generiche")
D("log-128", "Ragionamento", 2, "Il metodo induttivo:",
  "Cerca di stabilire una legge universale partendo da casi particolari", ["Deduce casi particolari da una legge universale", "Coincide con il sillogismo", "Non usa l'esperienza"],
  "È contrapposto al metodo deduttivo.", W("Induzione"), IND, "cerca di stabilire una legge universale partendo da singoli casi particolari")
D("log-129", "Ragionamento", 3, "A chi si deve l'introduzione del concetto di deduzione, identificata con il sillogismo?",
  "Aristotele", ["Platone", "Cartesio", "Kant"], "Voce «Deduzione».", W("Deduzione"), DED, "L'introduzione del concetto di deduzione si deve ad Aristotele")
D("log-130", "Sillogismo", 3, "Nel sillogismo, quale funzione ha il termine maggiore nella conclusione?",
  "È il predicato", ["È il soggetto", "Non compare", "È il termine medio"],
  "Il termine minore fa da soggetto; il medio compare solo nelle premesse.", WS, SIL, "(che funge da predicato nella conclusione)")
D("log-131", "Sillogismo", 2, "«Tutti i dolci sono alimenti; tutte le torte sono dolci.» Quale conclusione segue?",
  "Tutte le torte sono alimenti", ["Tutti gli alimenti sono torte", "Alcuni dolci non sono torte", "Nessuna conclusione"],
  "Schema: se M è A e B è M, allora B è A.", WS, SIL, "tutti i dolci sono alimenti e tutte le torte sono dolci")
D("log-132", "Sillogismo", 3, "«Nessun rettile è un mammifero; tutti i serpenti sono rettili.» Quale conclusione segue?",
  "Nessun serpente è un mammifero", ["Alcuni serpenti sono mammiferi", "Tutti i mammiferi sono serpenti", "Nessuna conclusione"],
  "Premessa universale negativa più universale affermativa.", WS, SIL, "universali negative (\"Nessun A è B\")")
D("log-133", "Sillogismo", 3, "«Alcuni impiegati sono laureati; tutti i laureati hanno un diploma.» Quale conclusione segue?",
  "Alcuni impiegati hanno un diploma", ["Tutti gli impiegati hanno un diploma", "Tutti i diplomati sono impiegati", "Nessun impiegato ha un diploma"],
  "Da una premessa particolare segue una conclusione particolare.", WS, SIL, "particolari affermative (\"Qualche A è B\")")
D("log-134", "Sillogismo", 4, "«Tutti i gatti sono animali; alcuni animali sono neri; quindi alcuni gatti sono neri.» Il ragionamento è:",
  "Non valido: la conclusione non segue dalle premesse", ["Valido", "Valido solo se i gatti esistono", "Valido perché la conclusione è vera"],
  "Gli animali neri potrebbero non essere gatti: premesse vere possono accompagnare una conclusione falsa.", WS, SIL, "non può darsi il caso in cui le proposizioni siano vere e la conclusione sia falsa")
D("log-135", "Sillogismo", 4, "«Gli dei sono immortali; gli uomini non sono dei; dunque gli uomini non sono immortali.» Il sillogismo è:",
  "Non valido, anche se le frasi sono tutte vere", ["Valido", "Valido perché le premesse sono vere", "Valido ma con premesse false"],
  "La verità delle proposizioni non garantisce la validità della forma.", WS, SIL, "Tale sillogismo è non valido logicamente")
D("log-136", "Sillogismo", 3, "«Ogni animale vola; l'asino è un animale; dunque l'asino vola.» Il sillogismo è:",
  "Valido, anche se la premessa maggiore è falsa", ["Non valido", "Valido solo se l'asino vola", "Una fallacia ad hominem"],
  "La validità dipende dalla forma, non dalla verità delle premesse.", WS, SIL, "La validità di un sillogismo non dipende dalla verità delle affermazioni che lo compongono")
D("log-137", "Sillogismo", 3, "Che cosa determina la «figura» di un sillogismo?",
  "La posizione del termine medio nelle premesse", ["Il numero delle premesse", "La verità della conclusione", "La lunghezza delle proposizioni"],
  "Aristotele classificò tre figure; gli scolastici ne aggiunsero una quarta.", WS, SIL, "La posizione del termine medio nelle premesse determina la figura del sillogismo")
D("log-138", "Sillogismo", 4, "Quante figure del sillogismo classificò Aristotele?",
  "Tre (la quarta fu aggiunta dagli scolastici)", ["Quattro", "Due", "Diciannove"],
  "Voce «Sillogismo».", WS, SIL, "Aristotele ne classificò tre, gli scolastici ne aggiunsero una quarta")
D("log-139", "Sillogismo", 3, "Quale di queste frasi NON può essere premessa di un sillogismo?",
  "Una domanda", ["Un'affermazione universale", "Un'affermazione particolare", "Una frase negativa"],
  "Le premesse devono essere enunciati dichiarativi, veri o falsi.", WS, SIL, "Non sono enunciati di tipo dichiarativo le preghiere, le esclamazioni, le domande")
D("log-140", "Sillogismo", 2, "«Marco è più alto di Luca; Luca è più alto di Alberto.» Quindi:",
  "Marco è più alto di Alberto", ["Alberto è più alto di Marco", "Luca è il più alto", "Non si può dire nulla"],
  "È la proprietà transitiva.", WS, SIL, "La proprietà transitiva è l'esempio più elementare del sillogismo")
D("log-141", "Sillogismo", 4, "Nel sillogismo retorico (o dialettico) le premesse sono:",
  "Probabili e non certe", ["Sempre false", "Certe e necessarie", "Solo apparentemente probabili"],
  "Nel sillogismo sofistico la probabilità è solo apparente.", WS, SIL, "sono date per probabili e non per certe")
D("log-142", "Opposizioni", 4, "Le proposizioni subcontrarie («alcuni S sono P» / «alcuni S non sono P»):",
  "Possono essere entrambe vere ma non entrambe false", ["Non possono essere entrambe vere", "Hanno sempre valori opposti", "Sono sempre entrambe false"],
  "Il contrario delle contrarie, che non possono essere entrambe vere.", W("Quadrato delle opposizioni"), QO, "possono essere entrambi veri ma non possono essere entrambi falsi")
D("log-143", "Fallacie", 3, "«Se legalizziamo X, poi verrà Y e infine la catastrofe», senza motivazioni logiche. Che fallacia è?",
  "Pendio scivoloso", ["Ad hominem", "Petitio principii", "Modus tollens"],
  "Si suppone che un evento debba per forza seguirne un altro.", W("Fallacia"), FAL, "Pendio scivoloso: si commette questo errore quando si prevede il verificarsi di un evento")
D("log-144", "Paradossi", 2, "Qual è il significato etimologico di «paradosso»?",
  "Contro l'opinione comune", ["Doppia verità", "Ragionamento corretto", "Domanda senza risposta"],
  "Dal greco pará (contro) e dóxa (opinione).", W("Paradosso"), PAR, "è, genericamente, la descrizione di un fatto che contraddice l'opinione comune")
D("log-145", "Probabilità", 4, "Nel problema di Monty Hall, cambiando porta dopo che il conduttore ha mostrato una capra, la probabilità di vincere l'auto:",
  "Passa da 1/3 a 2/3", ["Resta 1/3", "Diventa 1/2", "Passa da 1/2 a 1"],
  "È un risultato controintuitivo ma non contraddittorio.", W("Problema di Monty Hall"), MH, "portandole da 1/3 a 2/3")
D("log-146", "Probabilità", 3, "Da quale gioco televisivo prende spunto il problema di Monty Hall?",
  "Let's Make a Deal", ["Rischiatutto", "Jeopardy!", "Wheel of Fortune"], "Monty Hall ne era il conduttore.",
  W("Problema di Monty Hall"), MH, "legato al gioco a premi statunitense Let's Make a Deal")
D("log-147", "Problemi logici", 3, "Qual è il numero minimo di mosse per risolvere la Torre di Hanoi con 3 dischi?",
  "7", ["3", "6", "8"], "Il minimo è 2ⁿ − 1.", W("Torre di Hanoi"), HAN, "per spostare 3 dischi il numero minimo di mosse è 7")
D("log-148", "Problemi logici", 4, "Qual è il numero minimo di mosse per risolvere la Torre di Hanoi con 4 dischi?",
  "15", ["8", "16", "12"], "2⁴ − 1 = 15.", W("Torre di Hanoi"), HAN, "il numero minimo di mosse necessarie per completare il gioco")
D("log-149", "Problemi logici", 3, "Chi inventò nel 1883 il rompicapo della Torre di Hanoi?",
  "Édouard Lucas", ["Leonardo Fibonacci", "Blaise Pascal", "Lewis Carroll"], "È detta anche Torre di Lucas.",
  W("Torre di Hanoi"), HAN, "Il gioco fu inventato nel 1883 dal matematico francese")
D("log-150", "Numeri", 3, "Quale di questi numeri è «perfetto» (uguale alla somma dei propri divisori, escluso sé stesso)?",
  "28", ["12", "18", "24"], "28 = 1 + 2 + 4 + 7 + 14. Gli altri: 12 → 16, 18 → 21, 24 → 36.",
  W("Numero perfetto"), PERF, "un numero perfetto è un numero naturale che è uguale alla somma dei suoi divisori positivi")


# --- Blocco 5: divisibilità, MCD/mcm, percentuali, altri quesiti numerici ---
CD = "Wikipedia_Criteri-di-divisibilità.txt"
MCD = "Wikipedia_Massimo-comun-divisore.txt"
MCM = "Wikipedia_Minimo-comune-multiplo.txt"
PCT = "Wikipedia_Percentuale.txt"
R_MCD = "è il numero naturale più grande per il quale entrambi possono essere divisi esattamente"
R_MCM = "è il più piccolo numero intero positivo multiplo sia di"
R_PCT = "La formula per calcolare la variazione percentuale"

S("log-151", 2, "Quale di questi numeri è divisibile per 3?", "1.236", ["1.234", "2.351", "4.001"],
  "1 + 2 + 3 + 6 = 12, multiplo di 3.", "Criteri di divisibilità", CD, "Un numero è divisibile per 3 se la somma di tutte le sue cifre", "Numeri")
S("log-152", 2, "Quale di questi numeri è divisibile per 9?", "3.861", ["1.234", "5.552", "7.001"],
  "3 + 8 + 6 + 1 = 18, multiplo di 9.", "Criteri di divisibilità", CD, "Un numero è divisibile per 9 se la somma delle sue cifre è divisibile per nove", "Numeri")
S("log-153", 3, "Quale di questi numeri è divisibile per 4?", "1.316", ["1.318", "2.342", "5.106"],
  "Le ultime due cifre (16) formano un multiplo di 4.", "Criteri di divisibilità", CD, "Un numero è divisibile per 4 se le ultime due cifre sono due zeri oppure formano un numero multiplo di 4", "Numeri")
S("log-154", 4, "Quale di questi numeri è divisibile per 11?", "2.728", ["1.234", "5.050", "2.729"],
  "Cifre di posto dispari 8 + 7 = 15, di posto pari 2 + 2 = 4: la differenza 11 è multiplo di 11.", "Criteri di divisibilità", CD, "Un numero è divisibile per 11 se la differenza tra la somma delle sue cifre di posto dispari e la somma delle sue cifre di posto pari", "Numeri")
S("log-155", 1, "Quale di questi numeri NON è divisibile per 5?", "1.252", ["1.250", "3.005", "7.775"],
  "Un numero è divisibile per 5 se termina con 0 o 5.", "Criteri di divisibilità", CD, "Un numero è divisibile per 5 se la sua ultima cifra è 0 oppure 5", "Numeri")
S("log-156", 3, "Quale di questi numeri è divisibile per 25?", "3.175", ["3.170", "2.515", "4.105"],
  "Le ultime due cifre devono essere 00, 25, 50 o 75.", "Criteri di divisibilità", CD, "le sue ultime 2 cifre a destra sono 00, 25, 50 o 75", "Numeri")
S("log-157", 2, "Qual è il massimo comune divisore di 24 e 36?", "12", ["6", "4", "72"],
  "24 = 2³·3, 36 = 2²·3²: fattori comuni con esponente minore, 2²·3 = 12.", "Massimo comun divisore", MCD, R_MCD, "Numeri")
S("log-158", 3, "Qual è il massimo comune divisore di 42 e 56?", "14", ["7", "6", "28"],
  "42/56 si semplifica in 3/4 dividendo per 14.", "Massimo comun divisore", MCD, "Il massimo comun divisore è utile per ridurre una frazione ai minimi termini", "Numeri")
S("log-159", 3, "Due numeri si dicono «primi tra loro» (coprimi) quando:",
  "Il loro massimo comune divisore è 1", ["Sono entrambi numeri primi", "Uno divide l'altro", "Hanno la stessa somma delle cifre"],
  "Per esempio 9 e 28 sono coprimi pur non essendo primi.", "Massimo comun divisore", MCD, "Due numeri si dicono coprimi, o primi tra loro", "Numeri")
S("log-160", 1, "Qual è il minimo comune multiplo di 4 e 6?", "12", ["24", "2", "10"],
  "12 è il più piccolo multiplo comune.", "Minimo comune multiplo", MCM, R_MCM, "Numeri")
S("log-161", 3, "Due autobus partono insieme alle 8:00; uno passa ogni 12 minuti, l'altro ogni 18. Quando ripartiranno di nuovo insieme?",
  "Alle 8:36", ["Alle 8:30", "Alle 8:54", "Alle 9:00"], "mcm(12, 18) = 36 minuti.", "Minimo comune multiplo", MCM, R_MCM, "Numeri")
S("log-162", 2, "Qual è il minimo comune multiplo di 8 e 12?", "24", ["48", "96", "4"],
  "8 = 2³, 12 = 2²·3: 2³·3 = 24.", "Minimo comune multiplo", MCM, R_MCM, "Numeri")
S("log-163", 3, "Il minimo comune denominatore di più frazioni è:",
  "Il minimo comune multiplo dei denominatori", ["Il massimo comune divisore dei denominatori", "Il prodotto dei numeratori", "La somma dei denominatori"],
  "Serve per sommare le frazioni.", "Minimo comune multiplo", MCM, "detto minimo comune denominatore, è proprio il minimo comune multiplo dei denominatori", "Numeri")
S("log-164", 1, "Quanto è il 32% di 2.000?", "640", ["320", "64", "680"],
  "0,32 · 2.000 = 640.", "Percentuale", PCT, "Il 32% di 2000 è calcolato come", "Percentuali")
S("log-165", 2, "Un prezzo passa da 80 € a 100 €. Qual è l'aumento percentuale?", "25%", ["20%", "80%", "125%"],
  "(100 − 80)/80 · 100 = 25%.", "Percentuale", PCT, R_PCT, "Percentuali")
S("log-166", 3, "Il tasso di un mutuo passa dal 2% al 3%. Come si descrive correttamente la variazione?",
  "È aumentato di 1 punto percentuale (cioè del 50%)", ["È aumentato dell'1%", "È aumentato del 3%", "È aumentato del 33%"],
  "La differenza tra due percentuali si esprime in punti percentuali.", "Percentuale", PCT, "il tasso è aumentato di 1 punto percentuale", "Percentuali")
S("log-167", 4, "Un prezzo aumenta del 10% e poi diminuisce del 10%. Rispetto al prezzo iniziale è:",
  "Diminuito dell'1%", ["Invariato", "Aumentato dell'1%", "Diminuito del 10%"],
  "100 → 110 → 99: le percentuali si riferiscono a basi diverse e non si sommano.", "Percentuale", PCT, "Le percentuali non sono quasi mai sommabili perché si riferiscono a basi differenti", "Percentuali")
S("log-168", 3, "Una stazione passa da 3 binari a 2. Di quanto si sono ridotti, in percentuale?",
  "Del 33,3% circa", ["Del 50%", "Del 25%", "Dell'1%"], "1 binario su 3 di partenza.", "Percentuale", PCT, "i binari subiscono una riduzione del 33,3%", "Percentuali")
S("log-169", 2, "Un articolo costa 150 € ed è scontato del 20%. Quanto si paga?", "120 €", ["130 €", "30 €", "125 €"],
  "Il 20% di 150 è 30; 150 − 30 = 120.", "Percentuale", PCT, "in cento parti uguali, e prenderne esattamente", "Percentuali")
S("log-170", 1, "A quale numero decimale corrisponde il 45%?", "0,45", ["4,5", "45", "0,045"],
  "45 parti su 100.", "Percentuale", PCT, "quarantacinque per cento", "Percentuali")
S("log-171", 3, "Dopo uno sconto del 30% un oggetto costa 70 €. Qual era il prezzo iniziale?", "100 €", ["91 €", "97 €", "110 €"],
  "70 € è il 70% del prezzo: 70 / 0,70 = 100.", "Percentuale", PCT, R_PCT, "Percentuali")
S("log-172", 2, "25 candidati su 200 superano la prova. Che percentuale è?", "12,5%", ["25%", "8%", "15%"],
  "25/200 = 0,125.", "Percentuale", PCT, "una percentuale è un numero o un rapporto espresso sotto forma di frazione in centesimi", "Percentuali")
S("log-173", 2, "Con quale numero si rappresenta il totale nel «per mille» (‰)?", "1.000", ["100", "10", "1.000.000"],
  "Il per milione (ppm) usa invece un milione.", "Percentuale", PCT, "che rappresenta il totale con il numero 1000", "Percentuali")
S("log-174", 2, "Completa la serie: 13, 21, 34, 55, ...", "89", ["76", "84", "110"],
  "Successione di Fibonacci: 34 + 55 = 89.", "Successione di Fibonacci", FIB, R_FIB)
S("log-175", 2, "Completa la serie: 2, 3, 5, 7, 11, ...", "13", ["12", "15", "17"],
  "È la successione dei numeri primi.", "Numero primo", PRI, "La successione dei numeri primi comincia con 2, 3, 5, 7, 11, 13")
S("log-176", 3, "Completa la serie: 1, 2, 6, 24, 120, ...", "720", ["240", "600", "144"],
  "Sono i fattoriali: 6! = 720.", "Fattoriale", FAT, R_FAT)
S("log-177", 3, "In una progressione geometrica il primo termine è 3 e la ragione è 2. Quanto vale il quinto termine?", "48", ["24", "96", "30"],
  "aₙ = a₁ · rⁿ⁻¹ = 3 · 2⁴ = 48.", "Progressione geometrica", PG, R_PG)
S("log-178", 3, "Quanti sono i multipli di 7 compresi tra 1 e 100?", "14", ["13", "15", "16"],
  "7, 14, …, 98 è una progressione aritmetica di ragione 7: 98 = 7 + (n − 1)·7 → n = 14.", "Progressione aritmetica", PA, R_PA)
S("log-179", 3, "Quante persone servono, come minimo, per essere certi che almeno due compiano gli anni lo stesso giorno?",
  "367", ["366", "365", "183"], "I giorni possibili sono 366 (compreso il 29 febbraio): con 367 persone, per il principio dei cassetti, almeno due coincidono.",
  "Principio dei cassetti", CAS, "se n+k oggetti sono messi in n cassetti", "Combinatoria")
S("log-180", 3, "Un'urna contiene palline rosse, blu e verdi. Quante bisogna estrarne, al buio, per essere certi di averne due dello stesso colore?",
  "4", ["3", "2", "6"], "Con 3 colori, nel caso peggiore le prime 3 sono diverse; la quarta forma una coppia.",
  "Principio dei cassetti", CAS, "almeno un cassetto deve contenere più di un oggetto", "Combinatoria")
S("log-181", 2, "In un gruppo di 40 persone, 25 bevono tè, 20 caffè e 10 entrambi. Quante non bevono né tè né caffè?",
  "5", ["0", "10", "15"], "Tè o caffè = 25 + 20 − 10 = 35; 40 − 35 = 5.",
  "Diagramma di Venn", VEN, "mostra tutte le possibili relazioni logiche tra una collezione finita di insiemi", "Insiemi")
S("log-182", 4, "Quanti anagrammi distinti ha la parola ANNA?", "6", ["24", "12", "4"],
  "Permutazioni con ripetizione: 4!/(2!·2!) = 6.", "Calcolo combinatorio", CC, R_RIP, "Calcolo combinatorio")
S("log-183", 2, "In quanti modi si possono scegliere 2 oggetti da 4, senza contare l'ordine?", "6", ["8", "12", "16"],
  "4·3/2 = 6.", "Calcolo combinatorio", CC, R_COMB, "Calcolo combinatorio")
S("log-184", 2, "Da 5 uomini e 4 donne si sceglie una coppia formata da un uomo e una donna. Quante coppie sono possibili?", "20", ["9", "36", "10"],
  "5 · 4 = 20.", "Calcolo combinatorio", CC, "il primo elemento della configurazione può essere scelto in", "Calcolo combinatorio")
S("log-185", 3, "Tra 10 candidati si eleggono un presidente e un vicepresidente. Quanti esiti sono possibili?", "90", ["45", "100", "20"],
  "L'ordine conta: 10 · 9 = 90 disposizioni.", "Calcolo combinatorio", CC, R_DISP, "Calcolo combinatorio")
S("log-186", 3, "Quanti numeri di 3 cifre tutte diverse si possono scrivere con le cifre 1, 2, 3, 4?", "24", ["64", "12", "4"],
  "Disposizioni semplici: 4 · 3 · 2 = 24.", "Calcolo combinatorio", CC, R_DISP, "Calcolo combinatorio")
S("log-187", 3, "Nel problema di Monty Hall, qual è la probabilità di vincere se il concorrente NON cambia porta?", "1/3", ["1/2", "2/3", "1"],
  "La probabilità della scelta iniziale resta 1/3; cambiando sale a 2/3.", "Problema di Monty Hall", MH, "portandole da 1/3 a 2/3", "Probabilità")
S("log-188", 2, "Da un mazzo di 40 carte napoletane (12 figure), qual è la probabilità di estrarre una figura?", "3/10", ["1/12", "1/4", "12/52"],
  "12/40 = 3/10.", "Probabilità", PRO, R_PRO, "Probabilità")
S("log-189", 3, "Lanciando 3 monete, qual è la probabilità di ottenere almeno una testa?", "7/8", ["1/8", "3/8", "1/2"],
  "L'unico caso sfavorevole è CCC su 8 sequenze possibili.", "Probabilità", PRO, R_PRO, "Probabilità")
S("log-190", 3, "Lanciando due dadi, qual è la probabilità di ottenere due numeri uguali?", "1/6", ["1/36", "1/12", "1/3"],
  "6 coppie uguali su 36 possibili.", "Probabilità", PRO, R_PRO, "Probabilità")
S("log-191", 3, "Lanciando due dadi, qual è la probabilità che la somma sia 10?", "1/12", ["1/6", "1/36", "1/10"],
  "Coppie (4,6), (5,5), (6,4): 3 su 36.", "Probabilità", PRO, R_PRO, "Probabilità")
S("log-192", 4, "Lanciando tre dadi, Galileo spiegò che le somme 10 e 11 escono più spesso di:",
  "9 e 12", ["3 e 18", "7 e 14", "10 e 11 escono come tutte le altre"],
  "Pur ottenendosi da un uguale numero di combinazioni, hanno meno permutazioni.", "Probabilità", PRO, "la probabilità di uscita delle somme 10 e 11 sia più probabile dell'uscita del 9 e del 12", "Probabilità")
S("log-193", 4, "Chi scrisse nel 1657 il primo trattato sul calcolo delle probabilità, introducendo il valore atteso?",
  "Christiaan Huygens", ["Jakob Bernoulli", "Pierre de Fermat", "Gerolamo Cardano"], "Il «Libellus de ratiociniis in ludo aleae».",
  "Probabilità", PRO, "Nel 1657 Huygens scrisse", "Probabilità")
S("log-194", 4, "Quale opera di Jakob Bernoulli fu pubblicata postuma nel 1713?", "Ars conjectandi", ["Liber abbaci", "Summa de arithmetica", "Analytica priora"],
  "Voce «Probabilità».", "Probabilità", PRO, "Nel 1713 viene pubblicato postumo Ars conjectandi di Jakob Bernoulli", "Probabilità")
S("log-195", 2, "«Tutti gli uomini sono mortali; Socrate è un uomo.» Che tipo di ragionamento porta a «Socrate è mortale»?",
  "Deduttivo", ["Induttivo", "Abduttivo", "Analogico"], "Dall'universale al particolare.", "Deduzione", DED, "Socrate è mortale", "Ragionamento")
S("log-196", 3, "«Il cigno 1 è bianco, il cigno 2 è bianco… quindi tutti i cigni sono bianchi.» Che tipo di ragionamento è?",
  "Induttivo", ["Deduttivo", "Un sillogismo valido", "Una tautologia"], "Dal particolare all'universale: la conclusione non è certa.",
  "Induzione", IND, "il procedimento che dai particolari porta all'universale", "Ragionamento")
S("log-197", 3, "Che valore di verità ha la formula p ∧ ¬p?",
  "È sempre falsa", ["È sempre vera", "Dipende da p", "È soddisfacibile"],
  "Una formula è contraddizione se non è soddisfacibile.", "Logica proposizionale", LP, "contraddizione se non è soddisfacibile", "Tautologie")
S("log-198", 3, "Una formula ben formata si dice «soddisfacibile» se:",
  "Esiste almeno una valutazione che la rende vera", ["È vera in ogni valutazione", "È falsa in ogni valutazione", "Non contiene connettivi"],
  "Se è vera in ogni valutazione è una tautologia.", "Logica proposizionale", LP, "si dice soddisfacibile se esiste una valutazione v tale che v(A)=V", "Tautologie")
S("log-199", 3, "In una gara di nuoto Anna dice «Chiara è arrivata prima di Barbara», Barbara «Chiara è arrivata prima di Anna», Chiara «Sono arrivata seconda». Una sola dice il vero. Cosa si può stabilire?",
  "Solo chi è arrivata terza", ["Solo chi ha vinto", "Solo chi è arrivata seconda", "Nessuna posizione"],
  "Giochi di Archimede 2000; soluzione riportata nel testo.", ME, ES, "Chiara è arrivata prima di Barbara", "Problemi logici")
S("log-200", 4, "Sull'isola di cavalieri, furfanti e paggi: il vecchio dice «Io sono paggio; il ragazzo è cavaliere», il ragazzo «Io sono cavaliere; la ragazza è paggio», la ragazza «Io sono furfante; il vecchio è paggio». Quanti paggi ci sono?",
  "Tre", ["Uno", "Due", "Nessuno"], "La ragazza può essere solo paggio, quindi il vecchio è paggio e il ragazzo non è cavaliere: anche lui è paggio. Giochi di Archimede 1998.",
  ME, ES, "Il vecchio afferma", "Problemi logici")
