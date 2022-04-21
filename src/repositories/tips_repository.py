from db import db
from repositories.user_repository import (
    user_repository as default_user_repository
)

class TipsRepository:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def get_list(self):
        user_id = self._user_repository.user_id()
        sql = "SELECT T.id, T.tittle, T.link, T.created, T.user_id, R.user_id FROM tips T LEFT JOIN readed R ON T.id = R.tip_id AND R.user_id =:user_id"
        result = db.session.execute(sql, {"user_id":user_id})
        return result.fetchall()

    def mark_readed(self,tip_id):
        user_id = self._user_repository.user_id()
        if user_id == 0:
            return False
        try:
            sql = """INSERT INTO readed (user_id, tip_id)
            VALUES (:user_id, :tip_id)"""
            db.session.execute(sql, {"user_id":user_id, "tip_id":tip_id})
            db.session.commit()
            return True
        except Exception as error:
            raise Exception("Couldn't mark tip readed") from error

    def get_by_title(self, tittle):
        try:
            sql = "SELECT tittle, link FROM tips WHERE tittle LIKE (:tittle)"
            result = db.session.execute(sql, {"tittle":tittle})
        except Exception as error:
            raise Exception("Couldn't fetch from database") from error

        return result.fetchall()

    def add(self, tittle, link):
        user_id = self._user_repository.user_id()
        if user_id == 0:
            return False
        try:
            sql = """INSERT INTO tips (user_id, tittle,link, created)
            VALUES (:user_id, :tittle, :link, NOW())"""
            db.session.execute(sql, {"user_id":user_id, "tittle":tittle, "link":link})
            db.session.commit()
            return True
        except Exception as error:
            raise Exception("Couldn't add your new tip") from error

    def delete_by_id(self, id_to_delete):
        user_id = self._user_repository.user_id()
        if user_id == 0:
            return False
        try:
            sql = "DELETE FROM tips WHERE id=:id AND user_id=:user_id"
            db.session.execute(sql, {"id":id_to_delete, "user_id":user_id})
            db.session.commit()
            return True
        except Exception as error:
            raise Exception("Couldn't delete tip") from error

    def delete_all(self):
        try:
            sql = "DELETE FROM tips"
            db.session.execute(sql)
            db.session.commit()
        except Exception:
            db.session.rollback()

tips_repository = TipsRepository()
