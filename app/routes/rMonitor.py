# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
from app.controler.power_API import monitor_data
from app.controler.power_API import monitor_menu
monitorBp = Blueprint('monitor', __name__, url_prefix="/monitor")


@monitorBp.route('/monitor')
def index():
	username=[]
	login_count=0
	jsons = json.loads(monitor_login())

	if jsons["status"]=="0":
		for x in xrange(0,len(jsons["body"])):
			username.append("['"+str(jsons["body"][x]["name"])+"',"+str(jsons["body"][x]["time"])+"]")
			login_count+=int(jsons["body"][x]["time"])

		return render_template("monitor/monitor.html",title=U"网站统计",username=username,login_count=login_count)
	else:
		return render_template("error.html")

@monitorBp.route('/monitorJson')
def monitorJson():
	jsons = json.loads(monitor_data())  # 字符串传化为json 对象
	print(jsons)
	return json.dumps(jsons)



