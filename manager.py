# This Python file uses the following encoding: utf-8

from flask import Flask, url_for, redirect, request, json, session
from flask import render_template
from Config import Config
import random
import time
app = Flask(__name__)
app.secret_key = Config().SECRET_KEY

from app.routes.rUser import userBp
app.register_blueprint(userBp)

from app.routes.rAuth import authBp
app.register_blueprint(authBp)

from app.routes.rAnalyze import analyzeBp
app.register_blueprint(analyzeBp)


from app.routes.rMonitor import monitorBp
app.register_blueprint(monitorBp)


from app.controler.power_API import get_business_json


from app.controler.power_API import menu_click_write

@app.before_request
def before_request():
    print(session)
    if 'username' in session:
        menu_click_write(session["username"],request.path,time.strftime( '%Y-%m-%d %X', time.localtime(time.time())))

@app.route('/')
def index():
    # return render_template("index.html", title=U"首页")
    return redirect(url_for('expecting'))


@app.route('/channelIos600')
def channelIos600():
    sjs = 0
    if len(request.args) != 0:
        sjs = random.random()
    return render_template("channelIos600.html", title=U"iOS-渠道-明细", sjs=sjs)


@app.route('/channelIos600Json')
def channelIos600Json():
    jsons = json.loads(get_business_json("test.json", session["username"]))  # 字符串传化为json 对象
    return json.dumps(jsons["body"])


@app.route('/iOSTotalRoi')
def iOSTotalRoi():
    return render_template("iOSTotalRoi.html", title=U"iOS-整体-ROI", sjs=random.random())


@app.route('/expecting')
def expecting():
    return render_template("expecting.html", title=U"敬请期待")


@app.route('/widget')
def widget():
    return render_template("demoWidgets.html", title=U"面板")


if __name__ == '__main__':
    # open debug model
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
