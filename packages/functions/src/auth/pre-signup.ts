import { AdminLinkProviderForUserCommand, ListUsersCommand } from "@aws-sdk/client-cognito-identity-provider";
import { cognito } from "@imieiconcorsi/core/cognito";
import { emailConsentita, MESSAGGIO_EMAIL_NON_CONSENTITA } from "@imieiconcorsi/core/registrazione";
import type { PreSignUpTriggerEvent } from "aws-lambda";
import { decidi, providerDaUsername } from "./collega-account";

// Trigger Cognito "pre sign-up": registrazione con email solo dai provider di posta
// diffusi (niente caselle usa e getta) e niente account doppi con la stessa email.
export const handler = async (event: PreSignUpTriggerEvent) => {
  const email = event.request.userAttributes.email?.trim().toLowerCase();
  if (!email) return event;
  if (event.triggerSource === "PreSignUp_SignUp" && !emailConsentita(email)) throw new Error(MESSAGGIO_EMAIL_NON_CONSENTITA);

  const res = await cognito.send(
    new ListUsersCommand({ UserPoolId: event.userPoolId, Filter: `email = "${email.replace(/"/g, "")}"` }),
  );
  const esistenti = (res.Users ?? []).map((u) => ({ username: u.Username!, stato: u.UserStatus }));
  const decisione = decidi(event.triggerSource, esistenti);

  if (decisione.azione === "rifiuta") throw new Error(decisione.messaggio);

  if (decisione.azione === "collega") {
    const provider = providerDaUsername(event.userName);
    if (!provider) return event;
    await cognito.send(
      new AdminLinkProviderForUserCommand({
        UserPoolId: event.userPoolId,
        DestinationUser: { ProviderName: "Cognito", ProviderAttributeValue: decisione.destinazione },
        SourceUser: { ProviderName: provider.nome, ProviderAttributeName: "Cognito_Subject", ProviderAttributeValue: provider.id },
      }),
    );
    // Cognito a questo punto rifiuta la creazione dell'utente doppio ("Already found an
    // entry for username…"): il sito rifà il login da solo e si entra nell'account collegato.
    console.log(`Collegato ${provider.nome} all'account esistente ${decisione.destinazione}`);
  }
  return event;
};
