# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
import random
import re
import time
from app.controler.power_API import get_business_json
from app.controler.cMediaOverview import cMediaOverview
from app.controler.cNewTransfer import cNewTransfer
from app.controler.cMediaRetention import cMediaRetention
analyzeBp = Blueprint('analyze', __name__, url_prefix="/analyze")


# 媒体概览相关
@analyzeBp.route('/mediaOverview')
def mediaOverview():
    return render_template("putAnalyze/mediaAnalyze/mediaOverview.html", title=U"媒体概览", sjs=random.random())


@analyzeBp.route('/mediaOverviewJsonTJ')
def mediaOverviewJsonTJ():
    results = cMediaOverview.mediaOverviewTJ(session["username"])
    return results


@analyzeBp.route('/mediaOverviewJson')
def mediaOverviewJson():
    results = cMediaOverview.mediaOverviewJson(session["username"])
    return results


# 新增转化相关
@analyzeBp.route('/newTransfer')
def newTransfer():
    return render_template("putAnalyze/mediaAnalyze/newTransfer.html", title=U"新增转化", sjs=random.random())


@analyzeBp.route('/newTransferTJ')
def newTransferTJ():
    results = cNewTransfer.newTransferTJ(session["username"])
    tj = {"channel":[{"id":"17173", "text":"17173"},{"id":"点入", "text":"点入"}],"staff":[{"id":"172173", "text":"171373"},{"id":"点入", "text":"点入点入"}]}
    return json.dumps(tj)


@analyzeBp.route('/newTransferJson')
def newTransferJson():
    results = cNewTransfer.newTransferJson(session["username"])
    return results


#留存活跃相关
@analyzeBp.route('/mediaRetention')
def mediaRetention():
    return render_template("putAnalyze/mediaAnalyze/mediaRetention.html", title=U"留存活跃", sjs=random.random())


@analyzeBp.route('/mediaRetentionJson')
def mediaRetentionJson():
    args=request.args.items()
    jsons = json.loads(get_business_json("media_3.json", session["username"]))["body"]
    jsons = json.dumps(jsons)
    jsons = jsons.replace(" ","")
    resultjson=[]
    word=r'({[^}]*[^}]*})'
    jsons=",".join(re.findall(word,jsons))
    for x in xrange(0,len(args)):
        if args[x][0]=="date_" or args[x][0]=="channel_name" or args[x][0]=="game_id" or args[x][0]=="platform" or args[x][0]=="agent" or args[x][0]=="staff" :
            if args[x][1]!="":
                word=r'({[^}]*"'+args[x][0]+'":"'+args[x][1].replace(',','"[^}]+}|{[^}]+"'+args[x][0]+'":"')+'"[^}]*})'
                jsons=",".join(re.findall(word,jsons))
                print(4)
            else:
                word=r'({[^}]*[^}]*})'
                jsons=",".join(re.findall(word,jsons))
    jsons=jsons.replace('"re_0":""','"re_0":0')
    jsons=jsons.replace('"re_1":""','"re_1":0')
    jsons=jsons.replace('"re_2":""','"re_2":0')
    jsons=jsons.replace('"re_3":""','"re_3":0')
    jsons=jsons.replace('"re_4":""','"re_4":0')
    jsons=jsons.replace('"re_5":""','"re_5":0')
    jsons=jsons.replace('"re_6":""','"re_6":0')
    jsons=json.loads("["+jsons+"]")
    new_json=[]
    date_temp=[]
    print(5)
    print time.asctime(time.localtime(time.time()))
    jsons.sort(key=lambda jsons:jsons.get("date_",0))
    print(6)
    for x in xrange(1,len(jsons)):
        if jsons[x]["date_"] == jsons[x-1]["date_"]:

                jsons[x]["re_0"]=int(round(float(jsons[x]["re_0"])))+int(round(float(jsons[x-1]["re_0"]))) 
                jsons[x]["re_1"]=int(round(float(jsons[x]["re_1"])))+int(round(float(jsons[x-1]["re_1"]))) 
                jsons[x]["re_2"]=int(round(float(jsons[x]["re_2"])))+int(round(float(jsons[x-1]["re_2"]))) 
                jsons[x]["re_3"]=int(round(float(jsons[x]["re_3"])))+int(round(float(jsons[x-1]["re_3"]))) 
                jsons[x]["re_4"]=int(round(float(jsons[x]["re_4"])))+int(round(float(jsons[x-1]["re_4"]))) 
                jsons[x]["re_5"]=int(round(float(jsons[x]["re_5"])))+int(round(float(jsons[x-1]["re_5"]))) 
                jsons[x]["re_6"]=int(round(float(jsons[x]["re_6"])))+int(round(float(jsons[x-1]["re_6"]))) 
                jsons[x-1]=""
    for item in jsons[:]:
        if item == "":
            jsons.remove(item)
    print(type(jsons))
        #resultjson=resultjson[0:-1]
    print time.asctime(time.localtime(time.time()))
    return json.dumps(jsons)




@analyzeBp.route('/mediaRetentionTJ')
def mediaRetentionTJ():
    results = cMediaRetention.mediaRetentionTJ(session["username"])
    return results