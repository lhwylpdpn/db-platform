# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
import random

from app.controler.power_API import get_business_json


analyzeBp = Blueprint('analyze', __name__, url_prefix="/analyze")


@analyzeBp.route('/mediaOverview')
def mediaOverview():
    return render_template("putAnalyze/mediaAnalyze/mediaOverview.html", title=U"媒体概览", sjs=random.random())


@analyzeBp.route('/mediaOverviewJson')
def mediaOverviewJson():
    jsons = json.loads(get_business_json("media_1.json", session["username"]))  # 字符串传化为json 对象
    return json.dumps(jsons["body"])
