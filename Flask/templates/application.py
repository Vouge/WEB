from flask import Flask, render_template
from app import routes
app = Flask(__name__, template_folder='../templates')

@app.route("/")
def index():
    return render_template("index.html")
