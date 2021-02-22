from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("signup-form.html")


@app.route("/signup", methods=["POST"])
def save_signup():
    data = request.form
    return render_template("thank-you.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")
