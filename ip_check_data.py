#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import os
db=MySQLdb.connect('127.0.0.1','wangfei','rootroot','op_data')
cursor=db.cursor()

def db_data(gate,stat):
	sql='select * from ip_pool where gateway = "%s" and  status = %d;'%(gate,stat)
	li = [] 
	cursor.execute(sql)
	line=cursor.fetchall()
	for i in line:
		i=list(i)
		li.append(i)

	for i in li:
		#print i
		if i[2] == 1:
			i[2] = "已使用"
		else: 
			i[2] = "未使用"
		if i[3] == 0:
			i[3] = "物理ip"
		else:
			i[3] = "虚拟ip"
		
	return li


