from flask import Flask, request, session, redirect

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
        return "Logged in"
    return "Invalid", 401

@app.route("/change-email", methods=["POST"])
def change_email():
    if "user" not in session:
        return "Unauthorized", 401

    new_email = request.form.get("email")
    users[session["user"]]["email"] = new_email

    return "Email changed"

if __name__ == "__main__":
    app.run(port=5000)