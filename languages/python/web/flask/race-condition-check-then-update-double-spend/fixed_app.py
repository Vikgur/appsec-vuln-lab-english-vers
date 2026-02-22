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

    # Fixed: атомарный UPDATE с условием
    cur.execute(
        """
        UPDATE users
        SET balance = balance - ?
        WHERE id = ?
        AND balance >= ?
        """,
        (amount, user_id, amount)
    )

    if cur.rowcount == 0:
        return "Insufficient funds", 400

    conn.commit()

    return jsonify({"status": "ok"})