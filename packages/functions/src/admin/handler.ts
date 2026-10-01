import {
  AdminDisableUserCommand,
  AdminEnableUserCommand,
  AdminGetUserCommand,
  DescribeUserPoolCommand,
  ListUsersCommand,
  type UserType,
} from "@aws-sdk/client-cognito-identity-provider";
import { attributo, cognito, userPoolId, utentiNelGruppo } from "@imieiconcorsi/core/cognito";
import { batchGet, tables } from "@imieiconcorsi/core/db";
import { GRUPPI, pianoDaGruppi, type Profilo } from "@imieiconcorsi/core/domain";
import { HttpError, notFound, richiediAdmin, service } from "@imieiconcorsi/core/http";
import { assegnaPiano } from "@imieiconcorsi/core/piani";
import { z } from "zod";

// Pannello di controllo: solo per il gruppo Cognito "admin" (controllato in ogni route).

const PAGINA = 50;

const CambioPiano = z.object({
  piano: z.enum(["free", "medium", "pro"]),
  /** Data di fine (YYYY-MM-DD o ISO). Assente o null = senza scadenza. */
  scadenza: z.string().datetime({ offset: true }).or(z.string().date()).nullable().optional(),
});

const CambioStato = z.object({ abilitato: z.boolean() });

/** Membri dei gruppi medium/pro/admin, per username. */
async function gruppiPerUtente() {
  const mappa = new Map<string, string[]>();
  for (const gruppo of Object.values(GRUPPI)) {
    for await (const u of utentiNelGruppo(gruppo)) {
      mappa.set(u.Username!, [...(mappa.get(u.Username!) ?? []), gruppo]);
    }
  }
  return mappa;
}

async function utenteCognito(username: string) {
  try {
    return await cognito.send(new AdminGetUserCommand({ UserPoolId: userPoolId(), Username: username }));
  } catch (err) {
    if (err instanceof Error && err.name === "UserNotFoundException") throw notFound("Utente");
    throw err;
  }
}

const fineGiornata = (data: string) => (data.length === 10 ? `${data}T23:59:59.000Z` : new Date(data).toISOString());

export const handler = service({
  "GET /admin/riepilogo": async (ctx) => {
    richiediAdmin(ctx);
    const [pool, gruppi] = await Promise.all([
      cognito.send(new DescribeUserPoolCommand({ UserPoolId: userPoolId() })),
      gruppiPerUtente(),
    ]);
    const conta = (g: string) => [...gruppi.values()].filter((gs) => gs.includes(g)).length;
    return {
      utenti: pool.UserPool?.EstimatedNumberOfUsers ?? 0,
      medium: conta(GRUPPI.medium),
      pro: conta(GRUPPI.pro),
      admin: conta(GRUPPI.admin),
    };
  },

  /** ?cerca=inizio-email &pagina=<token della pagina successiva> */
  "GET /admin/utenti": async (ctx) => {
    richiediAdmin(ctx);
    const cerca = ctx.query.cerca?.trim().replace(/"/g, "");
    const [lista, gruppi] = await Promise.all([
      cognito.send(
        new ListUsersCommand({
          UserPoolId: userPoolId(),
          Limit: PAGINA,
          PaginationToken: ctx.query.pagina || undefined,
          Filter: cerca ? `email ^= "${cerca}"` : undefined,
        }),
      ),
      gruppiPerUtente(),
    ]);
    const utenti = lista.Users ?? [];
    const profili = await batchGet<Profilo>(
      tables.users,
      utenti.map((u) => ({ userId: attributo(u, "sub") })),
      "userId, scadenzaPiano, periodo, onboarded",
    );
    const profiloDi = new Map(profili.map((p) => [p.userId, p]));

    return {
      utenti: utenti.map((u: UserType) => {
        const sub = attributo(u, "sub")!;
        const gs = gruppi.get(u.Username!) ?? [];
        const p = profiloDi.get(sub);
        return {
          username: u.Username!,
          email: attributo(u, "email"),
          nome: attributo(u, "name"),
          accesso: u.Username!.includes("_") ? u.Username!.split("_")[0] : "email",
          stato: u.UserStatus,
          abilitato: u.Enabled ?? true,
          creatoIl: u.UserCreateDate?.toISOString(),
          piano: pianoDaGruppi(gs.filter((g) => g !== GRUPPI.admin)),
          admin: gs.includes(GRUPPI.admin),
          scadenzaPiano: p?.scadenzaPiano,
          periodo: p?.periodo,
          onboarded: p?.onboarded ?? false,
        };
      }),
      pagina: lista.PaginationToken,
    };
  },

  "PUT /admin/utenti/{username}/piano": async (ctx) => {
    richiediAdmin(ctx);
    const { piano, scadenza } = ctx.body(CambioPiano);
    const user = await utenteCognito(ctx.params.username!);
    const sub = user.UserAttributes?.find((a) => a.Name === "sub")?.Value;
    if (!sub) throw new HttpError(500, "Utente senza sub");
    await assegnaPiano({
      userId: sub,
      username: user.Username!,
      piano,
      scadenza: piano === "free" || !scadenza ? null : fineGiornata(scadenza),
    });
    return { ok: true };
  },

  "PUT /admin/utenti/{username}/stato": async (ctx) => {
    richiediAdmin(ctx);
    const { abilitato } = ctx.body(CambioStato);
    const username = ctx.params.username!;
    if (username === ctx.username) throw new HttpError(400, "Non puoi disattivare il tuo account");
    const Command = abilitato ? AdminEnableUserCommand : AdminDisableUserCommand;
    await cognito.send(new Command({ UserPoolId: userPoolId(), Username: username }));
    return { ok: true };
  },
});
