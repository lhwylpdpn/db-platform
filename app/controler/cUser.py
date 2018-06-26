from app.db.dbUser import DBUser


class CUser:
    @staticmethod
    def usercheck(username, password):
        result = DBUser().userCheck(username, password)
        if len(result) == 1:
            return True
        else:
            return False

    @staticmethod
    def userinfos(self):
        userInfos = DBUser().userLists()
        return userInfos


