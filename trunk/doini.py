#!/usr/bin/env python
#coding=utf-8

#Filename: doini.py
#Author: shuichon
#Email:shuichon@qq.com
#Version:2.0
#Date:2013-01-21

import ConfigParser
config = ConfigParser.ConfigParser()
config.read('proxy.ini')
sections=config.sections()

def ini_get(workip):
    try:
        proxyip = config.get("proxylist",workip)
#        print(workip,proxyip)
        return proxyip
    except Exception as e:
        print 'erro:'+str(e)

def ini_add(workip,proxyip):
#    print 'debug2'
    try:
        sections='proxylist'
        print config.has_option(sections,workip)
        if not config.has_section(sections):
            config.add_section(sections)
        config.set(sections,workip,proxyip)
        config.write(open('proxy.ini', 'w'))
    except Exception as e:
        print "erro:"+str(e)


def ini_del(workip):
    try:
        if not config.has_option('proxylist',workip):
            print "don't have this work ip !"
        else:
#            print 'debug'
            config.remove_option('proxylist',workip)
            config.write(open('proxy.ini', 'w'))
    except Exception as e:
        print "erro"+str(e)

def ini_show(sections,*forv):
    if forv:
        keys=config.options(sections)
        return keys
    else:
        print 'the wip list is :',keys
        v=config.items(sections)
        print ('items is ',v)


if __name__ == '__main__':
    #输出所有section
    print('section is ',sections)

    #输出所有KEY-VALUE，即所以的items
    v=config.items('proxylist')
    print('items is ',v)

    #输出所有的option，即KEY
    key=config.options('proxylist')
    print('key is ',key)

    print sections
    ini_add('wip0','0')
    ini_get('wip3')
    ini_del('1')
    ini_del('wip2')
    print 'two args debug but no *args'
    ini_show('proxylist')
    print 'two (*args)args debug '
    ini_show('proxylist',True)
