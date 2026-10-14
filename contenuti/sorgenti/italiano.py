# Italiano — fonti: voci di Wikipedia «Ortografia italiana», «Grammatica italiana», «Punteggiatura» (CC BY-SA 4.0), solo per le regole.
ORT = "Wikipedia_Ortografia-italiana.txt"
GRA = "Wikipedia_Grammatica-italiana.txt"
W = lambda voce: f"Wikipedia, «{voce}» (CC BY-SA 4.0)"

D("ita-001", "Ortografia", 1, "Quale grafia è corretta?",
  "qual è", ["qual'è", "quale'è", "qualè"],
  "«Qual» è un troncamento, non un'elisione: non vuole l'apostrofo. Lo stesso vale per «tal è».",
  W("Ortografia italiana"), ORT, "la grafia corretta è sempre qual è e tal è")

D("ita-002", "Ortografia", 2, "Quale grafia è corretta?",
  "pover'uomo", ["pover uomo", "pove'r uomo", "poveruomo"],
  "In «pover'uomo» c'è elisione: l'apostrofo è obbligatorio.",
  W("Ortografia italiana"), ORT, "la grafia corretta è pover'uomo")

D("ita-003", "Ortografia", 2, "In quale fenomeno l'uso dell'apostrofo è sempre obbligatorio?",
  "Nell'elisione", ["Nel troncamento", "Nell'aferesi", "Nella sincope"],
  "Con l'elisione l'apostrofo è obbligatorio; nel troncamento e nell'aferesi solo in alcuni casi.",
  W("Ortografia italiana"), ORT, "con l'elisione l'uso dell'apostrofo è obbligatorio")

D("ita-004", "Ortografia", 2, "Perché si scrive «un'artista» con l'apostrofo e «un artista» senza?",
  "Con l'apostrofo indica una donna (elisione di «una»), senza un uomo", ["Sono due grafie equivalenti", "«Un'artista» è un errore", "Dipende solo dalla parola che segue"],
  "L'apostrofo distingue l'elisione di «una» (femminile) dal troncamento di «uno» (maschile).",
  W("Ortografia italiana"), ORT, "si pensi al caso di un artista maschile e un'artista femminile")

D("ita-005", "Ortografia", 1, "Perché il verbo avere si scrive con la «h» in «ho, hai, ha, hanno»?",
  "Per distinguerlo da o, ai, a, anno", ["Per ragioni di pronuncia aspirata", "Per indicare l'accento", "È un residuo senza alcuna funzione"],
  "La h distingue le voci del verbo avere dalla congiunzione o, dalla preposizione ai e a, dal sostantivo anno.",
  W("Ortografia italiana"), ORT, "per distinguerle da: o (congiunzione), ai (preposizione articolata), a (preposizione semplice), anno (sostantivo)")

D("ita-006", "Ortografia", 3, "In quali parole il grado intensivo di «qu» si scrive con «qqu» invece che con «cqu»?",
  "Solo in soqquadro, beqquadro (biqquadro) e derivati", ["In tutte le parole che iniziano con «acqu-»", "In nessuna parola italiana", "In tutti i verbi in -quare"],
  "Il grado intensivo si scrive normalmente «cqu» (acqua, nacque); «qqu» solo in soqquadro, beqquadro e derivati.",
  W("Ortografia italiana"), ORT, "solo nelle parole soqquadro, beqquadro")

D("ita-007", "Ortografia", 3, "Quale plurale è corretto?",
  "le valigie", ["le valige", "le valiggie", "le valigge"],
  "Le parole in -cia e -gia atone mantengono la i al plurale se precedute da vocale (valigie, camicie), la perdono se precedute da consonante (arance, piogge).",
  W("Ortografia italiana"), ORT, "fanno il plurale in -cie e -gie se sono precedute da una lettera vocalica")

D("ita-008", "Ortografia", 3, "Quale plurale è corretto?",
  "le arance", ["le arancie", "le aranci", "le arancee"],
  "Se -cia è preceduto da consonante, al plurale la i cade: arancia → arance, pioggia → piogge.",
  W("Ortografia italiana"), ORT, "altrimenti perdono la I")

D("ita-009", "Ortografia", 2, "Quale accento segna le vocali dal timbro più chiuso, come in «perché»?",
  "L'accento acuto", ["L'accento grave", "L'accento circonflesso", "La dieresi"],
  "L'accento acuto segnala i suoni più chiusi (é, ó); il grave i suoni più aperti (à, è, ò). Si scrive quindi perché, poiché, affinché.",
  W("Ortografia italiana"), ORT, "accento acuto ( ́) che segnala i suoni vocalici più chiusi")

D("ita-010", "Ortografia", 2, "Su quali vocali si usa l'accento grave?",
  "Sui suoni più aperti (à, è, ò) e normalmente anche su ì e ù", ["Solo sulle vocali chiuse é e ó", "Solo sulla î", "Su nessuna vocale nella scrittura moderna"],
  "L'accento grave segna i suoni più aperti à, è, ò e si usa di norma anche su ì e ù.",
  W("Ortografia italiana"), ORT, "accento grave (`) presente sui suoni vocalici più aperti")

D("ita-011", "Ortografia", 2, "Quale grafia è corretta?",
  "cuore", ["quore", "cquore", "qore"],
  "Cuore si scrive con c; la q è sempre seguita da u più un'altra vocale (qua, que, qui, quo), ma non tutte le parole con questo suono si scrivono con q.",
  W("Ortografia italiana"), ORT, "batticuore, crepacuore")

D("ita-012", "Ortografia", 4, "La lettera «q» in italiano è sempre seguita da:",
  "u semiconsonantica più un'altra vocale", ["una consonante doppia", "una vocale qualsiasi senza u", "la lettera h"],
  "La q compare solo nei nessi qua, que, qui, quo, con valore /kw/.",
  W("Ortografia italiana"), ORT, "è sempre seguita da ⟨u⟩ (semiconsonantica) più altra vocale")

D("ita-013", "Morfologia", 2, "Quali sono i modi del verbo italiano?",
  "Indicativo, congiuntivo, condizionale, imperativo, infinito, gerundio e participio",
  ["Indicativo, congiuntivo e imperativo", "Presente, passato e futuro", "Attivo, passivo e riflessivo"],
  "I verbi si flettono per modo: indicativo, congiuntivo, condizionale, imperativo (finiti) e infinito, gerundio, participio (indefiniti). Presente, passato e futuro sono tempi.",
  W("Grammatica italiana"), GRA, "per modo (indicativo, congiuntivo, condizionale, imperativo, infinito, gerundio e participio)")

D("ita-014", "Morfologia", 2, "Come si distinguono le parole in grammatica rispetto alla flessione?",
  "In variabili (soggette a flessione) e invariabili", ["In semplici e composte", "In primitive e derivate", "In proprie e comuni"],
  "Le parole variabili cambiano forma (desinenza) secondo genere, numero, persona; le invariabili, come avverbi e preposizioni, no.",
  W("Grammatica italiana"), GRA, "variabili (cioè soggette a flessione) e invariabili")

D("ita-015", "Morfologia", 3, "Quale articolo indeterminativo si usa davanti a «iena»?",
  "una", ["un'", "uno", "un"],
  "«Un'» si usa davanti a vocale, ma non davanti a i semiconsonantica: quindi «una iena».",
  W("Grammatica italiana"), GRA, "non davanti a i semiconsonantica - esempio: una iena")

D("ita-016", "Sintassi", 3, "Che cos'è un «periodo» nell'analisi della frase?",
  "Una frase complessa in cui ci sono due o più predicati", ["Una frase con un solo predicato", "Un gruppo di parole senza verbo", "Il soggetto con i suoi complementi"],
  "Il periodo è una frase complessa con due o più predicati; l'analisi logica studia la frase, l'analisi del periodo il rapporto tra le proposizioni.",
  W("Grammatica italiana"), GRA, "periodo è una frase complessa, in cui si presentano due o più predicati")

D("ita-017", "Sintassi", 2, "Che cosa individua l'analisi logica?",
  "Le categorie sintattiche che costituiscono la frase (soggetto, predicato, complementi)", ["Le parti del discorso di ogni parola", "Il numero di sillabe", "L'origine etimologica delle parole"],
  "L'analisi grammaticale ha per oggetto le parole; l'analisi logica le funzioni sintattiche nella frase.",
  W("Grammatica italiana"), GRA, "l'analisi logica individua le categorie sintattiche che costituiscono la frase")

D("ita-018", "Ortografia", 5, "In una circolare si legge: «Qual'è il termine? Un pò di pazienza, il modulo va compilato un'altra volta». Quanti errori di ortografia contiene?",
  "Due: «qual'è» e «pò»", ["Nessuno", "Uno: solo «qual'è»", "Tre: «qual'è», «pò» e «un'altra»"],
  "Si scrive «qual è» (troncamento, senza apostrofo) e «un po'» (apocope, con apostrofo). «Un'altra» è corretto: elisione di «una».",
  W("Ortografia italiana"), ORT, "come \"qual'è\" o tal'è")


# --- Blocco 2: ortografia (voce «Ortografia italiana») ---
def O(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Ortografia italiana"), ORT, frase)

O("ita-019", "Ortografia", 2, "Quanti grafemi conta l'alfabeto italiano propriamente detto (senza le lettere straniere)?",
  "21", ["26", "24", "19"],
  "A questi si aggiungono 5 lettere «straniere»: j, k, w, x, y.",
  "usa 21 grafemi dell'alfabeto propriamente detto italiano")

O("ita-020", "Ortografia", 2, "Quali sono le lettere considerate «straniere» nell'alfabeto italiano?",
  "j, k, w, x, y", ["h, q, z, x, y", "b, d, g, k, w", "a, e, i, o, u"],
  "Sono usate soprattutto per parole di origine straniera.",
  "Vengono considerate lettere straniere i grafemi j, k, w, x e y")

O("ita-021", "Ortografia", 3, "Quali sono i trigrammi dell'italiano?",
  "gli e sci", ["ch e gh", "gn e sc", "qu e cq"],
  "I digrammi sono ch, ci, gh, gi, gl, gn, sc.",
  "2 trigrammi: ⟨gli⟩, ⟨sci⟩")

O("ita-022", "Ortografia", 2, "Che funzione ha la lettera «h» nei gruppi «ch» e «gh»?",
  "Indica il suono duro di c e g davanti a e e i", ["Rende aspirato il suono", "Indica una vocale lunga", "Non ha alcuna funzione"],
  "In italiano la h è muta: ha funzioni diacritiche e distintive.",
  "come segno nei digrammi ch- e gh- per indicare C e G dura")

O("ita-023", "Ortografia", 2, "Perché «hanno» (verbo avere) si scrive con la h?",
  "Per distinguerlo dal sostantivo «anno»", ["Perché si pronuncia aspirato", "Per una regola di accentazione", "Perché deriva dal greco"],
  "Allo stesso modo ho/o, hai/ai, ha/a.",
  "per distinguerle da: o (congiunzione), ai (preposizione articolata), a (preposizione semplice), anno (sostantivo)")

O("ita-024", "Ortografia", 3, "Quale grafia è corretta davanti a una parola che inizia per «i»?",
  "gl'italiani", ["begl'occhi", "gl'amici", "gl'uomini"],
  "L'elisione di «gli» è ammessa solo davanti a i-; davanti ad altre vocali si scrive per intero (begli occhi, gli amici).",
  "l'elisione grafica è possibile solo con i-: gl'italiani")

O("ita-025", "Ortografia", 3, "Quale di queste grafie è errata?",
  "c'ha (per «ci ha»)", ["c'è", "anch'io", "poc'anzi"],
  "«c'ha» e «c'offrì» sono considerate errate: si scrive «ci ha», «ci offrì».",
  "Sono invece da considerarsi errate grafie come: *c'ha, *c'offrì")

O("ita-026", "Ortografia", 3, "Quale grafia è corretta?",
  "anch'io", ["anc'io", "anchio", "anch io"],
  "Davanti a e- o i- la h è obbligatoria: anch'io, anch'egli.",
  "l'-h è obbligatoria davanti a parole che iniziano per e- o i-: anch'io, anch'egli")

O("ita-027", "Ortografia", 3, "Qual è il plurale corretto di «arancia»?",
  "arance", ["arancie", "aranci", "arancee"],
  "Le parole in -cia/-gia atone perdono la i al plurale se la c/g è preceduta da consonante (arance, piogge), la mantengono se preceduta da vocale (camicie, valigie).",
  "Le parole femminili in -cia e gia atone fanno il plurale in -cie e -gie se sono precedute da una lettera vocalica")

O("ita-028", "Ortografia", 3, "Qual è il plurale corretto di «valigia»?",
  "valigie", ["valige", "valigi", "valigee"],
  "Prima di -gia c'è una vocale (i), quindi la i si mantiene al plurale.",
  "fanno il plurale in -cie e -gie se sono precedute da una lettera vocalica")

O("ita-029", "Ortografia", 3, "Quale di queste parole si scrive con la «i» dopo la c?",
  "sufficiente", ["beneficente", "conoscente", "magnificente"],
  "La i è etimologica nelle parole da -cientis (sufficiente, efficiente, cosciente); non c'è in beneficente, conoscente, magnificente.",
  "NB: si scrivono senza i: beneficente/enza, conoscente/enza, magnificente/enza")

O("ita-030", "Ortografia", 3, "Quale grafia è corretta?",
  "superficie", ["superfice", "superfece", "superfige"],
  "La i è etimologica (dal latino superficies), come in effigie e specie.",
  "effigie, specie, superficie")

O("ita-031", "Ortografia", 3, "Quale grafia è oggi corretta?",
  "passeggero", ["passeggiero", "pasegero", "passegiero"],
  "Le forme in -ggiero (passeggiero, messaggiero, leggiero) sono antiquate.",
  "passeggiero > passeggero")

O("ita-032", "Ortografia", 3, "Come si scrive correttamente?",
  "ingegnere", ["ingegniere", "inggegnere", "ingeniere"],
  "Si scrive senza i, anche se deriva dal suffisso -(i)ere.",
  "NB: si scrive senza i ingegnere")

O("ita-033", "Ortografia", 3, "Quale grafia è corretta?",
  "cielo", ["celo (nel senso di firmamento)", "cello", "ciello"],
  "Cieco e cielo mantengono la i (residuo di -ae- latino); «celo» è voce del verbo celare.",
  "ceco (abitante della Rep. Ceca) e celo (voce del verbo celare)")

O("ita-034", "Ortografia", 2, "Davanti a b e p, quale lettera si usa di regola per la nasale?",
  "La m", ["La n", "La gn", "Si raddoppia la consonante"],
  "Esempio: campo, bambino; fanno eccezione pochi composti come panpepato e benpensante.",
  "è sempre pronunciata /m/")

O("ita-035", "Ortografia", 2, "Quale grafia è corretta?",
  "acqua", ["aqua", "accqua", "aqqua"],
  "Il grado intensivo di qu si scrive -cqu-.",
  "si usa il nesso -cq(u)- (/kk(w)/): acqua")

O("ita-036", "Ortografia", 3, "Quale parola si scrive con la «c» e non con la «q»?",
  "cuore", ["quota", "questo", "quindi"],
  "Scuola, cuore, cuoco, cuoio derivano dalla dittongazione di -ŏ- latina e si scrivono con c.",
  "scuola, cuore, capocuoco")

O("ita-037", "Ortografia", 4, "Quale parola si scrive con -cqui?",
  "piacqui", ["taqui", "naqui", "giaqqui"],
  "«Piacqui» viene dal latino PLACŬI.",
  "Si scrive con -cqui anche piacqui dal latino PLACŬI")

O("ita-038", "Ortografia", 3, "Qual è l'unica parola italiana con -cc- prima di u + vocale?",
  "taccuino", ["acquisto", "eccuo", "sacculo"],
  "Taccuino si scrive con -cc- e non con -cq-.",
  "unica parola con -cc- prima di u")

O("ita-039", "Ortografia", 2, "Quale accento grafico si usa sulla «a» finale (es. carità)?",
  "Solo l'accento grave", ["Solo l'accento acuto", "Il circonflesso", "Nessun accento"],
  "Sulla a si usa solo il grave.",
  "Sulla a si usa invece solo l'accento grave, à (come in carità)")

O("ita-040", "Ortografia", 2, "Quale accento richiede «perché»?",
  "L'accento acuto (é), perché la e è chiusa", ["L'accento grave (è)", "Nessun accento", "Il circonflesso"],
  "Su e e o si usa l'acuto per le vocali chiuse, il grave per quelle aperte (cioè).",
  "richiede di usare l'acuto se la vocale è chiusa (come in perché)")

O("ita-041", "Ortografia", 2, "Quale di questi monosillabi NON vuole mai l'accento?",
  "qui", ["più", "già", "può"],
  "Qua e qui non vogliono mai l'accento.",
  "Solo qua e qui fanno apparente eccezione, non volendo mai l'accento")

O("ita-042", "Ortografia", 2, "Quando l'accento grafico è obbligatorio sulle parole di più sillabe?",
  "Quando cade sulla vocale finale (es. città, perché)", ["Sempre sulla prima sillaba", "Mai", "Solo nelle parole straniere"],
  "Voce «Ortografia italiana».",
  "L'accento grafico è obbligatorio sulla vocale finale della parola")

O("ita-043", "Ortografia", 3, "Quale coppia mostra un accento distintivo su un monosillabo?",
  "dà (verbo dare) / da (preposizione)", ["qui / quì", "su / sù", "fa / fà"],
  "Hanno accento distintivo è, dà, dì, là, lì, né, sé, sì, tè, ché.",
  "dà (indicativo di dare)")

O("ita-044", "Ortografia", 3, "Su quale vocale finale si usa praticamente sempre l'accento grave (es. però, parlò)?",
  "Sulla o", ["Sulla e", "Sulla i soltanto nel futuro", "Su nessuna"],
  "La o tonica finale è quasi sempre aperta.",
  "In italiano la o tonica finale è praticamente sempre aperta")

O("ita-045", "Ortografia", 4, "Quale ente ha codificato nel 1967 la norma sugli accenti acuto e grave?",
  "L'UNI (Ente nazionale di unificazione)", ["L'Accademia della Crusca", "Il Ministero dell'istruzione", "La Treccani"],
  "Voce «Ortografia italiana».",
  "codificata nel 1967 dall'UNI")

O("ita-046", "Ortografia", 3, "Davanti a quali vocali «sc» indica il suono di «scena»?",
  "Davanti a e e i", ["Davanti a a, o, u", "Davanti a tutte le vocali", "Solo davanti a u"],
  "Davanti ad a, o, u serve il trigramma sci (sciopero, sciupare).",
  "il primo davanti a -e e -i, il secondo davanti alle altre vocali")

O("ita-047", "Ortografia", 3, "Quale regola vale per la z in posizione intervocalica?",
  "Si pronuncia sempre di grado intenso, anche se scritta scempia", ["Si pronuncia sempre semplice", "Si scrive sempre doppia", "Non può mai trovarsi tra due vocali"],
  "Per questo è difficile decidere tra -z- e -zz- (es. azione / pazzo).",
  "in tale posizione è sempre di grado intenso")

O("ita-048", "Ortografia", 3, "Quale grafia è corretta?",
  "azione", ["azzione", "aczione", "atione"],
  "Davanti a -zia, -zie, -zio la z è scempia (azione, grazie, ozio).",
  "nei seguenti nessi: zia, zie, zio, ziu")

O("ita-049", "Ortografia", 4, "Quale di questi derivati in -iere si scrive con la doppia z, eccezione alla regola di «-zie»?",
  "carrozziere", ["polizia", "grazie", "spazio"],
  "Le parole in -iere/-iera da basi in -zz- (carrozza, terrazza) mantengono la doppia.",
  "parole in -iere/-iera: arazziere, battezziere, biscazziere, capezziera, carrozziere")

O("ita-050", "Ortografia", 3, "Nell'italiano di inizio Novecento, come si scriveva spesso «ha» (verbo avere)?",
  "à, con l'accento", ["ha, come oggi", "hà", "a'"],
  "Si scriveva à, ànno al posto di ha, hanno.",
  "la norma accettava quindi à, ànno al posto delle attuali ha e hanno")

O("ita-051", "Ortografia", 4, "Quale grafia si è stabilizzata solo negli anni Sessanta?",
  "sopralluogo", ["sopraluogo", "sopra luogo", "sopral luogo"],
  "Voce «Ortografia italiana».",
  "la grafia sopralluogo (al posto di sopraluogo) si è stabilizzata solo negli anni sessanta")

O("ita-052", "Ortografia", 3, "Quale variante registra il dizionario De Mauro accanto a «tuttora»?",
  "tutt'ora", ["tutt'ora non è ammessa", "tuttoora", "tutto ora"],
  "«Tutt'ora» è considerata variante.",
  "registra la parola tuttora anche nella forma (considerata \"variante\") tutt'ora")

O("ita-053", "Ortografia", 4, "Quale lettera era usata fino all'Ottocento al posto della i intervocalica (es. «noja»)?",
  "La j", ["La y", "La h", "La x"],
  "Sopravvive in alcuni nomi e toponimi (Jesi, Jacopo).",
  "era correntemente utilizzata la ⟨j⟩ al posto della ⟨i⟩")

O("ita-054", "Ortografia", 4, "Davanti a quali vocali la c dolce si può elidere graficamente (es. c'è)?",
  "Solo davanti a e e i", ["Davanti a tutte le vocali", "Solo davanti ad a", "Mai"],
  "Per questo «c'è» è corretto ma «c'ha» no.",
  "l'elisione grafica è possibile soltanto davanti a parole inizianti per e- o per i-")


# --- Blocco 3: grammatica, sintassi e retorica (voci di Wikipedia, CC BY-SA 4.0) ---
CONG = "Wikipedia_Congiuntivo.txt"
COND = "Wikipedia_Condizionale.txt"
PRON = "Wikipedia_Pronome.txt"
AGG = "Wikipedia_Aggettivo.txt"
AVV = "Wikipedia_Avverbio.txt"
PREP = "Wikipedia_Preposizione.txt"
CONGZ = "Wikipedia_Congiunzione-linguistica.txt"
ALP = "Wikipedia_Analisi-logica-della-proposizione.txt"
ALPER = "Wikipedia_Analisi-logica-del-periodo.txt"
SUB = "Wikipedia_Proposizione-subordinata.txt"
CO = "Wikipedia_Complemento-oggetto.txt"
FR = "Wikipedia_Figura-retorica.txt"
MET = "Wikipedia_Metafora.txt"
OSS = "Wikipedia_Ossimoro.txt"
ART = "Wikipedia_Articolo-linguistica.txt"

D("ita-055", "Verbi", 2, "Quale modo verbale esprime un evento soggettivo, dubbioso o ipotetico (es. «Penso che sia ubriaco»)?",
  "Il congiuntivo", ["L'indicativo", "L'imperativo", "Il gerundio"],
  "L'indicativo esprime invece la realtà oggettiva.",
  W("Congiuntivo"), CONG, "la cui funzione basilare è quella di indicare un evento soggettivo, irreale, dubbioso, ipotetico")

D("ita-056", "Verbi", 2, "Quanti tempi ha il congiuntivo italiano?",
  "Quattro: presente, imperfetto, passato, trapassato", ["Due: presente e passato", "Otto, come l'indicativo", "Sei, compreso il futuro"],
  "Il congiuntivo non ha un futuro.",
  W("Congiuntivo"), CONG, "Congiuntivo trapassato (che io fossi arrivato/a")

D("ita-057", "Verbi", 3, "Il congiuntivo italiano ha una forma futura?",
  "No, al suo posto si usano il futuro indicativo o il congiuntivo presente", ["Sì, il congiuntivo futuro", "Sì, ma solo nei verbi irregolari", "Sì, nella lingua letteraria"],
  "Voce «Congiuntivo».",
  W("Congiuntivo"), CONG, "Una forma futura del congiuntivo manca in italiano")

D("ita-058", "Verbi", 2, "Qual è la forma corretta?",
  "Spero che tu venga presto.", ["Spero che tu vieni presto.", "Spero che tu verrai presto ieri.", "Spero che tu venissi presto domani."],
  "Dopo verbi di speranza si usa il congiuntivo.",
  W("Congiuntivo"), CONG, "Spero che tu venga presto.")

D("ita-059", "Verbi", 3, "In una concessiva come «non ti apro, sebbene tu stia suonando», quale modo si usa?",
  "Il congiuntivo", ["L'indicativo", "Il condizionale", "L'infinito"],
  "«Sebbene» regge il congiuntivo.",
  W("Congiuntivo"), CONG, "sebbene tu stia suonando da molto")

D("ita-060", "Verbi", 2, "Quali sono le forme del condizionale italiano?",
  "Presente (mangerei) e passato (avrei mangiato)", ["Presente, passato e futuro", "Solo presente", "Imperfetto e trapassato"],
  "Voce «Condizionale».",
  W("Condizionale"), COND, "le due forme di questo modo sono il condizionale presente")

D("ita-061", "Verbi", 3, "Quale frase è corretta?",
  "Verrei volentieri, se tu mi accompagnassi.", ["Verrei volentieri, se tu mi accompagneresti.", "Venissi volentieri, se tu mi accompagneresti.", "Verrò volentieri, se tu mi accompagnassi ieri."],
  "Nel periodo ipotetico: se + congiuntivo imperfetto, condizionale nella principale.",
  W("Condizionale"), COND, "Verrei volentieri, se tu mi accompagnassi.")

D("ita-062", "Verbi", 4, "In quale caso è corretto usare il condizionale dopo «se»?",
  "Nelle interrogative indirette (es. «Mi chiedo se mangerebbe con noi»)", ["Mai", "Nel periodo ipotetico della possibilità", "Sempre, al posto del congiuntivo"],
  "Voce «Condizionale».",
  W("Condizionale"), COND, "nelle interrogative indirette")

D("ita-063", "Morfologia", 1, "Cosa significa letteralmente «pronome»?",
  "«Al posto del nome»", ["«Prima del nome»", "«Nome importante»", "«Nome proprio»"],
  "Dal latino pro-nomen.",
  W("Pronome"), PRON, "dal latino pro-nomen, \"al posto del nome\"")

D("ita-064", "Morfologia", 2, "A quale categoria appartengono «che, cui, il quale»?",
  "Pronomi relativi", ["Pronomi personali", "Pronomi dimostrativi", "Congiunzioni coordinanti"],
  "Voce «Pronome».",
  W("Pronome"), PRON, "Pronome relativo: che, cui, il quale")

D("ita-065", "Morfologia", 3, "Nella frase «Ti credevo intelligente, ma non lo sei», cosa sostituisce il pronome «lo»?",
  "L'aggettivo «intelligente»", ["Il soggetto «tu»", "Il verbo «credevo»", "Nulla, è un articolo"],
  "Il pronome può sostituire anche aggettivi o intere frasi.",
  W("Pronome"), PRON, "il pronome lo sostituisce intelligente, che è un aggettivo")

D("ita-066", "Morfologia", 3, "Come si distingue un aggettivo da un pronome con la stessa forma (es. «questo»)?",
  "L'aggettivo accompagna il nome, il pronome lo sostituisce", ["Il pronome è sempre maiuscolo", "L'aggettivo è invariabile", "Non si possono distinguere"],
  "Voce «Pronome».",
  W("Pronome"), PRON, "gli aggettivi accompagnano il nome, mentre i pronomi lo sostituiscono")

D("ita-067", "Morfologia", 2, "Quali sono le due grandi classi tradizionali degli aggettivi?",
  "Qualificativi e determinativi", ["Semplici e composti", "Attivi e passivi", "Regolari e irregolari"],
  "I determinativi comprendono possessivi, numerali, dimostrativi, indefiniti, interrogativi ed esclamativi.",
  W("Aggettivo"), AGG, "Gli aggettivi vengono tradizionalmente divisi in due classi")

D("ita-068", "Morfologia", 3, "Quando un aggettivo ha funzione «predicativa»?",
  "Quando, in un predicato nominale, è unito al soggetto dalla copula", ["Quando precede sempre il nome", "Quando è al superlativo", "Quando è invariabile"],
  "Funzione attributiva: si unisce direttamente al nome.",
  W("Aggettivo"), AGG, "predicativa quando, in un predicato nominale, costituisce la parte nominale")

D("ita-069", "Morfologia", 3, "A quale tipo di aggettivi appartiene «alcuni»?",
  "Aggettivi indefiniti", ["Aggettivi qualificativi", "Aggettivi possessivi", "Aggettivi numerali"],
  "Voce «Aggettivo».",
  W("Aggettivo"), AGG, "aggettivi indefiniti (alcuni, tutti, nessuna")

D("ita-070", "Morfologia", 2, "L'avverbio è una parte del discorso variabile o invariabile?",
  "Invariabile", ["Variabile in genere e numero", "Variabile solo nel numero", "Variabile solo nel genere"],
  "Voce «Avverbio».",
  W("Avverbio"), AVV, "è una parte del discorso invariabile")

D("ita-071", "Morfologia", 2, "Che tipo di avverbio è «lentamente»?",
  "Di modo", ["Di tempo", "Di luogo", "Di quantità"],
  "Voce «Avverbio».",
  W("Avverbio"), AVV, "il modo (lentamente, piano, forte, brevemente)")

D("ita-072", "Morfologia", 3, "Che tipo di avverbi sono «probabilmente, certamente, francamente» quando esprimono il giudizio del parlante?",
  "Avverbi frasali", ["Avverbi di luogo", "Avverbi connettivi", "Avverbi di quantità"],
  "Voce «Avverbio».",
  W("Avverbio"), AVV, "avverbi frasali")

D("ita-073", "Morfologia", 1, "Quali sono le preposizioni proprie (semplici) dell'italiano?",
  "di, a, da, in, con, su, per, tra, fra", ["e, o, ma, però", "il, lo, la, i, gli, le", "qui, qua, lì, là"],
  "Voce «Preposizione».",
  W("Preposizione"), PREP, "preposizioni proprie: di, a, da, in, con, su, per, tra, fra")

D("ita-074", "Morfologia", 3, "Quali preposizioni semplici NON formano preposizioni articolate?",
  "tra e fra", ["di e a", "in e su", "da e con"],
  "Voce «Preposizione».",
  W("Preposizione"), PREP, "Non lo fanno tra e fra")

D("ita-075", "Morfologia", 3, "A quale categoria appartiene «tranne»?",
  "Preposizione impropria", ["Congiunzione coordinante", "Avverbio di tempo", "Pronome indefinito"],
  "Le improprie possono essere anche nomi, aggettivi, avverbi o forme verbali.",
  W("Preposizione"), PREP, "Per esempio: tranne, senza, eccetto, salvo")

D("ita-076", "Morfologia", 3, "In «Ho comprato dello zucchero», che funzione ha «dello»?",
  "Articolo partitivo", ["Preposizione semplice", "Pronome", "Complemento di specificazione"],
  "Voce «Preposizione».",
  W("Preposizione"), PREP, "Le preposizioni articolate derivate da di sono spesso usate con la funzione di articoli partitivi")

D("ita-077", "Morfologia", 3, "Quale di queste è una congiunzione composta, nata dalla fusione di più parole?",
  "affinché", ["ma", "e", "se"],
  "affinché = a + fine + che; anche cioè, oppure, perché, poiché.",
  W("Congiunzione (linguistica)"), CONGZ, "affinché (a + fine + che)")

D("ita-078", "Sintassi", 3, "Cosa fanno le congiunzioni subordinanti?",
  "Introducono proposizioni dipendenti", ["Collegano elementi sullo stesso piano", "Sostituiscono il nome", "Indicano il tempo verbale"],
  "Le coordinanti collegano elementi di uguale rango sintattico.",
  W("Congiunzione (linguistica)"), CONGZ, "Le seconde introducono le proposizioni dipendenti")

D("ita-079", "Sintassi", 2, "Da quali elementi è composta la frase minima?",
  "Soggetto e predicato", ["Soggetto, predicato e complemento oggetto", "Solo il predicato", "Articolo e nome"],
  "Voce «Analisi logica della proposizione».",
  W("Analisi logica della proposizione"), ALP, "La frase minima è composta da due elementi")

D("ita-080", "Sintassi", 2, "Da cosa è formato in italiano il predicato nominale?",
  "Dal verbo essere e da un elemento nominale o aggettivale", ["Da un verbo transitivo e un complemento", "Da un verbo all'infinito", "Da un nome e un avverbio"],
  "Esempio: «Lucia è bionda».",
  W("Analisi logica della proposizione"), ALP, "è formato, in italiano, dal verbo essere e da un elemento nominale o aggettivale")

D("ita-081", "Sintassi", 3, "Nella frase «Lucia è bionda», che tipo di predicato c'è?",
  "Predicato nominale", ["Predicato verbale", "Complemento predicativo", "Soggetto sottinteso"],
  "Voce «Analisi logica della proposizione».",
  W("Analisi logica della proposizione"), ALP, "Lucia è bionda")

D("ita-082", "Sintassi", 2, "In «Dormo», qual è il soggetto?",
  "Io, sottinteso", ["Dormo", "Non c'è soggetto", "Il sonno"],
  "Il soggetto può essere sottinteso.",
  W("Analisi logica della proposizione"), ALP, "in frasi come \"dormo\" (sottinteso \"io\")")

D("ita-083", "Sintassi", 2, "A quali domande risponde il complemento oggetto?",
  "Chi? Che cosa?", ["Dove? Quando?", "Con chi? Per chi?", "Di chi? Di che cosa?"],
  "Voce «Complemento oggetto».",
  W("Complemento oggetto"), CO, "Esso risponde alle domande: Chi? Che cosa?")

D("ita-084", "Sintassi", 3, "Da quale tipo di verbo è retto il complemento oggetto?",
  "Da un verbo transitivo attivo", ["Da un verbo intransitivo", "Dal verbo essere", "Da un verbo passivo"],
  "Voce «Complemento oggetto».",
  W("Complemento oggetto"), CO, "è di norma retto da un verbo transitivo")

D("ita-085", "Sintassi", 3, "Come si chiama il complemento oggetto introdotto da un articolo partitivo (es. «delle bibite»)?",
  "Complemento oggetto partitivo", ["Complemento di specificazione", "Complemento di materia", "Complemento oggetto interno"],
  "Voce «Complemento oggetto».",
  W("Complemento oggetto"), CO, "complemento oggetto partitivo")

D("ita-086", "Sintassi", 2, "Che cos'è il periodo, in analisi del periodo?",
  "Una frase compiuta formata da una o più proposizioni collegate", ["Una sola parola", "Un capoverso di un testo", "Il tempo verbale"],
  "Voce «Analisi logica del periodo».",
  W("Analisi logica del periodo"), ALPER, "Il periodo è una frase compiuta formata da una o più proposizioni collegate fra loro")

D("ita-087", "Sintassi", 3, "Come si contano le proposizioni di un periodo?",
  "In base al numero dei predicati", ["In base al numero delle virgole", "In base al numero dei soggetti", "In base al numero dei nomi"],
  "Ogni predicato segna una proposizione.",
  W("Analisi logica del periodo"), ALPER, "il quale segna la presenza di una nuova proposizione")

D("ita-088", "Sintassi", 4, "In «puoi omettere questa parola», quanti predicati ci sono?",
  "Uno: i verbi servili formano un unico predicato con l'infinito", ["Due", "Tre", "Nessuno"],
  "Voce «Analisi logica del periodo».",
  W("Analisi logica del periodo"), ALPER, "in \"puoi omettere questa parola\", il predicato è \"puoi omettere\"")

D("ita-089", "Sintassi", 4, "«Sciare è la mia passione»: quante proposizioni contiene?",
  "Una, perché l'infinito usato come soggetto non forma predicato", ["Due", "Tre", "Nessuna"],
  "Voce «Analisi logica del periodo».",
  W("Analisi logica del periodo"), ALPER, "\"Sciare è la mia passione\" è un'unica proposizione")

D("ita-090", "Sintassi", 3, "Quando una proposizione subordinata è «implicita»?",
  "Quando il verbo è in un modo indefinito", ["Quando il verbo è in un modo finito", "Quando non ha soggetto espresso", "Quando è tra parentesi"],
  "È esplicita se il verbo è in un modo finito.",
  W("Proposizione subordinata"), SUB, "implicita (il verbo è coniugato in un modo indefinito)")

D("ita-091", "Sintassi", 3, "Nella frase «Il cane insegue il gatto che scappa», cos'è «che scappa»?",
  "Una proposizione subordinata relativa", ["La proposizione principale", "Una coordinata", "Un complemento oggetto"],
  "Voce «Proposizione subordinata».",
  W("Proposizione subordinata"), SUB, "la proposizione subordinata (proposizione relativa) è che scappa")

D("ita-092", "Sintassi", 4, "Quali subordinate svolgono la funzione di soggetto o complemento oggetto della reggente?",
  "Le sostantive o completive", ["Le relative", "Le avverbiali", "Le coordinate"],
  "Voce «Proposizione subordinata».",
  W("Proposizione subordinata"), SUB, "Sostantive o completive")

D("ita-093", "Retorica", 2, "Quale figura retorica chiama un uomo coraggioso «un leone»?",
  "La metafora", ["La metonimia", "L'ossimoro", "L'iperbole"],
  "Voce «Figura retorica».",
  W("Figura retorica"), FR, "un uomo coraggioso viene indicato come \"un leone\"")

D("ita-094", "Retorica", 3, "Quale figura retorica è «leggere Dante» per «leggere le opere di Dante»?",
  "La metonimia", ["La metafora", "La similitudine", "L'anafora"],
  "Sostituzione per contiguità logica o materiale.",
  W("Figura retorica"), FR, "\"leggere Dante\" intendendo \"leggere le opere di Dante\"")

D("ita-095", "Retorica", 3, "Come si chiama la figura «parte per il tutto» (es. «vela» per «nave»)?",
  "Sineddoche", ["Metonimia", "Anafora", "Allitterazione"],
  "Voce «Figura retorica».",
  W("Figura retorica"), FR, "sineddoche")

D("ita-096", "Retorica", 3, "Come è definita talvolta l'allegoria?",
  "Una «metafora continuata»", ["Un ossimoro rovesciato", "Una similitudine breve", "Una ripetizione di suoni"],
  "Voce «Figura retorica».",
  W("Figura retorica"), FR, "\"metafora continuata\"")

D("ita-097", "Retorica", 3, "Chi fu il primo, secondo la tradizione, a individuare le figure retoriche nella prosa?",
  "Gorgia da Lentini", ["Cicerone", "Quintiliano", "Aristotele"],
  "Voce «Figura retorica».",
  W("Figura retorica"), FR, "Fu Gorgia da Lentini")

D("ita-098", "Retorica", 2, "Come viene spesso definita la metafora rispetto alla similitudine?",
  "Una similitudine senza il «come»", ["Una similitudine con due «come»", "Un'iperbole", "Un elenco di aggettivi"],
  "Voce «Metafora».",
  W("Metafora"), MET, "la metafora è una similitudine senza il come")

D("ita-099", "Retorica", 3, "Nel verso di Pascoli «Anche un uomo tornava al suo nido», «nido» è una metafora per:",
  "Casa", ["Albero", "Uccello", "Famiglia di uccelli"],
  "Voce «Metafora».",
  W("Metafora"), MET, "nido è una metafora per casa")

D("ita-100", "Retorica", 2, "Quale figura retorica accosta due termini di senso contrario (es. «silenzio assordante»)?",
  "L'ossimoro", ["L'antitesi", "La metafora", "L'iperbole"],
  "Voce «Ossimoro».",
  W("Ossimoro"), OSS, "consiste nell'accostamento di due termini di senso contrario")

D("ita-101", "Retorica", 4, "Quale verso di Leopardi è citato come esempio di ossimoro?",
  "«E 'l naufragar m'è dolce in questo mare»", ["«Sempre caro mi fu quest'ermo colle»", "«Silvia, rimembri ancora»", "«Il sabato del villaggio»"],
  "Voce «Ossimoro».",
  W("Ossimoro"), OSS, "E 'l naufragar m'è dolce in questo mare")

D("ita-102", "Morfologia", 4, "Qual è il plurale di «il dio»?",
  "Gli dèi", ["I dii", "Gli dii", "I dei"],
  "Eccezione nell'uso dell'articolo.",
  W("Articolo (linguistica)"), ART, "il dio ha plurale gli dèi")


# --- Blocco 4: storia della letteratura italiana (voce di Wikipedia, CC BY-SA 4.0) ---
LET = "Wikipedia_Storia-della-letteratura-italiana.txt"
def L(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Storia della letteratura italiana"), LET, frase)

L("ita-103", "Letteratura", 2, "Quale opera è considerata il primo documento letterario italiano di autore noto?",
  "Il Cantico delle creature di Francesco d'Assisi", ["La Divina Commedia", "Il Canzoniere di Petrarca", "Il Novellino"],
  "Voce «Storia della letteratura italiana».",
  "il Cantico delle creature di Francesco d'Assisi")

L("ita-104", "Letteratura", 3, "Sotto il patrocinio di quale sovrano nacque la Scuola siciliana?",
  "Federico II", ["Carlo d'Angiò", "Ruggero II", "Manfredi"],
  "Fu attiva dal 1220-50 circa, ispirata ai modelli provenzali.",
  "sotto il patrocinio di Federico II")

L("ita-105", "Letteratura", 2, "Quanti canti ha la Divina Commedia?",
  "100", ["99", "33", "120"],
  "Tre cantiche di 33 canti più il canto introduttivo.",
  "Esso è composto da 100 canti")

L("ita-106", "Letteratura", 3, "In che metro è scritta la Divina Commedia?",
  "Terzine incatenate di endecasillabi", ["Ottave di endecasillabi", "Endecasillabi sciolti", "Sonetti"],
  "Voce «Storia della letteratura italiana».",
  "in terzine incatenate di versi endecasillabi")

L("ita-107", "Letteratura", 3, "Quale movimento poetico nacque tra fine Duecento e inizio Trecento, maturando la tematica amorosa cortese?",
  "Il Dolce stil novo", ["La Scuola siciliana", "Il Petrarchismo", "La poesia comico-realistica"],
  "Vi appartennero Guinizzelli, Cavalcanti e Dante.",
  "nasce il Dolce stil novo")

L("ita-108", "Letteratura", 4, "A chi Dante dedicò la Vita Nova?",
  "A Guido Cavalcanti", ["A Cino da Pistoia", "A Beatrice Portinari", "A Brunetto Latini"],
  "Voce «Storia della letteratura italiana».",
  "Fu amico di Dante Alighieri, che a lui dedicò la Vita Nova")

L("ita-109", "Letteratura", 4, "Chi è considerato l'ultimo stilnovista, maestro di Petrarca nella musicalità del verso?",
  "Cino da Pistoia", ["Guido Guinizzelli", "Guittone d'Arezzo", "Cecco Angiolieri"],
  "Voce «Storia della letteratura italiana».",
  "L'ultimo stilnovista fu Cino da Pistoia")

L("ita-110", "Letteratura", 4, "Che cos'è il «Novellino»?",
  "Una raccolta di cento novelle antiche di autore ignoto, fine Duecento", ["Un'opera di Boccaccio", "Un poema di Ariosto", "Un trattato di Bembo"],
  "Voce «Storia della letteratura italiana».",
  "il Novellino o \"Le cento novelle antiche\"")

L("ita-111", "Letteratura", 3, "Chi scrisse l'Orlando innamorato, poi proseguito dall'Orlando furioso?",
  "Matteo Maria Boiardo", ["Ludovico Ariosto", "Luigi Pulci", "Torquato Tasso"],
  "Voce «Storia della letteratura italiana».",
  "Matteo Boiardo nel suo Orlando innamorato")

L("ita-112", "Letteratura", 2, "Chi è l'autore della Gerusalemme liberata?",
  "Torquato Tasso", ["Ludovico Ariosto", "Giambattista Marino", "Dante Alighieri"],
  "Voce «Storia della letteratura italiana».",
  "le opere letterarie di Torquato Tasso, il suo poema la Gerusalemme liberata")

L("ita-113", "Letteratura", 3, "Di quale corte fu cortigiano Ludovico Ariosto?",
  "Quella di Ferrara (Este)", ["Quella di Firenze (Medici)", "Quella di Milano (Sforza)", "Quella di Napoli (Aragona)"],
  "Voce «Storia della letteratura italiana».",
  "Cortigiano del casato ferrarese")

L("ita-114", "Letteratura", 2, "Qual è l'opera maggiore di Niccolò Machiavelli?",
  "Il Principe", ["La Storia d'Italia", "Il Cortegiano", "La Mandragola"],
  "La Mandragola è una commedia di Machiavelli.",
  "L'opera maggiore di Machiavelli è Il principe")

L("ita-115", "Letteratura", 3, "Chi scrisse la Storia d'Italia del Cinquecento, fondamentale per la storiografia moderna?",
  "Francesco Guicciardini", ["Niccolò Machiavelli", "Pietro Bembo", "Giorgio Vasari"],
  "Voce «Storia della letteratura italiana».",
  "Francesco Guicciardini, con le Storie fiorentine")

L("ita-116", "Letteratura", 3, "Quale opera di Pietro Bembo (1525) sostenne l'eccellenza del toscano letterario di Petrarca e Boccaccio?",
  "Prose della volgar lingua", ["Il Cortegiano", "De vulgari eloquentia", "Il Galateo"],
  "Voce «Storia della letteratura italiana».",
  "Prose della volgar lingua del Bembo (1525)")

L("ita-117", "Letteratura", 2, "Quale opera di Galileo Galilei è citata come esempio di italiano scientifico divulgativo?",
  "Dialogo sopra i due massimi sistemi del mondo", ["Il Saggiatore soltanto", "La Città del Sole", "Della ragion di Stato"],
  "Voce «Storia della letteratura italiana».",
  "Dialogo sopra i due massimi sistemi del mondo")

L("ita-118", "Letteratura", 4, "Qual è il poema maggiore di Giambattista Marino, simbolo della poesia barocca?",
  "L'Adone", ["La secchia rapita", "Il Morgante", "L'Arcadia"],
  "Voce «Storia della letteratura italiana».",
  "Il suo testo maggiore, l'Adone")

L("ita-119", "Letteratura", 3, "Chi scrisse il Morgante, poema in ottave del circolo mediceo?",
  "Luigi Pulci", ["Angelo Poliziano", "Lorenzo de' Medici", "Matteo Maria Boiardo"],
  "Voce «Storia della letteratura italiana».",
  "Luigi Pulci che scrisse un poema in ottave intitolato il Morgante")

L("ita-120", "Letteratura", 3, "In che anno e dove fu fondata l'Accademia dell'Arcadia?",
  "A Roma nel 1690", ["A Firenze nel 1583", "A Napoli nel 1700", "A Milano nel 1764"],
  "Fondata da Gravina e Crescimbeni.",
  "un'accademia letteraria fondata a Roma nel 1690")

L("ita-121", "Letteratura", 3, "Chi è il più importante autore dell'Arcadia, attivo alla corte austriaca?",
  "Pietro Metastasio", ["Carlo Goldoni", "Giuseppe Parini", "Vittorio Alfieri"],
  "Voce «Storia della letteratura italiana».",
  "Il più importante autore è sicuramente Pietro Metastasio")

L("ita-122", "Letteratura", 2, "Quale autore rinnovò il teatro italiano portando la commedia nella società del suo tempo?",
  "Carlo Goldoni", ["Vittorio Alfieri", "Pietro Metastasio", "Carlo Gozzi"],
  "Voce «Storia della letteratura italiana».",
  "Carlo Goldoni è assai conosciuto nella letteratura italiana teatrale")

L("ita-123", "Letteratura", 3, "In che metro è scritto «Il Giorno» di Parini?",
  "Endecasillabi sciolti", ["Terzine dantesche", "Ottave", "Sonetti"],
  "Satira dell'aristocrazia decaduta.",
  "Il Giorno, scritto in endecasillabi sciolti")

L("ita-124", "Letteratura", 3, "Chi fondò la rivista illuminista milanese «Il Caffè»?",
  "Pietro Verri", ["Cesare Beccaria", "Giuseppe Parini", "Gaetano Filangieri"],
  "Voce «Storia della letteratura italiana».",
  "Pietro Verri, fondatore della celebre rivista Il Caffè")

L("ita-125", "Letteratura", 2, "Quali sono i maggiori rappresentanti del Romanticismo italiano?",
  "Alessandro Manzoni e Giacomo Leopardi", ["Carducci e Pascoli", "Verga e Capuana", "Ungaretti e Montale"],
  "Voce «Storia della letteratura italiana».",
  "rappresentato maggiormente da Alessandro Manzoni e Giacomo Leopardi")

L("ita-126", "Letteratura", 3, "Come si chiama il diario-zibaldone di pensieri tenuto da Leopardi dal 1817?",
  "Lo Zibaldone", ["Le Operette morali", "I Canti", "L'Epistolario"],
  "Voce «Storia della letteratura italiana».",
  "Lo Zibaldone è un enorme diario personale")

L("ita-127", "Letteratura", 2, "Quale romanzo di Verga (1881) segna il pieno passaggio al verismo?",
  "I Malavoglia", ["Mastro-don Gesualdo", "Storia di una capinera", "Vita dei campi"],
  "Mastro-don Gesualdo è del 1888.",
  "con il romanzo de I Malavoglia (1881)")

L("ita-128", "Letteratura", 3, "Quale movimento lombardo si opponeva ai sistemi classici, incluso il Romanticismo?",
  "La Scapigliatura", ["Il Verismo", "Il Crepuscolarismo", "L'Ermetismo"],
  "Voce «Storia della letteratura italiana».",
  "il movimento lombardo della \"Scapigliatura\"")

L("ita-129", "Letteratura", 3, "Quale raccolta di Pascoli ha un titolo ispirato a un verso virgiliano?",
  "Myricae", ["Canti di Castelvecchio", "Laudi", "Alcyone"],
  "Voce «Storia della letteratura italiana».",
  "il titolo Myricae della raccolta poetica più famosa")

L("ita-130", "Letteratura", 3, "Quale romanzo di D'Annunzio apre la «trilogia della Rosa»?",
  "Il piacere", ["Il fuoco", "Le vergini delle rocce", "Forse che sì forse che no"],
  "Seguono L'innocente e Trionfo della morte.",
  "Il piacere - L'innocente - Trionfo della morte")

L("ita-131", "Letteratura", 2, "Quale celebre opera teatrale è di Luigi Pirandello?",
  "Sei personaggi in cerca d'autore", ["Natale in casa Cupiello", "La locandiera", "Mistero buffo"],
  "Pirandello vinse il Nobel nel 1934.",
  "Sei personaggi in cerca d'autore")

L("ita-132", "Letteratura", 3, "In che anno Pirandello vinse il premio Nobel per la letteratura?",
  "Nel 1934", ["Nel 1926", "Nel 1959", "Nel 1975"],
  "Grazia Deledda lo vinse nel 1926, Quasimodo nel 1959, Montale nel 1975.",
  "Luigi Pirandello, Premio Nobel per la letteratura nel 1934")

L("ita-133", "Letteratura", 2, "Qual è il romanzo più noto di Italo Svevo?",
  "La coscienza di Zeno", ["Il fu Mattia Pascal", "Uno, nessuno e centomila", "Il Gattopardo"],
  "Voce «Storia della letteratura italiana».",
  "Italo Svevo e La coscienza di Zeno")

L("ita-134", "Letteratura", 3, "Quale scrittrice italiana vinse il Nobel per la letteratura nel 1926?",
  "Grazia Deledda", ["Matilde Serao", "Elsa Morante", "Sibilla Aleramo"],
  "Autrice di Canne al vento.",
  "Grazia Deledda (Canne al vento; Premio Nobel per la letteratura nel 1926)")

L("ita-135", "Letteratura", 3, "Chi fondò il movimento futurista, con il Manifesto del 1909?",
  "Filippo Tommaso Marinetti", ["Gabriele D'Annunzio", "Umberto Boccioni", "Giovanni Papini"],
  "Voce «Storia della letteratura italiana».",
  "Fondatore del movimento futurista è Filippo Tommaso Marinetti")

L("ita-136", "Letteratura", 3, "Qual è il poeta crepuscolare più famoso?",
  "Guido Gozzano", ["Gabriele D'Annunzio", "Dino Campana", "Umberto Saba"],
  "Il termine «crepuscolari» fu coniato dal critico Borgese.",
  "il poeta che ha acquistato maggior fama è Guido Gozzano")

L("ita-137", "Letteratura", 3, "Chi coniò nel 1936 il termine «poesia ermetica»?",
  "Il critico Francesco Flora", ["Benedetto Croce", "Giuseppe Ungaretti", "Eugenio Montale"],
  "Voce «Storia della letteratura italiana».",
  "La poesia ermetica fu così chiamata nel 1936 dal critico Francesco Flora")

L("ita-138", "Letteratura", 3, "Quale poeta ermetico vinse il Nobel per la letteratura nel 1959?",
  "Salvatore Quasimodo", ["Giuseppe Ungaretti", "Eugenio Montale", "Umberto Saba"],
  "Voce «Storia della letteratura italiana».",
  "Salvatore Quasimodo vincitore del premio Nobel per la letteratura nel 1959")

L("ita-139", "Letteratura", 2, "Qual è la prima raccolta di Eugenio Montale (1925)?",
  "Ossi di seppia", ["L'allegria", "Le occasioni", "Il porto sepolto"],
  "Montale vinse il Nobel nel 1975.",
  "Montale, in Ossi di seppia (1925)")

L("ita-140", "Letteratura", 3, "Di quale raccolta di Ungaretti fa parte «Il porto sepolto»?",
  "L'allegria", ["Sentimento del tempo", "Ossi di seppia", "Acque e terre"],
  "Voce «Storia della letteratura italiana».",
  "La poesia che dà il titolo alla raccolta L'allegria del 1916")

L("ita-141", "Letteratura", 4, "Quale corrente si sviluppa in Italia nel secondo dopoguerra per raccontare la realtà della guerra e della Resistenza?",
  "Il neorealismo", ["Il decadentismo", "Il verismo", "Il futurismo"],
  "Voce «Storia della letteratura italiana».",
  "In questo periodo si sviluppa in Italia il neorealismo")

L("ita-142", "Letteratura", 4, "Quale autore teatrale napoletano scrisse «Natale in casa Cupiello» e «Filumena Marturano»?",
  "Eduardo De Filippo", ["Dario Fo", "Luigi Pirandello", "Carlo Goldoni"],
  "Voce «Storia della letteratura italiana».",
  "Natale in casa Cupiello e Filumena Marturano")

L("ita-143", "Letteratura", 4, "Quale accademia fiorentina, nata nel Cinquecento, contribuì a cristallizzare la lingua letteraria?",
  "L'Accademia della Crusca", ["L'Accademia dei Lincei", "L'Accademia del Cimento", "L'Arcadia"],
  "Voce «Storia della letteratura italiana».",
  "La fondazione dell'Accademia della Crusca")


# --- Blocco 5: fonetica, verbi e figure di suono (voci di Wikipedia, CC BY-SA 4.0) ---
PI = "Wikipedia_Periodo-ipotetico.txt"
AUS = "Wikipedia_Verbo-ausiliare.txt"
PART = "Wikipedia_Participio.txt"
GER = "Wikipedia_Gerundio.txt"
SIL = "Wikipedia_Sillaba.txt"
DIT = "Wikipedia_Dittongo.txt"
IAT = "Wikipedia_Iato.txt"
ELI = "Wikipedia_Elisione.txt"
APO = "Wikipedia_Apocope.txt"
ANA = "Wikipedia_Anafora-figura-retorica.txt"
ALL = "Wikipedia_Allitterazione.txt"
ONO = "Wikipedia_Onomatopea.txt"

D("ita-144", "Sintassi", 3, "Come si chiamano le due parti del periodo ipotetico?",
  "Protasi (condizione) e apodosi (conseguenza)", ["Tesi e antitesi", "Premessa e conclusione grammaticale", "Reggente e coordinata"],
  "Voce «Periodo ipotetico».",
  W("Periodo ipotetico"), PI, "proposizione subordinata condizionale (detta protasi) e dalla sua reggente (detta apodosi)")

D("ita-145", "Sintassi", 3, "Quali sono i tre tipi tradizionali di periodo ipotetico?",
  "Della realtà, della possibilità e dell'irrealtà", ["Del passato, del presente e del futuro", "Attivo, passivo e riflessivo", "Semplice, composto e complesso"],
  "Voce «Periodo ipotetico».",
  W("Periodo ipotetico"), PI, "periodo ipotetico della realtà, della possibilità e della irrealtà")

D("ita-146", "Sintassi", 2, "Qual è la congiunzione tipica della protasi in italiano?",
  "se", ["che", "quando", "perché"],
  "Voce «Periodo ipotetico».",
  W("Periodo ipotetico"), PI, "In italiano quella tipica della protasi è se")

D("ita-147", "Verbi", 2, "Quali sono i verbi ausiliari dell'italiano usati per i tempi composti?",
  "Essere e avere", ["Fare e andare", "Potere e dovere", "Stare e volere"],
  "Es. ho fatto, ero andato.",
  W("Verbo ausiliare"), AUS, "coniugati con l'ausilio dei verbi avere (ho fatto) ed essere (ero andato)")

D("ita-148", "Verbi", 3, "Perché il participio si chiama così?",
  "Perché partecipa delle categorie dell'aggettivo e del sostantivo", ["Perché indica partenza", "Perché si usa solo al passato", "Perché è parte del congiuntivo"],
  "Dal latino partem capit.",
  W("Participio"), PART, "Deve il suo nome al fatto che partecipa")

D("ita-149", "Verbi", 2, "Quanti tempi ha il participio in italiano?",
  "Due: presente e passato", ["Tre: presente, passato e futuro", "Uno", "Quattro"],
  "Voce «Participio».",
  W("Participio"), PART, "Ha in italiano due tempi, il presente e il passato")

D("ita-150", "Verbi", 3, "In «una scatola contenente diversi oggetti», cosa sostituisce il participio presente?",
  "Una proposizione relativa («che contiene»)", ["Un complemento di luogo", "Un avverbio", "Un imperativo"],
  "Voce «Participio».",
  W("Participio"), PART, "una scatola contenente diversi oggetti piccolissimi ('che contiene')")

D("ita-151", "Verbi", 2, "Quali sono i tempi del gerundio?",
  "Presente (mangiando) e passato (avendo mangiato)", ["Solo presente", "Presente, passato e futuro", "Imperfetto e trapassato"],
  "Voce «Gerundio».",
  W("Gerundio"), GER, "il presente (mangiando) e il passato (avendo mangiato)")

D("ita-152", "Verbi", 3, "Con quale verbo si forma la perifrasi progressiva (es. «sto scrivendo»)?",
  "Stare + gerundio", ["Essere + participio", "Avere + infinito", "Andare + gerundio passato"],
  "Voce «Gerundio».",
  W("Gerundio"), GER, "introdotta dal verbo stare (sto scrivendo)")

D("ita-153", "Verbi", 3, "Il gerundio si coniuga secondo la persona?",
  "No, non è coniugabile a seconda della persona", ["Sì, come l'indicativo", "Solo al passato", "Solo alla terza persona"],
  "È un modo indefinito.",
  W("Gerundio"), GER, "il gerundio non è coniugabile a seconda della persona")

D("ita-154", "Verbi", 3, "Qual è il gerundio di «fare»?",
  "facendo", ["fando", "facendendo", "fatto"],
  "I verbi con radice abbreviata formano il gerundio sulla base dell'imperfetto (facevo → facendo, dicevo → dicendo).",
  W("Gerundio"), GER, "fare, dire, bere, condurre e trarre danno rispettivamente facendo")

D("ita-155", "Fonetica", 2, "Come si chiama una parola con l'accento sulla penultima sillaba (es. «casa»)?",
  "Piana", ["Tronca", "Sdrucciola", "Bisdrucciola"],
  "Tronche: ultima sillaba; sdrucciole: terzultima; bisdrucciole: quartultima. In italiano prevalgono le piane.",
  W("Sillaba"), SIL, "piane quando la sillaba tonica è la penultima")

D("ita-156", "Fonetica", 2, "Come si chiama una parola con l'accento sulla terzultima sillaba (es. «tavolo»)?",
  "Sdrucciola", ["Piana", "Tronca", "Bisdrucciola"],
  "Voce «Sillaba».",
  W("Sillaba"), SIL, "sdrucciole quando la sillaba tonica è la terzultima")

D("ita-157", "Fonetica", 2, "Come si chiama una parola con l'accento sull'ultima sillaba (es. «città»)?",
  "Tronca", ["Piana", "Sdrucciola", "Atona"],
  "Voce «Sillaba».",
  W("Sillaba"), SIL, "parole tronche quando la sillaba tonica è l'ultima")

D("ita-158", "Fonetica", 3, "Quando una sillaba è detta «aperta» o «libera»?",
  "Quando termina per vocale", ["Quando termina per consonante", "Quando è accentata", "Quando ha due vocali"],
  "È «chiusa» o «implicata» se termina per consonante.",
  W("Sillaba"), SIL, "Una sillaba è detta \"aperta\" o \"libera\" quando termina per vocale")

D("ita-159", "Fonetica", 3, "Qual è l'unica parte obbligatoria di una sillaba?",
  "Il nucleo", ["L'attacco", "La coda", "La rima"],
  "Voce «Sillaba».",
  W("Sillaba"), SIL, "Il nucleo è l'unica parte obbligatoria")

D("ita-160", "Fonetica", 3, "Come si chiama la sillaba che precede la sillaba tonica?",
  "Protonica", ["Postonica", "Tronca", "Atona finale"],
  "Voce «Sillaba».",
  W("Sillaba"), SIL, "La sillaba protonica è quella che precede la sillaba tonica")

D("ita-161", "Fonetica", 2, "Cosa significa letteralmente «dittongo»?",
  "«Con due suoni»", ["«Due sillabe»", "«Suono doppio di consonante»", "«Senza accento»"],
  "Dal greco díphthongos.",
  W("Dittongo"), DIT, "\"con due suoni\"")

D("ita-162", "Fonetica", 3, "Cos'è lo iato?",
  "L'incontro di due vocali pronunciate in due sillabe distinte", ["L'unione di due vocali in una sillaba", "Una consonante doppia", "La caduta di una vocale finale"],
  "Dal latino hiatus, «apertura».",
  W("Iato"), IAT, "consiste nel dividere tra due sillabe due vocali")

D("ita-163", "Ortografia", 2, "Cos'è l'elisione?",
  "La caduta di una vocale finale non accentata davanti a parola che inizia per vocale", ["La caduta di una sillaba iniziale", "Il raddoppio di una consonante", "L'aggiunta di una vocale"],
  "Nello scritto si segnala con l'apostrofo.",
  W("Elisione"), ELI, "è la caduta di una vocale finale non accentata davanti a una parola che inizia per vocale")

D("ita-164", "Ortografia", 3, "Con quale parola l'elisione è considerata obbligatoria?",
  "Con l'articolo «lo» (es. l'animale)", ["Con «una» usato come pronome", "Con l'articolo «gli» davanti a qualsiasi vocale", "Con «tra» e «fra»"],
  "Anche con dello, allo, quello: dell'oro, quell'uomo.",
  W("Elisione"), ELI, "Con l'articolo lo e le preposizioni articolate che lo includono")

D("ita-165", "Ortografia", 3, "«Una» si apostrofa quando è pronome?",
  "No, mai", ["Sì, sempre", "Solo davanti a e", "Solo nello stile giornalistico"],
  "Voce «Elisione».",
  W("Elisione"), ELI, "una non si apostrofa mai quando è pronome")

D("ita-166", "Ortografia", 3, "In cosa l'apocope (troncamento) differisce dall'elisione?",
  "La parola tronca conserva il significato anche isolata e di solito non vuole l'apostrofo", ["L'apocope vuole sempre l'apostrofo", "L'apocope avviene solo davanti a vocale", "Non c'è differenza"],
  "Voce «Apocope».",
  W("Apocope"), APO, "l'elisione è sempre accompagnata dall'apostrofo, mentre il troncamento solo in pochi casi")

D("ita-167", "Ortografia", 4, "Parole come «città» e «virtù» derivano da quale fenomeno storico?",
  "Dal troncamento di antiche forme (cittade, virtute)", ["Dall'elisione davanti a vocale", "Dall'aggiunta di un accento grafico", "Da prestiti francesi"],
  "Voce «Apocope».",
  W("Apocope"), APO, "città(de), libertà(de), virtù(te)")

D("ita-168", "Retorica", 2, "Quale figura retorica ripete una o più parole all'inizio di versi o frasi successive?",
  "L'anafora", ["L'epifora", "L'ossimoro", "La sineddoche"],
  "L'epifora ripete invece alla fine.",
  W("Anafora (figura retorica)"), ANA, "consiste nel ripetere una o più parole all'inizio di frasi")

D("ita-169", "Retorica", 3, "Come si chiama la figura che ripete gli elementi alla fine dei versi o frasi?",
  "Epifora", ["Anafora", "Climax", "Chiasmo"],
  "Voce «Anafora (figura retorica)».",
  W("Anafora (figura retorica)"), ANA, "Analoga all'anafora è l'epifora, che però colloca gli elementi ripetuti alla fine")

D("ita-170", "Retorica", 3, "Come si chiama la ripetizione di una congiunzione coordinativa (es. «e... e... e»)?",
  "Polisindeto", ["Asindeto", "Anadiplosi", "Simploche"],
  "L'asindeto è invece l'assenza di congiunzioni.",
  W("Anafora (figura retorica)"), ANA, "si ottiene un polisindeto")

D("ita-171", "Retorica", 2, "Quale figura ripete suoni uguali o simili all'inizio di parole vicine (es. «senza capo né coda»)?",
  "L'allitterazione", ["L'onomatopea", "La rima", "L'anafora"],
  "Voce «Allitterazione».",
  W("Allitterazione"), ALL, "consiste nella ripetizione, spontanea o ricercata")

D("ita-172", "Retorica", 2, "Quale figura riproduce con i suoni della lingua un rumore (es. «bau bau», «rimbombo»)?",
  "L'onomatopea", ["L'allitterazione", "La sinestesia", "La metafora"],
  "Voce «Onomatopea».",
  W("Onomatopea"), ONO, "che riproduce, attraverso i suoni linguistici di una determinata lingua, il rumore")

D("ita-173", "Retorica", 4, "«Miagolare» e «ronzare» sono onomatopee:",
  "Secondarie, cioè parole con un significato che indicano un suono", ["Primarie", "Non sono onomatopee", "Straniere"],
  "Le primarie sono come «miao» o «brrr».",
  W("Onomatopea"), ONO, "come è il caso di termini che indicano il manifestarsi di un suono: miagolare, abbaiare, ronzare")


# --- Blocco 6: accenti, apostrofo, abbreviazioni, maiuscole (voce «Ortografia italiana») ---
O("ita-174", "Ortografia", 3, "Quale accento richiede il «tè» (bevanda) e quale «perché»?",
  "tè con il grave, perché con l'acuto", ["Entrambi con l'acuto", "Entrambi con il grave", "tè con l'acuto, perché con il grave"],
  "La e di tè, caffè, cioè è aperta; i composti di che (perché, affinché) hanno la é chiusa.",
  "La é sui composti di che (affinché, benché")

O("ita-175", "Ortografia", 3, "Quale grafia è corretta?",
  "ventitré", ["ventitrè", "ventitre", "venti tre"],
  "I composti di tre vogliono l'accento acuto.",
  "i composti di tre (ventitré")

O("ita-176", "Ortografia", 3, "Quale accento vuole la terza persona del passato remoto di potere?",
  "poté (acuto)", ["potè (grave)", "pote (senza accento)", "potê (circonflesso)"],
  "Le terze persone del passato remoto in -é hanno l'accento acuto.",
  "le terze persone singolari del passato remoto in -é (poté, credé)")

O("ita-177", "Ortografia", 3, "Come si scrive l'imperativo di «fare» per distinguerlo dalla terza persona?",
  "fa'", ["fà", "fa", "fah"],
  "Lo stesso per da', sta', va'.",
  "i quattro imperativi: da', fa', sta' e va'")

O("ita-178", "Ortografia", 2, "Quale grafia è corretta?",
  "un po'", ["un pò", "un po", "un pó"],
  "«Po'» è apocope di «poco» e vuole l'apostrofo.",
  "negli avverbi: po' e a mo' di, rispettivamente apocopi di poco e modo")

O("ita-179", "Ortografia", 3, "Come si indicano in forma abbreviata gli anni in cifre (es. 1968)?",
  "Con l'apostrofo: il '68", ["Senza segni: il 68", "Con l'accento: il 68'", "Con il trattino: il -68"],
  "L'apostrofo è obbligatorio in questo caso; con elisione se ne usa uno solo (dell'800).",
  "il '68 (il 1968)")

O("ita-180", "Ortografia", 3, "È un errore andare a capo dopo un apostrofo (es. dell'/oro)?",
  "No, è una consuetudine tipografica, non una regola grammaticale", ["Sì, è sempre un errore grammaticale", "Sì, ma solo nei testi giuridici", "No, anzi è obbligatorio"],
  "Voce «Ortografia italiana».",
  "è una norma destituita di qualsiasi fondamento grammaticale")

O("ita-181", "Ortografia", 3, "Dove si mette il punto nell'abbreviazione per contrazione «fratelli»?",
  "In mezzo: f.lli", ["Alla fine: flli.", "Non si mette", "All'inizio: .flli"],
  "Nelle abbreviazioni per troncamento il punto va alla fine (sig.).",
  "f.lli (fratelli), gent.ma (gentilissima)")

O("ita-182", "Ortografia", 3, "Come si abbrevia «pagine» al plurale?",
  "pp.", ["pg.", "p.p", "pagg"],
  "Il raddoppio dell'ultima lettera indica il plurale (pp., sgg.).",
  "pp. (pagine)")

O("ita-183", "Ortografia", 3, "Cosa significa l'abbreviazione «cfr.»?",
  "Confronta", ["Conforme", "Certificato", "Come sopra"],
  "Dal latino confer.",
  "cfr. (confer, confronta)")

O("ita-184", "Ortografia", 3, "In quali casi l'iniziale maiuscola è tassativamente obbligatoria?",
  "All'inizio di un periodo e con i nomi propri", ["Con tutti i nomi di professione", "Con i giorni della settimana", "Con tutti gli aggettivi"],
  "Gli altri usi dipendono da stile e consuetudine.",
  "l'iniziale maiuscola in due casi: 1. all'inizio di un periodo o di una frase, 2. con i nomi propri")

O("ita-185", "Ortografia", 3, "Come si scrivono di solito i nomi dei popoli del presente?",
  "Con la minuscola (gli italiani)", ["Sempre con la maiuscola", "Tutti in maiuscolo", "Con l'iniziale maiuscola solo al plurale"],
  "I popoli storici del passato si scrivono di solito con la maiuscola (i Romani).",
  "con la minuscola i popoli del presente (gli italiani)")

O("ita-186", "Ortografia", 4, "Quando le particelle «de», «di», «da» nei nomi vogliono la maiuscola?",
  "Negli attuali cognomi di cui fanno parte (De Nicola, D'Annunzio)", ["Sempre", "Mai", "Solo nei nomi medievali (Francesco Da Assisi)"],
  "Nei patronimici e toponimici antichi restano minuscole (Tommaso d'Aquino).",
  "la vogliono invece negli attuali cognomi di cui fanno parte")

O("ita-187", "Ortografia", 3, "Cos'è la «maiuscola reverenziale»?",
  "La maiuscola usata nei pronomi di cortesia o riferiti a Dio (es. «porgerLe»)", ["La maiuscola all'inizio di ogni verso", "La maiuscola delle sigle", "La maiuscola dei titoli di libro"],
  "Voce «Ortografia italiana».",
  "La \"maiuscola reverenziale\" è utilizzata ancora di frequente")

O("ita-188", "Ortografia", 3, "Quando è previsto l'uso del corsivo?",
  "Per titoli di opere, nomi scientifici e parole straniere non acclimatate", ["Per tutti i nomi propri", "Per i verbi", "Mai, è solo una scelta grafica"],
  "Voce «Ortografia italiana».",
  "nel riportare i titoli di opere")

O("ita-189", "Ortografia", 3, "Cosa indica il trattino a fine riga?",
  "La continuazione nella riga successiva di una parola spezzata", ["Un inciso", "Una pausa lunga", "Un'abbreviazione"],
  "Voce «Ortografia italiana».",
  "la continuazione nella riga successiva di una parola spezzata in fin di rigo")

O("ita-190", "Ortografia", 4, "Che funzione ha oggi il circonflesso nell'italiano, ad es. in «principî»?",
  "Segnala una contrazione e può distinguere omografi (principi/principî)", ["Indica una vocale aperta", "Indica una vocale lunga obbligatoria", "Indica l'accento tonico obbligatorio"],
  "Voce «Ortografia italiana».",
  "principi /ˈprintʃipi/ vs principî")

O("ita-191", "Ortografia", 3, "Nella scrittura di netiquette, scrivere tutto in maiuscolo equivale a:",
  "Urlare", ["Essere formali", "Citare", "Abbreviare"],
  "Voce «Ortografia italiana».",
  "in quanto equivale a urlare")

O("ita-192", "Ortografia", 3, "Quale di queste parole è tradizionalmente scritta unita (univerbata)?",
  "dappertutto", ["dapper tutto", "da per tutto obbligatorio", "d'appertutto"],
  "Voce «Ortografia italiana».",
  "Fanno eccezione alcune forme tradizionalmente univerbate: dappertutto")

O("ita-193", "Ortografia", 4, "Come si scrive correttamente la sequenza davanti a vocale?",
  "grand'uomo", ["gran'uomo", "grande'uomo", "grand uomo"],
  "«Grande» si elide davanti a vocale e si tronca davanti a consonante (gran giocatore).",
  "grand'uomo")

O("ita-194", "Ortografia", 3, "Quale forma è corretta davanti a consonante?",
  "un gatto", ["un'gatto", "uno gatto", "una gatto"],
  "«Un» è troncamento, non vuole apostrofo; «uno» davanti a s impura, z, gn ecc.",
  "un gatto")

O("ita-195", "Ortografia", 2, "Quale forma è corretta?",
  "un'amica", ["un amica", "una amica obbligatorio", "uno amica"],
  "Al femminile davanti a vocale si elide «una» con l'apostrofo.",
  "un'amica")

D("ita-196", "Punteggiatura", 2, "Da quale parola latina deriva «virgola»?",
  "Virgula, «piccola verga»", ["Virgo, «vergine»", "Vir, «uomo»", "Virtus, «virtù»"],
  "Voce «Punteggiatura».",
  W("Punteggiatura"), "Wikipedia_Punteggiatura.txt", "virgula, \"piccola verga\"")

PUN = "Wikipedia_Punteggiatura.txt"
D("ita-197", "Punteggiatura", 3, "Come è considerato il punto rispetto alla virgola in dottrina?",
  "Il punto è una pausa forte e chiusa, la virgola una pausa debole e aperta", ["Sono equivalenti", "La virgola è più forte del punto", "Nessuno dei due indica una pausa"],
  "Punto e virgola e due punti sono pause intermedie secondo la Treccani.",
  W("Punteggiatura"), PUN, "il punto viene considerata una pausa forte e chiusa mentre la virgola una pausa debole e aperta")

D("ita-198", "Punteggiatura", 3, "In greco moderno, quale segno indica la domanda?",
  "Un segno simile al punto e virgola", ["Il punto esclamativo", "Il punto interrogativo rovesciato", "I due punti"],
  "Voce «Punteggiatura».",
  W("Punteggiatura"), PUN, "in greco moderno, il punto interrogativo è rappresentato da un punto e virgola")

D("ita-199", "Punteggiatura", 3, "Quale lingua apre le domande con un punto interrogativo rovesciato (¿)?",
  "Lo spagnolo", ["Il francese", "Il tedesco", "L'inglese"],
  "Voce «Punteggiatura».",
  W("Punteggiatura"), PUN, "in spagnolo queste vengono racchiuse tra")

D("ita-200", "Punteggiatura", 4, "Da quale parola latina deriverebbe il punto esclamativo?",
  "Io, «evviva»", ["Quaestio, «domanda»", "Ecce, «ecco»", "Exclamatio"],
  "Il punto interrogativo deriverebbe invece da quaestio.",
  W("Punteggiatura"), PUN, "il punto esclamativo, che deriva dal latino io")

D("ita-201", "Punteggiatura", 4, "Chi propose nel 1962 il «punto esclarrogativo» (‽)?",
  "Il pubblicitario americano Martin K. Speckter", ["Francesco Flora", "Hervé Bazin", "Pietro Bembo"],
  "Voce «Punteggiatura».",
  W("Punteggiatura"), PUN, "il pubblicitario americano Martin K. Speckter propose il punto esclarrogativo")

# --- Ampliamento a 300: letteratura, grammatica, articolo, verbo, dittonghi, punteggiatura ---
def GR(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Grammatica italiana"), GRA, frase)

L("ita-202", "Letteratura", 3, "Quale antico documento in volgare paragona la scrittura al lavoro del seminatore?",
  "L'Indovinello veronese", ["Il Placito capuano", "Il Cantico delle creature", "Il Ritmo laurenziano"],
  "Fu scoperto nel 1924 in un codice della Biblioteca Capitolare di Verona (fine VIII-inizio IX secolo).", "l'Indovinello veronese, composto da quattro brevi versi")
L("ita-203", "Letteratura", 3, "A quale anno risale il Placito capuano, con la formula «Sao ko kelle terre…»?",
  "Al 960", ["Al 1224", "Al 1100", "Al 800"],
  "Riporta la testimonianza in una lite di confini tra il monastero di Montecassino e Rodelgrimo d'Aquino.", "In un placito capuano del 960")
L("ita-204", "Letteratura", 3, "Quale lauda di Jacopone da Todi segna il vertice della poesia religiosa del Duecento?",
  "Lo Stabat Mater", ["Il Cantico delle creature", "Il Dies irae", "Il Te Deum"],
  "È una lauda dialogata in volgare umbro con latinismi.", "con Jacopone da Todi e con lo Stabat Mater")
L("ita-205", "Letteratura", 4, "Chi diffuse in Toscana la lirica della Scuola siciliana?",
  "Guittone d'Arezzo", ["Brunetto Latini", "Cecco Angiolieri", "Guido Cavalcanti"],
  "Guittone ne trasse spunti linguistici e poetici.", "principalmente a opera di Guittone d'Arezzo")
L("ita-206", "Letteratura", 3, "Chi è considerato l'iniziatore del «dolce stil novo»?",
  "Il bolognese Guido Guinizelli", ["Dante Alighieri", "Cino da Pistoia", "Francesco Petrarca"],
  "Tra gli altri stilnovisti: Guido Cavalcanti, Dante, Cino da Pistoia, Lapo Gianni.", "L'iniziatore di questa scuola fu il bolognese Guido Guinizelli")
L("ita-207", "Letteratura", 3, "Quali sono i due poeti più significativi della poesia comico-realistica?",
  "Cecco Angiolieri e Folgore da San Gimignano", ["Guinizelli e Cavalcanti", "Petrarca e Boccaccio", "Jacopone e Bonaventura"],
  "La corrente esalta denaro, gioco e taverna, in opposizione alla lirica cortese.", "furono Cecco Angiolieri, Folgóre da San Gimignano")
L("ita-208", "Letteratura", 3, "A chi Marco Polo dettò il Milione, e in quale lingua?",
  "A Rustichello da Pisa, in francese", ["A Brunetto Latini, in latino", "A Dante, in volgare toscano", "A Boccaccio, in veneziano"],
  "Il francese era allora diffuso come lingua letteraria.", "al Milione che Marco Polo dettò a Rustichello da Pisa in francese")
L("ita-209", "Letteratura", 2, "In che data Petrarca incontrò Laura, secondo la tradizione?",
  "Il 6 aprile 1327", ["Il 25 dicembre 1300", "Il 14 settembre 1321", "Il 1° gennaio 1348"],
  "Da questo amore nacquero molte liriche del Canzoniere.", "Il 6 aprile del 1327 incontrò una giovane donna di nome Laura")
L("ita-210", "Letteratura", 3, "Chi è considerato il «padre spirituale» dell'Umanesimo?",
  "Francesco Petrarca", ["Dante Alighieri", "Lorenzo Valla", "Angelo Poliziano"],
  "Petrarca desiderava conoscere gli antichi e recuperarne le opere dimenticate.", "può infatti essere considerato il \"padre spirituale\" dell'Umanesimo")
L("ita-211", "Letteratura", 3, "In quale anno la peste uccise Laura e il cardinale Colonna, protettore di Petrarca?",
  "Nel 1348", ["Nel 1327", "Nel 1374", "Nel 1300"],
  "È la grande peste nera descritta anche da Boccaccio.", "Era infatti scoppiata nel 1348 la peste")
L("ita-212", "Letteratura", 3, "Dove nacque Giovanni Boccaccio, secondo i critici?",
  "A Certaldo", ["A Firenze", "A Napoli", "Ad Arezzo"],
  "A dodici anni fu mandato a Napoli per imparare la mercatura.", "Giovanni nacque, come concordano i critici contemporanei, a Certaldo")
L("ita-213", "Letteratura", 4, "Quale opera di Boccaccio, in 473 ottave, racconta una favola sulle origini di Fiesole e Firenze?",
  "Il Ninfale fiesolano", ["Il Corbaccio", "La Caccia di Diana", "Il Filocolo"],
  "È l'ultima opera composta prima del Decameron.", "in 473 ottave dal titolo il Ninfale fiesolano")
L("ita-214", "Letteratura", 3, "Quale scrittore del Seicento scrisse l'Istoria del concilio tridentino, messa all'Indice?",
  "Il frate veneziano Paolo Sarpi", ["Daniello Bartoli", "Galileo Galilei", "Tommaso Campanella"],
  "Fu edita a Londra nel 1619.", "l'Istoria del concilio tridentino del frate veneziano Paolo Sarpi")
L("ita-215", "Letteratura", 2, "Quale filosofo fu arso vivo per le sue idee, mentre Galileo fu costretto ad abiurare?",
  "Giordano Bruno", ["Tommaso Campanella", "Paolo Sarpi", "Pico della Mirandola"],
  "Le loro idee furono considerate eretiche dalla Chiesa controriformista.", "Bruno verrà arso vivo")
L("ita-216", "Letteratura", 3, "Chi scrisse il saggio «Dei delitti e delle pene», contro la pena di morte?",
  "Cesare Beccaria", ["Pietro Verri", "Giambattista Vico", "Gaetano Filangieri"],
  "Fu tra i protagonisti dell'Illuminismo milanese.", "Cesare Beccaria, autore del famoso saggio Dei delitti e delle pene")
L("ita-217", "Letteratura", 3, "Chi fondò l'Accademia dell'Arcadia a Roma nel 1690?",
  "Giovanni Vincenzo Gravina e Giovanni Mario Crescimbeni", ["Pietro Metastasio e Carlo Goldoni", "Pietro e Alessandro Verri", "Giuseppe Parini e Vittorio Alfieri"],
  "L'Arcadia promosse l'anti-barocchismo e la restaurazione classicistica.", "da Giovanni Vincenzo Gravina e da Giovanni Mario Crescimbeni")
L("ita-218", "Letteratura", 3, "Quali sono le parti originarie del poemetto «Il Giorno» di Parini?",
  "Mattino, Mezzogiorno e Sera", ["Alba, Meriggio e Tramonto", "Inverno, Primavera ed Estate", "Infanzia, Giovinezza e Vecchiaia"],
  "Il poemetto, in endecasillabi sciolti, satireggia l'aristocrazia decaduta.", "Il poemetto era inizialmente diviso in tre parti: Mattino, Mezz")
L("ita-219", "Letteratura", 3, "A quale romanzo europeo si ispirano le «Ultime lettere di Jacopo Ortis» di Foscolo?",
  "I dolori del giovane Werther di Goethe", ["Il rosso e il nero di Stendhal", "Robinson Crusoe di Defoe", "I miserabili di Hugo"],
  "Foscolo ne converte la vicenda nel gusto patriottico italiano.", "Ispirato a \"I dolori del giovane Werther\" di Goethe")
L("ita-220", "Letteratura", 3, "Quante redazioni dei Promessi sposi scrisse Manzoni, e quale è detta «quarantana»?",
  "Tre; la quarantana è quella del 1840", ["Due; la quarantana è del 1827", "Una sola, del 1840", "Quattro; la quarantana è del 1823"],
  "La prima è del 1823 con titolo diverso, la «ventisettana» del 1827.", "e l'ultima nel 1840, la \"quarantana\"")
L("ita-221", "Letteratura", 3, "Di quale illuminista Alessandro Manzoni era nipote?",
  "Cesare Beccaria", ["Pietro Verri", "Giuseppe Parini", "Vittorio Alfieri"],
  "Nelle opere giovanili di Manzoni è presente il pensiero illuminista.", "essendo nipote di Cesare Beccaria")
L("ita-222", "Letteratura", 3, "Quale romanzo di Verga è il secondo del «ciclo dei Vinti»?",
  "Mastro-don Gesualdo (1888)", ["I Malavoglia", "Storia di una capinera", "Vita dei campi"],
  "Il primo è I Malavoglia (1881).", "Mastro-don Gesualdo (1888)")
L("ita-223", "Letteratura", 3, "Qual è l'opera più famosa di Federico De Roberto?",
  "I Viceré", ["Il marchese di Roccaverdina", "Piccolo mondo antico", "Canne al vento"],
  "È ambientata nella Sicilia della seconda metà dell'Ottocento.", "La sua opera più famosa è I Viceré")
L("ita-224", "Letteratura", 3, "Chi fu la prima donna italiana a fondare e dirigere un giornale (Il Mattino)?",
  "Matilde Serao", ["Grazia Deledda", "Sibilla Aleramo", "Ada Negri"],
  "È tra le autrici del verismo e del secondo Ottocento.", "Matilde Serao, la prima donna italiana a fondare e dirigere un giornale")
L("ita-225", "Letteratura", 2, "Chi è l'autore di «Le avventure di Pinocchio» (1883)?",
  "Carlo Collodi", ["Edmondo De Amicis", "Emilio Salgari", "Gianni Rodari"],
  "Il libro ha venduto circa 80 milioni di copie.", "Lo scrittore e umorista toscano Carlo Collodi è il padre di Pinocchio")
L("ita-226", "Letteratura", 2, "Chi è il più noto romanziere italiano di avventura, autore de «Le tigri di Mompracem»?",
  "Emilio Salgari", ["Carlo Collodi", "Antonio Fogazzaro", "Italo Calvino"],
  "Fu giudicato negativamente dai critici contemporanei e rivalutato in seguito.", "Emilio Salgari, vissuto a Verona e Torino, è il più noto romanziere italiano di avventura")
L("ita-227", "Letteratura", 3, "Chi è l'autore di «Piccolo mondo antico»?",
  "Antonio Fogazzaro", ["Federico De Roberto", "Luigi Capuana", "Giovanni Verga"],
  "Opera del secondo Ottocento.", "Antonio Fogazzaro (Piccolo mondo antico)")
L("ita-228", "Letteratura", 3, "Quale romanzo di Pirandello anticipa soluzioni metanarrative?",
  "Il fu Mattia Pascal", ["La coscienza di Zeno", "Senilità", "Il piacere"],
  "Pirandello è anche autore di «Uno, nessuno e centomila» e delle «Novelle per un anno».", "con Il fu Mattia Pascal")
L("ita-229", "Letteratura", 3, "Come si chiama la corrente letteraria creata da Luigi Pirandello?",
  "Umorismo", ["Verismo", "Ermetismo", "Futurismo"],
  "Da qui l'aggettivo «pirandelliano» per situazioni strane o tragicomiche.", "definita come \"umorismo\"")
L("ita-230", "Letteratura", 4, "Quali autori furono scoperti tardi, Svevo grazie a James Joyce e Tozzi decenni dopo la morte?",
  "Italo Svevo e Federigo Tozzi", ["Pascoli e D'Annunzio", "Montale e Ungaretti", "Gozzano e Corazzini"],
  "La critica del primo Novecento non comprese molti grandi autori.", "due casi emblematici sono quelli di Italo Svevo e di Federigo Tozzi")
L("ita-231", "Letteratura", 3, "Chi fondò nel 1908 la rivista «La Voce»?",
  "Giuseppe Prezzolini e Giovanni Papini", ["Filippo Tommaso Marinetti", "Benedetto Croce", "Pietro Verri"],
  "Fu una delle più importanti riviste culturali italiane del Novecento.", "Nel 1908 fu fondata, da Giuseppe Prezzolini e Giovanni Papini, La Voce")
L("ita-232", "Letteratura", 3, "Quale critico definì «crepuscolari» un gruppo di poeti del primo Novecento?",
  "Giuseppe Antonio Borgese", ["Francesco Flora", "Benedetto Croce", "Natalino Sapegno"],
  "Il nome richiama il gusto per la penombra e i toni smorzati.", "Crepuscolari fu l'aggettivo con cui il critico Giuseppe Antonio Borgese")
L("ita-233", "Letteratura", 3, "Da quale dio greco deriva il termine «ermetismo»?",
  "Hermes (Mercurio per i Romani)", ["Apollo", "Dioniso", "Zeus"],
  "Indica una poesia dal linguaggio difficile e talvolta misterioso.", "il termine è derivato dal nome del dio greco Hèrmes")
L("ita-234", "Letteratura", 4, "Dove si costituì nell'ottobre 1963 la neoavanguardia del «Gruppo 63»?",
  "A Palermo", ["A Milano", "A Roma", "A Firenze"],
  "Tra gli esponenti: Umberto Eco, Nanni Balestrini, Edoardo Sanguineti.", "Gruppo 63 costituitosi a Palermo nell'ottobre di quell'anno")
L("ita-235", "Letteratura", 3, "Quale rivista fiorentina del periodo fascista ospitò autori come Montale e Gadda?",
  "Solaria", ["Il Caffè", "La Voce", "Lacerba"],
  "Le riviste fiorentine mantennero vivo il confronto letterario.", "come Solaria, alla quale collaboravano autori quali Eugenio Montale")
L("ita-236", "Letteratura", 4, "Quale romanzo barocco il critico Giovanni Getto indicò come il manoscritto «trovato» da Manzoni?",
  "Historia del cavalier perduto di Pace Pasini", ["Del cane di Diogene di Frugoni", "L'Adone di Marino", "La Secchia rapita di Tassoni"],
  "Il romanzo è del 1634.", "Historia del cavalier perduto (1634) di Pace Pasini")

GR("ita-237", "Morfologia", 2, "Qual è la differenza d'uso tra articolo indeterminativo e determinativo?",
  "L'indeterminativo introduce un'informazione nuova, il determinativo una già data", ["Non c'è differenza", "Il determinativo si usa solo al plurale", "L'indeterminativo si usa solo con i nomi propri"],
  "Es. «ho visto un cerbiatto» / «il cerbiatto è già sparito».", "Gli indeterminativi hanno inoltre la proprietà di introdurre un'informazione nuova")
GR("ita-238", "Morfologia", 2, "Quale articolo si usa davanti a «zaino»?",
  "lo", ["il", "l'", "la"],
  "«lo» si usa davanti a z, gn, x, ps, s impura e i semiconsonante.", "il suo zaino lo zaino")
GR("ita-239", "Morfologia", 3, "Quale articolo indeterminativo si usa davanti a «gnomo»?",
  "uno", ["un", "un'", "una"],
  "Come per l'articolo «lo», si usa «uno» davanti a gn, z, ps, x, s impura.", "uno (davanti prima tema invariabile comune ad una famiglia lessicale")
GR("ita-240", "Morfologia", 3, "Esiste in italiano un articolo indeterminativo plurale?",
  "No: si usa il partitivo (dei, degli, delle) o un indefinito", ["Sì: «uni» e «une»", "Sì: «gli un»", "Sì, ma solo nei testi antichi"],
  "Es. «dei libri», «alcuni libri».", "Non esiste una forma plurale vera e propria")
GR("ita-241", "Morfologia", 3, "In base a cosa si sceglie la forma dell'articolo?",
  "In base al suono iniziale della parola immediatamente successiva", ["In base al sostantivo a cui si riferisce, anche se lontano", "In base al verbo", "Liberamente"],
  "Es. «lo specchio» ma «il bello specchio».", "La scelta dell'articolo è effettuata in base al suono iniziale della parola immediatamente successiva")
GR("ita-242", "Morfologia", 3, "Quale posizione hanno gli aggettivi di colore, forma o nazionalità rispetto al nome?",
  "Seguono sempre il sostantivo", ["Lo precedono sempre", "Possono stare ovunque", "Si mettono dopo il verbo"],
  "Es. «una penna rossa», «un vino francese».", "quelli che indicano colore, forma o nazionalità seguono sempre il sostantivo")
GR("ita-243", "Morfologia", 3, "Che differenza c'è tra «una bella casa» e «una casa bella»?",
  "Nel secondo caso l'aggettivo distingue quella casa dalle altre", ["Nessuna", "Il primo è scorretto", "Il secondo indica una casa piccola"],
  "L'aggettivo posposto ha funzione distintiva.", "una bella casa (aggettivo caratterizzante), una casa bella")
GR("ita-244", "Morfologia", 2, "Qual è il plurale di «la virtù»?",
  "le virtù", ["le virtui", "le virtue", "i virtù"],
  "I nomi che terminano con vocale accentata sono invariabili.", "la virtù / le virtù, il re / i re")
GR("ita-245", "Morfologia", 3, "Come si chiamano i sostantivi privi della forma singolare o plurale, come «le nozze»?",
  "Difettivi", ["Invariabili", "Sovrabbondanti", "Collettivi"],
  "Gli invariabili hanno invece singolare e plurale identici.", "Sostantivi privi della forma singolare o della forma plurale vengono detti difettivi")
GR("ita-246", "Morfologia", 2, "Qual è il plurale di «poeta»?",
  "poeti", ["poete", "poetas", "poeta"],
  "I maschili in -a fanno il plurale in -i.", "poeta, poeti")
GR("ita-247", "Morfologia", 2, "Qual è il plurale di «la crisi»?",
  "le crisi", ["le crise", "le crisis", "i crisi"],
  "I nomi in -i non accentata sono invariabili.", "la crisi / le crisi")
GR("ita-248", "Morfologia", 2, "Quale forma è corretta?",
  "le penne rosa", ["le penne rose", "le penne rosee", "le penne rosi"],
  "Alcuni aggettivi di colore (rosa, blu, viola) sono invariabili.", "la penna rosa - le penne rosa")
GR("ita-249", "Morfologia", 3, "Quale frase è corretta?",
  "Mio padre è medico", ["Il mio padre è medico", "Lo mio padre è medico", "Padre mio il è medico"],
  "Davanti ai nomi di parentela singolari con il possessivo (tranne «loro») l'articolo si omette.", "L'articolo si omette davanti ai nomi di parentela preceduti da un aggettivo possessivo che non sia \"loro\"")
GR("ita-250", "Morfologia", 3, "Quale forma è corretta?",
  "il loro padre", ["loro padre il", "lo loro padre", "il padre di loro sua"],
  "Con «loro» l'articolo si mantiene anche davanti ai nomi di parentela.", "ma: il loro padre, la loro madre")
GR("ita-251", "Morfologia", 3, "Cosa indica il dimostrativo «codesto»?",
  "Un oggetto vicino a chi ascolta", ["Un oggetto vicino a chi parla", "Un oggetto lontano da entrambi", "Un oggetto già nominato"],
  "«questo» = vicino a chi parla, «quello» = lontano da chi parla.", "vicino a chi parla, lontano da chi parla e vicino a chi ascolta")
GR("ita-252", "Morfologia", 3, "In «Mi piace questa musica», «mi» è un pronome:",
  "atono (clitico)", ["tonico", "riflessivo", "relativo"],
  "In «A me piace questa musica», «me» è tonico.", "Mi piace questa musica A me piace questa musica")
GR("ita-253", "Morfologia", 4, "A chi si riferiscono «egli» ed «ella»?",
  "Solo a persone", ["Solo ad animali", "A cose e animali", "A persone, animali e cose indistintamente"],
  "Lui, lei e loro si riferiscono a persone o animali e talvolta a cose.", "Egli ed ella si riferiscono solo a persone")
GR("ita-254", "Morfologia", 2, "In italiano il pronome personale soggetto è obbligatorio?",
  "No, è facoltativo e spesso omesso", ["Sì, sempre", "Solo alla terza persona", "Solo nelle domande"],
  "Si esprime per enfasi o per evitare ambiguità, a differenza di inglese e francese.", "il pronome personale soggetto in italiano è facoltativo e viene sovente omesso")
GR("ita-255", "Morfologia", 3, "Quale ausiliare si usa per i tempi composti dei verbi transitivi in forma attiva?",
  "Avere", ["Essere", "Venire", "Andare"],
  "Essere si usa per la maggior parte degli intransitivi, per il passivo e per il riflessivo.", "Il verbo ausiliare è avere nelle frasi attive quando il verbo è transitivo")
GR("ita-256", "Verbi", 3, "In una frase passiva, quale verbo può sostituire «essere» per esprimere un obbligo (es. «la domanda va presentata»)?",
  "Andare", ["Venire", "Stare", "Avere"],
  "«Venire» si usa invece per enfatizzare l'azione, solo nei tempi semplici.", "viene sostituito da andare quando la frase esprime un obbligo od una prescrizione")
GR("ita-257", "Verbi", 3, "A quale coniugazione appartengono tradizionalmente «fare» e «dire»?",
  "Alla seconda, perché derivano da facĕre e dicĕre", ["Alla prima e alla terza", "Alla terza", "Sono senza coniugazione"],
  "Benché escano in -are e -ire.", "I verbi fare e dire, benché uscenti rispettivamente in -are e -ire, vengono spesso considerati facenti parte della 2a coniugazione")
GR("ita-258", "Verbi", 3, "Come si chiamano i verbi come «capire» che inseriscono -isc- (capisco)?",
  "Incoativi", ["Servili", "Fraseologici", "Difettivi"],
  "In italiano l'interfisso -isc- non ha valore semantico.", "vengono detti, forse impropriamente, verbi incoativi")
GR("ita-259", "Verbi", 4, "Quale tempo dell'indicativo si forma con passato remoto + participio passato?",
  "Il trapassato remoto", ["Il trapassato prossimo", "Il passato prossimo", "Il futuro anteriore"],
  "Il trapassato prossimo si forma con l'imperfetto dell'ausiliare.", "trapassato remoto (passato remoto+pp)")
GR("ita-260", "Verbi", 3, "Quale tempo dell'indicativo può esprimere una supposizione sul presente (es. «Sarà stanco»)?",
  "Il futuro semplice", ["Il passato remoto", "L'imperfetto", "Il trapassato prossimo"],
  "Il futuro anteriore indica invece una supposizione su un fatto già compiuto.", "come forma che indica delle supposizioni, anche sul presente")
GR("ita-261", "Verbi", 4, "«Credevo che la via ___ dritta»: quale forma esprime contemporaneità nel passato?",
  "fosse", ["sia", "sarà", "sia stata"],
  "Concordanza dei tempi: principale al passato → congiuntivo imperfetto.", "Credevo che la via fosse dritta")
GR("ita-262", "Verbi", 4, "«Immaginavo che il bimbo ___ buono»: quale forma esprime posteriorità rispetto al passato?",
  "sarebbe stato", ["fosse", "sarà", "sia"],
  "Si usa il condizionale passato (futuro nel passato).", "Immaginavo che il bimbo sarebbe stato buono")
GR("ita-263", "Verbi", 3, "Come si chiama l'insieme delle regole sul rapporto tra i tempi della principale e della subordinata?",
  "Consecutio temporum (concordanza dei tempi)", ["Periodo ipotetico", "Analisi logica", "Diatesi"],
  "È un'eredità della grammatica latina.", "la consecùtio tèmporum")
GR("ita-264", "Verbi", 3, "Quale forma usa l'imperativo per la terza persona (es. «Signora, mi guardi!»)?",
  "Il congiuntivo esortativo", ["L'indicativo presente", "L'infinito", "Il condizionale"],
  "In questo caso il pronome atono è anteposto.", "viene usata la corrispondente voce del congiuntivo (congiuntivo esortativo)")
GR("ita-265", "Morfologia", 2, "Quali parti del discorso esprimono l'espressione affettiva del parlante (ah, oh, ahi)?",
  "Le interiezioni", ["Le congiunzioni", "Le preposizioni", "Gli avverbi di luogo"],
  "Sono invariabili e non hanno un ruolo particolare nel costrutto della frase.", "Le interiezioni, che denotano l'espressione affettiva del parlante")
GR("ita-266", "Morfologia", 2, "Che tipo di avverbio è «volentieri»?",
  "Di modo", ["Di tempo", "Di luogo", "Di quantità"],
  "Di modo: bene, male, volentieri; di tempo: ieri, adesso.", "di modo (bene, male, volentieri)")

D("ita-267", "Morfologia", 3, "Da quale parola latina deriva «articolo»?",
  "Articulus, da artus, «membro, arto»", ["Ars, «arte»", "Articulare, «parlare»", "Arcus, «arco»"],
  "In greco antico è árthron.", W("Articolo (linguistica)"), ART, "dal latino articulus, da artus")
D("ita-268", "Morfologia", 3, "In quale lingua l'articolo determinativo è un suffisso enclitico, come in «omul» (l'uomo)?",
  "Il rumeno", ["L'italiano", "Lo spagnolo", "Il francese"],
  "Anche nelle lingue scandinave il determinativo è un suffisso.", W("Articolo (linguistica)"), ART, "omul, in rumeno \"l'uomo\"")
D("ita-269", "Morfologia", 3, "Quale di queste lingue NON usa articoli?",
  "Il latino", ["Il greco", "Lo spagnolo", "Il tedesco"],
  "L'articolo è assente anche in giapponese e cinese.", W("Articolo (linguistica)"), ART, "L'articolo è assente nel latino, nel giapponese e nel cinese")
D("ita-270", "Morfologia", 2, "Quale nome di città ha l'articolo come parte integrante?",
  "L'Aquila", ["Roma", "Milano", "Firenze"],
  "Così anche La Spezia, Il Cairo, La Mecca, L'Aia.", W("Articolo (linguistica)"), ART, "La Spezia, L'Aquila, Il Cairo")
D("ita-271", "Morfologia", 3, "Da quale parola latina derivano per lo più gli articoli romanzi?",
  "Dal dimostrativo ille, illa", ["Da unus", "Da hic, haec", "Da is, ea"],
  "In sardo derivano invece da ipsum, ipsam.", W("Articolo (linguistica)"), ART, "Derivano per lo più dal dimostrativo latino ille, illa")
D("ita-272", "Morfologia", 3, "Nelle frasi proverbiali come «can che abbaia non morde» l'articolo:",
  "si omette", ["è obbligatorio", "si raddoppia", "diventa partitivo"],
  "Si omette anche nei titoli e nel linguaggio telegrafico.", W("Articolo (linguistica)"), ART, "nelle frasi proverbiali (buon vino fa buon sangue, can che abbaia non morde)")
D("ita-273", "Morfologia", 4, "Con quali nomi propri si può usare l'articolo in registro familiare-affettivo?",
  "Con i nomi propri femminili (es. «la Maria»), non con i maschili", ["Con tutti i nomi propri", "Solo con i maschili", "Mai"],
  "L'uso è regionale e colloquiale.", W("Articolo (linguistica)"), ART, "Può inoltre essere usato davanti ai nomi propri femminili")
D("ita-274", "Morfologia", 3, "In «abito da sera», «sala da pranzo», l'articolo:",
  "è omesso", ["è obbligatorio", "è sempre determinativo", "si unisce alla preposizione"],
  "Quando un sostantivo integra il significato di un altro, l'articolo non si usa.", W("Articolo (linguistica)"), ART, "carte da gioco, sala da pranzo, abito da sera")

VRB = "Wikipedia_Verbo.txt"
D("ita-275", "Verbi", 1, "Da quale parola latina deriva «verbo»?",
  "Verbum, «parola»", ["Vertere, «girare»", "Vir, «uomo»", "Verus, «vero»"],
  "Il verbo è una parte del discorso variabile.", W("Verbo"), VRB, "Il verbo (dal latino verbum, \"parola\")")
D("ita-276", "Verbi", 3, "Cosa esprime la diatesi del verbo?",
  "Il rapporto del verbo con il soggetto o l'oggetto (attiva, passiva, riflessiva)", ["Il tempo dell'azione", "La persona del soggetto", "Il modo verbale"],
  "Può essere attiva, passiva, riflessiva o media.", W("Verbo"), VRB, "La diatesi esprime il rapporto del verbo con il soggetto o l'oggetto")
D("ita-277", "Verbi", 4, "«Scrivo» e «Sto scrivendo» sono entrambe al presente. Cosa le distingue?",
  "L'aspetto: durativo il primo, progressivo il secondo", ["Il modo", "La diatesi", "La persona"],
  "L'aspetto riguarda durata, momentaneità e compiutezza dell'azione.", W("Verbo"), VRB, "ma la prima ha aspetto durativo, la seconda progressivo")
D("ita-278", "Verbi", 4, "Quale filosofo definì il verbo come la forma che «aggiunge al suo significato il tempo»?",
  "Aristotele", ["Platone", "Cicerone", "Dante"],
  "Lo fa nel De Interpretatione.", W("Verbo"), VRB, "Già Aristotele aveva evidenziato, nel De Interpretatione")
D("ita-279", "Verbi", 3, "Quale frase è corretta?",
  "Io mi nutro", ["Io mi cibo (senza altro)", "Io mi nutrisco di", "Io mi cibo da solo"],
  "«Cibarsi» richiede l'indicazione del cibo: «mi cibo di broccoli».", W("Verbo"), VRB, "La forma corretta è \"io mi nutro\"")
D("ita-280", "Verbi", 4, "Come si chiamano gli elementi della frase che non possono essere eliminati senza renderla agrammaticale?",
  "Elementi nucleari (argomenti)", ["Elementi circostanziali", "Apposizioni", "Interiezioni"],
  "Gli elementi circostanziali (luogo, tempo, causa) si possono invece eliminare.", W("Verbo"), VRB, "sono detti elementi \"nucleari\"")
D("ita-281", "Verbi", 4, "In «Domani vedremo chi ha avuto ragione», il passato prossimo si riferisce a:",
  "un evento futuro", ["un evento remoto", "un'abitudine passata", "un ordine"],
  "Il tempo grammaticale non coincide sempre con quello reale.", W("Verbo"), VRB, "Domani vedremo chi ha avuto ragione")

D("ita-282", "Fonetica", 3, "In «pàusa», il nesso «au» è:",
  "un dittongo discendente", ["uno iato", "un dittongo ascendente", "un trittongo"],
  "Nei dittonghi discendenti l'accento è sul primo elemento.", W("Dittongo"), DIT, "/au/ come in pàusa")
D("ita-283", "Fonetica", 3, "In «piàno», il nesso «ia» è:",
  "un dittongo ascendente", ["un dittongo discendente", "uno iato", "una vocale lunga"],
  "Tradizionalmente chiamato «falso dittongo».", W("Dittongo"), DIT, "/ja/ come in piàno")
D("ita-284", "Fonetica", 3, "In «zìo» le due vocali formano:",
  "uno iato", ["un dittongo", "un trittongo", "una sillaba sola"],
  "Quando la i è tonica si ha iato.", W("Dittongo"), DIT, "/ˈio/ come in zìo")
D("ita-285", "Fonetica", 4, "Quali sono i «dittonghi mobili» dell'italiano?",
  "ie e uo", ["ai e au", "ia e io", "ei e eu"],
  "Derivano dalle vocali brevi latine e ed o (es. uomo, piede).", W("Dittongo"), DIT, "In italiano ci sono due nessi /ie, uo/")
D("ita-286", "Fonetica", 3, "In «cielo» e «scienza», la i dopo c e sc:",
  "è un segno grafico che non va pronunciato", ["forma un dittongo", "forma uno iato", "indica l'accento"],
  "È un residuo etimologico.", W("Dittongo"), DIT, "la i è seguita da una e ed è quindi un segno grafico che non va pronunciato")
D("ita-287", "Fonetica", 4, "In metrica, quale segno indica che due vocali vanno pronunciate separate (dieresi)?",
  "I due puntini sulla prima vocale (dieresi)", ["L'accento grave", "L'apostrofo", "Il trattino"],
  "Altrimenti in poesia ogni coppia di vocali è considerata dittongo.", W("Dittongo"), DIT, "a meno che il poeta non ponga la dieresi sulla prima vocale grafica")

D("ita-288", "Punteggiatura", 3, "In quale antica iscrizione compaiono i primi segni che indicano pause nel discorso?",
  "Nella stele di Mesha dei Moabiti (IX sec. a.C.)", ["Nella stele di Rosetta", "Nelle Dodici Tavole", "Nel Codice di Hammurabi"],
  "Greci e Romani usarono poi punti variamente disposti.", W("Punteggiatura"), PUN, "nella stele di Mesha dei Moabiti")
D("ita-289", "Punteggiatura", 3, "Da quale parola latina deriverebbe il punto interrogativo?",
  "Quaestio, «domanda»", ["Quare, «perché»", "Quis, «chi»", "Quid, «che cosa»"],
  "La «q» si spostò sopra la «o», che divenne un punto.", W("Punteggiatura"), PUN, "\"q\" ed \"o\" di quaestio (\"domanda\")")
D("ita-290", "Punteggiatura", 3, "Secondo l'Enciclopedia dell'italiano Treccani, punto e virgola e due punti sono:",
  "pause intermedie", ["pause fortissime", "segni senza valore di pausa", "segni di intonazione"],
  "Il punto è pausa forte e chiusa, la virgola debole e aperta.", W("Punteggiatura"), PUN, "Secondo l'Enciclopedia dell'italiano Treccani sono pause intermedie")
D("ita-291", "Punteggiatura", 4, "Come si chiamano in francese le virgolette basse « »?",
  "Guillemets", ["Caporali", "Apici", "Doppi accenti"],
  "In francese richiedono uno spazio che le separi dal testo.", W("Punteggiatura"), PUN, "dette guillemets")
D("ita-292", "Punteggiatura", 4, "Chi propose una serie di sei nuovi segni di punteggiatura, tra cui il «punto d'ironia»?",
  "Hervé Bazin", ["Martin K. Speckter", "Francesco Flora", "Umberto Eco"],
  "Lo fece nel libro «Plumons l'Oiseau».", W("Punteggiatura"), PUN, "è un libro del francese Hervé Bazin")
D("ita-293", "Punteggiatura", 3, "Quale studioso affermò che i moderni tendono «con ragione a diradare i troppi segni di interpunzione»?",
  "Francesco Flora", ["Benedetto Croce", "Alessandro Manzoni", "Gianfranco Contini"],
  "Aggiunse che talvolta li aboliscono per raffinatezza o per ignoranza.", W("Punteggiatura"), PUN, "i moderni tendono con ragione a diradare i troppi segni di interpunzione")

GR("ita-294", "Morfologia", 3, "Quale forma della preposizione articolata con «con» è ancora frequente anche nello scritto?",
  "col e coi", ["colla e colle", "cogli", "collo"],
  "Le altre forme con «con» sono tendenzialmente desuete.", "ad eccezione di col e coi che sono a tutt'oggi frequenti anche nello scritto")
GR("ita-295", "Morfologia", 4, "Quali preposizioni articolate con «per», ancora usate in registro elevato o burocratico, sopravvivono?",
  "pel e pei", ["pello e pella", "perlo e perla", "pegli e pelle"],
  "Le altre forme non sono in uso dalla prima metà del Novecento.", "di esse sopravvivono soprattutto pel e pei")
GR("ita-296", "Verbi", 3, "Nel passivo, quale verbo può sostituire «essere» nei tempi semplici per enfatizzare l'azione (es. «la lettera viene spedita»)?",
  "Venire", ["Andare", "Stare", "Avere"],
  "«Andare» esprime invece obbligo o prescrizione («va spedita»).", "può essere sostituito da venire (coniugato nei soli tempi semplici) per enfatizzare l'azione")
GR("ita-297", "Verbi", 3, "Come si forma il condizionale passato?",
  "Condizionale presente dell'ausiliare + participio passato (es. avrei parlato)", ["Condizionale presente + gerundio", "Imperfetto + participio", "Futuro + infinito"],
  "Il condizionale presente è il tempo semplice.", "io avrei parlato, io sarei caduto")
GR("ita-298", "Verbi", 3, "Qual è la desinenza del participio presente dei verbi in -are?",
  "-ante (es. parlante)", ["-ente", "-ando", "-ato"],
  "Per -ere e -ire: -ente (o -iente).", "presente -ante -ente -ente / -iente")
GR("ita-299", "Verbi", 4, "Come si nega la seconda persona singolare dell'imperativo (es. «non parlare!»)?",
  "Con «non» + infinito", ["Con «non» + imperativo", "Con «no» + congiuntivo", "Con «mai» + gerundio"],
  "Es. «parla!» → «non parlare!».", "preceduto da non, come negazione della seconda persona singolare dell'imperativo presente")
GR("ita-300", "Verbi", 3, "In «vedo gli uccelli volare», l'infinito sostituisce:",
  "una proposizione relativa («che volano»)", ["una causale", "una temporale", "un complemento di luogo"],
  "Il soggetto della subordinata passa all'accusativo: «lo vedo volare».", "\"vedo gli uccelli volare\" = \"vedo gli uccelli che volano\"")
GR("ita-301", "Morfologia", 3, "Qual è il plurale di «l'auto»?",
  "le auto", ["le auti", "gli auti", "le autos"],
  "I sostantivi accorciati (auto da automobile) sono invariabili.", "l'auto, le auto")

# ── Verso 350: la lingua degli atti amministrativi, dalla «Guida alla redazione degli atti
#    amministrativi» di ITTIG-Cnr e Accademia della Crusca (2011, CC BY-ND 2.5 IT).
CRU = "ITTIG-Crusca_Guida-redazione-atti-amministrativi.txt"
FCRU = "ITTIG-Cnr e Accademia della Crusca, «Guida alla redazione degli atti amministrativi» (2011)"
def K(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, FCRU, CRU, frase)
SA = "Scrittura amministrativa"

K("ita-302", SA, 2, "Come devono essere i periodi di un atto amministrativo secondo la Guida ITTIG-Crusca?",
  "Brevi e chiari, con frasi preferibilmente semplici", ["Lunghi e articolati, per essere completi", "Ricchi di incisi tra parentesi", "Scritti al congiuntivo"],
  "Regola 2: formulare periodi brevi e chiari, usare preferibilmente frasi semplici, con poche subordinate.",
  "Formulare periodi brevi e chiari.")
K("ita-303", SA, 3, "Quale ordine delle parole raccomanda la Guida nelle frasi degli atti amministrativi?",
  "Soggetto, verbo, oggetto diretto, oggetto indiretto", ["Verbo, soggetto, oggetto", "Oggetto indiretto, soggetto, verbo", "Nessun ordine: è indifferente"],
  "Es.: «l'utente consegna il modulo Y al responsabile della procedura»; non si inseriscono elementi tra soggetto e verbo.",
  "l'ordine soggetto-verbooggetto diretto-oggetto indiretto")
K("ita-304", SA, 3, "Nel periodo, dove va collocata preferibilmente la frase principale?",
  "Prima delle subordinate", ["Dopo tutte le subordinate", "Tra parentesi", "In una nota"],
  "La frase principale precede, preferibilmente, le subordinate, che devono essere poche; gli incisi vanno evitati.",
  "Nei periodi la frase principale precede, preferibilmente, le frasi subordinate")
K("ita-305", SA, 3, "Perché la Guida consiglia di limitare gli incisi?",
  "Costringono il lettore a memorizzare troppi elementi prima di capire il periodo", ["Perché sono errori grammaticali", "Perché allungano la stampa", "Perché sono vietati dalla legge"],
  "Gli incisi e le frasi tra parentesi costringono il lettore a memorizzare troppi elementi prima di dare un senso al periodo.",
  "Evitare, se possibile, gli incisi.")
K("ita-306", SA, 3, "Quali frasi implicite la Guida invita a evitare in particolare?",
  "Quelle con il verbo al gerundio", ["Quelle con il verbo all'indicativo", "Quelle con il soggetto espresso", "Quelle brevi"],
  "Regola 3: preferire le frasi esplicite alle implicite, evitando in particolare le frasi con il gerundio, che possono essere ambigue.",
  "Evitare in particolare le frasi con il verbo al gerundio.")
K("ita-307", SA, 2, "A cosa servono connettivi come «dunque», «inoltre», «successivamente» in un testo?",
  "A rendere espliciti i nessi logici tra le frasi", ["Ad allungare il testo", "A sostituire la punteggiatura", "A indicare il destinatario"],
  "Avverbi e congiunzioni usati come connettivi testuali esplicitano i legami logico-grammaticali tra le frasi e danno coerenza e coesione al testo.",
  "Esplicitare i nessi logici tra le frasi con congiunzioni o avverbi testuali.")
K("ita-308", SA, 4, "In un atto, «A e B» esprime una relazione in cui la conseguenza si realizza:",
  "Solo quando si avverano tutti gli elementi", ["Quando se ne avvera almeno uno", "Quando se ne avvera uno solo", "Mai"],
  "La congiunzione «e» è riservata alle relazioni congiuntive: la fattispecie si realizza quando tutti gli elementi correlati si avverano.",
  "La congiunzione e è riservata alle relazioni congiuntive")
K("ita-309", SA, 3, "Quale formulazione la Guida invita a evitare, sostituendola con l'elencazione esplicita dei casi?",
  "«e/o»", ["«oppure»", "«se»", "«soltanto»"],
  "In particolare va evitata la formulazione «e/o», sostituibile con l'elenco esplicito dei casi in cui la relazione si realizza e non si realizza.",
  "evitare la formulazione e/o")
K("ita-310", SA, 4, "Con quali avverbi si esplicita il carattere tassativo di un'enumerazione?",
  "Soltanto, esclusivamente, unicamente", ["In particolare, tra l'altro", "Inoltre, altresì", "Ad esempio, come"],
  "Il carattere tassativo si esprime con soltanto, esclusivamente, unicamente; quello esemplificativo con in particolare, tra l'altro.",
  "Il carattere tassativo di una enumerazione si esplicita attraverso l'uso di avverbi quali soltanto, esclusivamente, unicamente.")
K("ita-311", SA, 4, "Con quali locuzioni si esplicita il carattere esemplificativo di un'enumerazione?",
  "In particolare, tra l'altro", ["Soltanto, unicamente", "Esclusivamente", "Né… né"],
  "Il carattere esemplificativo di un'enumerazione si esplicita con locuzioni come «in particolare», «tra l'altro».",
  "Il carattere esemplificativo di una enumerazione si esplicita attraverso l'uso di locuzioni quali in particolare, tra l'altro.")
K("ita-312", SA, 3, "Nella protasi del periodo ipotetico, quale congiunzione preferisce la Guida?",
  "«Se», più semplice di «nel caso in cui» o «qualora»", ["«Qualora»", "«Nel caso in cui»", "«Ove»"],
  "Esempio: «Se il bilancio non viene approvato» e non «nel caso in cui il bilancio non venga approvato».",
  "preferire la congiunzione se ad altre più complesse")
K("ita-313", SA, 4, "Quando la conseguenza giuridica può derivare solo da quel caso specifico, come va introdotta la protasi?",
  "Con «solo se» o espressioni equivalenti", ["Con «se» semplice", "Con «qualora»", "Con «anche se»"],
  "La protasi è introdotta da «se» quando la conseguenza può derivare anche da altri casi; da «solo se» quando deriva solo da quel caso.",
  "questa è introdotta da solo se")
K("ita-314", SA, 2, "Tra «è vietato l'ingresso» e «l'ingresso non è autorizzato», cosa preferisce la Guida?",
  "La frase affermativa «è vietato l'ingresso»", ["La frase negativa, più cortese", "Indifferentemente l'una o l'altra", "Nessuna delle due"],
  "Le frasi affermative sono più brevi, semplici e inequivoche; la negazione può far pensare a interpretazioni possibiliste.",
  "Preferire, quando è possibile, le frasi affermative a quelle negative.")
K("ita-315", SA, 2, "Cosa raccomanda la Guida riguardo alla doppia negazione (es. «non si può non esprimere»)?",
  "Di evitarla, perché rende la frase complessa e ambigua", ["Di usarla per enfasi", "Di usarla solo nelle delibere", "Di preferirla alla frase affermativa"],
  "La doppia negazione appesantisce la frase e aumenta il rischio di interpretazioni errate: meglio «si deve esprimere».",
  "Evitare le frasi con la doppia negazione.")
K("ita-316", "Verbi", 3, "Quale modo verbale la Guida preferisce al congiuntivo nelle costruzioni degli atti?",
  "L'indicativo", ["Il condizionale", "Il gerundio", "L'infinito"],
  "Regola 8: preferire costruzioni con l'indicativo: «se si verifica» e non «nel caso in cui si verifichi».",
  "Preferire costruzioni sintattiche che richiedono l'indicativo al posto del congiuntivo.")
K("ita-317", "Verbi", 4, "In «Il sindaco provvede alle nomine», che valore ha l'indicativo presente?",
  "Valore prescrittivo: equivale a «deve provvedere»", ["Valore descrittivo di un'abitudine", "Valore ipotetico", "Valore passato"],
  "L'indicativo presente può avere valore prescrittivo al posto di dovere + infinito.",
  "L'indicativo presente può essere usato con valore prescrittivo al posto del costrutto dovere + infinito.")
K("ita-318", SA, 4, "Cos'è la «nominalizzazione», da evitare negli atti?",
  "Preferire il nome al verbo come portatore di significato", ["Usare troppi nomi propri", "Scrivere i nomi in maiuscolo", "Elencare i nomi dei destinatari"],
  "Es.: invece di «Il pagamento si effettua allo sportello» scrivere «Si paga allo sportello».",
  "la nominalizzazione che consiste nel preferire il nome al verbo come portatore di significato")
K("ita-319", SA, 2, "Secondo la Guida, invece di «apporre la firma» è meglio scrivere:",
  "Firmare", ["Sottoscrivere in calce", "Procedere alla sottoscrizione", "Effettuare la firma"],
  "Vanno evitate le perifrasi come «apporre la firma» al posto del semplice «firmare».",
  "le perifrasi come apporre la firma anziché firmare")
K("ita-320", SA, 3, "Al posto di «trattasi», cosa suggerisce la Guida?",
  "«Si tratta»", ["«Trattasi di»", "«Tratta»", "«È trattato»"],
  "Va evitata l'enclisi del -si in stereotipi come trattasi e dicasi, ai quali sono preferibili «si tratta» e «si dica».",
  "stereotipi come trattasi e dicasi ai quali sono preferibili si tratta e si dica")
K("ita-321", "Verbi", 4, "Come si esprime di regola un obbligo in un atto, secondo la Guida?",
  "Con l'indicativo presente, senza il verbo «dovere»", ["Sempre con «deve»", "Con il condizionale «dovrebbe»", "Con l'imperativo"],
  "Es.: «La ditta attiva i seguenti provvedimenti» e non «La ditta deve attivare…»: l'indicativo presente ha già valore imperativo.",
  "non usare di regola il verbo dovere per indicare l'obbligatorietà di una disposizione")
K("ita-322", "Verbi", 3, "Per cosa si può usare il verbo «potere» negli atti?",
  "Per indicare una facoltà, non un obbligo", ["Per indicare un obbligo", "Per indicare un divieto assoluto", "Mai"],
  "Il verbo potere si usa per indicare una facoltà; se l'ufficio è tenuto a fare qualcosa si scrive «rilascia», non «può rilasciare».",
  "È possibile usare il verbo potere per indicare una facoltà")
K("ita-323", "Verbi", 2, "Quale forma del verbo la Guida invita a usare quando è possibile?",
  "La forma attiva", ["La forma passiva", "La forma impersonale", "La forma riflessiva"],
  "Regola 10: usare quando è possibile la forma attiva; passivo e impersonale solo quando non si può o non serve indicare chi agisce.",
  "Usare quando è possibile la forma attiva del verbo.")
K("ita-324", SA, 4, "Perché un'amministrazione scrive «Si prega di non fumare» con l'impersonale?",
  "Per creare un distacco con il destinatario e non essere troppo diretta nel divieto", ["Perché il fumo è consentito", "Perché manca il soggetto per errore", "Perché è obbligatorio per legge"],
  "L'impersonale può servire quando l'amministrazione vuole creare un distacco tra sé e il destinatario, ad esempio nell'esprimere un divieto.",
  "quando l'amministrazione vuole creare un distacco tra sé e il")
K("ita-325", SA, 3, "Se un pronome («esso», «questi») rende ambiguo il testo, cosa conviene fare?",
  "Ripetere il nome a cui ci si riferisce", ["Usare un altro pronome", "Toglierlo e lasciare la frase incompleta", "Metterlo tra parentesi"],
  "È preferibile ripetere gli elementi già introdotti piuttosto che usare pronomi che possono rendere ambigua la comprensione.",
  "È preferibile ripetere elementi che sono già stati introdotti")
K("ita-326", SA, 4, "Quante parole contiene, secondo le stime citate dalla Guida, il vocabolario di base dell'italiano?",
  "Da 7.000 a 10.000", ["Circa 500", "Circa 50.000", "Oltre 200.000"],
  "I dizionari dell'uso registrano 90-120.000 parole, il vocabolario comune circa la metà, il vocabolario di base da 7.000 a 10.000: sono quelle da preferire.",
  "Il vocabolario di base della lingua italiana contiene, a seconda delle valutazioni, da 7.000 a 10.000 parole")
K("ita-327", SA, 2, "Quale parola, più comune, la Guida preferisce a «obliterare»?",
  "Timbrare", ["Annullare", "Vidimare", "Convalidare"],
  "Bisogna evitare le parole ricercate: «timbrare» e non «obliterare»; «impedimento» e non «condizione ostativa».",
  "evitando quelle ricercate (timbrare e non obliterare)")
K("ita-328", SA, 2, "Secondo la Guida, quale parola è meglio usare al posto di «nominativo»?",
  "Nome", ["Nominale", "Denominazione", "Intestatario"],
  "Il linguaggio burocratico preferisce parole astratte e lunghe: meglio «problema» e non «problematica», «nome» e non «nominativo».",
  "È opportuno non usare problematica al posto di problema e nominativo al posto di nome.")
K("ita-329", SA, 4, "«Porre in essere» al posto di «realizzare» è un esempio di:",
  "Tecnicismo collaterale", ["Tecnicismo specifico necessario", "Forestierismo", "Neologismo"],
  "I tecnicismi collaterali non rispondono a necessità comunicative ma a uno stile ricercato (procedere all'escussione per interrogare; porre in essere per realizzare).",
  "porre in essere per realizzare")
K("ita-330", SA, 5, "Quanti tecnicismi davvero necessari ci sono in media in un testo amministrativo, secondo la Guida?",
  "Meno di cinque su cento parole", ["Circa la metà delle parole", "Almeno venti su cento", "Nessuno"],
  "In un testo di servizio o amministrativo i tecnicismi necessari sono in media meno di cinque su cento; vanno spiegati almeno la prima volta.",
  "in media sono meno di cinque su cento")
K("ita-331", SA, 3, "Quali di queste parole, arcaiche, la Guida invita a evitare negli atti?",
  "All'uopo, testé, altresì", ["Quindi, perciò, inoltre", "Se, quando, mentre", "Firmare, pagare, consegnare"],
  "Vanno limitati arcaismi e latinismi come all'uopo, testé, altresì, nonché, il pronome «Ella», la formula «addì», «de iure», «de facto».",
  "all'uopo, testé, altresì, nonché")
K("ita-332", SA, 2, "Quale parola italiana la Guida suggerisce al posto di «meeting»?",
  "Riunione", ["Incontro di staff", "Convention", "Briefing"],
  "Meglio evitare forestierismi come project manager (capo progetto), meeting (riunione), planning (piano), staff (personale).",
  "meeting per riunione")
K("ita-333", "Morfologia", 3, "Come si comporta al plurale una parola straniera entrata stabilmente nell'italiano (es. «computer»)?",
  "È invariabile: i computer", ["Prende la -s: i computers", "Prende la -i: i computeri", "Non si può usare al plurale"],
  "Regola 16: la parola straniera assunta stabilmente nella lingua italiana è invariabile.",
  "La parola straniera assunta stabilmente nella lingua italiana è invariabile.")
K("ita-334", "Morfologia", 3, "Quale forma la Guida considera non grammaticale?",
  "La sindaco", ["La sindaca", "La presidente", "L'assessora"],
  "Tutti i nomi di mestiere e ruolo possono avere il femminile (sindaca, assessora, segretaria generale); è da evitare l'articolo femminile con la forma maschile.",
  "l'uso dell'articolo femminile seguito dalla forma maschile, es. la sindaco")
K("ita-335", SA, 4, "Con destinatari non definiti, quale formulazione suggerisce la Guida al posto di «il/la responsabile»?",
  "«La persona responsabile»", ["«Il responsabile» soltanto", "«Il/la/le responsabile/i»", "«Responsabile (m/f)»"],
  "Per destinatari non definiti si usano formulazioni che non specificano il genere: la persona responsabile, la direzione, chi è incaricato di…",
  "la persona responsabile anziché il/la responsabile")
K("ita-336", SA, 3, "Per evitare ripetizioni, è bene alternare termini diversi per lo stesso concetto in un atto?",
  "No: si usa sempre lo stesso termine, anche a costo di ripetersi", ["Sì, per uno stile più elegante", "Sì, ma solo nelle delibere", "Sì, usando sinonimi stranieri"],
  "Regola 18: usare sempre il medesimo termine per uno stesso concetto; alternare termini diversi genera confusione e ambiguità.",
  "Usare sempre il medesimo termine per esprimere uno stesso concetto")
K("ita-337", "Ortografia", 3, "Come si introduce una sigla la prima volta che compare in un testo?",
  "Con l'espressione per intero seguita dalla sigla tra parentesi tonde", ["Solo con la sigla", "Con la sigla in grassetto", "In nota a piè di pagina"],
  "La prima volta si scrive l'espressione per intero con la sigla tra parentesi; poi basta la sigla, salvo sigle molto note.",
  "farla precedere dall'espressione per intero e racchiuderla tra parentesi tonde")
K("ita-338", "Ortografia", 4, "Perché l'abbreviazione «ca» (circa) non vuole il punto?",
  "Perché riporta la lettera iniziale e quella finale della parola", ["Perché è una sigla", "Perché è latina", "Per errore: il punto ci vuole sempre"],
  "Le abbreviazioni vogliono il punto, tranne quando riportano iniziale e finale (ca per circa) o chiudono la frase.",
  "se la parola abbreviata riporta la lettera iniziale e finale (ca per circa)")
K("ita-339", "Ortografia", 4, "Come si forma il plurale di alcune abbreviazioni, ad esempio di «vol.» (volume)?",
  "Raddoppiando la lettera finale: voll.", ["Aggiungendo la -s: vols.", "Aggiungendo -i: voli.", "Non hanno plurale"],
  "In molte abbreviazioni la forma è unica; in certi casi il plurale si esprime raddoppiando iniziali o finali (voll. per volumi).",
  "voll. per volumi")
K("ita-340", "Ortografia", 2, "Come si scrivono di norma sigle e acronimi come INPS o ONU?",
  "In maiuscolo e senza punti tra le lettere", ["Con i punti: I.N.P.S.", "In minuscolo", "In corsivo con i punti"],
  "Le lettere di sigle e acronimi non sono generalmente seguite dal punto e sono scritte maiuscole, salvo sigle entrate nel lessico comune (vip, radar).",
  "Le lettere di sigle e acronimi non sono generalmente seguite dal punto e sono scritte sempre maiuscole")
K("ita-341", "Ortografia", 4, "Perché si scrive «lo SNALS» anche se la sigla sta per «il Sindacato autonomo…»?",
  "Perché l'articolo segue la struttura fonetica della sigla", ["Per un errore diffuso", "Perché le sigle sono femminili", "Perché SNALS è una parola straniera"],
  "Di regola l'articolo segue genere e numero della denominazione completa, ma con sigle che iniziano per consonante può seguire la pronuncia: lo SNALS.",
  "lo SNALS")
K("ita-342", "Ortografia", 3, "Quale di queste parole va scritta con la maiuscola?",
  "Novecento (il secolo)", ["ottobre", "lunedì", "piazza (nell'indirizzo)"],
  "Hanno la maiuscola, tra l'altro, i nomi dei secoli e dei decenni (il Novecento, gli anni Venti); mesi, giorni e «via», «piazza» mai.",
  "il Novecento, gli anni Venti")
K("ita-343", "Ortografia", 4, "Perché si scrive «i Romani» con la maiuscola parlando dell'antichità?",
  "Per distinguere il popolo antico da quello moderno (i romani)", ["Perché tutti i popoli vogliono la maiuscola", "Per rispetto", "Non va mai con la maiuscola"],
  "Ha la maiuscola il nome di un popolo antico (i Romani) per distinguerlo dal moderno (i romani).",
  "di un popolo antico (es. i Romani) per distinguerlo dal moderno (es. i romani)")
K("ita-344", "Ortografia", 3, "Quando si scioglie la sigla UE, come si scrive correttamente?",
  "Maiuscola solo sulla prima parola (Unione europea)", ["Maiuscola su entrambe le parole", "Tutto in minuscolo", "Tutto in maiuscolo come la sigla"],
  "Le sigle sono tutte maiuscole (UE), ma sciolte hanno la maiuscola solo sulla prima parola: Unione europea.",
  "quando la sigla viene sciolta ha la maiuscola solo il primo nome della serie (es. Unione europea)")
K("ita-345", "Ortografia", 4, "Quando «comune» si scrive con la minuscola?",
  "Quando è usato come nome comune («abito nel comune di Prato»)", ["Sempre", "Mai", "Solo nelle delibere"],
  "Il termine generico è minuscolo (abito nel comune di Prato); la maiuscola va quando indica la denominazione ufficiale (il Comune di Prato ha deliberato…).",
  "abito nel comune di Prato")
K("ita-346", "Ortografia", 4, "Oggi, per titoli come «sindaco» o «professore» seguiti dal nome, cosa si preferisce?",
  "La minuscola: il sindaco Mario Rossi", ["La maiuscola: il Sindaco Mario Rossi", "Tutto maiuscolo", "L'abbreviazione puntata"],
  "Un tempo si abbondava con le maiuscole; oggi si preferiscono le minuscole per titoli e appellativi, salvo quando il titolo indica l'organo nell'esercizio delle funzioni.",
  "oggi si preferiscono piuttosto le minuscole")
K("ita-347", "Ortografia", 4, "Nei nomi di organi composti da più parole, quali iniziali vanno in maiuscolo di regola?",
  "Solo quella della prima parola (es. Consiglio comunale)", ["Quelle di tutte le parole", "Nessuna", "Solo quella dell'ultima parola"],
  "Regola 21: nei nomi di organi o enti composti di regola solo la prima parola ha l'iniziale maiuscola (Consiglio comunale, Ufficio di presidenza).",
  "Consiglio comunale, Ufficio di presidenza")
K("ita-348", "Ortografia", 3, "In quale lingua tutti i sostantivi si scrivono con l'iniziale maiuscola?",
  "In tedesco", ["In inglese", "In francese", "In spagnolo"],
  "Per le parole straniere si seguono le regole di ogni lingua: in tedesco tutti i sostantivi hanno la maiuscola.",
  "tutti i sostantivi si scrivono con l'iniziale maiuscola")
K("ita-349", "Punteggiatura", 3, "Rispetto al punto fermo, il punto e virgola è:",
  "Un segno più debole, usato quando il legame tra le frasi è più forte", ["Un segno più forte", "Del tutto equivalente", "Un segno che chiude il testo"],
  "Il punto e virgola divide una frase dalla successiva ma è più debole del punto: si usa quando il legame logico tra le due frasi è più forte, e negli elenchi.",
  "ma è un segno più debole del punto fermo")
K("ita-350", "Punteggiatura", 4, "Perché in una lettera si può scrivere «Le comunichiamo… Sua domanda» con la maiuscola?",
  "Per distinguere il destinatario da altre persone citate e disambiguare il testo", ["Perché è obbligatorio in ogni testo", "Per errore di battitura", "Perché i pronomi vogliono sempre la maiuscola"],
  "La maiuscola dei pronomi e possessivi di cortesia è consigliabile nei contesti formali e serve a distinguere il destinatario da altri soggetti.",
  "permette infatti di disambiguare il testo")

# ── Banca dati ministeriale «1° Livello – Italiano» (italiano.pdf): domande riportate così come sono,
#    la risposta esatta è la A) del PDF. Generato con scripts/domande/da_banca_ministeriale.py.
D("ita-351", "Sintassi", 2, "Completare la frase \"…..aspettare che lei arrivasse\":",
  "Ho dovuto", ["avremmo", "abbiamo", "andiamo ad"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1: la risposta esatta è «Ho dovuto».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1", "italiano.txt", "Completare la frase \"…..aspettare che lei arrivasse\":")
D("ita-352", "Morfologia", 2, "La \"congiunzione avversativa\":",
  "esprime una contrapposizione tra due elementi di una stessa frase o tra due frasi indipendenti", ["esprime una conclusione", "introduce un chiarimento nell'ambito della frase o tra frasi indipendenti", "unisce due elementi della stessa importanza"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 15: la risposta esatta è «esprime una contrapposizione tra due elementi di una stessa frase o tra due frasi indipendenti».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 15", "italiano.txt", "La \"congiunzione avversativa\":")
D("ita-353", "Lessico", 2, "Tra i seguenti nomi indicare quello di forma promiscua:",
  "giraffa", ["capra", "compare", "montone"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 30: la risposta esatta è «giraffa».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 30", "italiano.txt", "Tra i seguenti nomi indicare quello di forma promiscua:")
D("ita-354", "Morfologia", 2, "Indicare quale tra questi non è un avverbio derivato:",
  "forte", ["fortemente", "fortissimamente", "penzoloni"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 44: la risposta esatta è «forte».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 44", "italiano.txt", "Indicare quale tra questi non è un avverbio derivato:")
D("ita-355", "Lessico", 2, "In quale delle seguenti frasi il \"si\" non è impersonale?",
  "Si pettina e si lava spesso", ["Si va a spasso", "Si nota un interesse", "Si gareggerà a lungo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 59: la risposta esatta è «Si pettina e si lava spesso».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 59", "italiano.txt", "In quale delle seguenti frasi il \"si\" non è impersonale?")
D("ita-356", "Sintassi", 2, "Completare la frase \"Ho visto Giovanni e … ho chiesto le informazioni che mi servivano\":",
  "gli", ["le", "glieli", "ti"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 73: la risposta esatta è «gli».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 73", "italiano.txt", "Completare la frase \"Ho visto Giovanni e … ho chiesto le informazioni che mi servivano\":")
D("ita-357", "Sintassi", 2, "\"Ritengo che abbiano preso delle decisioni sensate.\" In questa frase \"sensate\" è:",
  "attributo del complemento oggetto partitivo", ["complemento di fine", "attributo del complemento di specificazione", "complemento di modo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 87: la risposta esatta è «attributo del complemento oggetto partitivo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 87", "italiano.txt", "\"Ritengo che abbiano preso delle decisioni sensate.\" In questa frase \"sensate\" è:")
D("ita-358", "Ortografia", 2, "Indicare il plurale di \"manoscritto\":",
  "manoscritti", ["maniscritto", "maniscritti", "manoscritte"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 103: la risposta esatta è «manoscritti».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 103", "italiano.txt", "Indicare il plurale di \"manoscritto\":")
D("ita-359", "Sintassi", 2, "Completare la frase \"L'esame………..sostenuto ieri\":",
  "è stato", ["ha stato", "ha avuto", "sarà"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 120: la risposta esatta è «è stato».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 120", "italiano.txt", "Completare la frase \"L'esame………..sostenuto ieri\":")
D("ita-360", "Morfologia", 2, "Indicare in quale delle seguenti frasi vi è una congiunzione coordinante avversativa:",
  "non vuole ma non si oppone", ["fa sempre come vuole lui", "non viene né telefona", "venne quando poté"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 135: la risposta esatta è «non vuole ma non si oppone».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 135", "italiano.txt", "Indicare in quale delle seguenti frasi vi è una congiunzione coordinante avversativa:")
D("ita-361", "Morfologia", 2, "Indicare tra i seguenti il nome collettivo:",
  "fogliame", ["pirata", "penisola", "pecore"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 149: la risposta esatta è «fogliame».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 149", "italiano.txt", "Indicare tra i seguenti il nome collettivo:")
D("ita-362", "Ortografia", 2, "Individuare l'errore:",
  "un'articolo", ["un uomo", "un'attività", "un'anima"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 164: la risposta esatta è «un'articolo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 164", "italiano.txt", "Individuare l'errore:")
D("ita-363", "Ortografia", 2, "Quale delle seguenti proposizione presenta un errore?",
  "Laura pensa sempre a sé.", ["Ognuno pensi per sé.", "Se ne andò.", "Quel negozio ha tanti bellissimi aspirapolvere."],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 178: la risposta esatta è «Laura pensa sempre a sé.».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 178", "italiano.txt", "Quale delle seguenti proposizione presenta un errore?")
D("ita-364", "Ortografia", 2, "Qual è il modo corretto di dividere in sillabe la parola \"córrere\"?",
  "cór-re-re", ["có-rre-re", "cór-rer-e", "cór-rere"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 214: la risposta esatta è «cór-re-re».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 214", "italiano.txt", "Qual è il modo corretto di dividere in sillabe la parola \"córrere\"?")
D("ita-365", "Sintassi", 2, "Completare correttamente la frase \"Quando è partito questa mattina, Giovanni ha detto che…..non appena gli fosse stato possibile\" con il tempo e il modo richiesti dalla proposizione reggente:",
  "sarebbe rientrato", ["rientrò", "rientra", "avrebbe rientrato"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 230: la risposta esatta è «sarebbe rientrato».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 230", "italiano.txt", "Completare correttamente la frase \"Quando è partito questa mattina, Giovanni ha detto che…..non appena gli fosse stato possibile\" con il tempo e il modo richiesti dalla proposizione reggente:")
D("ita-366", "Lessico", 2, "Secondo un modo di dire della lingua italiana ha \"il coltello dalla parte del manico\" chi…",
  "è in una posizione di forza, decisamente favorevole", ["si attacca con un'insistenza inopportuna e molesta", "non vede l'evidenza", "consegue due risultati con una sola azione"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 244: la risposta esatta è «è in una posizione di forza, decisamente favorevole».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 244", "italiano.txt", "Secondo un modo di dire della lingua italiana ha \"il coltello dalla parte del manico\" chi…")
D("ita-367", "Verbi", 2, "Nella frase \"In quel momento non potevo prometterti niente\" il verbo \"potere\" ha funzione…",
  "servile", ["ausiliare", "fraseologica", "copulativa"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 258: la risposta esatta è «servile».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 258", "italiano.txt", "Nella frase \"In quel momento non potevo prometterti niente\" il verbo \"potere\" ha funzione…")
D("ita-368", "Sintassi", 2, "Nell'espressione \"Chiesi a mia figlia come si trovasse in un Paese di cui non conosceva la lingua\" la proposizione \"come si trovasse in un Paese\" è…",
  "subordinata di 1° grado", ["coordinata alla principale", "principale", "subordinata di 2° grado"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 273: la risposta esatta è «subordinata di 1° grado».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 273", "italiano.txt", "Nell'espressione \"Chiesi a mia figlia come si trovasse in un Paese di cui non conosceva la lingua\" la proposizione \"come si trovasse in un Paese\" è…")
D("ita-369", "Sintassi", 2, "Completare con un aggettivo indefinito la frase \"Ogni tanto in tram si trovano … persone molto maleducate\".",
  "certe", ["quelle", "tali", "codeste"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 287: la risposta esatta è «certe».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 287", "italiano.txt", "Completare con un aggettivo indefinito la frase \"Ogni tanto in tram si trovano … persone molto maleducate\".")
D("ita-370", "Sintassi", 2, "Nella frase \"In Italia si mangia bene\" la particella \"si\" è un pronome…",
  "impersonale", ["personale", "riflessivo", "reciproco"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 301: la risposta esatta è «impersonale».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 301", "italiano.txt", "Nella frase \"In Italia si mangia bene\" la particella \"si\" è un pronome…")
D("ita-371", "Sintassi", 2, "Sostituire l'aggettivo \"brutto\" con uno più appropriato nella frase \"Per come sono andate le cose, è un brutto inizio\".",
  "preoccupante", ["inopportuno", "pacifico", "aggressivo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 315: la risposta esatta è «preoccupante».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 315", "italiano.txt", "Sostituire l'aggettivo \"brutto\" con uno più appropriato nella frase \"Per come sono andate le cose, è un brutto inizio\".")
D("ita-372", "Sintassi", 2, "Nella frase \"Giovanni ci rimase male, perché aveva cercato di soddisfarvi\" la locuzione \"perché\" assume funzione di congiunzione…",
  "subordinante causale", ["subordinante finale", "subordinante consecutiva", "locuzione prepositiva"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 329: la risposta esatta è «subordinante causale».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 329", "italiano.txt", "Nella frase \"Giovanni ci rimase male, perché aveva cercato di soddisfarvi\" la locuzione \"perché\" assume funzione di congiunzione…")
D("ita-373", "Morfologia", 2, "L'aggettivo determinativo \"quello\" indica esseri o cose …",
  "lontani da chi parla e da chi ascolta", ["con la stessa identità", "vicini a chi parla", "vicini a chi ascolta"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 343: la risposta esatta è «lontani da chi parla e da chi ascolta».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 343", "italiano.txt", "L'aggettivo determinativo \"quello\" indica esseri o cose …")
D("ita-374", "Verbi", 2, "I nomi composti da una forma verbale e da un sostantivo singolare femminile formano in genere il plurale cambiando la desinenza…",
  "di nessuno dei due elementi", ["del secondo elemento", "del primo elemento", "di entrambi gli elementi"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 358: la risposta esatta è «di nessuno dei due elementi».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 358", "italiano.txt", "I nomi composti da una forma verbale e da un sostantivo singolare femminile formano in genere il plurale cambiando la desinenza…")
D("ita-375", "Verbi", 2, "Nella frase \"Permesso, posso entrare?\" il verbo \"potere\" ha funzione…",
  "servile", ["ausiliare", "predicativa", "fraseologica"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 374: la risposta esatta è «servile».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 374", "italiano.txt", "Nella frase \"Permesso, posso entrare?\" il verbo \"potere\" ha funzione…")
D("ita-376", "Verbi", 2, "Nella frase \"Non si guardano neppure in faccia\" il verbo riflessivo è…",
  "reciproco", ["proprio", "apparente", "intransitivo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 388: la risposta esatta è «reciproco».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 388", "italiano.txt", "Nella frase \"Non si guardano neppure in faccia\" il verbo riflessivo è…")
D("ita-377", "Lessico", 2, "Trovare un sinonimo comune per: bozza e piccola.",
  "Minuta", ["Bolla", "Grossa", "Stampa"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 402: la risposta esatta è «Minuta».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 402", "italiano.txt", "Trovare un sinonimo comune per: bozza e piccola.")
D("ita-378", "Sintassi", 2, "Quale delle seguenti frasi contiene un complemento di causa efficiente?",
  "L'uomo rimase stordito dal colpo ricevuto", ["È un bellissimo romanzo", "Potete uscire per la ricreazione, ad eccezione di chi deve finire il compito", "Mi piace il calore dell'estate"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 417: la risposta esatta è «L'uomo rimase stordito dal colpo ricevuto».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 417", "italiano.txt", "Quale delle seguenti frasi contiene un complemento di causa efficiente?")
D("ita-379", "Lessico", 2, "Vetro è un termine…",
  "primitivo", ["derivato", "alterato", "difettivo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 431: la risposta esatta è «primitivo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 431", "italiano.txt", "Vetro è un termine…")
D("ita-380", "Verbi", 2, "Nella frase \"Dopo aver raccontato la sua brutta esperienza ed il pericolo corso, Piero si mise a piangere\" il verbo \"mettersi\" ha funzione…",
  "fraseologica", ["ausiliare", "copulativa", "servile"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 445: la risposta esatta è «fraseologica».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 445", "italiano.txt", "Nella frase \"Dopo aver raccontato la sua brutta esperienza ed il pericolo corso, Piero si mise a piangere\" il verbo \"mettersi\" ha funzione…")
D("ita-381", "Lessico", 2, "Quale tra le seguenti coppie di sostantivi presenta un falso cambiamento di genere?",
  "Cavalletto – cavalletta", ["Contadino – contadina", "Cameriere – cameriera", "Cugino – cugina"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 459: la risposta esatta è «Cavalletto – cavalletta».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 459", "italiano.txt", "Quale tra le seguenti coppie di sostantivi presenta un falso cambiamento di genere?")
D("ita-382", "Sintassi", 2, "Si completi la seguente affermazione scegliendo la risposta corretta: le proposizioni subordinate relative o attributive sono quelle che…",
  "hanno funzione analoga a quella di un'apposizione nelle frasi semplici.", ["esprimono la causa di quanto detto nella reggente.", "esprimono la condizione affinché si verifichi quanto detto nella reggente.", "hanno una protasi e una apodosi."],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 473: la risposta esatta è «hanno funzione analoga a quella di un'apposizione nelle frasi semplici.».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 473", "italiano.txt", "Si completi la seguente affermazione scegliendo la risposta corretta: le proposizioni subordinate relative o attributive sono quelle che…")
D("ita-383", "Sintassi", 2, "Completare con un aggettivo dimostrativo la frase \"Ti ricordi …volta che abbiamo perso il treno: quanto abbiamo riso!\".",
  "quella", ["questa", "codesta", "una"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 487: la risposta esatta è «quella».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 487", "italiano.txt", "Completare con un aggettivo dimostrativo la frase \"Ti ricordi …volta che abbiamo perso il treno: quanto abbiamo riso!\".")
D("ita-384", "Ortografia", 2, "I nomi maschili che al singolare terminano in -co e in -go, se hanno accentuazione piana, in genere formano il plurale in…",
  "chi, ghi", ["ci, gi", "ce, ge", "che, ghe"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 502: la risposta esatta è «chi, ghi».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 502", "italiano.txt", "I nomi maschili che al singolare terminano in -co e in -go, se hanno accentuazione piana, in genere formano il plurale in…")
D("ita-385", "Verbi", 2, "Sostituire il verbo \"dare\" con uno più appropriato nella frase \"L'incasso della festa è stato dato all'ospedale\".",
  "devoluto", ["portato", "conferito", "trasmesso"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 516: la risposta esatta è «devoluto».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 516", "italiano.txt", "Sostituire il verbo \"dare\" con uno più appropriato nella frase \"L'incasso della festa è stato dato all'ospedale\".")
D("ita-386", "Sintassi", 2, "Sostituire l'aggettivo \"brillante\" con uno più appropriato nella frase \"E' un giovane molto brillante\".",
  "arguto", ["accigliato", "spontaneo", "elegante"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 531: la risposta esatta è «arguto».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 531", "italiano.txt", "Sostituire l'aggettivo \"brillante\" con uno più appropriato nella frase \"E' un giovane molto brillante\".")
D("ita-387", "Verbi", 2, "Il futuro anteriore del verbo \"elìdere\" è…",
  "io avrò eliso", ["io avessi eliso", "io elidessi", "io avrei eliso"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 545: la risposta esatta è «io avrò eliso».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 545", "italiano.txt", "Il futuro anteriore del verbo \"elìdere\" è…")
D("ita-388", "Sintassi", 2, "Trasformare in concessiva esplicita la frase \"Pur essendo arrivati tutti, la riunione non potrà iniziare\".",
  "Malgrado siano tutti arrivati, la riunione non potrà iniziare\"", ["Sono tutti arrivati ma la riunione non potrà iniziare\"", "Nonostante l'arrivo di tutti, la riunione non potrà iniziare", "Sono tutti arrivati ma la riunione non può iniziare"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 559: la risposta esatta è «Malgrado siano tutti arrivati, la riunione non potrà iniziare\"».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 559", "italiano.txt", "Trasformare in concessiva esplicita la frase \"Pur essendo arrivati tutti, la riunione non potrà iniziare\".")
D("ita-389", "Lessico", 2, "Nel linguaggio comune si usa dire che una persona \"aspetta la manna dal cielo\" per intendere che…",
  "resta inerte, inoperosa, aspettando la buona fortuna o l'iniziativa altrui", ["si trova di fronte a una realtà inaspettata", "si trova di fronte a qualcuno capace di tenere testa alla prepotenza o alle maggiori capacità", "particolare"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 573: la risposta esatta è «resta inerte, inoperosa, aspettando la buona fortuna o l'iniziativa altrui».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 573", "italiano.txt", "Nel linguaggio comune si usa dire che una persona \"aspetta la manna dal cielo\" per intendere che…")
D("ita-390", "Sintassi", 2, "Sostituire l'aggettivo \"cattivo\" con uno più appropriato nella frase \"Porto cattive notizie\".",
  "spiacevoli", ["nocivo", "povere", "meschine"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 587: la risposta esatta è «spiacevoli».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 587", "italiano.txt", "Sostituire l'aggettivo \"cattivo\" con uno più appropriato nella frase \"Porto cattive notizie\".")
D("ita-391", "Lessico", 2, "Il prefissoide \"acro-\" indica…",
  "alto, posto all'estremità", ["piccolo", "oscuro, misterioso", "che si oppone a qualcosa"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 601: la risposta esatta è «alto, posto all'estremità».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 601", "italiano.txt", "Il prefissoide \"acro-\" indica…")
D("ita-392", "Sintassi", 2, "Inserire la particella pronominale nella frase \"E' un argomento triste per lui, non …parlare\"",
  "gliene", ["ce ne", "lo ne", "ce lo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 616: la risposta esatta è «gliene».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 616", "italiano.txt", "Inserire la particella pronominale nella frase \"E' un argomento triste per lui, non …parlare\"")
D("ita-393", "Sintassi", 2, "Nell'espressione \"Mentre tu guardi la TV, vado da Franca per restituirle i pattini che mi ha prestato perché potessi partecipare alla gara\" la proposizione \"perché potessi partecipare alla gara\" è…",
  "subordinata di 3° grado", ["subordinata di 1° grado", "subordinata di 2° grado oggettiva esplicita", "subordinata di 2°grado relativa oggettiva"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 630: la risposta esatta è «subordinata di 3° grado».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 630", "italiano.txt", "Nell'espressione \"Mentre tu guardi la TV, vado da Franca per restituirle i pattini che mi ha prestato perché potessi partecipare alla gara\" la proposizione \"perché potessi partecipare alla gara\" è…")
D("ita-394", "Lessico", 2, "Non può assumere lo stesso significato degli altri tre il termine…",
  "cantina", ["lucernario", "abbaino", "soffitta"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 644: la risposta esatta è «cantina».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 644", "italiano.txt", "Non può assumere lo stesso significato degli altri tre il termine…")
D("ita-395", "Sintassi", 2, "Completare con un aggettivo dimostrativo la frase \"… parole sono molto efficaci\".",
  "queste", ["le sue", "alcune tue", "altre"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 659: la risposta esatta è «queste».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 659", "italiano.txt", "Completare con un aggettivo dimostrativo la frase \"… parole sono molto efficaci\".")
D("ita-396", "Morfologia", 2, "Quale tra le seguenti parole perde la \"i\" al plurale?",
  "spiaggia", ["farmacia", "bugia", "battigia"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 673: la risposta esatta è «spiaggia».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 673", "italiano.txt", "Quale tra le seguenti parole perde la \"i\" al plurale?")
D("ita-397", "Sintassi", 2, "Che funzione ha la particella \"vi\" nella frase \"Vi offrirò un pranzo per ringraziarvi dell'interessamento\"?",
  "Complemento di termine", ["Avverbio di luogo", "Complemento oggetto", "Articolo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 687: la risposta esatta è «Complemento di termine».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 687", "italiano.txt", "Che funzione ha la particella \"vi\" nella frase \"Vi offrirò un pranzo per ringraziarvi dell'interessamento\"?")
D("ita-398", "Sintassi", 2, "Completare con una proposizione coordinata avversativa la frase\"Era rimasto male per il comportamento di Luca,…\"",
  "tuttavia lo perdonò", ["e gli tolse il saluto", "come se l'avesse schiaffeggiato", "infatti lo aveva offeso"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 703: la risposta esatta è «tuttavia lo perdonò».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 703", "italiano.txt", "Completare con una proposizione coordinata avversativa la frase\"Era rimasto male per il comportamento di Luca,…\"")
D("ita-399", "Sintassi", 2, "Trasformare in esplicita la proposizione \"I primi giorni dopo aver smesso di fumare rappresentano il periodo più difficile\".",
  "I primi giorni dopo che si è smesso di fumare rappresentano il periodo più difficile", ["I primi giorni dopo lo smettere di fumare rappresentano il periodo più difficile", "Una volta smesso di fumare, i primi giorni rappresentano il periodo più difficile", "I primi giorni dopo smesso di fumare rappresentano il periodo più difficile"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 717: la risposta esatta è «I primi giorni dopo che si è smesso di fumare rappresentano il periodo più difficile».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 717", "italiano.txt", "Trasformare in esplicita la proposizione \"I primi giorni dopo aver smesso di fumare rappresentano il periodo più difficile\".")
D("ita-400", "Sintassi", 2, "Quale dei seguenti periodi contiene una proposizione subordinata avversativa?",
  "Credi di avere ragione, mentre invece hai torto", ["Vado a casa perché ho una fame da lupo", "Come pensavo, oggi non c'è il mercato", "Con questo caldo è difficile uscire presto"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 731: la risposta esatta è «Credi di avere ragione, mentre invece hai torto».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 731", "italiano.txt", "Quale dei seguenti periodi contiene una proposizione subordinata avversativa?")
D("ita-401", "Sintassi", 2, "Nella frase \"Non importa dove hai perso le chiavi, provvedi subito a sostituire la serratura attuale con una di sicurezza \" che funzione logica svolge l'espressione \"di sicurezza\"?",
  "Complemento di fine o scopo", ["Complemento di specificazione", "Complemento di mezzo", "Complemento di modo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 745: la risposta esatta è «Complemento di fine o scopo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 745", "italiano.txt", "Nella frase \"Non importa dove hai perso le chiavi, provvedi subito a sostituire la serratura attuale con una di sicurezza \" che funzione logica svolge l'espressione \"di sicurezza\"?")
D("ita-402", "Sintassi", 2, "Nella frase \"Meno male che c'è la luce del lampione\" troviamo un complemento...",
  "di specificazione", ["di mezzo", "di causa efficiente", "di materia"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 773: la risposta esatta è «di specificazione».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 773", "italiano.txt", "Nella frase \"Meno male che c'è la luce del lampione\" troviamo un complemento...")
D("ita-403", "Lessico", 2, "Tra le seguenti coppie di sostantivi quale non è legata da una relazione di derivazione né di alterazione?",
  "Tifo-tifone", ["Casa–casetta", "Scena–scenetta", "Maglia–maglione"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 788: la risposta esatta è «Tifo-tifone».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 788", "italiano.txt", "Tra le seguenti coppie di sostantivi quale non è legata da una relazione di derivazione né di alterazione?")
D("ita-404", "Sintassi", 2, "Nell'espressione \"Ho telefonato a Mariella per salutarla e invitarla allo spettacolo che si terrà sabato al solito teatro, ma ho dovuto lasciarle un messaggio perché non era in casa.\" la proposizione \"e invitarla allo spettacolo\" è…",
  "coordinata alla subordinata di 1° grado implicita", ["subordinata di 1° grado implicita", "subordinata di 2° grado", "coordinata alla principale"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 803: la risposta esatta è «coordinata alla subordinata di 1° grado implicita».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 803", "italiano.txt", "Nell'espressione \"Ho telefonato a Mariella per salutarla e invitarla allo spettacolo che si terrà sabato al solito teatro, ma ho dovuto lasciarle un messaggio perché non era in casa.\" la proposizione \"e invitarla allo spettacolo\" è…")
D("ita-405", "Morfologia", 2, "È un aggettivo indefinito che varia sia nel genere che nel numero…",
  "parecchio", ["qualche", "ciascuno", "qualsiasi"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 818: la risposta esatta è «parecchio».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 818", "italiano.txt", "È un aggettivo indefinito che varia sia nel genere che nel numero…")
D("ita-406", "Sintassi", 2, "Completare con una proposizione temporale la frase \"Me ne sono andato via …\".",
  "dopo avere salutato tutti i presenti", ["come ogni volta che sento quei discorsi", "sebbene avessi deciso di restare fino alla fine", "per non prendere la pioggia"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 832: la risposta esatta è «dopo avere salutato tutti i presenti».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 832", "italiano.txt", "Completare con una proposizione temporale la frase \"Me ne sono andato via …\".")
D("ita-407", "Verbi", 2, "Nella frase \"Perché non ti prepari una tisana?\" il verbo riflessivo è…",
  "apparente", ["reciproco", "intransitivo", "proprio"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 846: la risposta esatta è «apparente».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 846", "italiano.txt", "Nella frase \"Perché non ti prepari una tisana?\" il verbo riflessivo è…")
D("ita-408", "Verbi", 2, "Sostituire il verbo \"dire\" con uno più appropriato nella frase \"Finalmente Carlo ci ha detto il motivo della sua reazione\".",
  "spiegato", ["mostrato", "inserito", "procurato"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 860: la risposta esatta è «spiegato».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 860", "italiano.txt", "Sostituire il verbo \"dire\" con uno più appropriato nella frase \"Finalmente Carlo ci ha detto il motivo della sua reazione\".")
D("ita-409", "Sintassi", 2, "Completare la frase \"Mentre Marco giocava a pallone ____arrivò un calcio negli stinchi\".",
  "gli", ["le", "loro", "gliene"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 874: la risposta esatta è «gli».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 874", "italiano.txt", "Completare la frase \"Mentre Marco giocava a pallone ____arrivò un calcio negli stinchi\".")
D("ita-410", "Morfologia", 2, "Indicare il nome collettivo appropriato che indica un insieme di alberi:",
  "bosco", ["abeti", "fogliame", "larici"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 889: la risposta esatta è «bosco».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 889", "italiano.txt", "Indicare il nome collettivo appropriato che indica un insieme di alberi:")
D("ita-411", "Morfologia", 2, "Indicare tra i seguenti il nome difettivo:",
  "pazienza", ["alfabeto", "casa", "cadavere"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 903: la risposta esatta è «pazienza».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 903", "italiano.txt", "Indicare tra i seguenti il nome difettivo:")
D("ita-412", "Sintassi", 2, "Completare la frase \" Michelangelo è morto ____ novant'anni\":",
  "a", ["dal", "per", "con"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 917: la risposta esatta è «a».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 917", "italiano.txt", "Completare la frase \" Michelangelo è morto ____ novant'anni\":")
D("ita-413", "Lessico", 2, "Indicare il significato di \"di cui\" nella frase \"Le persone di cui ci siamo fidati ci hanno ingannati.\"",
  "delle quali", ["della quale", "dalle quali", "del quale"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 931: la risposta esatta è «delle quali».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 931", "italiano.txt", "Indicare il significato di \"di cui\" nella frase \"Le persone di cui ci siamo fidati ci hanno ingannati.\"")
D("ita-414", "Lessico", 2, "Indicare un sinonimo di \"Acquistare\":",
  "comprare", ["mangiare", "apprendere", "indicare"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 946: la risposta esatta è «comprare».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 946", "italiano.txt", "Indicare un sinonimo di \"Acquistare\":")
D("ita-415", "Lessico", 2, "Indicare un contrario di \"minimo\":",
  "massimo", ["basso", "alto", "minore"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 960: la risposta esatta è «massimo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 960", "italiano.txt", "Indicare un contrario di \"minimo\":")
D("ita-416", "Verbi", 2, "La III persona singolare dell'imperfetto congiuntivo del verbo sapere è:",
  "sapesse", ["sappia", "abbia saputo", "sapessi"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 974: la risposta esatta è «sapesse».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 974", "italiano.txt", "La III persona singolare dell'imperfetto congiuntivo del verbo sapere è:")
D("ita-417", "Sintassi", 2, "Completare la frase \"È necessario che gli studenti ____in orario in modo che _____assistere a tutta la lezione.\":",
  "arrivino, possano", ["possano, arrivino", "arrivano, possano", "arriverà, potevano"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 988: la risposta esatta è «arrivino, possano».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 988", "italiano.txt", "Completare la frase \"È necessario che gli studenti ____in orario in modo che _____assistere a tutta la lezione.\":")
D("ita-418", "Sintassi", 2, "\"Correvano verso la stazione per non perdere il treno.\" In questa frase \"correvano\" è:",
  "predicato verbale", ["predicato nominale", "complemento di modo", "copula"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1002: la risposta esatta è «predicato verbale».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1002", "italiano.txt", "\"Correvano verso la stazione per non perdere il treno.\" In questa frase \"correvano\" è:")
D("ita-419", "Sintassi", 2, "\"Sono tante le persone che mi hanno consigliato.\" In questa frase \"mi\" è:",
  "complemento di termine", ["complemento oggetto", "predicato verbale", "soggetto"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1016: la risposta esatta è «complemento di termine».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1016", "italiano.txt", "\"Sono tante le persone che mi hanno consigliato.\" In questa frase \"mi\" è:")
D("ita-420", "Sintassi", 2, "\"Sono stati raggiunti da Giuseppe in montagna.\" In questa frase il predicato è costituito da:",
  "un verbo transitivo in forma passiva", ["un verbo intransitivo", "un verbo transitivo in forma attiva", "un verbo ausiliare"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1031: la risposta esatta è «un verbo transitivo in forma passiva».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1031", "italiano.txt", "\"Sono stati raggiunti da Giuseppe in montagna.\" In questa frase il predicato è costituito da:")
D("ita-421", "Sintassi", 2, "\"Carlo sta studiando tantissimo, con l'obiettivo di prendere un bel voto.\" In questa frase è contenuta una proposizione:",
  "finale", ["temporale", "relativa", "causale"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1050: la risposta esatta è «finale».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1050", "italiano.txt", "\"Carlo sta studiando tantissimo, con l'obiettivo di prendere un bel voto.\" In questa frase è contenuta una proposizione:")
D("ita-422", "Verbi", 2, "Indicare il gerundio passato del verbo rodere:",
  "avendo roso", ["rodendo", "roso", "rodente"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1064: la risposta esatta è «avendo roso».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1064", "italiano.txt", "Indicare il gerundio passato del verbo rodere:")
D("ita-423", "Ortografia", 2, "Individuare l'errore:",
  "un'ospite", ["un uccello", "gli Spagnoli", "Francesi"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1078: la risposta esatta è «un'ospite».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1078", "italiano.txt", "Individuare l'errore:")
D("ita-424", "Morfologia", 2, "Quale tra le seguenti congiunzioni non è avversativa?",
  "dunque", ["Anzi", "invece", "ma"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1126: la risposta esatta è «dunque».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1126", "italiano.txt", "Quale tra le seguenti congiunzioni non è avversativa?")
D("ita-425", "Sintassi", 2, "Completare con il pronome personale adatto la frase \"Volete questi dischi?... presto volentieri.\" :",
  "ve li", ["me lo", "te li", "me li"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1140: la risposta esatta è «ve li».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1140", "italiano.txt", "Completare con il pronome personale adatto la frase \"Volete questi dischi?... presto volentieri.\" :")
D("ita-426", "Sintassi", 2, "La frase \"I padroni pagano il salario agli operai\" contiene un complemento:",
  "di termine", ["di luogo", "di modo", "di tempo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1163: la risposta esatta è «di termine».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1163", "italiano.txt", "La frase \"I padroni pagano il salario agli operai\" contiene un complemento:")
D("ita-427", "Sintassi", 2, "Nella frase \"Fu morso da un piccolo cane di razza\" l'attributo è:",
  "piccolo", ["morso", "cane", "razza"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1177: la risposta esatta è «piccolo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1177", "italiano.txt", "Nella frase \"Fu morso da un piccolo cane di razza\" l'attributo è:")
D("ita-428", "Sintassi", 2, "Nella frase \" La casa fu demolita dal terremoto di ieri\" il predicato nominale è:",
  "la frase non ha il predicato nominale", ["fu", "fu demolita", "demolita"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1191: la risposta esatta è «la frase non ha il predicato nominale».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1191", "italiano.txt", "Nella frase \" La casa fu demolita dal terremoto di ieri\" il predicato nominale è:")
D("ita-429", "Sintassi", 2, "Completare la frase \"La casa … abito è in collina\":",
  "dove", ["di dove", "per dove", "da dove"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1205: la risposta esatta è «dove».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1205", "italiano.txt", "Completare la frase \"La casa … abito è in collina\":")
D("ita-430", "Lessico", 2, "Quale tra le seguenti parole ha lo stesso significato di \"bollita\" e \"innamoramento\"?",
  "Cotta", ["Infinita", "Tempesta", "Calda"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1241: la risposta esatta è «Cotta».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1241", "italiano.txt", "Quale tra le seguenti parole ha lo stesso significato di \"bollita\" e \"innamoramento\"?")
D("ita-431", "Sintassi", 2, "Completare la frase \"... che… in Francia? \"",
  "Sapevate; sono nato", ["Sapevo; sono nato", "Sapevate; nascevo", "Sapreste; nascevo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1255: la risposta esatta è «Sapevate; sono nato».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1255", "italiano.txt", "Completare la frase \"... che… in Francia? \"")
D("ita-432", "Sintassi", 2, "Completare la frase \"Si preoccupano se non … a casa. \"",
  "telefono", ["telefonavo", "telefonassi", "telefonerei"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1269: la risposta esatta è «telefono».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1269", "italiano.txt", "Completare la frase \"Si preoccupano se non … a casa. \"")
D("ita-433", "Sintassi", 2, "Completare con la forma riflessiva corretta la frase \"Dopo aver lavorato, Luca … le mani\":",
  "si era lavato", ["mi aveva lavato", "si aveva lavato", "ci aveva lavato"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1284: la risposta esatta è «si era lavato».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1284", "italiano.txt", "Completare con la forma riflessiva corretta la frase \"Dopo aver lavorato, Luca … le mani\":")
D("ita-434", "Sintassi", 2, "Completare con la forma riflessiva corretta la frase \"Anna … lentamente alla madre.\"",
  "si era avvicinata", ["vi avrei avvicinato", "ti avrebbe avvicinato", "mi avrebbe avvicinato"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1298: la risposta esatta è «si era avvicinata».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1298", "italiano.txt", "Completare con la forma riflessiva corretta la frase \"Anna … lentamente alla madre.\"")
D("ita-435", "Sintassi", 2, "Completare la frase \"Se è vero che ieri gli … sicuramente oggi lui ti richiamerà.\"",
  "hai telefonato", ["Avresti telefonato", "telefonerai", "telefoneresti"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1312: la risposta esatta è «hai telefonato».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1312", "italiano.txt", "Completare la frase \"Se è vero che ieri gli … sicuramente oggi lui ti richiamerà.\"")
D("ita-436", "Lessico", 2, "Individuare quale tra i seguenti termini è il contrario di \"gracile\".",
  "Robusto", ["Riconoscente", "Abbondante", "Ristretto"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1326: la risposta esatta è «Robusto».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1326", "italiano.txt", "Individuare quale tra i seguenti termini è il contrario di \"gracile\".")
D("ita-437", "Ortografia", 2, "Individuare il termine scritto in modo errato.",
  "Freccie", ["Camice", "Marce", "Frange"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1341: la risposta esatta è «Freccie».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1341", "italiano.txt", "Individuare il termine scritto in modo errato.")
D("ita-438", "Lessico", 2, "Il contrario di \"mozzare \"è:",
  "congiungere", ["rompere", "stroncare", "stabilire"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1356: la risposta esatta è «congiungere».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1356", "italiano.txt", "Il contrario di \"mozzare \"è:")
D("ita-439", "Verbi", 2, "La prima persona singolare del passato remoto del verbo \"elidere\" è:",
  "elisi", ["elisei", "elidi", "eliddi"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1371: la risposta esatta è «elisi».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1371", "italiano.txt", "La prima persona singolare del passato remoto del verbo \"elidere\" è:")
D("ita-440", "Sintassi", 2, "Completare con la forma riflessiva corretta la frase \"I fratelli … abbracciarono.\"",
  "si", ["mi", "vi", "ti"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1386: la risposta esatta è «si».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1386", "italiano.txt", "Completare con la forma riflessiva corretta la frase \"I fratelli … abbracciarono.\"")
D("ita-441", "Sintassi", 2, "Completare la frase \"Se facesse del bel tempo loro … subito a sciare.\"",
  "Andrebbero", ["Andrà", "Andassero", "Andremo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1400: la risposta esatta è «Andrebbero».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1400", "italiano.txt", "Completare la frase \"Se facesse del bel tempo loro … subito a sciare.\"")
D("ita-442", "Ortografia", 2, "Individuare il termine che NON è scritto correttamente.",
  "Acredito", ["Avallare", "Assediare", "Arrosto"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1414: la risposta esatta è «Acredito».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1414", "italiano.txt", "Individuare il termine che NON è scritto correttamente.")
D("ita-443", "Sintassi", 2, "Quale subordinata contiene la proposizione: \"Il nostro ospite giunto tre giorni fa è appena ripartito\"?",
  "Relativa.", ["Oggettiva.", "Interrogativa indiretta.", "Finale."],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1430: la risposta esatta è «Relativa.».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1430", "italiano.txt", "Quale subordinata contiene la proposizione: \"Il nostro ospite giunto tre giorni fa è appena ripartito\"?")
D("ita-444", "Punteggiatura", 2, "Dal punto di vista grammaticale, quale tra le seguenti frasi proposte è corretta?",
  "L'analisi micro e macroeconomica non dà risultati incoraggianti", ["La propenzione al risparmio degli italiani è in calo", "Il peggio si raggiunge sul versante delli investimenti", "L'atitudine al consumo non cresce"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1444: la risposta esatta è «L'analisi micro e macroeconomica non dà risultati incoraggianti».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1444", "italiano.txt", "Dal punto di vista grammaticale, quale tra le seguenti frasi proposte è corretta?")
D("ita-445", "Sintassi", 2, "Nella frase \"Mimmo tornò a Milano, subito dopo aver lasciato la Francia\" il periodo \"subito dopo aver lasciato la Francia\" che tipo di proposizione subordinata è?",
  "Temporale", ["Dichiarativa", "Interrogativa indiretta", "Soggettiva"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1459: la risposta esatta è «Temporale».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1459", "italiano.txt", "Nella frase \"Mimmo tornò a Milano, subito dopo aver lasciato la Francia\" il periodo \"subito dopo aver lasciato la Francia\" che tipo di proposizione subordinata è?")
D("ita-446", "Morfologia", 2, "Indicare quale dei seguenti nomi, posti al femminile, è errato:",
  "pittora", ["impostora", "scrittrice", "avvocatessa"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1490: la risposta esatta è «pittora».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1490", "italiano.txt", "Indicare quale dei seguenti nomi, posti al femminile, è errato:")
D("ita-447", "Morfologia", 2, "Indicare quale dei seguenti aggettivi non è qualificativo:",
  "questo", ["triangolare", "spazioso", "blu"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1505: la risposta esatta è «questo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1505", "italiano.txt", "Indicare quale dei seguenti aggettivi non è qualificativo:")
D("ita-448", "Lessico", 2, "Paolo pensa di…..sempre ragione:",
  "avere", ["avete", "abbia", "essere"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1520: la risposta esatta è «avere».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1520", "italiano.txt", "Paolo pensa di…..sempre ragione:")
D("ita-449", "Ortografia", 2, "Indicare la frase scritta correttamente:",
  "parlammo ancora a lungo e lui, quando se ne andò, mi salutò con calore", ["parlammo, ancora, a lungo, e lui, quando, se ne andò, mi salutò con calore", "parlammo ancora a lungo e lui, quando, se, ne andò, mi, salutò con calore", "parlammo ancora, a, lungo e lui, quando se ne andò, mi salutò con calore"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1534: la risposta esatta è «parlammo ancora a lungo e lui, quando se ne andò, mi salutò con calore».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1534", "italiano.txt", "Indicare la frase scritta correttamente:")
D("ita-450", "Lessico", 2, "Quale è fra questi un simbolo che coinvolge un senso?",
  "Segno visivo", ["Segno naturale", "Segno effettuale", "Segno concreto"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1548: la risposta esatta è «Segno visivo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1548", "italiano.txt", "Quale è fra questi un simbolo che coinvolge un senso?")
D("ita-451", "Lessico", 2, "Come può essere definito un ricevente?",
  "Decodificatore", ["Interpretatore", "Referente", "Uditore"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1562: la risposta esatta è «Decodificatore».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1562", "italiano.txt", "Come può essere definito un ricevente?")
D("ita-452", "Lessico", 2, "La lingua in cui è formulato il messaggio di una e-mail può essere definita:",
  "codice", ["canale", "mezzo", "referente"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1577: la risposta esatta è «codice».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1577", "italiano.txt", "La lingua in cui è formulato il messaggio di una e-mail può essere definita:")
D("ita-453", "Lessico", 2, "I testi non letterari:",
  "sono utilizzati per scopi legati alla vita di tutti i giorni", ["non hanno una utilità pratica", "non servono a dare informazioni", "servono ad intrattenere e a divertire"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1591: la risposta esatta è «sono utilizzati per scopi legati alla vita di tutti i giorni».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1591", "italiano.txt", "I testi non letterari:")
D("ita-454", "Lessico", 2, "Che cos'è l'intreccio?",
  "un racconto nel quale gli eventi sono ordinati secondo un ordine narrativo e non logico o cronologico", ["è l'insieme degli eventi narrati nel testo nella loro successione temporale", "l'elenco degli avvenimenti come si sono realmente succeduti nel tempo", "è l'ordine della storia"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1606: la risposta esatta è «un racconto nel quale gli eventi sono ordinati secondo un ordine narrativo e non logico o cronologico».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1606", "italiano.txt", "Che cos'è l'intreccio?")
D("ita-455", "Lessico", 2, "Quale significato ha il termine essenziale?",
  "fondamentale", ["qualità", "talentuoso", "veritiero"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1621: la risposta esatta è «fondamentale».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1621", "italiano.txt", "Quale significato ha il termine essenziale?")
D("ita-456", "Lessico", 2, "Quale tra questi non è un sinonimo di docente?",
  "divulgatore", ["professore", "maestro", "insegnante"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1635: la risposta esatta è «divulgatore».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1635", "italiano.txt", "Quale tra questi non è un sinonimo di docente?")
D("ita-457", "Lessico", 2, "Uno tra questi termini non ha lo stesso significato di sommerso. Quale?",
  "sommesso", ["immerso", "nascosto", "affondato"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1649: la risposta esatta è «sommesso».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1649", "italiano.txt", "Uno tra questi termini non ha lo stesso significato di sommerso. Quale?")
D("ita-458", "Sintassi", 2, "Si individui la frase con il predicato nominale:",
  "Cleopatra divenne l'amante di Cesare", ["le modelle sfilano con abiti colorati", "stava per scatenarsi una tempesta di sabbia", "all'improvviso si udirono degli strani rumori"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1665: la risposta esatta è «Cleopatra divenne l'amante di Cesare».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1665", "italiano.txt", "Si individui la frase con il predicato nominale:")
D("ita-459", "Sintassi", 2, "Tra queste affermazioni, quale non si riferisce al predicato nominale?",
  "esprime un'azione compiuta dal soggetto che ricade sul soggetto stesso", ["è formato dal verbo essere più un nome o un aggettivo", "si può formare anche con un verbo copulativo", "il verbo essere svolge la funzione di copula"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1679: la risposta esatta è «esprime un'azione compiuta dal soggetto che ricade sul soggetto stesso».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1679", "italiano.txt", "Tra queste affermazioni, quale non si riferisce al predicato nominale?")
D("ita-460", "Lessico", 2, "In quale di queste frasi non è presente una apposizione:",
  "ho cucinato anche per la mia famiglia", ["La capitale d'Italia è Roma, città ricca di storia", "quel simpaticone di tuo fratello ha combinato un nuovo danno", "sono stata nel Sahara, deserto immenso"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1693: la risposta esatta è «ho cucinato anche per la mia famiglia».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1693", "italiano.txt", "In quale di queste frasi non è presente una apposizione:")
D("ita-461", "Sintassi", 2, "Nella frase:\" Udivamo un rullare di tamburi\" che tipo di complemento è \"un rullare\"?",
  "complemento oggetto", ["complemento di specificazione", "complemento di termine", "complemento di modo o maniera"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1707: la risposta esatta è «complemento oggetto».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1707", "italiano.txt", "Nella frase:\" Udivamo un rullare di tamburi\" che tipo di complemento è \"un rullare\"?")
D("ita-462", "Sintassi", 2, "Nella frase: \"Mi piace questo di te\" che tipo di complemento è \"di te\"?",
  "complemento di specificazione", ["complemento di modo o maniera", "complemento oggetto", "complemento di termine"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1721: la risposta esatta è «complemento di specificazione».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1721", "italiano.txt", "Nella frase: \"Mi piace questo di te\" che tipo di complemento è \"di te\"?")
D("ita-463", "Sintassi", 2, "La proposizione subordinata:",
  "dipende da altre proposizioni", ["da sola ha senso compiuto", "può anche essere detta indipendente", "non dipende dalla principale"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1735: la risposta esatta è «dipende da altre proposizioni».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1735", "italiano.txt", "La proposizione subordinata:")
D("ita-464", "Sintassi", 2, "Che tipo di proposizione è:\"Non verrò a scuola con te\"?",
  "enunciativa", ["interrogativa", "dubitativa", "esclamativa"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1751: la risposta esatta è «enunciativa».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1751", "italiano.txt", "Che tipo di proposizione è:\"Non verrò a scuola con te\"?")
D("ita-465", "Sintassi", 2, "La proposizione \"Con chi posso uscire?\" può essere definita:",
  "dubitativa", ["interrogativa", "enunciativa", "esclamativa"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1766: la risposta esatta è «dubitativa».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1766", "italiano.txt", "La proposizione \"Con chi posso uscire?\" può essere definita:")
D("ita-466", "Lessico", 2, "Si scelga il sinonimo di \"scialbo\" tra quelli proposti:",
  "sbiadito", ["sgraziato", "bugiardo", "finto"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1780: la risposta esatta è «sbiadito».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1780", "italiano.txt", "Si scelga il sinonimo di \"scialbo\" tra quelli proposti:")
D("ita-467", "Lessico", 2, "Il termine \"franco\" può avere diversi significati. Quale tra questi è sbagliato?",
  "goffo", ["libero", "sincero", "disinvolto"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1796: la risposta esatta è «goffo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1796", "italiano.txt", "Il termine \"franco\" può avere diversi significati. Quale tra questi è sbagliato?")
D("ita-468", "Sintassi", 2, "Quante proposizioni subordinate compaiono nel seguente periodo: \"Prendo il motorino perché è tardi e Lucia mia aspetta da un'ora\"?",
  "2", ["3", "1", "nessuna"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1814: la risposta esatta è «2».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1814", "italiano.txt", "Quante proposizioni subordinate compaiono nel seguente periodo: \"Prendo il motorino perché è tardi e Lucia mia aspetta da un'ora\"?")
D("ita-469", "Morfologia", 2, "Trova, fra questi, l'articolo partitivo:",
  "Dei, delle", ["Gli, le", "Un , una", "Degli, le"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1828: la risposta esatta è «Dei, delle».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1828", "italiano.txt", "Trova, fra questi, l'articolo partitivo:")
D("ita-470", "Sintassi", 2, "Nella frase \" Ho mangiato del buon pane\" , che tipo di articolo troviamo?",
  "Partitivo", ["Determinativo", "Indeterminativo", "Interrogativo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1842: la risposta esatta è «Partitivo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1842", "italiano.txt", "Nella frase \" Ho mangiato del buon pane\" , che tipo di articolo troviamo?")
D("ita-471", "Lessico", 2, "La parola \"papà\" in grammatica che genere è?",
  "Indipendente", ["Maschile", "Promiscuo", "Neutro"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1856: la risposta esatta è «Indipendente».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1856", "italiano.txt", "La parola \"papà\" in grammatica che genere è?")
D("ita-472", "Morfologia", 2, "Quale fra questi è un nome concreto ?",
  "Aiuola", ["Pensiero", "Sguardo", "Nessuno"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1870: la risposta esatta è «Aiuola».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1870", "italiano.txt", "Quale fra questi è un nome concreto ?")
D("ita-473", "Morfologia", 2, "Quale fra questi nomi hanno lo stesso genere al maschile e al femminile?",
  "Pantera", ["Gatto", "Asino", "Nessuno"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1885: la risposta esatta è «Pantera».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1885", "italiano.txt", "Quale fra questi nomi hanno lo stesso genere al maschile e al femminile?")
D("ita-474", "Lessico", 2, "Quali fra questi suffissi sono diminutivi?",
  "-icino, -etto, -icello", ["-etto, -uccio, -olo", "-iciattolo, -ucolo, -astro", "-astro, -etto, -olo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1899: la risposta esatta è «-icino, -etto, -icello».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1899", "italiano.txt", "Quali fra questi suffissi sono diminutivi?")
D("ita-475", "Lessico", 2, "Nello schema narrativo di un racconto che cos'è la situazione iniziale?",
  "l'inizio della vicenda", ["il fatto o la situazione che stanno alla base della vicenda", "l'avvenimento che ha caratterizzato la vicenda e ne ha indirizzato lo sviluppo verso situazioni non previste nella situazione iniziale", "la conclusione della vicenda"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1913: la risposta esatta è «l'inizio della vicenda».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1913", "italiano.txt", "Nello schema narrativo di un racconto che cos'è la situazione iniziale?")
D("ita-476", "Sintassi", 2, "Una di queste affermazioni non si riferisce all'analisi grammaticale. Quale?",
  "scompone le sequenze in sintagmi con lo scopo di definire le loro funzioni logiche", ["scompone le sequenze in singole parole con lo scopo di classificarle secondo le nove categorie", "procedimento per riconoscere la categoria grammaticale di ogni parola in funzione del contesto nel quale è usata", "consiste nel riconoscere le varie parti del discorso"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1927: la risposta esatta è «scompone le sequenze in sintagmi con lo scopo di definire le loro funzioni logiche».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1927", "italiano.txt", "Una di queste affermazioni non si riferisce all'analisi grammaticale. Quale?")
D("ita-477", "Lessico", 2, "Le parole dei personaggi in un racconto possono essere riferite attraverso diverse modalità. Quale di queste non esiste?",
  "discorso analitico", ["monologo", "discorso diretto", "soliloquio"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1942: la risposta esatta è «discorso analitico».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1942", "italiano.txt", "Le parole dei personaggi in un racconto possono essere riferite attraverso diverse modalità. Quale di queste non esiste?")
D("ita-478", "Sintassi", 2, "Quanti attributi puoi individuare nella seguente frase: \"Il piccolo Marco appartiene a una famiglia bene\"?",
  "2", ["1", "3", "nessuno"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1956: la risposta esatta è «2».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1956", "italiano.txt", "Quanti attributi puoi individuare nella seguente frase: \"Il piccolo Marco appartiene a una famiglia bene\"?")
D("ita-479", "Verbi", 2, "Quale tra queste voci verbali è al modo condizionale?",
  "potrei", ["possa", "dormi!", "avevi portato"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1970: la risposta esatta è «potrei».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1970", "italiano.txt", "Quale tra queste voci verbali è al modo condizionale?")
D("ita-480", "Verbi", 2, "Il verbo che compare nella frase: \"La balena emerge\" è:",
  "intransitivo", ["passivo", "impersonale", "transitivo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1984: la risposta esatta è «intransitivo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1984", "italiano.txt", "Il verbo che compare nella frase: \"La balena emerge\" è:")
D("ita-481", "Verbi", 2, "La voce verbale \"discussi\":",
  "è un participio passato", ["è un participio presente", "non esiste", "è un condizionale"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 1998: la risposta esatta è «è un participio passato».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 1998", "italiano.txt", "La voce verbale \"discussi\":")
D("ita-482", "Ortografia", 2, "La definizione \"Insieme di norme e di usi che regolano la corretta scrittura delle parole\" si riferisce a:",
  "ortografia", ["grammatica", "coesione", "coerenza"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2012: la risposta esatta è «ortografia».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2012", "italiano.txt", "La definizione \"Insieme di norme e di usi che regolano la corretta scrittura delle parole\" si riferisce a:")
D("ita-483", "Sintassi", 2, "In quale di queste frasi è presente un complemento di mezzo?",
  "Grazie alla mia insegnante ho trovato lavoro", ["Dovete studiare in vista della maturità", "Muoio di fame", "Ho perso per colpa tua"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2026: la risposta esatta è «Grazie alla mia insegnante ho trovato lavoro».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2026", "italiano.txt", "In quale di queste frasi è presente un complemento di mezzo?")
D("ita-484", "Lessico", 2, "Un testo informativo quale funzione può avere?",
  "esporre", ["persuadere", "esprimere sentimenti", "stabilire il contatto tra emittente e destinatario"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2040: la risposta esatta è «esporre».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2040", "italiano.txt", "Un testo informativo quale funzione può avere?")
D("ita-485", "Lessico", 2, "Il messaggio \"Come sei elegante!\" quale funzione ha?",
  "espressiva", ["informativa", "poetica", "fatica"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2054: la risposta esatta è «espressiva».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2054", "italiano.txt", "Il messaggio \"Come sei elegante!\" quale funzione ha?")
D("ita-486", "Sintassi", 2, "Che tipo di subordinata troviamo nella frase: \"Dimmi se hai fatto colazione\"?",
  "interrogativa diretta", ["modale", "finale", "consecutiva"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2069: la risposta esatta è «interrogativa diretta».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2069", "italiano.txt", "Che tipo di subordinata troviamo nella frase: \"Dimmi se hai fatto colazione\"?")
D("ita-487", "Sintassi", 2, "Che tipo di complemento di luogo troviamo nella frase: \"Mi ha mandato al diavolo\"?",
  "moto a luogo", ["moto da luogo", "stato in luogo", "moto per luogo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2083: la risposta esatta è «moto a luogo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2083", "italiano.txt", "Che tipo di complemento di luogo troviamo nella frase: \"Mi ha mandato al diavolo\"?")
D("ita-488", "Lessico", 2, "Una persona che fotografa avvenimenti per conto di giornali o agenzie è:",
  "un fotoreporter", ["un titolista", "uno speaker", "un commentatore"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2099: la risposta esatta è «un fotoreporter».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2099", "italiano.txt", "Una persona che fotografa avvenimenti per conto di giornali o agenzie è:")
D("ita-489", "Lessico", 2, "Nell'ambito giornalistico, chi è un corrispondente?",
  "un giornalista che svolge il proprio lavoro lontano dalla redazione centrale", ["un giornalista specializzato nel fare titoli", "colui che legge le notizie", "un giornalista che lavora stabilmente negli uffici in cui si realizza un giornale"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2113: la risposta esatta è «un giornalista che svolge il proprio lavoro lontano dalla redazione centrale».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2113", "italiano.txt", "Nell'ambito giornalistico, chi è un corrispondente?")
D("ita-490", "Lessico", 2, "Quale di queste coppie di termini è rispettivamente un sinonimo e un contrario di \"furbo\"?",
  "avveduto/ingenuo", ["astuto/sagace", "ingenuo/sincero", "birbone/abile"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2127: la risposta esatta è «avveduto/ingenuo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2127", "italiano.txt", "Quale di queste coppie di termini è rispettivamente un sinonimo e un contrario di \"furbo\"?")
D("ita-491", "Morfologia", 2, "Di che tipo può essere l'aggettivo determinativo?",
  "Dimostrativo", ["Qualificativo", "Derivato", "Di modo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2141: la risposta esatta è «Dimostrativo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2141", "italiano.txt", "Di che tipo può essere l'aggettivo determinativo?")
D("ita-492", "Morfologia", 2, "Qual è fra questi l'aggettivo possessivo?",
  "Mio", ["Questo", "Qualche", "Cinque"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2155: la risposta esatta è «Mio».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2155", "italiano.txt", "Qual è fra questi l'aggettivo possessivo?")
D("ita-493", "Morfologia", 2, "Come si definiscono gli aggettivi con una unica forma per entrambi i generi?",
  "Invariabili", ["Unici", "Neutri", "Maschili"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2169: la risposta esatta è «Invariabili».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2169", "italiano.txt", "Come si definiscono gli aggettivi con una unica forma per entrambi i generi?")
D("ita-494", "Morfologia", 2, "Come si definisce un prefisso derivato da un nome abbreviato?",
  "Prefissoide", ["Suffissoide", "Avverbioide", "Derivato"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2183: la risposta esatta è «Prefissoide».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2183", "italiano.txt", "Come si definisce un prefisso derivato da un nome abbreviato?")
D("ita-495", "Sintassi", 2, "Nella frase \"il cappotto rosa è molto costoso\" che grado d'intensità è l'aggettivo costoso?",
  "Superlativo", ["Comparativo", "Positivo", "Assoluto"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2198: la risposta esatta è «Superlativo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2198", "italiano.txt", "Nella frase \"il cappotto rosa è molto costoso\" che grado d'intensità è l'aggettivo costoso?")
D("ita-496", "Morfologia", 2, "Nessuno, che tipo di aggettivo è?",
  "Indefinito", ["Dimostrativo", "Numerale", "Possessivo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2213: la risposta esatta è «Indefinito».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2213", "italiano.txt", "Nessuno, che tipo di aggettivo è?")
D("ita-497", "Morfologia", 2, "Quale fra questi aggettivi numerali è di tipo frazionario?",
  "Mezzo", ["Sei", "Terzo", "Doppio"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2227: la risposta esatta è «Mezzo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2227", "italiano.txt", "Quale fra questi aggettivi numerali è di tipo frazionario?")
D("ita-498", "Morfologia", 2, "Come può essere l'aggettivo superlativo?",
  "Assoluto o relativo", ["Quantità o qualità", "Maggioranza o Minoranza", "Interrogativo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2242: la risposta esatta è «Assoluto o relativo».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2242", "italiano.txt", "Come può essere l'aggettivo superlativo?")
D("ita-499", "Sintassi", 2, "Nella frase \"vorrei mangiare qualcosa\" , il pronome \"qualcosa\" che tipo di pronome è?",
  "Indefinito", ["Complemento", "Possessivo", "Relativo"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2256: la risposta esatta è «Indefinito».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2256", "italiano.txt", "Nella frase \"vorrei mangiare qualcosa\" , il pronome \"qualcosa\" che tipo di pronome è?")
D("ita-500", "Morfologia", 2, "Riconosci I tre pronomi indefiniti:",
  "Qualcuno, nessuno, molti", ["Io, tu, egli", "Questo, Codesto, Quello", "Che , il quale, la quale"],
  "Banca dati ministeriale (1° livello, Italiano), domanda n. 2270: la risposta esatta è «Qualcuno, nessuno, molti».",
  "Banca dati ministeriale, 1° livello – Italiano, n. 2270", "italiano.txt", "Riconosci I tre pronomi indefiniti:")
