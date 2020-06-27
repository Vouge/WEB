from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/jack")
def david():
    return "Hello, Jack!"


@app.route("/<string:name>")
def hello(name):
    name1 = ""
    names = name.split(" ")
    for name in names:
        name1 += name.capitalize() + " "
    name1 = name1.strip()
    return f"Hello, {name1}!"
