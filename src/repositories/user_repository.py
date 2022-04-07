from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session

class UserRepository:
    def find_all(self):
        sql = "SELECT id, username FROM users"
        result = db.session.execute(sql)
        users = result.fetchall()
        return users

    def find_by_username(self, username):
        sql = "SELECT password, id FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        return user

    def delete_all(self):
        sql = "DELETE FROM users"
        db.session.execute(sql)
        db.session.commit()

    def login(self, username, password):
        user = self.find_by_username(username)
        if not user:
            raise Exception(
                f"User with username {username} does not exist"
            )
        if not check_password_hash(user.password, password):
            raise Exception(
                f"Incorrect username or password"
            )
        session["user_id"] = user.id
        session["username"] = username
        session["logged_in"] = True


    def logout(self):
        del session["user_id"]
        session['logged_in'] = False


    def register(self, username, password):
        hash_value = generate_password_hash(password)
        try:
            sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
            db.session.execute(sql, {"username":username,"password":hash_value})
            db.session.commit()
        except:
            raise Exception(
                f"User with username {username} already exists"
            )

    def logged_in(self):
        return session.get('logged_in', False)


user_repository = UserRepository()
