from flask import render_template, request, redirect, flash, session, current_app as app
from services.tips_service import tips_service
from services.user_service import user_service

@app.route("/")
def home_page():
    all_tips = tips_service.get_all_tips()
    if user_service.logged_in():
        return redirect("/welcome")
    return render_template("index.html", count=len(all_tips), tips=all_tips)

@app.route("/welcome")
def welcome():
    all_tips = tips_service.get_all_tips()
    return render_template("welcome.html", count=len(all_tips), tips=all_tips)

@app.route("/login", methods=["POST"])
def login():
    all_tips = tips_service.get_all_tips()
    username = request.form["username"]
    password = request.form["password"]
    try:
        user_service.login(username,password)
        return redirect("/welcome")
    except Exception as error:
        flash(str(error))
        return render_template("index.html", count=len(all_tips), tips=all_tips, entered_username=username, entered_pass=password)

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
        return render_template("register.html", entered_user=username, entered_pass=password)

@app.route("/new_book_tip")
def new_book_tip():
    return render_template("new_book_tip.html")

@app.route("/new_tip",methods=["POST"])
def new_tip():
    tittle = request.form["title"]
    link = request.form["link"]
    try:
        tips_service.add_new_tip(tittle,link)
        return redirect("/welcome")
    except Exception as error:
        flash(str(error))
        return render_template("new_book_tip.html", entered_title=tittle, entered_link=link)

@app.route("/delete_tip/<int:tip_id>")
def delete_tip(tip_id):
    try:
        tips_service.delete_tip(tip_id)
        return redirect("/welcome")
    except Exception as error:
        flash(str(error))
        return redirect("/welcome")

@app.route("/mark_tip_readed/<int:tip_id>")
def mark_tip_readed(tip_id):
    try:
        tips_service.mark_readed(tip_id)
        return redirect("/welcome")
    except Exception as error:
        flash(str(error))
        return redirect("/welcome")

@app.route("/togle_readed")
def togle_readed():
    try:
        if session["show_readed"]:
            session["show_readed"] = False
        else:
            session["show_readed"] = True
        return redirect("/welcome")
    except Exception as error:
        flash(str(error))
        return redirect("/welcome")

# sovelluksen tilan alustaminen testej?? varten
@app.route("/tests/reset", methods=["POST"])
def reset_tests():
    user_service.delete_all_users()
    tips_service.delete_all_tips()
    return "Reset"

@app.route("/ping")
def ping():
    return ""
