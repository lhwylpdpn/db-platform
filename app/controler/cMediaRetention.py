# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
import random
import re
from app.controler.power_API import get_business_json
from public_function import get_first_letter
import time
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')
class cMediaRetention:

	
	@staticmethod
	def tj_for_qiangye_test(username):
		game_id=[]
		platform=[]
		channel_name=[]
		staff=[]
		agent=[]
		tj=""
		tjtype=""
		args = request.args.items()
		jsons = json.loads(get_business_json("media_3.json", session["username"]).encode("utf-8"))["body"]
		jsons = json.dumps(jsons,ensure_ascii=False)
		jsons = jsons.replace(" ","")
		resultjson=[]
		word=r'({[^}]*[^}]*})'
		jsons=",".join(re.findall(word,jsons))
		for x in xrange(0,len(args)):
			if args[x][0]=="tjtype":
				tjtype=args[x][1]
			if args[x][0]=="channel_name" or args[x][0]=="game_id" or args[x][0]=="platform" or args[x][0]=="agent" or args[x][0]=="staff" :
				if args[x][1]!="":
					word=r'({[^}]*"'+args[x][0]+'":"'+args[x][1].replace(',','"[^}]+}|{[^}]+"'+args[x][0]+'":"')+'"[^}]*})'
	
					jsons=",".join(re.findall(word,jsons))
		   
				else:
					word=r'({[^}]*[^}]*})'
					jsons=",".join(re.findall(word,jsons))

		jsons=json.loads("["+jsons+"]")


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
		tj="["
		if tjtype=="channel_name":
			for x in xrange(0,len(channel_name)):

				tj+='{"channel_name":"'+str(channel_name[x])+'","initial":"'+str(get_first_letter(channel_name[x]))+'"},'
			tj=tj[0:-1]
		if tjtype=="agent":
			for x in xrange(0,len(agent)):
				tj+='{"agent":"'+str(agent[x])+'","initial":"'+str(get_first_letter(agent[x]))+'"},'
			tj=tj[0:-1]
		if tjtype=="staff":
			for x in xrange(0,len(staff)):
				tj+='{"staff":"'+str(staff[x])+'","initial":"'+str(get_first_letter(staff[x]))+'"},'
			tj=tj[0:-1]
		if tjtype=="platform":
			for x in xrange(0,len(platform)):
				tj+='{"platform":"'+str(platform[x])+'","initial":"'+str(get_first_letter(platform[x]))+'"},'
			tj=tj[0:-1]
		tj=tj+']'
		
		return tj



	@staticmethod
	def mediaRetentionTJ(username):
		game_id=[]
		platform=[]
		channel_name=[]
		staff=[]
		agent=[]
		tj=""
		jsons = json.loads(get_business_json("media_3.json", username))["body"]  # 字符串传化为json 对象

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
	def mediaRetentionJson(username):
		args = request.args.items()  #获取请求list
		jsons = json.loads(get_business_json("media_3.json", session["username"]).encode("utf-8"))["body"]# 获取body内容，注意为了匹配要encode一下 utf8
		jsons = json.dumps(jsons,ensure_ascii=False) #转成字符串，必须要有ensure_ascii=False，不然会自动转成ascii
		jsons = jsons.replace(" ","")#转完的 键值对之间有空格要去掉
		resultjson=[]
		word=r'({[^}]*[^}]*})' #将jsons字符串 筛选成{},{}的格式，也为了应对args根本没有参数，直接可以返回个全的
		jsons=",".join(re.findall(word,jsons))#将筛选的结果拼成list，然后用，连接成字符串
		for x in xrange(0,len(args)):#循环args 将所有参数拼接成正则表达式word，并进行筛选，诗选结果拼成一个list
			if args[x][0]=="date_" or args[x][0]=="channel_name" or args[x][0]=="game_id" or args[x][0]=="platform" or args[x][0]=="agent" or args[x][0]=="staff" :
				if args[x][1]!="":
					word=r'({[^}]*"'+args[x][0]+'":"'+args[x][1].replace(',','"[^}]+}|{[^}]+"'+args[x][0]+'":"')+'"[^}]*})'
	
					jsons=",".join(re.findall(word,jsons))
		   
				else:
					word=r'({[^}]*[^}]*})'
					jsons=",".join(re.findall(word,jsons))

		jsons=jsons.replace('"re_0":""','"re_0":0')
		jsons=jsons.replace('"re_1":""','"re_1":0')
		jsons=jsons.replace('"re_2":""','"re_2":0')
		jsons=jsons.replace('"re_3":""','"re_3":0')
		jsons=jsons.replace('"re_4":""','"re_4":0')
		jsons=jsons.replace('"re_5":""','"re_5":0')
		jsons=jsons.replace('"re_6":""','"re_6":0')#空变成0，方便我后面计算
		jsons=json.loads("["+jsons+"]")#加上[]  就可以返回了
		new_json=[]
		date_temp=[]
		print(5)
		print time.asctime(time.localtime(time.time()))
		jsons.sort(key=lambda jsons:jsons.get("date_",0))
		print(6)
		for x in xrange(1,len(jsons)):
			if jsons[x]["date_"] == jsons[x-1]["date_"]:

				jsons[x]["re_0"]=int(round(float(jsons[x]["re_0"])))+int(round(float(jsons[x-1]["re_0"])))
				jsons[x]["re_1"]=int(round(float(jsons[x]["re_1"])))+int(round(float(jsons[x-1]["re_1"])))
				jsons[x]["re_2"]=int(round(float(jsons[x]["re_2"])))+int(round(float(jsons[x-1]["re_2"])))
				jsons[x]["re_3"]=int(round(float(jsons[x]["re_3"])))+int(round(float(jsons[x-1]["re_3"])))
				jsons[x]["re_4"]=int(round(float(jsons[x]["re_4"])))+int(round(float(jsons[x-1]["re_4"])))
				jsons[x]["re_5"]=int(round(float(jsons[x]["re_5"])))+int(round(float(jsons[x-1]["re_5"])))
				jsons[x]["re_6"]=int(round(float(jsons[x]["re_6"])))+int(round(float(jsons[x-1]["re_6"])))
				jsons[x-1]=""
			else:
				jsons[x]["re_0"]=int(round(float(jsons[x]["re_0"])))
				jsons[x]["re_1"]=int(round(float(jsons[x]["re_1"])))
				jsons[x]["re_2"]=int(round(float(jsons[x]["re_2"])))
				jsons[x]["re_3"]=int(round(float(jsons[x]["re_3"])))
				jsons[x]["re_4"]=int(round(float(jsons[x]["re_4"])))
				jsons[x]["re_5"]=int(round(float(jsons[x]["re_5"])))
				jsons[x]["re_6"]=int(round(float(jsons[x]["re_6"])))

		for item in jsons[:]:
			if item == "":
				jsons.remove(item)

			#resultjson=resultjson[0:-1]
		print time.asctime(time.localtime(time.time()))
		jsons=json.dumps(jsons)

		jsons = jsons.replace(" ","")
		jsons=jsons.replace('"re_0":0','"re_0":""')
		jsons=jsons.replace('"re_1":0','"re_1":""')
		jsons=jsons.replace('"re_2":0','"re_2":""')
		jsons=jsons.replace('"re_3":0','"re_3":""')
		jsons=jsons.replace('"re_4":0','"re_4":""')
		jsons=jsons.replace('"re_5":0','"re_5":""')
		jsons=jsons.replace('"re_6":0','"re_6":""')
		return jsons

	@staticmethod
	def mediaRetentionJson_2(username):
		args=request.args.items()
		jsons = json.loads(get_business_json("media_3.json", session["username"]).encode("utf-8"))["body"]
		jsons = json.dumps(jsons,ensure_ascii=False)
		jsons = jsons.replace(" ","")
		resultjson=[]
		word=r'({[^}]*[^}]*})'
		jsons=",".join(re.findall(word,jsons))
		for x in xrange(0,len(args)):
			if args[x][0]=="date_" or args[x][0]=="channel_name" or args[x][0]=="game_id" or args[x][0]=="platform" or args[x][0]=="agent" or args[x][0]=="staff" :
				if args[x][1]!="":
					word=r'({[^}]*"'+args[x][0]+'":"'+args[x][1].replace(',','"[^}]+}|{[^}]+"'+args[x][0]+'":"')+'"[^}]*})'

					jsons=",".join(re.findall(word,jsons))

				else:
					word=r'({[^}]*[^}]*})'
					jsons=",".join(re.findall(word,jsons))

		jsons=jsons.replace('"re_0":""','"re_0":0')
		jsons=jsons.replace('"re_1":""','"re_1":0')
		jsons=jsons.replace('"re_2":""','"re_2":0')
		jsons=jsons.replace('"re_3":""','"re_3":0')
		jsons=jsons.replace('"re_4":""','"re_4":0')
		jsons=jsons.replace('"re_5":""','"re_5":0')
		jsons=jsons.replace('"re_6":""','"re_6":0')
		jsons=json.loads("["+jsons+"]")
		new_json=[]
		date_temp=[]

		print time.asctime(time.localtime(time.time()))
		jsons.sort(key=lambda jsons:jsons.get("date_",0))

		for x in xrange(1,len(jsons)):
			if jsons[x]["date_"] == jsons[x-1]["date_"]:

				jsons[x]["re_0"]=int(round(float(jsons[x]["re_0"])))+int(round(float(jsons[x-1]["re_0"])))
				jsons[x]["re_1"]=int(round(float(jsons[x]["re_1"])))+int(round(float(jsons[x-1]["re_1"])))
				jsons[x]["re_2"]=int(round(float(jsons[x]["re_2"])))+int(round(float(jsons[x-1]["re_2"])))
				jsons[x]["re_3"]=int(round(float(jsons[x]["re_3"])))+int(round(float(jsons[x-1]["re_3"])))
				jsons[x]["re_4"]=int(round(float(jsons[x]["re_4"])))+int(round(float(jsons[x-1]["re_4"])))
				jsons[x]["re_5"]=int(round(float(jsons[x]["re_5"])))+int(round(float(jsons[x-1]["re_5"])))
				jsons[x]["re_6"]=int(round(float(jsons[x]["re_6"])))+int(round(float(jsons[x-1]["re_6"])))
				jsons[x-1]=""
			else:
				jsons[x]["re_0"]=int(round(float(jsons[x]["re_0"])))
				jsons[x]["re_1"]=int(round(float(jsons[x]["re_1"])))
				jsons[x]["re_2"]=int(round(float(jsons[x]["re_2"])))
				jsons[x]["re_3"]=int(round(float(jsons[x]["re_3"])))
				jsons[x]["re_4"]=int(round(float(jsons[x]["re_4"])))
				jsons[x]["re_5"]=int(round(float(jsons[x]["re_5"])))
				jsons[x]["re_6"]=int(round(float(jsons[x]["re_6"])))

		for item in jsons[:]:
			if item == "":
				jsons.remove(item)

		for x in xrange(0,len(jsons)):
			if jsons[x]["re_0"]!=0:
				jsons[x]["re_1"]=str(round(float(jsons[x]["re_1"])/float(jsons[x]["re_0"])*100,2))+"%"
				jsons[x]["re_2"]=str(round(float(jsons[x]["re_2"])/float(jsons[x]["re_0"])*100,2))+"%"
				jsons[x]["re_3"]=str(round(float(jsons[x]["re_3"])/float(jsons[x]["re_0"])*100,2))+"%"
				jsons[x]["re_4"]=str(round(float(jsons[x]["re_4"])/float(jsons[x]["re_0"])*100,2))+"%"
				jsons[x]["re_5"]=str(round(float(jsons[x]["re_5"])/float(jsons[x]["re_0"])*100,2))+"%"
				jsons[x]["re_6"]=str(round(float(jsons[x]["re_6"])/float(jsons[x]["re_0"])*100,2))+"%"
				jsons[x]["re_0"]="100%"
			else:
				jsons[x]["re_0"]="100%"

		jsons=json.dumps(jsons)
		jsons = jsons.replace(" ","")

		jsons=jsons.replace('"re_0":"0.0%"','"re_0":""')
		jsons=jsons.replace('"re_1":"0.0%"','"re_1":""')
		jsons=jsons.replace('"re_2":"0.0%"','"re_2":""')
		jsons=jsons.replace('"re_3":"0.0%"','"re_3":""')
		jsons=jsons.replace('"re_4":"0.0%"','"re_4":""')
		jsons=jsons.replace('"re_5":"0.0%"','"re_5":""')
		jsons=jsons.replace('"re_6":"0.0%"','"re_6":""')
		return jsons
