from flask import Flask, render_template

app = Flask(__name__, template_folder='../variable0')

@app.route("/")
def index():
    headline = "Hello, World!!!!"
    #return "Hello, world!"
    return render_template("index.html", headline=headline)
if __name__=="__main__":
    app.run(debug = True)
