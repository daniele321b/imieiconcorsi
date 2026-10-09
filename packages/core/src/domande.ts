import { z } from "zod";
import { MATERIA_IDS } from "./domain";

// Controllo dei file della banca domande statica (data/domande/*.json) prima di caricarli:
// lo usano lo script di import (scripts/deploy.sh seed) e i test.

/**
 * Una domanda della banca statica (data/domande/<materia>.json). Stesso schema per le
 * domande scritte a mano e per quelle generate dai libri e poi riviste.
 */
export const DomandaSchema = z
  .object({
    materia: z.enum(MATERIA_IDS),
    id: z.string().regex(/^[a-z0-9-]+$/, "id: minuscole, numeri e trattini"),
    argomento: z.string().min(2),
    livello: z.number().int().min(1).max(5),
    testo: z.string().min(10),
    opzioni: z.array(z.string().min(1)).length(4),
    corretta: z.number().int().min(0).max(3),
    spiegazione: z.string().min(10),
    /** Da dove viene: libro + capitolo/pagina, oppure norma + articolo */
    fonte: z.string().min(3),
    /** Versione della banca domande (contenuti/VERSIONE): v1, poi v2… */
    versione: z.string().regex(/^v\d+$/),
  })
  .refine((d) => new Set(d.opzioni.map((o) => o.trim().toLowerCase())).size === 4, {
    message: "le 4 opzioni devono essere diverse",
  });

/** Un file della banca statica: un elenco di domande della stessa materia. */
export const FileDomandeSchema = z.array(DomandaSchema);
