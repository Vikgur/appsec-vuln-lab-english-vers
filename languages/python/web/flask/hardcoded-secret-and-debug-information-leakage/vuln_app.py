from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

# ❌ УЯЗВИМОСТЬ: секрет в коде
JWT_SECRET = "super-secret-production-key"
DB_PASSWORD = "P@ssw0rd123"

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
    # ❌ УЯЗВИМОСТЬ: утечка через stack trace
    return 1 / 0

if __name__ == "__main__":
    # ❌ УЯЗВИМОСТЬ: debug включён
    app.run(debug=True)