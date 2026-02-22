from flask import Flask, request, make_response, redirect
import secrets

app = Flask(__name__)

sessions = {}
users = {"admin": "password"}

def generate_session_id():
    # Fixed: криптографически стойкий id
    return secrets.token_urlsafe(32)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if users.get(username) != password:
        return "Invalid", 401

    # Fixed: всегда создаём новый session id (ротация)
    session_id = generate_session_id()

    sessions[session_id] = username

    resp = make_response("Logged in")

    # Fixed: безопасные cookie-флаги
    resp.set_cookie(
        "session_id",
        session_id,
        httponly=True,
        secure=True,
        samesite="Lax"
    )

    return resp

@app.route("/profile")
def profile():
    session_id = request.cookies.get("session_id")
    user = sessions.get(session_id)

    if not user:
        return "Unauthorized", 401

    return f"Hello {user}"

if __name__ == "__main__":
    app.run(port=5000)