from flask import session
from db import db

class TipsRepository:

    def get_list(self):
        sql = "SELECT id, tittle, link, created, user_id FROM tips"
        result = db.session.execute(sql)
        return result.fetchall()

    def get_by_title(self, tittle):

        try:
            sql = "SELECT tittle, link FROM tips WHERE tittle like '(:tittle)'"
            result = db.session.execute(sql, {"tittle": tittle})
        except Exception as error:
            raise Exception("Couldn't fetch from database") from error

        return result.fetchall()

    def add(self, tittle, link):

        user_id = session.get("user_id", 0)
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
        user_id = session.get("user_id", 0)
        if user_id == 0:
            return False
        try:
            sql = "DELETE FROM tips WHERE id =:id AND user_id =:user_id"
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
