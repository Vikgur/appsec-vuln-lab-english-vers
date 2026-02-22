from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

# Сервер думает, что использует RS256
PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqh...
-----END PUBLIC KEY-----"""

@app.route("/profile")
def profile():
    auth = request.headers.get("Authorization")

    if not auth or not auth.startswith("Bearer "):
        return "Missing token", 401

    token = auth.split(" ")[1]

    # УЯЗВИМОСТЬ: нет явной проверки алгоритма
    # нет проверки exp / iss / aud
    payload = jwt.decode(
        token,
        PUBLIC_KEY,
        options={"verify_signature": True}
    )

    return jsonify({
        "user": payload.get("sub"),
        "role": payload.get("role")
    })

if __name__ == "__main__":
    app.run(port=5000)