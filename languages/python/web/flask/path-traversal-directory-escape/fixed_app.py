from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

BASE_DIR = "/var/www/files"

@app.route("/download")
def download():
    filename = request.args.get("file")
    if not filename:
        abort(400)

    # Fixed: нормализация пути
    normalized_path = os.path.normpath(filename)

    # Fixed: запрещаем абсолютные пути и выход вверх
    if normalized_path.startswith("..") or os.path.isabs(normalized_path):
        abort(403)

    filepath = os.path.join(BASE_DIR, normalized_path)

    # Fixed: финальная проверка границы директории
    real_base = os.path.realpath(BASE_DIR)
    real_path = os.path.realpath(filepath)

    if not real_path.startswith(real_base + os.sep):
        abort(403)

    if not os.path.exists(real_path):
        abort(404)

    return send_file(real_path)

if __name__ == "__main__":
    app.run(port=5000)