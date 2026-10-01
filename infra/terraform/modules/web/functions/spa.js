// Le route del client (es. /app/concorsi/123) non sono file su S3: servono index.html.
// I file veri (/assets/x.js, /config.json, /favicon.svg) hanno un'estensione e passano così come sono.
function handler(event) {
  var request = event.request;
  var last = request.uri.split('/').pop();
  if (last.indexOf('.') === -1) {
    request.uri = '/index.html';
  }
  return request;
}
