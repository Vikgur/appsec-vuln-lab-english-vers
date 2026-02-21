from flask import Flask, request, session, redirect, abort
import secrets

app = Flask(__name__)
app.secret_key = "secret"

users = {
    "admin": {"email": "admin@example.com"}
}

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    if username in users:
        session["user"] = username
        # Fixed: генерируем CSRF token
        session["csrf_token"] = secrets.token_hex(16)
        return "Logged in"
    return "Invalid", 401

@app.route("/profile")
def profile():
    if "user" not in session:
        return "Unauthorized", 401

    # Fixed: вставляем CSRF token в форму
    return f"""
    <form method="POST" action="/change-email">
        <input type="hidden" name="csrf_token" value="{session['csrf_token']}">
        <input type="email" name="email">
        <button type="submit">Change</button>
    </form>
    """

@app.route("/change-email", methods=["POST"])
def change_email():
    if "user" not in session:
        return "Unauthorized", 401

    # Fixed: проверка CSRF token
    token = request.form.get("csrf_token")
    if not token or token != session.get("csrf_token"):
        abort(403)

    new_email = request.form.get("email")
    users[session["user"]]["email"] = new_email

    return "Email changed"

if __name__ == "__main__":
    app.run(port=5000)