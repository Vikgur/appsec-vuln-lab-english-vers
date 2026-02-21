from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

BASE_DIR = "/var/www/files"

@app.route("/download")
def download():
    filename = request.args.get("file")
    if not filename:
        abort(400)

    filepath = os.path.join(BASE_DIR, filename)

    if not os.path.exists(filepath):
        abort(404)

    return send_file(filepath)

if __name__ == "__main__":
    app.run(port=5000)