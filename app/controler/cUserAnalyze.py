# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
import random
import re
from app.controler.power_API import get_business_json
from public_function import get_first_letter
import time


class cUserAnalyze:

	@staticmethod
	def userAnalyzeJson(username,filternode):
		print filternode
		jsons = json.loads(get_business_json("detail_1.json", username))["body"]  # 字符串传化为json 对象 dict
		args = filternode
		jsons = json.dumps(jsons, ensure_ascii=False)
		jsons = jsons.replace(" ", "")

		resultjson=[]
		word=r'({[^}]*[^}]*})'
		jsons=",".join(re.findall(word, jsons))

		for x in xrange(0, len(args)):
			if args[x][0]=="tjtype":
				tjtype=args[x][1]
			if args[x][0]=="channel_name" or args[x][0]=="agent" or args[x][0]=="staff" or args[x][0]=="platform" :
				if args[x][1]!="":
					word=r'({[^}]*"'+args[x][0]+'":"'+args[x][1].replace(',','"[^}]*}|{[^}]*"'+args[x][0]+'":"')+'"[^}]*})'
					jsons=",".join(re.findall(word,jsons))
				else:
					word=r'({[^}]*[^}]*})'
					jsons=",".join(re.findall(word,jsons))

		jsons=jsons.replace('"r1":""','"r1":0')
		jsons=jsons.replace('"r29":""','"r29":0')
		jsons=jsons.replace('"r6":""','"r6":0')
		jsons=jsons.replace('"cumulative_flow":""','"cumulative_flow":0')
		jsons=jsons.replace('"cumulative_money":""','"cumulative_money":0')
		jsons=jsons.replace('"spend":""','"spend":0')
		jsons=json.loads("["+jsons+"]")#加上[]  就可以返回了
		# new_json=[]
		# date_temp=[]
		#
		# jsons.sort(key=lambda jsons:jsons.get("date_time", 0))
		#
		#
		#
		# for x in xrange(1,len(jsons)):
		# 	if jsons[x]["date_time"] == jsons[x-1]["date_time"]:
		#
		# 		jsons[x]["ad_click"]=int(round(float(jsons[x]["ad_click"])))+int(round(float(jsons[x-1]["ad_click"])))
		# 		jsons[x]["ad_action"]=int(round(float(jsons[x]["ad_action"])))+int(round(float(jsons[x-1]["ad_action"])))
		# 		jsons[x]["double_new"]=int(round(float(jsons[x]["double_new"])))+int(round(float(jsons[x-1]["double_new"])))
		# 		jsons[x]["back_user"]=int(round(float(jsons[x]["back_user"])))+int(round(float(jsons[x-1]["back_user"])))
		# 		jsons[x]["ad_action_new"]=int(round(float(jsons[x]["ad_action_new"])))+int(round(float(jsons[x-1]["ad_action_new"])))
		# 		jsons[x]["ad_account_new"]=int(round(float(jsons[x]["ad_account_new"])))+int(round(float(jsons[x-1]["ad_account_new"])))
		# 		jsons[x]["paid_account"]=int(round(float(jsons[x]["paid_account"])))+int(round(float(jsons[x-1]["paid_account"])))
		# 		jsons[x]["spend"]=int(round(float(jsons[x]["spend"])))+int(round(float(jsons[x-1]["spend"])))
		# 		jsons[x]["cumulative_flow"]=int(round(float(jsons[x]["cumulative_flow"])))+int(round(float(jsons[x-1]["cumulative_flow"])))
		# 		jsons[x]["cumulative_money"]=int(round(float(jsons[x]["cumulative_money"])))+int(round(float(jsons[x-1]["cumulative_money"])))
		# 		jsons[x]["r1"]=int(round(float(jsons[x]["r1"])))+int(round(float(jsons[x-1]["r1"])))
		# 		jsons[x]["r6"]=int(round(float(jsons[x]["r6"])))+int(round(float(jsons[x-1]["r6"])))
		# 		jsons[x]["r29"]=int(round(float(jsons[x]["r29"])))+int(round(float(jsons[x-1]["r29"])))
		# 		jsons[x]["ad_role_31"]=int(round(float(jsons[x]["ad_role_31"])))+int(round(float(jsons[x-1]["ad_role_31"])))
		# 		jsons[x]["ad_AU_5"]=int(round(float(jsons[x]["ad_AU_5"])))+int(round(float(jsons[x-1]["ad_AU_5"])))
		# 		jsons[x-1]=""
		# 	else:
		# 		jsons[x]["ad_click"]=int(round(float(jsons[x]["ad_click"])))
		# 		jsons[x]["ad_action"]=int(round(float(jsons[x]["ad_action"])))
		# 		jsons[x]["double_new"]=int(round(float(jsons[x]["double_new"])))
		# 		jsons[x]["back_user"]=int(round(float(jsons[x]["back_user"])))
		# 		#jsons[x]["ad_action_new"]=int(round(float(jsons[x]["ad_action_new"])))
		# 		jsons[x]["ad_account_new"]=int(round(float(jsons[x]["ad_account_new"])))
		# 		jsons[x]["paid_account"]=int(round(float(jsons[x]["paid_account"])))
		# 		jsons[x]["spend"]=int(round(float(jsons[x]["spend"])))
		# 		jsons[x]["cumulative_flow"]=int(round(float(jsons[x]["cumulative_flow"])))
		# 		jsons[x]["cumulative_money"]=int(round(float(jsons[x]["cumulative_money"])))
		# 		jsons[x]["r1"]=int(round(float(jsons[x]["r1"])))
		# 		jsons[x]["r6"]=int(round(float(jsons[x]["r6"])))
		# 		jsons[x]["r29"]=int(round(float(jsons[x]["r29"])))
		# 		jsons[x]["ad_role_31"]=int(round(float(jsons[x]["ad_role_31"])))
		# 		jsons[x]["ad_AU_5"]=int(round(float(jsons[x]["ad_AU_5"])))
		#
		# for item in jsons[:]: # 复制一个json list 出来，凡是刚才赋值为“”的都标记为删除，remove后 的jsons 就是结果了
		# 	if item == "":
		# 		jsons.remove(item)
		#
		#
		#
		# for x in xrange(0,len(jsons)):
		#
		# 		jsons[x]["fufeilv"]=float(float(jsons[x]["paid_account"])/float(jsons[x]["ad_account_new"])*100) if float(jsons[x]["ad_account_new"])!= 0 else 0
		# 		jsons[x]["ROI"]=float(float(jsons[x]["cumulative_money"])/float(jsons[x]["spend"])*100) if float(jsons[x]["spend"])!= 0 else 0
		# 		jsons[x]["CPA"]=float(float(jsons[x]["spend"])/float(jsons[x]["double_new"])) if float(jsons[x]["double_new"])!= 0 else 0
		# 		#print(jsons[x]["paid_account"],jsons[x]["ad_account_new"],jsons[x]["paid_account"]/jsons[x]["ad_account_new"])
		jsons=json.dumps(jsons)
		jsons = jsons.replace(" ", "")
		return jsons
