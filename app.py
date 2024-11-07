from flask import Flask, render_template
from flask_bootstrap import Bootstrap5 as B5

app = Flask(__name__)
bootstrap = B5(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mobs.com")
def mobs():
    return render_template("mobs.html")

if __name__ == "__main__":
    app.run(debug = True)