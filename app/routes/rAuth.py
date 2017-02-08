from flask import render_template,request
from flask import Blueprint


authBp = Blueprint('auth', __name__, url_prefix="/auth")


@authBp.route('/dataAuth')
def dataAuth():
    return render_template("authority/dataAuth.html")


@authBp.route('/menuAuth')
def menuAuth():
    return render_template("authority/menuAuth.html")
