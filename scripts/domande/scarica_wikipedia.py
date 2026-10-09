"""Scarica voci di Wikipedia come testo semplice in contenuti/libri/<materia>/ e le registra in contenuti/fonti.csv.
Uso: python3 scripts/domande/scarica_wikipedia.py <materia> [--lingua en] "Titolo voce" ["Titolo" ...]"""
import csv, datetime, json, pathlib, re, sys, time, urllib.error, urllib.parse, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
args = sys.argv[1:]
materia = args.pop(0)
lingua = "it"
if args and args[0] == "--lingua":
    args.pop(0); lingua = args.pop(0)
fonti = ROOT / "contenuti" / "fonti.csv"
righe = list(csv.DictReader(open(fonti, encoding="utf-8-sig")))
campi = list(righe[0].keys())
oggi = datetime.date.today().strftime("%d/%m/%Y")


def scarica(req):
    """Wikipedia risponde 429 se si chiede troppo in fretta: riprova con attese crescenti."""
    for attesa in (5, 15, 45, 0):
        try:
            return json.load(urllib.request.urlopen(req, timeout=30))
        except urllib.error.HTTPError as e:
            if e.code != 429 or not attesa:
                raise
            time.sleep(attesa)


for titolo in args:
    time.sleep(1)
    url = f"https://{lingua}.wikipedia.org/w/api.php?" + urllib.parse.urlencode(
        {"action": "query", "prop": "extracts", "explaintext": 1, "format": "json", "redirects": 1, "titles": titolo})
    req = urllib.request.Request(url, headers={"User-Agent": "iMieiConcorsi/0.1 (contenuti didattici)"})
    pagina = list(scarica(req)["query"]["pages"].values())[0]
    testo = pagina.get("extract", "")
    if not testo:
        print(f"  NON TROVATA: {titolo}"); continue
    nome = ("Wikipedia" if lingua == "it" else "Wikipedia-EN") + "_" + re.sub(r"[^\w]+", "-", pagina["title"]).strip("-") + ".txt"
    dest = ROOT / "contenuti" / "libri" / materia / nome
    dest.write_text(testo)
    if not any(r["file"] == nome for r in righe):
        righe.append({**{c: "" for c in campi}, "materia": materia, "file": nome,
                      "titolo": f"{pagina['title']} (voce di Wikipedia, scaricata il {oggi})", "autore": "Contributori di Wikipedia",
                      "link": f"https://{lingua}.wikipedia.org/wiki/" + urllib.parse.quote(pagina["title"].replace(" ", "_")),
                      "licenza": "CC BY-SA 4.0"})
    print(f"  {nome}: {len(testo.split())} parole")
w = csv.DictWriter(open(fonti, "w", encoding="utf-8", newline=""), fieldnames=campi)
w.writeheader(); w.writerows(righe)
