from flask import Flask, request, jsonify
import requests
from urllib.parse import urlparse
import socket
import ipaddress

app = Flask(__name__)

ALLOWED_HOSTS = {"example.com"}

def is_private_ip(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ipaddress.ip_address(ip).is_private
    except:
        return True

@app.route("/fetch")
def fetch():
    url = request.args.get("url")

    if not url:
        return "Missing url", 400

    parsed = urlparse(url)

    # Fixed: разрешаем только http/https
    if parsed.scheme not in ("http", "https"):
        return "Invalid scheme", 400

    hostname = parsed.hostname

    # Fixed: запрет private IP
    if is_private_ip(hostname):
        return "Forbidden host", 403

    # Fixed: allowlist доменов
    if hostname not in ALLOWED_HOSTS:
        return "Host not allowed", 403

    response = requests.get(url, timeout=3)

    return jsonify({
        "status_code": response.status_code,
        "body": response.text[:500]
    })

if __name__ == "__main__":
    app.run(port=5000)