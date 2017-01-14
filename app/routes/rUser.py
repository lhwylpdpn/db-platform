from flask import render_template,request
from app.controler.cUser import CUser
from flask import Blueprint

userBp = Blueprint('user', __name__, url_prefix="/user")


@userBp.route('/userlist')
def userlist():
    userinfos = CUser().userinfos()
    size = len(userinfos)
    return render_template('user/userlist.html', size=size, userinfos=userinfos)
