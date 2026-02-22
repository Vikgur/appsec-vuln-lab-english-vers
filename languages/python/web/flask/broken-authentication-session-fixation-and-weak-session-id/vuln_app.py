from flask import Flask, request, make_response, redirect
import hashlib

app = Flask(__name__)

sessions = {}
users = {"admin": "password"}

def generate_session_id(username):
    # слабый и предсказуемый session id
    return hashlib.md5(username.encode()).hexdigest()

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if users.get(username) != password:
        return "Invalid", 401

    # сервер принимает существующий session id из cookie
    session_id = request.cookies.get("session_id")

    if not session_id:
        session_id = generate_session_id(username)

    sessions[session_id] = username

    resp = make_response("Logged in")
    resp.set_cookie("session_id", session_id)
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