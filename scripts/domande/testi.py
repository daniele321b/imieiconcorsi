"""Testo dei PDF di contenuti/libri, estratto con pdftotext in .cache/testi/<materia>/ e normalizzato."""
import pathlib, re, subprocess, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
LIBRI = ROOT / "contenuti" / "libri"
CACHE = ROOT / ".cache" / "testi"


def normalizza(t: str) -> str:
    """Testo confrontabile: forme Unicode unificate, parole spezzate a fine riga riunite, virgolette e spazi uniformi."""
    t = unicodedata.normalize("NFKC", t).replace("­", "")
    t = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", t)  # sillabazione a fine riga
    t = t.replace("’", "'").replace("“", '"').replace("”", '"').replace("«", '"').replace("»", '"')
    return re.sub(r"\s+", " ", t)


def estrai(materia: str) -> dict[str, str]:
    """{nome file .txt: testo normalizzato}; estrae solo i PDF nuovi o cambiati."""
    out = {}
    # Testi già in formato .txt (es. voci di Wikipedia scaricate con scarica_wikipedia.py)
    for txt in sorted((LIBRI / materia).glob("*.txt")):
        out[txt.name] = normalizza(txt.read_text(errors="ignore"))
    for pdf in sorted((LIBRI / materia).glob("*.pdf")):
        txt = CACHE / materia / (pdf.stem + ".txt")
        if not txt.exists() or txt.stat().st_mtime < pdf.stat().st_mtime:
            txt.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(["pdftotext", "-q", "-layout", "-enc", "UTF-8", str(pdf), str(txt)], check=True)
        out[txt.name] = normalizza(txt.read_text(errors="ignore"))
    return out
