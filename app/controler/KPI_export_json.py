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

	

def export_clac(sql,name):#标量计算
	date_=[]
	value=[]


	conn =  pymysql.connect(host='120.26.162.150',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306)
	cur_1 = conn.cursor()
	cur_1.execute(sql)
	res=cur_1.fetchall()

	if len(res)>1:


		for r in res:

			if len(str(r[1]))>0: 
				value.append(r[1])




	word=str(name)+"		"+str(sum(value)/len(value))+"		"+str(min(value))+"		"+str(max(value))+"		"+str(value[len(value)/2])+"\n"


		
	cur_1.close()
	conn.close()

	create_json(word,"testtest")

def export_clac_detail():

	sql="""

SELECT DATE,game_channel,ROUND(SUM(ad_new)/SUM(ad_action),2)*100 FROM `ad_action_v2` WHERE  ad_id NOT IN ('10','20') AND platform='安卓' GROUP BY DATE ,game_channel
HAVING SUM(ad_action)>0  ORDER BY DATE ,game_channel


	"""

	conn =  pymysql.connect(host='120.26.162.150',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306)
	cur_1 = conn.cursor()
	cur_1.execute(sql)
	res=cur_1.fetchall()
	if len(res)>1:

		file_object = open(os.getcwd()+'/../../static/json/tttddd.json','a')
		for r in res:
			file_object.write(str(r[0])+"	"+str(r[1])+"	"+str(r[2])+"\n")

		file_object.close()




def create_json(word,name):
	file_object = open(os.getcwd()+'/../../static/json/'+name+'.json','a')
	file_object.write(word)
	file_object.close()
	print("create_json_"+name)


if __name__ == '__main__':
		export_clac_detail()
		print time.asctime(time.localtime(time.time()))
 		#export_clac("SELECT DATE,SUM(ad_action) FROM `ad_action_v2` WHERE ad_id='20' GROUP BY DATE ORDER BY SUM(ad_action)","安卓自然量激活分布")
# 		export_clac("SELECT DATE,SUM(ad_action) FROM `ad_action_v2` WHERE ad_id='10' and date>'2016-07-13' GROUP BY DATE ORDER BY SUM(ad_action)","iOS自然量激活分布")
# 		export_clac("SELECT DATE,SUM(ad_new) FROM `ad_action_v2` WHERE ad_id='20' GROUP BY DATE ORDER BY SUM(ad_new)","安卓自然量新增账号分布")
# 		export_clac("SELECT DATE,SUM(ad_new) FROM `ad_action_v2` WHERE ad_id='10' and date>'2016-07-13' GROUP BY DATE ORDER BY SUM(ad_new)","iOS自然量新增账号分布")
# 		export_clac("SELECT DATE,ROUND(SUM(ad_new)/SUM(ad_action),2)*100 FROM `ad_action_v2` WHERE ad_id='20' GROUP BY DATE ORDER BY SUM(ad_new)/SUM(ad_action)","安卓自然量激活新增账号转化率分布")
# 		export_clac("SELECT DATE,ROUND(SUM(ad_new)/SUM(ad_action),2)*100 FROM `ad_action_v2` WHERE ad_id='10' and date>'2016-07-13' GROUP BY DATE ORDER BY SUM(ad_new)/SUM(ad_action)","iOS自然量激活新增账号转化率分布")
# 		export_clac("SELECT DATE,ROUND(SUM(ad_pay_new)/SUM(ad_new),2)*100 FROM `ad_action_v2` WHERE ad_id='20' GROUP BY DATE ORDER BY SUM(ad_pay_new)/SUM(ad_new)","安卓自然量首日新增付费率分布")
# 		export_clac("SELECT DATE,ROUND(SUM(ad_pay_new)/SUM(ad_new),2)*100 FROM `ad_action_v2` WHERE ad_id='10'  and date>'2016-07-13' GROUP BY DATE ORDER BY SUM(ad_pay_new)/SUM(ad_new)","iOS自然量首日新增付费率分布")
	
# 		export_clac("""SELECT DATE,SUM(ad_action) FROM `ad_action_v2` WHERE ad_id NOT IN ('10','20') AND platform='安卓' GROUP BY DATE ORDER BY SUM(ad_action)""","安卓广告激活分布")
# 		export_clac("""SELECT DATE,SUM(ad_action) FROM `ad_action_v2` WHERE ad_id not in ('10','20') and platform='IOS正版' and date>'2016-07-13' GROUP BY DATE ORDER BY SUM(ad_action)""","iOS广告激活分布")
# 		export_clac("""SELECT DATE,SUM(ad_new) FROM `ad_action_v2` WHERE ad_id not in ('10','20') and platform='安卓' GROUP BY DATE ORDER BY SUM(ad_new)""","安卓广告新增账号分布")
# 		export_clac("""SELECT DATE,SUM(ad_new) FROM `ad_action_v2` WHERE ad_id not in ('10','20') and platform='IOS正版'  and date>'2016-07-13' GROUP BY DATE ORDER BY SUM(ad_new)""","iOS广告新增账号分布")
# 		export_clac("""SELECT DATE,ROUND(SUM(ad_new)/SUM(ad_action),2)*100 FROM `ad_action_v2` WHERE  ad_id not in ('10','20') and platform='安卓' GROUP BY DATE HAVING SUM(ad_action)>0  ORDER BY SUM(ad_new)/SUM(ad_action)""","安卓广告激活新增账号转化率分布")
# 		export_clac("""SELECT DATE,ROUND(SUM(ad_new)/SUM(ad_action),2)*100 FROM `ad_action_v2` WHERE ad_id not in ('10','20') and platform='IOS正版'  and date>'2016-07-13' GROUP BY DATE  HAVING SUM(ad_action)>0  ORDER BY SUM(ad_new)/SUM(ad_action)""","iOS广告激活新增账号转化率分布")
# 		export_clac("""SELECT DATE,ROUND(SUM(ad_pay_new)/SUM(ad_new),2)*100 FROM `ad_action_v2` WHERE ad_id not in ('10','20') and platform='安卓' GROUP BY DATE HAVING SUM(ad_new)>0  ORDER BY SUM(ad_pay_new)/SUM(ad_new)""","安卓广告首日新增付费率分布")
# 		export_clac("""SELECT DATE,ROUND(SUM(ad_pay_new)/SUM(ad_new),2)*100 FROM `ad_action_v2` WHERE  ad_id not in ('10','20') and platform='IOS正版' and date>'2016-07-13'  GROUP BY DATE  HAVING SUM(ad_new)>0 ORDER BY SUM(ad_pay_new)/SUM(ad_new)""","iOS广告首日新增付费率分布")



# 		export_clac("""

# 			SELECT DATE,SUM(money7)/SUM(ad_new) FROM 
# (

#  SELECT a.`ad_new`,b.* FROM `ad_action_v2` a ,`ad_re_money_v2` b WHERE a.`ad_id`=b.`ad_id`
#  AND a.`game_id`=b.`game_id` AND a.`platform`=b.`platform` AND a.`date`=b.`date` AND a.`game_channel`=b.`game_channel`
#  AND a.`agent`=b.`agent` AND a.`AdCreative`=b.`ad_Creative`
# ) a



# WHERE 
# a.ad_id ='10'    GROUP BY DATE  HAVING SUM(ad_new)>0 AND SUM(money7)>0 ORDER BY SUM(money7)/SUM(ad_new)
 
 
# ""","iOS自然量-+7arpu分布")


# 		export_clac("""

# 			SELECT DATE,SUM(money7)/SUM(ad_new) FROM 
# (

#  SELECT a.`ad_new`,b.* FROM `ad_action_v2` a ,`ad_re_money_v2` b WHERE a.`ad_id`=b.`ad_id`
#  AND a.`game_id`=b.`game_id` AND a.`platform`=b.`platform` AND a.`date`=b.`date` AND a.`game_channel`=b.`game_channel`
#  AND a.`agent`=b.`agent` AND a.`AdCreative`=b.`ad_Creative`
# ) a



# WHERE 
# a.ad_id ='20'    GROUP BY DATE  HAVING SUM(ad_new)>0 AND SUM(money7)>0 ORDER BY SUM(money7)/SUM(ad_new)
 
 
# ""","安卓自然量-+7arpu分布")



# 		export_clac("""

# 			SELECT DATE,SUM(money7)/SUM(ad_new) FROM 
# (

#  SELECT a.`ad_new`,b.* FROM `ad_action_v2` a ,`ad_re_money_v2` b WHERE a.`ad_id`=b.`ad_id`
#  AND a.`game_id`=b.`game_id` AND a.`platform`=b.`platform` AND a.`date`=b.`date` AND a.`game_channel`=b.`game_channel`
#  AND a.`agent`=b.`agent` AND a.`AdCreative`=b.`ad_Creative`
# ) a



# WHERE 
# a.ad_id NOT IN ('20','10') AND a.platform='IOS正版'   GROUP BY DATE  HAVING SUM(ad_new)>0 AND SUM(money7)>0 ORDER BY SUM(money7)/SUM(ad_new)
 
 
# ""","iOS广告量-+7arpu分布")



# 		export_clac("""

# 			SELECT DATE,SUM(money7)/SUM(ad_new) FROM 
# (

#  SELECT a.`ad_new`,b.* FROM `ad_action_v2` a ,`ad_re_money_v2` b WHERE a.`ad_id`=b.`ad_id`
#  AND a.`game_id`=b.`game_id` AND a.`platform`=b.`platform` AND a.`date`=b.`date` AND a.`game_channel`=b.`game_channel`
#  AND a.`agent`=b.`agent` AND a.`AdCreative`=b.`ad_Creative`
# ) a



# WHERE 
# a.ad_id NOT IN ('20','10') AND a.platform='安卓'  GROUP BY DATE  HAVING SUM(ad_new)>0 AND SUM(money7)>0 ORDER BY SUM(money7)/SUM(ad_new)
 
 
# ""","安卓广告量-+7arpu分布")





# 		export_clac("""

# 					SELECT DATE,SUM(online_avg0)/SUM(ad_new) FROM 
# (

#  SELECT a.`ad_new`,b.* FROM `ad_action_v2` a ,`ad_onlinetime_v2` b WHERE a.`ad_id`=b.`ad_id`
#  AND a.`game_id`=b.`game_id` AND a.`platform`=b.`platform` AND a.`date`=b.`date` AND a.`game_channel`=b.`game_channel`
#  AND a.`agent`=b.`agent` AND a.`AdCreative`=b.`ad_Creative`

# ) a



# WHERE 
# a.ad_id ='10'  GROUP BY DATE  HAVING SUM(ad_new)>0 AND SUM(online_avg0)>0 ORDER BY SUM(online_avg0)/SUM(ad_new)


 
# ""","iOS 自然量 首日活跃时长分布")


# 		export_clac("""

# 					SELECT DATE,SUM(online_avg0)/SUM(ad_new) FROM 
# (

#  SELECT a.`ad_new`,b.* FROM `ad_action_v2` a ,`ad_onlinetime_v2` b WHERE a.`ad_id`=b.`ad_id`
#  AND a.`game_id`=b.`game_id` AND a.`platform`=b.`platform` AND a.`date`=b.`date` AND a.`game_channel`=b.`game_channel`
#  AND a.`agent`=b.`agent` AND a.`AdCreative`=b.`ad_Creative`

# ) a



# WHERE 
# a.ad_id ='20'  GROUP BY DATE  HAVING SUM(ad_new)>0 AND SUM(online_avg0)>0 ORDER BY SUM(online_avg0)/SUM(ad_new)


 
# ""","安卓 自然量 首日活跃时长分布")

# 		export_clac("""

# 			SELECT DATE,SUM(online_avg0)/SUM(ad_new) FROM 
# (

#  SELECT a.`ad_new`,b.* FROM `ad_action_v2` a ,`ad_onlinetime_v2` b WHERE a.`ad_id`=b.`ad_id`
#  AND a.`game_id`=b.`game_id` AND a.`platform`=b.`platform` AND a.`date`=b.`date` AND a.`game_channel`=b.`game_channel`
#  AND a.`agent`=b.`agent` AND a.`AdCreative`=b.`ad_Creative`

# ) a



# WHERE 
# a.ad_id NOT IN ('20','10') AND a.platform='安卓'    GROUP BY DATE  HAVING SUM(ad_new)>0 AND SUM(online_avg0)>0 ORDER BY SUM(online_avg0)/SUM(ad_new)




 
# ""","安卓 广告量 首日活跃时长分布")



# 		export_clac("""

# 			SELECT DATE,SUM(online_avg0)/SUM(ad_new) FROM 
# (

#  SELECT a.`ad_new`,b.* FROM `ad_action_v2` a ,`ad_onlinetime_v2` b WHERE a.`ad_id`=b.`ad_id`
#  AND a.`game_id`=b.`game_id` AND a.`platform`=b.`platform` AND a.`date`=b.`date` AND a.`game_channel`=b.`game_channel`
#  AND a.`agent`=b.`agent` AND a.`AdCreative`=b.`ad_Creative`

# ) a



# WHERE 
# a.ad_id NOT IN ('20','10') AND a.platform='IOS正版'    GROUP BY DATE  HAVING SUM(ad_new)>0 AND SUM(online_avg0)>0 ORDER BY SUM(online_avg0)/SUM(ad_new)




 
# ""","iOS 广告量 首日活跃时长分布")