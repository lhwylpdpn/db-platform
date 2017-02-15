# This Python file uses the following encoding: utf-8
from flask import render_template, request, json
from flask import Blueprint
from app.controler.power_API import power_list
from app.db.dbUser import DBUser


authBp = Blueprint('auth', __name__, url_prefix="/auth")


@authBp.route('/dataAuth')
def dataAuth():
    # userlistt = json.loads(power_list(""), encoding="utf-8")  # 字符串传化为json 对象
    # userlistt = tuple(userlistt["body"])  # 将json对象的body转化为列表(转化为列表只会保留key)
    # print(userlistt)
    userlist = DBUser.userLists()
    print( userlist )
    return render_template("authority/dataAuth.html", userlist=userlist)


@authBp.route('/menuAuth')
def menuAuth():
    return render_template("authority/menuAuth.html")
