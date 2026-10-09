"""Cerca frasi nei testi di una materia, come li vede la verifica (per scrivere le frasi-prova).
Uso: python3 scripts/domande/cerca.py <materia> <prefisso-file> "frase" ["frase" ...]"""
import sys
from testi import estrai, normalizza

materia, prefisso, *frasi = sys.argv[1:]
for nome, testo in estrai(materia).items():
    if not nome.startswith(prefisso):
        continue
    basso = testo.lower()
    for f in frasi:
        i = basso.find(normalizza(f).lower())
        print(f"[{nome[:30]}] {f[:40]!r}: " + ("NON TROVATA" if i < 0 else "…" + testo[max(0, i - 60): i + len(f) + 140] + "…"))
