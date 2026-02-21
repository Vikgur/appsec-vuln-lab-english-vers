from flask import Flask, request, jsonify
import pickle
import base64

app = Flask(__name__)

@app.route("/import", methods=["POST"])
def import_data():
    data = request.get_json()
    payload = data.get("data")

    if not payload:
        return jsonify({"error": "data required"}), 400

    decoded = base64.b64decode(payload)
    obj = pickle.loads(decoded)

    return jsonify({"status": "loaded", "type": str(type(obj))})

if __name__ == "__main__":
    app.run(port=5000)