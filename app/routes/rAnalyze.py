# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
import random
import re
import time
from app.controler.power_API import get_business_json
from app.controler.cMediaOverview import cMediaOverview
from app.controler.cNewTransfer import cNewTransfer

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
    return results


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
    word=""
    resultjson=""
    for x in xrange(0,len(args)):
        if args[x][1]!="":
            word=r'({[^}]*"'+args[x][0]+'":"'+args[x][1].replace(',','"[^}]+}|{[^}]+"'+args[x][0]+'":"')+'"[^}]*})'
            jsons=",".join(re.findall(word,jsons))
            print(4)
        else:
            word=r'({[^}]*[^}]*})'
            jsons=",".join(re.findall(word,jsons))

    jsons=json.loads("["+jsons+"]")

    new_json=[]
    date_temp=[]
    print time.asctime(time.localtime(time.time()))
    jsons.sort(key=lambda jsons:jsons.get("date_",0))
    for x in xrange(1,len(jsons)):
        if jsons[x]["date_"] == jsons[x-1]["date_"]:
            if jsons[x-1]["re_0"]=="":

                jsons[x]["re_0"]=int(round(float(jsons[x]["re_0"])))+int(round(float(jsons[x-1]["re_0"]))) if len(jsons[x-1]["re_0"])>0 else int(round(float(jsons[x]["re_0"])))
                jsons[x]["re_1"]=int(round(float(jsons[x]["re_1"])))+int(round(float(jsons[x-1]["re_1"]))) if len(jsons[x-1]["re_1"])>0 else int(round(float(jsons[x]["re_1"])))
                jsons[x]["re_2"]=int(round(float(jsons[x]["re_2"])))+int(round(float(jsons[x-1]["re_2"]))) if len(jsons[x-1]["re_2"])>0 else int(round(float(jsons[x]["re_2"])))
                jsons[x]["re_3"]=int(round(float(jsons[x]["re_3"])))+int(round(float(jsons[x-1]["re_3"]))) if len(jsons[x-1]["re_3"])>0 else int(round(float(jsons[x]["re_3"])))
                jsons[x]["re_4"]=int(round(float(jsons[x]["re_4"])))+int(round(float(jsons[x-1]["re_4"]))) if len(jsons[x-1]["re_4"])>0 else int(round(float(jsons[x]["re_4"])))
                jsons[x]["re_5"]=int(round(float(jsons[x]["re_5"])))+int(round(float(jsons[x-1]["re_5"]))) if len(jsons[x-1]["re_5"])>0 else int(round(float(jsons[x]["re_5"])))
                jsons[x]["re_6"]=int(round(float(jsons[x]["re_6"])))+int(round(float(jsons[x-1]["re_6"]))) if len(jsons[x-1]["re_6"])>0 else int(round(float(jsons[x]["re_6"])))
                jsons[x-1]=""
    
    for x in xrange(0,len(jsons)):
        if jsons[x]!="":
            resultjson+=jsons[x]+","
        resultjson=resultjson[0:-1]
    print time.asctime(time.localtime(time.time()))
    r="["+resultjson+"]"
    return r




