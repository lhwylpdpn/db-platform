#!/usr/bin/python
# -*- coding: UTF-8 -*- 



import pymysql
import os
import sys
import time
import csv
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')
def import_csv():
	test = []
	test= os.listdir("/Users/liuhao/Desktop/zilong/app/controler")
	newlist=[]
	statinfo=[]
	for names in test:

		if names.endswith(".csv"):
			#statinfo.append(os.stat(os.getcwd()+"/src/"+names).st_ctime)
			newlist.append(names)
	for r in newlist:
		if  not r.find("Daily_xzff_detail_2017-02-27"):#投放转化
			filename=""+r
			filenode=open(filename)
			reader=csv.reader(filenode)
			sql="truncate zilong_report.ad_detail_IDFA;insert into zilong_report.ad_detail_IDFA values "
			for row in reader:
				sql=sql+"('"+"','".join(row)+"'),"
			sql=sql.strip(',')+";"
			print("6sql ok")
				#time.sleep(10)
			cur_1.execute(sql)
def import_excel_add():
	test = []
	test= os.listdir("/data1/bidata/")
	context=[]
	newlist=[]
	sql=""
	statinfo=[]
	for names in test:

		if names.endswith(".csv"):
			#statinfo.append(os.stat(os.getcwd()+"/src/"+names).st_ctime)
			newlist.append(names)

	for r in newlist:
		if  not r.find("tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))):
			filename="/data1/bidata/"+r
			print(r)
			filenode=open(filename)
			reader=csv.reader(filenode)
			reader.next()
			for row in reader:
				sql=sql+"delete from spend  where date='"+str(row[0])+"' and channel_name='"+str(row[4])+"' and agent='"+str(row[5])+"' and gamename='"+str(row[1])+"' and platform='"+str(row[2])+"' and class_A='"+str(row[3])+"' and class_ad='"+str(row[6])+"';"
				sql=sql+"insert into spend values (null,'"+str(row[0])+"','"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"','"+str(row[4])+"','"+str(row[5])+"','"+str(row[6])+"','"+str(row[7])+"','"+str(row[8])+"','"+str(row[9])+"','"+str(row[9])+"','"+str(row[10])+"','"+str(row[11])+"','"+str(row[12])+"','"+str(row[13])+"');"
				cur_1.execute(sql)
			print("5sql ok")
def import_excel():
	test = []
	test= os.listdir("/data1/bidata/1452827692979/")

	newlist=[]
	statinfo=[]
	for names in test:

		if names.endswith(".csv"):
			#statinfo.append(os.stat(os.getcwd()+"/src/"+names).st_ctime)
			newlist.append(names)

	for r in newlist:

		if  not r.find("Daily_lchy_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))):#投放转化
			filename="/data1/bidata/1452827692979/"+r
			filenode=open(filename)
			reader=csv.reader(filenode)
			sql="truncate zilong_report.retention;insert into zilong_report.retention values "
			for row in reader:
				sql=sql+"('"+"','".join(row)+"'),"
			sql=sql.strip(',')+";"
			print("1sql ok")
				#time.sleep(10)
			cur_1.execute(sql)
	
		if  not r.find("Daily_tfzh_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))):#投放转化
			filename="/data1/bidata/1452827692979/"+r
			filenode=open(filename)
			reader=csv.reader(filenode)
			sql="truncate zilong_report.ad_action;insert into zilong_report.ad_action values "
			for row in reader:
				sql=sql+"('"+"','".join(row)+"'),"
			sql=sql.strip(',')+";"
			print("2sql ok")
				#time.sleep(10)
			cur_1.execute(sql)

		if  not r.find("Daily_zbhs_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))):#投放转化
			filename="/data1/bidata/1452827692979/"+r
			filenode=open(filename)
			reader=csv.reader(filenode)
			sql="truncate zilong_report.re_money;insert into zilong_report.re_money values "
			for row in reader:
				sql=sql+"('"+"','".join(row)+"'),"
			sql=sql.strip(',')+";"
			print("3sql ok")
				#time.sleep(10)
			cur_1.execute(sql)

		if  not r.find("LaunchPaymentAll"):#投放转化
			filename="/data1/bidata/"+r
			filenode=open(filename)
			reader=csv.reader(filenode)
			sql="truncate zilong_report.spend;insert into zilong_report.spend values "
			for row in reader:
				sql=sql+"('"+"','".join(row)+"'),"
			sql=sql.strip(',')+";"
			print("4sql ok ")
			cur_1.execute(sql)


def user_info_create():
	user_DB=[]
	user_file=[]
	sql=""
	sql_get_file="SELECT staff FROM spend where length(staff)>1 group by staff "
	sql_get_user_info="SELECT username FROM user_info group by username"
	cur_1.execute(sql_get_file)
	rs=cur_1.fetchall()

	if len(rs)>0:
		for r in rs:
			user_file.append(r[0])
	cur_1.execute(sql_get_user_info)
	rs=cur_1.fetchall()

	if len(rs)>0:
		for r in rs:
			user_DB.append(r[0])

	for x in xrange(0,len(user_file)):
		if user_file[x] not in user_DB:
			sql=sql+"insert into user_info values(null,'"+user_file[x]+"',1,now(),1,now());insert into power_info select id,username from user_info where status=1 and username='"+user_file[x]+"';"
	if len(sql)>1:
		cur_1.execute(sql)
def export_media_1():
	sql="""SELECT 
a.channel_name,a.agent,b.staff,a.date,
ad_click,
ad_action,
ad_action_new ,
a.ad_account_new,
a.double_new , 
a.huiliu ,
a.fufeizhanghao
,sum(b.dis_spend),
round(sum(b.dis_spend)/a.ad_account_new,2) as cpa 
,a.money 

FROM (select DATE_FORMAT(substring_index(ad_action_time," ",1),"%Y-%m-%d") as date,
channel_name,agent,count(game_userid) as ad_account_new,
sum(case when a.game_type='ÐÂÔö' then 1 else 0 end) as double_new , 
sum(case when a.game_type='»ØÁ÷' then 1 else 0 end) as huiliu,
sum(case when a.game_pay_money>0 then 1 else 0 end) as fufeizhanghao,
sum(game_pay_money) as money
from ad_detail_IDFA a group by DATE_FORMAT(substring_index(ad_action_time," ",1),"%Y-%m-%d"),channel_name,agent) a,
spend b,(select DATE_FORMAT(substring_index(date," ",1),"%Y-%m-%d") as date_time,channel_name,agent,sum(ad_click) as ad_click,sum(ad_action) as ad_action,sum(ad_action_new) as ad_action_new from ad_action group by date,channel_name,agent) c 
where a.date=c.date_time
and a.channel_name=c.channel_name 
and a.agent=c.agent
and a.date=b.date 
and a.channel_name=b.channel_name 
and a.agent=b.agent
group by a.date,a.channel_name,a.agent"""
	cur_1.execute(sql)
	res=cur_1.fetchall()
	word="[\n"
	if len(res)>1:
		for r in res:
			word=word+'{'
			word=word+'"channel_name":"'+str(r[0])+'",'
			word=word+'"agent":"'+str(r[1])+'",'
			word=word+'"staff":"'+str(r[2])+'",'
			word=word+'"date_time":"'+str(r[3])+'",'
			word=word+'"ad_click":"'+str(r[4])+'",'
			word=word+'"ad_action":"'+str(r[5])+'",'
			word=word+'"ad_action_new":"'+str(r[6])+'",'
			word=word+'"ad_account_new":"'+str(r[7])+'",'
			word=word+'"double_new":"'+str(r[8])+'",'
			word=word+'"back_user":"'+str(r[9])+'",'
			word=word+'"paid_account":"'+str(r[10])+'",'
			word=word+'"fufeilv":"'+str(round(float(r[10])/float(r[7])*100,2))+'",'
			word=word+'"spend":"'+str(r[11])+'",'
			word=word+'"CPA":"'+str(r[12])+'",'
			word=word+'"cumulative_flow":"'+str(r[13])+'",'
			word=word+'"dis":"'+str(48.02)+'",'
			word=word+'"cumulative_moeny":"'+str(float(r[13])*48.02/100)+'",'
			word=word+'"ROI":"'+str(round(float(r[13])*48.02/100/float(r[11])))+'"'
			word=word+'}'+',\n'
		word=word[0:-2]+"\n]"
		create_json(word,"media_1")
def export():
	date_=[]
	channel_name=[]
	staff=[]
	ad_click=[]
	ad_action=[]
	ad_action_new=[]
	ad_account_new=[]
	ad_account_new_pay=[]
	ad_account_new_paymoney=[]
	fufeilv=[]
	cpa=[]
	dis_spend=[]
	agent=[]
	
	#sql="DROP TABLE IF EXISTS temp1;CREATE TABLE temp1 AS SELECT * FROM (SELECT DATE_FORMAT(b.DATE,'%Y-%m-%d') AS DATE,a.staff,b.channel_name,b.agent FROM `ad_action` b LEFT JOIN spend a ON a.date=b.date AND a.channel_name=b.channel_name AND a.agent=b.agent   UNION  SELECT DATE_FORMAT(a.DATE,'%Y-%m-%d') AS DATE,a.staff,a.channel_name,a.agent FROM `ad_action` b RIGHT JOIN spend a ON a.date=b.date AND a.channel_name=b.channel_name AND a.agent=b.agent  ) a order by date,channel_name,agent;delete from temp1 where date is null"
	#cur_1.execute(sql)
	sql="SELECT a.date,a.channel_name,b.staff, a.agent,a.ad_click,a.ad_action,a.ad_action_new,a.ad_account_new,a.ad_account_new_pay,a.ad_account_new_paymoney, a.fufeilv,ROUND(b.dis_spend/a.ad_account_new,2) AS cpa,b.dis_spend  FROM  (SELECT a.date,a.channel_name,a.agent,a.ad_click,a.ad_action,a.ad_action_new,a.ad_account_new,a.ad_account_new_pay,a.ad_account_new_paymoney ,CONCAT(ROUND(a.ad_account_new_pay/a.ad_account_new*100,2),'%') AS fufeilv FROM ad_action a  ) a left join (SELECT DATE ,channel_name,agent,staff,SUM(dis_spend) AS dis_spend FROM spend GROUP BY DATE,channel_name,agent ) b on a.date=b.date AND a.channel_name=b.channel_name AND a.agent=b.agent ORDER BY a.channel_name,a.agent,a.date desc"
	cur_1.execute(sql)
	res=cur_1.fetchall()

	if len(res)>1:


		for r in res:
			date_.append(r[0])
			channel_name.append(r[1])
			staff.append(r[2])
			agent.append(r[3])
			ad_click.append(r[4])
			ad_action.append(r[5])
			ad_action_new.append(r[6])
			ad_account_new.append(r[7])
			ad_account_new_pay.append(r[8])
			ad_account_new_paymoney.append(r[9])
			fufeilv.append(r[10])
			cpa.append(r[11])
			dis_spend.append(r[12])



	sql="SELECT case when  a.date<=date_sub(curdate(),interval 1 day)  then concat(ROUND(b.money_0*a.p/a.dis_spend*100,2),'') else null end ,case when  a.date<=date_sub(curdate(),interval 2 day)  then concat(ROUND(b.money_1*a.p/a.dis_spend*100,2),'') else null end,case when  a.date<=date_sub(curdate(),interval 3 day)  then concat(ROUND(b.money_2*a.p/a.dis_spend*100,2),'') else null end ,case when  a.date<=date_sub(curdate(),interval 4 day)  then concat(ROUND(b.money_3*a.p/a.dis_spend*100,2),'') else null end,case when  a.date<=date_sub(curdate(),interval 5 day)  then concat(ROUND(b.money_4*a.p/a.dis_spend*100,2),'')else null end,case when  a.date<=date_sub(curdate(),interval 6 day)  then concat(ROUND(b.money_5*a.p/a.dis_spend*100,2),'') else null end ,case when  a.date<=date_sub(curdate(),interval 7 day)  then concat(ROUND(b.money_6*a.p/a.dis_spend*100,2),'') else null end ,case when  a.date<=date_sub(curdate(),interval 8 day)  then concat(ROUND(b.money_7*a.p/a.dis_spend*100,2),'') else null end ,case when  a.date<=date_sub(curdate(),interval 9 day)  then concat(ROUND(b.money_8*a.p/a.dis_spend*100,2),'') else null end ,case when  a.date<=date_sub(curdate(),interval 10 day)  then concat(ROUND(b.money_9*a.p/a.dis_spend*100,2),'') else null end ,case when  a.date<=date_sub(curdate(),interval 11 day)  then concat(ROUND(b.money_10*a.p/a.dis_spend*100,2),'')else null end, case when  a.date<=date_sub(curdate(),interval 12 day)  then concat(ROUND(b.money_11*a.p/a.dis_spend*100,2),'')else null end ,case when  a.date<=date_sub(curdate(),interval 13 day)  then concat(ROUND(b.money_12*a.p/a.dis_spend*100,2),'') else null end ,case when  a.date<=date_sub(curdate(),interval 14 day)  then concat(ROUND(b.money_13*a.p/a.dis_spend*100,2),'') else null end ,case when  a.date<=date_sub(curdate(),interval 15 day)  then concat(ROUND(b.money_14*a.p/a.dis_spend*100,2),'') else null end FROM `re_money` b RIGHT JOIN ( SELECT aa.*,0.686 as p FROM  (SELECT a.date,b.staff,a.channel_name,a.agent,b.dis_spend FROM  ad_action a LEFT JOIN  (SELECT DATE ,channel_name,agent,SUM(dis_spend) AS dis_spend ,staff FROM spend GROUP BY DATE,channel_name,agent ) b   ON a.date=b.date AND a.channel_name=b.channel_name AND a.agent=b.agent) aa  LEFT JOIN dis_result bb  ON aa.date=bb.date ORDER BY aa.date) a ON  a.date=b.date AND a.channel_name=b.channel_name AND a.agent=b.agent  order by a.channel_name ,a.agent ,a.date desc;"
	cur_1.execute(sql)
	res=cur_1.fetchall()
	b_money_0=[]
	b_money_1=[]
	b_money_2=[]
	b_money_3=[]
	b_money_4=[]
	b_money_5=[]
	b_money_6=[]
	b_money_7=[]
	b_money_8=[]
	b_money_9=[]
	b_money_10=[]
	b_money_11=[]
	b_money_12=[]
	b_money_13=[]
	b_money_14=[]
	print(len(res))
	if len(res)>1:
		for r in res:
			b_money_0.append(r[0])
			b_money_1.append(r[1])
			b_money_2.append(r[2])
			b_money_3.append(r[3])
			b_money_4.append(r[4])
			b_money_5.append(r[5])
			b_money_6.append(r[6])
			b_money_7.append(r[7])
			b_money_8.append(r[8])
			b_money_9.append(r[9])
			b_money_10.append(r[10])
			b_money_11.append(r[11])
			b_money_12.append(r[12])
			b_money_13.append(r[13])
			b_money_14.append(r[14])






	#2017.3.9  增加留存部分的输出
	
	sql="""SELECT retention1*100,retention2*100,retention3*100,retention4*100,retention5*100,retention6*100 FROM  ad_action a 
 	LEFT JOIN
 	(select * from retention group by channel_name ,agent ,_date having count(*)=1) b
 	on a.date=b._date
 	and a.channel_name=b.channel_name
 	and a.agent=b.agent
 	order by a.channel_name ,a.agent ,a.date desc"""	
 	cur_1.execute(sql)
	res2=cur_1.fetchall()
	retention1=[]
	retention2=[]
	retention3=[]
	retention4=[]
	retention5=[]
	retention6=[]
	print(len(res2))
	if len(res2)>1:
		for r in res:
			retention1.append(r[0])
			retention2.append(r[1])
			retention3.append(r[2])
			retention4.append(r[3])
			retention5.append(r[4])
			retention6.append(r[5])




	word="["
	for i in xrange(0,len(res)):
		word=word+'{'
		word=word+'"1":"'+str(date_[i])[0:10]+'",'+'"2":"'+str(staff[i])+'",'+'"3":"'+str(channel_name[i])+'",'+'"4":"'+str(agent[i])+'",'+'"5":"'+str(ad_click[i])+'",'
		word=word+'"6":"'+str(ad_action[i])+'",'+'"7":"'+str(ad_action_new[i])+'",'+'"8":"'+str(ad_account_new[i])+'",'+'"9":"'+str(ad_account_new_pay[i])+'",'+'"10":"'+str(ad_account_new_paymoney[i])+'",'
		word=word+'"ffl":"'+str(fufeilv[i])+'",'+'"cpa":"'+str(cpa[i])+'",'+'"mo_th":"'+str(dis_spend[i])+'",'
		word=word+'"hs0":"'+str(b_money_0[i])+'",'
		word=word+'"hs1":"'+str(b_money_1[i])+'",'
		word=word+'"hs2":"'+str(b_money_2[i])+'",'
		word=word+'"hs3":"'+str(b_money_3[i])+'",'
		word=word+'"hs4":"'+str(b_money_4[i])+'",'
		word=word+'"hs5":"'+str(b_money_5[i])+'",'
		word=word+'"hs6":"'+str(b_money_6[i])+'",'
		word=word+'"hs7":"'+str(b_money_7[i])+'",'
		#word=word+'"hs8":"'+str(b_money_8[i])+'",'
		#word=word+'"hs9":"'+str(b_money_9[i])+'",'
		#word=word+'"hs10":"'+str(b_money_10[i])+'",'
		#word=word+'"hs11":"'+str(b_money_11[i])+'",'
		#word=word+'"hs12":"'+str(b_money_12[i])+'",'
		#word=word+'"hs13":"'+str(b_money_13[i])+'",'
		#word=word+'"hs14":"'+str(b_money_14[i])+'"'
		word=word+'"lc1":"'+str(retention1[i])+'",'
		word=word+'"lc2":"'+str(retention2[i])+'",'
		word=word+'"lc3":"'+str(retention3[i])+'",'
		word=word+'"lc4":"'+str(retention4[i])+'",'
		word=word+'"lc5":"'+str(retention5[i])+'",'
		word=word+'"lc6":"'+str(retention6[i])+'",'		
		if i==len(res)-1:
			word=word+'}'+'\n'
		else:
			word=word+'}'+',\n'
	word=word+']'



	create_json(word.replace('"None"','""'),"test")


	print("1ok")
	print time.asctime(time.localtime(time.time()))



################ 为了web计算时间所用##############################


time1=datetime.datetime.now()
def test_start():
	file_object = open('../../static/json/status.json','w')
	time1= datetime.datetime.now()#starttime
	file_object.write('{"update_time":"'+str(time1)+'","status":0,"time":"0"}')
	print("Daily_lchy_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d')))
	file_object.close()
def test_ok():
	file_object = open('../../static/json/status.json','w')
	time2=datetime.datetime.now()#oktime
	file_object.write('{"time_":"'+str(time2)+'"}')

	file_object.close()
def test_er():
	file_object = open('../../static/json/status.json','w')
	time3= datetime.datetime.now()#errtime
	file_object.write('{"update_time":"'+str(time3)+'","status":2,"time":"'+str((time3 -time1 ).seconds)+'"}')

	file_object.close()


def create_json(word,name):
	file_object = open(os.getcwd()+'/../../static/json/'+name+'.json','w')
	file_object.write(word)
	file_object.close()

if __name__ == '__main__':
	while(1):
		try:
			conn=pymysql.connect(host='localhost',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306)
			cur_1=conn.cursor()
			import_excel()
			import_excel_add()
			user_info_create()
			export()
			cur_1.close()
			conn.commit()
			conn.close()
			print time.asctime(time.localtime(time.time()))
			test_ok()
		except Exception, e:
			print(e)
			
		print time.asctime(time.localtime(time.time()))
		time.sleep(900)

	# conn=pymysql.connect(host='localhost',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306)
	# cur_1=conn.cursor()
	# #import_excel()
	# import_excel_add()
	# #user_info_create()
	# #export()
	# cur_1.close()
	# conn.commit()
	# conn.close()
	# print time.asctime(time.localtime(time.time()))
