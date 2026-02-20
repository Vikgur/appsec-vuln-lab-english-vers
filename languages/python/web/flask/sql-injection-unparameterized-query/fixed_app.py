from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

# Fixed
@app.route("/user")
def get_user():
    username = request.args.get("username")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, username, role FROM users WHERE username = ?",
        (username,)
    )

    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify(dict(row))
    return jsonify({"error": "not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)