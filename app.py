from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/rules")
def rules():
    return render_template("rules.html")

@app.route("/bots")
def bots():
    return render_template("bots.html")


if __name__ == "__main__":
    app.run(debug=True)