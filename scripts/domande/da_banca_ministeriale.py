"""Importa domande da una banca dati ministeriale (PDF in contenuti/libri/<materia>/) nel sorgente.

Le banche «1° Livello» hanno domande numerate «12) testo» con quattro risposte A)-D) e la nota
«la risposta corretta è sempre in posizione A)». Lo script sceglie le domande in modo uniforme
lungo il file, scarta quelle che non reggono da sole (figure, opzioni ripetute, doppioni con le
domande già presenti) e stampa i blocchi D(...) da aggiungere a contenuti/sorgenti/<materia>.py.
La frase-prova è il testo della domanda, che verifica.py ritrova nel PDF.

Uso: python3 scripts/domande/da_banca_ministeriale.py <materia> <file.pdf> <quante> <primo-id> [<prefisso-id>]
"""
import json, pathlib, re, sys

from testi import CACHE, ROOT, estrai, normalizza

NOMI = {"geografia": "Geografia", "italiano": "Italiano", "attualita": "Attualità", "algebra": "Algebra", "matematica": "Aritmetica"}

# Argomento per parole chiave (il primo che corrisponde), per materia; poi il valore di riserva.
ARGOMENTI = {
    "geografia": [
        (r"capoluog|region|provinc|\([A-Z]{2}\)|\bSS \d", "Regioni"), (r"vulcan|terremot|ipocentro|crosta|sism", "Vulcani"),
        (r"isol|arcipelag|penisola", "Isole"), (r"fium|affluent|foce|sorgent|emissari", "Fiumi"), (r"\blag", "Laghi"),
        (r"\bmonte\b|vetta|catena|alpi|appennin|monti\b|montuos|cima|cordiglier|dolomit", "Montagne"),
        (r"oceano", "Oceani"), (r"mare|stretto|golfo|canale|sbocco", "Mari e stretti"), (r"confin", "Confini"),
        (r"unione europea|\bue\b", "Unione europea"), (r"capitale", "Capitali"),
        (r"clima|atmosfer|foresta|deserto", "Ambiente"), (r"popolazion|abitant", "Popolazione"),
        (r"europe|europa|\bitalia", "Europa"),
    ],
    "italiano": [
        (r"sinonim|contrari|significato|signific", "Lessico"), (r"ortograf|errore|accent|apostrof|scritt", "Ortografia"),
        (r"\bverb|coniug|congiuntiv|condizional|participi|gerundi|infinit|indicativ|imperativ|passato remoto|futuro|imperfetto", "Verbi"),
        (r"sillab", "Ortografia"),
        (r"complement|proposizion|soggetto|predicat|periodo|frase|analisi", "Sintassi"),
        (r"figura retorica|metafor|similitudin|iperbol|onomatop|allitter", "Retorica"),
        (r"autore|scritt|poet|romanz|opera|poesia|divina commedia|promessi", "Letteratura"),
        (r"punteggiatura|virgola|punto", "Punteggiatura"),
        (r"nome|aggettiv|pronom|articol|avverbi|preposizion|congiunzion|plurale|femminile|singolare", "Morfologia"),
    ],
    "matematica": [
        (r"probabilit", "Probabilità"), (r"insiem|∩|∪", "Insiemi"), (r"disequazion|[<>≤≥]", "Disequazioni"),
        (r"retta|rette|cartesian|coordinat|asse|simmetric", "Piano cartesiano"), (r"prodotti notevoli|cubo:|\)²|\)³", "Prodotti notevoli"),
        (r"radice|√", "Radicali"), (r"equazion|\bx\s*=|valore della x", "Equazioni"), (r"proporzion|\d\s*:\s*\d+\s*=", "Proporzioni"),
        (r"%|percent|sconto", "Percentuali"), (r"polinomi|scompor", "Polinomi"), (r"monomi", "Monomi"),
        (r"fattori primi|numero primo|numeri primi", "Numeri primi"), (r"m\.c\.m|m\.c\.d|mcm|mcd|minimo comune|multipl|divisor", "MCD e mcm"),
        (r"frazion|/\d", "Frazioni"), (r"potenz|[²³⁴⁵⁶⁷⁸⁹¹⁰]|esponent", "Potenze"), (r"\(\s*[+-]\d", "Numeri relativi"),
        (r"metri|litri|grammi|\bore\b|minuti|giorni|\bkm\b|\bkg\b", "Misure"), (r"media|arrotond", "Statistica"),
        (r"triangol|quadrat|rettangol|cerchio|circonferenz|area|perimetro|angol|poligon|volume", "Geometria"),
        (r"\ba\b|\bb\b|letteral", "Monomi"),
    ],
    "attualita": [
        (r"calci|tennis|olimpi|mondiali di|coppa|campion|sport|ciclis|formula 1|wimbledon|roland|slam|atp\b|wta\b|davis|scudetto|pallone d|"
         r"\bgol\b|nazionale|juventus|milan\b|\binter\b|napoli di|maratona|marcia|salto|staffetta|\d+ ?m\b|portiere|\bct\b", "Sport"),
        (r"canzon|cantant|album|band|sanremo|music|film|oscar|regist|attore|attrice|palma d'oro|leone d'oro|serie tv|disney|netflix", "Spettacolo e cultura"),
        (r"\bue\b|unione europea|europe|euro\b|nato\b|onu\b|nazioni unite|unesco|schengen|bce\b", "Istituzioni internazionali"),
        (r"guerra|conflitt|attacc|invasion|russia|ucrain|israel|hamas|terror|intifad|palestin", "Conflitti e geopolitica"),
        (r"presidente|governo|ministro|elezion|parlament|partito|costituzion|repubblica|referendum", "Politica"),
        (r"nasa|spazi|luna\b|marte|sonda|satellit|scienz|scoper|vaccin|virus|covid|tecnolog|internet|intelligenza artificiale|smartphone|google|apple", "Scienza e tecnologia"),
        (r"clima|ambient|cop\s?\d|inquin|energia|sostenib|terremot|tsunami|alluvion|incendi|emission", "Ambiente"),
        (r"economi|\bpil\b|inflazion|banca|borsa|lavoro|tasse|moneta|finanz", "Economia"),
        (r"\b1[0-9]{3}\b|storia|impero|\bre\b|regno|rivoluzion|papa\b", "Storia"),
    ],
}
RISERVA = {"geografia": "Continenti", "italiano": "Lessico", "matematica": "Espressioni", "attualita": "Cultura generale"}
# Domande rovinate nel PDF stesso (dati mancanti o simboli persi), per file e numero.
ESCLUDI = {"matematica": {40}, "italiano": {2068}, "attualita": {343, 363, 492, 509, 512}}
# Dati che cambiano nel tempo (popolazioni, satelliti) o date di adesione all'UE incoerenti nel PDF:
# risposte non più sicure, si saltano.
SUPERATE = re.compile(r"dell'UE dal|numero di satelliti|(maggiore|minore) popolazione|più popolos|densamente popolat|abitanti del pianeta", re.I)
SCARTA = re.compile(r"figur|immagin|grafic|tabell|disegn|seguente schema|osserva|nessuna delle altre|tutte le altre|tutte le precedenti|nessuna delle precedenti", re.I)


def leggi(path: pathlib.Path):
    """Domande del file txt estratto: [{n, testo, opz:[A,B,C,D]}]."""
    out, cur, campo = [], None, None
    for r in path.read_text(encoding="utf-8").split("\n"):
        s = r.strip()
        if not s or re.match(r"^(Banca Dati|1° Livello|NOTA:|Pag\.|\d+$)", s):
            continue
        m, o = re.match(r"^(\d+)\)\s*(.*)$", s), re.match(r"^([A-D])\)\s*(.*)$", s)
        if m and (cur is None or len(cur["opz"]) == 4):
            cur = {"n": int(m.group(1)), "testo": m.group(2), "opz": []}
            out.append(cur)
            campo = "testo"
        elif o and cur is not None and len(cur["opz"]) == "ABCD".index(o.group(1)):
            cur["opz"].append(o.group(2))
            campo = "opz"
        elif cur is not None:
            if campo == "testo":
                cur["testo"] += " " + s
            elif campo == "opz":
                cur["opz"][-1] += " " + s
    return [x for x in out if len(x["opz"]) == 4]


def pulisci(t: str) -> str:
    """Testo come nel PDF, con apici (x², 5¹⁰) e simboli intatti: solo spazi e virgolette uniformati."""
    t = t.replace("\u00ad", "").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", t).strip()


def parole(t: str) -> set[str]:
    return {w for w in re.findall(r"\w+", t.lower()) if len(w) > 3}


def main():
    materia, pdf, quante, primo = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    prefisso = sys.argv[5] if len(sys.argv) > 5 else None
    testi = estrai(materia)  # crea la cache txt se manca
    txt = CACHE / materia / (pathlib.Path(pdf).stem + ".txt")
    nome = NOMI[pathlib.Path(pdf).stem]
    domande = leggi(txt)
    testo_pdf = testi[txt.name].lower()

    esistenti, compatti = [], set()
    file_dati = ROOT / "data" / "domande" / f"{materia}.json"
    if file_dati.exists():
        for d in json.loads(file_dati.read_text()):
            esistenti.append(parole(d["testo"] + " " + d["opzioni"][d["corretta"]]))
            compatti.add(re.sub(r"\W", "", (d["testo"] + d["opzioni"][d["corretta"]]).lower()))
            prefisso = prefisso or d["id"].split("-")[0]

    def buona(x):
        testo, opz = pulisci(x["testo"]), [pulisci(o) for o in x["opz"]]
        if len(testo) < 10 or any(not o for o in opz) or len({o.lower() for o in opz}) < 4:
            return False
        if SCARTA.search(testo + " " + " ".join(opz)) or SUPERATE.search(testo) or "?" in "".join(opz).replace("¿", ""):
            return False
        if x["n"] in ESCLUDI.get(pathlib.Path(pdf).stem, set()) or re.search(r"(seguente|seguenti) (numero|numeri|frazione|espressione|polinomio)\s*:?$", testo):
            return False
        # Insiemi con i simboli ⊂ ⊆ persi: rimangono lettere sole («A B e B C»).
        # Date diventate numeri seriali di Excel nel PDF («44616» per il 24/02/2022).
        if any(re.fullmatch(r"[A-Z] ?[A-Z]", o) or re.fullmatch(r"4\d{4}", o) for o in opz):
            return False
        # Matematica: frazioni impilate o esponenti persi nel PDF lasciano numeri attaccati alle lettere (523b, x2).
        if materia == "matematica" and re.search(r"\d{3,}[a-z]|[a-z]\d|\d[a-z]\d", testo + " " + " ".join(opz)):
            return False
        return normalizza(testo).lower() in testo_pdf

    candidate = [x for x in domande if buona(x)]
    # Scelta uniforme lungo il file, saltando i doppioni (con le esistenti e con quelle già scelte).
    scelte, passo, i = [], max(1, len(candidate) // (quante * 2)), 0
    giro = 0
    while len(scelte) < quante and giro < passo * 2 + 2:
        for x in candidate[giro % passo :: passo]:
            if len(scelte) >= quante:
                break
            if x in scelte:
                continue
            w = parole(x["testo"] + " " + x["opz"][0])
            compatto = re.sub(r"\W", "", (x["testo"] + x["opz"][0]).lower())
            if compatto in compatti:
                continue
            if any(len(w & e) / max(1, len(w | e)) >= 0.6 for e in esistenti):
                continue
            esistenti.append(w)
            compatti.add(compatto)
            scelte.append(x)
        giro += 1
    scelte.sort(key=lambda x: x["n"])

    regole = ARGOMENTI[materia]
    print(f"\n# ── Banca dati ministeriale «1° Livello – {nome}» ({pathlib.Path(pdf).name}): domande riportate così come sono,")
    print("#    la risposta esatta è la A) del PDF. Generato con scripts/domande/da_banca_ministeriale.py.")
    for k, x in enumerate(scelte):
        testo, opz = pulisci(x["testo"]), [pulisci(o) for o in x["opz"]]
        arg = next((a for r, a in regole if re.search(r, testo, re.I)), RISERVA[materia])
        spieg = f"Banca dati ministeriale (1° livello, {nome}), domanda n. {x['n']}: la risposta esatta è «{opz[0]}»."
        fonte = f"Banca dati ministeriale, 1° livello – {nome}, n. {x['n']}"
        print(f"D({json.dumps(f'{prefisso}-{primo + k:03d}')}, {json.dumps(arg, ensure_ascii=False)}, 2, {json.dumps(testo, ensure_ascii=False)},")
        print(f"  {json.dumps(opz[0], ensure_ascii=False)}, {json.dumps(opz[1:], ensure_ascii=False)},")
        print(f"  {json.dumps(spieg, ensure_ascii=False)},")
        print(f"  {json.dumps(fonte, ensure_ascii=False)}, {json.dumps(txt.name)}, {json.dumps(testo, ensure_ascii=False)})")
    print(f"# selezionate {len(scelte)} su {len(candidate)} candidate ({len(domande)} nel file)", file=sys.stderr)


if __name__ == "__main__":
    main()
