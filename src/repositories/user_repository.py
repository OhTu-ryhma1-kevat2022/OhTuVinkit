from db import db

class UserRepository:
    def __init__(self):
        self._users = []


    def register(username,password):

        try:
            sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
            db.session.execute(sql, {"username":username,"password":password})
            db.session.commit()
        except:
            return False
        return

    def find_all(self):
        return self._users

    def find_by_username(self, username):
        users = self.find_all()
        user_to_find = None
        for user in users:
            if user.username == username:
                user_to_find = user
        return user_to_find

    def create_user(self, user):
        users = self.find_all()

        if self.find_by_username(user.username):
            raise Exception(
                f"User with username {user.username} already exists"
            )

        users.append(user)
        self._users = users

        return user




    def delete_user(self, user_id):
        users = self.find_all()
        self._users = [user for user in users if user.id != user_id]

    def delete_all(self):
        self._users = []

