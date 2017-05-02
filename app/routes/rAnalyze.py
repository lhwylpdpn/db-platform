# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
import random
import re
import time
from app.controler.power_API import get_business_json
from app.controler.cMediaOverview import cMediaOverview
from app.controler.cNewTransfer import cNewTransfer
from app.controler.cMediaRetention import cMediaRetention
from app.controler.public_function import p_analyzeTJ
import datetime

analyzeBp = Blueprint('analyze', __name__, url_prefix="/analyze")


# 媒体概览相关
@analyzeBp.route('/mediaOverview')
def mediaOverview():
    return render_template("putAnalyze/mediaAnalyze/mediaOverview.html", title=U"媒体概览", sjs=random.random())



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
    filterS = request.args.items()
    results = cNewTransfer.newTransferJson(session["username"], filterS)
    return results


#留存活跃相关
@analyzeBp.route('/mediaRetention')
def mediaRetention():
    return render_template("putAnalyze/mediaAnalyze/mediaRetention.html", title=U"留存活跃", sjs=random.random())


@analyzeBp.route('/mediaRetentionJson')
def mediaRetentionJson():
    results=cMediaRetention.mediaRetentionJson(session["username"])
    return results

@analyzeBp.route('/mediaRetentionJson2')
def mediaRetentionJson_2():
    results=cMediaRetention.mediaRetentionJson_2(session["username"])
    return results
@analyzeBp.route('/mediaRetentionJson3')
def mediaRetentionJson_3():
    results=cMediaRetention.mediaRetentionJson_3(session["username"])
    return results


# @analyzeBp.route('/mediaRetentionTJ')
# def mediaRetentionTJ():
#     results = cMediaRetention.mediaRetentionTJ(session["username"])

#     return results


@analyzeBp.route('/analyzeTJ')

def analyzeTJ():
    print(datetime.datetime.now())
    results = p_analyzeTJ(session["username"],request.args.items())
    print(datetime.datetime.now())
    return results