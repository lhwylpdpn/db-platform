#!/usr/bin/python
# -*- coding: utf-8 -*-
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
import shutil
import random
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

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')




def file_name(file_dir): 
	level_1_file=[]
	for root, dirs, files in os.walk(file_dir):
		#print(root) #当前目录路径
		#print(dirs) #当前路径下所有子目录
		#print(files) #当前路径下所有非目录子文件
		if root==file_dir:
			level_1_file=files
			#print(3,level_1_file)
	return level_1_file
def clac():

	time1= time.time()


	try:
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		#print(sql)
		cursor.execute("delete from data_detail where date=LEFT(NOW(),10);")
		conn.commit()
		cursor.close()
		conn.close()
	except Exception, e:
		cursor.close()
		conn.close()
		print(str(e))
		return '{"status":"-1","body":"数据库初始清除出错 "}'


	trade_id=""
	trade_name=""
	money_in=""
 	money_out=""
	Transfer=""
	commission=""
	equity=""
	jiqibaozhengjin=""
	dinghuojingkuisun=""
	dangrikeyongzijin=""
	qichuzijin=""
	Transfer_clac=""
	test = []
	pwd="\static\csv\\"
	fileimportDB=0
	filelist=file_name(os.getcwd()+pwd)
	newlist=[]
	statinfo=[]
	file_mysql=""
	sql=""
	#time_tag=str(file_pwd.split("/")[-2])
	time_tag=str(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
	date=str(datetime.datetime.now().strftime('%Y-%m-%d'));
	for r in filelist:
		if  os.path.exists(os.getcwd()+pwd+r):
			file=r
			print('3',file)
			filename=os.getcwd()+pwd+r
			try:
				data = xlrd.open_workbook(filename)
			except:
				return '{"status":"-1","body":"'+str(file)+' 文件无法打开"}'

	 
			sql='insert into data_detail values ' 
			#print('4',sql)
			table = data.sheets()[0]
	#
	#by 2018-7-19 lhwylp
	#入库的市场规整一些,统一调整为一个代号
	# 	
		if 'GN' in file or 'gn' in file:
			file_mysql="GN"
		elif 'HB' in file  or 'hb' in file:
			file_mysql="HB"
		elif 'GS' in file  or 'gs' in file:
			file_mysql="GS"
		elif 'QB' in file  or 'qb' in file:
			file_mysql="QB"
		else:
			file_mysql=file
		for x in xrange(0,table.ncols):
			if table.cell(0,x).value=='交易商编号' or table.cell(0,x).value=='会员编号':
				trade_id=x
			if table.cell(0,x).value=='交易商名称' or table.cell(0,x).value=='会员名称':
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
			if table.cell(0,x).value=='即期保证金':
				jiqibaozhengjin=x
			if table.cell(0,x).value=='订货净亏损':
				dinghuojingkuisun=x
			if table.cell(0,x).value=='当日可用资金':
				dangrikeyongzijin=x
			if table.cell(0,x).value=='期初资金':
				qichuzijin=x

		for x in xrange(1,table.nrows):

			try:
				if Transfer=="":

					#print(float(table.cell(x,commission).value.replace('"','').replace(',','')) - float(table.cell(x,qichuzijin).value.replace('"','').replace(',','')));
					#print(float(table.cell(x,commission).value.replace('"','').replace(',','')) ,float(table.cell(x,qichuzijin).value.replace('"','').replace(',','')))
					Transfer_clac=float(table.cell(x,jiqibaozhengjin).value.replace('"','').replace(',',''))+float(table.cell(x,dinghuojingkuisun).value.replace('"','').replace(',',''))+float(table.cell(x,dangrikeyongzijin).value.replace('"','').replace(',',''))+float(table.cell(x,commission).value.replace('"','').replace(',','')) - float(table.cell(x,qichuzijin).value.replace('"','').replace(',','')) - float(table.cell(x,money_in).value.replace('"','').replace(',',''))



					sql+='("'+str(date)+'","'+str(table.cell(x,trade_id).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,trade_name).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,money_in).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,money_out).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,commission).value).replace('"','').replace(',','').decode()+'","'+str(Transfer_clac).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,equity).value).replace('"','').replace(',','').decode()+'","'+str(time_tag)+'","'+str(file_mysql)+'"),'
				else:
					#print(chardet.detect(sql))
					sql+='("'+str(date)+'","'+str(table.cell(x,trade_id).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,trade_name).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,money_in).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,money_out).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,commission).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,Transfer).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,equity).value).replace('"','').replace(',','').decode()+'","'+str(time_tag)+'","'+str(file_mysql)+'"),'

			except Exception, e:
				print("1",e)
				return '{"status":"-1","body":"'+str(file)+' 的excel文件可能有问题，常见可能问题：1、表头不对,不包含协定文字;2、各类价格字段中可能有非数字文字;"}'
 

		try:
			conn = DBConnect.db_connect(Config.DATABASE_MAIN)
			cursor = conn.cursor()
			#print(sql)
			cursor.execute(sql[:-1])
			conn.commit()
			cursor.close()
			conn.close()
			fileimportDB+=1
		except Exception, e:
			cursor.close()
			conn.close()
			print("2",str(e))
			return '{"status":"-1","body":"'+str(e)+'，已经入库了'+str(fileimportDB)+' 个文件,当前出错的文件是'+str(r)+'"}'
		#sql=""
		trade_id=""
		trade_name=""
		money_in=""
	 	money_out=""
		Transfer=""
		commission=""
		equity=""
		jiqibaozhengjin=""
		dinghuojingkuisun=""
		dangrikeyongzijin=""
		qichuzijin=""
		Transfer_clac=""

	time_tag=str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
		#os.mkdir(os.getcwd()+"\static\\"+time_tag)
		#print(filelist)
		#print(os.getcwd()+"\static\\"+time_tag+"\\")
	shutil.move(os.getcwd()+pwd,os.getcwd()+"\static\\"+time_tag)  
	os.mkdir(os.getcwd()+"\static\csv")
	return '{"status":0,"body":"'+str( round(time.time()-time1,3))+'秒,成功入库了'+str(fileimportDB)+' 个文件"}'

 #  by lhwylpdpn 返佣信息入库表 2018-08-02
def clac_config():

	time1= time.time()


	try:
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		#print(sql)
		cursor.execute("truncate agent_class;")
		conn.commit()
		cursor.close()
		conn.close()
	except Exception, e:
		cursor.close()
		conn.close()
		print(str(e))
		return '{"status":"-1","body":"返佣配置信息初始清除出错 "}'


	trade_id=""
	market=""
	class_name=""
 	agent_1=""
	agent_1_name=""
 	agent_2=""
	agent_2_name=""
 	agent_3=""
	agent_3_name=""
	zhifan=""
	zongfan=""
	test = []
	pwd="\static\csv_config\\"
	fileimportDB=0
	filelist=file_name(os.getcwd()+pwd)
	newlist=[]
	statinfo=[]
	file_mysql=""
	sql=""
	#time_tag=str(file_pwd.split("/")[-2])
	time_tag=str(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S'))
	date=str(datetime.datetime.now().strftime('%Y-%m-%d'));
	for r in filelist:
		if  r=='config.xls' or r=='config.xlsx':
			file=r
			
			filename=os.getcwd()+pwd+r
			try:
				data = xlrd.open_workbook(filename)
			except:
				return '{"status":"-1","body":"'+str(file)+' 文件无法打开"}'

	 
			sql='insert into agent_class values ' 
			#print('4',sql)
			table = data.sheets()[0]

		for x in xrange(0,table.ncols):
			if table.cell(0,x).value=='交易账号':
				trade_id=x
			if table.cell(0,x).value=='市场' :
				market=x
			if table.cell(0,x).value=='归属':
				class_name=x
			if table.cell(0,x).value=='1返佣人':
				agent_1_name=x
			if table.cell(0,x).value=='1返比例':
				agent_1=x
			if table.cell(0,x).value=='2返佣人':
				agent_2_name=x
			if table.cell(0,x).value=='2返比例':
				agent_2=x
			if table.cell(0,x).value=='3返佣人':
				agent_3_name=x
			if table.cell(0,x).value=='3返比例':
				agent_3=x
			if table.cell(0,x).value=='直返比例':
				zhifan=x
			if table.cell(0,x).value=='总返比例':
				zongfan=x

		for x in xrange(1,table.nrows):

			try:
				

				sql+='("'+str(int(table.cell(x,trade_id).value))+'","'+str(table.cell(x,market).value).replace('"','').replace(',','').strip().upper().decode()+'","'+str(table.cell(x,class_name).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,agent_1).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,agent_1_name).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,agent_2).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,agent_2_name).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,agent_3).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,agent_3_name).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,zhifan).value).replace('"','').replace(',','').decode()+'","'+str(table.cell(x,zongfan).value).replace('"','').replace(',','').decode()+'","'+str(time_tag)+'"),'

			except Exception, e:
				print("1",e)
				return '{"status":"-1","body":"'+str(file)+' 的excel文件可能有问题，常见可能问题：1、表头不对,不包含协定文字;2、各类价格字段中可能有非数字文字;"}'
 

		try:
			conn = DBConnect.db_connect(Config.DATABASE_MAIN)
			cursor = conn.cursor()
			#print(sql)
			cursor.execute(sql[:-1])
			conn.commit()
			cursor.close()
			conn.close()
			fileimportDB+=1
		except Exception, e:
			cursor.close()
			conn.close()
			print("2",str(e))
			return '{"status":"-1","body":"'+str(e)+'"}'
		#sql=""
		trade_id=""
		market=""
		class_name=""
	 	agent_1=""
		agent_1_name=""
	 	agent_2=""
		agent_2_name=""
	 	agent_3=""
		agent_3_name=""
		zhifan=""
		zongfan=""
	time_tag=str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
		#os.mkdir(os.getcwd()+"\static\\"+time_tag)
		#print(filelist)
		#print(os.getcwd()+"\static\\"+time_tag+"\\")
	shutil.move(os.getcwd()+pwd,os.getcwd()+"\static\\config"+time_tag)  
	os.mkdir(os.getcwd()+"\static\csv_config")
	return '{"status":0,"body":"'+str( round(time.time()-time1,3))+'秒,成功入库了'+str(fileimportDB)+' 个文件"}'



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

def get_data_detail(username,date,filename):#usernames是一维数组传入用户名，poweritems是二维数组，传入每个用户名的权限数组
# 判断数据文剑名是否存在
# 判断文件是否处于写状态
# copy文件
# 正则筛选
# 返回json

	user_=username
	date_=date
	result=""
	try:
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		sql="""
	SELECT a.`trade_id`,a.`trade_name`,a.`commission`,b.`agent_name_1`,CONVERT(b.`agent_ratio_1`*a.`commission`,DECIMAL(20,2)) AS m_1,b.`agent_name_2`,CONVERT(b.`agent_ratio_2`*a.`commission`,DECIMAL(20,2)) AS m_2, b.`agent_name_3`,CONVERT(b.`agent_ratio_3`*a.`commission` ,DECIMAL(20,2)) AS m_3
	,a.filename

	FROM `data_detail` a LEFT JOIN `agent_class` b ON a.`trade_id`=b.`trade_id` AND a.`filename`=b.`filename` 
	WHERE a.`date`='"""+str(date_)+"""'  AND b.class_name ='"""+str(user_)+"""'  
	AND a.filename LIKE '%"""+str(filename)+"""%' AND CAST(a.commission AS SIGNED)>0 







	"""
		#print(sql)
		cursor.execute(sql)
		rs=cursor.fetchall()

		for r in rs:
			result+='{"trade_id":"'+str(r[0])+'","trade_name":"'+str(r[1])+'","commission":"'+str(r[2])+'","agent_name_1":"'+str(r[3])+'","m_1":"'+str(r[4])+'","agent_name_2":"'+str(r[5])+'","m_2":"'+str(r[6])+'","agent_name_3":"'+str(r[7])+'","m_3":"'+str(r[8])+'","filename":"'+str(r[9])+'"},'
		
		
		result='{"status":"0","body":['+result[0:-1]+']}'
		#print(result)
		return result
	except Exception, e:
		print e
		return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'

#################################################

#by lhwylpdpn 临时增加的合计功能 2018-8-1

#数据返回接口##############################################################################

def get_data_detail_heji(username,date):#usernames是一维数组传入用户名，poweritems是二维数组，传入每个用户名的权限数组
# 判断数据文剑名是否存在
# 判断文件是否处于写状态
# copy文件
# 正则筛选
# 返回json

	user_=username
	date_=date
	result=""
	try:
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		sql="""
	SELECT "合计",SUM(m_1) AS m_1,SUM(m_2) AS m_2, SUM(m_3) AS m_3 FROM (	
	SELECT a.`trade_id`,a.`trade_name`,a.`commission`,b.`agent_name_1`,CONVERT(b.`agent_ratio_1`*a.`commission`,DECIMAL(20,2)) AS m_1,b.`agent_name_2`,CONVERT(b.`agent_ratio_2`*a.`commission`,DECIMAL(20,2)) AS m_2, b.`agent_name_3`,CONVERT(b.`agent_ratio_3`*a.`commission` ,DECIMAL(20,2)) AS m_3
	,a.filename

	FROM `data_detail` a LEFT JOIN `agent_class` b ON a.`trade_id`=b.`trade_id` AND a.`filename`=b.`filename` 
	WHERE a.`date`='"""+str(date_)+"""'  AND b.class_name ='"""+str(user_)+"""'  
	 AND CAST(a.commission AS SIGNED)>0 




	 ) a



	"""
		#print(sql)
		cursor.execute(sql)
		rs=cursor.fetchall()

		for r in rs:
			result+='{"trade_id":"'+str(r[0])+'","m_1":"'+str(r[1])+'","m_2":"'+str(r[2])+'","m_3":"'+str(r[3])+'"},'
		
		
		result='{"status":"0","body":['+result[0:-1]+']}'
		#print(result)
		return result
	except Exception, e:
		print e
		return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'

#################################################


def get_data_static(username,date_start,date_end,filename,allocation):#usernames是一维数组传入用户名，poweritems是二维数组，传入每个用户名的权限数组
# 判断数据文剑名是否存在
# 判断文件是否处于写状态
# copy文件
# 正则筛选
# 返回json

	user_=username
	date_s=date_start
	date_e=date_end
	file_=filename
	all_=allocation
 	result=""


	if date_s!="开始日期":
		date_s=""" and  DATE>='"""+str(date_s)+"""'"""
	else :
		date_s=""


	if date_e!="结束日期":
		date_e=""" and  DATE <='"""+str(date_e)+"""'"""
	else :
		date_e=""
  

	if file_!="全部市场":
		file_=""" and filename2='"""+str(file_)+"""'"""
	else :
		file_=""

	if user_!="全部归属人":
		user_=""" and class_name='"""+str(file_)+"""'"""
	else :
		user_=""


	print(all_)
	if all_=="配资":
		all_=""" and trade_id2='配资' """
	elif  all_=="非配资":
		all_=""" and trade_id2!="配资" """
	else:
		all_=""
	#print(all_)
	try:
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		sql="""
	SELECT * FROM (
	SELECT 1,case when b.trade_id is not null then '配资' else '非配资' end as trade_id2,CASE WHEN c.class_name IS NULL THEN '待定' ELSE c.class_name END AS class_name,
        CASE WHEN  a.filename LIKE '%HB%' THEN '新疆汇宝' 
        WHEN a.filename LIKE '%GN%' THEN '贵州西部'
        WHEN a.filename LIKE '%GS%' THEN '寿光果蔬'
        WHEN a.filename LIKE '%QB%' THEN '青岛北方'
		ELSE  a.filename END AS filename2,SUM(money_in) AS money_in,SUM(money_out) AS money_out,
        SUM(a.Transfer) AS Transfer,SUM(a.commission) AS commission,SUM(a.equity) AS equity,
        SUM((c.all_re_ratio-c.agent_ratio_1-c.agent_ratio_2-c.agent_ratio_3)*commission) AS lirun,
		SUM(-(c.day_re_ratio-c.agent_ratio_1-c.agent_ratio_2-c.agent_ratio_3)*commission) AS dianzi

	
	FROM `data_detail` a LEFT JOIN `agent_class` c ON a.`trade_id`=c.`trade_id` AND a.`filename`=c.`filename` 
	LEFT JOIN `trade_id_status` b ON a.trade_id=b.trade_id AND a.filename=b.filename
	
	WHERE 1=1 """+date_s+date_e+"""
	   GROUP BY c.class_name,filename2,trade_id2  )  a
	 
	WHERE  1=1  
	"""+user_+file_+all_

		#print(sql)
		cursor.execute(sql)
		rs=cursor.fetchall()

		for r in rs:
			result+='{"date":"'+str(r[0])+'","all_":"'+str(r[1])+'","class_name":"'+str(r[2])+'","filename":"'+str(r[3])+'","money_in":"'+str(r[4])+'","money_out":"'+str(r[5])+'","Transfer":"'+str(r[6])+'","commission":"'+str(r[7])+'","equity":"'+str(r[8])+'","liushui":"'+str(r[9])+'","dianzi":"'+str(r[10])+'"},'
		
		
		result='{"status":"0","body":['+result[0:-1]+']}'
		#print(result)
		return result
	except Exception, e:
		print e
		return '{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'

#################################################


def get_data_class_date():

	result=""
	try:
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		sql="""
SELECT distinct date FROM DBplatform.data_detail;

	"""
		cursor.execute(sql)
		rs=cursor.fetchall()
 		for r in rs:
 			 result+=str(r[0])+","
		
		
		
		return result[0:-1]
	except Exception, e:
		print e
		return ""



def get_data_class_name():#usernames是一维数组传入用户名，poweritems是二维数组，传入每个用户名的权限数组
# 判断数据文剑名是否存在
# 判断文件是否处于写状态
# copy文件
# 正则筛选
# 返回json

	result=""
	try:
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		sql="""
    	
	 SELECT DISTINCT  class_name  FROM `agent_class`
	 UNION ALL
	 SELECT "待定"

	"""
		cursor.execute(sql)
		rs=cursor.fetchall()
 		for r in rs:
 			 result+=str(r[0])+","
		
		
		
		return result[0:-1]
	except Exception, e:
		print e
		return ""




def get_data_class_filename():

	result=""
	try:
		conn = DBConnect.db_connect(Config.DATABASE_MAIN)
		cursor = conn.cursor()
		sql="""
		select '全部市场'
		union all
		
SELECT  DISTINCT CASE WHEN  filename LIKE '%HB%' THEN '新疆汇宝' 
        WHEN filename LIKE '%GN%' THEN '贵州西部'
        WHEN filename LIKE '%GS%' THEN '寿光果蔬'
        WHEN filename LIKE '%QB%' THEN '青岛北方'
		ELSE  filename END AS filename2  FROM `data_detail`

	"""
		cursor.execute(sql)
		rs=cursor.fetchall()
 		for r in rs:
 			 result+=str(r[0])+","
		
		
		
		return result[0:-1]
	except Exception, e:
		print e
		return ""
