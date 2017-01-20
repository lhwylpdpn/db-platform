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
		print(r)
	
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



	sql="SELECT a.date, case when  a.date<=date_sub(curdate(),interval 1 day)  then concat(ROUND(b.money_0*a.p/a.dis_spend*100,2),'%') else null end ,case when  a.date<=date_sub(curdate(),interval 2 day)  then concat(ROUND(b.money_1*a.p/a.dis_spend*100,2),'%') else null end,case when  a.date<=date_sub(curdate(),interval 3 day)  then concat(ROUND(b.money_2*a.p/a.dis_spend*100,2),'%') else null end ,case when  a.date<=date_sub(curdate(),interval 4 day)  then concat(ROUND(b.money_3*a.p/a.dis_spend*100,2),'%') else null end,case when  a.date<=date_sub(curdate(),interval 5 day)  then concat(ROUND(b.money_4*a.p/a.dis_spend*100,2),'%')else null end,case when  a.date<=date_sub(curdate(),interval 6 day)  then concat(ROUND(b.money_5*a.p/a.dis_spend*100,2),'%') else null end ,case when  a.date<=date_sub(curdate(),interval 7 day)  then concat(ROUND(b.money_6*a.p/a.dis_spend*100,2),'%') else null end ,case when  a.date<=date_sub(curdate(),interval 8 day)  then concat(ROUND(b.money_7*a.p/a.dis_spend*100,2),'%') else null end ,case when  a.date<=date_sub(curdate(),interval 9 day)  then concat(ROUND(b.money_8*a.p/a.dis_spend*100,2),'%') else null end ,case when  a.date<=date_sub(curdate(),interval 10 day)  then concat(ROUND(b.money_9*a.p/a.dis_spend*100,2),'%') else null end ,case when  a.date<=date_sub(curdate(),interval 11 day)  then concat(ROUND(b.money_10*a.p/a.dis_spend*100,2),'%')else null end, case when  a.date<=date_sub(curdate(),interval 12 day)  then concat(ROUND(b.money_11*a.p/a.dis_spend*100,2),'%')else null end ,case when  a.date<=date_sub(curdate(),interval 13 day)  then concat(ROUND(b.money_12*a.p/a.dis_spend*100,2),'%') else null end ,case when  a.date<=date_sub(curdate(),interval 14 day)  then concat(ROUND(b.money_13*a.p/a.dis_spend*100,2),'%') else null end ,case when  a.date<=date_sub(curdate(),interval 15 day)  then concat(ROUND(b.money_14*a.p/a.dis_spend*100,2),'%') else null end FROM `re_money` b RIGHT JOIN ( SELECT aa.*,0.686 as p FROM  (SELECT a.date,b.staff,a.channel_name,a.agent,b.dis_spend FROM  ad_action a LEFT JOIN  (SELECT DATE ,channel_name,agent,SUM(dis_spend) AS dis_spend ,staff FROM spend GROUP BY DATE,channel_name,agent ) b   ON a.date=b.date AND a.channel_name=b.channel_name AND a.agent=b.agent) aa  LEFT JOIN dis_result bb  ON aa.date=bb.date ORDER BY aa.date) a ON  a.date=b.date AND a.channel_name=b.channel_name AND a.agent=b.agent  order by a.channel_name ,a.agent ,a.date desc;"
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

	word="["
	for i in xrange(0,len(res)):
		word=word+'{'
		word=word+'"1":"'+str(date_[i])[0:10]+'",'+'"2":"'+str(staff[i])+'",'+'"3":"'+str(channel_name[i])+'",'+'"4":"'+str(agent[i])+'",'+'"5":"'+str(ad_click[i])+'",'
		word=word+'"6":"'+str(ad_action[i])+'",'+'"7":"'+str(ad_action_new[i])+'",'+'"8":"'+str(ad_account_new[i])+'",'+'"9":"'+str(ad_account_new_pay[i])+'",'+'"10":"'+str(ad_account_new_paymoney[i])+'",'
		word=word+'"11":"'+str(fufeilv[i])+'",'+'"cpa":"'+str(cpa[i])+'",'+'"mo_th":"'+str(dis_spend[i])+'",'
		word=word+'"120":"'+str(b_money_0[i])+'",'
		word=word+'"121":"'+str(b_money_1[i])+'",'
		word=word+'"122":"'+str(b_money_2[i])+'",'
		word=word+'"123":"'+str(b_money_3[i])+'",'
		word=word+'"124":"'+str(b_money_4[i])+'",'
		word=word+'"125":"'+str(b_money_5[i])+'",'
		word=word+'"126":"'+str(b_money_6[i])+'",'
		word=word+'"127":"'+str(b_money_7[i])+'",'
		word=word+'"128":"'+str(b_money_8[i])+'",'
		word=word+'"129":"'+str(b_money_9[i])+'",'
		word=word+'"130":"'+str(b_money_10[i])+'",'
		word=word+'"131":"'+str(b_money_11[i])+'",'
		word=word+'"132":"'+str(b_money_12[i])+'",'
		word=word+'"133":"'+str(b_money_13[i])+'",'
		word=word+'"134":"'+str(b_money_14[i])+'"'
		if i==len(res)-1:
			word=word+'}'+'\n'
		else:
			word=word+'}'+',\n'
	word=word+']'



	create_json(word.replace('"None"','""'))


	print("1ok")
	print time.asctime(time.localtime(time.time()))

def test():
	book=load_workbook('test.xlsx')
	export_sheet=book.get_sheet_by_name("test") 
	for i in range(3,export_sheet.max_row):

		for j in range(1,export_sheet.max_column):
	

			export_sheet.cell(row=i,column=j,value="")
	book.save('test.xlsx')




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


def create_json(word):
	file_object = open(os.getcwd()+'/../../static/json/test.json','w')
	file_object.write(word)
	file_object.close()

if __name__ == '__main__':
	while(1):
		try:
			conn=pymysql.connect(host='localhost',user='root',passwd='PkBJ2016@_*#',db='zilong_report',port=3306)
			cur_1=conn.cursor()
			import_excel()
			export()

			cur_1.close()
			conn.commit()
			conn.close()
			print time.asctime(time.localtime(time.time()))
			test_ok()
		except Exception, e:
			print(e)
			
		print time.asctime(time.localtime(time.time()))
		time.sleep(3000)

	# sql="insert into zilong_report.re_money values (truncate zilong_report.re_money;insert into zilong_report.re_money values ('2016-11-06','Aduu','Aduu','6.0','6.0','6.0','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-');insert into zilong_report.re_money values ('2016-11-04','Aduu','Aduu','0.0','6.0','6.0','6.0','6.0','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-');insert into zilong_report.re_money values ('2016-11-02','Aduu','Aduu','8.0','8.0','8.0','8.0','8.0','8.0','8.0','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-');"
	# sql=sql.strip(',')
	# sql=sql+");"
	# print(sql.replace("-","0"))