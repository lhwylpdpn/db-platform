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
reload(sys)
sys.setdefaultencoding('utf-8')


def export():
	game_id=[]
	platform=[]
	date_=[]
	channel_name=[]
	staff=[]
	ad_click=[]
	ad_action=[]
	ad_action_new=[]
	ad_action_new_back=[]
	ad_account_new_double=[]
	ad_pay_account=[]
	ad_AU_5=[]
	ad_create_role=[]
	ad_role_31=[]
	dis_spend=[]
	agent=[]
	

	sql="""
		select  a.game_id,a.platform,a.date,a.game_channel,a.agent, b.staff,b.dis_spend,
		sum(ad_click) as ad_click,sum(ad_action) as ad_action,sum(ad_new) as ad_new ,sum(ad_new_back) as ad_new_back,sum(ad_new_double) as ad_new_double,sum(ad_pay_account) as ad_pay_account,sum(ad_AU_5) as ad_AU_5,sum(ad_create_role) as ad_create_role,sum(ad_role_31) as ad_role_31
 		from `ad_action_v2` a left join 
 		(select date,gamename,platform,class_A,channel_name,agent,staff,sum(dis_spend) as dis_spend from  spend group by date,gamename,platform,class_A,channel_name,agent,staff) b
 		 on a.date=b.date and a.`platform`=b.platform and a.`game_channel`=b.channel_name and a.`agent`=b.agent
   		group by game_channel,agent,game_id,a.platform,date;
 		"""
	conn =  pymysql.connect(host='120.26.162.150',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306)
	cur_1 = conn.cursor()
	cur_1.execute(sql)
	res=cur_1.fetchall()

	if len(res)>1:


		for r in res:
			game_id.append(r[0])
			platform.append(r[1])
			date_.append(r[2])
			channel_name.append(r[3])
			agent.append(r[4])
			staff.append(r[5])
			dis_spend.append(r[6])
			ad_click.append(r[7])
			ad_action.append(r[8])
			ad_action_new.append(r[9])
			ad_action_new_back.append(r[10])
			ad_account_new_double.append(r[11])
			ad_pay_account.append(r[12])
			ad_AU_5.append(r[13])
			ad_create_role.append(r[14])
			ad_role_31.append(r[15])


	word="["
	for i in xrange(0,len(res)):
		word=word+'{'
		word=word+'"game_id":"'+str(game_id[i])+'",'+'"platform":"'+str(platform[i])+'",'+'"date_":"'+str(date_[i])+'",'+'"channel_name":"'+str(channel_name[i])+'",'+'"agent":"'+str(agent[i])+'",'
		word=word+'"staff":"'+str(staff[i])+'",'+'"dis_spend":"'+str(dis_spend[i])+'",'+'"ad_click":"'+str(ad_click[i])+'",'+'"ad_action":"'+str(ad_action[i])+'",'+'"ad_action_new":"'+str(ad_action_new[i])+'",'
		word=word+'"ad_action_new_back":"'+str(ad_action_new_back[i])+'",'+'"ad_account_new_double":"'+str(ad_account_new_double[i])+'",'+'"ad_pay_account":"'+str(ad_pay_account[i])+'",'
		word=word+'"ad_AU_5":"'+str(ad_AU_5[i])+'",'
		word=word+'"ad_create_role":"'+str(ad_create_role[i])+'",'
		word=word+'"ad_role_31":"'+str(ad_role_31[i])+'"'
		
		if i==len(res)-1:
			word=word+'}'+'\n'
		else:
			word=word+'}'+',\n'
	word=word+']'


	create_json(word,"media_2")





def create_json(word,name):
	file_object = open(os.getcwd()+'/../../static/json/'+name+'.json','w')
	file_object.write(word)
	file_object.close()
	print("create_json_"+name)


if __name__ == '__main__':

		export()