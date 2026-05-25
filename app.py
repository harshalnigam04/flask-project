from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Data served by the /api route (loaded from data.json)
import json, os

def load_data():
    path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(path) as f:
        return json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api")
def api():
    return jsonify(load_data())

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
