# Кейc: `race-condition-check-then-use-double-spend`

**Уязвимый код:**  

- Отдельная проверка баланса (`if balance < amount`) и последующее списание (`balance -= amount`) после задержки.  
- В многопоточном/многопроцессном окружении два запроса могут пройти проверку одновременно → **double spend / race condition**.  

**Вариант 1 — `threading.Lock`:**  

- Оборачивает проверку и списание в атомарную секцию `with lock`.  
- Гарантирует, что только один поток одновременно изменяет баланс.  
- Работает на уровне приложения в памяти.  

**Вариант 2 — атомарный SQL (SQLAlchemy):**  

- Списывает баланс напрямую через атомарный SQL `UPDATE ... WHERE balance >= amount`.  
- Проверяет `rowcount`, чтобы убедиться, что операция прошла.  
- Устраняет race condition на уровне базы, безопасно при нескольких инстансах приложения.  

**Итого:**  

- Первый фикс защищает на уровне памяти одного процесса.  
- Второй фикс продовый, безопасен для продакшена с многопоточными и распределёнными системами.

---

0. Кратко что это

Race Condition / TOCTOU (Time Of Check To Time Of Use):

Сценарий:

Проверяем условие (баланс ≥ сумма)

Потом используем ресурс (списываем)

Между check и use проходит время.
Если два запроса приходят параллельно — оба проходят проверку.

Итог: двойное списание, negative balance.

CWE-367.

1. Уязвимый код (Flask)

app.py

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

Что делает код:

проверяет баланс

ждёт

списывает деньги

Нет атомарности.

2. Где уязвимость и почему

Критичный участок:

if account["balance"] < amount:
    ...
time.sleep(1)
account["balance"] -= amount

Это classic check-then-act.

Если два запроса одновременно:

оба видят balance = 100

оба проходят check

оба списывают по 100

Итог: -100.

3. Минимальный exploit

Параллельно отправить два запроса:

POST /withdraw
{
  "user": "alice",
  "amount": 100
}

Оба выполнятся.

Итоговый баланс:

-100

В реальности:

использовать multithread

или burp intruder parallel

или ab / wrk

4. Исправленный код (с # Fixed)

Вариант 1 — lock.

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

Продовый вариант (правильный):

атомарный SQL:

UPDATE accounts
SET balance = balance - 100
WHERE username = 'alice'
AND balance >= 100;

и проверять affected rows.

Это устраняет TOCTOU полностью.

5. Принцип защиты

Делать операции атомарными.

Не разделять check и use.

Использовать:

DB transactions

row-level locks

optimistic locking (version field)

atomic update

Никогда не полагаться на in-memory state в multi-thread среде.

Core idea:

Security check и действие должны быть неразделимы.

6. Input / Trust Boundary / Security Boundary

Input:
request.json (amount)

Trust boundary:
Client → Backend

Security boundary:
Balance integrity

Атака:

concurrent requests → bypass balance check → double spending

7. Как искать глазами в code review

Ищи паттерн:

if condition:
    ...
do_action()

Особенно:

баланс

лимиты

quota

file existence check

permission check перед file open

Red flags:

if exists():
    open()
if balance >= x:
    balance -= x

Вопрос:

Что произойдёт, если два запроса придут одновременно?

8. Продовое Semgrep правило

TOCTOU сложно ловить статикой. Это heuristic rule.