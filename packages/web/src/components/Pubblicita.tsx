import { Crown } from "lucide-react";
import { useEffect, useRef, useState } from "react";
import { config } from "../lib/config";
import { ButtonLink, Button, Card } from "./ui";

/** Secondi prima che si possa andare avanti. */
const ATTESA = 3;

declare global {
  interface Window {
    adsbygoogle?: unknown[];
  }
}

/** Carica una volta sola lo script di Google AdSense. */
function caricaAdsense(client: string) {
  if (document.querySelector("script[data-adsense]")) return;
  const s = document.createElement("script");
  s.async = true;
  s.src = `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${encodeURIComponent(client)}`;
  s.crossOrigin = "anonymous";
  s.dataset.adsense = "1";
  document.head.appendChild(s);
}

/**
 * Annuncio tra una domanda e l'altra (solo piano Free). Con AdSense configurato in
 * config.json mostra un annuncio Google; altrimenti un annuncio interno sui piani.
 */
export function Pubblicita({ onContinua }: { onContinua: () => void }) {
  const [attesa, setAttesa] = useState(ATTESA);
  const adsense = config.pubblicita?.adsenseClient && config.pubblicita.adsenseSlot ? config.pubblicita : undefined;
  const slot = useRef<HTMLModElement>(null);

  useEffect(() => {
    const t = setInterval(() => setAttesa((s) => Math.max(0, s - 1)), 1000);
    return () => clearInterval(t);
  }, []);

  useEffect(() => {
    if (!adsense || !slot.current) return;
    caricaAdsense(adsense.adsenseClient!);
    try {
      (window.adsbygoogle = window.adsbygoogle ?? []).push({});
    } catch {}
  }, [adsense]);

  return (
    <Card className="animate-fade-up p-6 sm:p-8">
      <p className="text-xs font-semibold tracking-wide text-slate-400 uppercase">Pubblicità</p>
      {adsense ? (
        <ins
          ref={slot}
          className="adsbygoogle mt-3 block min-h-60"
          data-ad-client={adsense.adsenseClient}
          data-ad-slot={adsense.adsenseSlot}
          data-ad-format="auto"
          data-full-width-responsive="true"
        />
      ) : (
        <div className="mt-3 rounded-2xl bg-brand-950 p-6 text-white">
          <Crown className="size-6 text-accent-300" />
          <p className="mt-3 text-lg font-extrabold">Studia senza interruzioni</p>
          <p className="mt-1 text-sm text-brand-200">
            Con Medium niente pubblicità, banche dati ufficiali dei tuoi concorsi e simulazioni illimitate.
          </p>
          <ButtonLink to="/app/piani" variant="accent" size="sm" className="mt-4">
            Scopri i piani
          </ButtonLink>
        </div>
      )}
      <div className="mt-6 flex items-center justify-between gap-4">
        <p className="text-xs text-slate-400">Nel piano Free compare un annuncio ogni 5 domande.</p>
        <Button disabled={attesa > 0} onClick={onContinua}>
          {attesa > 0 ? `Continua tra ${attesa}…` : "Continua"}
        </Button>
      </div>
    </Card>
  );
}
