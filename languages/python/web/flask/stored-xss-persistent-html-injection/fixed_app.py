from flask import Flask, request, render_template_string, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["appdb"]
comments = db["comments"]

@app.route("/comment", methods=["POST"])
def add_comment():
    text = request.form.get("text")
    if not text:
        return "Text required", 400

    comments.insert_one({"text": text})
    return redirect("/comments")

@app.route("/comments")
def list_comments():
    all_comments = list(comments.find())

    # Fixed: используем шаблон с autoescaping
    template = """
    <h1>Comments</h1>
    {% for c in comments %}
        <div>{{ c.text }}</div>
    {% endfor %}
    """

    return render_template_string(template, comments=all_comments)

if __name__ == "__main__":
    app.run(port=5000)