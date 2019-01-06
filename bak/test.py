#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
从资料库获取所有设备，然后计算近7天的cpu信息
aws cloudwatch get-metric-statistics --metric-name CPUUtilization --start-time 2016-10-10T04:00:00Z --end-time 2016-10-31T04:10:00Z --period 1800 --namespace AWS/EC2  --statistics Maximum --dimensions Name=InstanceId,Value=i-2a4a0312
'''

import os, sys, datetime
from MyLink import MyRep
import sys
reload(sys)
sys.setdefaultencoding('utf8')



def main():

        



    now_time = datetime.datetime.now()
    count = 0
    date_lst = []
    
    yes_date = now_time + datetime.timedelta(days=-1)
    yes_date = yes_date.strftime('%Y-%m-%d')
    
    for n in range(1):
        count = 1
        count2 = 2
        yes_time = now_time + datetime.timedelta(days=-count)
        qian_time = now_time + datetime.timedelta(days=-count2)
        date_lst.append([qian_time.strftime('%Y-%m-%dT04:00:00Z'), yes_time.strftime('%Y-%m-%dT04:00:00Z')])
        now_time = yes_time

    mysql = MyRep()
    sql = "select ins_id, privateip, ins_name,ins_tag from ec2_instance_pool where state='running'"



    if os.path.exists('./tmp'):
        pass        
    else:
        os.mkdir('./tmp')

    f=open('./tmp/%s.txt'%yes_date,'w')
    for i_id, ip, name, tag in mysql.result_lst(sql):
        for date in date_lst:
            cmd = "aws cloudwatch get-metric-statistics --metric-name CPUUtilization --start-time %s --end-time %s --period 86400 --namespace AWS/EC2  --statistics Maximum --dimensions Name=InstanceId,Value=%s" % (date[0], date[1], i_id) 
            result_str = os.popen(cmd).read().strip()
            result_dict = eval(result_str)
            each_day_result = []
            if result_dict:
                for item in result_dict['Datapoints']:
                    each_day_result.append(item['Maximum'])
                try:
                    #avg_cpu = sum(each_day_result)/len(each_day_result)
                    avg_cpu = max(each_day_result)
                except:
                    avg_cpu = 0.0
                print  >> f , "%s,%s,%s,%s,%s,%.2f"  %(ip, name.encode('utf-8'),tag, date[0].split('T')[0], date[1].split('T')[0], float(avg_cpu))
                print ip, name.encode('utf-8'),tag, date[0].split('T')[0], date[1].split('T')[0], '%.2f' % float(avg_cpu)
            else:
                print ip, name.encode('utf-8'), date[0].split('T')[0], date[1].split('T')[0], 'null'

    f.close()
    
if __name__ == '__main__':
    main()
