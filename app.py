from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
