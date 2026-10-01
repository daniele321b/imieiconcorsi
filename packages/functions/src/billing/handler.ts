import { getProfilo } from "@imieiconcorsi/core/db";
import { PIANI } from "@imieiconcorsi/core/domain";
import { HttpError, service } from "@imieiconcorsi/core/http";
import { assegnaPiano, scadenzaDa } from "@imieiconcorsi/core/piani";
import { z } from "zod";

const Abbonamento = z.object({
  piano: z.enum(["free", "medium", "pro"]),
  periodo: z.enum(["mensile", "annuale"]).default("mensile"),
});

export const handler = service({
  "GET /piani": async ({ userId, piano }) => {
    const profilo = await getProfilo(userId);
    return {
      piani: Object.values(PIANI),
      attuale: piano,
      periodo: profilo?.periodo,
      scadenza: profilo?.scadenzaPiano,
      modalita: process.env.BILLING_MODE,
    };
  },

  /**
   * In modalità "mock" il piano cambia subito, senza pagamento: serve per provare la beta.
   * Con la piattaforma di pagamento questa route creerà l'ordine e il checkout; il piano lo
   * attiverà la conferma del pagamento, sempre tramite assegnaPiano.
   * Dopo la risposta il sito rinnova il token, così il nuovo gruppo Cognito è subito attivo.
   */
  "POST /me/abbonamento": async (ctx) => {
    const { piano, periodo } = ctx.body(Abbonamento);
    if (process.env.BILLING_MODE !== "mock") {
      throw new HttpError(501, "Pagamenti non ancora attivi");
    }
    const scadenza = piano === "free" ? null : scadenzaDa(periodo);
    await assegnaPiano({ userId: ctx.userId, username: ctx.username, piano, periodo, scadenza });
    return { piano, periodo: piano === "free" ? undefined : periodo, scadenza };
  },
});
