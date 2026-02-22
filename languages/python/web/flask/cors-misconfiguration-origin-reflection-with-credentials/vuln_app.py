from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    origin = request.headers.get("Origin")

    # ❌ динамическое отражение Origin
    response.headers["Access-Control-Allow-Origin"] = origin
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"

    return response

@app.route("/api/profile")
def profile():
    return jsonify({
        "email": "user@example.com",
        "role": "admin"
    })

if __name__ == "__main__":
    app.run()