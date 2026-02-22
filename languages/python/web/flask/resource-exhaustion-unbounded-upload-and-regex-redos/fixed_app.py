from flask import Flask, request, abort
import re

app = Flask(__name__)

# Fixed: ограничение размера запроса (10MB)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    # Fixed: стриминговая обработка
    total = 0
    chunk_size = 4096

    while True:
        chunk = file.stream.read(chunk_size)
        if not chunk:
            break
        total += len(chunk)

    return f"Uploaded {total} bytes"

@app.route("/validate")
def validate():
    user_input = request.args.get("q", "")

    # Fixed: безопасный regex (без вложенных квантификаторов)
    pattern = re.compile(r"^a+$")

    # Fixed: ограничение длины input
    if len(user_input) > 1000:
        abort(400)

    if pattern.match(user_input):
        return "Valid"

    return "Invalid"

if __name__ == "__main__":
    app.run()