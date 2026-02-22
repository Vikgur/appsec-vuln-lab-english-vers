from flask import Flask, request, jsonify

app = Flask(__name__)

# Примитивное "хранилище"
users = {
    "1": {"id": "1", "username": "alice", "email": "alice@example.com"},
    "2": {"id": "2", "username": "bob", "email": "bob@example.com"},
}

# Эмуляция аутентификации
def get_current_user():
    return request.headers.get("X-User-Id")

@app.route("/api/user/<user_id>")
def get_user(user_id):
    current_user = get_current_user()

    if not current_user:
        return "Unauthorized", 401

    # УЯЗВИМОСТЬ: нет проверки, что user_id == current_user
    user = users.get(user_id)

    if not user:
        return "Not found", 404

    return jsonify(user)

if __name__ == "__main__":
    app.run(port=5000)