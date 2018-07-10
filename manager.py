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



from app.controler.power_API import get_data_detail
from app.controler.power_API import clac



# @app.before_request
# # def before_request():
   
# #     if 'username' in session:
# #         menu_click_write(session["username"],request.path,time.strftime( '%Y-%m-%d %X', time.localtime(time.time())))

@app.route('/')
def index():
    return render_template("index.html", title=U"首页")


@app.route('/detail_json')
def data_detail_json():

    jsons = json.loads(get_data_detail("归属人测试名","2018-06-29"))  # 字符串传化为json 对象
    #print(jsons)
 
        
    return json.dumps(jsons["body"])


@app.route('/static_json')
def data_static_json():

    jsons = json.loads(get_business_json("data_static_json.json", session["username"]))  # 字符串传化为json 对象
    print(jsons)
    return json.dumps(jsons["body"])



@app.route('/detail')
def data_detail():
    sjs = 0
    if len(request.args) != 0:
        sjs = random.random()
    return render_template("data_detail.html", title=U"款项明细", sjs=sjs)


@app.route('/static')
def data_static():
    sjs = 0
    if len(request.args) != 0:
        sjs = random.random()
    return render_template("static_detail.html", title=U"汇总呈现", sjs=sjs)

@app.route('/clac_index')
def data_clac_index():
    return render_template("data_clac.html", title=U"数据计算", res="")


@app.route('/clac')
def data_clac():
    jsons=json.loads(clac())
   # print(json.dumps(jsons["status"]), json.dumps(jsons["status"])==0)
    if json.dumps(jsons["status"])=="0":

        return render_template("data_clac.html", title=U"数据计算", time=json.dumps(jsons["body"]).decode('unicode_escape'),res=1)
    else:
        return render_template("data_clac.html", title=U"数据计算", time=json.dumps(jsons["body"]).decode('unicode_escape'),res=-1)

@app.route('/expecting')
def expecting():
    return render_template("expecting.html", title=U"敬请期待")


 



if __name__ == '__main__':
    # open debug model
    app.debug = True
    app.run(host='0.0.0.0', port=4900)
