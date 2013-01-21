#!/usr/bin/env python
#coding=utf-8

#Filename: doini.py
#Author: shuichon
#Email:shuichon@qq.com
#Version:2.0
#Date:2013-01-21
'''

'''

import ConfigParser
workip=""
proxyip=""
INITXT="proxy.ini"
config = ConfigParser.ConfigParser()
config.read('proxy.ini')
sections=config.sections()

def ini_get(workip):
    try:
        proxyip = config.get("proxylist",workip)
        print(workip,proxyip)
    except Exception as e:
        print 'erro:'+str(e)



def ini_add(sections,workip,proxyip):
    try:
        print config.has_option(sections,workip)

        if not config.has_section(sections):
            config.add_section(sections)
        config.set(sections,workip,proxyip)
        config.write(open(INITXT, 'w'))
    except Exception as e:
        print "erro:"+str(e)


def ini_del(workip):
    try:
        if not config.has_option('proxylist',workip):
            print "don't have this work ip !"
        else:
            print 'debug'
            config.remove_option('proxylist',workip)
            config.write(open(INITXT, 'w'))
    except Exception as e:
        print "erro"+str(e)


if __name__ == '__main__':
    print sections
    ini_add('proxylist','1','2')
    ini_add('proxylist','333','222')
    ini_get('333')
    ini_add('proxylist','123','3')
    ini_get('tst')
    ini_del('1')
    ini_del('333')
