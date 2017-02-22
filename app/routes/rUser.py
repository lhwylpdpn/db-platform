# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
from app.controler.cUser import CUser
from app.controler.power_API import login_in, passwd_update

userBp = Blueprint('user', __name__, url_prefix="/user")


@userBp.route('/login')
def login():
    return render_template("user/login.html")


@userBp.route('/loginaction')
def loginaction():
    username = request.args.get('username')
    password = request.args.get('password')
    loginresult = login_in(username, password)
    return loginresult


@userBp.route('/loginout')
def loginout():
    session.pop('username', None)
    session.pop('zhanshi', None)
    return redirect(url_for('index', title='Good Bye'))


@userBp.route('/modifypassword')
def modifypassword():
    return render_template("user/modifyPassword.html")


@userBp.route('/modifypasswordaction')
def modifypasswordaction():
    oldpassword = request.args.get('oldpassword')
    checkResult = login_in(session['username'], oldpassword)  #先需要判断旧密码,用登录方法判断
    if int(json.loads(checkResult, encoding="utf-8")["status"]) >= 0:
        newpassword = request.args.get('newpassword')
        modifypasswordresult = passwd_update(session['username'], newpassword)  #判断通过调用修改密码接口
        return modifypasswordresult
    else:
        return U'{"status":"-1","body":"旧密码错误，请重新尝试。"}'


@userBp.route('/cancelMustModPass')
def cancelMustModPass():
    session['mustModPass'] = '2'
    return "1"


@userBp.route('/userlist')
def userlist():
    userinfos = CUser().userinfos()
    size = len(userinfos)
    return render_template('user/userList.html', size=size, userinfos=userinfos)
