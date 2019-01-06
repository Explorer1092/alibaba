# -*- coding: utf-8 -*-
#!/usr/bin/python
import smtplib, os, sys, datetime, subprocess
from ip_check_data import *


def ip_content():
	list5_0 = db_data("10.0.5.1",0)
	list5_1 = db_data("10.0.5.1",1)
	list6_0 = db_data("10.0.6.1",0)
	list6_1 = db_data("10.0.6.1",1)



	content_data5 = ''
	for li in (list5_1,list5_0):
		for i in li: 
			content_data5 += '''
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
<font color='black'>%s</font>
</td>
</tr>
'''%(i[1],i[2],i[3],i[4])




	content_data6 = ''
	for li in (list6_1,list6_0):
		for i in li: 
			content_data6 += '''
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
<font color='black'>%s</font>
</td>
</tr>'''%(i[1],i[2],i[3],i[4])


	content = '''
<div id="body5">
<center>
<table width="700" border="1" cellpadding="0" cellspacing="0">

<caption> ip 使用率明细 </caption>
<div id="head">

<tr>
<th>IP</th><th>已用</th><th>未使用</th>
</tr>

<tr>
<td style='text-align:center'><font color='black'><a href='#body5'>10.0.5 网段</a></font></td>
<td style='text-align:center'><font color='black'>%s</font></td>
<td style='text-align:center'><font color='black'>%s</font></td>
<tr>


<tr>
<td style='text-align:center'><font color='black'><a href='#body6'>10.0.6 网段</a></font></td>
<td style='text-align:center'><font color='black'>%s</font></td>
<td style='text-align:center'><font color='black'>%s</font></td>
<tr>

</table>
</center>

<div id="body5" href='#head'>
<center>
<table width="700" border="1" cellpadding="0" cellspacing="0">
<caption> <a href="#head">10.0.5网段 使用信息 </a></caption>
<td style='text-align:center'><font color='black'>IP</font></td>
<td style='text-align:center'><font color='black'>状态</font></td>
<td style='text-align:center'><font color='black'>类型</font></td>
<td style='text-align:center'><font color='black'>网关</font></td>
%s
</table>
</center>
</div>


<div id="body6" href='#head'>
<center>
<table width="700" border="1" cellpadding="0" cellspacing="0">
<caption><a href='#head'> 10.0.6网段 使用信息</a> </caption>
<td style='text-align:center'><font color='black'>IP</font></td>
<td style='text-align:center'><font color='black'>状态</font></td>
<td style='text-align:center'><font color='black'>类型</font></td>
<td style='text-align:center'><font color='black'>网关</font></td>

%s
</table>
</center>
</div>
</div>
'''%(len(list5_1),len(list5_0),len(list6_1),len(list6_0),content_data5,content_data6)
	return content
