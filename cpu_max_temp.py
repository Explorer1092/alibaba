# -*- coding: utf-8 -*-
#!/usr/bin/python
import smtplib, os, sys, datetime, subprocess
from email.mime.text import MIMEText
from cpu_max_data import *

#name = '2016-12-01'
def max_content(name):
	list1=fenduan(name)
	content= '' 
	###--1--###
	range_list=['0-1','1-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100','=100']
	content_range = ''
	number = 0
	for k in range(len(list1)):
		number = number + len(list1[k])
		content_range += '''
<tr>
<td style='width:150px;text-align:center'>
<font color='black'><a href="#ct%s">%s</a></font>
</td>
<td style='width:150px;text-align:center'>
<font color='black'>%s</font>
</td>
</tr>
'''%(k,range_list[k],len(list1[k]))



	###--mingxi--###

	#content_pertable = ''
	#for n in range(12):	
	#	content_perlist	=''
	#	for i in list1[n]:
	#		content_perlist += '''
	content_pertable = ''
	for n in range(len(list1)):	
		content_perlist	=''
		for i in list1[n]:
			content_perlist += '''
<tr>
<td style='width:150px;text-align:center'>
<font color='black'>%s</font>
</td> 

<td style='text-align:center'>
<font color='black'>%s</font>
</td>

<td style='text-align:center'>
<font color='black'>%s</font>
</td>

<td style='text-align:center'>
<font color='red'>%s</font>
</td>
</tr>
'''%(i[0],i[1],i[2],i[-1])
################################################
		content_pertable += '''
	<div id="ct%s">
	<a name="ct%s">
	<center>
	<table border="1" cellpadding="0" width="700" cellspacing="0">
  <caption><a href="#head">  CPU使用率%s明细  count(%s)</caption>
  <thead>
  <tr>
    <th>HOST</th>
    <th>Name</th>
    <th>Tag</th>
    <th>Max(cpu utilization)</th>
    </tr>
    %s
  </thead>
</table>
</center>
</div>
<hr style="height:1px;border:none;border-top:1px solid #555555;" />
'''%(n,n,range_list[n],len(list1[n]),content_perlist)


	content = '''
<div>
<center>
<table width="400" border="1" cellpadding="0" cellspacing="0">
<caption>%s CPU 使用率明细  count(%s) </caption>
  <tr>
    <th>Range(cpu utilization)</th>
    <th>Number</th>
    </tr>
<div id="head">
%s
</table>
</center>
</div>

    %s
''' %(list1[1][1][-2],number,content_range,content_pertable)
	#content_return = content_huizong + content_mingxi

	return content
