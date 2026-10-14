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

# --- Ampliamento a 300: esercizi di aritmetica, algebra, probabilità e geometria ---
P_PRIMO = "Un numero p > 1 si dice primo se è divisibile solo per se stesso e per l'unità"
P_TFA = "Ogni numero naturale n > 1 si può scrivere in modo unico come prodotto di numeri primi"
P_MCM = "è il più piccolo tra tutti i multipli comuni di a e di b"
P_MCD = "è il più grande tra tutti i divisori comuni ad a e b"
P_DIV3 = "Un numero è divisibile per 3 se e solo se la somma delle cifre che lo compongono è divisibile per 3"
P_PROD = "Il prodotto di due potenze con la stessa base è uguale a una potenza che ha per base la stessa base"
P_QUOZ = "Il quoziente di due potenze con la stessa base, la prima con esponente maggiore o uguale"
P_POTPOT = "La potenza di una potenza è uguale a una potenza che ha la base della prima potenza"
P_SEGNI = "regola dei segni"
P_DISC = "La somma di due numeri relativi discordi"
P_FRSUM = "Se le unità frazionarie sono diverse"
P_FRPROD = "Il prodotto di due frazioni è una frazione che ha per numeratore il prodotto dei numeratori"
P_FRQUOZ = "Il quoziente di due frazioni è la frazione che si ottiene moltiplicando la prima frazione per l'inverso della"
P_MINT = "Per ridurre ai minimi termini una frazione occorre dividere numeratore e denominatore per il loro"
P_NEG = "La potenza di un numero razionale diverso da zero elevato a un esponente intero negativo"
P_SCI = "dove k è un numero decimale maggiore o uguale a 1 e minore di 10"
P_MEDI = "In ogni proporzione il prodotto dei medi è uguale al prodotto degli estremi"
P_CONT = "Una proporzione si dice continua se ha i medi uguali"
P_PERC = "Le percentuali sono frazioni che hanno come denominatore 100"
P_DIR = "si dicono direttamente proporzionali se il loro rapporto è costante"
P_INV = "si dicono inversamente proporzionali se il loro prodotto è costante"
P_MEDIA = "La media aritmetica (semplice) è il valore ottenuto sommando tutti i dati e dividendo tale somma per il numero"
P_MEDIANA = "La mediana di una successione di dati disposti in ordine crescente è il valore equidistante dagli estremi"
P_BASE = "Si definisce base di un sistema di numerazione il numero di simboli"
P_MON = "Il prodotto di due monomi è il monomio avente per coefficiente il prodotto dei coefficienti"
P_POTMON = "La potenza di un monomio è un monomio avente per coefficiente la potenza del coefficiente"
P_GRADO = "Il grado complessivo di un monomio è la somma degli esponenti della parte letterale"
P_SIMILI = "Due o più monomi che hanno parte letterale identica si dicono simili"
P_QB = "Il quadrato di un binomio è uguale alla somma tra il quadrato del primo termine"
P_CB = "Il cubo di un binomio è uguale alla somma tra il cubo del primo monomio"
P_RESTO = "Il resto della divisione di un polinomio A(x) per un binomio del tipo (x − k) è uguale al valore che A(x) assu"
P_EQ1 = "Aggiungendo o sottraendo ad ambo i membri di un'equazione data uno stesso numero"
P_EQ2 = "Moltiplicando o dividendo ambo i membri di un'equazione per uno stesso numero non nullo"
P_IS = "Risolvere un'equazione significa determinare il suo Insieme Soluzione"
P_VERSO = "cambiare il verso della disequazione"
P_SIST = "Si definisce sistema di equazioni l'insieme di più equazioni"

M("mat-201", "Numeri primi", 1, "Quale di questi numeri, compresi tra 80 e 90, è primo?", "83", ["81", "85", "87"],
  "81 = 3⁴, 85 = 5 · 17, 87 = 3 · 29; 83 ha solo due divisori.", P_PRIMO)
M("mat-202", "Numeri primi", 2, "Qual è la scomposizione in fattori primi di 84?", "2² · 3 · 7", ["2 · 42", "4 · 21", "2³ · 3 · 7"],
  "84 = 2 · 2 · 3 · 7 = 2² · 3 · 7.", P_TFA)
M("mat-203", "MCD e mcm", 3, "Qual è il minimo comune multiplo di 8, 12 e 20?", "120", ["240", "60", "40"],
  "8 = 2³, 12 = 2² · 3, 20 = 2² · 5: mcm = 2³ · 3 · 5 = 120.", P_MCM)
M("mat-204", "MCD e mcm", 2, "Qual è il massimo comune divisore di 54 e 72?", "18", ["9", "6", "24"],
  "54 = 2 · 3³, 72 = 2³ · 3²: MCD = 2 · 3² = 18.", P_MCD)
M("mat-205", "Divisibilità", 2, "Quale di questi numeri è divisibile per 3?", "2.718", ["2.719", "2.720", "2.716"],
  "2 + 7 + 1 + 8 = 18, multiplo di 3.", P_DIV3)
M("mat-206", "Potenze", 2, "Quanto vale 3⁴ · 3²?", "3⁶ = 729", ["3⁸ = 6.561", "9⁶", "3² = 9"],
  "Stessa base: si sommano gli esponenti.", P_PROD)
M("mat-207", "Potenze", 2, "Quanto vale 10⁵ : 10³?", "10² = 100", ["10⁸", "1⁵", "10¹⁵"],
  "Stessa base: si sottraggono gli esponenti.", P_QUOZ)
M("mat-208", "Potenze", 2, "Quanto vale (2³)²?", "2⁶ = 64", ["2⁵ = 32", "2⁹ = 512", "6² = 36"],
  "Potenza di potenza: si moltiplicano gli esponenti.", P_POTPOT)
M("mat-209", "Numeri relativi", 2, "Quanto vale (−1)⁷?", "−1", ["+1", "−7", "0"],
  "Una potenza di base negativa con esponente dispari è negativa.", P_SEGNI)
M("mat-210", "Numeri relativi", 2, "Quanto vale (−12) : (+4)?", "−3", ["+3", "−8", "−48"],
  "Segni discordi: il quoziente è negativo.", P_SEGNI)
M("mat-211", "Numeri relativi", 1, "Quanto vale (−5) + (+3)?", "−2", ["+2", "−8", "+8"],
  "Numeri discordi: si sottraggono i valori assoluti e si prende il segno del maggiore.", P_DISC)
M("mat-212", "Frazioni", 2, "Quanto vale 3/4 + 1/6?", "11/12", ["4/10", "4/24", "5/12"],
  "m.c.d. 12: 9/12 + 2/12 = 11/12.", P_FRSUM)
M("mat-213", "Frazioni", 2, "Quanto vale 5/6 − 1/4?", "7/12", ["4/2", "1/3", "4/12"],
  "Con denominatore 12: 10/12 − 3/12 = 7/12.", P_FRSUM)
M("mat-214", "Frazioni", 2, "Quanto vale 3/5 · 10/9?", "2/3", ["30/14", "13/14", "3/2"],
  "3/5 · 10/9 = 30/45 = 2/3.", P_FRPROD)
M("mat-215", "Frazioni", 3, "Quanto vale 4/7 : 2/21?", "6", ["8/147", "1/6", "2/3"],
  "4/7 · 21/2 = 84/14 = 6.", P_FRQUOZ)
M("mat-216", "Frazioni", 2, "Come si riduce ai minimi termini 45/60?", "3/4", ["9/12", "15/20", "5/6"],
  "Si divide per MCD(45, 60) = 15.", P_MINT)
M("mat-217", "Potenze", 3, "Quanto vale (2/3)⁻²?", "9/4", ["4/9", "−4/9", "−9/4"],
  "Esponente negativo: si prende il reciproco della base con esponente positivo.", P_NEG)
M("mat-218", "Notazione scientifica", 2, "Come si scrive 72.000 in notazione scientifica?", "7,2 · 10⁴", ["72 · 10³", "0,72 · 10⁵", "7,2 · 10³"],
  "Il coefficiente deve essere tra 1 e 10.", P_SCI)
M("mat-219", "Notazione scientifica", 2, "Come si scrive 0,0036 in notazione scientifica?", "3,6 · 10⁻³", ["36 · 10⁻⁴", "3,6 · 10⁻²", "0,36 · 10⁻²"],
  "Si sposta la virgola di 3 posti verso destra.", P_SCI)
M("mat-220", "Proporzioni", 2, "Trova x nella proporzione 4 : 7 = 12 : x.", "21", ["28", "3", "16"],
  "4 · x = 7 · 12 → x = 84/4 = 21.", P_MEDI)
M("mat-221", "Proporzioni", 2, "Trova x nella proporzione x : 6 = 10 : 15.", "4", ["9", "25", "2,5"],
  "Prodotto dei medi = prodotto degli estremi: 15x = 60, x = 4.", P_MEDI)
M("mat-222", "Proporzioni", 3, "Nella proporzione continua 9 : x = x : 16, quanto vale x?", "12", ["12,5", "25", "144"],
  "Il medio è la radice del prodotto degli estremi: x² = 144.", P_CONT)
M("mat-223", "Percentuali", 1, "Quanto è il 35% di 80?", "28", ["35", "24", "45"],
  "80 · 35 / 100 = 28.", P_PERC)
M("mat-224", "Percentuali", 2, "Su 250 candidati ne vengono ammessi 60. Che percentuale è?", "24%", ["60%", "25%", "15%"],
  "60/250 = 0,24, cioè il 24%.", P_PERC)
M("mat-225", "Percentuali", 3, "Dopo un aumento del 10% un prezzo è di 154 €. Qual era il prezzo iniziale?", "140 €", ["138,60 €", "144 €", "150 €"],
  "Prezzo iniziale = 154 / 1,10 = 140.", P_PERC)
M("mat-226", "Proporzionalità", 2, "4 penne costano 6 €. Quanto costano 10 penne?", "15 €", ["12 €", "24 €", "20 €"],
  "Proporzionalità diretta: ogni penna costa 1,50 €.", P_DIR)
M("mat-227", "Proporzionalità", 3, "8 rubinetti riempiono una vasca in 6 ore. Quanto impiegano 12 rubinetti uguali?", "4 ore", ["9 ore", "3 ore", "5 ore"],
  "Proporzionalità inversa: 8 · 6 = 12 · x → x = 4.", P_INV)
M("mat-228", "Statistica", 1, "Qual è la media aritmetica di 12, 15, 18, 21 e 24?", "18", ["15", "21", "90"],
  "La somma 90 divisa per 5 dati.", P_MEDIA)
M("mat-229", "Statistica", 3, "Qual è la mediana dei dati 4, 9, 2, 7, 5, 8?", "6", ["5", "7", "5,8"],
  "Ordinati: 2, 4, 5, 7, 8, 9; con un numero pari di dati è la media dei due centrali: (5 + 7)/2 = 6.", P_MEDIANA)
M("mat-230", "Sistemi di numerazione", 2, "Quanto vale in base 10 il numero binario 1101?", "13", ["11", "1.101", "14"],
  "1·8 + 1·4 + 0·2 + 1·1 = 13.", P_BASE)
M("mat-231", "Insiemi", 2, "Quanti sottoinsiemi ha un insieme di 4 elementi?", "16", ["8", "4", "24"],
  "L'insieme delle parti ha 2⁴ = 16 elementi.", "si chiama insieme delle parti")
M("mat-232", "Insiemi", 2, "Se A ha 4 elementi e B ne ha 3, quante coppie ordinate ha il prodotto cartesiano A × B?", "12", ["7", "64", "81"],
  "Ogni elemento di A si accoppia con ogni elemento di B: 4 · 3 = 12.", "Un insieme di due elementi a e b presi in un determinato ordine si dice coppia ordinata")
M("mat-233", "Insiemi", 2, "A = {a, b, c, d, e}, B = {c, d, f}. Quanto vale A − B?", "{a, b, e}", ["{f}", "{c, d}", "{a, b, e, f}"],
  "Gli elementi di A che non appartengono a B.", "si dice insieme differenza tra A e B l'insieme C composto da tutti gli elementi di A che non appartengono a B")
M("mat-234", "Monomi", 2, "Quanto vale (4a³b) · (−3ab²)?", "−12a⁴b³", ["12a⁴b³", "−12a³b²", "a⁴b³"],
  "Si moltiplicano i coefficienti e si sommano gli esponenti delle lettere uguali.", P_MON)
M("mat-235", "Monomi", 2, "Quanto vale (−3x²y)²?", "9x⁴y²", ["−9x⁴y²", "−6x⁴y²", "9x⁴y"],
  "Il quadrato di un numero negativo è positivo.", P_POTMON)
M("mat-236", "Monomi", 2, "Qual è il grado complessivo del monomio 5a²b³c?", "6", ["5", "3", "2"],
  "Somma degli esponenti: 2 + 3 + 1 = 6.", P_GRADO)
M("mat-237", "Monomi", 2, "Quanto vale 5xy − 8xy + xy?", "−2xy", ["−3xy", "14xy", "−2x²y²"],
  "Monomi simili: si sommano i coefficienti (5 − 8 + 1 = −2).", P_SIMILI)
M("mat-238", "Prodotti notevoli", 2, "A cosa è uguale (x + 5)²?", "x² + 10x + 25", ["x² + 25", "x² + 5x + 25", "x² + 10x + 10"],
  "Quadrato del primo, doppio prodotto, quadrato del secondo.", P_QB)
M("mat-239", "Prodotti notevoli", 3, "A cosa è uguale (2a − 3b)²?", "4a² − 12ab + 9b²", ["4a² − 9b²", "4a² + 9b²", "4a² − 6ab + 9b²"],
  "(2a)² − 2·2a·3b + (3b)².", P_QB)
M("mat-240", "Prodotti notevoli", 2, "A cosa è uguale (x + 4)(x − 4)?", "x² − 16", ["x² + 16", "x² − 8x + 16", "x² − 8"],
  "Somma per differenza: differenza dei quadrati.", "somma per differenza")
M("mat-241", "Prodotti notevoli", 3, "Quanto vale 103 · 97, usando la somma per differenza?", "9.991", ["10.009", "9.909", "10.000"],
  "(100 + 3)(100 − 3) = 10.000 − 9.", "somma per differenza")
M("mat-242", "Prodotti notevoli", 3, "A cosa è uguale (x − 1)³?", "x³ − 3x² + 3x − 1", ["x³ − 1", "x³ − 3x + 1", "x³ + 3x² − 3x − 1"],
  "Cubo di un binomio con il segno alternato.", P_CB)
M("mat-243", "Scomposizione", 2, "Come si scompone 4x² − 25?", "(2x − 5)(2x + 5)", ["(4x − 5)(x + 5)", "(2x − 5)²", "Non si può scomporre"],
  "È una differenza di due quadrati.", "differenza di due quadrati")
M("mat-244", "Scomposizione", 2, "Come si scompone 10a²b − 15ab² raccogliendo a fattore comune?", "5ab(2a − 3b)", ["5(2a²b − 3ab²)", "ab(10a − 15b)", "5a(2ab − 3b)"],
  "Il fattore comune massimo è 5ab.", "Raccoglimento totale a fattore comune")
M("mat-245", "Polinomi", 3, "Qual è il resto della divisione di x³ + 2x² − 1 per (x + 1)?", "0", ["2", "−2", "1"],
  "Per il teorema del resto: A(−1) = −1 + 2 − 1 = 0.", P_RESTO)
M("mat-246", "Equazioni", 1, "Risolvi: 4x − 9 = 2x + 7.", "x = 8", ["x = 1", "x = −8", "x = 16"],
  "2x = 16 → x = 8.", P_EQ1)
M("mat-247", "Equazioni", 2, "Risolvi: 3(x + 2) = 5x − 4.", "x = 5", ["x = 1", "x = −5", "x = 2"],
  "3x + 6 = 5x − 4 → 10 = 2x → x = 5.", P_EQ1)
M("mat-248", "Equazioni", 2, "Risolvi: x/2 + x/3 = 10.", "x = 12", ["x = 6", "x = 60", "x = 5"],
  "Moltiplicando per 6: 3x + 2x = 60 → x = 12.", P_EQ2)
M("mat-249", "Equazioni", 2, "L'equazione 2(x − 3) = 2x − 6 è:", "indeterminata (vera per ogni x)", ["impossibile", "determinata con x = 3", "determinata con x = 0"],
  "Svolgendo si ottiene 0 = 0.", P_IS)
M("mat-250", "Disequazioni", 2, "Risolvi: 5 − 2x < 11.", "x > −3", ["x < −3", "x > 3", "x < 3"],
  "−2x < 6 → dividendo per −2 il verso si inverte: x > −3.", P_VERSO)
M("mat-251", "Sistemi", 2, "Risolvi il sistema: x + y = 12; x − y = 2.", "x = 7, y = 5", ["x = 5, y = 7", "x = 6, y = 6", "x = 10, y = 2"],
  "Sommando le equazioni: 2x = 14, quindi x = 7 e y = 5.", P_SIST)
M("mat-252", "Sistemi", 2, "Risolvi il sistema: 3x + y = 11; x + y = 5.", "x = 3, y = 2", ["x = 2, y = 3", "x = 4, y = 1", "x = 1, y = 4"],
  "Sottraendo la seconda dalla prima: 2x = 6.", P_SIST)
M("mat-253", "Problemi", 2, "Due numeri hanno somma 30 e uno è il doppio dell'altro. Quali sono?", "10 e 20", ["15 e 15", "12 e 18", "5 e 25"],
  "Posto x il minore: x + 2x = 30, x = 10.", P_SIST)
M("mat-254", "Problemi", 3, "Un padre ha il triplo dell'età del figlio; insieme hanno 48 anni. Quanti anni ha il figlio?", "12", ["16", "14", "36"],
  "Posto x l'età del figlio: x + 3x = 48, x = 12.", P_SIST)
M("mat-255", "Funzioni", 2, "Data y = −3x + 2, quanto vale y per x = −1?", "5", ["−1", "−5", "1"],
  "y = −3 · (−1) + 2 = 5.", "il cui grafico è una retta, è detta funzione lineare")
M("mat-256", "Piano cartesiano", 2, "Qual è il punto medio del segmento di estremi A(−2; 6) e B(4; 0)?", "(1; 3)", ["(2; 6)", "(3; 3)", "(1; 6)"],
  "Media delle coordinate: ((−2 + 4)/2; (6 + 0)/2).", "Il punto medio di un segmento AB è il punto M interno al segmento che lo divide in due parti congruenti")
M("mat-257", "Piano cartesiano", 1, "In quale quadrante si trova il punto (−3; −5)?", "Nel terzo", ["Nel primo", "Nel secondo", "Nel quarto"],
  "Ascissa e ordinata negative.", "Gli assi dividono il piano in quattro zone chiamate quadranti")

N("mat-258", "Radicali", 1, "Quanto vale √81 + √16?", "13", ["√97", "10", "25"],
  "9 + 4 = 13; la somma delle radici non è la radice della somma.", "Si dice radice quadrata di un numero reale a positivo o nullo")
N("mat-259", "Radicali", 2, "Quanto vale 3√2 + 4√2 − √2?", "6√2", ["7√2", "6√6", "8√2"],
  "Radicali simili: si sommano i coefficienti (3 + 4 − 1).", "È possibile effettuare somme algebriche soltanto se i radicali sono simili")
N("mat-260", "Radicali", 2, "Quanto vale √3 · √12?", "6", ["√15", "36", "3√2"],
  "√3 · √12 = √36 = 6.", "Si dice radice quadrata di un numero reale a positivo o nullo")
N("mat-261", "Radicali", 3, "Razionalizzando il denominatore, a cosa è uguale 10/√5?", "2√5", ["5√2", "√50", "10√5"],
  "10√5 / 5 = 2√5.", "Per razionalizzare il denominatore")
N("mat-262", "Radicali", 3, "Quanto vale 16^(3/4)?", "8", ["12", "4", "64"],
  "(⁴√16)³ = 2³ = 8.", "Si dice potenza a esponente razionale di un numero reale positivo")
N("mat-263", "Radicali", 2, "Quanto vale la radice cubica di −125?", "−5", ["5", "Non esiste nei reali", "±5"],
  "(−5)³ = −125: la radice cubica esiste anche per i negativi.", "Si dice radice cubica di un numero reale a quel numero che, elevato al cubo")
N("mat-264", "Equazioni di secondo grado", 2, "Quali sono le soluzioni di x² − 7x + 10 = 0?", "2 e 5", ["−2 e −5", "1 e 10", "3 e 4"],
  "Δ = 49 − 40 = 9 > 0: x = (7 ± 3)/2.", "l'equazione ammette due soluzioni reali e distinte")
N("mat-265", "Equazioni di secondo grado", 2, "Quali sono le soluzioni di x² + 6x + 9 = 0?", "x₁ = x₂ = −3", ["3 e −3", "x₁ = x₂ = 3", "Nessuna soluzione reale"],
  "Δ = 36 − 36 = 0: è (x + 3)² = 0.", "radici reali e coincidenti")
N("mat-266", "Equazioni di secondo grado", 3, "Quante soluzioni reali ha x² − 2x + 5 = 0?", "Nessuna", ["Una", "Due distinte", "Due coincidenti"],
  "Δ = 4 − 20 = −16, negativo.", "l'equazione non ammette soluzioni reali")
N("mat-267", "Equazioni di secondo grado", 2, "Quali sono le soluzioni di x² − 25 = 0?", "±5", ["5", "25", "Nessuna"],
  "Equazione pura: x² = 25, x = ±5.", "Risoluzione di un'equazione di secondo grado incompleta pura")
N("mat-268", "Equazioni di secondo grado", 2, "Quali sono le soluzioni di 3x² + 12x = 0?", "0 e −4", ["0 e 4", "±2", "−4 e 4"],
  "Equazione spuria: 3x(x + 4) = 0.", "Risoluzione di un'equazione incompleta spuria")
N("mat-269", "Equazioni di secondo grado", 3, "Quanto vale il discriminante di x² − 4x + 1 = 0?", "12", ["20", "−12", "4"],
  "Δ = b² − 4ac = 16 − 4 = 12.", "prende il nome di discriminante")
N("mat-270", "Equazioni di secondo grado", 3, "Qual è la somma delle soluzioni di x² − 9x + 14 = 0?", "9", ["−9", "14", "−14"],
  "Somma = −b/a = 9 (le soluzioni sono 2 e 7).", "la somma delle radici è x1 + x2 = −")
N("mat-271", "Probabilità", 3, "Un'urna contiene 5 palline rosse e 3 blu. Estraendone due con reimmissione, qual è la probabilità che siano entrambe rosse?", "25/64", ["5/14", "10/64", "5/8"],
  "Eventi indipendenti: 5/8 · 5/8 = 25/64.", "Due eventi A e B si dicono indipendenti se il verificarsi di A non cambia la probabilità")
N("mat-272", "Probabilità", 2, "Se la probabilità di un evento è 2/5, qual è la probabilità dell'evento complementare?", "3/5", ["2/5", "5/2", "1/5"],
  "P(non A) = 1 − 2/5 = 3/5.", "si definisce evento complementare di A")
N("mat-273", "Probabilità", 3, "Lanciando un dado, qual è la probabilità di ottenere un numero pari o maggiore di 4?", "2/3", ["5/6", "1/2", "1/3"],
  "P(pari) + P(>4) − P(pari e >4) = 3/6 + 2/6 − 1/6 = 4/6.", "la probabilità dell'unione degli eventi è uguale alla somma delle probabilità dei singoli eventi meno la probabilità della loro intersezione")
N("mat-274", "Equazioni", 3, "Qual è la soluzione reale dell'equazione binomia x³ + 27 = 0?", "−3", ["3", "±3", "Nessuna"],
  "x³ = −27, quindi x = −3.", "Un'equazione binomia è un'equazione del tipo")
N("mat-275", "Equazioni", 4, "Quante soluzioni reali ha l'equazione x⁴ − 10x² + 9 = 0?", "Quattro: ±1 e ±3", ["Due: 1 e 9", "Due: ±3", "Nessuna"],
  "Posto t = x²: t² − 10t + 9 = 0 → t = 1 o t = 9.", "Sono esempi di equazioni trinomie")
N("mat-276", "Sistemi", 3, "Qual è il grado di un sistema formato da due equazioni di secondo grado?", "4", ["2", "3", "1"],
  "Il grado del sistema è il prodotto dei gradi: 2 · 2 = 4.", "è dato dal prodotto dei gradi delle equazioni che lo compongono")

G("mat-277", "Geometria", 1, "Un triangolo ha due angoli di 35° e 85°. Quanto misura il terzo?", "60°", ["70°", "50°", "90°"],
  "180° − 35° − 85° = 60°.", "Triangolo", "la somma degli angoli interni è uguale a un angolo piatto, ossia 180°")
G("mat-278", "Geometria", 2, "Quanto vale la somma degli angoli interni di un pentagono?", "540°", ["360°", "720°", "450°"],
  "(5 − 2) · 180° = 540°.", "Poligono", "La somma degli angoli interni di un poligono è pari a tanti angoli piatti quanti sono i suoi lati")
G("mat-279", "Geometria", 3, "Quanto misura ciascun angolo interno di un ottagono regolare?", "135°", ["120°", "140°", "108°"],
  "(8 − 2) · 180° / 8 = 1080° / 8 = 135°.", "Poligono", "La somma degli angoli interni di un poligono è pari a tanti angoli piatti quanti sono i suoi lati")
G("mat-280", "Geometria", 1, "Qual è il complementare di un angolo di 35°?", "55°", ["145°", "325°", "65°"],
  "Complementare: ciò che manca per arrivare a 90°.", "Angolo", "Si dice complementare di un angolo di ampiezza")
G("mat-281", "Geometria", 1, "Qual è il supplementare di un angolo di 110°?", "70°", ["250°", "20°", "80°"],
  "Supplementare: ciò che manca per arrivare a 180°.", "Angolo", "Si dice supplementare di un angolo di ampiezza")
G("mat-282", "Geometria", 2, "Qual è l'area di un rettangolo di base 12 cm e altezza 5 cm?", "60 cm²", ["34 cm²", "17 cm²", "120 cm²"],
  "Area = base per altezza = 12 · 5.", "Rettangolo", "L'area del rettangolo è il prodotto della sua lunghezza per la sua larghezza")
G("mat-283", "Geometria", 2, "Quanto è lunga la diagonale di un rettangolo di lati 12 cm e 5 cm?", "13 cm", ["17 cm", "7 cm", "√119 cm"],
  "Per Pitagora: √(144 + 25) = √169 = 13.", "Teorema di Pitagora", PIT)
G("mat-284", "Geometria", 1, "Qual è il perimetro di un rettangolo di lati 8 m e 5 m?", "26 m", ["40 m", "13 m", "80 m"],
  "Perimetro = 2 · (8 + 5) = 26.", "Rettangolo", "per il suo perimetro")
G("mat-285", "Geometria", 2, "Qual è l'area di un trapezio con basi 12 cm e 8 cm e altezza 5 cm?", "50 cm²", ["100 cm²", "25 cm²", "480 cm²"],
  "Area = (12 + 8) · 5 / 2 = 50.", "Trapezio", "del trapezio è la somma delle basi per l'altezza diviso due")
G("mat-286", "Geometria", 2, "Qual è l'area di un triangolo di base 10 cm e altezza 6 cm?", "30 cm²", ["60 cm²", "16 cm²", "15 cm²"],
  "b · h / 2 = 30: il triangolo è metà di un parallelogramma.", "Triangolo", "perché il triangolo va visto come la metà di un parallelogramma")
G("mat-287", "Geometria", 3, "Quale formula permette di calcolare l'area di un triangolo conoscendo solo i tre lati?", "La formula di Erone", ["Il teorema di Talete", "La formula di Cramer", "Il teorema di Euclide"],
  "Usa il semiperimetro p: A = √(p(p − a)(p − b)(p − c)).", "Triangolo", "il semiperimetro (formula di Erone)")
G("mat-288", "Geometria", 2, "Quanto è lunga una circonferenza di raggio 7 cm?", "14π cm", ["49π cm", "7π cm", "28π cm"],
  "L = 2πr = 2π · 7.", "Circonferenza", "La formula per trovare la lunghezza della circonferenza è")
G("mat-289", "Geometria", 2, "Quanto è lunga una circonferenza di diametro 10 m?", "10π m", ["20π m", "25π m", "5π m"],
  "L = dπ, con d = 10.", "Circonferenza", "La formula per trovare la lunghezza della circonferenza è")
G("mat-290", "Geometria", 2, "Qual è l'area di un cerchio di raggio 5 cm?", "25π cm²", ["10π cm²", "5π cm²", "100π cm²"],
  "A = πr² = π · 5².", "Cerchio", "La formula dell'area del cerchio può essere ottenuta come limite di quella del poligono regolare")
G("mat-291", "Geometria", 3, "Qual è l'area di un cerchio di diametro 8 m?", "16π m²", ["64π m²", "8π m²", "32π m²"],
  "Il raggio è 4: π · 4² = 16π.", "Cerchio", "La formula dell'area del cerchio può essere ottenuta come limite di quella del poligono regolare")
G("mat-292", "Geometria solida", 3, "Qual è l'area della superficie di una sfera di raggio 3 cm?", "36π cm²", ["9π cm²", "12π cm²", "27π cm²"],
  "A = 4πR² = 4π · 9.", "Sfera", "è data dall'equazione: A = 4 π R 2")
G("mat-293", "Geometria solida", 3, "Qual è il volume di una sfera di raggio 3 cm?", "36π cm³", ["27π cm³", "12π cm³", "108π cm³"],
  "V = (4/3)πR³ = (4/3)π · 27 = 36π.", "Sfera", "è dato dall'equazione (integrale in d")
G("mat-294", "Geometria solida", 2, "Qual è l'area totale della superficie di un cubo di spigolo 4 cm?", "96 cm²", ["64 cm²", "16 cm²", "48 cm²"],
  "Il cubo ha 6 facce quadrate: 6 · 16 = 96.", "Cubo", "presenta 6 facce quadrate, 8 vertici e 12 spigoli")
G("mat-295", "Geometria solida", 2, "Qual è il volume di un parallelepipedo rettangolo di dimensioni 3, 4 e 5 m?", "60 m³", ["12 m³", "47 m³", "94 m³"],
  "V = 3 · 4 · 5 = 60.", "Parallelepipedo", "Il volume di un parallelepipedo è il prodotto dell'area di una qualsiasi delle sue 6 facce per la distanza")
G("mat-296", "Geometria", 2, "I cateti di un triangolo rettangolo misurano 9 cm e 12 cm. Quanto misura l'ipotenusa?", "15 cm", ["21 cm", "13 cm", "√63 cm"],
  "√(81 + 144) = √225 = 15.", "Teorema di Pitagora", PIT)
G("mat-297", "Geometria", 3, "In un triangolo rettangolo l'ipotenusa misura 25 e un cateto 7. Quanto misura l'altro cateto?", "24", ["18", "√674", "26"],
  "√(625 − 49) = √576 = 24.", "Teorema di Pitagora", PIT)
G("mat-298", "Geometria", 3, "Quali valori trovò Archimede come limiti per π, usando poligoni di 96 lati?", "223/71 < π < 22/7", ["3 < π < 4", "3,14 < π < 3,15", "π = 355/113"],
  "Il valore 355/113 si deve invece a Zu Chongzhi.", "Pi greco", "lo scienziato siracusano scoprì che 223⁄71 < π < 22⁄7")
G("mat-299", "Misure", 2, "Quale grandezza misura la candela nel Sistema internazionale?", "L'intensità luminosa", ["La temperatura", "La quantità di sostanza", "La corrente elettrica"],
  "Fu aggiunta nel 1954 insieme alla temperatura assoluta.", "Sistema internazionale di unità di misura", "intensità luminosa (definendo poi come sua unità di misura la candela)")
G("mat-300", "Misure", 3, "Quale unità SI è definita attraverso il numero di Avogadro?", "La mole", ["Il kelvin", "La candela", "L'ampere"],
  "La quantità di sostanza è diventata grandezza fondamentale nel 1971.", "Sistema internazionale di unità di misura", "definisce la mole attraverso il numero di Avogadro")

# ── Verso 350: definizioni e teoremi di «Matematica dolce 1» (MatematicaC3, 2021, CC BY-SA 3.0),
#    con piccole applicazioni: aritmetica, frazioni, calcolo letterale, geometria, insiemi,
#    relazioni e funzioni, statistica.
DOL = "MatematicaDolce_vol1.txt"
FDOL = "MatematicaC3, Matematica dolce 1 (CC BY-SA 3.0)"
def Q(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, FDOL, DOL, frase)

Q("mat-301", "Numeri naturali", 2, "Quanto vale 47 mod 5, cioè il resto della divisione intera di 47 per 5?", "2", ["9", "7", "0"],
  "47 = 5 · 9 + 2: l'operazione «modulo» restituisce il resto, 2.", "si chiama modulo di m rispetto a n")
Q("mat-302", "Divisibilità", 3, "Quanti divisori propri ha il numero 30?", "6", ["8", "4", "3"],
  "I divisori di 30 sono 1, 2, 3, 5, 6, 10, 15, 30; esclusi 1 e 30 restano 6 divisori propri.", "Chiamiamo divisore proprio di un numero un divisore diverso dal numero stesso e dall'unità")
Q("mat-303", "Divisibilità", 3, "Quale di questi numeri ha un numero dispari di divisori (ed è quindi un quadrato)?", "36", ["12", "18", "20"],
  "36 ha 9 divisori (1, 2, 3, 4, 6, 9, 12, 18, 36); gli altri ne hanno 6.", "si dice quadrato se ha un numero dispari di divisori")
Q("mat-304", "Numeri reali", 3, "Il numero 2,333… (2 con periodo 3) è razionale?", "Sì, perché è un decimale periodico", ["No, perché ha infinite cifre", "No, perché non è intero", "Solo se si arrotonda a 2,3"],
  "Ogni decimale limitato o periodico è razionale: 2,(3) = 7/3.", "Un numero razionale può essere scritto come numero decimale limitato o come numero decimale periodico")
Q("mat-305", "Frazioni", 3, "Tra due numeri razionali diversi, quanti altri numeri razionali ci sono?", "Sempre almeno uno, e quindi infiniti", ["Nessuno", "Esattamente uno", "Dipende dai numeri"],
  "L'insieme dei razionali è denso: tra due razionali diversi c'è sempre la loro media, e così via.", "Tra due numeri razionali diversi esiste sempre almeno un altro numero razionale")
Q("mat-306", "Frazioni", 2, "Le frazioni 6/8 e 9/12 sono equivalenti?", "Sì, perché 6 · 12 = 8 · 9", ["No, hanno denominatori diversi", "No, perché 6 + 12 ≠ 8 + 9", "Solo se semplificate a 2/3"],
  "Due frazioni sono equivalenti se i prodotti in croce sono uguali: 72 = 72.", "Due frazioni sono equivalenti se il prodotto del numeratore della prima per il denominatore della seconda")
Q("mat-307", "Frazioni", 2, "Qual è il reciproco di 0?", "Non è definito", ["0", "1", "Infinito"],
  "Il reciproco di a è il numero a' tale che a · a' = 1: per lo zero non esiste.", "Il reciproco di zero non è definito")
Q("mat-308", "Percentuali", 3, "Su un oggetto da 84 € si ottiene uno sconto di 10 €. Che percentuale di sconto è, circa?", "11,9%", ["10%", "8,4%", "12,5%"],
  "La percentuale è il rapporto tra le due grandezze per 100: 10 / 84 · 100 ≈ 11,9%.", "La percentuale è il rapporto tra due grandezze moltiplicato per 100")
Q("mat-309", "Frazioni", 4, "Qual è la frazione generatrice di 0,1666… (cioè 0,1 con periodo 6)?", "1/6", ["16/99", "1/16", "16/90"],
  "Numeratore: 16 − 1 = 15; denominatore: un 9 per la cifra del periodo e uno 0 per l'antiperiodo, 90. 15/90 = 1/6.", "per denominatore tanti 9 quante sono le cifre del periodo")
Q("mat-310", "Frazioni", 3, "Qual è la frazione generatrice di 0,363636… (periodo 36)?", "4/11", ["36/100", "9/25", "36/90"],
  "36/99, che semplificata per 9 dà 4/11.", "per denominatore tanti 9 quante sono le cifre del periodo")
Q("mat-311", "Monomi", 3, "Quando un monomio si dice «fratto»?", "Quando ha lettere al denominatore (esponenti negativi)", ["Quando ha coefficiente frazionario", "Quando ha grado zero", "Quando contiene un'addizione"],
  "Un monomio è intero se non ha lettere al denominatore, altrimenti è fratto; il coefficiente può essere una frazione.", "Diciamo che un monomio è intero se non ha lettere al denominatore")
Q("mat-312", "Monomi", 2, "Quale monomio è opposto di 3a²b?", "−3a²b", ["3ab²", "1/(3a²b)", "−3ab"],
  "Due monomi simili con coefficienti opposti sono opposti: la loro somma è 0.", "Si dicono opposti due monomi simili che hanno coefficiente opposto")
Q("mat-313", "Geometria", 3, "Come si chiamano due rette che non appartengono a uno stesso piano?", "Sghembe", ["Parallele", "Incidenti", "Coincidenti"],
  "Due rette nello stesso piano sono complanari; altrimenti sono sghembe e non hanno punti in comune.", "altrimenti si dicono sghembe")
Q("mat-314", "Geometria", 3, "Come si chiama l'insieme di tutte le rette di un piano che passano per uno stesso punto?", "Fascio proprio di rette", ["Fascio improprio", "Stella di piani", "Semipiano"],
  "Il punto comune a tutte le rette si dice centro del fascio.", "è detto fascio proprio di rette")
Q("mat-315", "Geometria", 3, "Quando due segmenti si dicono adiacenti?", "Quando sono consecutivi e appartengono alla stessa retta", ["Quando hanno la stessa lunghezza", "Quando non hanno punti in comune", "Quando sono perpendicolari"],
  "Consecutivi: un solo estremo in comune; adiacenti: consecutivi e sulla stessa retta.", "Due segmenti si dicono adiacenti se sono consecutivi ed appartengono alla stessa retta")
Q("mat-316", "Geometria", 3, "Quando una figura si dice convessa?", "Se il segmento che unisce due suoi punti qualsiasi è tutto contenuto nella figura", ["Se ha almeno un angolo ottuso", "Se ha tutti i lati uguali", "Se è un cerchio"],
  "Se invece esistono due punti per cui il segmento esce dalla figura, la figura è concava.", "il segmento che li unisce è contenuto nella figura")
Q("mat-317", "Geometria", 1, "Come si chiama l'angolo i cui lati sono uno il prolungamento dell'altro?", "Angolo piatto", ["Angolo retto", "Angolo giro", "Angolo nullo"],
  "L'angolo piatto misura 180°; l'angolo retto ne è la metà.", "Un angolo si dice piatto se i suoi lati sono uno il prolungamento dell'altro")
Q("mat-318", "Geometria", 2, "Due angoli adiacenti, quanto misurano insieme?", "180°, cioè un angolo piatto", ["90°", "360°", "Dipende dagli angoli"],
  "Sono consecutivi e i lati non comuni stanno sulla stessa retta: insieme formano un angolo piatto.", "Due angoli si dicono adiacenti se sono consecutivi e se i lati non comuni giacciono sulla stessa retta")
Q("mat-319", "Geometria", 2, "Che relazione c'è tra due angoli opposti al vertice?", "Sono congruenti", ["Sono supplementari", "Sono complementari", "Sono sempre retti"],
  "Teorema: angoli opposti al vertice sono congruenti (supplementari dello stesso angolo).", "Angoli opposti al vertice sono congruenti")
Q("mat-320", "Geometria", 2, "La bisettrice di un angolo di 70° lo divide in due angoli di:", "35°", ["70°", "20°", "110°"],
  "La bisettrice è la semiretta dal vertice che divide l'angolo in due parti congruenti.", "Si dice bisettrice di un angolo la semiretta che ha origine nel vertice dell'angolo")
Q("mat-321", "Geometria", 3, "Come si misura la distanza di un punto P da una retta?", "Con la lunghezza del segmento perpendicolare condotto da P alla retta", ["Con il segmento più lungo da P alla retta", "Con un segmento qualsiasi da P alla retta", "Con l'angolo tra P e la retta"],
  "La distanza punto-retta è la lunghezza del segmento di perpendicolare condotto dal punto alla retta.", "la lunghezza del segmento di perpendicolare condotta dal punto P alla retta")
Q("mat-322", "Geometria", 4, "Come si chiama una spezzata chiusa non intrecciata?", "Poligonale", ["Poligono regolare", "Spezzata aperta", "Corda"],
  "Una poligonale con la parte finita di piano che delimita forma un poligono.", "Si chiama poligonale una spezzata chiusa non intrecciata")
Q("mat-323", "Piano cartesiano", 3, "Cos'è un riferimento cartesiano ortogonale monometrico?", "Due assi perpendicolari con origine comune e uguale unità di misura", ["Due assi paralleli", "Un solo asse con l'origine", "Due assi con unità di misura diverse"],
  "Ortogonale: assi perpendicolari; monometrico: stessa unità di misura sui due assi.", "Si chiama riferimento cartesiano ortogonale monometrico la coppia di assi cartesiani perpendicolari")
Q("mat-324", "Insiemi", 2, "Le coppie ordinate (2, 5) e (5, 2) sono uguali?", "No, perché in una coppia ordinata conta l'ordine", ["Sì, hanno gli stessi elementi", "Sì, se 2 e 5 sono primi", "Solo nel piano cartesiano"],
  "Una coppia ordinata è formata da due elementi presi in un certo ordine: (a, b) ≠ (b, a) se a ≠ b.", "presi in un certo ordine si dice coppia ordinata")
Q("mat-325", "Relazioni", 4, "Quali proprietà deve avere una relazione per essere una relazione d'ordine?", "Antisimmetrica e transitiva", ["Riflessiva, simmetrica e transitiva", "Solo simmetrica", "Solo riflessiva"],
  "Esempio: «minore o uguale a» tra numeri. Riflessiva, simmetrica e transitiva caratterizzano invece l'equivalenza.", "si chiama relazione d'ordine se è antisimmetrica e transitiva")
Q("mat-326", "Funzioni", 2, "Come si chiama la funzione che associa a ogni valore di x lo stesso valore di y (es. y = 4)?", "Funzione costante", ["Funzione identità", "Proporzionalità diretta", "Funzione lineare crescente"],
  "Il grafico di una funzione costante è una retta parallela all'asse x.", "Si chiama funzione costante la legge che associa ad ogni valore")
Q("mat-327", "Funzioni", 2, "Data la funzione f(x) = 2x + 1, qual è l'immagine di 3?", "7", ["6", "5", "3"],
  "L'immagine di x è il valore y = f(x) del codominio: f(3) = 2 · 3 + 1 = 7.", "viene detto immagine di x nella funzione f")
Q("mat-328", "Statistica", 2, "In statistica, come si chiama ciascun elemento della popolazione oggetto d'indagine?", "Unità statistica", ["Carattere", "Modalità", "Frequenza"],
  "L'insieme oggetto dell'indagine è la popolazione (o universo); ogni suo elemento è un'unità statistica.", "mentre ciascun elemento della popolazione è detto unità statistica")
Q("mat-329", "Statistica", 3, "Cosa indica la frequenza di una modalità di un carattere?", "Il numero di unità statistiche in cui quella modalità si presenta", ["Il valore medio dei dati", "Il dato più alto", "La differenza tra massimo e minimo"],
  "Se 12 studenti su 30 hanno gli occhi castani, la frequenza della modalità «castani» è 12.", "si definisce frequenza il numero delle unità statistiche su cui una sua modalità si presenta")
Q("mat-330", "Statistica", 2, "Qual è la moda dei dati 3, 5, 5, 7, 8?", "5", ["5,6", "7", "8"],
  "La moda è il valore che si presenta più spesso.", "La moda è la modalità del carattere indagato che si presenta più frequentemente")
Q("mat-331", "Statistica", 3, "Dati 4, 6, 8 (media 6), qual è lo scarto dalla media del valore 8?", "+2", ["8", "−2", "0"],
  "Lo scarto è la differenza tra valore osservato e media: 8 − 6 = 2.", "Si definisce scarto dalla media (aritmetica) la differenza tra i valori osservati e la media")
Q("mat-332", "Statistica", 3, "Uno studente ha preso 6 in due verifiche e 9 in una. Qual è la media ponderata?", "7", ["7,5", "6,5", "8"],
  "(6 · 2 + 9 · 1) / 3 = 21 / 3 = 7: ogni dato pesa per la sua frequenza.", "La media aritmetica ponderata è il valore ottenuto moltiplicando ciascun dato con la propria frequenza")
Q("mat-333", "Geometria", 3, "Cosa afferma il primo criterio di congruenza dei triangoli?", "Sono congruenti se hanno congruenti due lati e l'angolo tra essi compreso", ["Sono congruenti se hanno tre angoli congruenti", "Sono congruenti se hanno la stessa area", "Sono congruenti se hanno un lato congruente"],
  "Primo criterio: lato-angolo-lato.", "Due triangoli sono congruenti se hanno congruenti due lati e l'angolo tra essi compreso")
Q("mat-334", "Geometria", 3, "Cosa afferma il secondo criterio di congruenza dei triangoli?", "Sono congruenti se hanno congruenti due angoli e il lato tra essi compreso", ["Sono congruenti se hanno congruenti le tre coppie di lati", "Sono congruenti se hanno lo stesso perimetro", "Sono congruenti se sono entrambi rettangoli"],
  "Secondo criterio: angolo-lato-angolo.", "Due triangoli sono congruenti se hanno congruenti due angoli e il lato tra essi compreso")
Q("mat-335", "Geometria", 3, "Cosa afferma il terzo criterio di congruenza dei triangoli?", "Sono congruenti se hanno congruenti le tre coppie di lati", ["Sono congruenti se hanno congruenti tre angoli", "Sono congruenti se hanno due lati congruenti", "Sono congruenti se hanno la stessa altezza"],
  "Terzo criterio: lato-lato-lato. Tre angoli congruenti non bastano (triangoli simili).", "Due triangoli sono congruenti se hanno congruenti le tre coppie di lati")
Q("mat-336", "Geometria", 2, "In un triangolo isoscele, cosa si può dire degli angoli alla base?", "Sono congruenti", ["Sono complementari", "Sono retti", "Sono diversi"],
  "Teorema diretto del triangolo isoscele.", "In un triangolo isoscele gli angoli alla base sono congruenti")
Q("mat-337", "Geometria", 3, "Se un triangolo ha due angoli congruenti, allora:", "È isoscele", ["È equilatero", "È rettangolo", "È scaleno"],
  "Teorema inverso del triangolo isoscele: la base è il lato compreso tra gli angoli congruenti.", "Se un triangolo ha due angoli congruenti, allora è isoscele")
Q("mat-338", "Geometria", 3, "Quanti punti ci sono, su una retta, tra due suoi punti distinti A e B?", "Infiniti (una quantità illimitata)", ["Nessuno", "Uno solo", "Due"],
  "Tra A e B c'è un punto C; tra A e C un altro, e così via senza fine.", "Tra due punti di una retta esiste sempre una quantità illimitata di altri punti")
Q("mat-339", "Geometria", 3, "Due angoli sono congruenti. Cosa si può dire dei loro supplementari?", "Sono anch'essi congruenti", ["Sono complementari", "Sono opposti al vertice", "Non si può dire nulla"],
  "Angoli supplementari di angoli congruenti sono congruenti.", "Angoli supplementari di angoli congruenti sono congruenti")
Q("mat-340", "Geometria", 1, "Un angolo convesso di 120° si dice:", "Ottuso", ["Acuto", "Retto", "Piatto"],
  "Ottuso: maggiore di un angolo retto (e convesso); acuto: minore di un angolo retto.", "Un angolo convesso si dice ottuso se è maggiore di un angolo retto")
Q("mat-341", "Geometria", 2, "Quando due rette si dicono perpendicolari?", "Quando sono incidenti e formano quattro angoli retti", ["Quando non si incontrano mai", "Quando formano due angoli acuti", "Quando coincidono"],
  "Si scrive r ⊥ s.", "Due rette si dicono perpendicolari se sono incidenti e formano tra loro quattro angoli retti")
Q("mat-342", "Geometria", 3, "Cos'è l'asse di un segmento?", "La retta perpendicolare al segmento passante per il suo punto medio", ["La retta che contiene il segmento", "La metà del segmento", "Una retta parallela al segmento"],
  "Due punti sono simmetrici rispetto a una retta se questa è l'asse del segmento che li unisce.", "Si chiama asse di un segmento la retta perpendicolare al segmento e passante per il suo punto medio")
Q("mat-343", "Geometria", 2, "Come si chiamano due rette che hanno un solo punto in comune?", "Incidenti", ["Parallele", "Coincidenti", "Sghembe"],
  "Se hanno almeno due punti in comune sono coincidenti; se nessuno e sono complanari, parallele.", "Due rette che hanno un solo punto in comune si dicono incidenti")
Q("mat-344", "Geometria", 2, "In un poligono, cos'è una diagonale?", "Una corda che unisce due vertici non consecutivi", ["Un lato del poligono", "Il segmento che unisce due vertici consecutivi", "La retta che divide a metà un angolo"],
  "Corda: segmento tra due punti del contorno non sullo stesso lato; diagonale: corda tra vertici non consecutivi.", "diagonale ogni corda che unisce due vertici non consecutivi")
Q("mat-345", "Numeri naturali", 2, "Per la proprietà invariantiva della sottrazione, 83 − 47 è uguale a:", "86 − 50", ["80 − 50", "83 − 50", "86 − 44"],
  "Aggiungendo 3 a entrambi i termini la differenza non cambia: 36 in entrambi i casi.", "Aggiungendo o togliendo ad entrambi i termini di una sottrazione la stessa quantità la differenza non cambia")
Q("mat-346", "Numeri naturali", 2, "Per la proprietà invariantiva della divisione, 350 : 50 è uguale a:", "35 : 5", ["350 : 5", "300 : 0", "35 : 50"],
  "Dividendo entrambi i termini per 10 il quoziente non cambia: 7.", "Moltiplicando o dividendo entrambi i termini di una divisione per la stessa quantità, diversa da zero, il quoziente non cambia")
Q("mat-347", "Geometria", 3, "Quando una spezzata si dice chiusa?", "Quando il primo estremo del primo segmento coincide con l'ultimo estremo dell'ultimo", ["Quando ha almeno quattro lati", "Quando i lati si intersecano", "Quando tutti i lati sono uguali"],
  "Altrimenti la spezzata è aperta; se due lati non consecutivi si incontrano è intrecciata.", "si dice chiusa se il primo estremo del primo segmento coincide con l'ultimo estremo dell'ultimo segmento")
Q("mat-348", "Geometria", 2, "Qual è il punto medio di un segmento AB?", "Il punto interno che lo divide in due parti congruenti", ["Uno degli estremi", "Un punto qualsiasi del segmento", "Il punto più vicino ad A"],
  "AM ≅ MB; si costruisce con riga e compasso tracciando l'asse del segmento.", "il punto M interno al segmento che lo divide in due parti tra loro congruenti")
Q("mat-349", "Geometria", 1, "Quanti lati ha un ettagono?", "7", ["6", "8", "9"],
  "Triangolo 3, quadrilatero 4, pentagono 5, esagono 6, ettagono 7 lati.", "ettagono: 7 lati")
Q("mat-350", "Insiemi", 3, "Come si chiama un insieme che contiene l'insieme A come sottoinsieme e in cui si studia A?", "Insieme universo (o ambiente)", ["Insieme vuoto", "Insieme delle parti", "Insieme complementare"],
  "Rispetto all'universo U si definisce il complementare di A: gli elementi di U che non stanno in A.", "si dice insieme universo o insieme ambiente")

# ── Banca dati ministeriale «1° Livello – Algebra» (algebra.pdf): domande riportate così come sono,
#    la risposta esatta è la A) del PDF. Generato con scripts/domande/da_banca_ministeriale.py.
D("mat-351", "Radicali", 2, "Il numero 80 si ottiene dalla radice quadrata di:",
  "6400", ["190", "9600", "8000"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 1: la risposta esatta è «6400».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 1", "algebra.txt", "Il numero 80 si ottiene dalla radice quadrata di:")
D("mat-352", "Equazioni", 2, "Qual è il valore della x nella proporzione 50 : 5 = 110 : x ?",
  "11", ["13", "10", "9"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 8: la risposta esatta è «11».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 8", "algebra.txt", "Qual è il valore della x nella proporzione 50 : 5 = 110 : x ?")
D("mat-353", "Radicali", 2, "Indicare la radice quadrata di 256:",
  "16", ["23", "0,23", "32"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 15: la risposta esatta è «16».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 15", "algebra.txt", "Indicare la radice quadrata di 256:")
D("mat-354", "Numeri relativi", 2, "L'espressione (-3a)∙(-4a) è uguale a:",
  "12a²", ["-12a", "-12a²", "12a"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 23: la risposta esatta è «12a²».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 23", "algebra.txt", "L'espressione (-3a)∙(-4a) è uguale a:")
D("mat-355", "Probabilità", 2, "Lanciando una moneta, qual è la probabilità che si ottenga testa?",
  "1/2", ["1/3", "2", "1/5"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 30: la risposta esatta è «1/2».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 30", "algebra.txt", "Lanciando una moneta, qual è la probabilità che si ottenga testa?")
D("mat-356", "Equazioni", 2, "Risolvere l'equazione 3x + 3 = 2x.",
  "x = -3", ["x = 4", "x = 2", "x = -2"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 37: la risposta esatta è «x = -3».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 37", "algebra.txt", "Risolvere l'equazione 3x + 3 = 2x.")
D("mat-357", "Prodotti notevoli", 2, "L'espressione (-8a⁴c)² è uguale a:",
  "64a⁸ c²", ["64bc", "64a¹²", "-64a⁴ c²"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 46: la risposta esatta è «64a⁸ c²».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 46", "algebra.txt", "L'espressione (-8a⁴c)² è uguale a:")
D("mat-358", "Monomi", 2, "Calcolare il valore dell'espressione letterale: 5a + 4b – 15. Per a = -7; b = 4",
  "-34", ["-32", "-45", "-17"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 55: la risposta esatta è «-34».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 55", "algebra.txt", "Calcolare il valore dell'espressione letterale: 5a + 4b – 15. Per a = -7; b = 4")
D("mat-359", "Potenze", 2, "10⁷ · 10⁴ : 10² =",
  "10⁹", ["10⁵", "10¹⁴", "10¹³"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 62: la risposta esatta è «10⁹».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 62", "algebra.txt", "10⁷ · 10⁴ : 10² =")
D("mat-360", "Equazioni", 2, "Calcolare x nell'equazione 2(x + 3) = 4(x - 4)",
  "11", ["-11", "-3,5", "3,5"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 97: la risposta esatta è «11».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 97", "algebra.txt", "Calcolare x nell'equazione 2(x + 3) = 4(x - 4)")
D("mat-361", "Potenze", 2, "8¹² · 8³: 8⁶ =",
  "8⁹", ["8¹⁵", "8²¹", "8⁶"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 104: la risposta esatta è «8⁹».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 104", "algebra.txt", "8¹² · 8³: 8⁶ =")
D("mat-362", "Probabilità", 2, "La parola GONIOMETRO viene tagliata in bigliettini, ognuno dei quali contiene una sola lettera. Qual è la probabilità che estraendo a caso uno dei biglietti si ottenga la lettera M?",
  "1/10", ["5/10", "3/10", "0"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 140: la risposta esatta è «1/10».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 140", "algebra.txt", "La parola GONIOMETRO viene tagliata in bigliettini, ognuno dei quali contiene una sola lettera. Qual è la probabilità che estraendo a caso uno dei biglietti si ottenga la lettera M?")
D("mat-363", "Monomi", 2, "eseguire la seguente addizione algebrica: a + 3a - 7a",
  "-3a", ["-3", "-3a + a", "-11a"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 185: la risposta esatta è «-3a».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 185", "algebra.txt", "eseguire la seguente addizione algebrica: a + 3a - 7a")
D("mat-364", "Frazioni", 2, "Eseguire la seguente addizione algebrica: (+5/12a²b²) - (-1/2a²b²) + (-2/3a²b²) - (-3/4a²b²)",
  "+a²b²", ["-a²b²", "0", "-2a²b²"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 199: la risposta esatta è «+a²b²».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 199", "algebra.txt", "Eseguire la seguente addizione algebrica: (+5/12a²b²) - (-1/2a²b²) + (-2/3a²b²) - (-3/4a²b²)")
D("mat-365", "Potenze", 2, "Eseguire la seguente addizione algebrica: 3x²y - 2x²y² + 6x²y² - 4x²y",
  "+4x²y² - x²y", ["+2x²y² - 4x²y", "x²y² + x²y", "+4x²y²"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 206: la risposta esatta è «+4x²y² - x²y».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 206", "algebra.txt", "Eseguire la seguente addizione algebrica: 3x²y - 2x²y² + 6x²y² - 4x²y")
D("mat-366", "Polinomi", 2, "Eseguire la seguente moltiplicazione di polinomi: (x+y²)(x²+y)",
  "x³+xy+x²y²+y³", ["x³-xy+x²y²+y³", "x³+xy-x²y²+y³", "x³+xy+x²y²-y³"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 213: la risposta esatta è «x³+xy+x²y²+y³».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 213", "algebra.txt", "Eseguire la seguente moltiplicazione di polinomi: (x+y²)(x²+y)")
D("mat-367", "Polinomi", 2, "Eseguire la seguente moltiplicazione di polinomi: (a+b)(a³-4a²b+ab²-b³)",
  "a⁴-3a³b-3a²b²-b⁴", ["a⁴+3a³b+3a²b²-b⁴", "-a⁴+3a³b-3a²b²-b⁴", "a⁴-3a³b-3a²b²+b⁴"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 220: la risposta esatta è «a⁴-3a³b-3a²b²-b⁴».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 220", "algebra.txt", "Eseguire la seguente moltiplicazione di polinomi: (a+b)(a³-4a²b+ab²-b³)")
D("mat-368", "Potenze", 2, "Risolvere la seguente espressione: 3(2x+y)-2(2x+y²)+3x(1-y)+y²",
  "5x-3xy+3y-y²", ["-5x-3xy+3y+y²", "5x+3xy-3y-y²", "-5x-3xy+3y-y²"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 234: la risposta esatta è «5x-3xy+3y-y²».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 234", "algebra.txt", "Risolvere la seguente espressione: 3(2x+y)-2(2x+y²)+3x(1-y)+y²")
D("mat-369", "Prodotti notevoli", 2, "Risolvere la seguente espressione applicando i prodotti notevoli: (a-b)²+2ab",
  "a²+b²", ["a²", "b²", "2ab"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 255: la risposta esatta è «a²+b²».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 255", "algebra.txt", "Risolvere la seguente espressione applicando i prodotti notevoli: (a-b)²+2ab")
D("mat-370", "Espressioni", 2, "Eseguire la seguente espressione: (x+y)(x-2y)+(x-y)(x+2y)",
  "2x²-4y²", ["-2x²-4y²", "2x²", "2x²+4y²"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 262: la risposta esatta è «2x²-4y²».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 262", "algebra.txt", "Eseguire la seguente espressione: (x+y)(x-2y)+(x-y)(x+2y)")
D("mat-371", "Prodotti notevoli", 2, "Semplificare la seguente espressione: (a+3)³-2(a²-1)(a+1)-3(a+3)²",
  "-a³+4a²+11a+2", ["-a³-4a²+11a-2", "a³+4a²-11a+2", "-2a³+2a²+11a+1"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 283: la risposta esatta è «-a³+4a²+11a+2».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 283", "algebra.txt", "Semplificare la seguente espressione: (a+3)³-2(a²-1)(a+1)-3(a+3)²")
D("mat-372", "Polinomi", 2, "Scomporre il numero 66 in fattori primi:",
  "2 ∙ 3 ∙ 11", ["3² ∙ 11", "2² ∙ 3²", "2² ∙ 3 ∙ 5"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 319: la risposta esatta è «2 ∙ 3 ∙ 11».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 319", "algebra.txt", "Scomporre il numero 66 in fattori primi:")
D("mat-373", "Frazioni", 2, "Indicare il risultato dell'addizione (1/5) + (5/6):",
  "31/30", ["5/30", "1/6", "7/3"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 326: la risposta esatta è «31/30».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 326", "algebra.txt", "Indicare il risultato dell'addizione (1/5) + (5/6):")
D("mat-374", "Frazioni", 2, "Indicare il risultato della sottrazione (12/13) - (3/5):",
  "21/65", ["21/11", "12/3", "9/8"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 333: la risposta esatta è «21/65».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 333", "algebra.txt", "Indicare il risultato della sottrazione (12/13) - (3/5):")
D("mat-375", "Piano cartesiano", 2, "Indicare la relazione corretta:",
  "7/9<7/8", ["7/8>1", "7/8=7/9", "7/8<7/9"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 340: la risposta esatta è «7/9<7/8».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 340", "algebra.txt", "Indicare la relazione corretta:")
D("mat-376", "Equazioni", 2, "Qual è il valore della x nell'equazione di primo grado: 2x(2 + 1) – 2 = x – 7?",
  "-1", ["1", "5", "-5"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 354: la risposta esatta è «-1».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 354", "algebra.txt", "Qual è il valore della x nell'equazione di primo grado: 2x(2 + 1) – 2 = x – 7?")
D("mat-377", "Prodotti notevoli", 2, "Applica le regole dei prodotti notevoli per calcolare il valore della seguente espressione: (a³ + 2b²)²",
  "a⁶ + 4b⁴ + 4b²a³", ["a⁶ + 4b⁴ + b²a³", "a⁶ + 4b⁴", "a⁶ + 4b⁴ + 4b⁴a⁶"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 361: la risposta esatta è «a⁶ + 4b⁴ + 4b²a³».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 361", "algebra.txt", "Applica le regole dei prodotti notevoli per calcolare il valore della seguente espressione: (a³ + 2b²)²")
D("mat-378", "Piano cartesiano", 2, "Quale dei seguenti punti appartiene alla retta di equazione x + 2y - 2 = 0?",
  "(0,1)", ["(1,0)", "(5,6)", "(-1,2)"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 368: la risposta esatta è «(0,1)».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 368", "algebra.txt", "Quale dei seguenti punti appartiene alla retta di equazione x + 2y - 2 = 0?")
D("mat-379", "Potenze", 2, "5³ + 2³ – 3³ =",
  "106", ["24", "121", "212"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 391: la risposta esatta è «106».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 391", "algebra.txt", "5³ + 2³ – 3³ =")
D("mat-380", "Potenze", 2, "5¹² : 5⁷ · 5³ =",
  "5⁸", ["5⁵", "5²", "5¹⁶"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 461: la risposta esatta è «5⁸».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 461", "algebra.txt", "5¹² : 5⁷ · 5³ =")
D("mat-381", "Probabilità", 2, "Qual è la probabilità che esca il numero 5 lanciando un dado?",
  "1/6", ["5", "2/6", "1/3"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 469: la risposta esatta è «1/6».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 469", "algebra.txt", "Qual è la probabilità che esca il numero 5 lanciando un dado?")
D("mat-382", "Potenze", 2, "Quanto vale l'espressione letterale -12a² se a = -2?",
  "-48", ["24", "48", "-24"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 483: la risposta esatta è «-48».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 483", "algebra.txt", "Quanto vale l'espressione letterale -12a² se a = -2?")
D("mat-383", "Piano cartesiano", 2, "Quale delle seguenti rette è parallela all'asse delle y?",
  "x=12", ["x=2y", "y=1", "y=x-1"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 490: la risposta esatta è «x=12».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 490", "algebra.txt", "Quale delle seguenti rette è parallela all'asse delle y?")
D("mat-384", "Piano cartesiano", 2, "Quale delle seguenti rette non passa per l'origine?",
  "y=2x+1", ["y=2x", "3x-y=0", "x=y"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 497: la risposta esatta è «y=2x+1».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 497", "algebra.txt", "Quale delle seguenti rette non passa per l'origine?")
D("mat-385", "Monomi", 2, "Quale tra i seguenti monomi ha il grado maggiore?",
  "4ab³c", ["2a²bc", "6abc²", "4a²b²"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 519: la risposta esatta è «4ab³c».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 519", "algebra.txt", "Quale tra i seguenti monomi ha il grado maggiore?")
D("mat-386", "Probabilità", 2, "In uno scaffale della libreria vi sono 2 libri di narrativa, 15 polizieschi e 3 testi scientifici. Prendendo un libro a caso qual è la probabilità che si tratti di un libro di narrativa?",
  "1/10", ["1/20", "20/2", "15/20"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 541: la risposta esatta è «1/10».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 541", "algebra.txt", "In uno scaffale della libreria vi sono 2 libri di narrativa, 15 polizieschi e 3 testi scientifici. Prendendo un libro a caso qual è la probabilità che si tratti di un libro di narrativa?")
D("mat-387", "Potenze", 2, "A quale potenza corrisponde il numero 8?",
  "2³", ["5³", "4²", "3²"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 548: la risposta esatta è «2³».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 548", "algebra.txt", "A quale potenza corrisponde il numero 8?")
D("mat-388", "Equazioni", 2, "L'equazione x-9=2x-6 che soluzione ammette?",
  "x=-3", ["x=2", "x=-2", "x=3"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 555: la risposta esatta è «x=-3».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 555", "algebra.txt", "L'equazione x-9=2x-6 che soluzione ammette?")
D("mat-389", "Disequazioni", 2, "Risolvere la seguente disequazione 3x+6(1-x)<(x-1)",
  "x>7/4", ["x>-(1/7)", "x<3/4", "x<4/7"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 562: la risposta esatta è «x>7/4».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 562", "algebra.txt", "Risolvere la seguente disequazione 3x+6(1-x)<(x-1)")
D("mat-390", "Frazioni", 2, "Disporre in ordine decrescente i valori seguenti: a=-1/2 b=-1,23 c=-0,55 d=-4/9.",
  "d > a > c > b", ["d > a > b > c", "a > c > d > b", "c > b > a > d"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 577: la risposta esatta è «d > a > c > b».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 577", "algebra.txt", "Disporre in ordine decrescente i valori seguenti: a=-1/2 b=-1,23 c=-0,55 d=-4/9.")
D("mat-391", "Monomi", 2, "Eseguire la seguente moltiplicazione di monomi: (-4/5xyz)(-15/8xy)",
  "+ 3/2x²y²z", ["- 3/2x²y²z", "+ x²y²z", "+ 2/3x²y²z"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 598: la risposta esatta è «+ 3/2x²y²z».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 598", "algebra.txt", "Eseguire la seguente moltiplicazione di monomi: (-4/5xyz)(-15/8xy)")
D("mat-392", "Polinomi", 2, "Eseguire la seguente sottrazione tra polinomi: (2ab+3c) - (2ab-2c)",
  "5c", ["c", "ab+5c", "-5c"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 613: la risposta esatta è «5c».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 613", "algebra.txt", "Eseguire la seguente sottrazione tra polinomi: (2ab+3c) - (2ab-2c)")
D("mat-393", "Insiemi", 2, "L'intersezione di due insiemi A e B si indica con:",
  "A ∩ B", ["A U B", "A - B", "B – A"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 641: la risposta esatta è «A ∩ B».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 641", "algebra.txt", "L'intersezione di due insiemi A e B si indica con:")
D("mat-394", "Insiemi", 2, "Dato l'insieme dei numeri naturali quale delle seguenti affermazioni è falsa?",
  "L'insieme dei numeri naturali è un insieme finito", ["L'insieme dei numeri naturali contiene lo 0", "L'insieme dei numeri naturali è un insieme infinito", "L'insieme dei numeri naturali è ordinabile"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 648: la risposta esatta è «L'insieme dei numeri naturali è un insieme finito».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 648", "algebra.txt", "Dato l'insieme dei numeri naturali quale delle seguenti affermazioni è falsa?")
D("mat-395", "Piano cartesiano", 2, "Quale delle seguenti scritture non è corretta?",
  "5 < 15 < 12", ["41 > 30", "10 > 7", "0 < 2"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 655: la risposta esatta è «5 < 15 < 12».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 655", "algebra.txt", "Quale delle seguenti scritture non è corretta?")
D("mat-396", "Insiemi", 2, "L'insieme A è costituito da 8 elementi e l'insieme B da 6 elementi: se A ∩ B = {a, b, c}, quanti sono gli elementi di A U B?",
  "11", ["10", "9", "14"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 662: la risposta esatta è «11».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 662", "algebra.txt", "L'insieme A è costituito da 8 elementi e l'insieme B da 6 elementi: se A ∩ B = {a, b, c}, quanti sono gli elementi di A U B?")
D("mat-397", "Monomi", 2, "Il m.c.m. fra due o più monomi è:",
  "divisibile per tutti i monomi assegnati", ["contenuto in tutti i monomi assegnati", "multiplo solo del monomio di grado minimo", "multiplo del prodotto dei monomi"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 670: la risposta esatta è «divisibile per tutti i monomi assegnati».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 670", "algebra.txt", "Il m.c.m. fra due o più monomi è:")
D("mat-398", "Monomi", 2, "Qual è il prodotto tra questi monomi 5a³b² ∙ (–2)a⁴b³x² =",
  "– 10a⁷b⁵x²", ["10a⁷b⁵x²", "8a⁷b⁵x²", "10 a⁶b⁵x²"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 677: la risposta esatta è «– 10a⁷b⁵x²».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 677", "algebra.txt", "Qual è il prodotto tra questi monomi 5a³b² ∙ (–2)a⁴b³x² =")
D("mat-399", "Disequazioni", 2, "Determinare i valori di k che verificano la disequazione 12 + 3k ≥ k.",
  "k ≥ -6", ["k ≥ 6", "k ≥ -3", "k ≤ -6"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 723: la risposta esatta è «k ≥ -6».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 723", "algebra.txt", "Determinare i valori di k che verificano la disequazione 12 + 3k ≥ k.")
D("mat-400", "Piano cartesiano", 2, "Nel piano cartesiano, le rette di equazioni:Y=2*X+A Y=2*X-3-B con A e B numeri reali:",
  "sono parallele fra loro", ["sono entrambe parallele all'asse delle ascisse (X)", "sono entrambe parallele all'asse delle ordinate (Y)", "sono perpendicolari"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 731: la risposta esatta è «sono parallele fra loro».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 731", "algebra.txt", "Nel piano cartesiano, le rette di equazioni:Y=2*X+A Y=2*X-3-B con A e B numeri reali:")
D("mat-401", "Espressioni", 2, "Calcolare il risultato dell'espressione 125-(45:5)",
  "116", ["129", "611", "161"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 738: la risposta esatta è «116».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 738", "algebra.txt", "Calcolare il risultato dell'espressione 125-(45:5)")
D("mat-402", "Piano cartesiano", 2, "Quali sono le coordinate del punto P' simmetrico di P (5 ; 2), rispetto all'asse x?",
  "P' (5; – 2)", ["P' (– 5; – 2)", "P' (– 5; 2)", "P' (5; 2)"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 746: la risposta esatta è «P' (5; – 2)».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 746", "algebra.txt", "Quali sono le coordinate del punto P' simmetrico di P (5 ; 2), rispetto all'asse x?")
D("mat-403", "Equazioni", 2, "Quale delle seguenti equazioni rappresenta la proporzionalità inversa?",
  "y = 4/x", ["x = 5", "y = 3x", "x + y = k"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 760: la risposta esatta è «y = 4/x».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 760", "algebra.txt", "Quale delle seguenti equazioni rappresenta la proporzionalità inversa?")
D("mat-404", "Insiemi", 2, "Quale numero non appartiene all'insieme A = {x|x è un numero dispari minore di 12}?",
  "13", ["7", "1", "3"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 767: la risposta esatta è «13».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 767", "algebra.txt", "Quale numero non appartiene all'insieme A = {x|x è un numero dispari minore di 12}?")
D("mat-405", "Polinomi", 2, "Quale polinomio si scompone in (a – 2b) (a² + 2ab + 4b²)?",
  "a³ - 8b³", ["a² – 4b²", "a³ – 2b³", "a³ + 8b³"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 781: la risposta esatta è «a³ - 8b³».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 781", "algebra.txt", "Quale polinomio si scompone in (a – 2b) (a² + 2ab + 4b²)?")
D("mat-406", "Polinomi", 2, "Qual è il grado del polinomio 2a² + a³x⁴ + x⁵ + 9 rispetto alla lettera a?",
  "3", ["5", "6", "9"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 788: la risposta esatta è «3».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 788", "algebra.txt", "Qual è il grado del polinomio 2a² + a³x⁴ + x⁵ + 9 rispetto alla lettera a?")
D("mat-407", "MCD e mcm", 2, "Il minimo comune multiplo dei numeri 5, 2 e 10 vale:",
  "10", ["1", "100", "20"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 826: la risposta esatta è «10».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 826", "algebra.txt", "Il minimo comune multiplo dei numeri 5, 2 e 10 vale:")
D("mat-408", "Insiemi", 2, "Dire quale delle seguenti affermazioni equivale a dire che \"due insiemi A e B sono disgiunti\".",
  "L'intersezione tra A e B è vuota.", ["Uno dei due tra A e B è vuoto", "L'unione di A e B dà come risultato A", "A è sottoinsieme di B o viceversa."],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 840: la risposta esatta è «L'intersezione tra A e B è vuota.».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 840", "algebra.txt", "Dire quale delle seguenti affermazioni equivale a dire che \"due insiemi A e B sono disgiunti\".")
D("mat-409", "Insiemi", 2, "Dire se la seguente affermazione è vera: \"se A è vuoto, allora A∩B è vuota\".",
  "Sì", ["No", "Non sempre", "Mai"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 848: la risposta esatta è «Sì».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 848", "algebra.txt", "Dire se la seguente affermazione è vera: \"se A è vuoto, allora A∩B è vuota\".")
D("mat-410", "Equazioni", 2, "Determinare la differenza X\\A, dove X={7, 14, 21, 28, 35, 42, 49, 57} e A={42, 49, 56, 63, 70}.",
  "{7, 14, 21, 28, 35, 57}", ["{7, 14, 21, 28, 35, 42, 49, -1}", "{7, 14, 21, 28, 35, 42, 49, 1}", "{7, 14, 21, 28, 35, 42, 49}"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 857: la risposta esatta è «{7, 14, 21, 28, 35, 57}».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 857", "algebra.txt", "Determinare la differenza X\\A, dove X={7, 14, 21, 28, 35, 42, 49, 57} e A={42, 49, 56, 63, 70}.")
D("mat-411", "Espressioni", 2, "Dati i tre numeri relativi -3, 1, 2, determinare il minimo tra i tre.",
  "-3", ["1", "2", "Non si può decidere."],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 864: la risposta esatta è «-3».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 864", "algebra.txt", "Dati i tre numeri relativi -3, 1, 2, determinare il minimo tra i tre.")
D("mat-412", "MCD e mcm", 2, "Calcolare il MCD(60, 96, 144).",
  "12", ["6", "4", "16"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 871: la risposta esatta è «12».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 871", "algebra.txt", "Calcolare il MCD(60, 96, 144).")
D("mat-413", "Frazioni", 2, "Determinare la frazione che si ottiene riducendo ai minimi termini la frazione 81/900.",
  "9/100.", ["1/100.", "81/100.", "900"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 878: la risposta esatta è «9/100.».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 878", "algebra.txt", "Determinare la frazione che si ottiene riducendo ai minimi termini la frazione 81/900.")
D("mat-414", "Monomi", 2, "Determinare il grado del seguente monomio: x² y³ z⁵.",
  "10", ["5", "Non si può stabilire.", "2"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 892: la risposta esatta è «10».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 892", "algebra.txt", "Determinare il grado del seguente monomio: x² y³ z⁵.")
D("mat-415", "Monomi", 2, "Completare la seguente affermazione: \"la somma di due monomi è un monomio...\"",
  "…solo quando i due addendi sono monomi simili.", ["...in ogni caso.", "...solo quando la x è elevata alla stessa potenza.", "...il cui grado è sempre la somma dei gradi degli addendi."],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 899: la risposta esatta è «…solo quando i due addendi sono monomi simili.».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 899", "algebra.txt", "Completare la seguente affermazione: \"la somma di due monomi è un monomio...\"")
D("mat-416", "Polinomi", 2, "Decidere se l'espressione x⁵ + 7 x⁴ è un polinomio.",
  "Sì", ["No.", "Dipende dal valore di x.", "Non si può stabilire con certezza."],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 906: la risposta esatta è «Sì».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 906", "algebra.txt", "Decidere se l'espressione x⁵ + 7 x⁴ è un polinomio.")
D("mat-417", "Prodotti notevoli", 2, "Sviluppare il seguente quadrato: (-2 x – y)².",
  "4 x² + 4 x y + y²", ["4 x² - 4 x y + y²", "4 x² + 2 x y + y²", "4 x² - 2 x y + y²"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 920: la risposta esatta è «4 x² + 4 x y + y²».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 920", "algebra.txt", "Sviluppare il seguente quadrato: (-2 x – y)².")
D("mat-418", "Monomi", 2, "Calcolare il seguente prodotto: (2 a + b)(2 a – b).",
  "4 a² – b²", ["4 a² + b²", "4 a² – 2 b²", "4 a² – 4 a b + b²"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 927: la risposta esatta è «4 a² – b²».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 927", "algebra.txt", "Calcolare il seguente prodotto: (2 a + b)(2 a – b).")
D("mat-419", "Polinomi", 2, "Determinare il quoziente e il resto della seguente divisione tra polinomi: (a⁷ – 3 a⁶ – 3 a⁵ + 9 a⁴ + 2 a² – 7 a + 3):(a – 3).",
  "Quoziente = a⁶ – 3 a⁴ + 2 a – 1, Resto = 0.", ["Quoziente = a⁶ – 2 a⁴ + 3 a – 1, Resto = 0.", "Quoziente = a⁶ – 3 a⁴ + 2 a – 1, Resto = 42.", "Quoziente = a⁶ – 2 a⁴ + 3 a – 1, Resto = 42."],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 934: la risposta esatta è «Quoziente = a⁶ – 3 a⁴ + 2 a – 1, Resto = 0.».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 934", "algebra.txt", "Determinare il quoziente e il resto della seguente divisione tra polinomi: (a⁷ – 3 a⁶ – 3 a⁵ + 9 a⁴ + 2 a² – 7 a + 3):(a – 3).")
D("mat-420", "Polinomi", 2, "Scomporre in fattori il seguente polinomio: t² – 10 t + 24.",
  "(t – 6) (t – 4)", ["(t – 3) (t – 8)", "(t + 6) (t + 4)", "(t + 12) (t + 2)"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 942: la risposta esatta è «(t – 6) (t – 4)».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 942", "algebra.txt", "Scomporre in fattori il seguente polinomio: t² – 10 t + 24.")
D("mat-421", "Frazioni", 2, "Eseguire la seguente addizione tra frazioni algebriche: a² + b² + [(a⁴ + b⁴)/(a² – b²)].",
  "(2 a⁴)/(a² – b²)", ["0", "(2 b⁴)/(a² – b²)", "(2 a² b²)/(a² – b²)"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 949: la risposta esatta è «(2 a⁴)/(a² – b²)».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 949", "algebra.txt", "Eseguire la seguente addizione tra frazioni algebriche: a² + b² + [(a⁴ + b⁴)/(a² – b²)].")
D("mat-422", "Radicali", 2, "Dire quale delle seguenti espressioni equivale a √24 * √6.",
  "12", ["√30", "144", "√72"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 956: la risposta esatta è «12».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 956", "algebra.txt", "Dire quale delle seguenti espressioni equivale a √24 * √6.")
D("mat-423", "Equazioni", 2, "Risolvere l'equazione 5 x + 6 + 2 x = 3 x + 5 + 4 x.",
  "L'equazione non ammette soluzioni.", ["L'equazione è un'identità.", "x = 11/14", "x = -11/14"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 963: la risposta esatta è «L'equazione non ammette soluzioni.».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 963", "algebra.txt", "Risolvere l'equazione 5 x + 6 + 2 x = 3 x + 5 + 4 x.")
D("mat-424", "Espressioni", 2, "Dato il sistema: 2 x + 4 y = 34; x + 2 y = 0, dire quale delle seguenti affermazioni è vera.",
  "È impossibile.", ["È indeterminato.", "È determinato.", "Non si può decidere."],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 971: la risposta esatta è «È impossibile.».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 971", "algebra.txt", "Dato il sistema: 2 x + 4 y = 34; x + 2 y = 0, dire quale delle seguenti affermazioni è vera.")
D("mat-425", "Disequazioni", 2, "Data la disequazione x > 2, dire quale delle seguenti disequazioni è equivalente alla disequazione data.",
  "-x < -2", ["x < -2", "-x < 2", "-x > -2"],
  "Banca dati ministeriale (1° livello, Algebra), domanda n. 978: la risposta esatta è «-x < -2».",
  "Banca dati ministeriale, 1° livello – Algebra, n. 978", "algebra.txt", "Data la disequazione x > 2, dire quale delle seguenti disequazioni è equivalente alla disequazione data.")

# ── Banca dati ministeriale «1° Livello – Aritmetica» (matematica.pdf): domande riportate così come sono,
#    la risposta esatta è la A) del PDF. Generato con scripts/domande/da_banca_ministeriale.py.
D("mat-426", "Espressioni", 2, "Calcolare il valore della seguente espressione 25 −14 : 2 − 8 + 2 − 40 : 5",
  "4", ["20", "12", "6"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 1: la risposta esatta è «4».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 1", "matematica.txt", "Calcolare il valore della seguente espressione 25 −14 : 2 − 8 + 2 − 40 : 5")
D("mat-427", "Misure", 2, "300 ml a quanti litri corrispondono?",
  "0,3", ["0,003", "3", "0,03"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 11: la risposta esatta è «0,3».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 11", "matematica.txt", "300 ml a quanti litri corrispondono?")
D("mat-428", "Frazioni", 2, "A quale frazione decimale corrisponde il numero decimale 0,032?",
  "32/1000", ["32/100", "32/10", "3/10"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 16: la risposta esatta è «32/1000».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 16", "matematica.txt", "A quale frazione decimale corrisponde il numero decimale 0,032?")
D("mat-429", "Percentuali", 2, "A quanto corrisponde il 20% di 980 ?",
  "196", ["900", "160", "320"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 22: la risposta esatta è «196».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 22", "matematica.txt", "A quanto corrisponde il 20% di 980 ?")
D("mat-430", "Frazioni", 2, "La somma 2/5 + 1/4 vale:",
  "13/20", ["21/54", "3/9", "5/2"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 34: la risposta esatta è «13/20».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 34", "matematica.txt", "La somma 2/5 + 1/4 vale:")
D("mat-431", "Frazioni", 2, "La somma 3/5 + 1/2 è uguale a:",
  "11/10", ["4/7", "31/52", "51/32"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 59: la risposta esatta è «11/10».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 59", "matematica.txt", "La somma 3/5 + 1/2 è uguale a:")
D("mat-432", "Frazioni", 2, "Cosa si ottiene semplificando la frazione 45/65?",
  "9/13", ["15/13", "9/65", "2/3"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 71: la risposta esatta è «9/13».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 71", "matematica.txt", "Cosa si ottiene semplificando la frazione 45/65?")
D("mat-433", "Percentuali", 2, "Il 20% di 300 è uguale a:",
  "60", ["80", "30", "20"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 89: la risposta esatta è «60».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 89", "matematica.txt", "Il 20% di 300 è uguale a:")
D("mat-434", "Percentuali", 2, "Il 5% di 8500 è uguale a:",
  "425", ["4250", "42,5", "85"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 101: la risposta esatta è «425».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 101", "matematica.txt", "Il 5% di 8500 è uguale a:")
D("mat-435", "Percentuali", 2, "Il prezzo di listino di un oggetto è 800 euro. Se ci applicano lo sconto del 5% quanto lo paghiamo ?",
  "760€", ["40€", "700€", "795€"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 113: la risposta esatta è «760€».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 113", "matematica.txt", "Il prezzo di listino di un oggetto è 800 euro. Se ci applicano lo sconto del 5% quanto lo paghiamo ?")
D("mat-436", "Piano cartesiano", 2, "Indicare la soluzione corretta per la seguente espressione: [–2 (–4 + 9 – 7) + 10] : 7",
  "2", ["1", "7", "-2"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 126: la risposta esatta è «2».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 126", "matematica.txt", "Indicare la soluzione corretta per la seguente espressione: [–2 (–4 + 9 – 7) + 10] : 7")
D("mat-437", "Espressioni", 2, "Indicare il numero più grande:",
  "2,5", ["1,9", "0,2", "2,4"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 132: la risposta esatta è «2,5».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 132", "matematica.txt", "Indicare il numero più grande:")
D("mat-438", "Statistica", 2, "Qual è la media tra i numeri 8, 79, 83 e 52 ?",
  "55,5", ["72,25", "45,5", "58,75"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 150: la risposta esatta è «55,5».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 150", "matematica.txt", "Qual è la media tra i numeri 8, 79, 83 e 52 ?")
D("mat-439", "Potenze", 2, "6² + 5 – 8 =",
  "33", ["12", "24", "36"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 162: la risposta esatta è «33».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 162", "matematica.txt", "6² + 5 – 8 =")
D("mat-440", "Monomi", 2, "Qual è il numero che moltiplicato per 5 va sottratto a 3885 per ottenere 300?",
  "717", ["153", "1183", "890"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 186: la risposta esatta è «717».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 186", "matematica.txt", "Qual è il numero che moltiplicato per 5 va sottratto a 3885 per ottenere 300?")
D("mat-441", "Frazioni", 2, "(3/6) : (10/5) =",
  "1/4", ["-3/2", "5/2", "2/2"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 192: la risposta esatta è «1/4».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 192", "matematica.txt", "(3/6) : (10/5) =")
D("mat-442", "Frazioni", 2, "(3/8) + (6/7) =",
  "69/56", ["-27/56", "9/28", "7/16"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 198: la risposta esatta è «69/56».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 198", "matematica.txt", "(3/8) + (6/7) =")
D("mat-443", "Frazioni", 2, "(6/8) + (7/2) =",
  "17/4", ["3/14", "-11/4", "21/8"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 204: la risposta esatta è «17/4».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 204", "matematica.txt", "(6/8) + (7/2) =")
D("mat-444", "Frazioni", 2, "(8/6) + (8/10) =",
  "32/15", ["5/3", "16/15", "8/15"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 210: la risposta esatta è «32/15».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 210", "matematica.txt", "(8/6) + (8/10) =")
D("mat-445", "Frazioni", 2, "(7/8) + (1/10) =",
  "39/40", ["7/80", "35/4", "31/40"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 216: la risposta esatta è «39/40».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 216", "matematica.txt", "(7/8) + (1/10) =")
D("mat-446", "Espressioni", 2, "Quale dei seguenti numeri è il più grande?",
  "12/11", ["15/14", "13/12", "9/10"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 240: la risposta esatta è «12/11».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 240", "matematica.txt", "Quale dei seguenti numeri è il più grande?")
D("mat-447", "Percentuali", 2, "Il 32% di 5200 è uguale a:",
  "1664", ["2600", "166,4", "450"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 258: la risposta esatta è «1664».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 258", "matematica.txt", "Il 32% di 5200 è uguale a:")
D("mat-448", "Percentuali", 2, "Il 210% di 580 è uguale a:",
  "1218", ["1341", "6120", "1485"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 264: la risposta esatta è «1218».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 264", "matematica.txt", "Il 210% di 580 è uguale a:")
D("mat-449", "Numeri primi", 2, "Quale tra i seguenti è un numero primo?",
  "41", ["49", "45", "44"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 270: la risposta esatta è «41».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 270", "matematica.txt", "Quale tra i seguenti è un numero primo?")
D("mat-450", "Frazioni", 2, "Quale tra le seguenti è una frazione apparente?",
  "76/4", ["57/7", "62/3", "81/7"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 306: la risposta esatta è «76/4».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 306", "matematica.txt", "Quale tra le seguenti è una frazione apparente?")
D("mat-451", "Frazioni", 2, "Tra le frazioni seguenti quale è minore di 1?",
  "3/4", ["8/3", "3/2", "7/5"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 342: la risposta esatta è «3/4».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 342", "matematica.txt", "Tra le frazioni seguenti quale è minore di 1?")
D("mat-452", "Espressioni", 2, "La somma dei numeri 1,42 e 0,091 da come risultato:",
  "1,511", ["1,4921", "1,611", "1,5011"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 354: la risposta esatta è «1,511».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 354", "matematica.txt", "La somma dei numeri 1,42 e 0,091 da come risultato:")
D("mat-453", "Frazioni", 2, "(4/3)+(2/7) è pari a:",
  "34/21", ["36/21", "6/21", "6/10"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 360: la risposta esatta è «34/21».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 360", "matematica.txt", "(4/3)+(2/7) è pari a:")
D("mat-454", "Insiemi", 2, "Gianfranco, Daniele e Gianluca comprano insieme 12 Kg di funghi, spendendo rispettivamente 20 euro, 24 euro e 36 euro. Se la distribuzione dei funghi avviene in proporzione alla cifra versata, qual è la quantità che spetta a Daniele?",
  "3,6 Kg", ["1,8 Kg", "3 Kg", "5,4 Kg"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 366: la risposta esatta è «3,6 Kg».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 366", "matematica.txt", "Gianfranco, Daniele e Gianluca comprano insieme 12 Kg di funghi, spendendo rispettivamente 20 euro, 24 euro e 36 euro. Se la distribuzione dei funghi avviene in proporzione alla cifra versata, qual è la quantità che spetta a Daniele?")
D("mat-455", "Numeri relativi", 2, "Calcolare il risultato della seguente addizione: (+31) + (+104)",
  "+135", ["+134", "+73", "+136"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 372: la risposta esatta è «+135».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 372", "matematica.txt", "Calcolare il risultato della seguente addizione: (+31) + (+104)")
D("mat-456", "Numeri relativi", 2, "Qual è la soluzione della seguente sottrazione: (-97) - (-56)",
  "-41", ["-40", "+153", "+41"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 384: la risposta esatta è «-41».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 384", "matematica.txt", "Qual è la soluzione della seguente sottrazione: (-97) - (-56)")
D("mat-457", "Frazioni", 2, "Trovare il risultato della seguente addizione frazionaria: (+1/5) + (+1/2)",
  "7/10", ["1/5", "2/5", "2/7"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 390: la risposta esatta è «7/10».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 390", "matematica.txt", "Trovare il risultato della seguente addizione frazionaria: (+1/5) + (+1/2)")
D("mat-458", "Numeri relativi", 2, "Trovare la soluzione della seguente addizione con più addendi: (-6) + (+3) + (-7)",
  "-10", ["10", "-2", "2"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 402: la risposta esatta è «-10».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 402", "matematica.txt", "Trovare la soluzione della seguente addizione con più addendi: (-6) + (+3) + (-7)")
D("mat-459", "Frazioni", 2, "Eseguire la seguente addizione frazionaria con più addendi: (+1/5)+(-3/10)+(5/4)+(-1/2)",
  "+13/20", ["+13/10", "+2/21", "+13/21"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 426: la risposta esatta è «+13/20».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 426", "matematica.txt", "Eseguire la seguente addizione frazionaria con più addendi: (+1/5)+(-3/10)+(5/4)+(-1/2)")
D("mat-460", "Espressioni", 2, "18 + 14 + 15 - 20 - 10 =",
  "17", ["11", "12", "13"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 606: la risposta esatta è «17».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 606", "matematica.txt", "18 + 14 + 15 - 20 - 10 =")
D("mat-461", "Statistica", 2, "Arrotondando al centesimo il numero 19,54604 si ottiene:",
  "19,55", ["19,5", "19,54", "19,6"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 613: la risposta esatta è «19,55».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 613", "matematica.txt", "Arrotondando al centesimo il numero 19,54604 si ottiene:")
D("mat-462", "Espressioni", 2, "Qual è il risultato corretto?",
  "68 : 1 = 68", ["68 : 0 = 68", "1 : 68 = 1", "2 : 68 = 0"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 625: la risposta esatta è «68 : 1 = 68».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 625", "matematica.txt", "Qual è il risultato corretto?")
D("mat-463", "Monomi", 2, "Per ottenere 2458 va aggiunta a 1541 la coppia di numeri…",
  "585; 332", ["773; 70", "457; 231", "64; 582"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 639: la risposta esatta è «585; 332».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 639", "matematica.txt", "Per ottenere 2458 va aggiunta a 1541 la coppia di numeri…")
D("mat-464", "Frazioni", 2, "9/3 – 3/7 =",
  "18/7", ["24/7", "9/7", "7/1"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 645: la risposta esatta è «18/7».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 645", "matematica.txt", "9/3 – 3/7 =")
D("mat-465", "Frazioni", 2, "9/3 + 7/9 =",
  "34/9", ["20/9", "27/7", "7/3"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 651: la risposta esatta è «34/9».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 651", "matematica.txt", "9/3 + 7/9 =")
D("mat-466", "Frazioni", 2, "9/2 – 8/4 =",
  "5/2", ["9/4", "9/1", "13/2"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 657: la risposta esatta è «5/2».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 657", "matematica.txt", "9/2 – 8/4 =")
D("mat-467", "Frazioni", 2, "4/2 – 8/5 =",
  "2/5", ["16/5", "5/4", "18/5"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 675: la risposta esatta è «2/5».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 675", "matematica.txt", "4/2 – 8/5 =")
D("mat-468", "Frazioni", 2, "7/10 + 10/7 =",
  "149/70", ["49/100", "1/1", "- 51/70"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 693: la risposta esatta è «149/70».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 693", "matematica.txt", "7/10 + 10/7 =")
D("mat-469", "Frazioni", 2, "9/7 – 2/4 =",
  "11/14", ["9/14", "25/14", "18/7"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 699: la risposta esatta è «11/14».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 699", "matematica.txt", "9/7 – 2/4 =")
D("mat-470", "Frazioni", 2, "6/4 + 10/6 =",
  "19/6", ["5/2", "9/10", "- 1/6"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 711: la risposta esatta è «19/6».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 711", "matematica.txt", "6/4 + 10/6 =")
D("mat-471", "Espressioni", 2, "65000 è il quadruplo di…",
  "16250", ["15200", "15550", "16500"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 717: la risposta esatta è «16250».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 717", "matematica.txt", "65000 è il quadruplo di…")
D("mat-472", "Espressioni", 2, "Quale delle seguenti terne di numeri contiene solo elementi divisibili per 7?",
  "56; 105;133", ["77; 114; 128", "86; 92; 118", "56; 92;128"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 723: la risposta esatta è «56; 105;133».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 723", "matematica.txt", "Quale delle seguenti terne di numeri contiene solo elementi divisibili per 7?")
D("mat-473", "Espressioni", 2, "81 è il triplo di…",
  "27", ["23", "37", "33"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 729: la risposta esatta è «27».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 729", "matematica.txt", "81 è il triplo di…")
D("mat-474", "Espressioni", 2, "141 e 245 sono rispettivamente il triplo e il quintuplo di…",
  "47; 49", ["37; 47", "39; 41", "33; 43"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 735: la risposta esatta è «47; 49».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 735", "matematica.txt", "141 e 245 sono rispettivamente il triplo e il quintuplo di…")
D("mat-475", "Frazioni", 2, "10/8 – 8/9 =",
  "13/36", ["10/9", "45/32", "77/36"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 742: la risposta esatta è «13/36».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 742", "matematica.txt", "10/8 – 8/9 =")
D("mat-476", "Frazioni", 2, "7/2 : 5/1 =",
  "7/10", ["17/2", "35/2", "- 3/2"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 749: la risposta esatta è «7/10».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 749", "matematica.txt", "7/2 : 5/1 =")
D("mat-477", "Piano cartesiano", 2, "Il giorno 07/11/17 Luigi riceve un assegno postdatato a 120 giorni. Da che giorno potrà Luigi incassare l'assegno?",
  "7/3/18", ["9/3/18", "6/3/18", "5/3/18"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 761: la risposta esatta è «7/3/18».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 761", "matematica.txt", "Il giorno 07/11/17 Luigi riceve un assegno postdatato a 120 giorni. Da che giorno potrà Luigi incassare l'assegno?")
D("mat-478", "Espressioni", 2, "Semplifica la seguente espressione 122*6:8 +2",
  "93,5", ["115", "106,5", "87,5"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 768: la risposta esatta è «93,5».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 768", "matematica.txt", "Semplifica la seguente espressione 122*6:8 +2")
D("mat-479", "Monomi", 2, "Per ottenere 456 quali due numeri vanno sommati a 111",
  "167;178", ["115;115", "171;256", "13;440"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 774: la risposta esatta è «167;178».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 774", "matematica.txt", "Per ottenere 456 quali due numeri vanno sommati a 111")
D("mat-480", "Geometria", 2, "625 è il quadrato di quale numero?",
  "25", ["28", "15", "26"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 781: la risposta esatta è «25».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 781", "matematica.txt", "625 è il quadrato di quale numero?")
D("mat-481", "Monomi", 2, "La zia Giulia, stanca della vecchia lavatrice, ne compra una nuova da 738,00 euro. Versa subito 138 euro e il resto lo pagherà in 4 comode rate trimestrali. A quando corrisponde la rata trimestrale?",
  "150 euro", ["100 euro", "125 euro", "175 euro"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 787: la risposta esatta è «150 euro».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 787", "matematica.txt", "La zia Giulia, stanca della vecchia lavatrice, ne compra una nuova da 738,00 euro. Versa subito 138 euro e il resto lo pagherà in 4 comode rate trimestrali. A quando corrisponde la rata trimestrale?")
D("mat-482", "Proporzioni", 2, "Risolvere la seguente proporzione: 9:84=21:x",
  "196", ["36", "2,25", "50"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 793: la risposta esatta è «196».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 793", "matematica.txt", "Risolvere la seguente proporzione: 9:84=21:x")
D("mat-483", "Potenze", 2, "Applica le proprietà delle potenze per risolvere la seguente espressione 5¹¹ * 5³ : 25²",
  "5¹⁰", ["5¹²", "5⁶", "25⁴"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 803: la risposta esatta è «5¹⁰».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 803", "matematica.txt", "Applica le proprietà delle potenze per risolvere la seguente espressione 5¹¹ * 5³ : 25²")
D("mat-484", "Numeri primi", 2, "Quale delle seguenti terne di numeri non contiene soltanto numeri primi",
  "1;6;7", ["3;5;7", "13;11;19", "7;29"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 809: la risposta esatta è «1;6;7».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 809", "matematica.txt", "Quale delle seguenti terne di numeri non contiene soltanto numeri primi")
D("mat-485", "Piano cartesiano", 2, "Una classe è formata da 28 alunni. I 4/7 vanno a scuola in bicicletta. Quanti alunni raggiungono la scuola con altri mezzi?",
  "12", ["15", "16", "8"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 821: la risposta esatta è «12».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 821", "matematica.txt", "Una classe è formata da 28 alunni. I 4/7 vanno a scuola in bicicletta. Quanti alunni raggiungono la scuola con altri mezzi?")
D("mat-486", "MCD e mcm", 2, "Quale delle seguenti coppie è formata da tutti multipli di 16",
  "112; 176", ["89; 65", "35; 156", "18; 90"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 833: la risposta esatta è «112; 176».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 833", "matematica.txt", "Quale delle seguenti coppie è formata da tutti multipli di 16")
D("mat-487", "Statistica", 2, "Cosa si ottiene arrotondando il seguente numero al millesimo 366,266858",
  "366,267", ["366,266", "366,27", "366,265"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 851: la risposta esatta è «366,267».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 851", "matematica.txt", "Cosa si ottiene arrotondando il seguente numero al millesimo 366,266858")
D("mat-488", "MCD e mcm", 2, "Calcola il minimo comune multiplo dei seguenti numeri: 9,4,7",
  "252", ["63", "36", "28"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 863: la risposta esatta è «252».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 863", "matematica.txt", "Calcola il minimo comune multiplo dei seguenti numeri: 9,4,7")
D("mat-489", "Espressioni", 2, "Indicare tra le seguenti quale disuguaglianza è quella vera:",
  "5 > – 20", ["– 5 < – 20", "15 < – 15", "5 < – 20"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 875: la risposta esatta è «5 > – 20».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 875", "matematica.txt", "Indicare tra le seguenti quale disuguaglianza è quella vera:")
D("mat-490", "Polinomi", 2, "Dato il polinomio 4a² + 2b²+ 2a² – 5b² + a² qual è la riduzione in forma normale?",
  "7a² – 3b²", ["7a² + 3b²", "7a² – 2b²", "5a² – b²"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 881: la risposta esatta è «7a² – 3b²».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 881", "matematica.txt", "Dato il polinomio 4a² + 2b²+ 2a² – 5b² + a² qual è la riduzione in forma normale?")
D("mat-491", "Insiemi", 2, "Dato l'insieme A = {x|x è un numero pari minore 8} indicare quale dei seguenti numeri non gli appartiene:",
  "12", ["6", "4", "2"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 887: la risposta esatta è «12».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 887", "matematica.txt", "Dato l'insieme A = {x|x è un numero pari minore 8} indicare quale dei seguenti numeri non gli appartiene:")
D("mat-492", "Espressioni", 2, "Indicare qual è la relazione errata:",
  "5 < 13 < 12", ["44 > 32", "11 > 8", "0 < 6"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 899: la risposta esatta è «5 < 13 < 12».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 899", "matematica.txt", "Indicare qual è la relazione errata:")
D("mat-493", "Insiemi", 2, "L'insieme A è costituito da 8 elementi e l'insieme B da 5 elementi: sapendo che la loro intersezione è data da A ∩ B = {a, b, c}, allora gli elementi di A U B sono:",
  "10", ["3", "5", "13"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 905: la risposta esatta è «10».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 905", "matematica.txt", "L'insieme A è costituito da 8 elementi e l'insieme B da 5 elementi: sapendo che la loro intersezione è data da A ∩ B = {a, b, c}, allora gli elementi di A U B sono:")
D("mat-494", "Insiemi", 2, "Siano dati due insiemi A e B. Sapendo che A è costituito da 8 elementi e B da 2 elementi, indicare quanti sono gli elementi dell'insieme A xB",
  "16", ["6", "10", "4"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 911: la risposta esatta è «16».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 911", "matematica.txt", "Siano dati due insiemi A e B. Sapendo che A è costituito da 8 elementi e B da 2 elementi, indicare quanti sono gli elementi dell'insieme A xB")
D("mat-495", "Monomi", 2, "Moltiplicando due monomi qualunque si ottiene sempre:",
  "un monomio di grado uguale alla somma dei gradi dei monomi che si moltiplicano", ["un monomio simile ai monomi che si moltiplicano", "un monomio di grado uguale al prodotto dei gradi dei monomi che si moltiplicano", "un polinomio"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 919: la risposta esatta è «un monomio di grado uguale alla somma dei gradi dei monomi che si moltiplicano».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 919", "matematica.txt", "Moltiplicando due monomi qualunque si ottiene sempre:")
D("mat-496", "Monomi", 2, "Indicare quali tra questi non è un monomio:",
  "15b + 317", ["3b", "8a²b", "– 4axy³"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 925: la risposta esatta è «15b + 317».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 925", "matematica.txt", "Indicare quali tra questi non è un monomio:")
D("mat-497", "Equazioni", 2, "Per quale valore di x è verificata la seguente equazione 4(x - 1) = 2x - 6?",
  "x = -1", ["x = 13", "x = 1", "x = -8"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 940: la risposta esatta è «x = -1».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 940", "matematica.txt", "Per quale valore di x è verificata la seguente equazione 4(x - 1) = 2x - 6?")
D("mat-498", "Equazioni", 2, "La soluzione dell'equazione 3x + 3 = 2x è:",
  "x = -3", ["x = 8", "x = 3", "x = -4"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 946: la risposta esatta è «x = -3».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 946", "matematica.txt", "La soluzione dell'equazione 3x + 3 = 2x è:")
D("mat-499", "Espressioni", 2, "Calcola il valore dell'espressione: 12 + 9 : 3 * 2",
  "18", ["14", "21/6", "30"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 953: la risposta esatta è «18».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 953", "matematica.txt", "Calcola il valore dell'espressione: 12 + 9 : 3 * 2")
D("mat-500", "Equazioni", 2, "Calcola il valore di x che verifica l'equazione 29x+31=727",
  "x=24", ["x=-24", "x=667", "x=-667"],
  "Banca dati ministeriale (1° livello, Aritmetica), domanda n. 959: la risposta esatta è «x=24».",
  "Banca dati ministeriale, 1° livello – Aritmetica, n. 959", "matematica.txt", "Calcola il valore di x che verifica l'equazione 29x+31=727")
