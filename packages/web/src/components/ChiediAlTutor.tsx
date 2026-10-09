import { Sparkles } from "lucide-react";
import { useState } from "react";
import type { DomandaTutor } from "../lib/api";
import { useUtente } from "../lib/auth";
import { TutorChat } from "./TutorChat";
import { Badge, PremiumModal } from "./ui";

/**
 * "Chiedi al tutor AI" sotto una domanda con la risposta giusta già visibile (studio,
 * revisione dopo la consegna, consultazione della banca dati). Pro: si apre la chat con la
 * domanda, la risposta giusta e, se c'è, quella data. Free e Medium: l'invito al piano Pro.
 */
export function ChiediAlTutor({
  domanda,
  risposta,
}: {
  domanda: Omit<DomandaTutor, "risposta">;
  /** Risposta data; assente = domanda solo consultata (banca dati) */
  risposta?: number | null;
}) {
  const { utente } = useUtente();
  const [aperto, setAperto] = useState(false);

  const suggerimenti =
    risposta === undefined
      ? ["Spiegami perché è questa la risposta giusta", "Dammi un trucco per ricordarla"]
      : risposta !== domanda.corretta
        ? ["Perché la mia risposta è sbagliata?", "Dammi un trucco per ricordarlo"]
        : ["Spiegamelo meglio con un esempio"];

  if (aperto && utente.limiti.ai) {
    return <TutorChat className="mt-4" domanda={{ ...domanda, ...(risposta !== undefined ? { risposta } : {}) }} suggerimenti={suggerimenti} />;
  }
  return (
    <>
      <button onClick={() => setAperto(true)} className="mt-3 inline-flex items-center gap-1.5 text-sm font-semibold text-brand-600 hover:text-brand-700">
        <Sparkles className="size-4" /> Chiedi al tutor AI
        {!utente.limiti.ai && <Badge tone="amber">Pro</Badge>}
      </button>
      {aperto && !utente.limiti.ai && (
        <PremiumModal titolo="Tutor AI" onClose={() => setAperto(false)}>
          Con il piano <strong>Pro</strong> il tutor AI ti spiega ogni domanda, anche quelle delle banche dati ufficiali: perché la
          risposta giusta è quella, come ricordarla, con esempi. In più, allenamenti con domande nuove sui tuoi punti deboli.
        </PremiumModal>
      )}
    </>
  );
}
