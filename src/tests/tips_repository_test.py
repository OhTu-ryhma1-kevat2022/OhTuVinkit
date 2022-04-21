import unittest
from unittest.mock import Mock
from repositories.tips_repository import TipsRepository
from repositories.user_repository import UserRepository, db

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

    def test_delete_by_id_method_deletes_the_created_tip(self):
        self.tips_repository.add("Test title", "https://testlink.com/mock")
        added_tip = self.tips_repository.get_list()[0]
        id_to_delete = added_tip.id

        self.assertTrue(self.tips_repository.delete_by_id(id_to_delete))

    def test_marking_a_tip_as_read_adds_a_line_into_read_table(self):
        self.assertTrue(self.tips_repository.mark_readed(None))

    def test_marking_a_tip_as_read_with_invalid_id_raises_exception(self):
        with self.assertRaises(Exception):
            self.tips_repository.mark_readed("invalid id")