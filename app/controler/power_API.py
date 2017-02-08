# coding=UTF-8
import sys
sys.path.append("..")
import db.dbBase
sys.path.append("../..")
import Config

conn = db.dbBase.DBConnect().db_connect(Config.Config().DATABASE_MAIN)
cursor_login = conn.cursor()
cursor_login_log = conn.cursor()
def login(username,password):
	user = username
	pwd = password
	result=""
	sql="SELECT status,id FROM user_info where username='"+user+"' and password='"+pwd+"' and  status in ('0','1');"
	#print(sql)
	cursor_login.execute(sql)
	rs = cursor_login.fetchall()
	cursor_login.close()
	if len(rs)>=1:
		for r in rs:
			if r[0]=="0":

				result="{'status':'0'}"
			if r[0]=="1":
				result="{'status':'1'}"
		login_log(r[1])
	elif len(rs)<1:
		result="{'status':‘-1’,'body':'该用户名不存在或密码错误，请重新尝试'}"
		conn.close()
	

	return result


def login_log(userid):
	sql="insert into  login_info values ("+str(userid)+",now())"
	cursor_login_log = conn.cursor()
	cursor_login_log.execute(sql)
	cursor_login_log.close()
	conn.commit()
	conn.close()

if __name__ == '__main__':
	print(login('liuhao','12345678'))
    

