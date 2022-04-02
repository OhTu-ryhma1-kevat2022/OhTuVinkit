from app import app
from db import db
from config import DATABASE_URL

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL


def create_tables():
    db.session.execute("""
        CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT NOT NULL
        );
    """)

    db.session.execute("""
        CREATE TABLE tips (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users,
        tittle TEXT NOT NULL,
        link TEXT NOT NULL
        );
    """)



    db.session.commit()


def drop_tables():
    db.session.execute("""
        DROP TABLE IF EXISTS users CASCADE;
    """)

    db.session.execute("""
        DROP TABLE IF EXISTS tips;
    """)

    db.session.commit()


def initialize_database():
    drop_tables()
    create_tables()


if __name__ == "__main__":
    initialize_database()