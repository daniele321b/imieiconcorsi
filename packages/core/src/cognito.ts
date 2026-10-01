import {
  AdminAddUserToGroupCommand,
  AdminRemoveUserFromGroupCommand,
  AdminUpdateUserAttributesCommand,
  CognitoIdentityProviderClient,
  ListUsersInGroupCommand,
  type UserType,
} from "@aws-sdk/client-cognito-identity-provider";
import { GRUPPI, type PianoId } from "./domain";
import { env } from "./env";

export const cognito = new CognitoIdentityProviderClient({});
export const userPoolId = () => env("USER_POOL_ID");

export const attributo = (user: UserType, nome: string) => user.Attributes?.find((a) => a.Name === nome)?.Value;

/** Porta l'utente nel gruppo del piano (e lo toglie dall'altro gruppo a pagamento). */
export async function impostaPianoCognito(username: string, piano: PianoId) {
  const pagati = [GRUPPI.medium, GRUPPI.pro] as const;
  for (const gruppo of pagati) {
    if (gruppo === piano) continue;
    await cognito.send(new AdminRemoveUserFromGroupCommand({ UserPoolId: userPoolId(), Username: username, GroupName: gruppo }));
  }
  if (piano !== "free") {
    await cognito.send(new AdminAddUserToGroupCommand({ UserPoolId: userPoolId(), Username: username, GroupName: piano }));
  }
}

export async function impostaGruppo(username: string, gruppo: string, presente: boolean) {
  const Command = presente ? AdminAddUserToGroupCommand : AdminRemoveUserFromGroupCommand;
  await cognito.send(new Command({ UserPoolId: userPoolId(), Username: username, GroupName: gruppo }));
}

export async function aggiornaNome(username: string, nome: string) {
  await cognito.send(
    new AdminUpdateUserAttributesCommand({
      UserPoolId: userPoolId(),
      Username: username,
      UserAttributes: [{ Name: "name", Value: nome }],
    }),
  );
}

/** Tutti gli utenti di un gruppo, pagina per pagina (60 alla volta). */
export async function* utentiNelGruppo(gruppo: string): AsyncGenerator<UserType> {
  let NextToken: string | undefined;
  do {
    const res = await cognito.send(
      new ListUsersInGroupCommand({ UserPoolId: userPoolId(), GroupName: gruppo, Limit: 60, NextToken }),
    );
    yield* res.Users ?? [];
    NextToken = res.NextToken;
  } while (NextToken);
}
