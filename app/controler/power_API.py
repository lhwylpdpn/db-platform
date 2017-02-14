coding=UTF-8
import sys
from flask import session
from app.db.dbBase import DBConnect
from Config import Config
# 非flask运行测试用
# import sys
# sys.path.append("..")
# from db.dbBase import DBConnect
# sys.path.append("../..")
# from Config import Config
# moke login function
def login_in_M(username,password):
	session['username'] = username
	result = '{"status":"0"}'
	return result


def login_in(username,password):
	user = username
	pwd = password
	result=""
	sql="SELECT status,id FROM user_info where username='"+user+"' and password='"+pwd+"' and  status in ('0','1');"
	#print(sql)
	conn = DBConnect.db_connect(Config.DATABASE_MAIN)
	cursor_login = conn.cursor()
	cursor_login.execute(sql)
	rs = cursor_login.fetchall()
	cursor_login.close()
	if len(rs)>=1:
		for r in rs:
			if r[0]=="0":
				session['username'] = username
				result='{"status":"0"}'
			if r[0]=="1":
				result='{"status":"1"}'
		login_log(r[1])
	elif len(rs)<1:
		result='{"status":"-1","body":"该用户名不存在或密码错误，请重新尝试"}'
		conn.close()
	

	return result


def login_log(userid):
	sql="insert into  login_info values ("+str(userid)+",now())"
	conn = DBConnect.db_connect(Config.DATABASE_MAIN)
	cursor_login_log = conn.cursor()
	cursor_login_log.execute(sql)
	cursor_login_log.close()
	conn.commit()
	conn.close()
#  更改密码部分###########################################################
def passwd_update(username,password):#强制更新传入用户新密码，后台修改传入密码为空
	user = username
	pwd = password
	result=""
	sql_1="select password from user_info where username='"+str(user)+"'"
	if pwd.strip()=="":
		sql_2 = "update user_info set password='1',user_up_time=now() ,status='1' where username='"+str(user)+"' and status='0'"
	else:
		sql_2 = "update user_info set password='"+str(pwd)+"',status='0' ,user_up_time=now() where username='"+str(user)+"' and status='1'"
	conn = DBConnect.db_connect(Config.DATABASE_MAIN)
	cursor = conn.cursor()
	cursor.execute(sql_1)
	rs = cursor.fetchall()
	if len(rs)>=1:
		for r in rs:
			if r[0]==str(pwd):
				result='{"status":"-1","body":"新密码不能与旧密码相同，请重新尝试"}'
				cursor.close()
				conn.close()
				return result
	else:
		result='{"status":"-1","body":"该用户名并不存在，请重新尝试"}'
		cursor.close()
		conn.close()
		return result
	try:
		cursor.execute(sql_2)
		cursor.close()
		conn.commit()
		conn.close()
		result='{"status":"0"}'
		return result
	except Exception, e:
		cursor.close()
		conn.close()
		result='{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'
		return result
################################################################################



# 获取用户权限接口########################################################
def power_list(usernames):# 输入需要获取权限的用户名、返回权限list，如果输入是空，返回所有
	users = ""
	power =[]
	result=""
	if len(usernames)==0:
		result='{"status":"-1","body":"suoyou shuju"}'
	elif len(usernames)>=1:
		users=",".join(map(str,usernames))
		print(users)
		return 1
	else:
		result='{"status":"-1","body":"系统存在问题，暂时无法操作，请联系管理员"}'
		return result


	sql="select username,power_user_list from power_info a ,user_info b where a.user_id=b.id and b.username in ()"

	

	return result 
################################################################################
if __name__ == '__main__':
	test=[1,3,4,5]
	print(power_list(test))
    

