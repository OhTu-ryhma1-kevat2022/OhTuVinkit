from db import db
from flask import session

def get_list():
    sql = "SELECT tittle, link FROM tips"
    result = db.session.execute(sql)
    return result.fetchall()

def add(tittle,link):

    user_id = session.get("user_id",0)
    if user_id == 0:
        return False
    sql = "INSERT INTO tips (user_id, tittle,link) VALUES (:user_id, :tittle, :link)"
    db.session.execute(sql, {"user_id":user_id, "tittle":tittle, "link":link})
    db.session.commit()
    return True