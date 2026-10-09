# Matematica — fonte: MatematicaC3, Algebra 1 (CC BY 3.0). Le regole vengono dal libro; i calcoli sono verificati a parte.
A1 = "MatematicaC3_Algebra1.txt"
F = "MatematicaC3, Algebra 1 (CC BY 3.0)"

D("mat-001", "Numeri primi", 1, "Quando un numero maggiore di 1 si dice primo?",
  "Quando è divisibile solo per se stesso e per l'unità", ["Quando è dispari", "Quando non è divisibile per 2", "Quando ha esattamente tre divisori"],
  "Un numero p > 1 è primo se è divisibile solo per se stesso e per 1; altrimenti è composto.",
  F, A1, "Un numero p > 1 si dice primo se è divisibile solo per se stesso e per l'unità")

D("mat-002", "Numeri primi", 3, "Quale di questi numeri è primo?",
  "97", ["91", "51", "87"],
  "97 non è divisibile per 2, 3, 5, 7 (i primi fino alla sua radice). 91 = 7 × 13, 51 = 3 × 17, 87 = 3 × 29.",
  F, A1, "verifico se 59 è divisibile per un numero primo")

D("mat-003", "Numeri primi", 3, "Cosa afferma il teorema fondamentale dell'aritmetica?",
  "Ogni numero naturale maggiore di 1 si scrive in modo unico come prodotto di numeri primi", ["I numeri primi sono infiniti", "Ogni numero pari è somma di due primi", "Il prodotto di due primi è sempre primo"],
  "Ogni n > 1 ammette un'unica scomposizione in fattori primi (a meno dell'ordine).",
  F, A1, "Ogni numero naturale n > 1 si può scrivere in modo unico come prodotto di numeri primi")

D("mat-004", "Divisibilità", 1, "Quando un numero è divisibile per 3?",
  "Quando la somma delle sue cifre è divisibile per 3", ["Quando finisce per 3", "Quando è dispari", "Quando le ultime due cifre formano un multiplo di 3"],
  "Criterio di divisibilità per 3: la somma delle cifre deve essere divisibile per 3.",
  F, A1, "Un numero è divisibile per 3 se e solo se la somma delle cifre che lo compongono è divisibile per 3")

D("mat-005", "Divisibilità", 2, "Il numero 1.234.567 è divisibile per 3?",
  "No, perché la somma delle cifre è 28", ["Sì, perché è dispari", "Sì, perché la somma delle cifre è 27", "No, perché finisce per 7"],
  "1+2+3+4+5+6+7 = 28, che non è divisibile per 3.",
  F, A1, "Un numero è divisibile per 3 se e solo se la somma delle cifre")

D("mat-006", "Divisibilità", 1, "Quando un numero è divisibile per 5?",
  "Quando la sua ultima cifra è 0 o 5", ["Quando la somma delle cifre è 5", "Quando è dispari", "Quando la penultima cifra è 5"],
  "Criterio di divisibilità per 5: l'ultima cifra è 0 o 5.",
  F, A1, "Un numero è divisibile per 5 se la sua ultima cifra è 0 o 5")

D("mat-007", "MCD e mcm", 2, "Qual è il minimo comune multiplo di 12 e 18?",
  "36", ["6", "72", "216"],
  "12 = 2²·3, 18 = 2·3²: il mcm prende i fattori con esponente massimo, 2²·3² = 36. Il MCD è 6.",
  F, A1, "è il più piccolo tra tutti i multipli comuni di a e di b")

D("mat-008", "MCD e mcm", 2, "Qual è il massimo comune divisore di 48 e 36?",
  "12", ["6", "4", "144"],
  "48 = 2⁴·3, 36 = 2²·3²: il MCD prende i fattori comuni con esponente minimo, 2²·3 = 12.",
  F, A1, "è il più grande tra tutti i divisori comuni ad a e b")

D("mat-009", "Potenze", 2, "Quanto vale 2⁵ · 2³?",
  "2⁸ = 256", ["2¹⁵", "4⁸", "2²"],
  "Il prodotto di potenze con la stessa base ha per esponente la somma degli esponenti: 2⁵ · 2³ = 2⁸ = 256.",
  F, A1, "Il prodotto di due potenze con la stessa base è uguale a una potenza che ha per base la stessa base e per esponente la somma degli esponenti")

D("mat-010", "Potenze", 3, "Quanto vale (3²)³?",
  "3⁶ = 729", ["3⁵ = 243", "9³ = 27", "3⁹"],
  "La potenza di una potenza ha per esponente il prodotto degli esponenti: (3²)³ = 3⁶ = 729.",
  F, A1, "La potenza di una potenza è uguale a una potenza che ha la base della prima potenza e per esponente il prodotto degli esponenti")

D("mat-011", "Potenze", 1, "Quanto vale 5⁰?",
  "1", ["0", "5", "Non è definito"],
  "Qualunque numero diverso da zero elevato a zero è uguale a 1.",
  F, A1, "qualunque numero diverso da zero elevato a zero è uguale a 1")

D("mat-012", "Proporzioni", 2, "Quale proprietà vale in ogni proporzione A : B = C : D?",
  "Il prodotto dei medi è uguale al prodotto degli estremi", ["La somma dei medi è uguale alla somma degli estremi", "Gli antecedenti sono uguali", "Il rapporto tra estremi è sempre 1"],
  "Proprietà fondamentale: A · D = B · C.",
  F, A1, "In ogni proporzione il prodotto dei medi è uguale al prodotto degli estremi")

D("mat-013", "Proporzioni", 3, "Trova x nella proporzione 3 : 5 = x : 40.",
  "24", ["15", "20", "66,6"],
  "Prodotto dei medi = prodotto degli estremi: 5x = 3 · 40 = 120, quindi x = 24.",
  F, A1, "il prodotto dei medi è uguale al prodotto degli estremi")

D("mat-014", "Percentuali", 2, "Un articolo costa 80 €. Con uno sconto del 20%, quanto si paga?",
  "64 €", ["60 €", "16 €", "70 €"],
  "Il 20% di 80 è 16; 80 − 16 = 64 €.",
  F, A1, "La percentuale si indica con un numero intero o decimale seguita dal simbolo %")

D("mat-015", "Percentuali", 3, "Un prezzo di 120 € aumenta del 15%. Quanto diventa?",
  "138 €", ["135 €", "132 €", "150 €"],
  "Il 15% di 120 è 18; 120 + 18 = 138 €.",
  F, A1, "La percentuale si indica con un numero intero o decimale seguita dal simbolo %")

D("mat-016", "Percentuali", 1, "Quanto è il 25% di 360?",
  "90", ["72", "36", "120"],
  "25% = 25/100 = 1/4; 360 : 4 = 90.",
  F, A1, "La percentuale si indica con un numero intero o decimale")

D("mat-017", "Statistica", 2, "Qual è la media aritmetica di 4, 7, 10 e 11?",
  "8", ["7,5", "8,5", "10"],
  "Somma dei dati diviso il loro numero: (4 + 7 + 10 + 11) : 4 = 32 : 4 = 8.",
  F, A1, "La media aritmetica (semplice) è il valore ottenuto sommando tutti i dati e dividendo tale somma per il numero dei dati")

D("mat-018", "Statistica", 3, "Qual è la mediana dei dati 3, 8, 5, 10, 2?",
  "5", ["8", "5,6", "3"],
  "Si ordinano i dati: 2, 3, 5, 8, 10. Il valore centrale è 5. La media sarebbe invece 5,6.",
  F, A1, "La mediana di una successione di dati disposti in ordine crescente è il valore equidistante dagli estremi")

D("mat-019", "Equazioni", 2, "Risolvi l'equazione 3x + 7 = 22.",
  "x = 5", ["x = 15", "x = 29/3", "x = 3"],
  "3x = 22 − 7 = 15, quindi x = 15 : 3 = 5.",
  F, A1, "Espressioni numeriche")

D("mat-020", "Problemi", 4, "In un concorso il 40% dei candidati supera lo scritto e, di questi, il 25% supera l'orale. Su 1.000 candidati, quanti superano entrambe le prove?",
  "100", ["250", "400", "65"],
  "Lo scritto lo superano 1.000 · 0,40 = 400 candidati; l'orale 400 · 0,25 = 100.",
  F, A1, "seguita dal simbolo %")


# --- Blocco 2: numeri, frazioni, potenze, proporzioni, insiemi (MatematicaC3, Algebra 1) ---
def M(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, F, A1, frase)

M("mat-021", "Numeri naturali", 2, "Quale di queste divisioni è «indeterminata»?", "0 : 0", ["5 : 0", "0 : 5", "5 : 5"],
  "n : 0 con n ≠ 0 è impossibile; 0 : 0 è indeterminata; 0 : 5 = 0.", "mentre la divisione 0 : 0 è indeterminata")
M("mat-022", "Numeri naturali", 1, "Nella divisione intera 17 : 5, quanto valgono quoziente e resto?", "Quoziente 3, resto 2", ["Quoziente 3, resto 3", "Quoziente 4, resto 3", "Quoziente 2, resto 7"],
  "5 · 3 = 15 ≤ 17; 17 − 15 = 2.", "Si dice resto della divisione tra n e m")
M("mat-023", "Numeri naturali", 2, "Quanto vale 23 mod 7?", "2", ["3", "16", "0"],
  "L'operazione modulo restituisce il resto: 23 = 7 · 3 + 2.", "si chiama modulo di n rispetto a m")
M("mat-024", "Potenze", 1, "Quanto vale 2⁵?", "32", ["10", "25", "64"],
  "Cinque fattori uguali a 2: 2·2·2·2·2 = 32.", "si ottiene moltiplicando fra loro n fattori tutti uguali ad a")
M("mat-025", "Radici", 1, "Qual è la radice cubica di 64?", "4", ["8", "16", "3"],
  "4 · 4 · 4 = 64.", "si definisce radice n-esima di a il numero r tale che moltiplicando tra loro n fattori tutti uguali a r")
M("mat-026", "Divisibilità", 2, "Quali sono i divisori propri di 12?", "2, 3, 4, 6", ["1, 2, 3, 4, 6, 12", "1, 12", "2, 4, 6, 8"],
  "Sono i divisori diversi dal numero stesso e dall'unità.", "Chiamiamo divisore proprio di un numero un suo divisore diverso dal numero stesso e dall'unità")
M("mat-027", "Numeri primi", 2, "Quale teorema afferma che i numeri primi sono infiniti?", "Il teorema di Euclide", ["Il teorema di Pitagora", "Il teorema di Talete", "Il teorema di Ruffini"],
  "Algebra 1, teorema 1.4.", "(di Euclide). I numeri primi sono infiniti")
M("mat-028", "Numeri primi", 3, "Qual è la scomposizione in fattori primi di 630?", "2 · 3² · 5 · 7", ["2 · 3 · 5 · 21", "2² · 3 · 5 · 7", "3² · 7 · 10"],
  "630 = 2 · 315 = 2 · 3 · 105 = 2 · 3 · 3 · 35 = 2 · 3² · 5 · 7.", "Scomporre in fattori primi il numero 630")
M("mat-029", "MCD e mcm", 2, "12 e 25 sono:", "Primi tra loro (coprimi)", ["Entrambi numeri primi", "Uno multiplo dell'altro", "Con MCD uguale a 5"],
  "MCD(12, 25) = 1: non hanno fattori primi comuni.", "12 e 25 sono primi tra loro")
M("mat-030", "MCD e mcm", 1, "Qual è il minimo comune multiplo di 6 e 15?", "30", ["90", "3", "15"],
  "6 = 2·3, 15 = 3·5: mcm = 2·3·5 = 30.", "Per calcolare il minimo comune multiplo tra 6 e 15")
M("mat-031", "MCD e mcm", 1, "Qual è il massimo comune divisore di 18 e 12?", "6", ["3", "2", "36"],
  "Divisori comuni: 1, 2, 3, 6.", "il massimo comune divisore tra 18 e 12")
M("mat-032", "Numeri relativi", 1, "Due numeri relativi si dicono concordi quando:", "Hanno lo stesso segno", ["Hanno lo stesso valore assoluto", "Hanno segni opposti", "La loro somma è zero"],
  "+3 e +5 sono concordi; +3 e −5 sono discordi.", "Due numeri relativi si dicono concordi, se hanno lo stesso segno")
M("mat-033", "Numeri relativi", 1, "Quanto vale |−7|?", "7", ["−7", "0", "1/7"],
  "Il valore assoluto è il numero senza segno.", "Il valore assoluto di un numero relativo è il numero senza il segno")
M("mat-034", "Numeri relativi", 1, "Due numeri relativi sono «opposti» quando:", "Hanno lo stesso valore assoluto ma segni diversi", ["Hanno lo stesso segno", "Il loro prodotto è 1", "Sono entrambi negativi"],
  "Esempio: +3 e −3.", "si dicono opposti se hanno lo stesso valore assoluto ma segni diversi")
M("mat-035", "Numeri relativi", 1, "Quanto vale (−3) + (−5)?", "−8", ["+8", "−2", "+2"],
  "Concordi: si sommano i valori assoluti e si mantiene il segno.", "La somma di due numeri relativi concordi è il numero che ha per valore assoluto la somma dei singoli valori assoluti")
M("mat-036", "Numeri relativi", 2, "Quanto vale (+7) + (−10)?", "−3", ["+3", "−17", "+17"],
  "Discordi: si sottraggono i valori assoluti e si prende il segno del maggiore in valore assoluto.", "La somma di due numeri relativi discordi")
M("mat-037", "Numeri relativi", 1, "Quanto vale (−4) · (−6)?", "+24", ["−24", "−10", "+10"],
  "Regola dei segni: meno per meno dà più.", "regola dei segni")
M("mat-038", "Numeri relativi", 2, "Quanto vale (−2)³?", "−8", ["+8", "−6", "+6"],
  "Tre fattori negativi: il prodotto è negativo.", "regola dei segni")
M("mat-039", "Frazioni", 1, "Una frazione si dice «propria» quando:", "Il numeratore è minore del denominatore", ["Il numeratore è maggiore del denominatore", "Il numeratore è multiplo del denominatore", "È ridotta ai minimi termini"],
  "Rappresenta una grandezza minore dell'intero.", "Si chiamano proprie le frazioni che hanno il numeratore minore del denominatore")
M("mat-040", "Frazioni", 1, "Come si chiama una frazione come 7/4?", "Impropria", ["Propria", "Apparente", "Equivalente"],
  "Il numeratore è maggiore del denominatore ma non ne è multiplo.", "Si chiamano improprie le frazioni che hanno il numeratore maggiore del denominatore")
M("mat-041", "Frazioni", 2, "Come si chiama una frazione come 12/4?", "Apparente", ["Propria", "Impropria non apparente", "Irriducibile"],
  "Il numeratore è multiplo del denominatore: 12/4 = 3.", "Si chiamano apparenti le frazioni che hanno il numeratore multiplo del denominatore")
M("mat-042", "Frazioni", 1, "Quale frazione è equivalente a 2/3?", "8/12", ["6/8", "4/9", "3/2"],
  "Proprietà invariantiva: numeratore e denominatore moltiplicati per 4.", "Se si moltiplica, o si divide, numeratore e denominatore di una stessa frazione per uno stesso numero")
M("mat-043", "Frazioni", 1, "Come si riduce ai minimi termini 18/24?", "3/4", ["9/12", "6/8", "2/3"],
  "Si dividono numeratore e denominatore per MCD(18, 24) = 6.", "Per ridurre ai minimi termini una frazione occorre dividere numeratore e denominatore per il loro")
M("mat-044", "Frazioni", 2, "Quanto vale 1/4 + 1/6?", "5/12", ["2/10", "1/5", "7/12"],
  "Denominatore comune 12: 3/12 + 2/12 = 5/12.", "Se le unità frazionarie sono diverse")
M("mat-045", "Frazioni", 2, "Quanto vale 2/3 · 9/4?", "3/2", ["18/7", "11/7", "8/27"],
  "Numeratori per numeratori e denominatori per denominatori: 18/12 = 3/2.", "Il prodotto di due frazioni è una frazione che ha per numeratore il prodotto dei numeratori")
M("mat-046", "Frazioni", 2, "Quanto vale 2/3 : 4/9?", "3/2", ["8/27", "2/3", "4/3"],
  "Si moltiplica per l'inverso: 2/3 · 9/4 = 3/2.", "Il quoziente di due frazioni è la frazione che si ottiene moltiplicando la prima frazione per l'inverso della seconda")
M("mat-047", "Frazioni", 1, "Qual è il reciproco di 3/5?", "5/3", ["−3/5", "3/5", "−5/3"],
  "Il prodotto di un numero per il suo reciproco è 1.", "si definisce il suo inverso o reciproco")
M("mat-048", "Potenze", 2, "Quanto vale 2⁻³?", "1/8", ["−8", "−6", "8"],
  "Esponente negativo: si prende il reciproco della base con esponente opposto.", "La potenza di un numero razionale diverso da zero elevato a un esponente intero negativo")
M("mat-049", "Notazione scientifica", 2, "Come si scrive 0,00045 in notazione scientifica?", "4,5 · 10⁻⁴", ["45 · 10⁻⁵", "4,5 · 10⁴", "0,45 · 10⁻³"],
  "Il coefficiente deve essere compreso tra 1 (incluso) e 10 (escluso).", "dove k è un numero decimale maggiore o uguale a 1 e minore di 10")
M("mat-050", "Notazione scientifica", 1, "Come si scrive 3.500.000 in notazione scientifica?", "3,5 · 10⁶", ["35 · 10⁵", "3,5 · 10⁵", "0,35 · 10⁷"],
  "Il coefficiente deve essere compreso tra 1 e 10.", "dove k è un numero decimale maggiore o uguale a 1 e minore di 10")
M("mat-051", "Notazione scientifica", 3, "Qual è l'ordine di grandezza di 8.200?", "10⁴", ["10³", "10²", "10⁵"],
  "È la potenza di 10 più vicina: 8.200 è più vicino a 10.000 che a 1.000.", "la potenza di 10 più vicina al numero")
M("mat-052", "Proporzioni", 1, "Nel rapporto A : B, come si chiamano A e B?", "Antecedente e conseguente", ["Estremi e medi", "Dividendo e quoziente", "Numeratore e resto"],
  "Il rapporto è il quoziente del primo numero per il secondo.", "Il primo numero si dice antecedente, il secondo conseguente")
M("mat-053", "Proporzioni", 1, "Nella proporzione A : B = C : D, quali sono gli estremi?", "A e D", ["B e C", "A e B", "C e D"],
  "B e C sono i medi.", "A e D sono detti estremi, mentre B e C si dicono medi")
M("mat-054", "Proporzioni", 3, "Nella proporzione continua 4 : x = x : 9, quanto vale x?", "6", ["6,5", "36", "13"],
  "x² = 4 · 9 = 36, x = 6.", "Una proporzione si dice continua se ha i medi uguali")
M("mat-055", "Proporzioni", 2, "Se in una proporzione si scambiano tra loro i medi:", "Si ottiene ancora una proporzione", ["La proporzione diventa falsa", "Bisogna scambiare anche gli antecedenti", "Si ottiene il reciproco"],
  "È la proprietà del permutare.", "Se in una proporzione scambiamo tra loro i medi otteniamo ancora una proporzione")
M("mat-056", "Proporzionalità", 1, "Due grandezze sono direttamente proporzionali quando:", "Il loro rapporto è costante", ["Il loro prodotto è costante", "La loro somma è costante", "Crescono entrambe di 1"],
  "Il rapporto y/x = k è costante.", "si dicono direttamente proporzionali se il loro rapporto è costante")
M("mat-057", "Proporzionalità", 1, "Due grandezze sono inversamente proporzionali quando:", "Il loro prodotto è costante", ["Il loro rapporto è costante", "La loro differenza è costante", "Una è il doppio dell'altra"],
  "x · y = k.", "si dicono inversamente proporzionali se il loro prodotto è costante")
M("mat-058", "Proporzionalità", 3, "6 operai finiscono un lavoro in 10 giorni. In quanti giorni lo finirebbero 4 operai, lavorando allo stesso ritmo?", "15", ["12", "6,7", "8"],
  "Proporzionalità inversa: 6 · 10 = 4 · x, x = 15.", "si dicono inversamente proporzionali se il loro prodotto è costante")
M("mat-059", "Proporzionalità", 2, "3 kg di mele costano 7,50 €. Quanto costano 5 kg?", "12,50 €", ["10,50 €", "12,00 €", "15,00 €"],
  "Proporzionalità diretta: 2,50 € al kg · 5.", "si dicono direttamente proporzionali se il loro rapporto è costante")
M("mat-060", "Percentuali", 2, "A quale frazione corrisponde il 12,5%?", "1/8", ["1/12", "1/4", "5/4"],
  "12,5/100 = 125/1000 = 1/8.", "Le percentuali sono frazioni che hanno come denominatore 100")
M("mat-061", "Sistemi di numerazione", 3, "Quanto vale in base 10 il numero binario 1011?", "11", ["1011", "13", "9"],
  "1·2³ + 0·2² + 1·2 + 1 = 11.", "Si definisce base di un sistema di numerazione il numero di simboli")
M("mat-062", "Sistemi di numerazione", 2, "Come si chiama la scrittura 352 = 3·10² + 5·10 + 2?", "Notazione polinomiale", ["Notazione scientifica", "Ordine di grandezza", "Scomposizione in fattori"],
  "Somma delle cifre moltiplicate per le potenze della base.", "si chiama notazione polinomiale")
M("mat-063", "Insiemi", 1, "Come si chiama un insieme privo di elementi?", "Insieme vuoto", ["Insieme universo", "Insieme delle parti", "Insieme unitario"],
  "Si indica con ∅ o {}.", "Un insieme privo di elementi si chiama insieme vuoto")
M("mat-064", "Insiemi", 1, "Qual è la cardinalità dell'insieme {a, b, c, d}?", "4", ["1", "5", "16"],
  "È il numero dei suoi elementi.", "Si definisce cardinalità (o potenza) di un insieme finito il numero degli elementi")
M("mat-065", "Insiemi", 3, "Quanti elementi ha l'insieme delle parti di un insieme con 3 elementi?", "8", ["3", "6", "9"],
  "I sottoinsiemi di un insieme di n elementi sono 2ⁿ (compresi ∅ e l'insieme stesso).", "si chiama insieme delle parti")
M("mat-066", "Insiemi", 1, "Due insiemi si dicono disgiunti quando:", "Non hanno elementi in comune", ["Hanno gli stessi elementi", "Uno è contenuto nell'altro", "Hanno la stessa cardinalità"],
  "La loro intersezione è vuota.", "essi si dicono disgiunti se non hanno elementi in comune")
M("mat-067", "Insiemi", 2, "A = {1, 2, 3, 4}, B = {3, 4, 5}. Quanto vale A − B?", "{1, 2}", ["{5}", "{3, 4}", "{1, 2, 5}"],
  "Elementi di A che non appartengono a B.", "si dice insieme differenza tra A e B l'insieme C composto da tutti gli elementi di A che non appartengono a B")
M("mat-068", "Insiemi", 3, "Quale condizione NON è richiesta perché alcuni sottoinsiemi formino una partizione di A?", "Che abbiano tutti lo stesso numero di elementi", ["Che siano non vuoti", "Che siano a due a due disgiunti", "Che la loro unione sia A"],
  "Bastano: non vuoti, disgiunti a due a due, unione uguale ad A.", "si dice che questi costituiscono una partizione di A")
M("mat-069", "Insiemi", 2, "Se A ha 3 elementi e B ne ha 2, quante coppie ordinate ha il prodotto cartesiano A × B?", "6", ["5", "8", "9"],
  "3 · 2 = 6 coppie (a; b).", "Un insieme di due elementi a e b presi in un determinato ordine si dice coppia ordinata")
M("mat-070", "Relazioni", 3, "Quali proprietà deve avere una relazione di equivalenza?", "Riflessiva, simmetrica e transitiva", ["Antisimmetrica e transitiva", "Riflessiva e antisimmetrica", "Solo transitiva"],
  "Antisimmetrica e transitiva caratterizzano invece le relazioni d'ordine.", "Chiamiamo relazione d'equivalenza una relazione che gode delle tre proprietà riflessiva, simmetrica e transitiva")


# --- Blocco 3: calcolo letterale, equazioni, disequazioni, sistemi, funzioni (MatematicaC3, Algebra 1) ---
M("mat-071", "Monomi", 1, "Come si chiama un'espressione letterale in cui numeri e lettere sono legati solo dalla moltiplicazione?", "Monomio", ["Polinomio", "Equazione", "Frazione algebrica"],
  "Esempio: 5a²b.", "Un'espressione letterale in cui numeri e lettere sono legati dalla sola moltiplicazione si chiama monomio")
M("mat-072", "Monomi", 1, "Nel monomio −7x²y, come si chiama −7?", "Coefficiente", ["Parte letterale", "Grado", "Esponente"],
  "x²y è la parte letterale.", "La parte numerica del monomio ridotto a forma normale si chiama coefficiente")
M("mat-073", "Monomi", 1, "Quale monomio è simile a 3a²b?", "−5a²b", ["3ab²", "3a²b²", "3a³b"],
  "Monomi simili hanno parte letterale identica.", "Due o più monomi che hanno parte letterale identica si dicono simili")
M("mat-074", "Monomi", 2, "Qual è il grado complessivo del monomio 4x³y²?", "5", ["3", "6", "4"],
  "Somma degli esponenti: 3 + 2.", "Il grado complessivo di un monomio è la somma degli esponenti della parte letterale")
M("mat-075", "Monomi", 1, "Come si chiamano i monomi 5ab² e −5ab²?", "Opposti", ["Reciproci", "Uguali", "Non simili"],
  "Sono simili con coefficienti opposti: la loro somma è zero.", "Due monomi simili che hanno coefficiente opposto si dicono monomi opposti")
M("mat-076", "Monomi", 2, "Quanto vale (3x²y) · (−2xy³)?", "−6x³y⁴", ["−6x²y³", "x³y⁴", "6x³y⁴"],
  "Si moltiplicano i coefficienti e si sommano gli esponenti delle stesse lettere.", "Il prodotto di due monomi è il monomio avente per coefficiente il prodotto dei coefficienti")
M("mat-077", "Monomi", 3, "Quanto vale (−2a²b)³?", "−8a⁶b³", ["−6a⁶b³", "8a⁶b³", "−8a⁵b³"],
  "(−2)³ = −8; (a²)³ = a⁶; b³.", "La potenza di un monomio è un monomio avente per coefficiente la potenza del coefficiente")
M("mat-078", "Monomi", 1, "Quanto vale 3x² + 5x²?", "8x²", ["8x⁴", "15x²", "8x"],
  "Si sommano i coefficienti dei monomi simili.", "Due o più monomi che hanno parte letterale identica si dicono simili")
M("mat-079", "Polinomi", 1, "Che cos'è un polinomio?", "Una somma algebrica di monomi", ["Un prodotto di monomi", "Un monomio di grado elevato", "Un'equazione con più incognite"],
  "Esempio: 6a + 2b.", "Un polinomio è un'espressione algebrica letterale che consiste in una somma algebrica di monomi")
M("mat-080", "Polinomi", 2, "Qual è il grado del polinomio x³y + 2x²y³ − 5?", "5", ["4", "3", "6"],
  "È il massimo dei gradi dei termini: x³y ha grado 4, 2x²y³ grado 5.", "Il grado complessivo (o semplicemente grado) di un polinomio è il massimo dei gradi complessivi dei suoi termini")
M("mat-081", "Polinomi", 2, "Il polinomio a³ − b³ + ab² è:", "Omogeneo di grado 3", ["Completo", "Di grado 1", "Ordinato e completo"],
  "Tutti i termini hanno grado 3.", "Un polinomio si dice omogeneo se tutti i termini che lo compongono sono dello stesso grado")
M("mat-082", "Polinomi", 2, "Quale di questi polinomi è completo rispetto a x?", "x³ − 2x² + x − 5", ["x³ + x − 1", "x⁴ − 3x² + 2", "x³ + 4"],
  "Contiene tutte le potenze di x di grado inferiore a 3, compreso il termine noto.", "si dice completo se contiene tutte le potenze di tale lettera di grado inferiore a n, compreso il termine noto")
M("mat-083", "Prodotti notevoli", 1, "A cosa è uguale (a + b)²?", "a² + 2ab + b²", ["a² + b²", "a² + ab + b²", "2a + 2b"],
  "Quadrato del primo, più doppio prodotto, più quadrato del secondo.", "Il quadrato di un binomio è uguale alla somma tra il quadrato del primo termine")
M("mat-084", "Prodotti notevoli", 2, "A cosa è uguale (x − 3)²?", "x² − 6x + 9", ["x² − 9", "x² + 9", "x² − 3x + 9"],
  "Il doppio prodotto ha segno negativo.", "Il quadrato di un binomio è uguale alla somma tra il quadrato del primo termine")
M("mat-085", "Prodotti notevoli", 1, "A cosa è uguale (a + b)(a − b)?", "a² − b²", ["a² + b²", "(a − b)²", "a² − 2ab + b²"],
  "Somma per differenza: differenza dei quadrati.", "somma per differenza")
M("mat-086", "Prodotti notevoli", 3, "Quanto vale 51 · 49, usando la somma per differenza?", "2.499", ["2.501", "2.500", "2.449"],
  "(50 + 1)(50 − 1) = 2.500 − 1.", "somma per differenza")
M("mat-087", "Prodotti notevoli", 3, "A cosa è uguale (a + b)³?", "a³ + 3a²b + 3ab² + b³", ["a³ + b³", "a³ + 3ab + b³", "a³ + 2a²b + 2ab² + b³"],
  "Cubo di un binomio.", "Il cubo di un binomio è uguale alla somma tra il cubo del primo monomio")
M("mat-088", "Scomposizione", 2, "Come si scompone x² − 9?", "(x − 3)(x + 3)", ["(x − 3)²", "(x − 9)(x + 1)", "Non si scompone"],
  "È una differenza di due quadrati.", "differenza di due quadrati")
M("mat-089", "Scomposizione", 2, "Come si scompone 6x² + 9x con il raccoglimento a fattore comune?", "3x(2x + 3)", ["3(2x² + 3)", "x(6x + 9x)", "6x(x + 9)"],
  "MCD dei termini: 3x.", "Raccoglimento totale a fattore comune")
M("mat-090", "Polinomi", 3, "Qual è il resto della divisione di x³ − 2x + 1 per (x − 2)?", "5", ["0", "1", "9"],
  "Teorema del resto: A(2) = 8 − 4 + 1 = 5.", "Il resto della divisione di un polinomio A(x) per un binomio del tipo (x − k) è uguale al valore che A(x) assume")
M("mat-091", "Polinomi", 3, "Per quale binomio è divisibile x² − 5x + 6?", "x − 2", ["x + 2", "x − 1", "x + 3"],
  "Teorema di Ruffini: A(2) = 4 − 10 + 6 = 0.", "Condizione necessaria e sufficiente affinché un polinomio A(x) sia divisibile per un binomio del tipo (x − k) è che risulti A(k) = 0")
M("mat-092", "Scomposizione", 2, "Quando un polinomio si dice riducibile?", "Quando si può scrivere come prodotto di polinomi di grado maggiore di zero", ["Quando ha grado 1", "Quando ha coefficienti interi", "Quando è omogeneo"],
  "Altrimenti è irriducibile.", "Un polinomio si dice riducibile (scomponibile) se può essere scritto come prodotto di due o più polinomi")
M("mat-093", "Equazioni", 1, "Come si chiamano le formule aperte costruite con il predicato «essere uguale»?", "Equazioni", ["Uguaglianze", "Disequazioni", "Identità numeriche"],
  "Le formule chiuse con «essere uguale» sono uguaglianze.", "Le formule aperte costruite con il predicato essere uguale si chiamano equazioni")
M("mat-094", "Equazioni", 2, "Quando due equazioni sono equivalenti?", "Quando hanno lo stesso insieme soluzione", ["Quando hanno lo stesso grado", "Quando hanno gli stessi coefficienti", "Quando hanno la stessa incognita"],
  "Algebra 1, definizione 15.3.", "Due equazioni sono equivalenti se hanno lo stesso insieme soluzione")
M("mat-095", "Equazioni", 2, "Cosa afferma il primo principio di equivalenza delle equazioni?", "Aggiungendo o sottraendo ad ambo i membri lo stesso numero si ottiene un'equazione equivalente", ["Si possono moltiplicare i membri per zero", "Si può elevare al quadrato", "Si possono scambiare incognita e termine noto"],
  "Consente di «trasportare» termini cambiandone il segno.", "Aggiungendo o sottraendo ad ambo i membri di un'equazione data uno stesso numero")
M("mat-096", "Equazioni", 2, "Cosa afferma il secondo principio di equivalenza delle equazioni?", "Moltiplicando o dividendo ambo i membri per uno stesso numero non nullo si ottiene un'equazione equivalente", ["Si può dividere per zero", "Si possono sommare due equazioni", "Si può cambiare il segno di un solo membro"],
  "Il numero deve essere diverso da zero.", "Moltiplicando o dividendo ambo i membri di un'equazione per uno stesso numero non nullo")
M("mat-097", "Equazioni", 1, "Risolvi: 3x − 7 = 2x + 5.", "x = 12", ["x = −2", "x = 2", "x = −12"],
  "3x − 2x = 5 + 7.", "Aggiungendo o sottraendo ad ambo i membri di un'equazione data uno stesso numero")
M("mat-098", "Equazioni", 2, "Risolvi: 5(x − 2) = 3x + 4.", "x = 7", ["x = 3", "x = −7", "x = 1"],
  "5x − 10 = 3x + 4 → 2x = 14.", "Aggiungendo o sottraendo ad ambo i membri di un'equazione data uno stesso numero")
M("mat-099", "Equazioni", 2, "Risolvi: x/3 + x/6 = 5.", "x = 10", ["x = 5", "x = 15", "x = 30"],
  "Moltiplicando per 6: 2x + x = 30.", "Moltiplicando o dividendo ambo i membri di un'equazione per uno stesso numero non nullo")
M("mat-100", "Equazioni", 3, "L'equazione 2x + 3 = 2x + 5 è:", "Impossibile", ["Determinata con x = 1", "Indeterminata", "Di secondo grado"],
  "Si riduce a 0 · x = 2: nessun valore la soddisfa.", "Risolvere un'equazione significa determinare il suo Insieme Soluzione")
M("mat-101", "Equazioni", 3, "L'equazione 2(x + 1) = 2x + 2 è:", "Indeterminata (ogni numero è soluzione)", ["Impossibile", "Determinata con x = 0", "Determinata con x = 1"],
  "Si riduce a 0 · x = 0.", "Risolvere un'equazione significa determinare il suo Insieme Soluzione")
M("mat-102", "Equazioni", 2, "Come si chiama un'equazione in cui l'incognita compare al denominatore?", "Frazionaria (o fratta)", ["Irrazionale", "Letterale", "Lineare"],
  "Bisogna porre le condizioni di esistenza.", "Un'equazione in cui l'incognita compare al denominatore si chiama frazionaria o fratta")
M("mat-103", "Equazioni", 2, "Dalla formula dell'area del triangolo A = b · h / 2, come si ricava h?", "h = 2A / b", ["h = A / 2b", "h = A · b / 2", "h = 2b / A"],
  "Si moltiplica per 2 e si divide per b.", "Per il primo principio di equivalenza moltiplichiamo per 2 entrambi i membri")
M("mat-104", "Disequazioni", 2, "L'intervallo aperto (2, 5) contiene gli estremi 2 e 5?", "No, gli estremi sono esclusi", ["Sì, entrambi", "Solo 2", "Solo 5"],
  "L'intervallo chiuso [2, 5] li include.", "intervallo limitato aperto (a e b sono esclusi)")
M("mat-105", "Disequazioni", 2, "Cosa succede al verso di una disequazione se si moltiplicano entrambi i membri per un numero negativo?", "Il verso si inverte", ["Resta uguale", "Diventa un'uguaglianza", "La disequazione diventa impossibile"],
  "Esempio: −x > 2 diventa x < −2.", "cambiare il verso della disequazione")
M("mat-106", "Disequazioni", 2, "Risolvi: −2x > 6.", "x < −3", ["x > −3", "x < 3", "x > 3"],
  "Dividendo per −2 il verso si inverte.", "cambiare il verso della disequazione")
M("mat-107", "Disequazioni", 1, "Risolvi: 3x − 4 ≤ 11.", "x ≤ 5", ["x ≥ 5", "x ≤ 7/3", "x < 5"],
  "Si ottiene 3x ≤ 15, quindi x ≤ 5.", "Due disequazioni si dicono equivalenti se hanno lo stesso insieme delle soluzioni")
M("mat-108", "Sistemi", 1, "Che cos'è un sistema di equazioni?", "Un insieme di equazioni che devono essere verificate contemporaneamente", ["Un'equazione con più soluzioni", "Una disequazione doppia", "Un'equazione di grado superiore"],
  "Si scrive raggruppando le equazioni con una parentesi graffa.", "Si definisce sistema di equazioni l'insieme di più equazioni, in due o più incognite, che devono essere verificate contemporaneamente")
M("mat-109", "Sistemi", 2, "Risolvi il sistema: x + y = 10; x − y = 4.", "x = 7, y = 3", ["x = 3, y = 7", "x = 6, y = 4", "x = 14, y = −4"],
  "Sommando: 2x = 14.", "Si definisce sistema di equazioni l'insieme di più equazioni")
M("mat-110", "Sistemi", 2, "Risolvi il sistema: 2x + y = 7; x − y = 2.", "x = 3, y = 1", ["x = 1, y = 3", "x = 2, y = 3", "x = 4, y = 2"],
  "Sommando: 3x = 9.", "Si definisce sistema di equazioni l'insieme di più equazioni")
M("mat-111", "Problemi", 2, "Due numeri hanno somma 16 e differenza 6. Quali sono?", "11 e 5", ["10 e 6", "12 e 4", "8 e 8"],
  "x + y = 16, x − y = 6 → x = 11, y = 5.", "Determinare due numeri naturali la cui somma sia 16")
M("mat-112", "Geometria", 3, "Cosa afferma il teorema di Talete?", "Un fascio di rette parallele tagliato da due trasversali determina segmenti proporzionali", ["In un triangolo rettangolo il quadrato dell'ipotenusa è la somma dei quadrati dei cateti", "La somma degli angoli interni di un triangolo è 180°", "Ogni angolo alla circonferenza è metà del corrispondente angolo al centro"],
  "AB : A'B' = BC : B'C'.", "Un fascio di rette parallele tagliato da due trasversali r e r 0 determina su esse segmenti che mantengono tra loro le proporzioni")
M("mat-113", "Funzioni", 1, "Che cosa caratterizza una funzione da A a B?", "Ogni elemento di A ha uno e un solo corrispondente in B", ["Ogni elemento di B ha un corrispondente in A", "A e B hanno lo stesso numero di elementi", "Ogni elemento di A ha almeno due immagini"],
  "A è il dominio, B il codominio.", "In altre parole ogni elemento del dominio A è in corrispondenza con un solo elemento del codominio B")
M("mat-114", "Funzioni", 2, "Quando una funzione si dice iniettiva?", "Quando elementi distinti del dominio hanno immagini distinte", ["Quando ogni elemento del codominio è immagine", "Quando è costante", "Quando il dominio è vuoto"],
  "Se è anche suriettiva è biunivoca.", "Si dice iniettiva una funzione per la quale elementi distinti del dominio D hanno immagini distinte")
M("mat-115", "Funzioni", 2, "Quando una funzione si dice biunivoca (biiettiva)?", "Quando è contemporaneamente iniettiva e suriettiva", ["Quando è solo iniettiva", "Quando è costante", "Quando ha due variabili"],
  "Algebra 1, definizione 8.5.", "Si dice biunivoca o biiettiva una funzione che sia contemporaneamente iniettiva e suriettiva")
M("mat-116", "Funzioni", 1, "Qual è il grafico della funzione y = mx + q?", "Una retta", ["Una parabola", "Un'iperbole", "Una circonferenza"],
  "È detta funzione lineare.", "il cui grafico è una retta, è detta funzione lineare")
M("mat-117", "Funzioni", 1, "Data y = 2x + 3, quanto vale y per x = 4?", "11", ["9", "14", "24"],
  "2 · 4 + 3 = 11.", "il cui grafico è una retta, è detta funzione lineare")
M("mat-118", "Piano cartesiano", 2, "In quale quadrante si trova il punto (−2; 3)?", "Nel secondo", ["Nel primo", "Nel terzo", "Nel quarto"],
  "Ascissa negativa e ordinata positiva.", "Gli assi dividono il piano in quattro zone chiamate quadranti")
M("mat-119", "Piano cartesiano", 2, "Qual è il punto medio del segmento di estremi A(2; 4) e B(6; 8)?", "(4; 6)", ["(8; 12)", "(2; 2)", "(3; 5)"],
  "Media delle ascisse e media delle ordinate.", "Il punto medio di un segmento AB è il punto M interno al segmento che lo divide in due parti congruenti")
M("mat-120", "Funzioni", 2, "Che tipo di proporzionalità esprime la funzione y = 12/x?", "Proporzionalità inversa", ["Proporzionalità diretta", "Proporzionalità quadratica", "Funzione costante"],
  "x · y = 12 costante.", "si chiama funzione di proporzionalità inversa")


# --- Blocco 4: radicali, equazioni di secondo grado, probabilità (MatematicaC3, Algebra 2) ---
A2 = "MatematicaC3_Algebra2.txt"
F2 = "MatematicaC3, Algebra 2 (CC BY 3.0)"
def N(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, F2, A2, frase)

N("mat-121", "Radicali", 1, "Quanto vale √49?", "7", ["−7", "±7", "24,5"],
  "La radice quadrata aritmetica è il numero non negativo che elevato al quadrato dà 49.", "Si dice radice quadrata di un numero reale a positivo o nullo")
N("mat-122", "Radicali", 2, "√(−4) è un numero reale?", "No: nei reali non esiste la radice quadrata di un numero negativo", ["Sì, vale −2", "Sì, vale 2", "Sì, vale ±2"],
  "La radice quadrata è definita per a ≥ 0.", "Si dice radice quadrata di un numero reale a positivo o nullo")
N("mat-123", "Radicali", 2, "Quanto vale la radice cubica di −27?", "−3", ["3", "Non esiste", "−9"],
  "(−3)³ = −27: la radice cubica è definita anche per i negativi.", "Si dice radice cubica di un numero reale a quel numero che, elevato al cubo")
N("mat-124", "Radicali", 3, "Quanto vale 8^(2/3)?", "4", ["16/3", "2", "64"],
  "8^(2/3) = (∛8)² = 2² = 4.", "Si dice potenza a esponente razionale di un numero reale positivo")
N("mat-125", "Radicali", 1, "Quando due radicali si dicono simili?", "Quando hanno lo stesso indice e lo stesso radicando", ["Quando hanno lo stesso coefficiente", "Quando hanno lo stesso indice", "Quando hanno radicandi opposti"],
  "Solo i radicali simili si possono sommare.", "Due radicali si dicono simili se hanno lo stesso indice e lo stesso radicando")
N("mat-126", "Radicali", 1, "Quanto vale 2√3 + 5√3?", "7√3", ["7√6", "10√3", "√21"],
  "Radicali simili: si sommano i coefficienti.", "È possibile effettuare somme algebriche soltanto se i radicali sono simili")
N("mat-127", "Radicali", 2, "Quanto vale √12 portando fuori dal segno di radice?", "2√3", ["3√2", "4√3", "6√2"],
  "√12 = √(4 · 3) = 2√3; 2 diventa il coefficiente del radicale.", "Il numero a prende il nome di coefficiente del radicale")
N("mat-128", "Radicali", 2, "Quanto vale √2 · √8?", "4", ["√10", "16", "2√2"],
  "√(2 · 8) = √16 = 4.", "Si dice radice quadrata di un numero reale a positivo o nullo")
N("mat-129", "Radicali", 3, "Razionalizzando il denominatore, a cosa è uguale 6/√3?", "2√3", ["6√3", "√3/6", "3√2"],
  "6/√3 · √3/√3 = 6√3/3 = 2√3.", "Per razionalizzare il denominatore")
N("mat-130", "Numeri reali", 2, "Quale di questi numeri è irrazionale?", "√2", ["0,5", "3/7", "√9"],
  "√9 = 3; 0,5 e 3/7 sono razionali.", "Chiamiamo numero razionale le partizioni che ammettono elemento separatore e numero irrazionale")
N("mat-131", "Equazioni di secondo grado", 1, "Qual è la forma generale di un'equazione di secondo grado?", "ax² + bx + c = 0 con a ≠ 0", ["ax + b = 0", "ax² + bx + c = 0 con b ≠ 0", "ax³ + bx = 0"],
  "Se a = 0 l'equazione è di primo grado.", "Si dice equazione di secondo grado, un'equazione del tipo")
N("mat-132", "Equazioni di secondo grado", 1, "Come si chiama l'espressione b² − 4ac?", "Discriminante", ["Determinante", "Vertice", "Coefficiente direttivo"],
  "Si indica con Δ.", "prende il nome di discriminante")
N("mat-133", "Equazioni di secondo grado", 2, "Se Δ > 0, l'equazione di secondo grado ha:", "Due soluzioni reali e distinte", ["Due soluzioni coincidenti", "Nessuna soluzione reale", "Infinite soluzioni"],
  "Se Δ = 0 coincidenti, se Δ < 0 nessuna reale.", "l'equazione ammette due soluzioni reali e distinte")
N("mat-134", "Equazioni di secondo grado", 2, "Se Δ = 0, l'equazione di secondo grado ha:", "Due soluzioni reali coincidenti", ["Due soluzioni distinte", "Nessuna soluzione reale", "Una sola soluzione uguale a zero"],
  "x₁ = x₂ = −b/2a.", "radici reali e coincidenti")
N("mat-135", "Equazioni di secondo grado", 2, "L'equazione x² + x + 3 = 0:", "Non ha soluzioni reali", ["Ha due soluzioni distinte", "Ha due soluzioni coincidenti", "Ha soluzione x = −3"],
  "Δ = 1 − 12 = −11 < 0.", "l'equazione non ammette soluzioni reali")
N("mat-136", "Equazioni di secondo grado", 2, "Quali sono le soluzioni di x² − 5x + 6 = 0?", "2 e 3", ["−2 e −3", "1 e 6", "−1 e 6"],
  "Δ = 25 − 24 = 1; x = (5 ± 1)/2.", "prende il nome di discriminante")
N("mat-137", "Equazioni di secondo grado", 3, "Quali sono le soluzioni di 4x² − 12x + 9 = 0?", "x₁ = x₂ = 3/2", ["3 e −3", "Nessuna soluzione reale", "9/4 e 1"],
  "Δ = 144 − 144 = 0; x = 12/8 = 3/2.", "radici reali e coincidenti")
N("mat-138", "Equazioni di secondo grado", 3, "Qual è la somma delle soluzioni di 2x² − 8x + 3 = 0?", "4", ["−4", "3/2", "8"],
  "x₁ + x₂ = −b/a = 8/2.", "la somma delle radici è x1 + x2 = −")
N("mat-139", "Equazioni di secondo grado", 3, "Qual è il prodotto delle soluzioni di 2x² − 8x + 3 = 0?", "3/2", ["3", "−4", "−3/2"],
  "x₁ · x₂ = c/a.", "il prodotto delle radici è x1 · x2 =")
N("mat-140", "Equazioni di secondo grado", 2, "Quali sono le soluzioni dell'equazione pura x² − 16 = 0?", "±4", ["4", "16", "Nessuna"],
  "Da x² = 16 si ricava x = ±4.", "Risoluzione di un'equazione di secondo grado incompleta pura")
N("mat-141", "Equazioni di secondo grado", 2, "Quali sono le soluzioni dell'equazione spuria x² − 5x = 0?", "0 e 5", ["5", "±5", "0 e −5"],
  "x(x − 5) = 0.", "Risoluzione di un'equazione incompleta spuria")
N("mat-142", "Equazioni di secondo grado", 4, "Per la regola di Cartesio, quante soluzioni positive ha x² − 5x + 6 = 0 (Δ > 0)?", "Due", ["Una", "Nessuna", "Tre"],
  "Segni dei coefficienti + − +: due variazioni, due radici positive (2 e 3).", "il numero di radici positive è uguale al numero di variazioni")
N("mat-143", "Funzioni", 2, "Qual è il grafico della funzione y = x² − 4?", "Una parabola", ["Una retta", "Un'iperbole", "Una circonferenza"],
  "È una funzione polinomiale di secondo grado.", "si chiama funzione polinomiale di secondo grado")
N("mat-144", "Equazioni", 2, "Qual è la soluzione reale dell'equazione binomia x³ − 8 = 0?", "2", ["±2", "8/3", "4"],
  "Da x³ = 8 si ricava x = 2.", "Un'equazione binomia è un'equazione del tipo")
N("mat-145", "Equazioni", 4, "Quante soluzioni reali ha l'equazione x⁴ − 5x² + 4 = 0?", "Quattro: ±1 e ±2", ["Due: 1 e 4", "Due: ±2", "Nessuna"],
  "Ponendo t = x²: t² − 5t + 4 = 0 → t = 1 o t = 4.", "Sono esempi di equazioni trinomie x4 − 5x2 + 4 = 0")
N("mat-146", "Equazioni", 2, "Quando un'equazione si dice irrazionale?", "Quando l'incognita compare sotto il segno di radice", ["Quando ha soluzioni irrazionali", "Quando l'incognita è al denominatore", "Quando è di grado superiore al secondo"],
  "Algebra 2, definizione 8.1.", "Un'equazione si dice irrazionale quando l'incognita compare sotto il segno di radice")
N("mat-147", "Sistemi", 3, "Qual è il grado di un sistema formato da un'equazione di secondo grado e una di primo grado?", "2", ["3", "1", "4"],
  "È il prodotto dei gradi: 2 · 1.", "è dato dal prodotto dei gradi delle equazioni che lo compongono")
N("mat-148", "Sistemi", 3, "Quando un sistema in due incognite si dice simmetrico?", "Quando resta lo stesso scambiando tra loro le incognite", ["Quando ha soluzioni opposte", "Quando ha due equazioni uguali", "Quando è omogeneo"],
  "Esempio: x + y = s, xy = p.", "si dice simmetrico se rimane lo stesso scambiando tra loro le incognite")
N("mat-149", "Probabilità", 1, "Come si chiama il risultato di un fenomeno aleatorio?", "Evento", ["Spazio campionario", "Frequenza", "Variabile"],
  "Algebra 2, definizione 9.1.", "Si chiama evento il risultato di un fenomeno aleatorio")
N("mat-150", "Probabilità", 2, "Come si chiama l'insieme di tutti gli esiti possibili di un fenomeno aleatorio?", "Spazio degli eventi (Ω)", ["Evento certo", "Evento elementare", "Insieme delle parti"],
  "Ogni suo elemento è un evento elementare.", "Si chiama spazio degli eventi, l'insieme di tutti gli esiti possibili del fenomeno considerato")
N("mat-151", "Probabilità", 2, "Cos'è un evento elementare?", "Ogni singolo elemento dello spazio degli eventi Ω", ["Un evento impossibile", "Un evento con probabilità 1/2", "L'unione di due eventi"],
  "Un evento composto è invece un sottoinsieme qualsiasi di Ω.", "Si chiama evento elementare ogni elemento dell'insieme Ω")
N("mat-152", "Probabilità", 1, "Due eventi si dicono incompatibili quando:", "Non si possono verificare contemporaneamente", ["Hanno la stessa probabilità", "Uno implica l'altro", "Sono indipendenti"],
  "A ∩ B = ∅.", "Due eventi A e B si dicono incompatibili quando non si possono verificare contemporaneamente")
N("mat-153", "Probabilità", 4, "Da un mazzo di 40 carte (10 di denari, 12 figure, 3 figure di denari) si estrae una carta. Qual è la probabilità che sia di denari o una figura?", "19/40", ["22/40", "1/4", "3/40"],
  "Teorema delle probabilità totali per eventi compatibili: 10/40 + 12/40 − 3/40.", "(delle probabilità totali)")
N("mat-154", "Probabilità", 2, "Se la probabilità di un evento A è 0,3, qual è la probabilità dell'evento complementare?", "0,7", ["0,3", "1,3", "0"],
  "P(non A) = 1 − P(A).", "si definisce evento complementare di A")
N("mat-155", "Probabilità", 2, "Quando due eventi si dicono indipendenti?", "Quando il verificarsi dell'uno non cambia la probabilità dell'altro", ["Quando non possono verificarsi insieme", "Quando hanno probabilità 1/2", "Quando si escludono"],
  "Altrimenti sono dipendenti.", "Due eventi A e B si dicono indipendenti se il verificarsi di A non cambia la probabilità")
N("mat-156", "Probabilità", 3, "Un'urna ha 3 palline rosse e 2 bianche. Si estraggono due palline con reimmissione: qual è la probabilità che siano entrambe rosse?", "9/25", ["3/10", "6/25", "3/5"],
  "Eventi indipendenti: 3/5 · 3/5.", "(delle probabilità composte)")
N("mat-157", "Probabilità", 4, "Stessa urna (3 rosse, 2 bianche), ma senza reimmissione: probabilità di due rosse?", "3/10", ["9/25", "6/25", "1/2"],
  "Probabilità condizionata: 3/5 · 2/4 = 6/20.", "Si chiama probabilità condizionata o subordinata")
N("mat-158", "Probabilità", 1, "Come si chiama un evento che non può verificarsi in alcun caso?", "Evento impossibile", ["Evento certo", "Evento aleatorio", "Evento complementare"],
  "Si indica con ∅; ha probabilità 0.", "Chiamiamo evento impossibile")
N("mat-159", "Numeri reali", 3, "Secondo il teorema di Dedekind, ogni sezione dell'insieme dei numeri reali ammette:", "Uno e un solo elemento separatore", ["Nessun elemento separatore", "Due elementi separatori", "Infiniti elementi separatori"],
  "Per questo R è un insieme continuo.", "Ogni sezione (A; B) dell'insieme R ammette uno e un solo elemento separatore")
N("mat-160", "Radicali", 2, "Quanto vale √(3²)?", "3", ["9", "√3", "6"],
  "La radice quadrata di un quadrato di un numero positivo è il numero stesso.", "Si dice radice quadrata di un numero reale a positivo o nullo")


# --- Blocco 5: geometria, misure, capitalizzazione (voci di Wikipedia, CC BY-SA 4.0) ---
def G(id, arg, liv, testo, giusta, sbagliate, spieg, voce, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, f"Wikipedia, «{voce}» (CC BY-SA 4.0)",
      "Wikipedia_" + voce.replace(" ", "-").replace("'", "-") + ".txt", frase)

PIT = "In ogni triangolo rettangolo l'area del quadrato costruito sull'ipotenusa è uguale alla somma delle aree dei quadrati costruiti sui cateti"
G("mat-161", "Geometria", 1, "Cosa afferma il teorema di Pitagora?", "In un triangolo rettangolo il quadrato dell'ipotenusa è uguale alla somma dei quadrati dei cateti",
  ["In ogni triangolo la somma degli angoli è 180°", "In un triangolo rettangolo i cateti sono uguali", "L'ipotenusa è la somma dei cateti"],
  "c² = a² + b².", "Teorema di Pitagora", PIT)
G("mat-162", "Geometria", 1, "I cateti di un triangolo rettangolo misurano 3 cm e 4 cm. Quanto misura l'ipotenusa?", "5 cm", ["7 cm", "6 cm", "12 cm"],
  "√(9 + 16) = √25.", "Teorema di Pitagora", PIT)
G("mat-163", "Geometria", 2, "I cateti di un triangolo rettangolo misurano 6 m e 8 m. Quanto misura l'ipotenusa?", "10 m", ["14 m", "12 m", "48 m"],
  "√(36 + 64) = √100.", "Teorema di Pitagora", PIT)
G("mat-164", "Geometria", 2, "In un triangolo rettangolo l'ipotenusa misura 13 e un cateto 5. Quanto misura l'altro cateto?", "12", ["8", "18", "√194"],
  "√(169 − 25) = √144.", "Teorema di Pitagora", "Una terna di numeri interi positivi")
G("mat-165", "Geometria", 2, "Quale di queste è una terna pitagorica?", "5, 12, 13", ["4, 5, 6", "2, 3, 4", "6, 7, 8"],
  "25 + 144 = 169.", "Teorema di Pitagora", "Una terna di numeri interi positivi")
G("mat-166", "Geometria", 3, "Quale popolo conosceva già l'enunciato del teorema di Pitagora prima di Pitagora?", "I Babilonesi", ["I Romani", "Gli Etruschi", "I Celti"],
  "L'enunciato, non la dimostrazione.", "Teorema di Pitagora", "era già noto ai Babilonesi")
G("mat-167", "Geometria", 1, "Quanto vale la somma degli angoli interni di un triangolo (geometria euclidea)?", "180°", ["360°", "90°", "270°"],
  "È un angolo piatto.", "Triangolo", "la somma degli angoli interni è uguale a un angolo piatto, ossia 180°")
G("mat-168", "Geometria", 1, "Un triangolo ha due angoli di 50° e 60°. Quanto misura il terzo?", "70°", ["80°", "90°", "250°"],
  "180° − 110°.", "Triangolo", "la somma degli angoli interni è uguale a un angolo piatto, ossia 180°")
G("mat-169", "Geometria", 1, "Quanto misura ciascun angolo interno di un triangolo equilatero?", "60°", ["90°", "45°", "120°"],
  "Gli angoli sono uguali: 180°/3.", "Triangolo", "triangolo avente i suoi angoli interni di uguale ampiezza, pari a 60°")
G("mat-170", "Geometria", 1, "Come si chiama un triangolo con due lati uguali?", "Isoscele", ["Scaleno", "Equilatero", "Ottusangolo"],
  "Ha anche due angoli uguali.", "Triangolo", "In un triangolo isoscele due lati hanno lunghezza uguale")
G("mat-171", "Geometria", 1, "Come si chiama un triangolo con tutti i lati di lunghezza diversa?", "Scaleno", ["Isoscele", "Equilatero", "Rettangolo"],
  "Ha anche i tre angoli diversi.", "Triangolo", "In un triangolo scaleno tutti i lati hanno lunghezze differenti")
G("mat-172", "Geometria", 2, "Un triangolo con un angolo di 120° si dice:", "Ottusangolo", ["Acutangolo", "Rettangolo", "Equilatero"],
  "Ha un angolo maggiore di 90°.", "Triangolo", "ha un angolo interno maggiore di 90°")
G("mat-173", "Geometria", 3, "Quale poligono non può mai essere concavo?", "Il triangolo", ["Il quadrilatero", "Il pentagono", "L'esagono"],
  "Voce «Triangolo».", "Triangolo", "è l'unico poligono che non può essere concavo")
G("mat-174", "Geometria", 1, "Quanto vale la somma degli angoli interni di un quadrilatero?", "360°", ["180°", "540°", "720°"],
  "Un angolo giro.", "Quadrilatero", "La somma delle ampiezze degli angoli interni di un quadrilatero semplice ABCD è uguale a 360°")
G("mat-175", "Geometria", 2, "Quanto vale la somma degli angoli interni di un esagono?", "720°", ["540°", "1.080°", "360°"],
  "180° · (6 − 2).", "Poligono", "La somma degli angoli interni di un poligono è pari a tanti angoli piatti quanti sono i suoi lati")
G("mat-176", "Geometria", 2, "Quando un poligono si dice regolare?", "Quando è convesso, equilatero ed equiangolo", ["Quando ha lati paralleli", "Quando ha almeno un angolo retto", "Quando è inscritto in un quadrato"],
  "Voce «Poligono».", "Poligono", "regolare se è convesso, equilatero ed equiangolo")
G("mat-177", "Geometria", 1, "Qual è l'area di un rettangolo di base 7 m e altezza 4 m?", "28 m²", ["22 m²", "11 m²", "14 m²"],
  "Base per altezza.", "Rettangolo", "L'area del rettangolo è il prodotto della sua lunghezza per la sua larghezza")
G("mat-178", "Geometria", 2, "Il quadrato è un caso particolare di:", "Rettangolo (e di rombo)", ["Trapezio scaleno", "Triangolo", "Pentagono"],
  "Ha tutti i lati congruenti e tutti gli angoli retti.", "Rettangolo", "Il quadrato è un tipo particolare di rettangolo")
G("mat-179", "Geometria", 2, "Qual è l'area di un trapezio con basi 10 cm e 6 cm e altezza 4 cm?", "32 cm²", ["64 cm²", "40 cm²", "24 cm²"],
  "(10 + 6) · 4 / 2.", "Trapezio", "del trapezio è la somma delle basi per l'altezza diviso due")
G("mat-180", "Geometria", 1, "Che cos'è un trapezio?", "Un quadrilatero con due lati paralleli", ["Un quadrilatero con tutti i lati uguali", "Un triangolo con un angolo retto", "Un quadrilatero senza lati paralleli"],
  "I lati paralleli sono le basi.", "Trapezio", "un trapezio è un quadrilatero con due lati paralleli")
G("mat-181", "Geometria", 2, "Quanto è lunga una circonferenza di raggio 5 cm?", "10π cm", ["25π cm", "5π cm", "100π cm"],
  "L = 2πr = 2π · 5 = 10π.", "Circonferenza", "La formula per trovare la lunghezza della circonferenza è")
G("mat-182", "Geometria", 2, "Qual è l'area di un cerchio di raggio 3 m?", "9π m²", ["6π m²", "3π m²", "18π m²"],
  "A = πr² = π · 3² = 9π.", "Cerchio", "La formula dell'area del cerchio può essere ottenuta come limite di quella del poligono regolare")
G("mat-183", "Geometria", 1, "Come si chiama una corda che passa per il centro del cerchio?", "Diametro", ["Raggio", "Arco", "Tangente"],
  "Divide il cerchio in due semicerchi.", "Cerchio", "Se la corda in questione passa per il centro, essa si chiama diametro")
G("mat-184", "Geometria", 2, "Come si definisce π nella geometria piana?", "Il rapporto tra la lunghezza della circonferenza e il suo diametro", ["Il rapporto tra raggio e diametro", "L'area di un quadrato di lato 1", "La metà della circonferenza"],
  "Vale circa 3,14159.", "Pi greco", "viene definito come il rapporto tra la lunghezza della circonferenza e quella del suo diametro")
G("mat-185", "Geometria", 4, "Chi dimostrò nel 1761 che π è irrazionale?", "Johann Heinrich Lambert", ["Archimede", "Eulero", "Ferdinand von Lindemann"],
  "Lindemann dimostrò nel 1882 che è trascendente.", "Pi greco", "Johann Heinrich Lambert dimostrò nel 1761")
G("mat-186", "Geometria", 4, "Perché la quadratura del cerchio con riga e compasso è impossibile?", "Perché π è un numero trascendente", ["Perché π è razionale", "Perché il cerchio non ha area", "Perché π è maggiore di 3"],
  "Dimostrato da Ferdinand von Lindemann nel 1882.", "Pi greco", "Ferdinand von Lindemann")
G("mat-187", "Geometria", 2, "Come si chiama la parte di cerchio delimitata da due raggi e da un arco?", "Settore circolare", ["Segmento circolare", "Corona circolare", "Corda"],
  "È l'intersezione tra un angolo al centro e il cerchio.", "Cerchio", "si chiama settore circolare")
G("mat-188", "Geometria", 2, "Come si chiama la regione compresa tra due circonferenze concentriche?", "Corona circolare", ["Settore circolare", "Semicerchio", "Lunula"],
  "Voce «Cerchio».", "Cerchio", "L'area compresa fra le due circonferenze si chiama corona circolare")
G("mat-189", "Geometria", 1, "Quanti gradi misura un angolo retto?", "90°", ["180°", "45°", "360°"],
  "È la metà di un angolo piatto.", "Angolo", "un angolo retto è la metà di un angolo piatto")
G("mat-190", "Geometria", 1, "Un angolo di 35° si dice:", "Acuto", ["Ottuso", "Retto", "Piatto"],
  "È minore di un angolo retto.", "Angolo", "si dice angolo acuto")
G("mat-191", "Geometria", 1, "In quanti gradi sessagesimali si divide l'angolo giro?", "360", ["180", "400", "100"],
  "Voce «Angolo».", "Angolo", "l'angolo completo o angolo giro è suddiviso in 360 spicchi")
G("mat-192", "Geometria", 3, "Come si definisce il radiante?", "Il rapporto tra la lunghezza di un arco e il raggio della circonferenza", ["La centesima parte dell'angolo retto", "Un trecentosessantesimo dell'angolo giro", "L'angolo di un triangolo equilatero"],
  "Un angolo giro misura 2π radianti.", "Angolo", "il radiante, definito come il rapporto tra la lunghezza di un arco di circonferenza e il raggio")
G("mat-193", "Geometria solida", 1, "Quanti spigoli ha un cubo?", "12", ["8", "6", "24"],
  "6 facce, 8 vertici, 12 spigoli.", "Cubo", "presenta 6 facce quadrate, 8 vertici e 12 spigoli")
G("mat-194", "Geometria solida", 1, "Qual è il volume di un cubo con spigolo 3 cm?", "27 cm³", ["9 cm³", "18 cm³", "54 cm³"],
  "V = a³ = 3³ = 27.", "Cubo", "Ogni cubo è caratterizzato dalla lunghezza a dei suoi spigoli")
G("mat-195", "Geometria solida", 2, "Qual è il volume di un parallelepipedo rettangolo di dimensioni 2, 3 e 4 m?", "24 m³", ["9 m³", "52 m³", "26 m³"],
  "Area di base (2 · 3) per l'altezza 4.", "Parallelepipedo", "Il volume di un parallelepipedo è il prodotto dell'area di una qualsiasi delle sue 6 facce per la distanza")
G("mat-196", "Geometria solida", 3, "Qual è la formula del volume della sfera di raggio R?", "(4/3)πR³", ["4πR²", "πR²", "2πR³"],
  "4πR² è la superficie sferica.", "Sfera", "è dato dall'equazione (integrale in d")
G("mat-197", "Misure", 2, "Quante sono le unità di misura di base del Sistema internazionale (SI)?", "7", ["3", "5", "10"],
  "Metro, chilogrammo, secondo, ampere, kelvin, mole, candela.", "Sistema internazionale di unità di misura", "fino ad arrivare a sette nel 1971")
G("mat-198", "Misure", 1, "Qual è l'unità di misura della massa nel Sistema internazionale?", "Chilogrammo", ["Grammo", "Newton", "Libbra"],
  "Il sistema MKS usava metro, chilogrammo e secondo.", "Sistema internazionale di unità di misura", "le sue unità di misura erano metro, chilogrammo e secondo")
G("mat-199", "Misure", 2, "Qual è l'unità SI della temperatura assoluta?", "Kelvin", ["Grado Celsius", "Grado Fahrenheit", "Joule"],
  "Introdotta come grandezza fondamentale nel 1954.", "Sistema internazionale di unità di misura", "aggiunse la temperatura assoluta (e l'unità di misura associata: kelvin)")
G("mat-200", "Matematica finanziaria", 3, "Un capitale di 1.000 € è investito in capitalizzazione semplice al 5% annuo per 3 anni. Qual è il montante?", "1.150 €", ["1.157,63 €", "1.050 €", "1.500 €"],
  "M = C(1 + it) = 1.000 · (1 + 0,05 · 3).", "Capitalizzazione semplice", "il capitale finale, detto anche montante")
