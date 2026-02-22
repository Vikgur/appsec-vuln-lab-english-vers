from flask import Flask, request, jsonify
import hashlib
import random
import string

app = Flask(__name__)

users = {}

def hash_password(password):
    # УЯЗВИМОСТЬ: MD5 без salt
    return hashlib.md5(password.encode()).hexdigest()

def generate_reset_token():
    # УЯЗВИМОСТЬ: предсказуемый random
    return ''.join(random.choice(string.ascii_letters) for _ in range(16))

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

    if user["password"] == hash_password(password):
        return "Logged in"

    return "Invalid", 401

if __name__ == "__main__":
    app.run(port=5000)