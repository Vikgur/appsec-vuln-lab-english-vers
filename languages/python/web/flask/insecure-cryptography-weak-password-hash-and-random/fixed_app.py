from flask import Flask, request, jsonify
import bcrypt
import secrets

app = Flask(__name__)

users = {}

def hash_password(password):
    # Fixed: bcrypt (slow hash + salt)
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password, hashed):
    # Fixed
    return bcrypt.checkpw(password.encode(), hashed)

def generate_reset_token():
    # Fixed: криптографически стойкий random
    return secrets.token_urlsafe(32)

@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username")
    password = request.json.get("password")

    users[username] = {
        "password": hash_password(password),
        "reset_token": generate_reset_token()
    }

    return jsonify({"status": "created"})

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    user = users.get(username)

    if not user:
        return "Invalid", 401

    if verify_password(password, user["password"]):
        return "Logged in"

    return "Invalid", 401

if __name__ == "__main__":
    app.run(port=5000)