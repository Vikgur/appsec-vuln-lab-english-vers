from flask import Flask, request
import yaml
import requests

app = Flask(__name__)

@app.route("/parse", methods=["POST"])
def parse():
    data = request.data

    # ❌ Использование небезопасного loader (если старая версия PyYAML)
    obj = yaml.load(data)

    return str(obj)

@app.route("/external")
def external():
    url = request.args.get("url")
    return requests.get(url).text

if __name__ == "__main__":
    app.run()