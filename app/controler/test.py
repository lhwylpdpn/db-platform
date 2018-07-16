#!/usr/bin/python
# -*- coding: UTF-8 -*- 


import chardet
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')


if __name__ == '__main__':
	#print(u'\u7c73\u8fea'.decode("UTF-8"))
	a="归属人测试名,陈丽华"

	print(chardet.detect(a))
	t=a.split(u',')
	for r in t:
		print r

	# print(a.decode())
	# print(a.encode())
	# print(a.decode("GB2312"))
	# print(a.encode("GB2312"))
	# print(a.decode('unicode_escape'))
	# print(a.encode('unicode_escape'))

	# conn=pymysql.connect(host='localhost',user='root',passwd='123456',db='zilong_report',port=3306)
	# cur_1=conn.cursor()
	# #import_excel()
	# #import_excel_add()
	# import_csv()
	# export_media_1()
	# #user_info_create()
	# #export()
	# cur_1.close()
	# conn.commit()
	# conn.close()
	# print time.asctime(time.localtime(time.time()))
