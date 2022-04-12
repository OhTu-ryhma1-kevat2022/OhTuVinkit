import unittest
from repositories.tips_repository import tips_repository
from repositories.user_repository import user_repository
from flask import session
from initialize_database import app

class TestTipsRepository(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_list_returns_all_created_tips(self):
        with app.test_request_context():
            user_repository.register("test_user", "password")
            session["user_id"] = 1
            tips_repository.add("title", "testlink")
            tips = tips_repository.get_list()

            self.assertEqual(len(tips), 1)