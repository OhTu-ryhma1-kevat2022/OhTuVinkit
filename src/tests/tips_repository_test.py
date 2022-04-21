import unittest
from unittest.mock import Mock
from repositories.tips_repository import TipsRepository
from repositories.user_repository import UserRepository

class TestTipsRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository_mock = Mock()
        self.user_repository_mock.user_id.return_value = None
        self.tips_repository = TipsRepository(self.user_repository_mock)

        self.tips_repository.delete_all()

    def test_get_list_returns_correct_number_of_tips(self):
        self.tips_repository.add("This is a title", "https://testlink.com")
        all_tips = self.tips_repository.get_list()

        self.assertEqual(len(all_tips), 1)