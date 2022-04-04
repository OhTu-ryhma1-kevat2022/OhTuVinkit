from repositories.tips_repository import (
    tips_repository as default_tips_repository
)

class TipsService:
    def __init__(self, tips_repository=default_tips_repository):
        self._tips_repository = tips_repository

    def get_all_tips(self):
        return self._tips_repository.get_list()

    def add_new_tip(self, title, link):
        return self._tips_repository.add(title, link)

tips_service = TipsService()