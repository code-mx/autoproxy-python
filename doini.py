#!/usr/bin/env python
# -*- coding:gb2312 -*-

#Filename: doini.py
#Author: KING RING
#Email:shuichon@qq.com
#Version:1.0

'''ini文件格式
内含一个proxylist的section，格式为工作环境的地址workip对应
于代理服务器的地址proxyip
ini文件格式
[section]
options=[key] {该一对为一个items}
'''

import ConfigParser
workip=""  #工作环境IP
proxyip=""  #对应代理IP和端口
INITXT="f:/proxy.ini"  #INI文件名字
#打开INI文件
config = ConfigParser.ConfigParser()
config.readfp(open(INITXT))

sections=config.sections()

'''
#输出所有section
print('section is ',sections)
#输出所有KEY-VALUE，即所以的items
v=config.items('proxylist')
print('items is ',v)
#输出所有的option，即KEY
key=config.options('proxylist')
print('key is ',key)
'''


def ini_get(workip):  #读取INI
    try:
        #获取workip项的配置内容
        proxyip = config.get("proxylist",workip)
        print(workip,proxyip)
    except Exception as e:
        print '读取ini错误！',str(e)

def ini_add(sections,workip,proxyip):#写入INI
    try:
        print('好吧，我是打酱油滴～～～')
        #判断是否已经存在该workip
        print(config.has_option(sections,workip))
        #看是否存在该Section，不存在则创建
        if not config.has_section(sections):
            config.add_section(sections)
        config.set(sections,workip,proxyip)
        #config.set("proxylist","proxyip",proxyip)
        config.write(open(INITXT, "r+"))# 写入文件
    except Exception as e:
        print("写入INI错误",str(e))

#修改INI
def ini_del(workip):
    try:
        #global INITXT
        #config.read(INITXT)
        #看是否存在该option,即workip，此处sections默认为proxylist
        if not config.has_option('proxylist',workip):
            print("don't have this work ip !")
        config.remove_option('proxylist',workip)
        config.write(open(INITXT, "r+"))
    except Exception as e:
        print"修改INI错误",str(e)

#几个测试
ini_add('proxylist','1','2')
ini_add('proxylist','333','222')
ini_get('333')
ini_add('proxylist','123','3')
ini_get('tst')
ini_del('1')
