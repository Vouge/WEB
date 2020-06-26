import datetime

from flask import Flask, render_template

app = Flask(__name__, template_folder='../conditions')



@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    new_year = False
    return render_template("index.html", new_year = new_year)


if __name__=="__main__":
    app.run(debug=True)
