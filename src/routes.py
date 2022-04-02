from app import app
from repositories import users
from services.user_service import user_service
from flask import (Flask, render_template, request, redirect, flash)


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
    confirm_password = request.form["password2"]

    try:
        user_service.create_user(username, password, confirm_password)
        return render_template("welcome.html")
    except Exception as error:
        flash(str(error))
        return redirect("/register")

@app.route("/new_book_tip")
def new_book_tip():
    return render_template("new_book_tip.html")




