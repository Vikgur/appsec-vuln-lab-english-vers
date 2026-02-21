from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route("/parse", methods=["POST"])
def parse_yaml():
    data = request.get_data(as_text=True)

    # Fixed: используем SafeLoader
    try:
        obj = yaml.load(data, Loader=yaml.SafeLoader)
    except Exception:
        return jsonify({"error": "invalid yaml"}), 400

    return jsonify({"parsed": str(obj)})

if __name__ == "__main__":
    app.run(port=5000)