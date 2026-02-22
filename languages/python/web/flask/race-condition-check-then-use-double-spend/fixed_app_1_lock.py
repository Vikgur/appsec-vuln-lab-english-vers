from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

accounts = {
    "alice": {"balance": 100}
}

lock = threading.Lock()

@app.route("/withdraw", methods=["POST"])
def withdraw():
    username = request.json.get("user")
    amount = int(request.json.get("amount"))

    with lock:  # Fixed: атомарная секция
        account = accounts.get(username)

        if not account:
            return "Not found", 404

        if account["balance"] < amount:
            return "Insufficient funds", 400

        account["balance"] -= amount

        return jsonify({"balance": account["balance"]})

if __name__ == "__main__":
    app.run(threaded=True)