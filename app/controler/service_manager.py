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


import media_export_json
import service_json_A
import csv_import_A


if __name__ == '__main__':
	


 
######service_json_A
	service_json_A.main()
######csv_import_A
	csv_import_A.import_check("/data1/bidata/1452827692979/","market_newuser_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1452827692979/","market_logincount_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1452827692979/","market_ltv_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1452827692979/","market_onlinetime_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1452827692979/","market_retain_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1452827692979/","market_login_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1452827692979/","market_levelup_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1452827692979/","market_logout_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1452827692979/","market_recharge_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1452827692979/","market_callback_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")

	csv_import_A.import_check("/data1/bidata/1479458217005/","market_newuser_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1479458217005/","market_logincount_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1479458217005/","market_ltv_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1479458217005/","market_onlinetime_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1479458217005/","market_retain_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1479458217005/","market_login_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1479458217005/","market_levelup_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1479458217005/","market_logout_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1479458217005/","market_recharge_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")
	csv_import_A.import_check("/data1/bidata/1479458217005/","market_callback_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv")

	csv_import_A.delete_csv("ad_action_v2","")
	csv_import_A.import_csv("/data1/bidata/1452827692979/","market_newuser_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'ad_action_v2')
	csv_import_A.import_csv("/data1/bidata/1479458217005/","market_newuser_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'ad_action_v2')



	csv_import_A.delete_csv("ad_logincount_v2","")
	csv_import_A.import_csv("/data1/bidata/1452827692979/","market_logincount_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'ad_logincount_v2')
	csv_import_A.import_csv("/data1/bidata/1479458217005/","market_logincount_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'ad_logincount_v2')

	csv_import_A.delete_csv("ad_re_money_v2","")
	csv_import_A.import_csv("/data1/bidata/1452827692979/","market_ltv_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'ad_re_money_v2')
	csv_import_A.import_csv("/data1/bidata/1479458217005/","market_ltv_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'ad_re_money_v2')

	csv_import_A.delete_csv("ad_onlinetime_v2","")
	csv_import_A.import_csv("/data1/bidata/1452827692979/","market_onlinetime_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'ad_onlinetime_v2')
	csv_import_A.import_csv("/data1/bidata/1479458217005/","market_onlinetime_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'ad_onlinetime_v2')

	csv_import_A.delete_csv("ad_retention_v2","")
	csv_import_A.import_csv("/data1/bidata/1452827692979/","market_retain_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'ad_retention_v2')
	csv_import_A.import_csv("/data1/bidata/1479458217005/","market_retain_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'ad_retention_v2')


	csv_import_A.delete_csv("login_detail",str(datetime.datetime.now().strftime('%Y-%m-%d')))
	csv_import_A.import_csv("/data1/bidata/1452827692979/","market_login_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'login_detail')
	csv_import_A.import_csv("/data1/bidata/1479458217005/","market_login_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'login_detail_1479458217005')
 

	csv_import_A.delete_csv("level_detail",str(datetime.datetime.now().strftime('%Y-%m-%d')))
	csv_import_A.import_csv("/data1/bidata/1452827692979/","market_levelup_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'level_detail')
	csv_import_A.import_csv("/data1/bidata/1479458217005/","market_levelup_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'level_detail_1479458217005')
 
	csv_import_A.delete_csv("logout_detail",str(datetime.datetime.now().strftime('%Y-%m-%d')))
	csv_import_A.import_csv("/data1/bidata/1452827692979/","market_logout_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'logout_detail')
	csv_import_A.import_csv("/data1/bidata/1479458217005/","market_logout_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'logout_detail_1479458217005')
 

	csv_import_A.delete_csv("recharge_detail",str(datetime.datetime.now().strftime('%Y-%m-%d')))
	csv_import_A.import_csv("/data1/bidata/1452827692979/","market_recharge_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'recharge_detail')
	csv_import_A.import_csv("/data1/bidata/1479458217005/","market_recharge_log_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'recharge_detail_1479458217005')
 

	csv_import_A.delete_csv("ad_action_idfa","")
	csv_import_A.import_csv("/data1/bidata/1452827692979/","market_callback_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'ad_action_idfa')
	csv_import_A.import_csv("/data1/bidata/1479458217005/","market_callback_"+str((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))+".csv",'ad_action_idfa')


	csv_import_A.import_clac()#补充自然量的数据到spend表





	print("step3 ok")

