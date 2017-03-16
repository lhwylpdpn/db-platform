import os
import time
import datetime
def collect_data():
	value=[]
	#for wanggang
	pwd_yuan="/Users/liuhao/Desktop/zilong/app/controler"
	if  os.path.exists(pwd_yuan+"/service_json_A.py") and os.path.exists(pwd_yuan+"/service_json_A.py") and os.path.exists(pwd_yuan+"/service_json_A.py") and os.path.exists(pwd_yuan+"/service_json_A.py"):
		
		statinfo=os.stat(pwd_yuan+"/service_json_A.py")
		#print(statinfo.st_mtime)
		value.append(["files",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
		print(time.asctime(time.localtime(statinfo.st_mtime)))
	else:
		value.append(0)
		
	#for zengliang

	pwd_yuan="/Users/liuhao/Desktop/zilong/app/controler"
	if  os.path.exists(pwd_yuan+"/service_json_A.py") and os.path.exists(pwd_yuan+"/service_json_A.py") and os.path.exists(pwd_yuan+"/service_json_A.py") and os.path.exists(pwd_yuan+"/service_json_A.py"):
		
		statinfo=os.stat(pwd_yuan+"/service_json_A.py")
		#print(statinfo.st_mtime)
		value.append(["spend", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
		print(time.asctime(time.localtime(statinfo.st_mtime)))
	else:
		value.append(0)


	#process id,monitor ,service_json_A,manager
	process_list = os.popen("ps -ef |grep monitor.py |awk '{print $2}'").readlines()
	if len(process_list)>1:
		value.append(["monitor",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
		#print(time.asctime("monitor",time.localtime(statinfo.st_mtime)))
		print(process_list[0])
	process_list = os.popen("ps -ef |grep service_json_A.py |awk '{print $2}'").readlines()
	if len(process_list)>1:
		value.append(["service_json_A",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
		#print(time.asctime("service_json_A",time.localtime(statinfo.st_mtime)))
		print(process_list[0])
	process_list = os.popen("ps -ef |grep manager.py |awk '{print $2}'").readlines()
	if len(process_list)>1:
		value.append(["manager",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))])
		#print(time.asctime("manager",time.localtime(statinfo.st_mtime)))
		print(process_list[0])

	#for nohup manager

	pwd_yuan="/Users/liuhao/Desktop/zilong/app/controler"
	if  os.path.exists(pwd_yuan+"/service_json_A.py") and os.path.exists(pwd_yuan+"/service_json_A.py") and os.path.exists(pwd_yuan+"/service_json_A.py") and os.path.exists(pwd_yuan+"/service_json_A.py"):
		
		statinfo=os.stat(pwd_yuan+"/service_json_A.py")
		#print(statinfo.st_mtime)
		value.append(["index", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
		print(time.asctime(time.localtime(statinfo.st_mtime)))
	else:
		value.append(0)	
	# for json tongbu zengquexing

	pwd_yuan="/Users/liuhao/Desktop/zilong/app/controler"
	if  os.path.exists(pwd_yuan+"/service_json_A.py") and os.path.exists(pwd_yuan+"/service_json_A.py") and os.path.exists(pwd_yuan+"/service_json_A.py") and os.path.exists(pwd_yuan+"/service_json_A.py"):
		
		statinfo=os.stat(pwd_yuan+"/service_json_A.py")
		#print(statinfo.st_mtime)
		value.append(["json", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(statinfo.st_mtime))])
		print(time.asctime(time.localtime(statinfo.st_mtime)))
	else:
		value.append(0)
	word="{"
	for x in xrange(0,len(value)):
		word+='"'+value[x][0]+'":"'+value[x][1]+'",'
	word=word[0:-1]
	word+="}"
	create_json(word,"monitor")
def create_json(word,name):
	file_object = open(os.getcwd()+'/../../static/json/'+name+'.json','w')
	file_object.write(word)
	file_object.close()
if __name__ == '__main__':
	collect_data()

