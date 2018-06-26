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

SELECT a.*,b.* ,c.*,d.*
FROM 
(
SELECT  platform,game_channel,agent,
SUM(ad_click),
SUM(ad_action),
SUM(ad_new),
SUM(ad_pay_new),
SUM(ad_AU_5),
SUM(ad_create_role),
SUM(ad_role_31)


 FROM `ad_action_v2`
 WHERE DATE<'2017-04-20'
 GROUP BY  platform,game_channel,agent

) a
LEFT JOIN 

 (SELECT  platform,game_channel,agent,
SUM(retention0),
SUM(retention1),
SUM(retention2),
SUM(retention3),
SUM(retention4),
SUM(retention5),
SUM(retention6),
SUM(retention7),
SUM(retention8),
SUM(retention9),
SUM(retention10),
SUM(retention11),
SUM(retention12),
SUM(retention13),
SUM(retention14),
SUM(retention15),
SUM(retention16),
SUM(retention17),
SUM(retention18),
SUM(retention19),
SUM(retention20),
SUM(retention21),
SUM(retention22),
SUM(retention23),
SUM(retention24),
SUM(retention25),
SUM(retention26),
SUM(retention27),
SUM(retention28),
SUM(retention29)


 FROM `ad_retention_v2`
 WHERE DATE<'2017-04-20'
 GROUP BY  platform,game_channel,agent
 ) b
 ON a.platform=b.platform
 AND a.game_channel=b.game_channel
 AND a.agent=b.agent
 
 
LEFT JOIN (
  
SELECT  platform,game_channel,agent,
SUM(online_avg0),
SUM(online_avg1),
SUM(online_avg2),
SUM(online_avg3),
SUM(online_avg4),
SUM(online_avg5),
SUM(online_avg6),
SUM(online_avg7),
SUM(online_avg8),
SUM(online_avg9),
SUM(online_avg10),
SUM(online_avg11),
SUM(online_avg12),
SUM(online_avg13),
SUM(online_avg14),
SUM(online_avg15),
SUM(online_avg16),
SUM(online_avg17),
SUM(online_avg18),
SUM(online_avg19),
SUM(online_avg20),
SUM(online_avg21),
SUM(online_avg22),
SUM(online_avg23),
SUM(online_avg24),
SUM(online_avg25),
SUM(online_avg26),
SUM(online_avg27),
SUM(online_avg28),
SUM(online_avg29)


 FROM `ad_onlinetime_v2`
 WHERE DATE<'2017-04-20'
 GROUP BY  platform,game_channel,agent
 ) c
  ON a.platform=c.platform
 AND a.game_channel=c.game_channel
 AND a.agent=c.agent
 
LEFT JOIN 
(

SELECT  platform,game_channel,agent,
SUM(money0),
SUM(money1),
SUM(money2),
SUM(money3),
SUM(money4),
SUM(money5),
SUM(money6),
SUM(money7),
SUM(money8),
SUM(money9),
SUM(money10),
SUM(money11), 
SUM(money12),
SUM(money13),
SUM(money14),
SUM(money15),
SUM(money16),
SUM(money17),
SUM(money18),
SUM(money19),
SUM(money20),
SUM(money21),
SUM(money22),
SUM(money23),
SUM(money24),
SUM(money25),
SUM(money26),
SUM(money27),
SUM(money28),
SUM(money29)


 FROM `ad_re_money_v2`
 WHERE DATE<'2017-04-20'
 GROUP BY  platform,game_channel,agent
 
 ) d 
  ON a.platform=d.platform
 AND a.game_channel=d.game_channel
 AND a.agent=d.agent
 


	"""
	sql ="""
SELECT DISTINCT DATE,game_channel,agent,ad_Creative,CONCAT("'",accountid),logouttime,TIME  FROM `logout_detail` WHERE DATE_FORMAT(logouttime,'%Y-%m-%d') IN ('2017-05-01','2017-05-02')


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
			file_object.write(word)
			word=""
		file_object.close()














if __name__ == '__main__':
	export_excel()