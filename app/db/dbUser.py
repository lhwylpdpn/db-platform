"""
    AUTHOR : zhipeng.wang@corp.elong.com
    DATE : 20160920

"""
from Config import Config
from app.db.dbBase import DBConnect


class DBUser():
    @staticmethod
    def userCheck(username, password):
        conn = DBConnect().db_connect(Config().DATABASE_BUGFREE)
        cursor = conn.cursor()
        cursor.execute("SELECT `name` FROM `user` WHERE `name` = %s and `password` = %s", (username, password))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


    def userLists(self):
        userInfos = {
            'kye1': {'id': 1, 'name': 'wzp', 'info1': '12', 'info2': 'a'},
            'kye2': {'id': 2, 'name': 'order', 'info1': '23', 'info2': 'a'},
            'kye3': {'id': 3, 'name': 'nanxiao', 'info1': '43', 'info2': 'a'},
            'kye4': {'id': 4, 'name': 'guest', 'info1': '54', 'info2': 'a'},
            'kye5': {'id': 5, 'name': 'zengzhan', 'info1': '54', 'info2': 'a'}
        }
        return userInfos