from app import app
from flask_sqlalchemy import SQLAlchemy


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///jovajova"
db = SQLAlchemy(app)


