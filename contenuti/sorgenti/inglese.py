# Inglese — fonti: voci di Wikipedia in inglese (CC BY-SA 4.0), solo per le regole grammaticali. Esempi scritti da noi.
MOD = "Wikipedia-EN_English-modal-auxiliary-verbs.txt"
CON = "Wikipedia-EN_English-conditional-sentences.txt"
PAS = "Wikipedia-EN_English-passive-voice.txt"
REL = "Wikipedia-EN_English-relative-clauses.txt"
USE = "Wikipedia-EN_Uses-of-English-verb-forms.txt"
W = lambda voce: f"Wikipedia (EN), «{voce}» (CC BY-SA 4.0)"

D("eng-001", "Modal verbs", 1, "Which of these is a modal auxiliary verb?",
  "must", ["have", "go", "seem"],
  "I modali centrali sono can/could, may/might, shall/should, will/would e must.",
  W("English modal auxiliary verbs"), MOD, "The central English modal auxiliary verbs are can (with could), may (with might), shall (with should), will (with would), and must")

D("eng-002", "Modal verbs", 2, "Qual è la forma «passata» o condizionale abbinata al modale «may»?",
  "might", ["must", "would", "should"],
  "Le coppie sono can/could, may/might, shall/should, will/would.",
  W("English modal auxiliary verbs"), MOD, "may (with might)")

D("eng-003", "Modal verbs", 3, "Complete: «Nobody ___ say a word.» (= nessuno dovrebbe dire una parola)",
  "ought to", ["ought", "must to", "should to"],
  "«Ought» è seguito da to + infinito: «Nobody ought to say a word». Gli altri modali vogliono l'infinito senza to.",
  W("English modal auxiliary verbs"), MOD, "\"Nobody ought to say a word.\"")

D("eng-004", "Conditionals", 2, "Come si chiamano i tipi di periodo ipotetico nell'insegnamento dell'inglese?",
  "Zero, first, second, third e mixed conditional", ["Simple, perfect e continuous conditional", "Real e unreal conditional, senza altre distinzioni", "Present, past e future conditional"],
  "Le frasi condizionali sono classificate come zero, first, second, third e mixed conditional, in base allo schema grammaticale.",
  W("English conditional sentences"), CON, "zero conditional, first conditional (or conditional I), second conditional (or conditional II), third conditional (or conditional III) and mixed conditional")

D("eng-005", "Conditionals", 3, "Complete the third conditional: «If you had called me, I ___.»",
  "would have come", ["will come", "would come", "came"],
  "Terzo condizionale: if + past perfect, would have + participio passato. «If you had called me, I would have come.»",
  W("English conditional sentences"), CON, "If you had called me, I would have come")

D("eng-006", "Conditionals", 3, "Which form is used in «If I ___ king, I could have you thrown in the dungeon»?",
  "were", ["was being", "am", "will be"],
  "Nelle ipotesi irreali si usa «were» anche con I/he/she: «If I were king…».",
  W("English conditional sentences"), CON, "If I were king, I could have you thrown in the dungeon")

D("eng-007", "Conditionals", 4, "Perché nel second conditional si usa il passato (es. «If you saw him…»)?",
  "Per indicare che chi parla considera l'ipotesi impossibile o improbabile", ["Perché il fatto è già avvenuto", "Perché è obbligatorio dopo if", "Per esprimere un ordine"],
  "L'inglese usa la morfologia del passato per indicare che l'antecedente è impossibile o improbabile.",
  W("English conditional sentences"), CON, "English uses past tense morphology to indicate that the speaker regards the antecedent as impossible or unlikely")

D("eng-008", "Passive voice", 2, "How is the passive voice formed in English?",
  "be (or get) + past participle", ["have + past participle", "be + -ing form", "do + infinitive"],
  "Il passivo si forma con be (o get) seguito dal participio passato: «The enemy was defeated».",
  W("English passive voice"), PAS, "The passive voice is marked by using be or get followed by a past participle")

D("eng-009", "Passive voice", 2, "Turn into the passive: «Brutus stabbed Caesar.»",
  "Caesar was stabbed by Brutus.", ["Caesar stabbed by Brutus.", "Caesar has stabbing by Brutus.", "Brutus was stabbed by Caesar."],
  "Nel passivo l'oggetto diventa soggetto, il verbo diventa be + participio passato e l'agente si introduce con «by».",
  W("English passive voice"), PAS, "Caesar was stabbed")

D("eng-010", "Passive voice", 3, "In a passive sentence, how is the agent (who performs the action) usually introduced?",
  "With a by-phrase", ["With a with-phrase", "With a from-phrase", "It can never be expressed"],
  "L'agente può essere omesso o espresso con «by»: «The patient was murdered by his own doctor».",
  W("English passive voice"), PAS, "usually via a by-phrase")

D("eng-011", "Relative clauses", 2, "Which are the basic relative pronouns in English?",
  "who, which and that", ["what, where and when", "he, she and it", "this, that and these"],
  "I pronomi relativi di base sono who, which e that; da who derivano whom e whose.",
  W("English relative clauses"), REL, "The basic relative pronouns are who, which, and that")

D("eng-012", "Relative clauses", 3, "Complete: «The teacher ___ car was stolen called the police.»",
  "whose", ["who", "whom", "which"],
  "«Whose» esprime possesso (la cui auto); è una forma derivata di who.",
  W("English relative clauses"), REL, "who also has the derived forms whom and whose")

D("eng-013", "Relative clauses", 4, "In which relative clauses can «that» be used?",
  "Only in restrictive clauses, without a comma", ["Only in non-restrictive clauses, after a comma", "In both kinds of clause", "Never with things"],
  "«That» introduce solo relative restrittive e non è preceduto da virgola; who e which si usano in entrambi i tipi.",
  W("English relative clauses"), REL, "that is used only in restrictive relative clauses, and is not preceded by a comma")

D("eng-014", "Verb tenses", 3, "Does English have a morphological future tense (a special verb ending for the future)?",
  "No: the future is expressed with constructions such as will, shall or be going to", ["Yes, the ending -ed", "Yes, the ending -ing", "Yes, but only for regular verbs"],
  "L'inglese non ha una flessione del verbo per il futuro: usa will, shall, to be going to e altre costruzioni.",
  W("Uses of English verb forms"), USE, "English lacks a morphological future tense")

D("eng-015", "Verb tenses", 2, "Complete: «Don't go near that bomb! It ___ explode!»",
  "is going to", ["going to", "goes to", "will to"],
  "«Be going to» indica un futuro previsto da segnali presenti: «It's going to explode!».",
  W("Uses of English verb forms"), USE, "It's going to explode!")

D("eng-016", "Verb tenses", 4, "What does the present perfect primarily denote?",
  "Past events seen through their resulting present situation", ["Only actions happening right now", "Only future plans", "Habits in the distant past"],
  "Il present perfect si riferisce a eventi passati ma soprattutto alla situazione presente che ne deriva (es. «I have lost my keys»).",
  W("Uses of English verb forms"), USE, "The present perfect intrinsically refers to past events")


# --- Blocco 2: articoli, plurali, pronomi, possessivo, comparativi, tempi passati ---
def E(id, arg, liv, testo, giusta, sbagliate, spieg, voce, file, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W(voce), f"Wikipedia-EN_{file}.txt", frase)

ART = ("English articles", "English-articles")
E("eng-017", "Articles", 1, "Complete: «I have ___ apple.»", "an", ["a", "the", "—"],
  "Si usa «an» davanti a un suono vocalico.", *ART, "which takes the alternate form an when followed by a vowel sound")
E("eng-018", "Articles", 2, "Complete: «We waited for ___ hour.»", "an", ["a", "—", "some"],
  "In «hour» la h è muta: il suono iniziale è vocalico.", *ART, "an hour (the h is silent)")
E("eng-019", "Articles", 3, "Complete: «She bought ___ one-way ticket.»", "a", ["an", "the", "—"],
  "«One» si pronuncia «won»: il suono iniziale è consonantico.", *ART, "a one-armed bandit (pronounced \"won...\")")
E("eng-020", "Articles", 2, "Which article is used when the listener already knows which thing we mean?", "the", ["a", "an", "No article"],
  "È l'articolo determinativo.", *ART, "The definite article is the default determiner when the speaker believes that the listener knows the identity")
E("eng-021", "Articles", 2, "Which sentence is grammatically correct?", "I have a box.", ["I have box.", "I have an box.", "I have the a box."],
  "Un sostantivo singolare numerabile richiede di norma un determinante.", *ART, "For example, I have a box is grammatically correct, but *I have box is not")
E("eng-022", "Articles", 3, "Complete: «John likes ___ fast cars.» (in general)", "— (no article)", ["the", "a", "an"],
  "Con plurali usati in senso generale non si usa l'articolo.", *ART, "John likes fast cars")
PLU = ("English plurals", "English-plurals")
E("eng-023", "Plurals", 1, "What is the plural of «box»?", "boxes", ["boxs", "boxen", "box"],
  "Dopo un suono sibilante si aggiunge -es.", *PLU, "The spelling adds -es, or -s if the singular already ends in -e")
E("eng-024", "Plurals", 1, "What is the plural of «city»?", "cities", ["citys", "cityes", "cityies"],
  "Consonante + y: la y cade e si aggiunge -ies.", *PLU, "preceded by a consonant usually drop the y and add -ies")
E("eng-025", "Plurals", 2, "What is the plural of «potato»?", "potatoes", ["potatos", "potatis", "potato"],
  "Molti nomi in consonante + o aggiungono -es.", *PLU, "Singular nouns ending in o preceded by a consonant in many cases spell the plural by adding -es")
E("eng-026", "Plurals", 2, "What is the plural of «leaf»?", "leaves", ["leafs", "leafes", "leaf"],
  "Alcuni nomi in -f cambiano in -ves.", *PLU, "the plural of leaf is leaves")
E("eng-027", "Plurals", 1, "What is the plural of «person» in everyday English?", "people", ["persones", "peoples", "personen"],
  "«Persons» si usa in contesti formali (legali, tecnici).", *PLU, "person—people")
E("eng-028", "Plurals", 1, "What is the plural of «woman»?", "women", ["womans", "womens", "womanes"],
  "Plurale irregolare, come man → men.", *PLU, "There are many compounds of man and woman that form their plurals in the same way")
E("eng-029", "Plurals", 2, "What is the plural of «goose»?", "geese", ["gooses", "geeses", "goose"],
  "Plurale irregolare con cambio vocalico.", *PLU, "goose / geese")
E("eng-030", "Plurals", 2, "What is the plural of «sheep»?", "sheep", ["sheeps", "sheepes", "shoop"],
  "Alcuni nomi di animali hanno il plurale uguale al singolare.", *PLU, "salmon sheep shrimp")
E("eng-031", "Plurals", 4, "In standard English, «criteria» and «phenomena» are:", "plural forms", ["singular forms", "uncountable nouns", "verbs"],
  "I singolari sono criterion e phenomenon.", *PLU, "words such as criteria and phenomena are used as singular by some speakers, although this is still considered incorrect")
E("eng-032", "Plurals", 3, "What is the plural of «die» (the cube used in games)?", "dice", ["dies", "dye", "dices"],
  "Plurale irregolare.", *PLU, "die—dice")
PRO = ("Personal pronouns in English", "Personal-pronouns-in-English")
E("eng-033", "Pronouns", 1, "Complete: «___ am a teacher.»", "I", ["Me", "My", "Mine"],
  "Il soggetto vuole la forma soggetto (I, we…).", *PRO, "subjective (nominative) case (I, we, etc.), used as the subject of a verb")
E("eng-034", "Pronouns", 1, "Complete: «Can you help ___?»", "me", ["I", "my", "mine"],
  "Il complemento oggetto vuole la forma oggetto (me, us…).", *PRO, "objective (accusative) case (me, us, etc.), used as the object of a verb")
E("eng-035", "Pronouns", 2, "Complete: «She cut ___ while cooking.»", "herself", ["her", "she", "hers"],
  "Pronome riflessivo: si riferisce al soggetto della stessa frase.", *PRO, "She cut herself")
E("eng-036", "Pronouns", 2, "Complete: «This book is ___.» (= è mio)", "mine", ["my", "me", "I"],
  "Il pronome possessivo sostituisce il nome; my è aggettivo e precede il nome.", *PRO, "this book is mine")
E("eng-037", "Pronouns", 3, "In «She made the dress herself», «herself» is used as:", "an intensive pronoun", ["an object pronoun", "a possessive", "a subject"],
  "Rafforza il soggetto («da sola»).", *PRO, "The same reflexive forms also are used as intensive pronouns")
E("eng-038", "Pronouns", 4, "With singular «they», which verb form is used?", "The plural form: «they are»", ["The singular form: «they is»", "Either, freely", "No verb"],
  "Singular they è morfosintatticamente plurale.", *PRO, "singular they is morphosyntactically plural")
POS = ("English possessive", "English-possessive")
E("eng-039", "Possessive", 1, "How do you say «la macchina di Mark»?", "Mark's car", ["Marks car", "the car Mark", "Mark car's"],
  "Genitivo sassone: -'s.", *POS, "the possessive is generally formed with the suffix -'s")
E("eng-040", "Possessive", 2, "Which is correct?", "The dog wagged its tail.", ["The dog wagged it's tail.", "The dog wagged its' tail.", "The dog wagged it tail."],
  "«its» possessivo non ha l'apostrofo (it's = it is).", *POS, "personal pronouns have irregular possessives that do not use an apostrophe, such as its")
E("eng-041", "Possessive", 3, "What is the possessive of «the king of Spain»?", "the king of Spain's", ["the king's of Spain", "the kings of Spain", "of the king Spain's"],
  "Il morfema -'s si attacca all'ultima parola del sintagma.", *POS, "the phrase the king of Spain forms the possessive the king of Spain's")
E("eng-042", "Possessive", 2, "Complete: «The man ___ car was stolen went to the police.»", "whose", ["who's", "who", "which"],
  "whose è il possessivo di who.", *POS, "The interrogative and relative pronoun who has the possessive whose")
E("eng-043", "Possessive", 2, "What is the possessive form of «boss»?", "boss's", ["bosses", "boss'es", "bosss"],
  "Anche i nomi singolari in -s prendono di solito -'s.", *POS, "Singular nouns ending in s also form a possessive regularly by adding 's")
CMP = ("Degrees of comparison of adjectives and adverbs", "Degrees-of-comparison-of-adjectives-and-adverbs")
E("eng-044", "Comparatives", 1, "What is the comparative of «big»?", "bigger", ["more big", "biger", "biggest"],
  "Gli aggettivi di una sillaba prendono il suffisso -er.", *CMP, "words of one syllable require the suffix")
E("eng-045", "Comparatives", 1, "What is the superlative of «good»?", "best", ["goodest", "better", "most good"],
  "good → better → best (irregolare).", *CMP, "such as better and best (from good)")
E("eng-046", "Comparatives", 2, "What is the comparative of «beautiful»?", "more beautiful", ["beautifuller", "most beautiful", "beautifulest"],
  "Gli aggettivi di tre o più sillabe usano more/most.", *CMP, "words of three or more syllables require \"more\" or \"most\"")
E("eng-047", "Comparatives", 2, "Complete: «My house is ___ yours.» (= grande quanto)", "as big as", ["so big than", "as big than", "bigger as"],
  "Comparativo di uguaglianza: as … as.", *CMP, "as big and as fully [comparative of equality]")
E("eng-048", "Comparatives", 2, "Which word introduces the second term of a comparison?", "than", ["then", "that", "of"],
  "Es. «She is taller than me».", *CMP, "as with than in English")
E("eng-049", "Comparatives", 3, "Which form is a non-standard «double comparative»?", "more louder", ["louder", "more loud", "the loudest"],
  "Si usa o il suffisso o more, non entrambi.", *CMP, "If an adjective has two comparative markers, it is known as a double comparative")
E("eng-050", "Comparatives", 3, "What are the comparative and superlative of «little» (quantity)?", "less, least", ["littler, littlest", "lesser, lessest", "more little, most little"],
  "Forme irregolari.", *CMP, "less and least (from little/few)")
PV = ("English phrasal verbs", "English-phrasal-verbs")
E("eng-051", "Phrasal verbs", 2, "What is a phrasal verb?", "A verb + particle forming a single unit of meaning (e.g. turn down)", ["A verb in the passive", "A verb with two objects", "A modal verb"],
  "Il significato spesso non è deducibile dalle singole parti.", *PV, "a phrasal verb typically constitutes a single semantic unit consisting of a verb followed by a particle")
E("eng-052", "Phrasal verbs", 3, "What does «put up with» mean?", "to tolerate", ["to build", "to hang up", "to reject"],
  "«I can't put up with this noise» = non sopporto questo rumore.", *PV, "Who can put up with that?")
E("eng-053", "Phrasal verbs", 3, "What does «look forward to» mean?", "to wait for something with pleasure", ["to look ahead on the road", "to forget", "to look after"],
  "Seguito da nome o -ing: «I look forward to hearing from you».", *PV, "She looks forward to a rest")
E("eng-054", "Phrasal verbs", 3, "What does «run out of» (e.g. «we ran out of milk») mean?", "to have no more of something", ["to run away from", "to buy more", "to spill"],
  "Esempio di verbo con particella e preposizione.", *PV, "run out of")
PP = ("Present perfect", "Present-perfect")
E("eng-055", "Verb tenses", 1, "How is the present perfect formed?", "have/has + past participle", ["had + past participle", "will + infinitive", "am/is/are + -ing"],
  "Es. «I have finished».", *PP, "the present tense of the auxiliary verb have")
E("eng-056", "Verb tenses", 2, "Complete: «I have lived here ___ five years.»", "for", ["since", "from", "ago"],
  "for + durata; since + punto di inizio.", *PP, "I have lived here for five years")
E("eng-057", "Verb tenses", 2, "Complete: «She has worked here ___ 2015.»", "since", ["for", "from", "ago"],
  "since + momento d'inizio.", *PP, "normally based on time expressions with for or since")
E("eng-058", "Verb tenses", 2, "Complete: «He has ___ arrived in London.»", "already", ["yet", "ago", "since"],
  "already si usa nelle frasi affermative al present perfect.", *PP, "He has already arrived in America")
E("eng-059", "Verb tenses", 3, "Which tense combines present tense, perfect aspect and continuous aspect («I have been eating»)?", "Present perfect continuous", ["Past continuous", "Past perfect", "Future perfect"],
  "Indica un'azione iniziata nel passato e ancora in corso.", *PP, "English also has a present perfect continuous")
SP_ = ("Simple past", "Simple-past")
E("eng-060", "Verb tenses", 1, "What is the simple past of «study»?", "studied", ["studyed", "studed", "studies"],
  "Consonante + y → -ied.", *SP_, "verbs ending in -y change to -ied")
E("eng-061", "Verb tenses", 1, "What is the simple past of «stop»?", "stopped", ["stoped", "stopt", "stops"],
  "Consonante + vocale + consonante: si raddoppia la consonante finale.", *SP_, "double the final consonant")
E("eng-062", "Verb tenses", 1, "What is the simple past of «live»?", "lived", ["liveed", "livd", "lives"],
  "I verbi in -e aggiungono solo -d.", *SP_, "verbs ending in -e add only –d")
E("eng-063", "Verb tenses", 1, "Complete: «They ___ at home yesterday.»", "were", ["was", "are", "been"],
  "be ha due forme al passato: was (I/he/she/it) e were (le altre).", *SP_, "the copula verb be has two past tense forms")
E("eng-064", "Verb tenses", 2, "Complete: «We turned the oven off two minutes ___.»", "ago", ["since", "for", "before now"],
  "ago si usa con il simple past.", *SP_, "We turned the oven off two minutes ago")
E("eng-065", "Verb tenses", 2, "Which auxiliary is used to form questions and negatives in the simple past?", "did", ["was", "had", "does"],
  "Es. «When did they get married?», «I didn't go».", *SP_, "use the auxiliary did")
E("eng-066", "Verb tenses", 2, "Does the simple past add -s for the third person singular?", "No, it has the same form for all persons (except be)", ["Yes, always", "Only for regular verbs", "Only in questions"],
  "Es. I/you/he helped.", *SP_, "there is no addition of -s for the third person singular")


# --- Blocco 3: futuro, question tags, discorso indiretto, gerundio, nomi numerabili, do-support ---
GT = ("Going-to future", "Going-to-future")
E("eng-067", "Future", 1, "Complete: «Look at those clouds! It ___ rain.»", "is going to", ["goes to", "will to", "is go to"],
  "be going to esprime un evento imminente con indizi presenti.", *GT, "It's going to rain")
E("eng-068", "Future", 2, "How is the going-to future formed?", "be (am/is/are) + going to + infinitive", ["will + going + infinitive", "go + to + -ing", "have + going to"],
  "Es. «I am going to visit Paris».", *GT, "It is made using appropriate forms of the expression to be going to")
E("eng-069", "Future", 2, "«I'm going to visit Paris someday» mainly expresses:", "an intention", ["a past habit", "an obligation", "a certainty about the past"],
  "be going to può esprimere intenzione o imminenza.", *GT, "which expresses intention but not imminence")
E("eng-070", "Future", 2, "What is the colloquial contracted form of «going to»?", "gonna", ["wanna", "gotta", "goin'"],
  "Tipico dell'inglese parlato informale.", *GT, "with the colloquial form gonna")
E("eng-071", "Future", 3, "Which future form is often used to announce a decision at the moment it is made («The phone is ringing – I'll answer it»)?", "will", ["be going to", "present perfect", "used to"],
  "Voce «Going-to future».", *GT, "The will future is often used for announcing a decision at the time when it is made")
TQ = ("Tag question", "Tag-question")
E("eng-072", "Question tags", 1, "Complete: «You're John, ___?»", "aren't you", ["are you", "isn't it", "don't you"],
  "Frase affermativa → tag negativo con lo stesso ausiliare.", *TQ, "You're John, aren't you?")
E("eng-073", "Question tags", 2, "Complete: «You don't remember my name, ___?»", "do you", ["don't you", "are you", "remember you"],
  "Frase negativa → tag positivo.", *TQ, "You don't remember my name, do you?")
E("eng-074", "Question tags", 2, "Complete: «Let's start, ___?»", "shall we", ["will you", "don't we", "let we"],
  "Con «let's» il tag è «shall we?».", *TQ, "Let's start, shall we?")
E("eng-075", "Question tags", 3, "In standard British/American English, what is the tag for «I'm clever, ___?»", "aren't I", ["amn't I", "am not I", "isn't I"],
  "«amn't I» è scozzese/irlandese; «ain't I» non standard.", *TQ, "Clever, aren't I?")
E("eng-076", "Question tags", 3, "Complete: «Be careful, ___?»", "will you", ["do you", "are you", "be you"],
  "Dopo un imperativo si usa spesso «will you?» / «won't you?».", *TQ, "Be careful, will you?")
IS = ("Indirect speech", "Indirect-speech")
E("eng-077", "Reported speech", 2, "Direct: Jill said, «I'm coming». Reported:", "Jill said she was coming.", ["Jill said I'm coming.", "Jill said she is come.", "Jill said she coming."],
  "Cambiano persona e tempo verbale.", *IS, "Jill said she was coming")
E("eng-078", "Reported speech", 3, "Direct: «I shall come to your party tomorrow». Reported:", "I said that I would come to his party the next day.", ["I said that I shall come to his party tomorrow.", "I said that I will came to his party tomorrow.", "I said I come to his party the next day."],
  "shall → would; tomorrow → the next day.", *IS, "I said that I would come to his party the next day")
E("eng-079", "Reported speech", 3, "Direct: «Will you come to my party tomorrow?» Reported:", "I asked if she would come to my party the next day.", ["I asked will she come to my party tomorrow.", "I asked if would she come to my party.", "I asked she will come to my party."],
  "Domanda indiretta con if + ordine soggetto-verbo.", *IS, "I asked if he/she would come to my party the next day")
E("eng-080", "Reported speech", 3, "In reported speech, «tomorrow» usually becomes:", "the next day / the following day", ["yesterday", "today", "the day before"],
  "Cambiano anche le espressioni di tempo.", *IS, "the next day/the following day")
GER = ("Gerund", "Gerund")
E("eng-081", "Gerund and infinitive", 1, "Complete: «I enjoy ___.»", "reading", ["to read", "read", "reads"],
  "enjoy è seguito dalla forma in -ing.", *GER, "I enjoy reading")
E("eng-082", "Gerund and infinitive", 2, "Complete: «___ is fun.» (= nuotare è divertente)", "Swimming", ["Swim", "To swimming", "Swims"],
  "Il gerundio può fare da soggetto.", *GER, "Swimming is fun")
E("eng-083", "Gerund and infinitive", 2, "Complete: «You should avoid ___ late.»", "arriving", ["to arrive", "arrive", "arrived"],
  "avoid è seguito dalla forma in -ing.", *GER, "avoid, (not) bother, escape, evade")
E("eng-084", "Gerund and infinitive", 2, "Complete: «He gave up ___.» (= ha smesso di fumare)", "smoking", ["to smoke", "smoke", "smoked"],
  "give up + -ing.", *GER, "give over, give up, go about")
MN = ("Mass noun", "Mass-noun")
E("eng-085", "Countable and uncountable", 1, "Which of these is an uncountable (mass) noun?", "water", ["chair", "book", "apple"],
  "Si dice «20 litres of water», non «20 waters».", *MN, "the mass noun \"water\" is quantified as \"20 litres of water\"")
E("eng-086", "Countable and uncountable", 1, "Complete: «How ___ water do you drink?»", "much", ["many", "a", "few"],
  "much con i non numerabili, many con i numerabili.", *MN, "though note the different quantifiers \"much\" and \"many\"")
E("eng-087", "Countable and uncountable", 1, "Complete: «How ___ chairs are there?»", "many", ["much", "a lot", "little"],
  "many con i numerabili plurali.", *MN, "\"so many chairs\"")
E("eng-088", "Countable and uncountable", 2, "Which is correct?", "some furniture", ["a furniture", "two furnitures", "many furnitures"],
  "furniture è non numerabile; chair è numerabile.", "Count noun", "Count-noun", "\"seven chairs\" and \"some furniture\"")
E("eng-089", "Countable and uncountable", 2, "Can an uncountable noun take the indefinite article «a/an»?", "No (e.g. not «a water»)", ["Yes, always", "Only in the plural", "Only with adjectives"],
  "Voce «Mass noun».", *MN, "by the impossibility of being combined with an indefinite article")
E("eng-090", "Countable and uncountable", 3, "Do uncountable nouns take singular or plural verbs in English?", "Singular verbs (e.g. «the water is cold»)", ["Plural verbs", "Either", "No verb"],
  "Voce «Mass noun».", *MN, "although in English they take singular verb forms")
E("eng-091", "Countable and uncountable", 3, "Which determiners can be used with both countable and uncountable nouns?", "all, no, some", ["every, each, several", "many, few, a", "a, an, one"],
  "every/each/several vanno solo con i numerabili.", "Count noun", "Count-noun", "Some determiners can be used with both mass and count nouns, including \"all\", \"no\", and \"some\"")
DS = ("Do-support", "Do-support")
E("eng-092", "Questions and negatives", 1, "Which question is correct in modern English?", "Do you know him?", ["Know you him?", "You know him?", "Does you know him?"],
  "Senza altro ausiliare si usa do.", *DS, "today's English usually substitutes Do you know him?")
E("eng-093", "Questions and negatives", 1, "How do you make «I know» negative?", "I don't know.", ["I know not.", "I not know.", "I no know."],
  "«I know not» è arcaico.", *DS, "the auxiliary do is used to produce a form like I do not (don't) know")
E("eng-094", "Questions and negatives", 2, "Is do-support used with «be»? (e.g. «I ___ not tired»)", "No: «I am not tired»", ["Yes: «I do not be tired»", "Yes: «I don't am tired»", "Only in questions"],
  "Non si usa do con be o con altri ausiliari.", *DS, "Do-support is not used when there is already an auxiliary or copular verb present")
E("eng-095", "Questions and negatives", 3, "In «I did shut the fridge», what is the function of «did»?", "Emphasis", ["Negation", "Question", "Passive"],
  "do può dare enfasi anche in frasi affermative.", *DS, "usually as a means of adding emphasis")
IMP = ("Imperative mood", "Imperative-mood")
E("eng-096", "Imperative", 1, "How is the English imperative formed?", "With the bare infinitive (e.g. «Go!»)", ["With to + infinitive", "With the -ing form", "With will + infinitive"],
  "Il soggetto «you» è di solito sottinteso.", *IMP, "In English, the imperative is formed using the bare infinitive form of the verb")
E("eng-097", "Imperative", 1, "What is the negative imperative of «touch me»?", "Don't touch me!", ["Not touch me!", "No touch me!", "Touch me not!"],
  "Si usa do not.", *IMP, "the imperative is negated using do not, as in \"Don't touch me!\"")
E("eng-098", "Imperative", 2, "Which form expresses a first-person plural suggestion (= facciamo…)?", "Let's (do something)", ["We do!", "Do we!", "Shall do!"],
  "Es. «Let's go!».", *IMP, "with the meaning of \"let's (do something)\"")
HAB = ("English markers of habitual aspect", "English-markers-of-habitual-aspect")
E("eng-099", "Used to", 2, "Complete: «When I was a child, I ___ play football every day.» (abitudine passata)", "used to", ["use to", "am used to", "was use to"],
  "used to + infinito per le abitudini passate.", *HAB, "used to as in we used to go there")
E("eng-100", "Used to", 3, "Which other construction can express a past habit, especially in stories?", "would + infinitive", ["will + infinitive", "have + past participle", "be + -ing"],
  "Es. «We would often have a drink after class».", *HAB, "The form [would + infinitive] is employed to talk about a habit or frequent action in a former time")
E("eng-101", "Used to", 2, "Which tense is used for present habits (e.g. «I ___ there every Thursday»)?", "simple present: «I go»", ["present continuous: «I am going»", "used to: «I use to go»", "present perfect: «I have gone»"],
  "Non esiste un marcatore speciale per le abitudini presenti.", *HAB, "the simple present is used, as in I go there (every Thursday)")
QW = ("Interrogative word", "Interrogative-word")
E("eng-102", "Questions and negatives", 1, "Which question word asks about a place?", "where", ["when", "who", "why"],
  "when = tempo, who = persona, why = causa.", *QW, "such as what, which, when, where, who, whom, whose, why, whether and how")
E("eng-103", "Questions and negatives", 2, "Why are question words often called «wh-words»?", "Because most of them start with wh-", ["Because they are always at the end", "Because they come from Welsh", "Because they need «what»"],
  "what, which, when, where, who, why…", *QW, "They are sometimes called wh-words, because in English most of them start with wh-")
E("eng-104", "Questions and negatives", 2, "Which is an indirect question?", "I wonder where he is going.", ["Where is he going?", "Where he is going?", "Is where he going?"],
  "Nelle domande indirette l'ordine è soggetto + verbo.", *QW, "I wonder where he is going")
FF = ("False friend", "False-friend")
E("eng-105", "Vocabulary", 2, "What does the English word «parents» mean?", "Genitori", ["Parenti", "Padroni", "Paesani"],
  "È un falso amico: «parenti» si dice relatives.", *FF, "Italian parenti (the latter two both meaning 'relatives')")
E("eng-106", "Vocabulary", 2, "What does the English verb «to demand» mean?", "Esigere, pretendere", ["Domandare", "Rispondere", "Dimenticare"],
  "«Domandare» si dice to ask.", *FF, "English demand and French demander ('ask')")
E("eng-107", "Vocabulary", 1, "What is a «false friend»?", "A word similar in form to one in another language but with a different meaning", ["A synonym", "An idiom", "A wrong spelling"],
  "Es. embarrassed ≠ embarazada.", *FF, "a false friend is a word in a different language that looks or sounds similar to a word in a given language, but differs significantly in meaning")
CT = ("Contraction (grammar)", "Contraction-grammar")
E("eng-108", "Contractions", 1, "What is the contraction of «I am»?", "I'm", ["Im'", "I'am", "I's"],
  "La vocale omessa è sostituita dall'apostrofo.", *CT, "as in I'm for \"I am\"")
E("eng-109", "Contractions", 2, "Are contractions like «don't» recommended in formal writing?", "They tend to be avoided in formal writing", ["Yes, always", "They are compulsory", "Only in legal texts"],
  "Sono comuni nel parlato e nella scrittura informale.", *CT, "tend to be avoided in more formal writing")
E("eng-110", "Contractions", 2, "What does «won't» stand for?", "will not", ["would not", "was not", "want not"],
  "Contrazione irregolare.", *CT, "English has a number of contractions")


# --- Blocco 4: tempi progressivi e perfetti, verbi, infinito, aggettivi, numeri, domande ---
CPA = ("Continuous and progressive aspects", "Continuous-and-progressive-aspects")
def V(id, arg, liv, testo, giusta, sbagliate, spieg, frase):
    D(id, arg, liv, testo, giusta, sbagliate, spieg, W("Uses of English verb forms"), USE, frase)

E("eng-111", "Verb tenses", 1, "How is the continuous (progressive) aspect formed?", "be + present participle (-ing)", ["have + past participle", "do + infinitive", "will + infinitive"],
  "Es. «I am reading», «he was playing».", *CPA, "The continuous aspect is constructed by using a form of the copula, \"to be\", together with the present participle")
E("eng-112", "Verb tenses", 2, "Complete: «Andrew ___ tennis when Jane called him.»", "was playing", ["played", "has played", "is playing"],
  "Past continuous: azione in corso in un momento del passato.", *CPA, "Andrew was playing tennis when Jane called him")
E("eng-113", "Verb tenses", 3, "«Andrew was playing tennis when Jane called him» tells us:", "what Andrew was doing at that moment, not how long he played", ["that Andrew plays tennis every day", "that the game was finished", "that Jane played tennis"],
  "Per azioni concluse si usa il simple past.", *CPA, "but does not indicate for how long Andrew played")
V("eng-114", "Verb tenses", 2, "Which tense describes a permanent situation, as in «We ___ in Dallas»?", "simple present: live", ["present continuous: are living", "present perfect: have lived", "simple past: lived"],
  "Il simple present esprime stati permanenti e abitudini.", "We live in Dallas")
V("eng-115", "Verb tenses", 3, "What does the progressive aspect usually denote?", "A temporary action or state that began earlier and continues", ["A completed past action", "A permanent truth", "A future decision"],
  "Es. «I am working from home this week».", "The progressive or continuous aspect is used to denote a temporary action or state")
V("eng-116", "Verb tenses", 3, "For an action ongoing at a past moment, which form is generally used?", "past progressive", ["simple present", "future perfect", "present perfect"],
  "Es. «I was cooking when you arrived».", "for action that was ongoing at the time referred to, the past progressive is generally used instead")
FP = ("Future perfect", "Future-perfect")
E("eng-117", "Verb tenses", 2, "Complete: «I ___ by tomorrow.» (= avrò finito)", "will have finished", ["will finish", "have finished", "would finish"],
  "Future perfect: will + have + participio passato.", *FP, "I will have finished by tomorrow")
E("eng-118", "Verb tenses", 3, "Complete: «She ___ asleep by the time we get home.»", "will have fallen", ["will fall", "has fallen", "falls"],
  "Azione che sarà conclusa prima di un momento futuro.", *FP, "She will have fallen asleep by the time we get home")
PLP = ("Pluperfect", "Pluperfect")
E("eng-119", "Verb tenses", 2, "What is the past perfect (pluperfect) used for?", "An action completed before another past moment", ["A future plan", "A present habit", "A general truth"],
  "Es. «We had arrived before the game began».", *PLP, "\"we had arrived\" before the game began")
E("eng-120", "Verb tenses", 2, "How is the past perfect formed?", "had + past participle", ["has + past participle", "was + -ing", "would + infinitive"],
  "Corrisponde al trapassato prossimo italiano.", *PLP, "usually called past perfect in English")
E("eng-121", "Verb tenses", 3, "Complete: «They ___ for an hour when the bell rang.»", "had been writing", ["have been writing", "were write", "had wrote"],
  "Past perfect continuous.", *PLP, "\"they had been writing\" when the bell rang")
EV = ("English verbs", "English-verbs")
E("eng-122", "Verb forms", 1, "Complete: «She ___ in a bank.» (lavora)", "works", ["work", "working", "is work"],
  "Al presente la terza persona singolare prende -s.", *EV, "a third person singular present tense form ending in -s")
E("eng-123", "Verb forms", 2, "About how many irregular verbs are there in English?", "About 200", ["About 20", "About 2,000", "None"],
  "L'irregolarità riguarda quasi sempre passato e participio.", *EV, "although there are about 200 irregular verbs")
E("eng-124", "Verb forms", 1, "What are the three forms (infinitive, past, past participle) of «go»?", "go – went – gone", ["go – goed – goed", "go – gone – went", "go – went – went"],
  "Verbo irregolare: le irregolarità riguardano passato e participio.", *EV, "the irregularity in nearly all cases concerns the past tense and past participle forms")
E("eng-125", "Verb forms", 1, "What is the past simple of «see»?", "saw", ["seen", "seed", "sawn"],
  "see – saw – seen.", *EV, "the irregularity in nearly all cases concerns the past tense and past participle forms")
E("eng-126", "Verb forms", 1, "What is the past participle of «write»?", "written", ["wrote", "writed", "writ"],
  "write – wrote – written.", *EV, "the irregularity in nearly all cases concerns the past tense and past participle forms")
E("eng-127", "Verb forms", 2, "What is the past simple of «buy»?", "bought", ["buyed", "brought", "boughten"],
  "buy – bought – bought; attenzione a bring – brought.", *EV, "the irregularity in nearly all cases concerns the past tense and past participle forms")
E("eng-128", "Verb forms", 2, "What is the past participle of «take»?", "taken", ["took", "taked", "tooken"],
  "take – took – taken.", *EV, "the irregularity in nearly all cases concerns the past tense and past participle forms")
E("eng-129", "Verb forms", 2, "Which list contains all the forms of «be»?", "be, am, is, are, was, were, been, being", ["be, is, was, been", "am, are, were, being", "be, am, is, are, was, were"],
  "be è il verbo più irregolare.", *EV, "with the forms be, am, is, are, was, were, been and being")
E("eng-130", "Verb forms", 3, "In standard English, which sentence is correct?", "Have they gone yet?", ["Have they went yet?", "Have they go yet?", "Have they goed yet?"],
  "«have they went» è considerato non standard.", *EV, "have they went yet?")
INF = ("Infinitive", "Infinitive")
E("eng-131", "Gerund and infinitive", 2, "In «I can go there», what form is «go»?", "the bare infinitive", ["the to-infinitive", "the gerund", "the past participle"],
  "Dopo i modali si usa l'infinito senza to.", *INF, "The form without to is called the bare infinitive")
E("eng-132", "Gerund and infinitive", 2, "What is a «split infinitive»?", "An adverb placed between «to» and the verb (e.g. to happily sit)", ["An infinitive without to", "A verb in the past", "Two infinitives together"],
  "Es. «I expect to happily sit here».", *INF, "I expect to happily sit here")
E("eng-133", "Gerund and infinitive", 2, "Complete: «I want ___ a car.»", "to buy", ["buy", "buying", "bought"],
  "want è seguito dal to-infinitive.", *INF, "to buy a car")
ADJ = ("Adjective", "Adjective")
E("eng-134", "Adjectives", 3, "Which phrase has the correct adjective order?", "a beautiful small old red Italian car", ["a red small beautiful old Italian car", "an Italian red old small beautiful car", "a small beautiful Italian old red car"],
  "Ordine: opinione, dimensione, età/forma, colore, origine, materiale, scopo.", *ADJ, "opinion, size, age or shape, colour, origin, material, purpose")
E("eng-135", "Adjectives", 2, "In «My kids are happy», «happy» is:", "a predicative adjective", ["an attributive adjective", "an adverb", "a noun"],
  "Segue un verbo copulativo.", *ADJ, "as a predicative adjective, e.g. \"My kids are happy\"")
E("eng-136", "Adjectives", 2, "Where do English attributive adjectives usually go?", "Before the noun (e.g. a funny idea)", ["After the noun", "At the end of the sentence", "After the verb"],
  "Es. «That used to be an immensely funny idea».", *ADJ, "That used to be an immensely funny idea. (Prepositive attributive)")
ADV = ("English adverbs", "English-adverbs")
E("eng-137", "Adverbs", 1, "How are many English adverbs formed?", "Adjective + -ly (e.g. final → finally)", ["Adjective + -er", "Noun + -ness", "Verb + -ing"],
  "Es. probably, especially, finally.", *ADV, "derived from adjectives + the suffix -ly")
E("eng-138", "Adverbs", 2, "Which of these is an adverb that does NOT end in -ly?", "fast", ["quickly", "slowly", "carefully"],
  "fast, well, right, very sono avverbi semplici.", *ADV, "These include not, well, fast, right, and very")
E("eng-139", "Adverbs", 2, "Which adverbs take part in negation?", "not and never", ["very and too", "here and there", "soon and late"],
  "Voce «English adverbs».", *ADV, "The words not and never are adverbs that participate in negation")
DET = ("English determiners", "English-determiners")
E("eng-140", "Determiners", 3, "Complete: «___ answer is correct: both are wrong.»", "Neither", ["Either", "Both", "None"],
  "either/neither indicano una scelta tra esattamente due elementi.", *DET, "They also imply a single selection from a set of exactly two")
E("eng-141", "Determiners", 3, "After «either» or «neither», is the noun singular or plural?", "Singular (e.g. either side)", ["Plural", "Uncountable only", "It depends on the verb"],
  "Segnalano una sola scelta.", *DET, "disjunctive determiners select singular nouns")
E("eng-142", "Determiners", 2, "Which of these is a determiner?", "each", ["quickly", "beautiful", "run"],
  "Determinanti: the, a, each, some, which, this, numerali…", *DET, "are words – such as the, a, each, some, which, this, and numerals such as five")
NUM = ("English numerals", "English-numerals")
E("eng-143", "Numbers", 1, "How do you write 45 in words?", "forty-five", ["fourty-five", "forty five-", "fourtyfive"],
  "Tra 21 e 99 si usa il trattino.", *NUM, "the number is typically written as two words separated by a hyphen")
E("eng-144", "Numbers", 2, "Which is correct?", "three hundred people", ["three hundreds people", "three hundreds of people", "three hundred of people"],
  "hundred resta al singolare dopo un numero.", *NUM, "the word hundred remains in its singular form regardless of the number preceding it")
E("eng-145", "Numbers", 2, "What do ordinal numbers (first, second, third…) indicate?", "A position in a sequence", ["A quantity", "A fraction", "A date only"],
  "I cardinali indicano la quantità.", *NUM, "Ordinal numbers refer to a position")
E("eng-146", "Numbers", 2, "How many is «half a dozen»?", "6", ["12", "5", "15"],
  "A dozen = 12.", *NUM, "6: half a dozen")
E("eng-147", "Numbers", 3, "In modern English, a «billion» is:", "a thousand million (10⁹)", ["a million million (10¹²)", "a hundred million", "a thousand billion"],
  "Il «long scale» britannico (milione di milioni) è obsoleto.", *NUM, "a billion is used for a million million")
HOM = ("Homophone", "Homophone")
E("eng-148", "Vocabulary", 2, "«to», «too» and «two» are:", "homophones (same sound, different spelling)", ["synonyms", "antonyms", "false friends"],
  "Gli omofoni con grafia diversa si dicono anche eterografi.", *HOM, "Homophones that are spelled differently are also called heterographs, e.g. to, too, and two")
E("eng-149", "Vocabulary", 3, "«rain», «reign» and «rein» are an example of:", "homophones", ["plurals", "phrasal verbs", "compound nouns"],
  "Stessa pronuncia, significato e grafia diversi.", *HOM, "or spelled differently, as in rain, reign, and rein")
QST = ("Question", "Question")
E("eng-150", "Questions and negatives", 1, "«Are you hungry?» is a:", "yes–no question", ["wh-question", "tag question", "alternative question"],
  "Si risponde con sì o no.", *QST, "yes–no questions (such as \"Are you hungry?\")")
E("eng-151", "Questions and negatives", 2, "«Do you want jam or marmalade?» is a:", "alternative question", ["yes–no question", "open question", "tag question"],
  "Offre una scelta tra alternative.", *QST, "alternative questions (such as \"Do you want jam or marmalade?\")")
E("eng-152", "Questions and negatives", 2, "«What is your name?» is an example of:", "an open (wh-) question", ["a closed question", "a yes–no question", "a tag question"],
  "Ammette infinite risposte possibili.", *QST, "An open question, such as \"What is your name?\"")
CMPD = ("English compound", "English-compound")
E("eng-153", "Vocabulary", 3, "How can English compound words be written?", "Open, hyphenated or solid (closed up)", ["Only as one word", "Only with a hyphen", "Only as separate words"],
  "Es. ice cream, mother-of-pearl, notebook.", *CMPD, "Orthography: open, hyphenated, or solid (closed up)")


# --- Blocco 5: modali, periodo ipotetico, passivo, relative, verbi irregolari ---
def X(file, voce):
    return lambda id, arg, liv, testo, giusta, sbagliate, spieg, frase: D(id, arg, liv, testo, giusta, sbagliate, spieg, W(voce), file, frase)
Mo = X(MOD, "English modal auxiliary verbs")
Co = X(CON, "English conditional sentences")
Pa = X(PAS, "English passive voice")
Re = X(REL, "English relative clauses")
IRR = "the irregularity in nearly all cases concerns the past tense and past participle forms"

_q = [
 (Mo, "Modal verbs", 2, "Which is the past form of «I can swim» (ability)?", "I could swim", ["I canned swim", "I can swam", "I could swam"], "could è il passato di can per l'abilità.", "I could swim may serve as a past form of I can swim"),
 (Mo, "Modal verbs", 2, "Which expression can replace «can» in tenses where «can» has no form (e.g. future)?", "be able to", ["be allowed to", "have to", "ought"], "Es. «I will be able to come».", "replaced by be able to"),
 (Mo, "Modal verbs", 2, "Which expression can replace «may» meaning permission?", "be allowed to", ["be able to", "have to", "used to"], "Es. «You are allowed to leave».", "can be replaced by be allowed to"),
 (Mo, "Modal verbs", 2, "Which expression can replace «must» in most meanings?", "have to", ["ought", "may", "would"], "Es. «I had to work» (passato di must).", "The modal must in most meanings can be replaced by have to"),
 (Mo, "Modal verbs", 1, "Complete: «She ___ speak three languages.»", "can", ["cans", "can to", "is can"], "I modali non prendono -s alla terza persona e non vogliono to.", "They can most easily be distinguished from other verbs by their defectiveness"),
 (Mo, "Modal verbs", 2, "What is the negative contracted form of «must»?", "mustn't", ["don't must", "mustn", "not must"], "Si nega aggiungendo not al modale.", "mustn't"),
 (Mo, "Modal verbs", 2, "Complete the suggestion: «___ I read now?»", "Shall", ["Will", "Must", "Do"], "shall nelle richieste di consiglio o proposte.", "Shall I read now?"),
 (Mo, "Modal verbs", 2, "Which properties do modal verbs mainly express?", "Possibility and obligation (modality)", ["Tense and aspect only", "Number and gender", "Plural forms"], "Es. may, might, must.", "used mostly to express modality, properties such as possibility and obligation"),
 (Mo, "Modal verbs", 3, "Which verbs are also usually classed as modals, in addition to the central ones?", "ought, dare and need", ["have, be and do", "get, go and come", "want, like and love"], "In alcuni usi.", "A few other verbs are usually also classed as modals: ought"),
 (Co, "Conditionals", 2, "Complete: «If it rains this afternoon, we ___ find somewhere to shelter.»", "can", ["could have", "would have", "had"], "First conditional: if + present, modale nella principale.", "If it rains this afternoon, we can/could/should/may/might find somewhere to shelter"),
 (Co, "Conditionals", 2, "Which sentence correctly uses an imperative in a first conditional?", "If it rains this afternoon, come round to my place!", ["If it will rain, come round!", "If it rained, come round to my place!", "If it rains, you came round!"], "Nella proposizione con if si usa il present simple.", "If it rains this afternoon, come round to my place!"),
 (Co, "Conditionals", 2, "Which word can introduce a condition with the meaning «if not»?", "unless", ["until", "while", "since"], "Es. «Unless you hurry, you'll miss the bus».", "such as whenever, unless, provided (that), and as long as"),
 (Co, "Conditionals", 1, "Complete the zero conditional (general truth): «If you heat ice, it ___.»", "melts", ["will melt", "would melt", "melted"], "Zero conditional: if + present, present.", "zero conditional"),
 (Co, "Conditionals", 2, "Complete the second conditional: «If I had more money, I ___ a new car.»", "would buy", ["will buy", "would have bought", "buy"], "Second conditional: if + past, would + infinito.", "second conditional (or conditional II)"),
 (Co, "Conditionals", 3, "«If I were to be king, I could…» is a:", "future less vivid conditional", ["zero conditional", "third conditional", "mixed conditional"], "were + to + infinito.", "If I were to be king, I could have you thrown"),
 (Co, "Conditionals", 3, "Complete the third conditional: «If she had studied, she ___ the exam.»", "would have passed", ["would pass", "will pass", "had passed"], "if + past perfect, would have + participio.", "third conditional (or conditional III)"),
 (Co, "Conditionals", 2, "Which other expressions can introduce a condition besides «if»?", "provided (that), as long as", ["although, though", "because, since", "so, therefore"], "Voce «English conditional sentences».", "such as whenever, unless, provided (that), and as long as"),
 (Pa, "Passive voice", 2, "Why is the passive used in «Three stores were robbed last night»?", "Because the agent may be unknown", ["Because the stores did the action", "Because it is a future event", "Because it is a question"], "Il passivo omette l'agente.", "Three stores were robbed last night (the identity of the agent may be unknown)"),
 (Pa, "Passive voice", 2, "Which tense is «A new cancer drug has been discovered»?", "Present perfect passive", ["Simple past active", "Past perfect passive", "Future passive"], "has been + participio passato.", "A new cancer drug has been discovered"),
 (Pa, "Passive voice", 3, "In «Mistakes have been made», why might the speaker use the passive?", "To avoid identifying who made the mistakes", ["Because mistakes are people", "Because it is more informal", "To express the future"], "Voce «English passive voice».", "Mistakes have been made on this project (the speaker may not wish to identify the agent)"),
 (Pa, "Passive voice", 3, "Which sentence is an example of the «get-passive»?", "Don't get killed.", ["Don't kill.", "He killed them.", "They are killing."], "get + participio passato.", "Don't get killed"),
 (Pa, "Passive voice", 2, "Complete: «Have you ever ___ by an elephant?»", "been kicked", ["kicked", "being kicked", "be kicked"], "Present perfect passivo.", "you ever been kicked by an elephant"),
 (Pa, "Passive voice", 2, "Turn into the passive: «Someone robbed three stores.»", "Three stores were robbed.", ["Three stores robbed.", "Three stores have rob.", "Three stores was robbed."], "be (al tempo dell'attivo) + participio passato.", "Three stores were robbed last night"),
 (Re, "Relative clauses", 3, "When is «whom» used?", "When the antecedent is the object of the relative clause", ["When the antecedent is the subject", "Only for things", "Only in questions"], "Es. «the man whom I met».", "whom is used only when its antecedent is the object of the relative clause"),
 (Re, "Relative clauses", 2, "In «This is the man I saw», what has been omitted?", "The relative pronoun (that/who)", ["The subject", "The verb", "The article"], "Il pronome relativo oggetto si può omettere.", "In some cases the relative pronoun may be omitted"),
 (Re, "Relative clauses", 3, "How is a non-restrictive relative clause usually marked in writing?", "With commas", ["With brackets only", "With a dash only", "It is not marked"], "Es. «My teacher, who…, …».", "a non-restrictive relative clause is surrounded by pauses in speech and usually by commas in writing"),
 (Re, "Relative clauses", 2, "Complete: «My car, ___ is ten years old, still works.»", "which", ["who", "that", "whom"], "which per le cose; in una non-restrittiva non si usa that.", "who and which may be used in both restrictive and non-restrictive clauses"),
]
for n, (f, arg, liv, t, g, s, sp, fr) in enumerate(_q, start=154):
    f(f"eng-{n:03d}", arg, liv, t, g, s, sp, fr)

E("eng-181", "Verb forms", 1, "What is the past simple of «bring»?", "brought", ["bringed", "brang", "bought"], "bring – brought – brought.", *EV, IRR)
E("eng-182", "Verb forms", 1, "What is the past simple of «think»?", "thought", ["thinked", "thank", "taught"], "think – thought – thought.", *EV, IRR)
E("eng-183", "Verb forms", 2, "What is the past participle of «begin»?", "begun", ["began", "beginned", "begin"], "begin – began – begun.", *EV, IRR)
E("eng-184", "Verb forms", 2, "What is the past participle of «speak»?", "spoken", ["spoke", "speaked", "spoked"], "speak – spoke – spoken.", *EV, IRR)
E("eng-185", "Verb forms", 1, "What is the past simple of «teach»?", "taught", ["teached", "thought", "tought"], "teach – taught – taught.", *EV, IRR)
E("eng-186", "Verb forms", 1, "What is the past simple of «leave»?", "left", ["leaved", "lefted", "leave"], "leave – left – left.", *EV, IRR)
E("eng-187", "Verb forms", 2, "What are the past forms of «choose»?", "chose – chosen", ["choosed – choosed", "chosen – chose", "chose – chose"], "choose – chose – chosen.", *EV, IRR)
E("eng-188", "Verb forms", 2, "What is the past participle of «do»?", "done", ["did", "doed", "do"], "do – did – done; «I seen it, he done it» è non standard.", *EV, "I seen it, he done it")
E("eng-189", "Verb tenses", 1, "Complete: «I ___ born in 1980.»", "was", ["am", "have been", "were"], "Simple past di be.", *SP_, "I was born in 1980")
E("eng-190", "Verb tenses", 2, "Complete: «When ___ they get married?»", "did", ["do", "have", "were"], "Domanda al simple past con did + infinito.", *SP_, "When did they get married?")
E("eng-191", "Verb tenses", 2, "Which tense is mainly used to describe finished events in the past?", "simple past", ["present perfect continuous", "simple present", "future perfect"], "Es. «I came home at 6 o'clock».", *SP_, "It is used principally to describe events in the past")
E("eng-192", "Articles", 2, "Complete: «The boy was looking at ___ moon.»", "the", ["a", "an", "—"], "Referente unico o noto: articolo determinativo.", *ART, "The boy with glasses was looking at the moon")
E("eng-193", "Possessive", 2, "In «women's shoes», the possessive expresses:", "for whom something is intended", ["who physically owns the shoes", "a plural only", "the material"], "Si parafrasa con for: shoes for women.", *POS, "expresses for whom something is intended")
E("eng-194", "Gerund and infinitive", 1, "Complete: «I like ___.» (nuotare)", "swimming", ["swim", "swims", "swam"], "Gerundio come complemento oggetto.", *GER, "I like swimming")
E("eng-195", "Plurals", 1, "What is the plural of «child»?", "children", ["childs", "childes", "childrens"], "Plurale irregolare.", *PLU, "0.5 children per woman")
E("eng-196", "Comparatives", 3, "Which comparatives are both acceptable for the two-syllable adjective «polite»?", "politer / more polite", ["politest / most polite", "more politer", "politelier"], "Con due sillabe alcuni aggettivi ammettono entrambe le forme.", *CMP, "polite can use politer or more polite")
E("eng-197", "Comparatives", 3, "What is the superlative of inferiority of «big»?", "least big", ["less big", "biggest", "most big"], "less = comparativo di minoranza, least = superlativo.", *CMP, "least big and least fully [superlative of inferiority]")
E("eng-198", "Question tags", 2, "Complete: «I'll make tea, ___?»", "shall I", ["will I", "won't I", "do I"], "Offerta con «shall I?».", *TQ, "I'll make tea, shall I?")
E("eng-199", "Phrasal verbs", 2, "Which of these is a phrasal verb meaning «rifiutare»?", "turn down", ["sit up", "run into", "get together"], "Es. «She turned down the offer».", *PV, "turn down, run into, or sit up")
E("eng-200", "Reported speech", 3, "Direct: «I can get it for free». Reported (past reporting verb):", "He said that he could get it for free.", ["He said that he can got it for free.", "He said that I could get it for free.", "He said he gets it for free."], "can → could nel discorso indiretto.", *IS, "He said that he could get it for free")

# --- Ampliamento a 300: preposizioni, determinanti, infinito, nomi, composti, verbi, numeri, avverbi ---
PRE = ("English prepositions", "English-prepositions")
E("eng-201", "Prepositions", 2, "Which of these words is a preposition?", "on", ["quickly", "beautiful", "they"],
  "Le preposizioni (of, in, on, at, from…) introducono un sintagma preposizionale.", *PRE, "English prepositions are words – such as of, in, on, at, from, etc.")
E("eng-202", "Prepositions", 3, "What do English prepositions most typically express?", "Relations in space and time", ["Actions and events", "Qualities of nouns", "Questions"],
  "Es. «in the water», «at noon».", *PRE, "Semantically, they most typically denote relations in space and time")
E("eng-203", "Prepositions", 3, "Complete: «Come and sit near ___.»", "me", ["I", "my", "mine"],
  "Dopo una preposizione si usa il pronome complemento (near me, at her).", *PRE, "we expect to see prepositional phrases like near me and at her rather than near I and at she")
E("eng-204", "Prepositions", 4, "Are prepositions an open or a closed class of words?", "A closed lexical category", ["An open class, new ones are created every year", "They are a kind of verb", "They are a kind of noun"],
  "Le preposizioni sono poche e non flettono.", *PRE, "They form a closed lexical category")
E("eng-205", "Prepositions", 4, "Which English preposition typically corresponds to the Latin genitive?", "of", ["to", "by", "with"],
  "Es. «the king of Spain».", *PRE, "of typically corresponds to the genitive")
E("eng-206", "Prepositions", 5, "Which preposition can also follow its object, as in «the contrary ___»?", "notwithstanding", ["despite", "during", "among"],
  "È uno dei rari casi di posposizione in inglese.", *PRE, "notwithstanding, which can appear either before the object")

DET = ("English determiners", "English-determiners")
E("eng-207", "Determiners", 3, "Why is «I live in small house» ungrammatical?", "A singular countable noun needs a determiner (a, my, that…)", ["«small» must follow the noun", "«house» is uncountable", "«live» needs «at»"],
  "Corretto: «I live in a small house» o «I live in my house».", *DET, "I live in small house is ungrammatical")
E("eng-208", "Determiners", 2, "Complete: «___ books are mine.» (= questi libri)", "These", ["This", "That", "Thats"],
  "Alcuni determinanti concordano nel numero: this book, these books.", *DET, "this book, these books")
E("eng-209", "Determiners", 3, "Which form is correct?", "some of the people", ["happy of the people", "my of the people", "every of people"],
  "I determinanti compaiono nelle costruzioni partitive, aggettivi e possessivi no.", *DET, "some of the people but not *happy of the people")
E("eng-210", "Adverbs", 2, "What is the adverb formed from «cheap»?", "cheaply", ["cheapful", "cheapness", "cheaper"],
  "Molti avverbi si formano aggiungendo -ly all'aggettivo.", *DET, "cheap → cheaply")

INF = ("Infinitive", "Infinitive")
E("eng-211", "Gerund and infinitive", 2, "In «I want to sit on the other chair», «to sit» is:", "a full infinitive (to-infinitive)", ["a bare infinitive", "a gerund", "a past participle"],
  "La forma senza «to» si chiama bare infinitive.", *INF, "the form introduced by to is called the full infinitive or to-infinitive")
E("eng-212", "Gerund and infinitive", 3, "Complete: «I want ___ to eat their dinner.»", "them", ["they", "their", "theirs"],
  "Il soggetto implicito dell'infinito è al caso oggetto.", *INF, "I want them to eat their dinner")
E("eng-213", "Gerund and infinitive", 3, "How is an infinitive made negative?", "By putting «not» before it (e.g. «not to go»)", ["With «don't» before it", "By adding -n't", "With «no» after it"],
  "Es. «I decided not to go».", *INF, "Infinitives are negated by simply preceding them with not")
E("eng-214", "Gerund and infinitive", 4, "What is the passive infinitive of «eat»?", "to be eaten", ["to have eaten", "to be eating", "to eaten"],
  "«to have eaten» è l'infinito perfetto, «to be eating» quello progressivo.", *INF, "(to) be eaten (passive)")
E("eng-215", "Gerund and infinitive", 4, "Which is the perfect infinitive?", "to have eaten", ["to be eaten", "to eat", "to be eating"],
  "Es. «I'm happy to have met you».", *INF, "(to) have eaten (perfect active)")
E("eng-216", "Modal verbs", 3, "Complete: «You had better ___ now.»", "go", ["to go", "going", "went"],
  "«had better», come i modali, è seguito dall'infinito senza to.", *INF, "had better or ought to as substitutes for should")

CN = ("Count noun", "Count-noun")
E("eng-217", "Countable and uncountable", 2, "Which determiner is used only with countable nouns?", "many", ["much", "little", "a little"],
  "few, many e i numeri vanno con i numerabili; little e much con i non numerabili.", *CN, "\"few\", \"many\", \"those\", and numbers (\"one\") are used with count nouns")
E("eng-218", "Countable and uncountable", 2, "Complete: «There are some ___ of furniture in the room.»", "pieces", ["furnitures", "many", "a"],
  "«furniture» è non numerabile: si conta con «pieces of».", *CN, "There are some pieces of furniture in the room")
E("eng-219", "Countable and uncountable", 3, "Which quantifiers can go with count nouns but not with mass nouns?", "every, each, several", ["much, little", "some, no", "all, any"],
  "I nomi numerabili hanno singolare e plurale e accettano numeri.", *CN, "can co-occur with quantificational determiners like every, each, several")
E("eng-220", "Countable and uncountable", 3, "Complete: «I'll have two ___.» (= due caffè, in un bar)", "coffees", ["coffee", "coffee's", "coffeies"],
  "«coffee» può essere usato come numerabile per indicare le tazze.", *CN, "I'll have two coffees.")
E("eng-221", "Countable and uncountable", 4, "According to traditional prescription, «fewer» is used with ___ nouns and «less» with ___ nouns.", "count / mass", ["mass / count", "proper / common", "plural / singular only for people"],
  "Es. «fewer cars», «less traffic».", *CN, "\"fewer\" and \"fewest\" is reserved for count nouns and \"less\" and \"least\" for mass nouns")

CMPD = ("English compound", "English-compound")
E("eng-222", "Vocabulary", 2, "Which of these is a «solid» (closed) compound?", "basketball", ["ice cream", "mother-of-pearl", "high school"],
  "I composti si scrivono aperti, con trattino o uniti.", *CMPD, "Examples are \"housewife\", \"lawsuit\", \"wallpaper\", \"basketball\"")
E("eng-223", "Vocabulary", 3, "How is the compound «hide-and-seek» written?", "Hyphenated", ["Open (with spaces)", "Solid (one word)", "With an apostrophe"],
  "I composti con articoli, preposizioni o congiunzioni sono spesso con trattino.", *CMPD, "\"rent-a-cop\", \"mother-of-pearl\" and \"hide-and-seek\"")
E("eng-224", "Vocabulary", 3, "What tends to happen to compounds like «data set» over time?", "They tend to solidify (dataset)", ["They split into separate words", "They become verbs", "They take a hyphen permanently"],
  "Es. coal mine → coalmine, bottle cap → bottlecap.", *CMPD, "compounds tend to solidify as they age")
E("eng-225", "Vocabulary", 3, "Which pattern is typical for compounds naming people, like «fire-fighter»?", "noun + verb + -er", ["verb + noun", "adjective + noun", "preposition + noun"],
  "Il nome è l'oggetto del verbo: chi combatte il fuoco.", *CMPD, "noun + verb + -er, where the noun is the object of the verb")
E("eng-226", "Vocabulary", 4, "About what share of the words in the Old English poem Beowulf are compounds?", "Close to two-thirds", ["About 5%", "About 20%", "All of them"],
  "La composizione è il processo di formazione delle parole più produttivo dell'inglese.", *CMPD, "Close to two-thirds of the words in the Old English poem Beowulf are found to be compounds")

FPF = ("Future perfect", "Future-perfect")
E("eng-227", "Verb tenses", 3, "What is the negative of «He will have done it by this evening»?", "He won't have done it by this evening.", ["He will have not did it.", "He don't have done it.", "He won't has done it."],
  "Negativo: will not / won't + have + participio passato.", *FPF, "He won't have done (or will not have done) it by this evening")
E("eng-228", "Verb tenses", 4, "«He will have woken up by now» expresses:", "a confident assumption about the present", ["a future plan", "a past habit", "an order"],
  "Il future perfect con will può indicare una supposizione sul presente.", *FPF, "He will have woken up by now")
E("eng-229", "Verb tenses", 4, "What was the old name of the future perfect in traditional grammars?", "Second future tense", ["Past future", "Perfect conditional", "Future continuous"],
  "Il termine è oggi obsoleto.", *FPF, "the \"second future tense.\"")
E("eng-230", "Verb tenses", 4, "Complete: «In 1982, I knew that by 1986 I ___ to prison.»", "would have already gone", ["will have already gone", "had already went", "would already go"],
  "«would have + participio» esprime il futuro anteriore visto dal passato.", *FPF, "In 1982, I knew that by 1986 I would have already gone to prison")
E("eng-231", "Verb tenses", 3, "Complete: «I'll have ___ the dinner by 6 PM.»", "made", ["make", "making", "makes"],
  "Future perfect: will have + past participle.", *FPF, "I'll have made the dinner by 6 PM")

VRB = ("Verb", "Verb")
E("eng-232", "Verb forms", 1, "Complete: «He ___ to work every day.»", "walks", ["walk", "walking", "walkes"],
  "Al presente la terza persona singolare prende -s (o -es: fishes).", *VRB, "marked by adding \"-s\" ( walks) or \"-es\" (fishes)")
E("eng-233", "Verb forms", 3, "In «The boy wept», the verb «wept» is:", "intransitive (no direct object)", ["transitive", "ditransitive", "a modal"],
  "Un verbo intransitivo non ha complemento oggetto.", *VRB, "\"The boy wept.\"")
E("eng-234", "Verb forms", 3, "How can you check that a verb is transitive?", "Turn the sentence into the passive", ["Add -ing", "Put it in the future", "Remove the subject"],
  "«My friend read the newspaper» → «The newspaper was read by my friend».", *VRB, "A way to identify a transitive verb is to invert the sentence, making it passive")

IRR = ("List of English irregular verbs", "List-of-English-irregular-verbs")
E("eng-235", "Verb forms", 3, "Which form of «learn» is more typical of American English?", "learned", ["learnt", "lorn", "learen"],
  "L'inglese americano preferisce le forme regolari (learned, spelled), quello britannico spesso quelle irregolari (learnt, spelt).", *IRR, "learn (learnt vs. learned)")
E("eng-236", "Verb forms", 3, "Are newly created English verbs regular or irregular?", "Always regular: irregular verbs are a closed group", ["Always irregular", "They follow the pattern of «sing, sang, sung»", "It depends on the length of the verb"],
  "Es. «to google» → googled.", *IRR, "newly formed verbs are always regular")
E("eng-237", "Verb forms", 4, "Which verbs are irregular in the present tense (besides modals)?", "be, do, have and say", ["go, come, take and make", "can, may, will and shall", "eat, drink, sleep and run"],
  "Es. he is, he does, he has, he says (pronunciato in modo irregolare).", *IRR, "there are only four of them")
E("eng-238", "Verb forms", 2, "What is the contracted negative of «he does not»?", "he doesn't", ["he don't", "he doesnt'", "he not does"],
  "Le contrazioni di do si usano solo al negativo.", *IRR, "he does not = he doesn't")
E("eng-239", "Verb forms", 4, "Is the -ing form (present participle/gerund) of English verbs ever irregular?", "No, it is always regular", ["Yes, for all strong verbs", "Only for modal verbs", "Only in British English"],
  "Anche i verbi irregolari formano -ing in modo regolare (go → going).", *IRR, "ending in -ing, are always regular")

PLU2 = ("English plurals", "English-plurals")
E("eng-240", "Plurals", 2, "What is the plural of «deer»?", "deer", ["deers", "deeren", "dear"],
  "Alcuni nomi di animali hanno plurale uguale al singolare: deer, sheep, salmon, trout.", *PLU2, "deer (and all species in the deer family")
E("eng-241", "Plurals", 3, "What is the plural of «aircraft»?", "aircraft", ["aircrafts", "aircraves", "airscraft"],
  "Anche spacecraft, hovercraft: plurale invariato.", *PLU2, "craft (meaning 'vessel'), including aircraft")
E("eng-242", "Plurals", 3, "What is the plural of «series»?", "series", ["serieses", "serie", "seriess"],
  "Anche «species» resta uguale.", *PLU2, "series, species")
E("eng-243", "Plurals", 4, "As a fraction of a pound, what is the plural of «penny»?", "pence", ["pennies", "pennys", "pens"],
  "«pennies» indica invece le monete.", *PLU2, "penny—pence")
E("eng-244", "Plurals", 3, "What is the plural of «datum»?", "data", ["datums", "datae", "datas"],
  "I neutri latini in -um fanno il plurale in -a (stadium, stadia).", *PLU2, "datum, data")
E("eng-245", "Plurals", 4, "For a scholar, what is the plural of «appendix»?", "appendices", ["appendixs", "appendixi", "appendixen"],
  "Alcuni medici usano «appendixes»: le forme latine e inglesi coesistono.", *PLU2, "the plural of appendix is appendices")
E("eng-246", "Plurals", 3, "What is the plural of «postman»?", "postmen", ["postmans", "postmens", "postmannes"],
  "I composti con man/woman fanno il plurale come man → men.", *PLU2, "postmen, policewomen")
E("eng-247", "Plurals", 4, "An entomologist talks about insects'…", "antennae", ["antennas", "antennaes", "antennum"],
  "Un tecnico radio parla invece di «antennas».", *PLU2, "an entomologist deals with antennae")

NUM = ("English numerals", "English-numerals")
E("eng-248", "Numbers", 3, "On a cheque, how is 100 always written?", "one hundred", ["a hundred", "hundred", "an hundred"],
  "Mai «a hundred» sugli assegni.", *NUM, "the number 100 is always written \"one hundred\"")
E("eng-249", "Numbers", 3, "In English, which symbol is the decimal separator?", "The point (.)", ["The comma (,)", "The apostrophe (')", "The colon (:)"],
  "La virgola separa invece le migliaia (1,000).", *NUM, "In English the point (.) is used as the decimal separator")
E("eng-250", "Numbers", 3, "How is zero usually called in British football scores («The score is two–___»)?", "nil", ["love", "oh", "aught"],
  "Nel tennis si dice «love»; nei numeri di telefono «oh».", *NUM, "nil: in general sport scores, British usage")
E("eng-251", "Numbers", 2, "How is zero called in tennis?", "love", ["nil", "nothing", "naught"],
  "L'origine del termine è discussa.", *NUM, "love: in tennis, badminton, squash")
E("eng-252", "Numbers", 4, "What is a googol?", "Ten to the one hundredth power (10¹⁰⁰)", ["A million million", "A thousand million", "The largest prime number"],
  "Un googolplex è 1 seguito da un googol di zeri.", *NUM, "If a googol is ten to the one hundredth power")

HOM = ("Homophone", "Homophone")
E("eng-253", "Vocabulary", 3, "Homophones spelled differently, like «to», «too» and «two», are also called:", "heterographs", ["synonyms", "antonyms", "acronyms"],
  "Gli omofoni scritti allo stesso modo sono anche omografi.", *HOM, "Homophones that are spelled differently are also called heterographs")
E("eng-254", "Vocabulary", 3, "«rose» (flower) and «rose» (past of «rise») are:", "homophones spelled the same (also homographs)", ["synonyms", "antonyms", "false friends"],
  "Hanno stesso suono e grafia ma significato diverso.", *HOM, "rose (flower) and rose (past tense of \"rise\")")
E("eng-255", "Vocabulary", 3, "Which pair are homophones?", "flour – flower", ["flour – floor", "flower – flow", "floor – flower"],
  "In origine erano varianti grafiche della stessa parola.", *HOM, "flour and flower")

CTR = ("Contraction (grammar)", "Contraction-grammar")
E("eng-256", "Contractions", 2, "Which contraction is fully standard even in formal writing?", "o'clock", ["gonna", "ain't", "wanna"],
  "Le contrazioni sono comuni nel parlato e nella scrittura informale.", *CTR, "such as the now-standard form \"o'clock\"")
E("eng-257", "Contractions", 3, "Rewrite naturally: «they will see that it is just what we are like»", "they'll see that it's just what we're like", ["they'l see that its just what were like", "the'll see that tis just what wer like", "they will'nt see"],
  "Evitare del tutto le contrazioni può far suonare il testo innaturale.", *CTR, "they'll see that it's just what we're like")

PHV = ("English phrasal verbs", "English-phrasal-verbs")
E("eng-258", "Phrasal verbs", 2, "What does «She takes after her mother» mean?", "She resembles her mother", ["She follows her mother", "She takes care of her mother", "She leaves after her mother"],
  "«take after» = assomigliare (a un genitore).", *PHV, "She takes after her mother")
E("eng-259", "Phrasal verbs", 2, "What does «I ran into an old friend» mean?", "I met an old friend by chance", ["I hit an old friend with my car", "I ran away from an old friend", "I raced against an old friend"],
  "«run into» = incontrare per caso.", *PHV, "I ran into an old friend")
E("eng-260", "Phrasal verbs", 3, "What does «Susan had to sit in for me» mean?", "Susan had to replace me", ["Susan had to sit next to me", "Susan had to wait for me", "Susan had to come in with me"],
  "«sit in for» = sostituire qualcuno.", *PHV, "Susan had to sit in for me")
E("eng-261", "Phrasal verbs", 4, "Which sentence is correct?", "He thought the situation over.", ["He got the situation over.", "You can bank Susan on.", "He looked the problem forward to."],
  "Una particella può seguire l'oggetto (think over); una preposizione no (get over).", *PHV, "He thought the situation over")
E("eng-262", "Phrasal verbs", 3, "What does «You should stand by your friend» mean?", "You should support your friend", ["You should stand next to your friend", "You should wait for your friend", "You should leave your friend"],
  "«stand by» = sostenere, restare al fianco.", *PHV, "You should stand by your friend")

FF2 = ("False friend", "False-friend")
E("eng-263", "Vocabulary", 2, "What does the English word «actual» usually mean?", "Real", ["Current (attuale)", "Active", "Recent"],
  "È un falso amico: «attuale» si dice «current».", *FF2, "Actual, which in English is usually a synonym of real")
E("eng-264", "Vocabulary", 3, "In English, «confetti» means:", "Small pieces of coloured paper thrown at celebrations (coriandoli)", ["Sugared almonds", "Sweets in general", "Wedding favours"],
  "In italiano i confetti sono mandorle zuccherate; in inglese «confetti» sono i coriandoli.", *FF2, "in Italian, the corresponding word is coriandoli")

ADV = ("English adverbs", "English-adverbs")
E("eng-265", "Adverbs", 2, "Which is correct?", "the happy child", ["the happily child", "the child happy is", "the happyly child"],
  "Gli avverbi non modificano i nomi in posizione attributiva.", *ADV, "So you have the happy child, but not *the happily child")
E("eng-266", "Adverbs", 3, "Is «friendly» an adverb?", "No, it is an adjective ending in -ly", ["Yes, all words in -ly are adverbs", "It is a noun", "It is a preposition"],
  "Per l'avverbio si usa «in a friendly way».", *ADV, "some adjectives end in -ly (e.g., friendly)")
E("eng-267", "Adverbs", 3, "Which are the two interrogative adverbs?", "how and why", ["who and whom", "which and what", "this and that"],
  "Who/which/what sono pronomi o determinanti interrogativi.", *ADV, "There are two interrogative adverbs: how and why")
E("eng-268", "Adverbs", 3, "Which is correct?", "very happy", ["very enjoyed", "very liked it", "very love"],
  "«very» modifica aggettivi e avverbi, non verbi (si dice «enjoyed it very much»).", *ADV, "very happy & very happily, but not *very enjoyed")
E("eng-269", "Adverbs", 4, "Which adverbs can modify a whole noun phrase, as in «___ my neighbour»?", "even, only, alone", ["very, quite, rather", "how, why", "not, never"],
  "Es. «Even my neighbour knew».", *ADV, "These include even, only, and alone")

PRN = ("Personal pronouns in English", "Personal-pronouns-in-English")
E("eng-270", "Pronouns", 2, "Complete: «Is this car ___ or mine?» (= tua)", "yours", ["your", "you", "yourself"],
  "I pronomi possessivi (mine, yours…) non precedono il nome.", *PRN, "this book is mine")
E("eng-271", "Pronouns", 3, "What is the objective form of «who», now mainly formal?", "whom", ["whose", "which", "whoever"],
  "«whose» è il possessivo.", *PRN, "which has the objective form whom")
E("eng-272", "Pronouns", 4, "What is the reflexive of the indefinite pronoun «one»?", "oneself", ["oneselves", "ones", "one's self only"],
  "Il possessivo si scrive «one's».", *PRN, "which has the reflexive oneself")
E("eng-273", "Pronouns", 4, "Which archaic pronoun corresponds to singular «you» (subject)?", "thou", ["ye", "thee", "thine"],
  "thou (soggetto), thee (oggetto), thy/thine (possessivi), thyself (riflessivo).", *PRN, "thou, thee, thy, thine, thyself")
E("eng-274", "Pronouns", 2, "Complete: «I prefer ___.» (= il mio)", "mine", ["my", "me", "myself"],
  "I pronomi possessivi sostituiscono il nome già citato.", *PRN, "as in I prefer mine")

CMP2 = ("Degrees of comparison of adjectives and adverbs", "Degrees-of-comparison-of-adjectives-and-adverbs")
E("eng-275", "Comparatives", 3, "With two competitors, traditional grammar requires:", "May the better man win", ["May the best man win", "May the most good man win", "May the gooder man win"],
  "Con due elementi si usa il comparativo; nell'uso informale si sente anche «best».", *CMP2, "\"May the better man win\" would be considered correct if there are two individuals competing")
E("eng-276", "Comparatives", 2, "Complete: «Ram is ___ good ___ Shyam.» (uguaglianza)", "as … as", ["more … than", "so … that", "the … the"],
  "Comparativo di uguaglianza: as + aggettivo + as.", *CMP2, "\"Ram is as good as Shyam\"")
E("eng-277", "Comparatives", 3, "Which one-syllable adjective does NOT take -er/-est?", "fun", ["big", "tall", "fast"],
  "Eccezioni: fun, real, right, wrong (more fun, most real…).", *CMP2, "except for a few words such as fun, real, right, wrong")
E("eng-278", "Comparatives", 3, "How do adjectives of three or more syllables form the comparative?", "With «more» (e.g. more expensive)", ["With -er", "With -est", "With «much»"],
  "I monosillabi prendono -er/-est; i bisillabi variano.", *CMP2, "words of three or more syllables require \"more\" or \"most\"")
E("eng-279", "Comparatives", 4, "Why do some grammarians object to «more unique»?", "«unique» is an absolute adjective that denotes a totality", ["«unique» is a noun", "«unique» is always plural", "«unique» takes -er"],
  "Anche full, complete, empty sono considerati assoluti.", *CMP2, "full, complete, unique, or empty")

ADJ = ("Adjective", "Adjective")
E("eng-280", "Adjectives", 3, "In «The meek shall inherit the Earth», «the meek» means:", "those who are meek (a group of people)", ["a single meek person", "the meekness", "a place"],
  "Aggettivi sostantivati: the rich, the poor, the famous.", *ADJ, "where \"the meek\" means \"those who are meek\"")
E("eng-281", "Adjectives", 3, "In «he drove fast», «fast» is:", "an adverb", ["an adjective", "a noun", "a verb"],
  "In «a fast car» è invece un aggettivo.", *ADJ, "but an adverb in \"he drove fast\"")
E("eng-282", "Adjectives", 3, "How do you say «avere fame» in English?", "to be hungry", ["to have hunger", "to make hungry", "to do hungry"],
  "L'inglese usa be + aggettivo (hungry), l'italiano avere + nome.", *ADJ, "where English uses \"to be hungry\"")
E("eng-283", "Adjectives", 4, "Where does an adjective phrase with a complement usually go?", "After the noun (e.g. «a box full of toys»)", ["Always before the noun", "At the end of the sentence", "Before the article"],
  "Es. «an evildoer devoid of redeeming qualities».", *ADJ, "attributive adjective phrases that include complements typically follow the noun")

IS2 = ("Indirect speech", "Indirect-speech")
E("eng-284", "Reported speech", 3, "Direct: «I have painted the ceiling blue». Reported:", "He said that he had painted the ceiling blue.", ["He said that he has painted the ceiling blue yesterday.", "He said that I painted the ceiling.", "He said he paints the ceiling."],
  "Present perfect → past perfect se il verbo introduttivo è al passato.", *IS2, "He said that he had painted the ceiling blue")
E("eng-285", "Reported speech", 3, "Direct: «Please leave the room». Reported:", "I asked them to leave the room.", ["I asked them that they leave the room please.", "I asked them leaving the room.", "I said them leave the room."],
  "Le richieste si riportano con verbo + oggetto + to-infinitive.", *IS2, "I asked them to leave the room")
E("eng-286", "Reported speech", 4, "Is backshifting obligatory if the situation is still true («Ed is a bore»)?", "No: «She said that Ed was/is a bore» are both possible", ["Yes, always", "Only in American English", "Only with «tell»"],
  "Il cambio di tempo è facoltativo se il fatto resta valido.", *IS2, "She said that Ed was/is a bore")
E("eng-287", "Reported speech", 3, "Direct: «How do people manage to live in this city?» Reported:", "I asked him how people managed to live in that city.", ["I asked him how do people manage to live in this city.", "I asked him how people did manage to live in this city?", "I asked how people manage live in that city."],
  "Nelle domande indirette non c'è inversione e il dimostrativo cambia (this → that).", *IS2, "I asked him how people managed to live in that city")
E("eng-288", "Reported speech", 4, "What is the change of tense in reported speech called?", "Backshifting", ["Inversion", "Do-support", "Ellipsis"],
  "Avviene perché il verbo principale (said, asked) è al passato.", *IS2, "also called backshifting")

PLP2 = ("Pluperfect", "Pluperfect")
E("eng-289", "Verb tenses", 2, "What is the pluperfect usually called in English grammar?", "Past perfect", ["Present perfect", "Simple past", "Future perfect"],
  "Combina tempo passato e aspetto perfettivo (had written).", *PLP2, "is now usually called the past perfect")
E("eng-290", "Verb tenses", 3, "Complete: «We ___ before the game began.»", "had arrived", ["have arrived", "arrive", "were arrive"],
  "Past perfect: azione anteriore a un'altra azione passata.", *PLP2, "\"we had arrived\" before the game began")
E("eng-291", "Verb tenses", 4, "From which Latin expression does «pluperfect» come?", "plus quam perfectum («more than perfect»)", ["post perfectum", "per fectum", "ante perfectum"],
  "«perfect» significa qui «completato».", *PLP2, "The word is derived from the Latin plus quam perfectum")
E("eng-292", "Verb tenses", 4, "Complete: «It ___ for a week when the big storm started.»", "had already been raining", ["has already rained", "was already raining since", "already rains"],
  "Past perfect continuous: azione iniziata prima di un momento passato.", *PLP2, "It had already been raining for a week when the big storm started")

QW2 = ("Interrogative word", "Interrogative-word")
E("eng-293", "Questions and negatives", 3, "In «Which road leads to the city center?», «which» is:", "an interrogative determiner", ["an interrogative pronoun", "an interrogative adverb", "a relative pronoun"],
  "In «Which leads to the city center?» è invece un pronome.", *QW2, "the word which is an interrogative determiner for the noun road")
E("eng-294", "Questions and negatives", 2, "Complete: «___ gorgeous pink painting is that?» (= di chi)", "Whose", ["Who's", "Whom", "Which"],
  "«whose» chiede il possessore.", *QW2, "Whose gorgeous, pink painting is that?")
E("eng-295", "Questions and negatives", 3, "In «The country where he was born», «where» is used as:", "a relative word", ["an interrogative adverb", "a preposition", "a noun"],
  "Le stesse forme delle parole interrogative si usano anche nelle relative.", *QW2, "The country where he was born")

IMP2 = ("Imperative mood", "Imperative-mood")
E("eng-296", "Imperative", 2, "Which is a more polite way to say «Come here!»?", "Could you come here for a moment?", ["Come here now!", "You come here!", "Here come!"],
  "Nel registro cortese gli ordini si formulano come domande.", *IMP2, "Could you come here for a moment?")
E("eng-297", "Imperative", 2, "How do negative imperatives usually begin?", "With «don't» (e.g. «Don't be like that»)", ["With «no»", "With «not»", "With «never to»"],
  "Es. «Don't go too near the tiger».", *IMP2, "They usually begin with the verb \"don't\"")
E("eng-298", "Imperative", 3, "«Have a nice trip!» is an imperative used to express:", "a wish", ["an order", "a prohibition", "a question"],
  "Gli imperativi servono anche per inviti, permessi, auguri e scuse.", *IMP2, "Have a nice trip! (wish)")
E("eng-299", "Imperative", 3, "«Eat the apple if you want» expresses:", "permission", ["an obligation", "a threat", "a past habit"],
  "«Come to the party tomorrow!» esprime invece un invito.", *IMP2, "Eat the apple if you want. (permission)")
E("eng-300", "Pronouns", 3, "Complete: «For someone like ___, this is easy.» (uso non riflessivo, sconsigliato dalle guide di stile)", "myself", ["I", "mine", "my"],
  "La forma riflessiva usata al posto di «me» è comune ma alcune guide la sconsigliano.", *PRN, "For someone like myself")
