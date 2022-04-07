from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session

class UserRepository:
    def __init__(self):
        self._users = []

    def find_all(self):
        sql = "SELECT id, username FROM users"
        result = db.session.execute(sql)
        users = result.fetchall()
        return users

    def find_by_username(self, username):
        users = self.find_all()
        user_to_find = None
        for user in users:
            if user.username == username:
                user_to_find = user
        return user_to_find

    def create(self, username, password):
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username,"password":password})
        db.session.commit()

    def delete_all(self):
        sql = "DELETE FROM users"
        db.session.execute(sql)
        db.session.commit()

    def login(self, username, password):

        sql = "SELECT password, id FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        if user == None:
            raise Exception(
                f"User with username {username} does not exist"
            )
        else:
            if check_password_hash(user[0],password):

                session['user_id'] = user.id
                session['username'] = username
                session['logged_in'] = True
            else:
                raise Exception(
                    f"Incorrect username or password"
                )

    def logout(self):
        del session["user_id"]
        session['logged_in'] = False


    def register(self, username, password):
        hash_value = generate_password_hash(password)
        try:
            sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
            db.session.execute(sql, {"username":username,"password":hash_value})
            db.session.commit()
        except:
            raise Exception(
                f"User with username {username} already exists"
            )
        self.login(username, password)

    def logged_in(self):
        return session.get('logged_in', False)


user_repository = UserRepository()
