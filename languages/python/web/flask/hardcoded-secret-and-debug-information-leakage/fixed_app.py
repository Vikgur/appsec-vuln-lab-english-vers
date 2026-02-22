from flask import Flask, request, jsonify
import jwt
import os

app = Flask(__name__)

# Fixed: секреты из environment
JWT_SECRET = os.environ.get("JWT_SECRET")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

@app.route("/token")
def generate_token():
    username = request.args.get("user")

    token = jwt.encode(
        {"sub": username},
        JWT_SECRET,
        algorithm="HS256"
    )

    return jsonify({"token": token})

@app.route("/error")
def trigger_error():
    try:
        return 1 / 0
    except Exception:
        # Fixed: не раскрываем детали
        return "Internal error", 500

if __name__ == "__main__":
    # Fixed: debug выключен
    app.run(debug=False)