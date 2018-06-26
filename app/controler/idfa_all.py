#!/usr/bin/python
# -*- coding: UTF-8 -*- 



import pymysql
import os
import sys
import time
import csv
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')
def import_csv():
	test = []
	pwd="/data1/bidata/1452827692979/"
	test= os.listdir(pwd)
	newlist=[]
	statinfo=[]
	for names in test:

		if names.endswith(".csv"):
			#statinfo.append(os.stat(os.getcwd()+"/src/"+names).st_ctime)
			newlist.append(names)
	for r in newlist:
		if  not r.find("Daily_xzff_detail_2016-07-01_2017-04-11"):
			filename="/data1/bidata/1452827692979/"+r
			filenode=open(filename)
			reader=filenode.readlines()
			time_tag=str(datetime.datetime.now().strftime('%Y-%m-%d'))
			sql="delete from ad_detail_IDFA  where csv_update_time='"+time_tag+"';"
			cur_1.execute(sql)
			conn.commit()
			sql=""
			i=0
			for row in reader:
				i=i+1
				if i>50000:
					sql="insert into ad_detail_IDFA values "+sql
					sql=sql.strip(',')+";"
					cur_1.execute(sql)
					conn.commit()
					print(i,"执行成功")
					sql=""
					i=0				
				sql+="('"+row.replace(",","','")+"','"+time_tag+"'),"
			sql="insert into ad_detail_IDFA values "+sql
			sql=sql.strip(',')+";"
			cur_1.execute(sql)
			create_json(sql,"sql")
				#time.sleep(10)
			
	print("6sql ok")
	return sql
def create_json(word,name):
	file_object = open(os.getcwd()+'/'+name+'.json','w')
	file_object.write(word)
	file_object.close()
	print("create_json_"+name)

if __name__ == '__main__':

	conn=pymysql.connect(host='localhost',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306)
	cur_1=conn.cursor()
	import_csv()

	cur_1.close()
	conn.commit()
	conn.close()


