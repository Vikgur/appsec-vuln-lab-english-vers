# Наличие requirements.txt/Poetry.lock
# flask==2.3.2  # Fixed
# requests==2.31.0  # Fixed
# pyyaml==6.0.1  # Fixed

from flask import Flask, request
import yaml
import requests

app = Flask(__name__)

@app.route("/parse", methods=["POST"])
def parse():
    data = request.data

    # Fixed: безопасный loader
    obj = yaml.safe_load(data)

    return str(obj)

@app.route("/external")
def external():
    url = request.args.get("url")
    return requests.get(url, timeout=3)

if __name__ == "__main__":
    app.run()