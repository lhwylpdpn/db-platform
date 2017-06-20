"""
    AUTHOR : zhipeng.wang@corp.elong.com
    DATE : 20160920

"""
import sys
import pymysql


class DBConnect:
    @staticmethod
    def db_connect(DATABASE_URL):
        try:
            host = DATABASE_URL['host']
            port = DATABASE_URL['port']
            user = DATABASE_URL['user']
            password = DATABASE_URL['password']
            db = DATABASE_URL['dbName']
            charset = DATABASE_URL['charset']

            conn = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)
            return conn
        except Exception as e:
            print(e)
            sys.exit()
