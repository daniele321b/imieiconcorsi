import {
  AdminAddUserToGroupCommand,
  AdminDeleteUserCommand,
  AdminListGroupsForUserCommand,
  AdminRemoveUserFromGroupCommand,
  AdminUpdateUserAttributesCommand,
  CognitoIdentityProviderClient,
  ListUsersInGroupCommand,
  type UserType,
} from "@aws-sdk/client-cognito-identity-provider";
import { GRUPPI, type PianoId } from "./domain";
import { env } from "./env";

// Operazioni su Amazon Cognito, il servizio che gestisce gli account (login, password, Google
// e Facebook). Qui stanno solo i dati d'identità: email, nome e gruppi. Il gruppo dice il
// piano (medium, pro) e il ruolo (admin); tutto il resto sta in DynamoDB sotto l'id anonimo (sub).
// Le Lambda che usano queste funzioni hanno USER_POOL_ID e i permessi cognito-idp in Terraform.

/** Client Cognito condiviso (la regione arriva dall'ambiente della Lambda). */
export const cognito = new CognitoIdentityProviderClient({});
/** Id del pool degli utenti, passato da Terraform (local.cognito_env). */
export const userPoolId = () => env("USER_POOL_ID");

/** Valore di un attributo di un utente Cognito (es. "email", "sub", "name"). */
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

/** Gruppi Cognito attuali di un utente (piano e admin), letti al momento. */
export async function gruppiDi(username: string) {
  const res = await cognito.send(new AdminListGroupsForUserCommand({ UserPoolId: userPoolId(), Username: username, Limit: 60 }));
  return (res.Groups ?? []).map((g) => g.GroupName!);
}

/** Aggiunge (`presente` = true) o toglie un utente da un gruppo, es. "admin". */
export async function impostaGruppo(username: string, gruppo: string, presente: boolean) {
  const Command = presente ? AdminAddUserToGroupCommand : AdminRemoveUserFromGroupCommand;
  await cognito.send(new Command({ UserPoolId: userPoolId(), Username: username, GroupName: gruppo }));
}

/** Il nome è un dato personale: si salva solo su Cognito, non nel database. */
export async function aggiornaNome(username: string, nome: string) {
  await cognito.send(
    new AdminUpdateUserAttributesCommand({
      UserPoolId: userPoolId(),
      Username: username,
      UserAttributes: [{ Name: "name", Value: nome }],
    }),
  );
}

/** Ultimo passo dell'eliminazione dell'account: cancella l'utente (e il suo login) da Cognito. */
export async function eliminaUtenteCognito(username: string) {
  await cognito.send(new AdminDeleteUserCommand({ UserPoolId: userPoolId(), Username: username }));
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
