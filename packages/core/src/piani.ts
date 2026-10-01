import { UpdateCommand } from "@aws-sdk/lib-dynamodb";
import { impostaPianoCognito } from "./cognito";
import { db, tables } from "./db";
import type { Periodo, PianoId } from "./domain";

export const GIORNI_PERIODO: Record<Periodo, number> = { mensile: 30, annuale: 365 };

/** Fine di un periodo pagato che parte adesso (nessun pro-rata: il nuovo periodo parte dal pagamento). */
export function scadenzaDa(periodo: Periodo, da = new Date()) {
  return new Date(da.getTime() + GIORNI_PERIODO[periodo] * 86_400_000).toISOString();
}

/**
 * Unico punto in cui cambia il piano di un utente: gruppo Cognito (fonte di verità del
 * piano, finisce nel token) + scadenza sul profilo. Lo usano pagamenti, pannello admin
 * e job delle scadenze.
 */
export async function assegnaPiano(args: {
  userId: string;
  username: string;
  piano: PianoId;
  /** null = senza scadenza (solo l'admin) */
  scadenza: string | null;
  periodo?: Periodo;
}) {
  await impostaPianoCognito(args.username, args.piano);

  const now = new Date().toISOString();
  const set = [
    // Il profilo può non esistere ancora (piano dato dall'admin prima del primo accesso).
    "username = if_not_exists(username, :un)",
    "onboarded = if_not_exists(onboarded, :f)",
    "interessi = if_not_exists(interessi, :vuota)",
    "livelli = if_not_exists(livelli, :mappa)",
    "avvisi = if_not_exists(avvisi, :avvisi)",
    "createdAt = if_not_exists(createdAt, :now)",
    "updatedAt = :now",
  ];
  const remove = ["promemoriaInviatoPer"];
  const values: Record<string, unknown> = {
    ":un": args.username,
    ":f": false,
    ":vuota": [],
    ":mappa": {},
    ":avvisi": "settimanale",
    ":now": now,
  };
  if (args.piano !== "free" && args.scadenza) {
    set.push("scadenzaPiano = :s");
    values[":s"] = args.scadenza;
  } else {
    remove.push("scadenzaPiano");
  }
  if (args.piano !== "free" && args.periodo) {
    set.push("periodo = :p");
    values[":p"] = args.periodo;
  } else {
    remove.push("periodo");
  }

  await db.send(
    new UpdateCommand({
      TableName: tables.users,
      Key: { userId: args.userId },
      UpdateExpression: `SET ${set.join(", ")} REMOVE ${remove.join(", ")}`,
      ExpressionAttributeValues: values,
    }),
  );
}
