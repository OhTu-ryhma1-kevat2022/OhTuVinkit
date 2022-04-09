from app import create_app
from db import db

app = create_app()

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
        link TEXT NOT NULL,
        created TIMESTAMP
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