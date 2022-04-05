from db import db
from flask import session


class TipsRepository:

    def get_list(self):
        sql = "SELECT tittle, link FROM tips"
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
        sql = "INSERT INTO tips (user_id, tittle,link) VALUES (:user_id, :tittle, :link)"
        db.session.execute(
            sql, {"user_id": user_id, "tittle": tittle, "link": link})
        db.session.commit()
        return True


tips_repository = TipsRepository()
