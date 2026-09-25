from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/yes")
def yes():
    return "ایول! منم آموزش امروزمو تموم کردم 🎉 این اولین سایتمه!"


@app.route("/no")
def no():
    return render_template("no.html")


@app.route("/work")
def work():
    return render_template("answer.html")


@app.route("/hungry")
def hungry():
    return render_template("answer.html")


@app.route("/lazy")
def lazy():
    return render_template("answer.html")


@app.route("/cant")
def cant():
    return render_template("answer.html")


app.run(host="0.0.0.0", port=10000)
