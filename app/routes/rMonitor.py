# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
from app.controler.power_API import monitor_data

monitorBp = Blueprint('monitor', __name__, url_prefix="/monitor")


@monitorBp.route('/monitor')
def index():
    return render_template("monitor/monitor.html",title=U"网站统计")


@monitorBp.route('/monitorJson')
def monitorJson():
    jsons = json.loads(monitor_data())  # 字符串传化为json 对象
    return json.dumps(jsons)
