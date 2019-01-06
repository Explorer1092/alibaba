# -*- coding: utf-8 -*-
#!/usr/bin/python
import smtplib, os, sys, datetime, subprocess
from email.mime.text import MIMEText
from ip_check_temp import *
mailto_list = ['wangfei1@vipkid.com.cn','zhanggong@vipkid.com.cn']
#mailto_list = ['wangfei1@vipkid.com.cn','zhanggong@vipkid.com.cn','libaoyang@vipkid.com.cn']
#mailto_list = ['wangfei1@vipkid.com.cn']
mail_host = "smtp.exmail.qq.com"
mail_user = "wangfei1@vipkid.com.cn"
mail_pass = "Wffeige18101335251"

def send_mail(to_list, sub):
    content = ip_content()
    me = "autopost"+ "<" + mail_user + ">"
    msg = MIMEText(content, _subtype='html', _charset='utf8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False



if __name__ == '__main__':
    if send_mail(mailto_list, " IP使用明细"):
        pass
    else:
        print "fail"
