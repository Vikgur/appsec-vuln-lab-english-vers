from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/fetch")
def fetch():
    url = request.args.get("url")

    if not url:
        return "Missing url", 400

    # УЯЗВИМОСТЬ: сервер делает запрос к user-controlled URL
    response = requests.get(url, timeout=3)

    return jsonify({
        "status_code": response.status_code,
        "body": response.text[:500]
    })

if __name__ == "__main__":
    app.run(port=5000)