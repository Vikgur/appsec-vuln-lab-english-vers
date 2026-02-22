from flask import Flask, request
import re

app = Flask(__name__)

# ❌ УЯЗВИМОСТЬ 1: нет ограничения на размер upload
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    data = file.read()  # читает весь файл в память
    return f"Uploaded {len(data)} bytes"

# ❌ УЯЗВИМОСТЬ 2: catastrophic backtracking
@app.route("/validate")
def validate():
    user_input = request.args.get("q", "")

    pattern = re.compile(r"(a+)+$")  # опасный regex
    if pattern.match(user_input):
        return "Valid"

    return "Invalid"

if __name__ == "__main__":
    app.run()