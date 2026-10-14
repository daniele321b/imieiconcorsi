// Le route del client (es. /app/concorsi/123) non sono file su S3: servono index.html.
// I file veri (/assets/x.js, /config.json, /favicon.svg) hanno un'estensione e passano così come sono.
// Prima di tutto la manutenzione (manutenzione.js, messo in cima da Terraform): i dati JSON
// (/config.json, /dati/bandi/…) ricevono il JSON 503, il resto la pagina.
async function handler(event) {
  var request = event.request;
  var last = request.uri.split('/').pop();
  var chiusa = await manutenzione(request, /\.json$/.test(last));
  if (chiusa) return chiusa;
  if (last.indexOf('.') === -1) {
    request.uri = '/index.html';
  }
  return request;
}
