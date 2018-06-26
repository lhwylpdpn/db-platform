# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
from app.controler.monitor import monitor_data
from app.controler.monitor import monitor_login
from app.controler.monitor import monitor_menu
from app.controler.monitor import monitor_pv
monitorBp = Blueprint('monitor', __name__, url_prefix="/monitor")


@monitorBp.route('/monitor')
def index():
	date = request.args.get('date')
	username=[]
	login_count=0
	menulist=[]
	menu_count=0
	pv_list=[]
	pv_count=0
	if date:
		jsons = json.loads(monitor_login(date))
		jsons_menu = json.loads(monitor_menu(date))
		jsons_pv=json.loads(monitor_pv(date))
  
	else :

		jsons = json.loads(monitor_login(""))
		jsons_menu = json.loads(monitor_menu(""))
		jsons_pv=json.loads(monitor_pv(""))
	print(jsons_menu)
	if jsons["status"]=="0" and jsons_menu["status"]=="0" and jsons_pv["status"]=="0":
		for x in xrange(0,len(jsons["body"])):
			username.append("['"+str(jsons["body"][x]["name"])+"',"+str(jsons["body"][x]["time"])+"]")
			login_count+=int(jsons["body"][x]["time"])
		for x in xrange(0,len(jsons_menu["body"])):

			menulist.append("['"+jsons_menu["body"][x]["url"]+"',"+str(jsons_menu["body"][x]["count"])+"]")
			menu_count+=int(jsons_menu["body"][x]["count"])
		for x in xrange(0,len(jsons_pv["body"])):

			pv_list.append("["+str(jsons_pv["body"][x]["date"])+","+str(jsons_pv["body"][x]["count"])+"]")
			#print(pv_list)
			##pv_count+=int(jsons_pv["body"][x]["count"])
		return render_template("monitor/monitor.html",title=U"网站统计",username=username,login_count=login_count,menulist=menulist,menu_count=menu_count,pv_list=pv_list,pv_count=pv_count)
	else:
		return render_template("monitor/monitor.html",title=U"网站统计",username=username,login_count=login_count,menulist=menulist,menu_count=menu_count,pv_list=pv_list,pv_count=pv_count)

@monitorBp.route('/monitorJson')
def monitorJson():
	jsons = json.loads(monitor_data())  # 字符串传化为json 对象
	#print(jsons)
	return json.dumps(jsons)



