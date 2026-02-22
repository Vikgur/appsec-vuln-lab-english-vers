0. Кратко что это

Race Condition / TOCTOU (Time Of Check To Time Of Use):

сначала проверяем условие

потом выполняем действие

между ними состояние может измениться

Итог:

двойное списание

обход лимитов

нарушение инвариантов

CWE-367.

1. Уязвимый код (Flask + SQLite)

app.py

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

Что делает код:

проверяет баланс

если хватает — списывает

операции разделены

2. Где уязвимость и почему

Критический участок:

SELECT balance
if balance >= amount:
    UPDATE balance = balance - amount

Это классический check-then-use.

Если два запроса приходят одновременно:

Оба читают баланс = 100

Оба проходят проверку

Оба списывают 100

Баланс становится -100

Нет атомарности.

3. Минимальный exploit

Баланс: 100
Отправляем 2 параллельных запроса:

curl -X POST /transfer -d '{"user_id":1,"amount":100}' &
curl -X POST /transfer -d '{"user_id":1,"amount":100}' &

Оба проходят check.
Двойное списание.

В реальности — через Burp Intruder или параллельные потоки.

4. Исправленный код (с # Fixed)

Правильный подход — атомарная операция.

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

Теперь:

UPDATE выполнится только если баланс достаточен

операция атомарна на уровне БД

Продовый уровень:

транзакции с SERIALIZABLE isolation

row-level locking (SELECT ... FOR UPDATE)

optimistic locking (version field)

5. Принцип защиты

Никогда не разделять check и state change.

Делать атомарные операции.

Использовать транзакции.

Блокировки или versioning.

Думать в терминах инвариантов.

Core idea:

Security инвариант должен проверяться и применяться в одной операции.

6. Input / Trust Boundary / Security Boundary

Input:
amount из request.json

Trust boundary:
Client → Backend

Security boundary:
Application → Database consistency

Атака:

concurrent requests → bypass business rule → финансовая потеря

Это логическая уязвимость, не injection.

7. Как искать глазами в code review

Ищи паттерн:

SELECT ...
if condition:
    UPDATE ...

Особенно в:

платежах

лимитах

купонах

голосованиях

инвентаре

Красные флаги:

два отдельных запроса

нет транзакции

нет row lock

нет optimistic lock

Вопрос:

Что произойдёт, если 100 запросов придут одновременно?

8. Продовое Semgrep правило

(Точный матчинг SQL строк ограничен, но паттерн check→update ловится.)
