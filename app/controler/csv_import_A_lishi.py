#!/usr/bin/python
# -*- coding: UTF-8 -*- 



import os
import sys
import time
import csv
import sys
import datetime

import os
import shutil
import re
sys.path.append("..")
from db.dbBase import DBConnect
sys.path.append("../..")
from Config import Config
import time
import pymysql
import csv

import threading

reload(sys)
sys.setdefaultencoding('utf-8')
def import_csv(file_pwd,filename,table,type):

	test = []
	pwd=file_pwd
	file=filename
	newlist=[]
	statinfo=[]
	tablename=table
	reader=[]
	time_tag="bushu"


	sql=""

	i=0
	if  os.path.exists(pwd+file):
		print(pwd+file)
		filename=pwd+file
		filenode=open(filename)

		j=1
		for row in filenode:

			i=i+1

			if i>100:
				
	
				sql="insert into "+tablename+"  values "+sql
				sql=sql.strip(',')+";"
			
		
				conn =  pymysql.connect(host='120.26.162.150',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306,charset='utf8')
				cursor=conn.cursor()
				cursor.execute(sql)
				conn.commit()
				conn.close()
				sql=""
				i=0
				j=j+1
				print("on "+str(j)+" commit")


			sql+="('"+str(row).replace('"','')replace(",","','")+"','"+time_tag+"'),"
 
		sql="insert into "+tablename+"  values "+sql
		sql=sql.strip(',')+";"
		#print(sql)
		
		conn = pymysql.connect(host='120.26.162.150',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306,charset='utf8')
		cursor=conn.cursor()
		cursor.execute(sql)
		conn.commit()
		conn.close()
	else:
		print(pwd+file+" not found")


# def test():
# 	word="""DROP TABLE IF EXISTS `login_detail`;

# 	CREATE TABLE `login_detail` (
#   `ad_id` varchar(45) DEFAULT NULL,
#   `game_id` varchar(45) DEFAULT NULL,
#   `platform` varchar(100) DEFAULT NULL,
#   `date` varchar(40) DEFAULT NULL,
#   `game_channel` varchar(100) DEFAULT NULL,
#   `agent` varchar(100) DEFAULT NULL,
#   `ad_Creative` varchar(100) DEFAULT NULL,"""
# 	# for x in xrange(0,730):
# 	# 	word+='  `money'+str(x)+'` varchar(30) DEFAULT NULL,'
# 	word+=" `accountid` varchar(100) DEFAULT NULL,`login_time` varchar(100) DEFAULT NULL,"
# 	word+="""`csv_update_time` varchar(45) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
# 	create_txt(word,"test")

def create_txt(word,name):
	file_object = open(os.getcwd()+'/'+name+'.txt','w')
	file_object.write(word)
	file_object.close()
	print("create_json_"+name)

def import_check(pwd,file):
	strlen=[]
	if  os.path.exists(pwd+file):
		print(pwd+file)
		filename=pwd+file
		filenode=open(filename)
		reader=csv.reader(filenode)
		for r in reader:
			strlen.append(len(r))
		if strlen.count(strlen[0])==len(strlen):
			print(file+" file format  ok")
		else:
			print(file+" file format  error, min is "+str(min(strlen))+"  max is "+str(max(strlen)))
	else:
		print(pwd+file+" not found")


if __name__ == '__main__':

#-2

		# import_check("/var/www/zilong_new/","market_login_log_2016-07-04~2017-05-15.csv")
		# import_check("/var/www/zilong_new/","market_logout_log_2016-07-04~2017-05-15.csv")
		# import_check("/var/www/zilong_new/","market_levelup_log_2016-07-04~2017-05-15.csv")
		# #import_check("/data1/bidata/1452827692979/","market_recharge_log_2016-07-04~2017-05-11.csv")



		# #import_csv("/var/www/zilong_new/","market_login_log_2016-07-04~2017-05-15.csv",'login_detail','1')
		# #import_csv("/var/www/zilong_new/","market_logout_log_2016-07-04~2017-05-15.csv",'logout_detail','1')
		# #import_csv("/var/www/zilong_new/","market_levelup_log_2016-07-04~2017-05-15.csv",'level_detail','1')
		# #import_csv("/data1/bidata/1452827692979/","market_recharge_log_2016-07-04~2017-05-11.csv",'recharge_detail','1')

		# import_csv("/data1/bidata/1452827692979/","market_recharge_log_2016-07-04~2017-05-11.csv",'recharge_detail','1')
		for x in xrange(2,22):
			#print("market_recharge_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-x)).strftime('%Y-%m-%d'))+".csv")
		#import_csv("/data1/bidata/1452827692979/","market_recharge_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'recharge_detail','1')
			import_csv("/data1/bidata/1452827692979/","market_login_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'login_detail','1')
			import_csv("/data1/bidata/1452827692979/","market_levelup_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'level_detail','1')
			import_csv("/data1/bidata/1452827692979/","market_logout_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'logout_detail','1')
			import_csv("/data1/bidata/1452827692979/","market_recharge_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'recharge_detail','1')
