from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/login")
def login():
    next_url = request.args.get("next")

    # УЯЗВИМОСТЬ: редирект на произвольный URL
    if next_url:
        return redirect(next_url)

    return "Login page"

if __name__ == "__main__":
    app.run(port=5000)