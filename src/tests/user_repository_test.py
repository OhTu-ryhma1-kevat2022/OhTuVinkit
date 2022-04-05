import unittest
from repositories.user_repository import UserRepository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        usernames = ("hamid", "joonas", "jorma", "miia", "rasmus", "veera")
        self.users = [User(username, "password1") for username in usernames]
        
        self.repository = UserRepository()
        for user in self.users:
            self.repository.create(user)

    def test_find_all_returns_all_users_in_repository(self):
        self.assertListEqual(self.repository.find_all(), self.users)

    def test_find_by_username_returns_correct_user(self):
        self.assertEqual(self.repository.find_by_username("joonas").username, "joonas")

    def test_if_username_exists_create_user_raises_exception_and_user_is_not_created(self):
        with self.assertRaises(Exception):
            self.repository.create(User("joonas", "password1"))
        self.assertListEqual(self.repository.find_all(), self.users)

    def test_if_username_is_available_new_user_is_created_and_returned(self):
        new_user = User("kalle", "password1")
        created_user = self.repository.create(new_user)

        self.assertEqual(self.repository.find_by_username("kalle").username, "kalle")
        self.assertEqual(created_user.username, new_user.username)

    """def test_no_users_remain_after_delete_all_method_is_called(self):
        users = self.repository.find_all()
        self.assertGreater(len(users), 0)

        self.repository.delete_all()

        users = self.repository.find_all()
        self.assertEqual(len(users), 0)"""
