# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
import random
import re
from app.controler.power_API import get_business_json
import time


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


    	#tj = {"channel":[{"id":"17173", "text":"17173"},{"id":"点入", "text":"点入"}],"staff":[{"id":"172173", "text":"171373"},{"id":"点入", "text":"点入点入"}]}