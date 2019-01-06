#!/usr/bin/python

from ip_check_data import *

def ip_ccontent():
	list5_0 = db_data("10.0.5.1",0)
	list5_1 = db_data("10.0.5.1",1)
	list6_0 = db_data("10.0.6.1",0)
	list6_1 = db_data("10.0.6.1",1)

	for li in (list5_0,list5_1):
		for i in li:
			print i

ip_ccontent()
