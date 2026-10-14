import cf from 'cloudfront';

// Manutenzione (docs/MANUTENZIONE.md): con la chiave "attiva" = "si" nella KeyValueStore del sito,
// ogni richiesta riceve la pagina "Siamo in manutenzione" (o, per /api, un JSON) con stato 503:
// sito pubblico, area privata e API restano chiusi. Si accende e si spegne in pochi secondi con
// scripts/deploy.sh manutenzione on|off, senza rifare il deploy. Chi ha il link con ?accesso=<codice>
// riceve un cookie e vede il sito normale (per controllare prima di riaprire).
// Questo pezzo sta in cima alle funzioni spa.js e api-prefix.js (Terraform le unisce); l'id della
// KeyValueStore lo mette Terraform al posto di __KVS_ID__.

var kvs = cf.kvs('__KVS_ID__');
var COOKIE_ACCESSO = 'imc_accesso_manutenzione'; // stesso nome nel cookie della risposta qui sotto
var MESSAGGIO_PREDEFINITO = 'Stiamo aggiornando iMieiConcorsi. Torniamo il prima possibile.';

// Valore di una chiave della KeyValueStore; '' se manca (chiave mai scritta = manutenzione spenta).
async function valore(chiave) {
  try {
    return await kvs.get(chiave);
  } catch (e) {
    return '';
  }
}

// Testo sicuro dentro l'HTML.
function html(testo) {
  return testo.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// Intestazioni comuni delle risposte di manutenzione: niente cache, riprova tra mezz'ora.
function intestazioni(tipo) {
  return {
    'content-type': { value: tipo },
    'cache-control': { value: 'no-store' },
    'retry-after': { value: '1800' },
    'x-robots-tag': { value: 'noindex' },
  };
}

// La pagina "Siamo in manutenzione": autonoma (stili e logo dentro), chiara e scura.
function paginaManutenzione(messaggio) {
  var corpo =
    '<!doctype html><html lang="it"><head><meta charset="utf-8">' +
    '<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">' +
    '<title>iMieiConcorsi · In manutenzione</title><style>' +
    ':root{--sf:#f8fafc;--card:#fff;--txt:#0f172a;--sec:#475569;--bordo:#e2e8f0;--brand:#4f46e5}' +
    '@media (prefers-color-scheme:dark){:root{--sf:#0b1020;--card:#151b2e;--txt:#f1f5f9;--sec:#a5b4c8;--bordo:#26304a;--brand:#818cf8}}' +
    '*{box-sizing:border-box}body{margin:0;min-height:100vh;display:grid;place-items:center;padding:24px 16px;' +
    'background:var(--sf);color:var(--txt);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}' +
    'main{width:100%;max-width:480px;background:var(--card);border:1px solid var(--bordo);border-radius:20px;padding:32px 28px;text-align:center}' +
    '.logo{display:inline-flex;align-items:center;gap:8px;font-weight:800;font-size:20px;letter-spacing:-.02em}' +
    '.logo b{color:var(--brand)}h1{font-size:24px;line-height:1.25;margin:28px 0 12px}' +
    'p{margin:0 0 12px;color:var(--sec)}.msg{color:var(--txt);font-weight:600}' +
    'a{display:inline-block;margin-top:16px;padding:12px 22px;border-radius:12px;background:#4f46e5;color:#fff;font-weight:600;text-decoration:none}' +
    '</style></head><body><main>' +
    '<span class="logo"><svg width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#4f46e5"/>' +
    '<path d="M9 17.5l4.5 4.5L23 11" fill="none" stroke="#fbbf24" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>' +
    '<span>iMiei<b>Concorsi</b></span></span>' +
    '<h1>Siamo in manutenzione</h1>' +
    '<p class="msg">' + html(messaggio || MESSAGGIO_PREDEFINITO) + '</p>' +
    '<p>I tuoi dati, i progressi e il tuo piano sono al sicuro: non devi fare nulla.</p>' +
    '<a href="/">Riprova</a></main></body></html>';
  return {
    statusCode: 503,
    statusDescription: 'Service Unavailable',
    headers: intestazioni('text/html; charset=utf-8'),
    body: { encoding: 'text', data: corpo },
  };
}

// Stessa cosa per le chiamate all'API e ai dati JSON: l'app già aperta ricarica la pagina (lib/api.ts).
function jsonManutenzione(messaggio) {
  return {
    statusCode: 503,
    statusDescription: 'Service Unavailable',
    headers: intestazioni('application/json; charset=utf-8'),
    body: { encoding: 'text', data: JSON.stringify({ error: messaggio || MESSAGGIO_PREDEFINITO, code: 'MANUTENZIONE' }) },
  };
}

// Risposta di manutenzione per questa richiesta, oppure null per lasciarla passare.
// ?manutenzione=anteprima mostra la pagina anche a manutenzione spenta (per vederla prima).
async function manutenzione(request, comeJson) {
  var q = request.querystring || {};
  var anteprima = q.manutenzione && q.manutenzione.value === 'anteprima';
  var attiva = (await valore('attiva')) === 'si';
  if (!attiva && !anteprima) return null;
  var messaggio = await valore('messaggio');
  if (attiva && !anteprima) {
    var codice = await valore('accesso');
    if (codice) {
      // Link con il codice: cookie per 12 ore e di nuovo alla stessa pagina, senza il codice nell'indirizzo.
      if (q.accesso && q.accesso.value === codice) {
        return {
          statusCode: 302,
          statusDescription: 'Found',
          headers: { location: { value: request.uri }, 'cache-control': { value: 'no-store' } },
          cookies: {
            imc_accesso_manutenzione: { value: codice, attributes: 'Path=/; Max-Age=43200; Secure; HttpOnly; SameSite=Lax' },
          },
        };
      }
      var cookie = request.cookies && request.cookies[COOKIE_ACCESSO];
      if (cookie && cookie.value === codice) return null;
    }
  }
  return comeJson ? jsonManutenzione(messaggio) : paginaManutenzione(messaggio);
}
