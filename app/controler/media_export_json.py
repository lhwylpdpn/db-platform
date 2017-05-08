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
	ad_pay_new=[]
	ad_pay_back=[]
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
GROUP BY a.`game_id`,a.`platform`,a.`game_channel`,a.`agent`,b.`staff`

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

def export_meida_all():#媒体概览
	game_id=[]
	platform=[]
	date_=[]
	channel_name=[]
	staff=[]
	ad_click=[]
	ad_action=[]
	ad_new=[]
	ad_new_back=[]
	ad_pay_new=[]
	ad_pay_back=[]
	ad_AU_5=[]
	liushui=[]
	ad_role_31=[]
	spend=[]
	agent=[]
	r1=[]
	r29=[]
	r6=[]
	r_all=[]
	sql="""

SELECT a.gamename,a.platform,a.date,a.channel_name,a.agent,
CASE WHEN ad_click >0 THEN ad_click ELSE 0 END AS ad_click,
CASE WHEN ad_action >0 THEN ad_action  ELSE 0 END AS ad_action ,
CASE WHEN ad_new >0 THEN ad_new  ELSE 0 END AS ad_new ,
CASE WHEN ad_new_back >0 THEN ad_new_back ELSE 0 END AS ad_new_back ,
CASE WHEN ad_pay_new >0 THEN ad_pay_new  ELSE 0 END AS ad_pay_new ,
CASE WHEN ad_pay_back >0 THEN ad_pay_back ELSE 0 END AS ad_pay_back ,
CASE WHEN ad_role_31 >0 THEN ad_role_31  ELSE 0 END AS ad_role_31 ,
CASE WHEN ad_AU_5  >0 THEN ad_AU_5  ELSE 0 END AS ad_AU_5 ,
CASE WHEN liushui  >0 THEN liushui  ELSE 0 END AS liushui  ,
CASE WHEN spend >0 THEN spend  ELSE 0 END AS spend ,
 staff ,
CASE WHEN retention1 >0 THEN retention1  ELSE 0 END AS retention1,
CASE WHEN retention6 >0 THEN retention6  ELSE 0 END AS retention6,
CASE WHEN retention29 >0 THEN retention29 ELSE 0 END AS retention29,
CASE WHEN huoyue >0 THEN huoyue ELSE 0 END AS huoyue 
FROM 
(
SELECT a.gamename,a.platform,a.date,a.channel_name,a.agent,c.ad_click,c.ad_action,c.ad_new,c.ad_new_back,c.ad_pay_new,c.ad_pay_back,c.ad_role_31,c.ad_AU_5 ,b.liushui ,a.spend,a.staff
,d.retention1,d.retention6,d.retention29,e.huoyue
FROM (SELECT DATE,gamename,platform,channel_name,agent ,SUM(dis_spend) AS spend,staff FROM spend  where class_A="投放" and gamename="1452827692979"   and platform="IOS正版" and dis_spend>0 GROUP BY DATE,gamename,platform,channel_name,agent


 ) a
LEFT JOIN 
(
 SELECT game_id,platform,DATE,game_channel,agent ,
 SUM(GREATEST
(money0,
money1,
money2,
money3,
money4,
money5,
money6,
money7,
money8,
money9,
money10,
money11,
money12,
money13,
money14,
money15,
money16,
money17,
money18,
money19,
money20,
money21,
money22,
money23,
money24,
money25,
money26,
money27,
money28,
money29,
money30,
money31,
money32,
money33,
money34,
money35,
money36,
money37,
money38,
money39,
money40,
money41,
money42,
money43,
money44,
money45,
money46,
money47,
money48,
money49,
money50,
money51,
money52,
money53,
money54,
money55,
money56,
money57,
money58,
money59,
money60,
money61,
money62,
money63,
money64,
money65,
money66,
money67,
money68,
money69,
money70,
money71,
money72,
money73,
money74,
money75,
money76,
money77,
money78,
money79,
money80,
money81,
money82,
money83,
money84,
money85,
money86,
money87,
money88,
money89,
money90,
money91,
money92,
money93,
money94,
money95,
money96,
money97,
money98,
money99,
money100,
money101,
money102,
money103,
money104,
money105,
money106,
money107,
money108,
money109,
money110,
money111,
money112,
money113,
money114,
money115,
money116,
money117,
money118,
money119,
money120,
money121,
money122,
money123,
money124,
money125,
money126,
money127,
money128,
money129,
money130,
money131,
money132,
money133,
money134,
money135,
money136,
money137,
money138,
money139,
money140,
money141,
money142,
money143,
money144,
money145,
money146,
money147,
money148,
money149,
money150,
money151,
money152,
money153,
money154,
money155,
money156,
money157,
money158,
money159,
money160,
money161,
money162,
money163,
money164,
money165,
money166,
money167,
money168,
money169,
money170,
money171,
money172,
money173,
money174,
money175,
money176,
money177,
money178,
money179,
money180,
money181,
money182,
money183,
money184,
money185,
money186,
money187,
money188,
money189,
money190,
money191,
money192,
money193,
money194,
money195,
money196,
money197,
money198,
money199,
money200,
money201,
money202,
money203,
money204,
money205,
money206,
money207,
money208,
money209,
money210,
money211,
money212,
money213,
money214,
money215,
money216,
money217,
money218,
money219,
money220,
money221,
money222,
money223,
money224,
money225,
money226,
money227,
money228,
money229,
money230,
money231,
money232,
money233,
money234,
money235,
money236,
money237,
money238,
money239,
money240,
money241,
money242,
money243,
money244,
money245,
money246,
money247,
money248,
money249,
money250,
money251,
money252,
money253,
money254,
money255,
money256,
money257,
money258,
money259,
money260,
money261,
money262,
money263,
money264,
money265,
money266,
money267,
money268,
money269,
money270,
money271,
money272,
money273,
money274,
money275,
money276,
money277,
money278,
money279,
money280,
money281,
money282,
money283,
money284,
money285,
money286,
money287,
money288,
money289,
money290,
money291,
money292,
money293,
money294,
money295,
money296,
money297,
money298,
money299,
money300,
money301,
money302,
money303,
money304,
money305,
money306,
money307,
money308,
money309,
money310,
money311,
money312,
money313,
money314,
money315,
money316,
money317,
money318,
money319,
money320,
money321,
money322,
money323,
money324,
money325,
money326,
money327,
money328,
money329,
money330,
money331,
money332,
money333,
money334,
money335,
money336,
money337,
money338,
money339,
money340,
money341,
money342,
money343,
money344,
money345,
money346,
money347,
money348,
money349,
money350,
money351,
money352,
money353,
money354,
money355,
money356,
money357,
money358,
money359,
money360,
money361,
money362,
money363,
money364,
money365,
money366,
money367,
money368,
money369,
money370,
money371,
money372,
money373,
money374,
money375,
money376,
money377,
money378,
money379,
money380,
money381,
money382,
money383,
money384,
money385,
money386,
money387,
money388,
money389,
money390,
money391,
money392,
money393,
money394,
money395,
money396,
money397,
money398,
money399,
money400,
money401,
money402,
money403,
money404,
money405,
money406,
money407,
money408,
money409,
money410,
money411,
money412,
money413,
money414,
money415,
money416,
money417,
money418,
money419,
money420,
money421,
money422,
money423,
money424,
money425,
money426,
money427,
money428,
money429,
money430,
money431,
money432,
money433,
money434,
money435,
money436,
money437,
money438,
money439,
money440,
money441,
money442,
money443,
money444,
money445,
money446,
money447,
money448,
money449,
money450,
money451,
money452,
money453,
money454,
money455,
money456,
money457,
money458,
money459,
money460,
money461,
money462,
money463,
money464,
money465,
money466,
money467,
money468,
money469,
money470,
money471,
money472,
money473,
money474,
money475,
money476,
money477,
money478,
money479,
money480,
money481,
money482,
money483,
money484,
money485,
money486,
money487,
money488,
money489,
money490,
money491,
money492,
money493,
money494,
money495,
money496,
money497,
money498,
money499,
money500,
money501,
money502,
money503,
money504,
money505,
money506,
money507,
money508,
money509,
money510,
money511,
money512,
money513,
money514,
money515,
money516,
money517,
money518,
money519,
money520,
money521,
money522,
money523,
money524,
money525,
money526,
money527,
money528,
money529,
money530,
money531,
money532,
money533,
money534,
money535,
money536,
money537,
money538,
money539,
money540,
money541,
money542,
money543,
money544,
money545,
money546,
money547,
money548,
money549,
money550,
money551,
money552,
money553,
money554,
money555,
money556,
money557,
money558,
money559,
money560,
money561,
money562,
money563,
money564,
money565,
money566,
money567,
money568,
money569,
money570,
money571,
money572,
money573,
money574,
money575,
money576,
money577,
money578,
money579,
money580,
money581,
money582,
money583,
money584,
money585,
money586,
money587,
money588,
money589,
money590,
money591,
money592,
money593,
money594,
money595,
money596,
money597,
money598,
money599,
money600,
money601,
money602,
money603,
money604,
money605,
money606,
money607,
money608,
money609,
money610,
money611,
money612,
money613,
money614,
money615,
money616,
money617,
money618,
money619,
money620,
money621,
money622,
money623,
money624,
money625,
money626,
money627,
money628,
money629,
money630,
money631,
money632,
money633,
money634,
money635,
money636,
money637,
money638,
money639,
money640,
money641,
money642,
money643,
money644,
money645,
money646,
money647,
money648,
money649,
money650,
money651,
money652,
money653,
money654,
money655,
money656,
money657,
money658,
money659,
money660,
money661,
money662,
money663,
money664,
money665,
money666,
money667,
money668,
money669,
money670,
money671,
money672,
money673,
money674,
money675,
money676,
money677,
money678,
money679,
money680,
money681,
money682,
money683,
money684,
money685,
money686,
money687,
money688,
money689,
money690,
money691,
money692,
money693,
money694,
money695,
money696,
money697,
money698,
money699,
money700,
money701,
money702,
money703,
money704,
money705,
money706,
money707,
money708,
money709,
money710,
money711,
money712,
money713,
money714,
money715,
money716,
money717,
money718,
money719,
money720,
money721,
money722,
money723,
money724,
money725,
money726,
money727,
money728,
money729)) AS liushui FROM `ad_re_money_v2`  GROUP BY game_id,platform,DATE,game_channel,agent) b
ON a.gamename=b.game_id AND a.date=b.date  AND  a.channel_name=b.game_channel AND a.agent =b.agent AND a.platform=b.platform
LEFT JOIN 

(
SELECT game_id,platform,DATE,game_channel,agent,SUM(ad_click) AS ad_click ,SUM(ad_action) AS ad_action ,SUM(ad_new) AS ad_new,
SUM(ad_new_back) AS ad_new_back ,SUM(ad_pay_new) AS ad_pay_new ,SUM(ad_pay_back) AS ad_pay_back  ,SUM(ad_role_31) AS ad_role_31  ,SUM(ad_AU_5) AS ad_AU_5
 FROM `ad_action_v2` GROUP BY game_id,platform,DATE,game_channel,agent
 
) c
ON a.gamename=c.game_id AND a.date=c.date  AND  a.channel_name=c.game_channel AND a.agent =c.agent  AND a.platform=c.platform
LEFT JOIN
(

SELECT DATE,game_id,platform,game_channel,agent,  SUM(retention1)  AS retention1 ,SUM(retention6) AS retention6,SUM(retention29) AS retention29 FROM `ad_retention_v2` 
GROUP BY DATE,game_id,platform,game_channel,agent 
) d

ON  a.gamename=d.game_id AND a.date=d.date  AND  a.channel_name=d.game_channel AND a.agent =d.agent  AND a.platform=d.platform
left join 
(

 SELECT game_id,platform,DATE,game_channel,agent ,
 SUM(GREATEST
(retention0,
retention1,
retention2,
retention3,
retention4,
retention5,
retention6,
retention7,
retention8,
retention9,
retention10,
retention11,
retention12,
retention13,
retention14,
retention15,
retention16,
retention17,
retention18,
retention19,
retention20,
retention21,
retention22,
retention23,
retention24,
retention25,
retention26,
retention27,
retention28,
retention29,
retention30,
retention31,
retention32,
retention33,
retention34,
retention35,
retention36,
retention37,
retention38,
retention39,
retention40,
retention41,
retention42,
retention43,
retention44,
retention45,
retention46,
retention47,
retention48,
retention49,
retention50,
retention51,
retention52,
retention53,
retention54,
retention55,
retention56,
retention57,
retention58,
retention59,
retention60,
retention61,
retention62,
retention63,
retention64,
retention65,
retention66,
retention67,
retention68,
retention69,
retention70,
retention71,
retention72,
retention73,
retention74,
retention75,
retention76,
retention77,
retention78,
retention79,
retention80,
retention81,
retention82,
retention83,
retention84,
retention85,
retention86,
retention87,
retention88,
retention89,
retention90,
retention91,
retention92,
retention93,
retention94,
retention95,
retention96,
retention97,
retention98,
retention99,
retention100,
retention101,
retention102,
retention103,
retention104,
retention105,
retention106,
retention107,
retention108,
retention109,
retention110,
retention111,
retention112,
retention113,
retention114,
retention115,
retention116,
retention117,
retention118,
retention119,
retention120,
retention121,
retention122,
retention123,
retention124,
retention125,
retention126,
retention127,
retention128,
retention129,
retention130,
retention131,
retention132,
retention133,
retention134,
retention135,
retention136,
retention137,
retention138,
retention139,
retention140,
retention141,
retention142,
retention143,
retention144,
retention145,
retention146,
retention147,
retention148,
retention149,
retention150,
retention151,
retention152,
retention153,
retention154,
retention155,
retention156,
retention157,
retention158,
retention159,
retention160,
retention161,
retention162,
retention163,
retention164,
retention165,
retention166,
retention167,
retention168,
retention169,
retention170,
retention171,
retention172,
retention173,
retention174,
retention175,
retention176,
retention177,
retention178,
retention179,
retention180,
retention181,
retention182,
retention183,
retention184,
retention185,
retention186,
retention187,
retention188,
retention189,
retention190,
retention191,
retention192,
retention193,
retention194,
retention195,
retention196,
retention197,
retention198,
retention199,
retention200,
retention201,
retention202,
retention203,
retention204,
retention205,
retention206,
retention207,
retention208,
retention209,
retention210,
retention211,
retention212,
retention213,
retention214,
retention215,
retention216,
retention217,
retention218,
retention219,
retention220,
retention221,
retention222,
retention223,
retention224,
retention225,
retention226,
retention227,
retention228,
retention229,
retention230,
retention231,
retention232,
retention233,
retention234,
retention235,
retention236,
retention237,
retention238,
retention239,
retention240,
retention241,
retention242,
retention243,
retention244,
retention245,
retention246,
retention247,
retention248,
retention249,
retention250,
retention251,
retention252,
retention253,
retention254,
retention255,
retention256,
retention257,
retention258,
retention259,
retention260,
retention261,
retention262,
retention263,
retention264,
retention265,
retention266,
retention267,
retention268,
retention269,
retention270,
retention271,
retention272,
retention273,
retention274,
retention275,
retention276,
retention277,
retention278,
retention279,
retention280,
retention281,
retention282,
retention283,
retention284,
retention285,
retention286,
retention287,
retention288,
retention289,
retention290,
retention291,
retention292,
retention293,
retention294,
retention295,
retention296,
retention297,
retention298,
retention299,
retention300,
retention301,
retention302,
retention303,
retention304,
retention305,
retention306,
retention307,
retention308,
retention309,
retention310,
retention311,
retention312,
retention313,
retention314,
retention315,
retention316,
retention317,
retention318,
retention319,
retention320,
retention321,
retention322,
retention323,
retention324,
retention325,
retention326,
retention327,
retention328,
retention329,
retention330,
retention331,
retention332,
retention333,
retention334,
retention335,
retention336,
retention337,
retention338,
retention339,
retention340,
retention341,
retention342,
retention343,
retention344,
retention345,
retention346,
retention347,
retention348,
retention349,
retention350,
retention351,
retention352,
retention353,
retention354,
retention355,
retention356,
retention357,
retention358,
retention359,
retention360,
retention361,
retention362,
retention363,
retention364,
retention365,
retention366,
retention367,
retention368,
retention369,
retention370,
retention371,
retention372,
retention373,
retention374,
retention375,
retention376,
retention377,
retention378,
retention379,
retention380,
retention381,
retention382,
retention383,
retention384,
retention385,
retention386,
retention387,
retention388,
retention389,
retention390,
retention391,
retention392,
retention393,
retention394,
retention395,
retention396,
retention397,
retention398,
retention399,
retention400,
retention401,
retention402,
retention403,
retention404,
retention405,
retention406,
retention407,
retention408,
retention409,
retention410,
retention411,
retention412,
retention413,
retention414,
retention415,
retention416,
retention417,
retention418,
retention419,
retention420,
retention421,
retention422,
retention423,
retention424,
retention425,
retention426,
retention427,
retention428,
retention429,
retention430,
retention431,
retention432,
retention433,
retention434,
retention435,
retention436,
retention437,
retention438,
retention439,
retention440,
retention441,
retention442,
retention443,
retention444,
retention445,
retention446,
retention447,
retention448,
retention449,
retention450,
retention451,
retention452,
retention453,
retention454,
retention455,
retention456,
retention457,
retention458,
retention459,
retention460,
retention461,
retention462,
retention463,
retention464,
retention465,
retention466,
retention467,
retention468,
retention469,
retention470,
retention471,
retention472,
retention473,
retention474,
retention475,
retention476,
retention477,
retention478,
retention479,
retention480,
retention481,
retention482,
retention483,
retention484,
retention485,
retention486,
retention487,
retention488,
retention489,
retention490,
retention491,
retention492,
retention493,
retention494,
retention495,
retention496,
retention497,
retention498,
retention499,
retention500,
retention501,
retention502,
retention503,
retention504,
retention505,
retention506,
retention507,
retention508,
retention509,
retention510,
retention511,
retention512,
retention513,
retention514,
retention515,
retention516,
retention517,
retention518,
retention519,
retention520,
retention521,
retention522,
retention523,
retention524,
retention525,
retention526,
retention527,
retention528,
retention529,
retention530,
retention531,
retention532,
retention533,
retention534,
retention535,
retention536,
retention537,
retention538,
retention539,
retention540,
retention541,
retention542,
retention543,
retention544,
retention545,
retention546,
retention547,
retention548,
retention549,
retention550,
retention551,
retention552,
retention553,
retention554,
retention555,
retention556,
retention557,
retention558,
retention559,
retention560,
retention561,
retention562,
retention563,
retention564,
retention565,
retention566,
retention567,
retention568,
retention569,
retention570,
retention571,
retention572,
retention573,
retention574,
retention575,
retention576,
retention577,
retention578,
retention579,
retention580,
retention581,
retention582,
retention583,
retention584,
retention585,
retention586,
retention587,
retention588,
retention589,
retention590,
retention591,
retention592,
retention593,
retention594,
retention595,
retention596,
retention597,
retention598,
retention599,
retention600,
retention601,
retention602,
retention603,
retention604,
retention605,
retention606,
retention607,
retention608,
retention609,
retention610,
retention611,
retention612,
retention613,
retention614,
retention615,
retention616,
retention617,
retention618,
retention619,
retention620,
retention621,
retention622,
retention623,
retention624,
retention625,
retention626,
retention627,
retention628,
retention629,
retention630,
retention631,
retention632,
retention633,
retention634,
retention635,
retention636,
retention637,
retention638,
retention639,
retention640,
retention641,
retention642,
retention643,
retention644,
retention645,
retention646,
retention647,
retention648,
retention649,
retention650,
retention651,
retention652,
retention653,
retention654,
retention655,
retention656,
retention657,
retention658,
retention659,
retention660,
retention661,
retention662,
retention663,
retention664,
retention665,
retention666,
retention667,
retention668,
retention669,
retention670,
retention671,
retention672,
retention673,
retention674,
retention675,
retention676,
retention677,
retention678,
retention679,
retention680,
retention681,
retention682,
retention683,
retention684,
retention685,
retention686,
retention687,
retention688,
retention689,
retention690,
retention691,
retention692,
retention693,
retention694,
retention695,
retention696,
retention697,
retention698,
retention699,
retention700,
retention701,
retention702,
retention703,
retention704,
retention705,
retention706,
retention707,
retention708,
retention709,
retention710,
retention711,
retention712,
retention713,
retention714,
retention715,
retention716,
retention717,
retention718,
retention719,
retention720,
retention721,
retention722,
retention723,
retention724,
retention725,
retention726,
retention727,
retention728,
retention729)) AS huoyue FROM `ad_retention_v2`  GROUP BY game_id,platform,DATE,game_channel,agent


)e
ON  a.gamename=e.game_id AND a.date=e.date  AND  a.channel_name=e.game_channel AND a.agent =e.agent  AND a.platform=e.platform

ORDER BY a.gamename,a.date,a.platform,a.channel_name,a.agent

) a 




 		"""


	conn =  pymysql.connect(host='120.26.162.150',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306)
	cur_1 = conn.cursor()
	cur_1.execute(sql)
	res=cur_1.fetchall()
	print(len(res))
	if len(res)>=1:


		for r in res:
			game_id.append(r[0])
			platform.append(r[1])
			date_.append(r[2])
			channel_name.append(r[3])
			agent.append(r[4])
			ad_click.append(r[5])
			ad_action.append(r[6])
			ad_new.append(r[7])
			ad_new_back.append(r[8])
			ad_pay_new.append(r[9])
			ad_pay_back.append(r[10])
			ad_role_31.append(r[11])
			ad_AU_5.append(r[12])
			liushui.append(r[13])
			spend.append(r[14])
			staff.append(r[15])
			r1.append(r[16])
			r6.append(r[17])
			r29.append(r[18])
		#	r_all.append(r[19])



	word="["
	for i in xrange(0,len(res)):
 
		word=word+'{'
		word=word+'"game_id":"'+str(game_id[i])+'",'+'"platform":"'+str(platform[i])+'",'+'"channel_name":"'+str(channel_name[i])+'",'+'"agent":"'+str(agent[i])+'",'+'"staff":"'+str(staff[i])+'",'
		word=word+'"date_time":"'+str(date_[i])+'",'+'"ad_click":"'+str(ad_click[i])+'",'+'"ad_action":"'+str(ad_action[i])+'",'+'"double_new":"'+str(ad_new[i])+'",'+'"back_user":"'+str(ad_new_back[i])+'",'
		word=word+'"ad_action_new":"'+str(int(ad_new_back[i])+int(ad_new[i]))+'",'+'"ad_account_new":"'+str(int(ad_new_back[i])+int(ad_new[i]))+'",'+'"paid_account":"'+str(int(ad_pay_new[i])+int(ad_pay_back[i]))+'",'+'"spend":"'+str(spend[i])+'",'+'"cumulative_flow":"'+str(liushui[i])+'",'+'"dis":"'+str(48.02)+'",'
		if  liushui[i]:
			word=word+'"cumulative_money":"'+str(round(float(liushui[i])*48.02/100,2)) +'",'
		else:
			word=word+'"cumulative_money":"None",'
		word=word+'"r1":"'+str(r1[i])+'",'+'"r6":"'+str(r6[i])+'",'+'"r29":"'+str(r29[i])+'",'+'"ad_role_31":"'+str(ad_role_31[i])+'",'+'"ad_AU_5":"'+str(ad_AU_5[i])+'"}'+',\n'
	word=word[0:-2]
	word=word+']'
	word=word.replace('"None"','""')
	word=word.replace('"staff":"-"','"staff":"weizhi_none"')

	create_json(word,"media_1")
def create_json(word,name):
	file_object = open(os.getcwd()+'/../../static/json/'+name+'.json','w')
	file_object.write(word)
	file_object.close()
	print("create_json_"+name)


if __name__ == '__main__':
		print time.asctime(time.localtime(time.time()))
		export_meida_all()
		print time.asctime(time.localtime(time.time()))
		export_meida_TJ()