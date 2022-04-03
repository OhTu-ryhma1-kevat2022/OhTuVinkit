from app import app
from repositories.user_repository import user_repository
from services.tips_service import tips_service
from services.user_service import user_service
from flask import (render_template, request, redirect, flash)


@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/welcome")
def welcome():
    list = tips_service.get_all_tips()
    return render_template("welcome.html", count=len(list), tips=list)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if user_service.login(username,password):
        return redirect("/welcome")
    else:
        return render_template("index.html")

@app.route("/logout")
def logout():
    user_service.logout()
    return redirect("/")


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
        return welcome()
    except Exception as error:
        flash(str(error))
        return redirect("/register")

@app.route("/new_book_tip")
def new_book_tip():
    return render_template("new_book_tip.html")

@app.route("/new_tip",methods=["POST"])
def new_tip():
    tittle = request.form["title"]
    link = request.form["link"]
    tips_service.add_new_tip(tittle,link)
    return welcome()

# sovelluksen tilan alustaminen testejä varten
@app.route("/tests/reset", methods=["POST"])
def reset_tests():
    user_repository.delete_all()
    return "Reset"
