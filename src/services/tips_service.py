from repositories.tips_repository import (
    tips_repository as default_tips_repository
)

class TipsService:
    def __init__(self, tips_repository=default_tips_repository):
        self._tips_repository = tips_repository

    def get_all_tips(self):
        return self._tips_repository.get_list()

    def add_new_tip(self, title, link):
        if not title or not link:
            raise Exception("Title and link are required!")

        return self._tips_repository.add(title, link)
    def delete_tip(self, id_to_delete):
        if not id_to_delete:
            raise Exception("Title and link are required!")

        return self._tips_repository.delete_by_id(id_to_delete)

    def mark_readed(self, id_to_mark_readed):
        if not id_to_mark_readed:
            raise Exception("Title and link are required!")

        return self._tips_repository.mark_readed(id_to_mark_readed)

    def delete_all_tips(self):
        self._tips_repository.delete_all()


tips_service = TipsService()
