# This Python file uses the following encoding: utf-8
from flask import render_template, request, json
from flask import Blueprint
from app.controler.power_API import power_list, power_list_update
from app.db.dbUser import DBUser


authBp = Blueprint('auth', __name__, url_prefix="/auth")


@authBp.route('/dataAuth')
def dataAuth():
    # userlist = json.loads(power_list(""), encoding="utf-8")  # 字符串传化为json 对象
    # userlist = tuple(userlist["body"])  # 将json对象的body转化为列表(转化为列表只会保留key)
    # print(userlist)
    userlist = DBUser.userLists()

    return render_template("authority/dataAuth.html", userlist=userlist)


@authBp.route('/dataAuth/<username>')
def dataAuthU(username):

    # 获取全部用户列表
    userlist = list(DBUser.userLists())
    # 获取选中用户的权限
    powerlist = json.loads(power_list([username]), encoding="utf-8")  # 字符串传化为json 对象

    if powerlist["body"]:
        powerlist = powerlist["body"][username].split(",")  # 将json对象的body username 进行split


        newuserlist = []
        for i in range(len(userlist)):
            newuserlist.append([userlist[i][0]])
            for j in range(len(powerlist)):
                if userlist[i][0] == powerlist[j]:
                    newuserlist[i].append("selected")


        return render_template("authority/dataAuth.html", selectedUser=username, userlist=newuserlist)
    else:
        return render_template("authority/dataAuth.html", selectedUser=username, userlist=userlist)


@authBp.route('/updateDataAuth')
def updateDataAuth():
    username = request.args.get('username')
    userlist = request.args.get('userlist')
    if userlist :
        newuserlist = userlist.split(",")
        newuserlist.append(username)  # 系统设计需要把自己加到权限列表里
    else:
        newuserlist = [username]

    result = power_list_update([username], [newuserlist])
    return result


@authBp.route('/menuAuth')
def menuAuth():
    return render_template("authority/menuAuth.html")
