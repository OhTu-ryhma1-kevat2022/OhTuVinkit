from flask import (Flask, render_template, request)

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/register")
def new_user():
    return render_template("register.html")

@app.route("/create-user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password = request.form["password"]
    password2 = request.form["password2"]
    # check validity here
    pass