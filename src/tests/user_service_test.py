import unittest
from unittest.mock import Mock
from services.user_service import UserService, UserInputError, AuthenticationError

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_repository_mock = Mock()
        self.user_service = UserService(self.user_repository_mock)
    
    def test_if_no_username_is_provided_check_credentials_raises_exception(self):
        with self.assertRaises(UserInputError):
            self.user_service.check_credentials(None, "password1")

    def test_if_no_password_is_provided_check_credentials_raises_exception(self):
        with self.assertRaises(UserInputError):
            self.user_service.check_credentials("kalle", None)

    def test_if_username_and_password_is_provided_check_credentials_returns_none(self):
        self.assertIsNone(self.user_service.check_credentials("kalle", "password1"))

    def test_login_calls_repository_login_with_username_and_password(self):
        username = "kalle"
        password = "password1"
        self.user_service.login(username, password)

        self.user_repository_mock.login.assert_called_with(username, password)

    def test_logout_calls_repository_logout_once(self):
        self.user_service.logout()

        self.user_repository_mock.logout.assert_called_once()

    def test_create_user_calls_repository_register_with_username_and_password(self):
        username = "kalle"
        password = "password1"
        confirmation = password
        self.user_service.create_user(username, password, confirmation)

        self.user_repository_mock.register.assert_called_with(username, password)

    def test_if_no_username_or_password_is_provided_validate_raises_exception(self):
        with self.assertRaises(UserInputError):
            self.user_service.validate(None, "password", "password")

        with self.assertRaises(UserInputError):
            self.user_service.validate("user", None, "password")

    def test_if_password_and_password_confirmation_do_not_match_validate_raises_exception(self):
        with self.assertRaises(UserInputError):
            self.user_service.validate("new_user", "password", "not_the_same_password")

    def test_delete_all_users_calls_repository_delete_all_once(self):
        self.user_service.delete_all_users()

        self.user_repository_mock.delete_all.assert_called_once()
