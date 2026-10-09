import { nomeComparto } from "@imieiconcorsi/core/domain";
import { Bookmark, BookmarkCheck, CalendarClock, MapPin, Users } from "lucide-react";
import { Link } from "react-router";
import type { ConcorsoApi } from "../lib/api";
import { giorniA, scadenzaTesto, tipoProcedura } from "../lib/format";
import { Badge, Button, cx } from "./ui";

type Sintesi = Omit<ConcorsoApi, "descrizione">;

export function ConcorsoCard({
  concorso,
  onSegui,
  inCorso,
}: {
  concorso: Sintesi;
  onSegui?: (c: Sintesi) => void;
  inCorso?: boolean;
}) {
  const giorni = giorniA(concorso.scadenza);
  const urgente = giorni !== undefined && giorni <= 7;

  return (
    // Tutta la card apre il dettaglio (il link si allarga con after:inset-0); il pulsante Segui sta sopra.
    <article className="group relative flex min-w-0 flex-col rounded-2xl bg-white p-5 shadow-sm ring-1 ring-slate-200/70 transition hover:shadow-md hover:ring-brand-200">
      <div className="flex items-start justify-between gap-3">
        <p className="line-clamp-1 min-w-0 text-xs font-semibold tracking-wide break-words text-brand-600 uppercase">{concorso.ente}</p>
        <Badge tone={urgente ? "red" : "slate"} className="shrink-0">
          <CalendarClock className="size-3" /> {scadenzaTesto(concorso.scadenza)}
        </Badge>
      </div>
      <Link
        to={`/app/concorsi/${concorso.id}`}
        className="mt-2 line-clamp-2 font-bold break-words text-slate-900 group-hover:text-brand-700 after:absolute after:inset-0 after:rounded-2xl"
      >
        {concorso.figura ?? concorso.titolo}
      </Link>
      <div className="mt-3 flex flex-wrap gap-x-4 gap-y-1 text-sm text-slate-500">
        {concorso.sedi[0] && (
          <span className="inline-flex min-w-0 items-center gap-1">
            <MapPin className="size-3.5 shrink-0" /> <span className="truncate">{concorso.sedi[0]}</span>
          </span>
        )}
        {concorso.posti ? (
          <span className="inline-flex items-center gap-1">
            <Users className="size-3.5" /> {concorso.posti} {concorso.posti === 1 ? "posto" : "posti"}
          </span>
        ) : null}
      </div>
      <div className="mt-4 flex flex-wrap items-center gap-2">
        <Badge tone="brand">{nomeComparto(concorso.comparto)}</Badge>
        {tipoProcedura(concorso.tipoProcedura) && <Badge>{tipoProcedura(concorso.tipoProcedura)}</Badge>}
        {onSegui && (
          <Button
            size="sm"
            variant={concorso.seguito ? "secondary" : "primary"}
            className={cx("relative z-10 ml-auto")}
            loading={inCorso}
            onClick={() => onSegui(concorso)}
          >
            {concorso.seguito ? <BookmarkCheck className="size-4" /> : <Bookmark className="size-4" />}
            {concorso.seguito ? "Seguito" : "Segui"}
          </Button>
        )}
      </div>
    </article>
  );
}
