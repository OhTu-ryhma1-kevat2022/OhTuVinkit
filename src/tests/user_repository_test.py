import unittest
from repositories.user_repository import UserRepository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        usernames = ("hamid", "joonas", "jorma", "miia", "rasmus", "veera")
        self.users = [User(username, "password1") for username in usernames]
        
        self.repository = UserRepository()
        for user in self.users:
            self.repository.create_user(user)

    def test_find_all_method_returns_all_users_in_repository(self):
        self.assertListEqual(self.repository.find_all(), self.users)

    def test_find_by_username_method_returns_correct_user(self):
        self.assertEqual(self.repository.find_by_username("joonas").username, "joonas")
