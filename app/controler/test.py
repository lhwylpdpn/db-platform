#!/usr/bin/python
# -*- coding: UTF-8 -*- 



import pymysql
import os
import sys
import time
import csv
import sys
import datetime
import re
import json

reload(sys)
sys.setdefaultencoding('utf-8')

def import_excel():
	#pwd="/Users/liuhao/Desktop/zilong/app/controler/"
	pwd="C:\Users\Zlongame0156\Documents\GitHub\zilong\\app\controler\\"
	test = []
	test= os.listdir(pwd+"")

	newlist=[]
	statinfo=[]
	for names in test:

		if names.endswith(".csv"):
			#statinfo.append(os.stat(os.getcwd()+"/src/"+names).st_ctime)
			newlist.append(names)
	print(newlist)
	for r in newlist:

		if  not r.find("Daily_lchy_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))) and r.find("new")<0:#投放转化
			filename=pwd+""+r
			print(filename)
			filenode=open(filename)
			reader=csv.reader(filenode)
			sql="truncate zilong_report.retention;insert into zilong_report.retention values "
			for row in reader:
				sql=sql+"('"+"','".join(row)+"'),"
			sql=sql.strip(',')+";"
			print("1sql ok")
				#time.sleep(10)
			cur_1.execute(sql)
	
		if  not r.find("Daily_tfzh_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))) and r.find("new")<0:#投放转化

			filename=pwd+""+r
			print(filename)
			filenode=open(filename)
			reader=csv.reader(filenode)
			sql="truncate zilong_report.ad_action;insert into zilong_report.ad_action values "
			for row in reader:
				sql=sql+"('"+"','".join(row)+"'),"
			sql=sql.strip(',')+";"
			print("2sql ok")
				#time.sleep(10)
			cur_1.execute(sql)

		if  not r.find("Daily_zbhs_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))) and r.find("new")<0:#投放转化
			filename=pwd+""+r
			print(filename)
			filenode=open(filename)
			reader=csv.reader(filenode)
			sql="truncate zilong_report.re_money;insert into zilong_report.re_money values "
			for row in reader:
				sql=sql+"('"+"','".join(row[0:369])+"'),"
			sql=sql.strip(',')+";"
			print("3sql ok")
				#time.sleep(10)
			cur_1.execute(sql)

		if  not r.find("LaunchPaymentAll"):#投放转化
			filename=""+r
			print(filename)
			filenode=open(filename)
			reader=csv.reader(filenode)
			sql="truncate zilong_report.spend;insert into zilong_report.spend values "
			i=0
			for row in reader:
				print(i)
				i=i+1
				sql=sql+"('"+"','".join(row)+"'),"
			sql=sql.strip(',')+";"
			print("4sql ok ")
			cur_1.execute(sql)
			print("ok")

################ 为了web计算时间所用##############################





def create_json(word,name):
	file_object = open(os.getcwd()+'/../../static/json/'+name+'.json','w')
	file_object.write(word)
	file_object.close()
	print("create_json_"+name)



def guolv():

	jsons = open("../../static/json/media_3.json").read()

	r=re.findall(r'({[^}]*"channel_name":"内涵段子"[^}]*})',jsons)
	t=",".join(r)
	print(t)

def paixu():
	str1="""
	[{"game_id":"1452827692979","platform":"IOS正版","date_":"2016-07-01","channel_name":"自然量","agent":"自然量","staff":"luojiaming","re_0":"0.0","re_1":"0.0","re_2":"0.0","re_3":"0.0","re_4":"0.0","re_5":"0.0","re_6":"0.0"},
{"game_id":"1452827692979","platform":"安卓","date_":"2016-07-01","channel_name":"自然量","agent":"自然量","staff":"luojiaming","re_0":"0.0","re_1":"0.0","re_2":"0.0","re_3":"0.0","re_4":"0.0","re_5":"0.0","re_6":"0.0"},
{"game_id":"1452827692979","platform":"IOS正版","date_":"2016-07-03","channel_name":"自然量","agent":"自然量","staff":"luojiaming","re_0":"0.0","re_1":"0.0","re_2":"0.0","re_3":"0.0","re_4":"0.0","re_5":"0.0","re_6":"0.0"},
{"game_id":"1452827692979","platform":"安卓","date_":"2016-07-03","channel_name":"自然量","agent":"自然量","staff":"luojiaming","re_0":"0.0","re_1":"0.0","re_2":"0.0","re_3":"0.0","re_4":"0.0","re_5":"0.0","re_6":"0.0"},
{"game_id":"1452827692979","platform":"IOS正版","date_":"2016-07-04","channel_name":"自然量","agent":"自然量","staff":"luojiaming","re_0":"0.0","re_1":"0.0","re_2":"0.0","re_3":"0.0","re_4":"0.0","re_5":"0.0","re_6":"0.0"},
{"game_id":"1452827692979","platform":"安卓","date_":"2016-07-04","channel_name":"自然量","agent":"自然量","staff":"luojiaming","re_0":"0.0","re_1":"0.0","re_2":"0.0","re_3":"0.0","re_4":"0.0","re_5":"0.0","re_6":"0.0"},
{"game_id":"1452827692979","platform":"IOS正版","date_":"2016-07-05","channel_name":"自然量","agent":"自然量","staff":"luojiaming","re_0":"0.0","re_1":"0.0","re_2":"0.0","re_3":"0.0","re_4":"0.0","re_5":"0.0","re_6":"0.0"},
{"game_id":"1452827692979","platform":"安卓","date_":"2016-07-05","channel_name":"自然量","agent":"自然量","staff":"luojiaming","re_0":"0.0","re_1":"0.0","re_2":"0.0","re_3":"0.0","re_4":"0.0","re_5":"0.0","re_6":"0.0"},
{"game_id":"1452827692979","platform":"IOS正版","date_":"2016-07-06","channel_name":"自然量","agent":"自然量","staff":"luojiaming","re_0":"0.0","re_1":"0.0","re_2":"0.0","re_3":"0.0","re_4":"0.0","re_5":"0.0","re_6":"0.0"},
{"game_id":"1452827692979","platform":"安卓","date_":"2016-07-06","channel_name":"自然量","agent":"自然量","staff":"luojiaming","re_0":"0.0","re_1":"0.0","re_2":"0.0","re_3":"0.0","re_4":"0.0","re_5":"0.0","re_6":"0.0"}
]
"""
	jsons=json.loads(str1)






if __name__ == '__main__':
	print(u'\u7c73\u8fea'.decode("UTF-8"))
	# conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='zilong_report',port=3306)
	# cur_1=conn.cursor()
	# #import_excel()
	# #import_excel_add()
	# import_csv()
	# export_media_1()
	# #user_info_create()
	# #export()
	# cur_1.close()
	# conn.commit()
	# conn.close()
	# print time.asctime(time.localtime(time.time()))
