"""Genera data/domande/<materia>.json e contenuti/prove/<materia>.json da contenuti/sorgenti/<materia>.py.

Nel sorgente ogni domanda è:
  D(id, argomento, livello, testo, giusta, [3 sbagliate], spiegazione, fonte, file_txt, frase_prova)
La risposta giusta ruota sulle 4 posizioni (distribuzione uniforme); le sbagliate sono
mescolate in modo stabile per id. Ogni domanda porta la versione della banca scritta in
contenuti/VERSIONE (v1, v2…). Uso: python3 scripts/domande/genera.py <materia>
"""
import json, pathlib, random, runpy, sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[2]
materia = sys.argv[1]
versione = (ROOT / "contenuti" / "VERSIONE").read_text().strip()
assert versione[:1] == "v" and versione[1:].isdigit(), f"contenuti/VERSIONE: atteso v1, v2…, trovato {versione!r}"
domande, prove = [], []


def D(id, argomento, livello, testo, giusta, sbagliate, spiegazione, fonte, file, frase):
    """Una domanda del sorgente: controlla i vincoli, mette la giusta in una posizione a rotazione e la aggiunge ai file."""
    assert len(sbagliate) == 3, f"{id}: servono 3 risposte sbagliate"
    # Stessi vincoli di DomandaSchema (packages/core/src/domande.ts): meglio fermarsi qui che ai test.
    assert len(testo) >= 10 and len(spiegazione) >= 10, f"{id}: testo e spiegazione almeno 10 caratteri"
    assert len({o.strip().lower() for o in [giusta, *sbagliate]}) == 4, f"{id}: le 4 opzioni devono essere diverse"
    opzioni = list(sbagliate)
    random.Random(id).shuffle(opzioni)
    opzioni.insert(len(domande) % 4, giusta)
    domande.append({"materia": materia, "id": id, "argomento": argomento, "livello": livello, "testo": testo,
                    "opzioni": opzioni, "corretta": opzioni.index(giusta), "spiegazione": spiegazione, "fonte": fonte, "versione": versione})
    prove.append({"id": id, "file": file, "frase": frase})


runpy.run_path(str(ROOT / "contenuti" / "sorgenti" / f"{materia}.py"), init_globals={"D": D})
ids = [d["id"] for d in domande]
assert len(ids) == len(set(ids)), "id doppi"
(ROOT / "data" / "domande" / f"{materia}.json").write_text(json.dumps(domande, ensure_ascii=False, indent=2) + "\n")
(ROOT / "contenuti" / "prove" / f"{materia}.json").write_text(json.dumps(prove, ensure_ascii=False, indent=2) + "\n")
print(f"{materia}: {len(domande)} domande, livelli {dict(sorted(Counter(d['livello'] for d in domande).items()))}")
