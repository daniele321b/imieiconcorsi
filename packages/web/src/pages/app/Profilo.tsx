import { MATERIE, periodo, PIANI, type CompartoId, type FrequenzaAvvisi, type MateriaId } from "@imieiconcorsi/core/domain";
import { LifeBuoy, LogOut, ShieldCheck, Trash2 } from "lucide-react";
import { useState } from "react";
import { useNavigate } from "react-router";
import { FeedbackApp } from "../../components/FeedbackApp";
import { InvitaAmico } from "../../components/InvitaAmico";
import { StoricoPagamenti } from "../../components/StoricoPagamenti";
import { StoricoSeguiti } from "../../components/StoricoSeguiti";
import { AvvisiPicker, InteressiPicker, LivelliPicker } from "../../components/ProfiloPickers";
import { Alert, Badge, Button, ButtonLink, Card, Espandibile, Field, PageHeader } from "../../components/ui";
import { api } from "../../lib/api";
import { messaggioErrore, useAuth, useUtente } from "../../lib/auth";
import { data } from "../../lib/format";

// Profilo (/app/profilo): piano, nome, comparti, livelli, avvisi, storico dei pagamenti, invita
// un amico, storico dei concorsi seguiti, assistenza, parere sull'app, uscita ed eliminazione.

/** Pagina /app/profilo. */
export function Profilo() {
  const { utente } = useUtente();
  const { esci, ricarica } = useAuth();
  const [nome, setNome] = useState(utente.nome ?? "");
  const [interessi, setInteressi] = useState<CompartoId[]>(utente.interessi);
  const [livelli, setLivelli] = useState<Partial<Record<MateriaId, number>>>(utente.livelli);
  const [avvisi, setAvvisi] = useState<FrequenzaAvvisi>(utente.avvisi);
  const [salvataggio, setSalvataggio] = useState(false);
  const [esito, setEsito] = useState<{ tone: "success" | "error"; testo: string }>();
  const navigate = useNavigate();
  const [conferma, setConferma] = useState("");
  const [eliminazione, setEliminazione] = useState(false);
  const [erroreEliminazione, setErroreEliminazione] = useState<string>();

  async function eliminaAccount() {
    setEliminazione(true);
    setErroreEliminazione(undefined);
    try {
      await api("/me", { method: "DELETE" });
      // L'utente Cognito non esiste più: si chiude la sessione locale e si torna alla home.
      await esci().catch(() => {});
      navigate("/", { replace: true });
    } catch (err) {
      setErroreEliminazione(messaggioErrore(err));
      setEliminazione(false);
    }
  }

  async function salva() {
    setSalvataggio(true);
    setEsito(undefined);
    try {
      await api("/me/profilo", { method: "PUT", body: { nome: nome || undefined, interessi, livelli, avvisi } });
      // Il nome sta su Cognito: con un token nuovo lo vede subito tutta l'app.
      await ricarica({ rinnovaToken: true });
      setEsito({ tone: "success", testo: "Profilo aggiornato." });
    } catch (err) {
      setEsito({ tone: "error", testo: messaggioErrore(err) });
    } finally {
      setSalvataggio(false);
    }
  }

  return (
    <div className="space-y-8">
      <PageHeader
        title="Il tuo profilo"
        actions={
          <div className="flex gap-2">
            {utente.admin && (
              <ButtonLink to="/admin" variant="secondary">
                <ShieldCheck className="size-4" /> Pannello admin
              </ButtonLink>
            )}
            <Button variant="secondary" onClick={() => void esci()}>
              <LogOut className="size-4" /> Esci
            </Button>
          </div>
        }
      />

      <Card className="grid gap-4 sm:grid-cols-3">
        <div>
          <p className="text-xs font-semibold text-slate-500 uppercase">Email</p>
          <p className="mt-1 truncate font-medium">{utente.email ?? "—"}</p>
        </div>
        {utente.admin ? (
          <div>
            <p className="text-xs font-semibold text-slate-500 uppercase">Ruolo</p>
            <p className="mt-1 flex items-center gap-2 font-medium">
              <Badge tone="amber">Admin</Badge> tutte le funzioni
            </p>
          </div>
        ) : (
          <div>
            <p className="text-xs font-semibold text-slate-500 uppercase">Piano</p>
            <p className="mt-1 flex items-center gap-2 font-medium">
              {PIANI[utente.piano].nome} {utente.periodo && <Badge>{periodo(utente.periodo).nome}</Badge>}
              <ButtonLink to="/app/piani" variant="ghost" size="sm">
                Cambia
              </ButtonLink>
            </p>
          </div>
        )}
        <div>
          <p className="text-xs font-semibold text-slate-500 uppercase">
            {!utente.admin && utente.piano !== "free" ? "Piano valido fino al" : "Iscritto dal"}
          </p>
          <p className="mt-1 font-medium">
            {!utente.admin && utente.piano !== "free"
              ? utente.scadenzaPiano
                ? data(utente.scadenzaPiano)
                : "Senza scadenza"
              : data(utente.createdAt)}
          </p>
        </div>
      </Card>

      <section className="space-y-3">
        <h2 className="text-lg font-bold">Nome</h2>
        <Field label="Come vuoi che ti chiamiamo?" name="nome" value={nome} onChange={(e) => setNome(e.target.value)} className="max-w-sm" />
      </section>

      <section className="space-y-3">
        <h2 className="text-lg font-bold">Comparti di interesse</h2>
        <InteressiPicker value={interessi} onChange={setInteressi} />
      </section>

      <Espandibile titolo="Livello nelle materie" riassunto={`${Object.keys(livelli).length} su ${MATERIE.length} indicate`}>
        <LivelliPicker value={livelli} onChange={setLivelli} />
      </Espandibile>

      <section className="space-y-3">
        <h2 className="text-lg font-bold">Avvisi sui nuovi bandi</h2>
        <AvvisiPicker value={avvisi} onChange={setAvvisi} />
      </section>

      <div className="sticky bottom-20 flex flex-wrap items-center justify-end gap-4 md:bottom-4">
        {esito && (
          <div className="flex-1">
            <Alert tone={esito.tone} onClose={() => setEsito(undefined)}>
              {esito.testo}
            </Alert>
          </div>
        )}
        <Button size="lg" loading={salvataggio} disabled={!interessi.length} onClick={() => void salva()}>
          Salva modifiche
        </Button>
      </div>

      {!utente.admin && <StoricoPagamenti />}

      {!utente.admin && <InvitaAmico />}

      <StoricoSeguiti />

      <section className="space-y-3">
        <h2 className="flex items-center gap-2 text-lg font-bold">
          <LifeBuoy className="size-5 text-brand-600" /> Assistenza
        </h2>
        <p className="text-sm text-slate-500">Ti serve una banca dati, hai trovato una domanda sbagliata o hai un problema con l'accesso o un pagamento? Scrivici.</p>
        <ButtonLink to="/app/assistenza" variant="secondary">
          Le mie richieste
          {!!utente.richiesteDaLeggere &&
            ` · ${utente.richiesteDaLeggere} ${utente.richiesteDaLeggere === 1 ? "risposta nuova" : "risposte nuove"}`}
        </ButtonLink>
      </section>

      <FeedbackApp />

      <section className="space-y-3 rounded-2xl p-5 ring-1 ring-rose-200">
        <h2 className="flex items-center gap-2 text-lg font-bold text-rose-700">
          <Trash2 className="size-5" /> Elimina account
        </h2>
        <p className="text-sm text-slate-600">
          Cancella email, nome, profilo di studio, concorsi seguiti e sessioni. L'operazione non si può annullare e un eventuale
          piano attivo non viene rimborsato.
        </p>
        {erroreEliminazione && <Alert tone="error">{erroreEliminazione}</Alert>}
        <div className="flex flex-wrap items-end gap-3">
          <Field
            label='Per confermare scrivi "ELIMINA"'
            name="conferma-eliminazione"
            value={conferma}
            onChange={(e) => setConferma(e.target.value)}
            className="max-w-xs"
          />
          <Button variant="danger" disabled={conferma !== "ELIMINA"} loading={eliminazione} onClick={() => void eliminaAccount()}>
            Elimina definitivamente
          </Button>
        </div>
      </section>
    </div>
  );
}
