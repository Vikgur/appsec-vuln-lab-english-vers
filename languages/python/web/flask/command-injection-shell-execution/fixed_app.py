from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/ping")
def ping():
    host = request.args.get("host")
    if not host:
        return jsonify({"error": "host required"}), 400

    # Fixed
    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True,
        check=False
    )

    return jsonify({
        "output": result.stdout
    })

if __name__ == "__main__":
    app.run(port=5000)