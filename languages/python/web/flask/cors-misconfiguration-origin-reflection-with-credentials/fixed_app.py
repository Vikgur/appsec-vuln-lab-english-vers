from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Fixed: строгий whitelist
ALLOWED_ORIGINS = {
    "https://app.example.com",
    "https://admin.example.com"
}

@app.after_request
def add_cors_headers(response):
    origin = request.headers.get("Origin")

    if origin in ALLOWED_ORIGINS:
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