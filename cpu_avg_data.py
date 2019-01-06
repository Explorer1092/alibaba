# -*- coding: utf-8 -*-
#!/usr/bin/python
import os,datetime

def sort_lst(name):
    li=[]
    f=open('/vipkid/lianxi/app/cpu/tmp/avg/%s.txt'%name,'r')
    line=f.read()
    for i in line.split('\n'):
        i=i.strip()
        i=i.split(',')
        if i==['']:
            i.remove('')
        li.append(i)
    li.remove([])
    #print len(li)
    
    for i in li :
#        print i
        i[-1]=float(i[-1])

    li=sorted(li,key=lambda li:li[2])        
    return  li

def fenduan(name):
    li=sort_lst(name)
    li0=[]
    li1=[]
    li2=[]
    li3=[]
    li4=[]
    li5=[]
    li6=[]
    li7=[]
    li8=[]
    li9=[]
    li10=[]
    li11=[]
    li_zong=[]

    for i in li:
        if float(i[-1]) < 1:
            li0.append(i)
        elif float(i[-1]) >= 1 and float(i[-1]) < 10:
            li1.append(i)
        elif float(i[-1]) >= 10 and float(i[-1]) < 20:
            li2.append(i)
        elif float(i[-1]) >= 20 and float(i[-1]) < 30:
            li3.append(i)
        elif float(i[-1]) >= 30 and float(i[-1]) < 40:
            li4.append(i)
        elif float(i[-1]) >= 40 and float(i[-1]) < 50:
            li5.append(i)
        elif float(i[-1]) >= 50 and float(i[-1]) < 60:
            li6.append(i)
        elif float(i[-1]) >= 60 and float(i[-1]) < 70:
            li7.append(i)
        elif float(i[-1]) >= 70 and float(i[-1]) < 80:
            li8.append(i)
        elif float(i[-1]) >= 80 and float(i[-1]) < 90:
            li9.append(i)
        elif float(i[-1]) >= 90 and float(i[-1]) < 100:
            li10.append(i)
        elif float(i[-1]) == 100:
            li11.append(i)
        else:
            print "error"
    list_zong=[li0,li1,li2,li3,li4,li5,li6,li7,li8,li9,li10,li11]
 #   print list_zong
    return list_zong

