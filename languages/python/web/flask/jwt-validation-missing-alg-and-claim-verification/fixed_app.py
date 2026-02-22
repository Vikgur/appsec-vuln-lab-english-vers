from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqh...
-----END PUBLIC KEY-----"""

EXPECTED_ISSUER = "auth.mycompany.com"
EXPECTED_AUDIENCE = "api.mycompany.com"

@app.route("/profile")
def profile():
    auth = request.headers.get("Authorization")

    if not auth or not auth.startswith("Bearer "):
        return "Missing token", 401

    token = auth.split(" ")[1]

    try:
        payload = jwt.decode(
            token,
            PUBLIC_KEY,
            algorithms=["RS256"],  # Fixed: жёстко задан алгоритм
            issuer=EXPECTED_ISSUER,  # Fixed: проверка iss
            audience=EXPECTED_AUDIENCE,  # Fixed: проверка aud
            options={
                "require": ["exp", "iss", "aud"],  # Fixed
            }
        )
    except jwt.InvalidTokenError:
        return "Invalid token", 401

    return jsonify({
        "user": payload.get("sub"),
        "role": payload.get("role")
    })

if __name__ == "__main__":
    app.run(port=5000)