from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

    def login(self, username, password):
        self.check_credentials(username, password)
        self._user_repository.login(username, password)

    def logout(self):
        self._user_repository.logout()

    def create_user(self, username, password, confirm_password):
        self.validate(username, password, confirm_password)
        self._user_repository.register(username, password)
        self._user_repository.login(username, password)

    def validate(self, username, password, confirm_password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        if password != confirm_password:
            raise UserInputError("Password do not match")

    def delete_all_users(self):
        self._user_repository.delete_all()

    def logged_in(self):
        return self._user_repository.logged_in()

user_service = UserService()