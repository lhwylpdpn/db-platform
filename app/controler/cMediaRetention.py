# This Python file uses the following encoding: utf-8
from flask import render_template, request, Blueprint, session, redirect, url_for, json
import random
import re
from app.controler.power_API import get_business_json
from public_function import get_first_letter
import time
import sys 
import datetime
reload(sys) 
sys.setdefaultencoding('utf-8')
class cMediaRetention:

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
		#鹏鹏参考这部分group by 
		jsons.sort(key=lambda jsons:jsons.get("date_",0)) # step1 对json里的date 排序，排序出来的每一条日期都相邻,2017-04-27 2017-04-27 2017-04-27 2017-04-28 2017-04-28 ....
		print(6)
		for x in xrange(1,len(jsons)):# 日期相邻后，一次循环，只要[x] 和[x-1] 的日期一样，就把[x-1]的valuej和[x]的value加一起，给[x],然后删除掉[x-1]的元素，一次循环下来 就把所有日期相同的加一起了
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

		for item in jsons[:]: # 复制一个json list 出来，凡是刚才赋值为“”的都标记为删除，remove后 的jsons 就是结果了
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

	@staticmethod
	def mediaRetentionJson_3(username):
		args=request.args.items()
		jsons = json.loads(get_business_json("media_4.json", session["username"]).encode("utf-8"))["body"]
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
		jsons=jsons.replace('"online0":""','"online0":0')
		jsons=jsons.replace('"online1":""','"online1":0')
		jsons=jsons.replace('"online2":""','"online2":0')
		jsons=jsons.replace('"online3":""','"online3":0')
		jsons=jsons.replace('"online4":""','"online4":0')
		jsons=jsons.replace('"online5":""','"online5":0')
		jsons=jsons.replace('"online6":""','"online6":0')
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
				jsons[x]["online0"]=float(jsons[x]["online0"])+float(jsons[x-1]["online0"])
				jsons[x]["online1"]=float(jsons[x]["online1"])+float(jsons[x-1]["online1"])
				jsons[x]["online2"]=float(jsons[x]["online2"])+float(jsons[x-1]["online2"])
				jsons[x]["online3"]=float(jsons[x]["online3"])+float(jsons[x-1]["online3"])
				jsons[x]["online4"]=float(jsons[x]["online4"])+float(jsons[x-1]["online4"])
				jsons[x]["online5"]=float(jsons[x]["online5"])+float(jsons[x-1]["online5"])
				jsons[x]["online6"]=float(jsons[x]["online6"])+float(jsons[x-1]["online6"])
				jsons[x-1]=""
			else:
				jsons[x-1]["re_0"]=round(float(jsons[x-1]["online0"]/jsons[x-1]["re_0"])) if jsons[x-1]["re_0"]!=0 else 0
				jsons[x-1]["re_1"]=round(float(jsons[x-1]["online1"]/jsons[x-1]["re_1"])) if jsons[x-1]["re_1"]!=0 else 0
				jsons[x-1]["re_2"]=round(float(jsons[x-1]["online2"]/jsons[x-1]["re_2"])) if jsons[x-1]["re_2"]!=0 else 0
				jsons[x-1]["re_3"]=round(float(jsons[x-1]["online3"]/jsons[x-1]["re_3"])) if jsons[x-1]["re_3"]!=0 else 0
				jsons[x-1]["re_4"]=round(float(jsons[x-1]["online4"]/jsons[x-1]["re_4"])) if jsons[x-1]["re_4"]!=0 else 0
				jsons[x-1]["re_5"]=round(float(jsons[x-1]["online5"]/jsons[x-1]["re_5"])) if jsons[x-1]["re_5"]!=0 else 0
				jsons[x-1]["re_6"]=round(float(jsons[x-1]["online6"]/jsons[x-1]["re_6"])) if jsons[x-1]["re_6"]!=0 else 0

				jsons[x]["re_0"]=int(round(float(jsons[x]["re_0"])))
				jsons[x]["re_1"]=int(round(float(jsons[x]["re_1"])))
				jsons[x]["re_2"]=int(round(float(jsons[x]["re_2"])))
				jsons[x]["re_3"]=int(round(float(jsons[x]["re_3"])))
				jsons[x]["re_4"]=int(round(float(jsons[x]["re_4"])))
				jsons[x]["re_5"]=int(round(float(jsons[x]["re_5"])))
				jsons[x]["re_6"]=int(round(float(jsons[x]["re_6"])))
				jsons[x]["online0"]=float(jsons[x]["online0"])
				jsons[x]["online1"]=float(jsons[x]["online1"])
				jsons[x]["online2"]=float(jsons[x]["online2"])
				jsons[x]["online3"]=float(jsons[x]["online3"])
				jsons[x]["online4"]=float(jsons[x]["online4"])
				jsons[x]["online5"]=float(jsons[x]["online5"])
				jsons[x]["online6"]=float(jsons[x]["online6"])
			if x==len(jsons)-1:
				print(3333)
				jsons[x]["re_0"]=round(float(jsons[x]["online0"]/jsons[x]["re_0"])) if jsons[x]["re_0"]!=0 else 0
				jsons[x]["re_1"]=round(float(jsons[x]["online1"]/jsons[x]["re_1"])) if jsons[x]["re_1"]!=0 else 0
				jsons[x]["re_2"]=round(float(jsons[x]["online2"]/jsons[x]["re_2"])) if jsons[x]["re_2"]!=0 else 0
				jsons[x]["re_3"]=round(float(jsons[x]["online3"]/jsons[x]["re_3"])) if jsons[x]["re_3"]!=0 else 0
				jsons[x]["re_4"]=round(float(jsons[x]["online4"]/jsons[x]["re_4"])) if jsons[x]["re_4"]!=0 else 0
				jsons[x]["re_5"]=round(float(jsons[x]["online5"]/jsons[x]["re_5"])) if jsons[x]["re_5"]!=0 else 0
				jsons[x]["re_6"]=round(float(jsons[x]["online6"]/jsons[x]["re_6"])) if jsons[x]["re_6"]!=0 else 0	
		for item in jsons[:]:
			if item == "":
				jsons.remove(item)
	
		jsons=json.dumps(jsons)
		return jsons
