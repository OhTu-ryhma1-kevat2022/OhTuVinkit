import unittest
from repositories.user_repository import user_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()

    def test_after_registering_a_new_user_find_all_returns_one_user(self):
        user_repository.register("user", "password123")
        users = user_repository.find_all()
        username = users[0].username
        
        self.assertEqual(username, "user")
        self.assertEqual(len(users), 1)

    def test_find_by_username_returns_correct_user(self):
        user_repository.register("user", "password123")
        user_to_find = user_repository.find_by_username("user")

        self.assertEqual(user_to_find.username, "user")

    def test_if_username_exists_registering_user_raises_exception(self):
        user_repository.register("user", "password123")
        with self.assertRaises(Exception):
            user_repository.register("user", "password123")

    def test_if_username_does_not_exist_logging_in_raises_exception(self):
        with self.assertRaises(Exception):
            user_repository.login("non-existing_user", "password123")

    def test_if_incorrect_password_is_entered_logging_in_raises_exception(self):
        user_repository.register("user", "password123")
        with self.assertRaises(Exception):
            user_repository.login("user", "wrong_password")
"""
    def test_no_users_remain_after_delete_all_method_is_called(self):
        user_repository.register("user1", "password123")
        user_repository.register("user2", "password123")
        users = user_repository.find_all()
        self.assertGreater(len(users), 0)

        user_repository.delete_all()

        users = user_repository.find_all()
        self.assertEqual(len(users), 0)
"""