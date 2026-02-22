from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q", "")

    # Fixed: используем шаблон с autoescaping
    template = """
    <html>
        <body>
            <h1>Search results for: {{ query }}</h1>
        </body>
    </html>
    """

    return render_template_string(template, query=query)

if __name__ == "__main__":
    app.run(port=5000)