from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/preview")
def preview():
    name = request.args.get("name", "")

    template = f"""
    <html>
        <body>
            <h1>Hello {name}</h1>
        </body>
    </html>
    """

    return render_template_string(template)

if __name__ == "__main__":
    app.run(port=5000)