from flask import Flask, render_template, request

app = Flask(__name__, template_folder = 'templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET","POST"])
# This page can only be accessed after post.
def hello():
    if request.method == "GET":
        return "Please submit the form first."
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)
