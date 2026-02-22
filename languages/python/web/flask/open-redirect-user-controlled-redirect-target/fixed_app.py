from flask import Flask, request, redirect, url_for
from urllib.parse import urlparse

app = Flask(__name__)

ALLOWED_HOST = "example.com"

def is_safe_url(target):
    parsed = urlparse(target)

    # Fixed: разрешаем только относительные пути
    if parsed.netloc != "":
        return False

    # запрет //evil.com
    if target.startswith("//"):
        return False

    return True

@app.route("/login")
def login():
    next_url = request.args.get("next")

    if next_url and is_safe_url(next_url):  # Fixed
        return redirect(next_url)

    # Fixed: безопасный дефолт
    return redirect(url_for("home"))

@app.route("/")
def home():
    return "Home"

if __name__ == "__main__":
    app.run(port=5000)