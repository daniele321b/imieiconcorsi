# Immagini per i social

Foto profilo di Instagram e Facebook e copertina della Pagina Facebook.

La foto profilo è la spunta gialla del logo sul gradiente viola del sito, con gli
stessi colori di `packages/web/src/index.css` (`brand-600` #4f46e5 → `brand-800` #3730a3, spunta
`accent-400` #fbbf24).

| File | Dove si carica | Misura |
| --- | --- | --- |
| `instagram-profilo-1080.png` | Instagram → Modifica profilo → Cambia immagine del profilo | 1080 × 1080 |
| `facebook-profilo-1080.png` | Pagina Facebook → Modifica → Immagine del profilo | 1080 × 1080 |
| `anteprima-cerchio.png` | Non si carica: mostra come appare ritagliata nel cerchio a 320, 170, 110 e 40 px | — |
| `profilo.svg` | Sorgente delle due foto profilo | vettoriale |
| `facebook-copertina-1640x624.png` | Pagina Facebook → Modifica → Immagine di copertina | 1640 × 624 |
| `anteprima-copertina.png` | Non si carica: la copertina da computer (con la foto profilo sopra) e da telefono | — |
| `facebook-copertina.html` | Sorgente della copertina (font del sito incorporato) | — |

I due PNG sono uguali: un file per social, così si trova subito quello giusto. I social ritagliano la
foto in un cerchio. La spunta sta al centro, con margine su ogni lato, e si legge anche nei
cerchietti piccoli dei commenti. Nella foto profilo non c'è la scritta "iMieiConcorsi": a quelle
misure non si leggerebbe, e il nome compare già accanto alla foto.

La copertina riprende la parte alta della home del sito: sfondo `brand-950` con le stesse luci
sfumate, il logo, la frase "Il tuo concorso pubblico, studiato su misura.", i punti dell'app e
l'indirizzo. Testi e logo stanno al centro, perché da telefono Facebook mostra solo la fascia
centrale (circa 1100 × 624). L'angolo in basso a sinistra resta vuoto: da computer lì c'è la foto
profilo. Per cambiare frase o punti modifica `facebook-copertina.html` (aprendolo nel browser vedi
subito il risultato) e riesporta.

## Rigenerare i PNG

Se cambiano colori o logo, modifica `profilo.svg` e riesporta con Chrome, dalla radice del repo:

```bash
cd docs/brand/social
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --hide-scrollbars --force-device-scale-factor=1 --window-size=1080,1080 \
  --screenshot="$PWD/instagram-profilo-1080.png" "file://$PWD/profilo.svg"
cp instagram-profilo-1080.png facebook-profilo-1080.png
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --hide-scrollbars --force-device-scale-factor=1 --window-size=1640,624 \
  --screenshot="$PWD/facebook-copertina-1640x624.png" "file://$PWD/facebook-copertina.html"
```
