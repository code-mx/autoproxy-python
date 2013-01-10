#!/usr/bin/env python
# -*- coding:gb2312 -*-

#Filename: doini.py
#Author: KING RING
#Email:shuichon@qq.com
#Version:1.0

'''ini�ļ���ʽ
�ں�һ��proxylist��section����ʽΪ���������ĵ�ַworkip��Ӧ
�ڴ���������ĵ�ַproxyip
ini�ļ���ʽ
[section]
options=[key] {��һ��Ϊһ��items}
'''

import ConfigParser
workip=""  #��������IP
proxyip=""  #��Ӧ����IP�Ͷ˿�
INITXT="f:/proxy.ini"  #INI�ļ�����
#��INI�ļ�
config = ConfigParser.ConfigParser()
config.readfp(open(INITXT))

sections=config.sections()

'''
#�������section
print('section is ',sections)
#�������KEY-VALUE�������Ե�items
v=config.items('proxylist')
print('items is ',v)
#������е�option����KEY
key=config.options('proxylist')
print('key is ',key)
'''


def ini_get(workip):  #��ȡINI
    try:
        #��ȡworkip�����������
        proxyip = config.get("proxylist",workip)
        print(workip,proxyip)
    except Exception as e:
        print '��ȡini����',str(e)

def ini_add(sections,workip,proxyip):#д��INI
    try:
        print('�ðɣ����Ǵ��͵Ρ�����')
        #�ж��Ƿ��Ѿ����ڸ�workip
        print(config.has_option(sections,workip))
        #���Ƿ���ڸ�Section���������򴴽�
        if not config.has_section(sections):
            config.add_section(sections)
        config.set(sections,workip,proxyip)
        #config.set("proxylist","proxyip",proxyip)
        config.write(open(INITXT, "r+"))# д���ļ�
    except Exception as e:
        print("д��INI����",str(e))

#�޸�INI
def ini_del(workip):
    try:
        #global INITXT
        #config.read(INITXT)
        #���Ƿ���ڸ�option,��workip���˴�sectionsĬ��Ϊproxylist
        if not config.has_option('proxylist',workip):
            print("don't have this work ip !")
        config.remove_option('proxylist',workip)
        config.write(open(INITXT, "r+"))
    except Exception as e:
        print"�޸�INI����",str(e)

#��������
ini_add('proxylist','1','2')
ini_add('proxylist','333','222')
ini_get('333')
ini_add('proxylist','123','3')
ini_get('tst')
ini_del('1')
