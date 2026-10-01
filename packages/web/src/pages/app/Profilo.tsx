import { PIANI, type CompartoId, type FrequenzaAvvisi, type MateriaId } from "@imieiconcorsi/core/domain";
import { LogOut, ShieldCheck } from "lucide-react";
import { useState } from "react";
import { AvvisiPicker, InteressiPicker, LivelliPicker } from "../../components/ProfiloPickers";
import { Alert, Badge, Button, ButtonLink, Card, Field, PageHeader } from "../../components/ui";
import { api } from "../../lib/api";
import { messaggioErrore, useAuth, useUtente } from "../../lib/auth";
import { data } from "../../lib/format";

export function Profilo() {
  const { utente } = useUtente();
  const { esci, ricarica } = useAuth();
  const [nome, setNome] = useState(utente.nome ?? "");
  const [interessi, setInteressi] = useState<CompartoId[]>(utente.interessi);
  const [livelli, setLivelli] = useState<Partial<Record<MateriaId, number>>>(utente.livelli);
  const [avvisi, setAvvisi] = useState<FrequenzaAvvisi>(utente.avvisi);
  const [salvataggio, setSalvataggio] = useState(false);
  const [esito, setEsito] = useState<{ tone: "success" | "error"; testo: string }>();

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
        <div>
          <p className="text-xs font-semibold text-slate-500 uppercase">Piano</p>
          <p className="mt-1 flex items-center gap-2 font-medium">
            {PIANI[utente.piano].nome} {utente.periodo && <Badge>{utente.periodo}</Badge>}
            {utente.admin && <Badge tone="amber">admin</Badge>}
            <ButtonLink to="/app/piani" variant="ghost" size="sm">
              Cambia
            </ButtonLink>
          </p>
        </div>
        <div>
          <p className="text-xs font-semibold text-slate-500 uppercase">
            {utente.piano !== "free" ? "Piano valido fino al" : "Iscritto dal"}
          </p>
          <p className="mt-1 font-medium">
            {utente.piano !== "free" ? (utente.scadenzaPiano ? data(utente.scadenzaPiano) : "Senza scadenza") : data(utente.createdAt)}
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

      <section className="space-y-3">
        <h2 className="text-lg font-bold">Livello nelle materie</h2>
        <LivelliPicker value={livelli} onChange={setLivelli} />
      </section>

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
    </div>
  );
}
