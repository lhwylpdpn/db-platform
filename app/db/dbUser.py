"""
    AUTHOR : zhipeng.wang@corp.elong.com
    DATE : 20160920

"""
from Config import Config
from app.db.dbBase import DBConnect


class DBUser():
    @staticmethod
    def userLists():
        conn = DBConnect().db_connect(Config.DATABASE_MAIN)

        cursor = conn.cursor()
        cursor.execute("SELECT `username` FROM user_info")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
