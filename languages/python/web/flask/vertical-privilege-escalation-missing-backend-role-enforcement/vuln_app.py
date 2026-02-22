from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "1": {"id": "1", "username": "alice", "role": "user"},
    "2": {"id": "2", "username": "bob", "role": "admin"},
}

def get_current_user():
    user_id = request.headers.get("X-User-Id")
    return users.get(user_id)

@app.route("/admin/delete_user", methods=["POST"])
def delete_user():
    current_user = get_current_user()

    if not current_user:
        return "Unauthorized", 401

    # УЯЗВИМОСТЬ: нет проверки роли
    target_user_id = request.json.get("user_id")

    if target_user_id in users:
        del users[target_user_id]
        return jsonify({"status": "deleted"})

    return "Not found", 404

if __name__ == "__main__":
    app.run(port=5000)