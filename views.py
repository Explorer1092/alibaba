#coding=utf-8
from app import app 
from flask import Flask,render_template,request, abort, redirect, url_for,flash,escape,session
from flask.ext.login import login_required
import psutil,os,sys
from  commands import getoutput
import json
from . import cpu
from forms import * 
from cpu_avg_temp import * 
from cpu_max_temp import *
from ip_check_temp import *

reload(sys)
sys.setdefaultencoding('utf8')


@cpu.route('/', methods=['POST', 'GET'])
def index():
    return render_template('cpu_max.html')

@cpu.route('/cpumax', methods=['POST', 'GET'])
def cpumax():
    form=LoginForm()
    name = request.form['name']
    content=max_content(name)
    return render_template('cpu_max.html',content=content)

@cpu.route('/cpuavg', methods=['POST', 'GET'])
def cpuavg():
    return render_template('cpuavg.html')



@cpu.route('/cpuavg1', methods=['POST', 'GET'])
def cpuavg1():
    form=LoginForm()
    name = request.form['name']
    content=avg_content(name)
    return render_template('cpuavg.html',content=content)


@cpu.route('/ip', methods=['POST', 'GET'])
def ip_check():
    content=ip_content()
    return render_template('ip.html',content=content)


@cpu.route('/cpu_fenzu', methods=['POST', 'GET'])
def cpu_fenzu():
    return render_template('fenzu.html')


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

