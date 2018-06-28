#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#encoding=utf-8


import sys
import os
import shutil
import re
from flask import session
from app.db.dbBase import DBConnect
from Config import Config
import time
import datetime
import xlrd
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

############################################################################
# 1、获取明细json
# 2、获取汇总json
# 3、登录、权限等
# 4、
##
############################################################################

def clac():
	time1= time.time()
	trade_id=88
	trade_name=88
	money_in=88
 	money_out=88
	Transfer=88
	commission=88
	equity=88
	test = []
	pwd="\static\csv\\"
	file="GN (1).xls"
	newlist=[]
	statinfo=[]
	print(os.getcwd()+pwd+file)
	sql=""
	#time_tag=str(file_pwd.split("/")[-2])
	time_tag=str(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
	date=str(datetime.datetime.now().strftime('%Y-%m-%d'));
	print(pwd+file)
	if  os.path.exists(os.getcwd()+pwd+file):
		print(1)
		filename=os.getcwd()+pwd+file
		try:
			data = xlrd.open_workbook(filename)
		except:
			return '{"status":"-1","body":"'+str(file)+' 文件无法打开"}'

 
		sql='insert into data_detail values ' 

		table = data.sheets()[0]

	for x in xrange(0,table.ncols):
		if table.cell(0,x).value=='交易商编号':
			trade_id=x
		if table.cell(0,x).value=='交易商名称':
			trade_name=x
		if table.cell(0,x).value=='入金':
			money_in=x
		if table.cell(0,x).value=='出金':
			money_out=x
		if table.cell(0,x).value=='转让盈亏':
			Transfer=x
		if table.cell(0,x).value=='交易手续费':
			commission=x
		if table.cell(0,x).value=='总权益':
			equity=x
	for x in xrange(0,table.nrows):

		try:
			sql+='("'+str(date)+'\","'+str(table.cell(x,trade_id).value).replace('"','')+'\\","'+str(table.cell(x,trade_name).value).replace('"','')+'\","'+str(table.cell(x,money_in).value).replace('"','')+'\","'+str(table.cell(x,commission).value).replace('"','')+'\","'+str(table.cell(x,Transfer).value).replace('"','')+'\","'+str(table.cell(x,equity).value).replace('"','')+'\","'+str(time_tag)+'\","'+str(file)+'\")'
			
		except:
			return '{"status":"-1","body":"'+str(file)+' 的表头命名不正确"}'


	

	try:
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		print(sql)
		cursor.execute(sql)
		conn.commit()
		cursor.close()
		conn.close()
	except Exception, e:
		cursor.close()
		conn.close()
		print(str(e))
		return '{"status":"-1","body":"数据库连接出错 "}'

	return '{"status":"0","body":"'+str( time.time()-time1)+'"}'

 



def login_in(username,password):
	print("runlogin")
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
				print(Config.ADMIN,session['zhanshi'] )
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

				pattern=pattern+re.findall(r"{[^\}]*"+str(reg[x])+"[^\}]*.}",context)
	
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
	result=result.replace("other", "其他")
	result=result.replace("linxu", "林旭")
	result=result.replace("weizhi_none", "未归类")
	result=result.replace("zhangchi", "张弛")
	return result

