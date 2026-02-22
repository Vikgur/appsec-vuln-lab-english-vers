from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# имитация БД
accounts = {
    "alice": {"balance": 100}
}

@app.route("/withdraw", methods=["POST"])
def withdraw():
    username = request.json.get("user")
    amount = int(request.json.get("amount"))

    account = accounts.get(username)

    if not account:
        return "Not found", 404

    # ❌ CHECK
    if account["balance"] < amount:
        return "Insufficient funds", 400

    # искусственная задержка (усиливает race)
    time.sleep(1)

    # ❌ USE
    account["balance"] -= amount

    return jsonify({"balance": account["balance"]})

if __name__ == "__main__":
    app.run(threaded=True)