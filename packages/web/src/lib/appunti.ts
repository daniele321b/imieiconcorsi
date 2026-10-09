/**
 * Copia negli appunti. navigator.clipboard non c'è o fallisce su alcuni telefoni
 * (iOS in certe condizioni, browser in-app): ripiego sul vecchio execCommand.
 */
export async function copiaTesto(testo: string): Promise<boolean> {
  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(testo);
      return true;
    }
  } catch {}
  const area = document.createElement("textarea");
  area.value = testo;
  area.setAttribute("readonly", "");
  // Fuori schermo ma selezionabile; font 16px per evitare lo zoom di iOS.
  Object.assign(area.style, { position: "fixed", top: "0", left: "-9999px", fontSize: "16px" });
  document.body.appendChild(area);
  area.select();
  area.setSelectionRange(0, testo.length);
  let ok = false;
  try {
    ok = document.execCommand("copy");
  } catch {}
  area.remove();
  return ok;
}
