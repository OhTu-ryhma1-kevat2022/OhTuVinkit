"""
import unittest
from unittest.mock import Mock, ANY
from services.user_service import UserService, UserInputError, AuthenticationError
from entities.user import User

class TestUserService(unittest.TestCase):
    def setUp(self):
        usernames = ("hamid", "joonas", "jorma", "miia", "rasmus", "veera")
        self.users = [User(username, "password1") for username in usernames]
        
        def find_by_username(username):
            for user in self.users:
                if user.username == username:
                    return user
            return None

        self.user_repository_mock = Mock()
        self.user_repository_mock.find_by_username = find_by_username

        self.service = UserService(user_repository=self.user_repository_mock)

    def test_if_no_username_is_provided_check_credentials_raises_exception(self):
        with self.assertRaises(UserInputError):
            self.service.check_credentials(None, "password1")

    def test_if_no_password_is_provided_check_credentials_raises_exception(self):
        with self.assertRaises(UserInputError):
            self.service.check_credentials("kalle", None)

    def test_with_wrong_password_check_credentials_raises_exception(self):
        with self.assertRaises(AuthenticationError):
            self.service.check_credentials("joonas", "wrongword")
"""
