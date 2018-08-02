# This Python file uses the following encoding: utf-8
#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8

from flask import Flask, url_for, redirect, request, json, session
from flask import render_template
from Config import Config
import random
import time
import chardet
app = Flask(__name__)
app.secret_key = Config().SECRET_KEY

from app.routes.rUser import userBp
app.register_blueprint(userBp)

from app.routes.rAuth import authBp
app.register_blueprint(authBp)
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')



from app.controler.power_API import get_data_class_name
from app.controler.power_API import get_data_detail
from app.controler.power_API import get_data_detail_heji
from app.controler.power_API import clac
from app.controler.power_API import clac_config
from app.controler.power_API import get_data_class_date
from app.controler.power_API import get_data_static
from app.controler.power_API import get_data_class_filename

# @app.before_request
# # def before_request():
   
# #     if 'username' in session:
# #         menu_click_write(session["username"],request.path,time.strftime( '%Y-%m-%d %X', time.localtime(time.time())))

@app.route('/')
def index():
    return render_template("index.html", title=U"首页")


@app.route('/detail_json')
def data_detail_json():
    date=request.args.get('date')
    person=request.args.get('person')
    filename=request.args.get('filename')
    #print(filename)
    jsons = json.loads(get_data_detail(person,date,filename))  # 字符串传化为json 对象
    #print(jsons)
 
        
    return json.dumps(jsons["body"])

@app.route('/detail_json_heji')
def data_detail_json_heji():
    date=request.args.get('date')
    person=request.args.get('person')
    
    #print(filename)
    jsons = json.loads(get_data_detail_heji(person,date))  # by lhwylp 临时加的合计功能
   # print(jsons)
 
        
    return json.dumps(jsons["body"])



@app.route('/static_json')
def data_static_json():
    date_start=request.args.get('date_start')
    date_end=request.args.get('date_end')
    person=request.args.get('person')
    filename=request.args.get('filename')
    all_=request.args.get('all_')
    #print(filename)
    jsons = json.loads(get_data_static(person,date_start,date_end,filename,all_))  # 字符串传化为json 对象
    #print(jsons)
 
        
    return json.dumps(jsons["body"])

# @app.route('/static_json')
# def data_static_json():

#     jsons = json.loads(get_business_json("data_static_json.json", session["username"]))  # 字符串传化为json 对象
#     print(jsons)
#     return json.dumps(jsons["body"])



@app.route('/detail')
def data_detail():
    sjs = 0
    class_name=[]
    if len(request.args) != 0:
        sjs = random.random()
    jsons=get_data_class_name()
    jsons=jsons.split(u",")
    dates=get_data_class_date()
    dates=dates.split(u",")



    return render_template("data_detail.html", title=U"款项明细", sjs=sjs, jsons_=jsons,dates_=dates)


@app.route('/static')
def data_static():
    sjs = 0
    class_name=[]
    if len(request.args) != 0:
        sjs = random.random()
    jsons=get_data_class_name()
    jsons=jsons.split(u",")
    dates=get_data_class_date()
    dates=dates.split(u",")
    files=get_data_class_filename()
    files=files.split(u",")
    return render_template("static_detail.html", title=U"汇总呈现", sjs=sjs,jsons_=jsons,dates_=dates,files_=files)

@app.route('/clac_index')
def data_clac_index():
    return render_template("data_clac.html", title=U"数据计算", res="")


@app.route('/clac_index_config')
def data_clac_index_config():
    return render_template("data_clac_config.html", title=U"数据计算", res="")


@app.route('/clac')
def data_clac():
    jsons=json.loads(clac())
   # print(json.dumps(jsons["status"]), json.dumps(jsons["status"])==0)
    if json.dumps(jsons["status"])=="0":

        return render_template("data_clac.html", title=U"数据计算", time=json.dumps(jsons["body"]).decode('unicode_escape'),res=1)
    else:
        return render_template("data_clac.html", title=U"数据计算", time=json.dumps(jsons["body"]).decode('unicode_escape'),res=-1)

@app.route('/clac_config')
def data_clac_config():
    jsons=json.loads(clac_config())
   # print(json.dumps(jsons["status"]), json.dumps(jsons["status"])==0)
    if json.dumps(jsons["status"])=="0":

        return render_template("data_clac_config.html", title=U"数据计算", time=json.dumps(jsons["body"]).decode('unicode_escape'),res=1)
    else:
        return render_template("data_clac_config.html", title=U"数据计算", time=json.dumps(jsons["body"]).decode('unicode_escape'),res=-1)


@app.route('/expecting')
def expecting():
    return render_template("expecting.html", title=U"敬请期待")


 



if __name__ == '__main__':
    # open debug model
    app.debug = True
    app.run(host='0.0.0.0', port=4900)
