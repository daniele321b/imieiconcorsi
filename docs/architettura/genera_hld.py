"""Genera docs/architettura/iMieiConcorsi-HLD.drawio: una pagina per ambiente (dev, prod, shared).

Schema ad alto livello (account, region, rete, servizi principali e flussi). Quando cambia
l'architettura (servizi, tabelle, job), aggiorna qui e rigenera:

    python3 docs/architettura/genera_hld.py docs/architettura/iMieiConcorsi-HLD.drawio

Il file .drawio si apre con draw.io (app desktop o https://app.diagrams.net).
"""
import sys
from xml.sax.saxutils import escape

COLORI = {
    "rete": "#8C4FFF", "integrazione": "#E7157B", "calcolo": "#ED7100", "storage": "#7AA116",
    "db": "#C925D1", "sicurezza": "#DD344C", "ml": "#01A88D", "gestione": "#E7157B", "costi": "#7AA116",
}


class Pagina:
    def __init__(self, nome):
        self.nome = nome
        self.celle = []
        self.n = 2

    def _id(self):
        self.n += 1
        return f"{self.nome}-{self.n}"

    def _cella(self, valore, stile, x, y, w, h, vertex=True, extra=""):
        i = self._id()
        v = escape(valore, {'"': "&quot;"})
        tipo = 'vertex="1"' if vertex else 'edge="1"'
        self.celle.append(
            f'<mxCell id="{i}" value="{v}" style="{stile}" {tipo} parent="1" {extra}>'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>'
        )
        return i

    def gruppo(self, testo, x, y, w, h, icona, colore, tratteggio=False, testo_colore=None):
        stile = (
            "points=[];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=13;fontStyle=1;"
            f"container=0;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.{icona};"
            f"strokeColor={colore};fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor={testo_colore or colore};"
            f"dashed={1 if tratteggio else 0};"
        )
        return self._cella(testo, stile, x, y, w, h)

    def riquadro(self, testo, x, y, w, h, fondo="#F5F5F5", bordo="#999999", tratteggio=False, size=11, align="left"):
        stile = (
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={fondo};strokeColor={bordo};fontSize={size};align={align};"
            f"verticalAlign=top;spacingLeft=8;spacingTop=4;arcSize=6;dashed={1 if tratteggio else 0};"
        )
        return self._cella(testo, stile, x, y, w, h)

    def icona(self, testo, x, y, icona, categoria, w=54, etichetta="sotto"):
        pos = {
            "sotto": "verticalLabelPosition=bottom;verticalAlign=top;align=center;",
            "destra": "labelPosition=right;verticalLabelPosition=middle;align=left;verticalAlign=middle;spacingLeft=4;",
            "sopra": "verticalLabelPosition=top;verticalAlign=bottom;align=center;",
        }[etichetta]
        stile = (
            "sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],"
            "[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;gradientColor=none;"
            f"fillColor={COLORI[categoria]};strokeColor=#ffffff;dashed=0;{pos}"
            f"html=1;fontSize=11;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{icona};"
        )
        return self._cella(testo, stile, x, y, w, w)

    def utenti(self, testo, x, y):
        stile = (
            "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;"
            "verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=11;aspect=fixed;pointerEvents=1;"
            "shape=mxgraph.aws4.users;"
        )
        return self._cella(testo, stile, x, y, 54, 54)

    def testo(self, testo, x, y, w, h, size=11, colore="#232F3E", grassetto=False):
        stile = f"text;html=1;whiteSpace=wrap;align=left;verticalAlign=top;fontSize={size};fontColor={colore};fontStyle={1 if grassetto else 0};"
        return self._cella(testo, stile, x, y, w, h)

    def freccia(self, da, a, etichetta="", tratteggio=False, colore="#545B64", uscita=None, ingresso=None, punti=()):
        stile = (
            f"edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;html=1;endArrow=block;endFill=1;fontSize=10;"
            f"strokeColor={colore};fontColor=#232F3E;labelBackgroundColor=#FFFFFF;dashed={1 if tratteggio else 0};"
        )
        if uscita:
            stile += f"exitX={uscita[0]};exitY={uscita[1]};exitDx=0;exitDy=0;"
        if ingresso:
            stile += f"entryX={ingresso[0]};entryY={ingresso[1]};entryDx=0;entryDy=0;"
        i = self._id()
        v = escape(etichetta, {'"': "&quot;"})
        pts = "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in punti)
        geo = f'<mxGeometry relative="1" as="geometry"><Array as="points">{pts}</Array></mxGeometry>' if punti else '<mxGeometry relative="1" as="geometry"/>'
        self.celle.append(f'<mxCell id="{i}" value="{v}" style="{stile}" edge="1" parent="1" source="{da}" target="{a}">{geo}</mxCell>')

    def xml(self):
        celle = "".join(self.celle)
        return (
            f'<diagram id="{self.nome}" name="{self.nome}"><mxGraphModel dx="1800" dy="1200" grid="1" gridSize="10" guides="1" '
            'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1800" pageHeight="1180" math="0" shadow="0">'
            f'<root><mxCell id="0"/><mxCell id="1" parent="0"/>{celle}</root></mxGraphModel></diagram>'
        )


def ambiente(env):
    prod = env == "prod"
    nome = f"imieiconcorsi-{env}"
    dominio = "imieiconcorsi.it" if prod else "dev.imieiconcorsi.it"
    p = Pagina("Prod" if prod else "Dev")

    p.testo(
        f"<b>iMieiConcorsi — ambiente {env.upper()}</b> (risorse <i>{nome}-…</i>) · https://{dominio}"
        + (" · <font color='#DD344C'>congelato durante la revisione SES</font>" if prod else ""),
        20, 10, 1500, 30, size=16,
    )

    # Esterni (colonna a sinistra)
    utenti = p.utenti("Utenti<br>(browser, telefono)", 90, 335)
    p.riquadro("<b>Servizi esterni</b>", 20, 520, 210, 470, fondo="#FFFFFF", bordo="#545B64", tratteggio=True)
    p.riquadro("<b>Google / Facebook</b><br>login social (OAuth)<br>tramite Cognito", 35, 545, 180, 60, fondo="#FFF4E5", bordo="#ED7100")
    stripe = p.riquadro("<b>Stripe</b><br>Checkout e webhook" + ("<br>(senza chiavi live: acquisti chiusi)" if prod else "<br>(modalità test o mock)"), 35, 630, 180, 65, fondo="#F3EEFF", bordo="#8C4FFF")
    inpa = p.riquadro("<b>inPA</b><br>API pubblica dei bandi", 35, 787, 180, 55, fondo="#E8F4FD", bordo="#147EBA")
    caselle = p.riquadro("<b>Caselle email</b><br>degli utenti e dell'admin", 35, 880, 180, 55, fondo="#FDEDEF", bordo="#DD344C")

    # Account e zone
    p.gruppo("Account AWS (unico: dev, prod e shared; ospita anche altre app)", 250, 50, 1530, 1110, "group_account", "#CD2264")
    p.gruppo("Globale / us-east-1 (CloudFront e servizi collegati)", 275, 95, 370, 1040, "group_region", "#00A4A6", tratteggio=True, testo_colore="#147EBA")
    p.gruppo("Region eu-south-1 (Milano)", 670, 95, 1090, 1040, "group_region", "#00A4A6", tratteggio=True, testo_colore="#147EBA")

    # Globale
    r53 = p.icona("Route 53<br>zona imieiconcorsi.it", 300, 185, "route_53", "rete", etichetta="sopra")
    acm = p.icona("ACM<br>certificato HTTPS", 520, 185, "certificate_manager_3", "sicurezza", etichetta="sopra")
    cf = p.icona(f"CloudFront<br>{dominio}<br>HTTPS, HSTS, CSP<br>funzioni: sito a pagina unica, /api", 420, 330, "cloudfront", "rete", w=64)
    if prod:
        waf = p.icona("AWS WAF<br>OWASP, input noti, IP malevoli<br>2.000 rich./5 min per IP<br>100 POST pubblici per IP", 300, 500, "waf", "sicurezza")
        p.freccia(waf, cf, "filtra", uscita=(0.5, 0), ingresso=(0, 0.85), punti=[(327, 384)])
    else:
        p.riquadro("Niente WAF in dev<br>(in prod sì, circa 8-10 $/mese)", 300, 510, 200, 45, fondo="#FFFFFF", bordo="#BBBBBB", tratteggio=True)
    snsUs = p.icona(f"SNS {nome}-<br>monitoraggio-us-east-1<br>(allarmi CloudFront, budget)", 300, 960, "sns", "integrazione")
    budget = p.icona("AWS Budgets<br>budget dell'account", 520, 960, "budgets", "costi")

    # Region
    p.riquadro(
        "<b>Rete:</b> nessuna VPC, subnet, NAT o load balancer. L'app è tutta serverless: servizi gestiti AWS "
        "raggiunti con IAM. Le Lambda girano fuori da VPC; l'unico ingresso pubblico è CloudFront (l'API Gateway "
        "rifiuta chi non passa da CloudFront, con un'intestazione segreta).",
        690, 125, 620, 62, fondo="#FFF8E1", bordo="#F2B807",
    )
    s3web = p.icona("S3 sito<br>privato, solo da CloudFront", 720, 230, "s3", "storage")
    cognito = p.icona("Cognito user pool<br>login SRP, gruppi = piani<br>Google e Facebook (OAuth)", 930, 230, "cognito", "sicurezza")
    trigger = p.icona("Lambda trigger (2)<br>auth-pre-signup<br>auth-accessi", 1180, 230, "lambda", "calcolo")
    bedrock = p.icona("Amazon Bedrock<br>Claude Sonnet 4.6<br>(profilo EU, solo Pro)", 1600, 230, "bedrock", "ml")

    apigw = p.icona("API Gateway HTTP<br>JWT Cognito<br>1.000 rich./s<br>picchi 2.000", 720, 430, "api_gateway", "integrazione")
    servizi = p.icona(
        "Lambda API (8)<br>profile · concorsi · study<br>billing · ai · richieste<br>pubblico · admin",
        930, 420, "lambda", "calcolo", w=64,
    )
    dynamo = p.icona(
        "<b>DynamoDB</b> (13 tabelle, on demand,<br>backup continuo" + (", protette)" if prod else ")")
        + "<br>users · concorsi · follows · questions<br>attempts · codici · ordini · banche-dati<br>richieste · progressi · contatori<br>accessi · attivita",
        1300, 420, "dynamodb", "db", w=64, etichetta="destra",
    )

    scheduler = p.icona("EventBridge Scheduler<br>6:00 scraper · 6:15 scadenze<br>7:00 avvisi<br>dom e mer 3:00 pulizia", 720, 660, "eventbridge", "integrazione")
    jobs = p.icona("Lambda job (4)<br>inpa-scraper · pulizia-bandi<br>avvisi · scadenze", 930, 660, "lambda", "calcolo")
    s3cont = p.icona("S3 contenuti<br>domande, PDF banche dati<br>(PDF dall'admin con URL firmato)", 1300, 660, "s3", "storage")
    cont = p.icona("Lambda contenuti (2)<br>import-domande<br>estrai-banca-dati", 1560, 660, "lambda", "calcolo")

    sns = p.icona(f"SNS<br>{nome}-avvisi-admin<br>{nome}-monitoraggio", 720, 880, "sns", "integrazione")
    cw = p.icona("CloudWatch<br>allarmi, dashboard<br>log 14 giorni", 930, 880, "cloudwatch_2", "gestione")
    ses = p.icona("SES (ambiente shared)<br>noreply@imieiconcorsi.it<br>configuration set", 1150, 880, "simple_email_service", "sicurezza", etichetta="destra")

    # Flussi
    p.freccia(utenti, r53, "DNS", uscita=(0.5, 0), ingresso=(0, 0.5), punti=[(117, 212)])
    p.freccia(utenti, cf, "HTTPS", uscita=(1, 0.5), ingresso=(0, 0.5))
    p.freccia(r53, cf, "alias", uscita=(0.5, 1), ingresso=(0.3, 0), punti=[(327, 290), (439, 290)])
    p.freccia(acm, cf, "", tratteggio=True, uscita=(0.5, 1), ingresso=(0.7, 0), punti=[(547, 290), (465, 290)])
    p.freccia(cf, s3web, "sito e bandi in cache", uscita=(1, 0.25), ingresso=(0, 0.5), punti=[(660, 346), (660, 257)])
    p.freccia(cf, apigw, "/api + segreto", uscita=(1, 0.75), ingresso=(0, 0.5), punti=[(690, 378), (690, 457)])
    p.freccia(apigw, cognito, "verifica token", tratteggio=True, uscita=(1, 0.2), ingresso=(0, 0.5), punti=[(860, 441), (860, 257)])
    p.freccia(cognito, trigger, "eventi", uscita=(1, 0.5), ingresso=(0, 0.5))
    p.freccia(apigw, servizi, "route", uscita=(1, 0.5), ingresso=(0, 0.5))
    p.freccia(servizi, dynamo, "dati", uscita=(1, 0.5), ingresso=(0, 0.5))
    p.freccia(servizi, bedrock, "tutor AI", uscita=(0.75, 0), ingresso=(0, 0.5), punti=[(978, 360), (1560, 360), (1560, 257)])
    p.freccia(servizi, stripe, "pagamenti", uscita=(0, 0.9), ingresso=(1, 0.5), punti=[(880, 478), (880, 662)])
    p.freccia(servizi, ses, "email", uscita=(1, 1), ingresso=(0, 0.3), punti=[(1120, 484), (1120, 896)])
    p.freccia(scheduler, jobs, "orari", uscita=(1, 0.5), ingresso=(0, 0.5))
    p.freccia(jobs, dynamo, "", uscita=(0.75, 0), ingresso=(0.25, 1), punti=[(970, 610), (1316, 610)])
    p.freccia(jobs, inpa, "bandi", uscita=(0.25, 1), ingresso=(1, 0.5), punti=[(943, 814)])
    p.freccia(jobs, ses, "avvisi", uscita=(1, 0.75), ingresso=(0, 0.7), punti=[(1100, 700), (1100, 918)])
    p.freccia(s3cont, cont, "nuovo file", uscita=(1, 0.5), ingresso=(0, 0.5))
    p.freccia(cont, dynamo, "", uscita=(0.5, 0), ingresso=(0.75, 1), punti=[(1587, 610), (1348, 610)])
    p.freccia(cw, sns, "allarmi", uscita=(0, 0.5), ingresso=(1, 0.5))
    p.freccia(sns, caselle, "email admin", uscita=(0, 0.5), ingresso=(1, 0.5))
    p.freccia(ses, caselle, "email", uscita=(0.5, 1), ingresso=(0.5, 1), punti=[(1177, 1075), (125, 1075)])
    p.freccia(snsUs, caselle, "", tratteggio=True, uscita=(0, 0.5), ingresso=(0.75, 1), punti=[(260, 987), (260, 955), (170, 955)])
    p.freccia(budget, snsUs, "", uscita=(0, 0.5), ingresso=(1, 0.5))

    p.testo(
        "Legenda: frecce piene = traffico o chiamate; tratteggiate = login, configurazione o file caricati. "
        "Stato Terraform, SES e zona DNS: pagina «Shared».",
        690, 1100, 1060, 30, size=10, colore="#545B64",
    )
    return p


def shared():
    p = Pagina("Shared")
    p.testo("<b>iMieiConcorsi — risorse comuni (ambiente SHARED e bootstrap)</b>, lette da dev e prod con terraform_remote_state", 20, 10, 1500, 30, size=16)
    utenti = p.utenti("Admin / sviluppatore<br>(scripts/deploy.sh)", 90, 560)
    caselle = p.riquadro("<b>Caselle email</b><br>utenti e admin", 35, 430, 180, 70, fondo="#FDEDEF", bordo="#DD344C")
    p.gruppo("Account AWS (unico)", 250, 50, 1100, 760, "group_account", "#CD2264")
    p.gruppo("Globale", 275, 95, 330, 690, "group_region", "#00A4A6", tratteggio=True, testo_colore="#147EBA")
    p.gruppo("Region eu-south-1 (Milano)", 630, 95, 700, 690, "group_region", "#00A4A6", tratteggio=True, testo_colore="#147EBA")
    p.riquadro("<b>Rete:</b> nessuna VPC o subnet: solo servizi gestiti.", 650, 135, 420, 28, fondo="#FFF8E1", bordo="#F2B807")

    r53 = p.icona(
        "Route 53 — zona imieiconcorsi.it<br>(dominio comprato su Route 53)<br>sito: imieiconcorsi.it, dev.imieiconcorsi.it<br>"
        "email: DKIM ×3, MAIL FROM (MX, SPF), DMARC",
        410, 220, "route_53", "rete",
    )
    ses = p.icona(
        "<b>SES</b><br>dominio imieiconcorsi.it (DKIM)<br>mittente noreply@imieiconcorsi.it<br>"
        "configuration set imieiconcorsi<br>soppressione rimbalzi e reclami<br>(account e configuration set)<br>"
        "sandbox: solo indirizzi verificati",
        720, 220, "simple_email_service", "sicurezza", etichetta="destra",
    )
    sns = p.icona("SNS imieiconcorsi-ses-notifiche<br>rimbalzi, reclami, rifiuti → email", 1160, 220, "sns", "integrazione")
    stato = p.icona("S3 stato Terraform<br>(bootstrap, versionato, cifrato)<br>dev/ · prod/ · shared/", 720, 560, "s3", "storage")
    p.riquadro(
        "Usano queste risorse:<br>• <b>dev</b> e <b>prod</b>: mittente SES, configuration set, zona DNS<br>"
        "• lo stato di ogni ambiente sta nello stesso bucket (chiavi diverse)<br>"
        "• nello stesso account e nella stessa zona ci sono anche identità di altre app (es. Fleet Audit)",
        960, 540, 350, 120, fondo="#FFFFFF", bordo="#BBBBBB",
    )
    p.freccia(r53, ses, "record DKIM / MAIL FROM", tratteggio=True, uscita=(1, 0.5), ingresso=(0, 0.5))
    p.freccia(ses, sns, "eventi", uscita=(0.5, 0), ingresso=(0.5, 0), punti=[(747, 190), (1187, 190)])
    p.freccia(sns, caselle, "email all'admin", uscita=(1, 0.5), ingresso=(1, 0.3), punti=[(1290, 247), (1290, 451)])
    p.freccia(ses, caselle, "email dell'app", uscita=(0.5, 1), ingresso=(1, 0.8), punti=[(747, 486)])
    p.freccia(utenti, stato, "terraform", tratteggio=True, uscita=(1, 0.5), ingresso=(0, 0.5))
    return p


def main(uscita):
    pagine = [ambiente("dev"), ambiente("prod"), shared()]
    xml = '<mxfile host="app.diagrams.net" type="device">' + "".join(p.xml() for p in pagine) + "</mxfile>"
    with open(uscita, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"scritto {uscita}: {sum(len(p.celle) for p in pagine)} elementi")


if __name__ == "__main__":
    main(sys.argv[1])
