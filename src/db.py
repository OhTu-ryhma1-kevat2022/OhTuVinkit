from app import app
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///user" # userin tilalle oma
db = SQLAlchemy(app)


