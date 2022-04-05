from flask import Flask
from config import DATABASE_URL
from db import db
import routes
import os

def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.secret_key = os.getenv("SECRET_KEY")

    db.init_app(app)

    app.add_url_rule('/', view_func=routes.home_page)
    app.add_url_rule('/welcome', view_func=routes.welcome)
    app.add_url_rule('/login', view_func=routes.login, methods=["POST"])
    app.add_url_rule('/logout', view_func=routes.logout)
    app.add_url_rule('/register', view_func=routes.new_user)
    app.add_url_rule('/create-user', view_func=routes.create_user, methods=["POST"])
    app.add_url_rule('/new_book_tip', view_func=routes.new_book_tip)
    app.add_url_rule('/new_tip', view_func=routes.new_tip, methods=["POST"])
    app.add_url_rule('/tests/reset', view_func=routes.reset_tests, methods=["POST"])

    return app