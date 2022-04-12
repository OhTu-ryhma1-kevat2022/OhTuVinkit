import unittest
from unittest.mock import Mock
from services.tips_service import TipsService

class TestTipsService(unittest.TestCase):
    def setUp(self):
        self.tips_repository_mock = Mock()
        self.tips_service = TipsService(self.tips_repository_mock)

    def test_if_no_title_is_provided_add_new_tip_raises_exception(self):
        with self.assertRaises(Exception):
            self.tips_service.add_new_tip(None, "https://example.com/None")

    def test_if_no_link_is_provided_add_new_tip_raises_exception(self):
        with self.assertRaises(Exception):
            self.tips_service.add_new_tip("Just The Tip", None)

    def test_if_title_and_link_provided_add_new_tip_calls_method_add_with_title_and_link(self):
        title = "Test Tip"
        link = "https://example.com/Test"
        self.tips_service.add_new_tip(title, link)

        self.tips_repository_mock.add.assert_called_with(title, link)

    def test_id_not_provided_delete_tip_raises_exception(self):
        with self.assertRaises(Exception):
            self.tips_service.delete_tip(None)

    def test_if_id_is_provided_delete_tip_calls_delete_by_id_with_id(self):
        id_to_test = "testId123"
        self.tips_service.delete_tip(id_to_test)

        self.tips_repository_mock.delete_by_id.assert_called_with(id_to_test)
