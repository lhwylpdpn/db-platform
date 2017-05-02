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


def export_meida_A():
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
 		 and a.`game_id`=b.gamename
   		group by game_channel,agent,game_id,a.platform,date
   		order by date,game_channel,agent,game_id,a.platform;


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
		word=word+'"game_id":"'+str(game_id[i])+'",'+'"platform":"'+str(platform[i])+'",'+'"date_time":"'+str(date_[i])+'",'+'"channel_name":"'+str(channel_name[i])+'",'+'"agent":"'+str(agent[i])+'",'
		word=word+'"staff":"'+str(staff[i])+'",'+'"dis_spend":"'+str(dis_spend[i])+'",'+'"ad_click":"'+str(ad_click[i])+'",'+'"ad_action":"'+str(ad_action[i])+'",'+'"ad_action_new":"'+str(ad_action_new[i])+'",'
		word=word+'"ad_action_new_back":"'+str(ad_action_new_back[i])+'",'+'"ad_account_new_double":"'+str(ad_account_new_double[i])+'",'+'"ad_login_count":"'+str(ad_pay_account[i])+'",'
		word=word+'"ad_AU_5":"'+str(ad_AU_5[i])+'",'
		word=word+'"ad_create_role":"'+str(ad_create_role[i])+'",'
		word=word+'"ad_role_31":"'+str(ad_role_31[i])+'"'
		
		if i==len(res)-1:
			word=word+'}'+'\n'
		else:
			word=word+'}'+',\n'
	word=word+']'

	word=word.replace('"None"','""')
	word=word.replace('"staff":""','"staff":"weizhi_none"')
	create_json(word,"media_2")




def export_meida_B():#媒体分析 留存内容
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
	re_0=[]
	re_1=[]
	re_2=[]
	re_3=[]
	re_4=[]
	re_5=[]
	re_6=[]

	sql="""
		select  a.game_id,a.platform,a.date,a.game_channel,a.agent, b.staff,
		case when  a.date<=date_sub(curdate(),interval 1 day) then sum(retention0)   else null end  as retention0,
		case when  a.date<=date_sub(curdate(),interval 2 day) then sum(retention1) else null end  as retention1,
		case when  a.date<=date_sub(curdate(),interval 3 day) then sum(retention2) else null end as retention2,
		case when  a.date<=date_sub(curdate(),interval 4 day) then sum(retention3) else null end  as retention3,
		case when  a.date<=date_sub(curdate(),interval 5 day) then sum(retention4) else null end as retention4,
		case when  a.date<=date_sub(curdate(),interval 6 day) then sum(retention5) else null end as retention5,
		case when  a.date<=date_sub(curdate(),interval 7 day) then sum(retention6) else null end  as retention6
 		from `ad_retention_v2` a 
 		
 		
  		left join 
 		(select date,gamename,platform,class_A,channel_name,agent,staff,sum(dis_spend) as dis_spend from  spend group by date,gamename,platform,class_A,channel_name,agent,staff) b
 		 on a.date=b.date and a.`platform`=b.platform and a.`game_channel`=b.channel_name and a.`agent`=b.agent
 		 and a.`game_id`=b.gamename
   		group by game_channel,agent,game_id,a.platform,date
		order by date,game_channel,agent,game_id,a.platform;
 			
 		
 		

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
			re_0.append(r[6])
			re_1.append(r[7])
			re_2.append(r[8])
			re_3.append(r[9])
			re_4.append(r[10])
			re_5.append(r[11])
			re_6.append(r[12])


	word="["
	for i in xrange(0,len(res)):
		word=word+'{'
		word=word+'"game_id":"'+str(game_id[i])+'",'+'"platform":"'+str(platform[i])+'",'+'"date_":"'+str(date_[i])+'",'+'"channel_name":"'+str(channel_name[i])+'",'+'"agent":"'+str(agent[i])+'",'
		word=word+'"staff":"'+str(staff[i])+'",'
		word=word+'"re_0":"'+str(re_0[i])+'",'
		word=word+'"re_1":"'+str(re_1[i])+'",'
		word=word+'"re_2":"'+str(re_2[i])+'",'
		word=word+'"re_3":"'+str(re_3[i])+'",'
		word=word+'"re_4":"'+str(re_4[i])+'",'
		word=word+'"re_5":"'+str(re_5[i])+'",'
		word=word+'"re_6":"'+str(re_6[i])+'"'
		
		if i==len(res)-1:
			word=word+'}'+'\n'
		else:
			word=word+'}'+',\n'
	word=word+']'
	word=word.replace('"None"','""')
	word=word.replace('"staff":""','"staff":"weizhi_none"')
	create_json(word,"media_3")


def export_meida_C():#媒体分析 留存内容
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
	re_0=[]
	re_1=[]
	re_2=[]
	re_3=[]
	re_4=[]
	re_5=[]
	re_6=[]
	online0=[]
	online1=[]
	online2=[]
	online3=[]
	online4=[]
	online5=[]
	online6=[]
	sql="""
		SELECT a.game_id,a.platform,a.date,a.game_channel,a.agent,b.staff,
		a.retention0,
		a.retention1,
		a.retention2,
		a.retention3,
		a.retention4,
		a.retention5,
		a.retention6,
		a.online_avg0,
		a.online_avg1,
		a.online_avg2,
		a.online_avg3,
		a.online_avg4,
		a.online_avg5,
		a.online_avg6

		 FROM (SELECT  a.game_id,a.platform,a.date,a.game_channel,a.agent,
		SUM(retention0) AS retention0,  
		SUM(retention1) AS retention1,  
		SUM(retention2) AS retention2,  
		SUM(retention3) AS retention3,  
		SUM(retention4) AS retention4,  
		SUM(retention5) AS retention5,
		SUM(retention6) AS retention6,
		SUM(online_avg0) AS online_avg0,  
		SUM(online_avg1) AS online_avg1,  
		SUM(online_avg2) AS online_avg2,  
		SUM(online_avg3) AS online_avg3,  
		SUM(online_avg4) AS online_avg4,  
		SUM(online_avg5) AS online_avg5,
		SUM(online_avg6) AS online_avg6
    
		FROM `ad_onlinetime_v2` b
		RIGHT JOIN 
		ad_retention_v2 a
		ON a.date=b.date AND a.`platform`=b.platform AND a.`game_channel`=b.game_channel AND a.`agent`=b.agent
		AND a.`game_id`=b.game_id
		GROUP BY a.game_channel,a.agent,a.game_id,a.platform,a.DATE) a

		LEFT JOIN 
		(SELECT DATE,gamename,platform,class_A,channel_name,agent,staff,SUM(dis_spend) AS dis_spend FROM  spend GROUP BY DATE,gamename,platform,class_A,channel_name,agent,staff) b
		 ON a.date=b.date AND a.`platform`=b.platform AND a.`game_channel`=b.channel_name AND a.`agent`=b.agent
		 AND a.`game_id`=b.gamename
		GROUP BY a.game_channel,a.agent,a.game_id,a.platform,a.DATE
		ORDER BY a.DATE,a.game_channel,a.agent,a.game_id,a.platform;


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
			re_0.append(r[6])
			re_1.append(r[7])
			re_2.append(r[8])
			re_3.append(r[9])
			re_4.append(r[10])
			re_5.append(r[11])
			re_6.append(r[12])
			online0.append(r[13])
			online1.append(r[14])
			online2.append(r[15])
			online3.append(r[16])
			online4.append(r[17])
			online5.append(r[18])
			online6.append(r[19])


	word="["
	for i in xrange(0,len(res)):
		word=word+'{'
		word=word+'"game_id":"'+str(game_id[i])+'",'+'"platform":"'+str(platform[i])+'",'+'"date_":"'+str(date_[i])+'",'+'"channel_name":"'+str(channel_name[i])+'",'+'"agent":"'+str(agent[i])+'",'
		word=word+'"staff":"'+str(staff[i])+'",'
		word=word+'"re_0":"'+str(re_0[i])+'",'
		word=word+'"re_1":"'+str(re_1[i])+'",'
		word=word+'"re_2":"'+str(re_2[i])+'",'
		word=word+'"re_3":"'+str(re_3[i])+'",'
		word=word+'"re_4":"'+str(re_4[i])+'",'
		word=word+'"re_5":"'+str(re_5[i])+'",'
		word=word+'"re_6":"'+str(re_6[i])+'",'
		word=word+'"online0":"'+str(online0[i])+'",'
		word=word+'"online1":"'+str(online1[i])+'",'
		word=word+'"online2":"'+str(online2[i])+'",'
		word=word+'"online3":"'+str(online3[i])+'",'
		word=word+'"online4":"'+str(online4[i])+'",'
		word=word+'"online5":"'+str(online5[i])+'",'
		word=word+'"online6":"'+str(online6[i])+'"'		
		
		if i==len(res)-1:
			word=word+'}'+'\n'
		else:
			word=word+'}'+',\n'
	word=word+']'
	word=word.replace('"None"','""')
	word=word.replace('"staff":""','"staff":"weizhi_none"')
	create_json(word,"media_4")

def export_meida_TJ():#媒体分析 留存内容
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
	re_0=[]
	re_1=[]
	re_2=[]
	re_3=[]
	re_4=[]
	re_5=[]
	re_6=[]
	online0=[]
	online1=[]
	online2=[]
	online3=[]
	online4=[]
	online5=[]
	online6=[]
	sql="""
	SELECT a.`game_id`,a.`platform`,a.`game_channel`,a.`agent`,b.`staff` FROM (SELECT a.`game_id`,a.`platform`,a.`game_channel`,a.`agent` FROM `ad_action_v2`  a 
GROUP BY a.`game_id`,a.`platform`,a.`game_channel`,a.`agent` ) a , spend b WHERE   a.game_id=b.gamename
AND a.platform=b.platform AND a.game_channel=b.channel_name AND a.agent=b.agent
GROUP BY a.`game_id`,a.`platform`,a.`game_channel`,a.`agent`

 		"""
	conn =  pymysql.connect(host='120.26.162.150',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306)
	cur_1 = conn.cursor()
	cur_1.execute(sql)
	res=cur_1.fetchall()

	if len(res)>1:


		for r in res:
			game_id.append(r[0])
			platform.append(r[1])
			channel_name.append(r[2])
			agent.append(r[3])
			staff.append(r[4])



	word="["
	for i in xrange(0,len(res)):
		word=word+'{'
		word=word+'"game_id":"'+str(game_id[i])+'",'+'"platform":"'+str(platform[i])+'",'+'"channel_name":"'+str(channel_name[i])+'",'+'"agent":"'+str(agent[i])+'",'
		word=word+'"staff":"'+str(staff[i])+'"'

		
		if i==len(res)-1:
			word=word+'}'+'\n'
		else:
			word=word+'}'+',\n'
	word=word+']'
	word=word.replace('"None"','""')
	word=word.replace('"staff":"-"','"staff":"weizhi_none"')
	create_json(word,"media_TJ")


def create_json(word,name):
	file_object = open(os.getcwd()+'/../../static/json/'+name+'.json','w')
	file_object.write(word)
	file_object.close()
	print("create_json_"+name)


if __name__ == '__main__':
		#export_meida_A()
#
		#export_meida_B()

		#export_meida_C()

		export_meida_TJ()