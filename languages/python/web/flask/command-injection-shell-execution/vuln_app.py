from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/ping")
def ping():
    host = request.args.get("host")
    if not host:
        return jsonify({"error": "host required"}), 400

    cmd = f"ping -c 1 {host}"
    output = os.popen(cmd).read()

    return jsonify({
        "command": cmd,
        "output": output
    })

if __name__ == "__main__":
    app.run(port=5000)