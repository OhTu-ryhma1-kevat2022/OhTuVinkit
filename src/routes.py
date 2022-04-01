from app import app
from repositories import users

from flask import (Flask, render_template, request)


@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username,password):
        return render_template("welcome.html")
    else:
        return render_template("index.html")

@app.route("/logout")
def logout():

    users.logout()
    return render_template("welcome.html")


@app.route("/register")
def new_user():
    return render_template("register.html")

@app.route("/create-user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password = request.form["password"]
    password2 = request.form["password2"]

    if users.register(username,password):
        return render_template("welcome.html")
    else:
        return render_template("index.html")



