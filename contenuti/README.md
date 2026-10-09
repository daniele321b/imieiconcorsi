# Contenuti

Sorgenti della banca domande statica (piano Free).

- `libri/<materia>/`: i PDF da cui si generano le domande. **Non vanno su git**
  (diritti d'autore e dimensioni): restano solo sul tuo Mac.
- `fonti.csv`: il registro delle fonti, versionato. Un libro entra solo se la
  licenza consente l'uso commerciale (pubblico dominio, CC BY, CC BY-SA). NC o
  licenza non chiara = escluso.
- Per diritto costituzionale e amministrativo la fonte principale sono i testi
  ufficiali delle norme (Normattiva): gli atti ufficiali dello Stato non sono
  coperti da diritto d'autore (art. 5, L. 633/1941).

Le domande generate e riviste vanno in `data/domande/<materia>.json`. Lo schema
lo controlla `scripts/deploy.sh test`; il caricamento sul sito lo fa
`scripts/deploy.sh infra`.

## Regole per generare le domande senza violare il diritto d'autore

Le domande nascono dai **fatti e dai concetti** contenuti nelle fonti, che non sono
protetti. Il testo con cui un libro li esprime invece è protetto. Per questo:

1. **Solo fonti registrate.** Un libro entra in `fonti.csv` solo con una licenza che
   consente l'uso commerciale: pubblico dominio, CC BY o CC BY-SA. "Gratis da
   scaricare" non basta, e "NC" (non commerciale) esclude il libro.
2. **Parole nostre.** Domanda, opzioni e spiegazione si scrivono da zero. Del libro
   si riprendono solo termini tecnici, nomi, date e numeri, mai frasi intere.
3. **Niente quiz copiati.** Le domande e gli esercizi già presenti nel libro sono
   opera dell'autore: non si copiano, non si traducono e non si riformulano.
4. **Fonte citata, non riportata.** Il campo `fonte` dice da dove viene il fatto
   (es. `Manuale X, cap. 3` oppure `Costituzione, art. 83`), senza estratti.
5. **CC BY e CC BY-SA:** in `fonte` vanno autore e licenza. Con CC BY-SA, le domande
   derivate da quel libro vanno pubblicate con la stessa licenza: da tenere presente
   prima di sceglierlo.
6. **Norme:** i testi ufficiali di leggi e decreti sono liberi (art. 5, L. 633/1941).
   I commenti e le note dei manuali giuridici, invece, no.
7. **Risposta verificata.** Ogni risposta si controlla sul passo della fonte. Se il
   dubbio resta, la domanda non entra.

## Come sono fatte le domande

- `sorgenti/<materia>.py`: le domande scritte a mano. Per ognuna ci sono testo,
  risposta giusta, tre sbagliate, spiegazione, fonte e **frase-prova**, cioè le
  parole esatte del PDF che confermano la risposta.
- `scripts/deploy.sh genera-domande` scrive `data/domande/<materia>.json` (quello
  che va sul sito). Distribuisce la risposta giusta in modo uniforme sulle 4
  posizioni.
- `scripts/deploy.sh verifica-domande` estrae il testo dei PDF (in `.cache/`) e
  controlla che ogni frase-prova ci sia davvero. Una domanda senza prova non
  passa.
- `prove/<materia>.json`: le frasi-prova, generate insieme alle domande.

## Fonti escluse

Non usate, per le regole 1 e 5 (licenza che non consente l'uso commerciale o da
verificare):

- Camera_Dentro-la-Camera.pdf, SenatoRagazzi_Incontro-con-la-Costituzione.pdf,
  SenatoRagazzi_Storia-della-Costituzione-2022.pdf: copyright di Camera e Senato
- ITTIG-Crusca_Guida-redazione-atti-amministrativi.pdf: copyright degli autori
- Galileo_College-ESL-Writers.pdf: CC BY-NC-SA (non commerciale)
- AgID_DigComp-2.2-italiano.pdf: licenza della traduzione da verificare
- CCNL_Funzioni-Locali-2019-2021.pdf: utilizzabile, ma il testo estratto dal PDF
  (su due colonne) non è affidabile per le frasi-prova
