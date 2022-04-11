import unittest
from services.user_service import user_service, UserInputError, AuthenticationError

class TestUserService(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_if_no_username_is_provided_check_credentials_raises_exception(self):
        with self.assertRaises(UserInputError):
            user_service.check_credentials(None, "password1")

    def test_if_no_password_is_provided_check_credentials_raises_exception(self):
        with self.assertRaises(UserInputError):
            user_service.check_credentials("kalle", None)

    def test_if_no_username_or_password_is_provided_validate_raises_exception(self):
        with self.assertRaises(UserInputError):
            user_service.validate(None, "password", "password")

        with self.assertRaises(UserInputError):
            user_service.validate("user", None, "password")

    def test_if_password_and_password_confirmation_do_not_match_validate_raises_exception(self):
        with self.assertRaises(UserInputError):
            user_service.validate("new_user", "password", "not_the_same_password")