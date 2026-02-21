from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route("/parse", methods=["POST"])
def parse_yaml():
    data = request.get_data(as_text=True)

    obj = yaml.load(data, Loader=yaml.Loader)

    return jsonify({"parsed": str(obj)})

if __name__ == "__main__":
    app.run(port=5000)