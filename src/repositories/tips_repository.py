from db import db
from flask import session


class TipsRepository:

    def get_list(self):
        sql = "SELECT id, tittle, link, created, user_id FROM tips"
        result = db.session.execute(sql)
        return result.fetchall()

    def get_by_title(self, tittle):

        try:
            sql = "SELECT tittle, link FROM tips WHERE tittle like '(:tittle)'"
            result = db.session.execute(sql, {"tittle": tittle})
        except:
            raise Exception(f"Couldn't fetch from database")

        return result.fetchall()

    def add(self, tittle, link):

        user_id = session.get("user_id", 0)
        if user_id == 0:
            return False
        try:

            sql = "INSERT INTO tips (user_id, tittle,link, created) VALUES (:user_id, :tittle, :link, NOW())"
            db.session.execute(
                sql, {"user_id": user_id, "tittle": tittle, "link": link})
            db.session.commit()
            return True
        except:
            raise Exception(f"Couldn't add your new tip")

    def delete_by_id(self,id):
        user_id = session.get("user_id", 0)
        if user_id == 0:
            return False
        try:
            sql = "DELETE FROM tips WHERE id =:id AND user_id =:user_id"
            db.session.execute(sql, {"id":id, "user_id":user_id})
            db.session.commit()
            return True
        except:
            raise Exception(f"Couldn't delete tip")


tips_repository = TipsRepository()
