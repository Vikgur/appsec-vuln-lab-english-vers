from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["appdb"]
users = db["users"]

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # Fixed: строгая типизация + allowlist
    if not isinstance(username, str) or not isinstance(password, str):
        return jsonify({"status": "fail"}), 400

    if len(username) > 50 or len(password) > 128:
        return jsonify({"status": "fail"}), 400

    query = {
        "username": username,
        "password": password
    }

    user = users.find_one(query)

    if user:
        return jsonify({"status": "ok"})
    return jsonify({"status": "fail"}), 401

if __name__ == "__main__":
    app.run(port=5000)