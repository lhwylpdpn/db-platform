# This Python file uses the following encoding: utf-8
import sys
import os
import shutil
import re
from flask import session
from app.db.dbBase import DBConnect
from Config import Config
import time
import datetime



def monitor_data():# 收集监控所需要的系统文件数据
	value=[]
	#for wanggang
	pwd_yuan="/data1/bidata"

	if  os.path.exists(pwd_yuan+"/LaunchPaymentAll.csv"):
		statinfo=os.stat(pwd_yuan+"/LaunchPaymentAll.csv")
		value.append(["LaunchPaymentAll",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["LaunchPaymentAll","0"])

	if  os.path.exists(pwd_yuan+"/1452827692979/Daily_lchy_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv"):
		statinfo=os.stat(pwd_yuan+"/1452827692979/Daily_lchy_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv")
		value.append(["Daily_lchy",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["Daily_lchy","0"])

	if  os.path.exists(pwd_yuan+"/1452827692979/Daily_tfzh_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv"):
		statinfo=os.stat(pwd_yuan+"/1452827692979/Daily_tfzh_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv")
		value.append(["Daily_tfzh",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["Daily_tfzh","0"])

	if  os.path.exists(pwd_yuan+"/1452827692979/Daily_zbhs_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv"):
		statinfo=os.stat(pwd_yuan+"/1452827692979/Daily_zbhs_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv")
		value.append(["Daily_zbhs",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["Daily_zbhs","0"])

	if  os.path.exists(pwd_yuan+"/1452827692979/Daily_xzff_detail_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv"):
		statinfo=os.stat(pwd_yuan+"/1452827692979/Daily_xzff_detail_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
		value.append(["Daily_xzff_detail",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["Daily_xzff_detail","0"])

	if  os.path.exists(pwd_yuan+"/1452827692979/market_onlinetime_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv"):
		statinfo=os.stat(pwd_yuan+"/1452827692979/market_onlinetime_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
		value.append(["market_onlinetime_",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["market_onlinetime_","0"])

	if  os.path.exists(pwd_yuan+"/1452827692979/market_newuser_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv"):
		statinfo=os.stat(pwd_yuan+"/1452827692979/market_newuser_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
		value.append(["market_newuser_",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["market_newuser_","0"])

	if  os.path.exists(pwd_yuan+"/1452827692979/market_logincount_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv"):
		statinfo=os.stat(pwd_yuan+"/1452827692979/market_logincount_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
		value.append(["market_logincount_",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["market_logincount_","0"])

	if  os.path.exists(pwd_yuan+"/1452827692979/market_ltv_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv"):
		statinfo=os.stat(pwd_yuan+"/1452827692979/market_ltv_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
		value.append(["market_ltv_",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["market_ltv_","0"])

	if  os.path.exists(pwd_yuan+"/1452827692979/market_retain_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv"):
		statinfo=os.stat(pwd_yuan+"/1452827692979/market_retain_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
		value.append(["market_retain_",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["market_retain_","0"])

	if  os.path.exists(pwd_yuan+"/1452827692979/market_levelup_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv"):
		statinfo=os.stat(pwd_yuan+"/1452827692979/market_levelup_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
		value.append(["market_levelup_log_",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["market_levelup_log_","0"])

	if  os.path.exists(pwd_yuan+"/1452827692979/market_login_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv"):
		statinfo=os.stat(pwd_yuan+"/1452827692979/market_login_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
		value.append(["market_login_log_",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["market_login_log_","0"])


	if  os.path.exists(pwd_yuan+"/1452827692979/market_logout_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv"):
		statinfo=os.stat(pwd_yuan+"/1452827692979/market_logout_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
		value.append(["market_logout_log_",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["market_logout_log_","0"])
		
	#for zengliang

	pwd_yuan="/data1/bidata"
	#print(pwd_yuan+"/tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv");
	#print(os.path.exists(pwd_yuan+"/tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv"));
	if  os.path.exists(pwd_yuan+"/tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv"):
		
		statinfo=os.stat(pwd_yuan+"/tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv")
		#print(statinfo.st_mtime)
		value.append(["tffy_", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["tffy_","0"])


	#process id,monitor ,service_json_A,manager
	process_list = os.popen("ps -ef |grep monitor.py |awk '{print $2}'").readlines()
	#print(len(process_list))
	if len(process_list)>2:
		value.append(["monitor",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
		#print(time.asctime("monitor",time.localtime(statinfo.st_mtime)))
	else:
		value.append(["monitor","0"])
	process_list = os.popen("ps -ef |grep service_json_A.py |awk '{print $2}'").readlines()
	#print(len(process_list))
	if len(process_list)>2:
		value.append(["service_json_A",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
	else:
		value.append(["service_json_A","0"])
	process_list = os.popen("ps -ef |grep manager.py |awk '{print $2}'").readlines()
	#print(len(process_list))
	if len(process_list)>3:
		value.append(["manager",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
	else:
		value.append(["manager","0"])

	if len(process_list)>3:
		value.append(["csv_import_A",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
	else:
		value.append(["csv_import_A","0"])


	# for json tongbu zengquexing

	pwd_yuan="/var/www/zilong_new/static/json"
	if  os.path.exists(pwd_yuan+"/test.json"):
		
		statinfo=os.stat(pwd_yuan+"/test.json")
		#print(statinfo.st_mtime)
		value.append(["test_json", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
		#print(time.asctime(time.localtime(statinfo.st_mtime)))
	else:
		value.append(["test_json","0"])	

	if  os.path.exists(pwd_yuan+"/media_1.json"):
		
		statinfo=os.stat(pwd_yuan+"/media_1.json")
		#print(statinfo.st_mtime)
		value.append(["media_1.json", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
		#print(time.asctime(time.localtime(statinfo.st_mtime)))
	else:
		value.append(["media_1.json","0"])	
	word="["
	for x in xrange(0,len(value)):
		status=""
		if value[x][1]=="0":
			status="error"
		else:
			status="ok"
		word+='{"file":"'+str(value[x][0])+'","time":"'+str(value[x][1])+'","status":"'+status+'"},'
	word=word[0:-1]
	word+="]"
	return word


################################################################################

def monitor_login():

	try:
		result=""
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		sql="select a.`username`,count(b.`login_time`) from `user_info` a ,`login_info` b where a.`id` =b.`user_id`  and a.username!='admin'  group by username"
		cursor.execute(sql)
		rs=cursor.fetchall()
		if len(rs)<=0:
			return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'
		else:
			for r in rs:
				result+='{"name":"'+str(r[0])+'","time":"'+str(r[1])+'"},'
			result=result[0:-1]
		result='{"status":"0","body":['+result+']}'

		cursor.execute(sql)
		cursor.close()
		conn.commit()
		conn.close()
		return result
	except Exception, e:
		return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'

def menu_click_write(username,menu_url,time_click):#username 代表登录的人，menu_url 代表访问链接 time 代表访问时间
	if username=="admin":
		return '{"status":"0"}'

	try:
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		name=str(username)
		menu=str(menu_url)
		time=str(time_click)
		sql="insert into menu_click values (null,'"+name+"','"+menu+"','"+time+"');"
		cursor.execute(sql)

		cursor.close()
		conn.commit()
		conn.close()
		return '{"status":"0"}'
	except Exception, e:
		return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'




def monitor_menu():
	result=""
	name=[]
	Transfer_menu_name=[]
	Transfer_menu_name.append(['/monitor/monitor','网站监控'])
	Transfer_menu_name.append(['/analyze/mediaOverview','媒体概览'])
	Transfer_menu_name.append(['/channelIos600','iOS-渠道-明细'])
	Transfer_menu_name.append(['/analyze/newTransfer','新增转化'])
	for x in xrange(0,len(Transfer_menu_name)):
		name.append(Transfer_menu_name[x][0])


	try:
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		test=[["/monitor/monitor",'网站监控'],['/analyze/mediaOverview','媒体概览'],['/channelIos600','iOS-渠道-明细'],['/analyze/newTransfer','新增转化']]
		sql="select menu_url,count(*) from menu_click group  by menu_url"
		cursor.execute(sql)
		rs=cursor.fetchall()
		if len(rs)<=0:
			return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'
		else:
			for x in xrange(0,len(rs)):
	
				try:
					result+='{"url":"'+str(Transfer_menu_name[name.index(str(rs[x][0]))][1])+'","count":"'+str(rs[x][1])+'"},'
				except Exception, e:
					continue
				
			result=result[0:-1]
		result='{"status":"0","body":['+result+']}'
		result=result.decode("utf-8")
		cursor.close()
		conn.commit()
		conn.close()
		return result
	except Exception, e:
		print(e)
		return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'



def monitor_pv():
	result=""
	name=[]
	date=[]
	count=[]
	Transfer_menu_name=[]
	Transfer_menu_name.append(['/monitor/monitor','网站监控'])
	Transfer_menu_name.append(['/analyze/mediaOverview','媒体概览'])
	Transfer_menu_name.append(['/channelIos600','iOS-渠道-明细'])
	Transfer_menu_name.append(['/analyze/newTransfer','新增转化'])
	for x in xrange(0,len(Transfer_menu_name)):
		name.append(Transfer_menu_name[x][0])


	try:
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		sql="SELECT  menu_url,concat(UNIX_TIMESTAMP(DATE_FORMAT(TIME, '%Y-%m-%d')),'000'),COUNT(*)  FROM  `menu_click` GROUP BY menu_url,UNIX_TIMESTAMP(DATE_FORMAT(TIME, '%Y-%m-%d'))"
		cursor.execute(sql)
		rs=cursor.fetchall()
		if len(rs)<=0:
			return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'
		else:
			for x in xrange(0,len(rs)):
	
				try:
					Transfer_menu_name[name.index(str(rs[x][0]))][1]
					if date.count(str(rs[x][1]))>0:
						count[date.index(str(rs[x][1]))]=int(count[date.index(str(rs[x][1]))])+int(rs[x][2])
					else:
						date.append(str(rs[x][1]))
						count.append(int(rs[x][2]))
					
				except Exception, e:
					continue
			for x in xrange(0,len(date)):
				result+='{"date":"'+str(date[x])+'","count":"'+str(count[x])+'"},'
			result=result[0:-1]
		result='{"status":"0","body":['+result+']}'
		result=result.decode("utf-8")
		cursor.close()
		conn.commit()
		conn.close()
		return result
	except Exception, e:
		print(e)
		return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'