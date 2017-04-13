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
#非flask运行测试用 
#coding=UTF-8
# import sys
# import os
# import shutil
# import re
# sys.path.append("..")
# from db.dbBase import DBConnect
# sys.path.append("../..")
# from Config import Config
# import time
# import datetime
# import json

def login_in(username,password):
	user = username
	pwd = password
	result=""
	sql="SELECT status,id FROM user_info where username='"+user+"' and password='"+pwd+"' and  status in ('0','1');"
	#print(sql)
	conn = DBConnect.db_connect(Config.DATABASE_MAIN)
	cursor_login = conn.cursor()
	cursor_login.execute(sql)
	rs = cursor_login.fetchall()
	cursor_login.close()
	if len(rs)>=1:
		for r in rs:
			if r[0]=="0":
				session['username'] = username
				session['zhanshi'] = Config.ADMIN
				result='{"status":"0"}'
			if r[0]=="1":
				session['username'] = username
				session['mustModPass'] = '1'
				result='{"status":"1"}'
		login_log(r[1])
	elif len(rs)<1:
		result='{"status":"-1","body":"该用户名不存在或密码错误，请重新尝试"}'
		conn.close()
	

	return result


def login_log(userid):
	sql="insert into  login_info values ("+str(userid)+",now())"
	conn = DBConnect.db_connect(Config.DATABASE_MAIN)
	cursor_login_log = conn.cursor()
	cursor_login_log.execute(sql)
	cursor_login_log.close()
	conn.commit()
	conn.close()
#  更改密码部分###########################################################
def passwd_update(username,password):#强制更新传入用户新密码，后台修改传入密码为空
	user = username
	pwd = password
	result=""
	sql_1="select password from user_info where username='"+str(user)+"'"
	if pwd.strip()=="":
		sql_2 = "update user_info set password='1',user_up_time=now() ,status='1' where username='"+str(user)+"' and status='0'"
	else:
		sql_2 = "update user_info set password='"+str(pwd)+"',status='0' ,user_up_time=now() where username='"+str(user)+"' and status in ('1','0')"
	conn = DBConnect.db_connect(Config.DATABASE_MAIN)
	cursor = conn.cursor()
	cursor.execute(sql_1)
	rs = cursor.fetchall()
	if len(rs)>=1:
		for r in rs:
			if r[0]==str(pwd):
				result='{"status":"-1","body":"新密码不能与旧密码相同，请重新尝试"}'
				cursor.close()
				conn.close()
				return result
	else:
		result='{"status":"-1","body":"该用户名并不存在，请重新尝试"}'
		cursor.close()
		conn.close()
		return result
	try:
		cursor.execute(sql_2)
		cursor.close()
		conn.commit()
		conn.close()
		result='{"status":"0"}'
		#密码更新成功后需要去掉强制更新标识
		session.pop('mustModPass', None)
		return result
	except Exception, e:
		cursor.close()
		conn.close()
		result='{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'
		return result
################################################################################



# 获取用户权限接口########################################################
def power_list(usernames):# 输入需要获取权限的用户名、返回权限list，如果输入是空，返回所有
	users = ""
	power_r =[]
	user_r=[]
	result=""
	conn = DBConnect.db_connect(Config.DATABASE_MAIN)
	cursor = conn.cursor()
	
	if len(usernames)==0:
		sql="select username,power_user_list from power_info a ,user_info b where a.user_id=b.id"
	elif len(usernames)>=1:
		users="','".join(map(str,usernames))
		sql="select username,power_user_list from power_info a ,user_info b where a.user_id=b.id and b.username in ('"+users+"')"
	else:
		result='{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'
		cursor.close()
		conn.close()
		return result
	cursor.execute(sql)
	rs=cursor.fetchall()
	if len(rs)>=1:
		for r in rs:
			user_r.append(r[0])
			power_r.append(r[1])
		result='{"status":"0","body":{'
		for x in xrange(0,len(user_r)):
			result=result+'"'+str(user_r[x])+'":"'+str(power_r[x])+'",'
		result="".join(list(result)[0:len(list(result))-1])
		result=result+'}}'
	else:
		result='{"status":"0","body":{}}'
	cursor.close()
	conn.close()


	return result 
################################################################################

def power_list_update(usernames,poweritems):#usernames是一维数组传入用户名，poweritems是二维数组，传入每个用户名的权限数组

	if len(usernames)!=len(poweritems):
		return '{"status":"-1","body":"接口输入参数错误,用户名和权限数组长度不同"}'
	if len(usernames)<1:
		return '{"status":"-1","body":"接口输入参数错误,用户名或权限不能为空"}'
	try:

		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		sql=""
		for x in xrange(0,len(usernames)):

			sql=sql+"update  power_info set power_user_list ='"+str(",".join(poweritems[x]))+"' where user_id in (select id from user_info where username='"+str(usernames[x])+"');"

		cursor.execute(sql)
		cursor.close()
		conn.commit()
		conn.close()
		return '{"status":"0"}'
	except Exception, e:

		return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'


#数据返回接口##############################################################################

def get_business_json(filename,username):#usernames是一维数组传入用户名，poweritems是二维数组，传入每个用户名的权限数组
# 判断数据文剑名是否存在
# 判断文件是否处于写状态
# copy文件
# 正则筛选
# 返回json
	result=""
	pattern=[]
	pwd="../../static/json/"+str(filename)
	pwd="./static/json/"+str(filename)  # flask 项目当前目录是zilong根目录
	if os.path.exists(pwd):
		shutil.copyfile(pwd,str(filename))
	f=open(str(filename))
	try:
		context=f.read()
	except Exception, e:
		return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'
	finally:
		f.close()
	os.remove(str(filename))
	conn = DBConnect.db_connect(Config.DATABASE_MAIN)
	cursor = conn.cursor()
	sql="select power_user_list from power_info a ,user_info b where a.user_id=b.id and username in ('"+str(username)+"') and b.status in (0,1)"
	cursor.execute(sql)
	rs=cursor.fetchall()
	if len(rs)!=1:
		return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'
	else:
		for r in rs:
			reg=re.split(",",r[0])
			for x in xrange(0,len(reg)):
				print(reg[x])
				pattern=pattern+re.findall(r"{[^\}]+"+str(reg[x])+"[^\}]+.}",context)

	result=",".join(pattern)
	result='{"status":"0","body":['+result+']}'
	return staff_rename(result)

#################################################

#人名替换部分
def staff_rename(result):

	result=result.replace("chenlin", "陈琳")
	result=result.replace("hanpeng", "韩鹏")
	result=result.replace("lisihan", "刘思涵")
	result=result.replace("luojiaming", "罗家明")
	result=result.replace("qinxuetao", "秦雪涛")
	result=result.replace("tongfangfang", "陈琳")
	result=result.replace("wangyaxin", "王雅馨")
	result=result.replace("zhangmeng", "张萌")
	result=result.replace("zhangshuang", "张爽")
	result=result.replace("zhaojia", "赵佳")
	result=result.replace("zhouhao", "周浩")
	result=result.replace("zhangkaiwang", "张凯旺")
	result=result.replace("zhangkaiwangg", "张凯旺")
	result=result.replace("jinboxin", "金博鑫")
	result=result.replace("sunyueqiao", "孙月乔")
	result=result.replace("lijinquan", "李晋泉")
	result=result.replace("qingxuetao", "秦雪涛")
	result=result.replace("liusihan", "刘思涵")
	result=result.replace("zhengcaitong", "郑彩彤")
	return result

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

		
	#for zengliang

	pwd_yuan="/data1/bidata"
	print(pwd_yuan+"/tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv");
	print(os.path.exists(pwd_yuan+"/tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv"));
	if  os.path.exists(pwd_yuan+"/tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv"):
		
		statinfo=os.stat(pwd_yuan+"/tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv")
		#print(statinfo.st_mtime)
		value.append(["tffy_", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["tffy_","0"])


	#process id,monitor ,service_json_A,manager
	process_list = os.popen("ps -ef |grep monitor.py |awk '{print $2}'").readlines()
	print(len(process_list))
	if len(process_list)>2:
		value.append(["monitor",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
		#print(time.asctime("monitor",time.localtime(statinfo.st_mtime)))
	else:
		value.append(["monitor","0"])
	process_list = os.popen("ps -ef |grep service_json_A.py |awk '{print $2}'").readlines()
	print(len(process_list))
	if len(process_list)>2:
		value.append(["service_json_A",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
	else:
		value.append(["service_json_A","0"])
	process_list = os.popen("ps -ef |grep manager.py |awk '{print $2}'").readlines()
	print(len(process_list))
	if len(process_list)>3:
		value.append(["manager",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
	else:
		value.append(["manager","0"])




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
#if __name__ == '__main__':
#	print(get_business_json("test.json","admin"))
# 	test=["liuhao","admin"]
# 	test2=[["liuhao"],["liuhao","admin"]]
# 	print(power_list_update(test,test2))
	#test=["admin","liuhao"]
#	print(power_list(test))

################################################################################

def monitor_login():

	try:
		result=""
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		sql="select a.`username`,count(b.`login_time`) from `user_info` a ,`login_info` b where a.`id` =b.`user_id`   group by username"
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





#数据返回接口##############################################################################





def menu_click_write(username,menu_url,time_click):#username 代表登录的人，menu_url 代表访问链接 time 代表访问时间

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
		sql="SELECT  menu_url,CONCAT('Date.UTC(',DATE_FORMAT(TIME,'%Y,%c,%d'),')'),COUNT(*) AS a FROM  `menu_click` GROUP BY menu_url,DATE_FORMAT(TIME, '%Y-%m-%d') "
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
