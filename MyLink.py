#!/usr/bin/env python
'''
mysql connection
    
'''
import os
import mysql.connector

Bi_config = dict((['host', '10.0.1.131'], ['port', 3306], ['user', 'cp_read_user'], ['password', 'GiGhaBwlBgYI'], ['database', 'vipkid']))
Rep_config = dict((['host', '10.0.2.202'], ['port', 3306], ['user', 'op_data'], ['password', 'op_data2016'], ['database', 'op_data']))
Pro_config = dict((['host', 'pro.cecakn50ylo9.rds.cn-north-1.amazonaws.com.cn'], ['port', 3306], ['user', 'vipkid'], ['password', 'Vi1pkidDb_rootZAQ!'], ['database', 'vipkid']))

class MySQL(object):
    def __init__(self, config):
        self.config = config
        try:
            self.cnn = mysql.connector.connect(**self.config)
            self.cursor = self.cnn.cursor()
        except Exception, e:
            raise Exception("MySQL connect error, check my_config.")
    
    def result_lst(self, sql):
        try:
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
        except Exception, e:
            print e
            return 0
        return rs

    def commit(self, sql) :
        try:
            self.cursor.execute(sql)
            self.cnn.commit()
        except Exception, e:
            return 0
        return 1

    def __del__(self):
        try:
            self.cursor.close()
            self.cnn.close()
        except:
            pass

class MyRep(MySQL):
    def __init__(self):
        super(MyRep, self).__init__(Rep_config)
        
class MyBi(MySQL):
    def __init__(self):
        super(MyBi, self).__init__(Bi_config)
        #MySQL.__init__(self, Bi_config)

class MyPro(MySQL):
    def __init__(self):
        super(MyPro, self).__init__(Pro_config)

class MyDefine(MySQL):
    def __init__(self, configure):
        super(MyDefine, self).__init__(configure)
