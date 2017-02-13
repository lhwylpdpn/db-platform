from flask import render_template, request, Blueprint, session, redirect, url_for
from app.controler.cUser import CUser
from app.controler.power_API import login_in, login_in_M

userBp = Blueprint('user', __name__, url_prefix="/user")


@userBp.route('/login')
def login():
    return render_template("user/login.html")


@userBp.route('/loginaction')
def loginaction():
    username = request.args.get('username')
    password = request.args.get('password')
    loginresult = login_in_M(username, password)
    return loginresult


@userBp.route('/loginout')
def loginout():
    session.pop('username', None)
    return redirect(url_for('index', title='Good Bye'))


@userBp.route('/userlist')
def userlist():
    userinfos = CUser().userinfos()
    size = len(userinfos)
    return render_template('user/userlist.html', size=size, userinfos=userinfos)
