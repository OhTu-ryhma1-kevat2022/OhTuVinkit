from services.tips_service import tips_service
from services.user_service import user_service
from flask import render_template, request, redirect, flash


def home_page():
    if user_service.logged_in():
        return redirect("/welcome")
    return render_template("index.html")

def welcome():
    list = tips_service.get_all_tips()
    return render_template("welcome.html", count=len(list), tips=list)

def login():
    username = request.form["username"]
    password = request.form["password"]
    try:
        user_service.login(username,password)
        return redirect("/welcome")
    except Exception as error:
        flash(str(error))
        return render_template("index.html")

def logout():
    user_service.logout()
    return redirect("/")


def new_user():
    return render_template("register.html")

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

def new_book_tip():
    return render_template("new_book_tip.html")

def new_tip():
    tittle = request.form["title"]
    link = request.form["link"]
    tips_service.add_new_tip(tittle,link)
    return welcome()

# sovelluksen tilan alustaminen testejä varten
def reset_tests():
    user_service.delete_all_users()
    return "Reset"
