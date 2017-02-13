# This Python file uses the following encoding: utf-8

from flask import Flask, url_for, redirect, request
from flask import render_template
from Config import Config
import random

app = Flask(__name__)
app.secret_key = Config().SECRET_KEY

from app.routes.rUser import userBp
app.register_blueprint(userBp)

from app.routes.rAuth import authBp
app.register_blueprint(authBp)


@app.route('/')
def index():
    # return render_template("index.html", title=U"首页")
    return redirect(url_for('channelIos600'))


@app.route('/channelIos600')
def channelIos600():
    sjs = 0
    if len(request.args) != 0:
        sjs = random.random()
    return render_template("channelIos600.html", title=U"iOS-渠道-明细600", sjs=sjs)


@app.route('/channelIos850')
def channelIos850():
    return render_template("channelIos850.html", title=U"iOS-渠道-明细850", sjs=random.random())


@app.route('/channelIos1200')
def channelIos1200():
    return render_template("channelIos1200.html", title=U"iOS-渠道-明细1200", sjs=random.random())


@app.route('/iOSTotalRoi')
def iOSTotalRoi():
    return render_template("iOSTotalRoi.html", title=U"iOS-整体-ROI", sjs=random.random())


if __name__ == '__main__':
    # open debug model
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
