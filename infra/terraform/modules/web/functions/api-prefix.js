// /api/me -> /me: le route dell'API Gateway non hanno il prefisso /api.
function handler(event) {
  var request = event.request;
  request.uri = request.uri.replace(/^\/api(?=\/|$)/, '') || '/';
  return request;
}
