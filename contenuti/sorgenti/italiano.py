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
