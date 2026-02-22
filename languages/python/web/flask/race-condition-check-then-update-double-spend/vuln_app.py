from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("bank.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/transfer", methods=["POST"])
def transfer():
    user_id = request.json.get("user_id")
    amount = int(request.json.get("amount"))

    conn = get_db()
    cur = conn.cursor()

    # ❌ CHECK
    cur.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()

    if not row:
        return "User not found", 404

    if row["balance"] < amount:
        return "Insufficient funds", 400

    # ❌ USE (отдельный запрос)
    cur.execute(
        "UPDATE users SET balance = balance - ? WHERE id = ?",
        (amount, user_id)
    )
    conn.commit()

    return jsonify({"status": "ok"})