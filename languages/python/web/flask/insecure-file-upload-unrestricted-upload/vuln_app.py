from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "file required"}), 400

    filepath = os.path.join(UPLOAD_DIR, file.filename)
    file.save(filepath)

    return jsonify({"status": "uploaded", "path": filepath})

if __name__ == "__main__":
    app.run(port=5000)