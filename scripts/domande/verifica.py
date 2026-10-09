"""Controlla che ogni domanda abbia la sua frase-prova nel testo della fonte (contenuti/prove/<materia>.json).
Uso: python3 scripts/domande/verifica.py [materia ...]   (senza argomenti: tutte)"""
import json, pathlib, sys
from testi import ROOT, estrai, normalizza

materie = sys.argv[1:] or sorted(p.stem for p in (ROOT / "data" / "domande").glob("*.json"))
problemi = 0
for materia in materie:
    testi = {k: v.lower() for k, v in estrai(materia).items()}
    prove = json.loads((ROOT / "contenuti" / "prove" / f"{materia}.json").read_text())
    domande = {d["id"] for d in json.loads((ROOT / "data" / "domande" / f"{materia}.json").read_text())}
    ko = []
    for p in prove:
        t = testi.get(p["file"])
        if t is None or normalizza(p["frase"]).lower() not in t:
            ko.append(f"  NON TROVATA  {p['id']}  [{p['file']}]  {p['frase'][:80]}")
    ko += [f"  SENZA PROVA  {i}" for i in sorted(domande - {p["id"] for p in prove})]
    print(f"{materia}: {len(domande)} domande, {len(ko)} problemi")
    print("\n".join(ko)) if ko else None
    problemi += len(ko)
sys.exit(1 if problemi else 0)
