from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from db import db

class UserRepository:
    def find_all(self):
        sql = "SELECT id, username FROM users"
        result = db.session.execute(sql)
        users = result.fetchall()
        return users

    def find_by_username(self, username):
        sql = "SELECT password, id, username FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        return user

    def delete_all(self):
        try:
            sql = "DELETE FROM users"
            db.session.execute(sql)
            db.session.commit()
        except Exception:
            db.session.rollback()

    def login(self, username, password):
        user = self.find_by_username(username)
        if not user:
            raise Exception(
                f"User with username {username} does not exist"
                )
        if not check_password_hash(user.password, password):
            raise Exception(
                "Incorrect username or password"
            )
        session["user_id"] = user.id
        session["username"] = username
        session["logged_in"] = True
        session["has_visited"] = True
        session["show_readed"] = False


    def logout(self):
        del session["user_id"]
        session['logged_in'] = False


    def register(self, username, password):
        hash_value = generate_password_hash(password)
        try:
            sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
            db.session.execute(sql, {"username":username,"password":hash_value})
            db.session.commit()
        except Exception as error:
            raise Exception(
                f"User with username {username} already exists"
            ) from error

    def logged_in(self):
        return session.get('logged_in', False)




user_repository = UserRepository()
