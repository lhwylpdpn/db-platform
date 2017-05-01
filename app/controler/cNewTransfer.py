# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
import random
import re
import time
from app.controler.power_API import get_business_json


class cNewTransfer:
	@staticmethod
	def newTransferTJ(username):
		game_id = []
		platform = []
		channel_name = []
		staff = []
		agent = []
		tj = ""
		jsons = json.loads(get_business_json("media_2.json", username))["body"]  # 字符串传化为json 对象

		for x in xrange(0,len(jsons)):
			game_id.append(jsons[x]["game_id"])
			platform.append(jsons[x]["platform"])
			channel_name.append(jsons[x]['channel_name'])
			agent.append(jsons[x]['agent'])
			staff.append(jsons[x]['staff'])
		game_id=list(set(game_id))
		platform=list(set(platform))
		channel_name=list(set(channel_name))
		agent=list(set(agent))
		staff=list(set(staff))
		tj+='{"game_id":['
		for x in xrange(0,len(game_id)):
			tj+='{"id":"'+str(game_id[x])+'","text":"'+str(game_id[x])+'"},'
		tj=tj[0:-1]+'],'
		tj+='"channel_name":['
		for x in xrange(0,len(channel_name)):
			tj+='{"id":"'+str(channel_name[x].encode('utf-8'))+'","text":"'+str(channel_name[x].encode('utf-8'))+'"},'
		tj=tj[0:-1]+'],'
		tj+='"staff":['
		for x in xrange(0,len(staff)):
			tj+='{"id":"'+str(staff[x].encode('utf-8'))+'","text":"'+str(staff[x].encode('utf-8'))+'"},'
		tj=tj[0:-1]+'],'
		tj+='"platform":['
		for x in xrange(0,len(platform)):
			tj+='{"id":"'+str(platform[x].encode('utf-8'))+'","text":"'+str(platform[x].encode('utf-8'))+'"},'
		tj=tj[0:-1]+'],'
		tj+='"agent":['
		for x in xrange(0,len(agent)):
			tj+='{"id":"'+str(agent[x].encode('utf-8'))+'","text":"'+str(agent[x].encode('utf-8'))+'"},'
		tj=tj[0:-1]


		tj=tj+']}'
		
		return tj


	@staticmethod
	def newTransferJson(username, args):
		jsons = json.loads(get_business_json("media_2.json", username).encode("utf-8"))["body"]  #获取body内容，注意为了匹配要encode一下 utf8
		jsons = json.dumps(jsons, ensure_ascii=False)  # 转成字符串，必须要有ensure_ascii=False，不然会自动转成ascii
		jsons = jsons.replace(" ", "")  # 转完的 键值对之间有空格要去掉

		jsons=jsons.replace('"dis_spend":""', '"dis_spend":"0"')
		word = r'({[^}]*[^}]*})'  # 将jsons字符串 筛选成{},{}的格式，也为了应对args根本没有参数，直接可以返回个全的
		jsons = ",".join(re.findall(word, jsons))  # 将筛选的结果拼成list，然后用，连接成字符串

		for x in xrange(0, len(args)):  # 循环args 将所有参数拼接成正则表达式word，并进行筛选，诗选结果拼成一个list
			if args[x][0] == "date_time" or args[x][0] == "channel_name" or args[x][0] == "game_id" or args[x][0] == "platform" or args[x][0] == "agent" or args[x][0] == "staff":
				if args[x][1] != "":
					word = r'({[^}]*"' + args[x][0] + '":"' + args[x][1].replace(',', '"[^}]+}|{[^}]+"' + args[x][0] + '":"') + '"[^}]*})'

					jsons = ",".join(re.findall(word, jsons))

				else:
					word = r'({[^}]*[^}]*})'
					jsons = ",".join(re.findall(word, jsons))

		jsons=jsons.replace('"dis_spend":""', '"dis_spend":0')  # 空变成0，方便我后面计算
		jsons=jsons.replace('"ad_click":""', '"ad_click":0')
		jsons=jsons.replace('"ad_action":""', '"ad_action":0')
		jsons=jsons.replace('"ad_action_new":""', '"ad_action_new":0')
		jsons=jsons.replace('"ad_action_new_back":""', '"ad_action_new_back":0')
		jsons=jsons.replace('"ad_account_new_double":""', '"ad_account_new_double":0')
		jsons=jsons.replace('"ad_login_count":""', '"ad_login_count":0')
		jsons=jsons.replace('"ad_AU_5":""', '"ad_AU_5":0')
		jsons=jsons.replace('"ad_create_role":""', '"ad_create_role":0')
		jsons=jsons.replace('"ad_role_31":""', '"ad_role_31":0')


		jsons = json.loads("[" + jsons + "]")  # 加上[]  就可以返回了

		jsons.sort(key=lambda jsons: jsons.get("date_time", 0))  # step1 对json里的date 排序，排序出来的每一条日期都相邻,2017-04-27 2017-04-27 2017-04-27 2017-04-28 2017-04-28 ....

		for x in xrange(1,len(jsons)):# 日期相邻后，一次循环，只要[x] 和[x-1] 的日期一样，就把[x-1]的valuej和[x]的value加一起，给[x],然后删除掉[x-1]的元素，一次循环下来 就把所有日期相同的加一起了
			if jsons[x]["date_time"] == jsons[x-1]["date_time"]:

				jsons[x]["game_id"] = "groupBy"
				jsons[x]["platform"] = "groupBy"
				jsons[x]["channel_name"] = "groupBy"
				jsons[x]["agent"] = "groupBy"
				jsons[x]["staff"] = "groupBy"

				jsons[x]["dis_spend"] = int(round(float(jsons[x]["dis_spend"]))) + int(round(float(jsons[x-1]["dis_spend"])))
				jsons[x]["ad_click"] = int(round(float(jsons[x]["ad_click"]))) + int(round(float(jsons[x-1]["ad_click"])))
				jsons[x]["ad_action"] = int(round(float(jsons[x]["ad_action"]))) + int(round(float(jsons[x-1]["ad_action"])))
				jsons[x]["ad_action_new"] = int(round(float(jsons[x]["ad_action_new"]))) + int(round(float(jsons[x-1]["ad_action_new"])))
				jsons[x]["ad_action_new_back"] = int(round(float(jsons[x]["ad_action_new_back"]))) + int(round(float(jsons[x-1]["ad_action_new_back"])))
				jsons[x]["ad_account_new_double"] = int(round(float(jsons[x]["ad_account_new_double"]))) + int(round(float(jsons[x-1]["ad_account_new_double"])))
				jsons[x]["ad_login_count"] = int(round(float(jsons[x]["ad_login_count"]))) + int(round(float(jsons[x-1]["ad_login_count"])))
				jsons[x]["ad_AU_5"] = int(round(float(jsons[x]["ad_AU_5"]))) + int(round(float(jsons[x-1]["ad_AU_5"])))
				jsons[x]["ad_create_role"] = int(round(float(jsons[x]["ad_create_role"]))) + int(round(float(jsons[x-1]["ad_create_role"])))
				jsons[x]["ad_role_31"] = int(round(float(jsons[x]["ad_role_31"]))) + int(round(float(jsons[x-1]["ad_role_31"])))
				jsons[x-1] = ""   # 这句话是精髓
			else:
				jsons[x]["game_id"] = "groupBy"
				jsons[x]["platform"] = "groupBy"
				jsons[x]["channel_name"] = "groupBy"
				jsons[x]["agent"] = "groupBy"
				jsons[x]["staff"] = "groupBy"

				jsons[x]["dis_spend"] = int(round(float(jsons[x]["dis_spend"])))
				jsons[x]["ad_click"] = int(round(float(jsons[x]["ad_click"])))
				jsons[x]["ad_action"] = int(round(float(jsons[x]["ad_action"])))
				jsons[x]["ad_action_new"] = int(round(float(jsons[x]["ad_action_new"])))
				jsons[x]["ad_action_new_back"] = int(round(float(jsons[x]["ad_action_new_back"])))
				jsons[x]["ad_account_new_double"] = int(round(float(jsons[x]["ad_account_new_double"])))
				jsons[x]["ad_login_count"] = int(round(float(jsons[x]["ad_login_count"])))
				jsons[x]["ad_AU_5"] = int(round(float(jsons[x]["ad_AU_5"])))
				jsons[x]["ad_create_role"] = int(round(float(jsons[x]["ad_create_role"])))
				jsons[x]["ad_role_31"] = int(round(float(jsons[x]["ad_role_31"])))

		for item in jsons[:]:  # 复制一个json list 出来，凡是刚才赋值为“”的都标记为删除，remove后 的jsons 就是结果了
			if item == "":
				jsons.remove(item)

		jsons = json.dumps(jsons)

		return jsons
