# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
import random
import re
from app.controler.power_API import get_business_json
import time
import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')
class cMediaRetention:
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
	    print(jsons[0:100])
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
	    for item in jsons[:]:
	        if item == "":
	            jsons.remove(item)
	    print(type(jsons))
	        #resultjson=resultjson[0:-1]
	    print time.asctime(time.localtime(time.time()))
	    return json.dumps(jsons)

    	#tj = {"channel":[{"id":"17173", "text":"17173"},{"id":"点入", "text":"点入"}],"staff":[{"id":"172173", "text":"171373"},{"id":"点入", "text":"点入点入"}]}