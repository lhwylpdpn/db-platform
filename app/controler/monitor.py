import os
import time
import datetime
def collect_data():
	value=[]
	#for wanggang
	pwd_yuan="/data1/bidata"
	print(pwd_yuan+"/LaunchPaymentAll.csv");
	print(pwd_yuan+"/1452827692979/Daily_lchy_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv");
	print(pwd_yuan+"/1452827692979/Daily_tfzh_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv");
	print(pwd_yuan+"/1452827692979/Daily_zbhs_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv");
	if  os.path.exists(pwd_yuan+"/LaunchPaymentAll.csv") and os.path.exists(pwd_yuan+"/1452827692979/Daily_lchy_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv") and os.path.exists(pwd_yuan+"/1452827692979/Daily_tfzh_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv") and os.path.exists(pwd_yuan+"/1452827692979/Daily_zbhs_2016-07-01~"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv"):
		
		statinfo=os.stat(pwd_yuan+"/LaunchPaymentAll.csv")
		#print(statinfo.st_mtime)
		value.append(["files",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["files","0"])
		
	#for zengliang

	pwd_yuan="/data1/bidata"
	print(pwd_yuan+"/tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv");
	print(os.path.exists(pwd_yuan+"/tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv"));
	if  os.path.exists(pwd_yuan+"/tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv"):
		
		statinfo=os.stat(pwd_yuan+"/tffy_"+str(datetime.datetime.now().strftime('%Y-%m-%d'))+".csv")
		#print(statinfo.st_mtime)
		value.append(["spend", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
	else:
		value.append(["spend","0"])


	#process id,monitor ,service_json_A,manager
	process_list = os.popen("ps -ef |grep monitor.py |awk '{print $2}'").readlines()
	print(len(process_list))
	if len(process_list)>2:
		value.append(["monitor",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
		#print(time.asctime("monitor",time.localtime(statinfo.st_mtime)))
	else:
		value.append(["monitor","0"])
	process_list = os.popen("ps -ef |grep service_json_A.py |awk '{print $2}'").readlines()
	print(len(process_list))
	if len(process_list)>2:
		value.append(["service_json_A",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
	else:
		value.append(["service_json_A","0"])
	process_list = os.popen("ps -ef |grep manager.py |awk '{print $2}'").readlines()
	print(len(process_list))
	if len(process_list)>3:
		value.append(["manager",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
	else:
		value.append(["manager","0"])

	#for nohup manager

	pwd_yuan="/var/www/zilong_new"
	if  os.path.exists(pwd_yuan+"/nohup.out"):
		
		statinfo=os.stat(pwd_yuan+"/nohup.out")
		#print(statinfo.st_mtime)
		value.append(["index", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
		#print(time.asctime(time.localtime(statinfo.st_mtime)))
	else:
		value.append(["index","0"])	
	# for json tongbu zengquexing

	pwd_yuan="/var/www/zilong_new/static/json"
	if  os.path.exists(pwd_yuan+"/status.json"):
		
		statinfo=os.stat(pwd_yuan+"/status.json")
		#print(statinfo.st_mtime)
		value.append(["json", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
		#print(time.asctime(time.localtime(statinfo.st_mtime)))
	else:
		value.append(["json","0"])	
	word="{"
	for x in xrange(0,len(value)):
		word+='"'+str(value[x][0])+'":"'+str(value[x][1])+'",'
	word=word[0:-1]
	word+="}"
	create_json(word,"monitor")
def create_json(word,name):
	file_object = open(os.getcwd()+'/../../static/json/'+name+'.json','w')
	file_object.write(word)
	file_object.close()
if __name__ == '__main__':
	while(1):
		collect_data()
		time.sleep(60)
