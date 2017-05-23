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

def export_excel():
	sql="""

SELECT DATE,gamename,platform,channel_name,agent ,today_spend,today_budget,SUM(dis_spend) AS spend,staff FROM spend  WHERE

 (class_A IN ("投放")  AND gamename="1452827692979"  AND today_spend>0)  
 
AND staff='-'  
 
 GROUP BY DATE,gamename,platform,channel_name,agent

	"""

	conn =  pymysql.connect(host='120.26.162.150',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306)
	cur_1 = conn.cursor()
	cur_1.execute(sql)
	res=cur_1.fetchall()
	file_object = open(os.getcwd()+'/../../static/json/export_.csv','w')
	file_object.write("")
	file_object.close()
	file_object = open(os.getcwd()+'/../../static/json/export_.csv','a')
	word=""
	if len(res)>1:
		for r in res:
			for x in xrange(0,len(r)):
				word+=str(r[x])+"	"
			file_object.write(word+"\n")
			word=""
		file_object.close()














if __name__ == '__main__':
	export_excel()