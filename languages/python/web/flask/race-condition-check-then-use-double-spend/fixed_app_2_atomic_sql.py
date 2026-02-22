from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///accounts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Account(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    balance = db.Column(db.Integer, nullable=False)

@app.route("/withdraw", methods=["POST"])
def withdraw():
    amount = int(request.json.get("amount"))

    if amount <= 0:
        return jsonify({"error": "Amount must be positive"}), 400

    try:
        # Атомарный списание для alice
        result = db.session.execute(
            db.text("""
                UPDATE accounts
                SET balance = balance - :amount
                WHERE username = 'alice' AND balance >= :amount
            """),
            {"amount": amount}
        )

        if result.rowcount == 0:
            return jsonify({"error": "Insufficient funds"}), 400

        db.session.commit()

        account = db.session.get(Account, "alice")
        return jsonify({"balance": account.balance})

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(threaded=True)