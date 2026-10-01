const dataFmt = new Intl.DateTimeFormat("it-IT", { day: "numeric", month: "long", year: "numeric" });
const dataBreveFmt = new Intl.DateTimeFormat("it-IT", { day: "numeric", month: "short" });
const euroFmt = new Intl.NumberFormat("it-IT", { style: "currency", currency: "EUR" });

export const data = (iso?: string) => (iso ? dataFmt.format(new Date(iso)) : "—");
export const dataBreve = (iso?: string) => (iso ? dataBreveFmt.format(new Date(iso)) : "—");
export const euro = (n: number) => euroFmt.format(n);

export function giorniA(iso?: string) {
  if (!iso) return undefined;
  return Math.ceil((new Date(iso).getTime() - Date.now()) / 86_400_000);
}

export function scadenzaTesto(iso?: string) {
  const g = giorniA(iso);
  if (g === undefined) return "Scadenza non indicata";
  if (g < 0) return "Scaduto";
  if (g === 0) return "Scade oggi";
  if (g === 1) return "Scade domani";
  return `Scade tra ${g} giorni`;
}

const PROCEDURE: Record<string, string> = {
  ESAMI: "Esami",
  TITOLI: "Titoli",
  TITOLI_ESAMI: "Titoli ed esami",
  COLLOQUIO: "Colloquio",
  TITOLI_COLLOQUIO: "Titoli e colloquio",
};
export const tipoProcedura = (t?: string) => (t ? (PROCEDURE[t] ?? t.replace(/_/g, " ").toLowerCase()) : undefined);

export function durata(ms: number) {
  const s = Math.max(0, Math.floor(ms / 1000));
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = s % 60;
  const mm = String(m).padStart(2, "0");
  const ss = String(sec).padStart(2, "0");
  return h ? `${h}:${mm}:${ss}` : `${mm}:${ss}`;
}
