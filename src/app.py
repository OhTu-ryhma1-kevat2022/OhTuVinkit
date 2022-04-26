from flask import Flask
from config import DATABASE_URL, SECRET_KEY, ENV
from db import db

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ENV'] = ENV

    db.init_app(app)

    app.app_context().push()

    import routes # pylint: disable=W0611,C0415

    return app
