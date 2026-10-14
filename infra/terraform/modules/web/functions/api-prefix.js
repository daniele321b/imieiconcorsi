// /api/me -> /me: le route dell'API Gateway non hanno il prefisso /api.
// Con la manutenzione accesa (manutenzione.js, messo in cima da Terraform) risponde subito 503 in JSON.
async function handler(event) {
  var request = event.request;
  var chiusa = await manutenzione(request, true);
  if (chiusa) return chiusa;
  request.uri = request.uri.replace(/^\/api(?=\/|$)/, '') || '/';
  return request;
}
