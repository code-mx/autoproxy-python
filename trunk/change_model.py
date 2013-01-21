#! /usr/bin/env python
#coding=utf-8
# Filename: change_model.py\
#Author: shuichon
#Email:shuichon@qq.com

from xml.etree import ElementTree as ET

def change_xml(tree,wip,pip):
#    print 'print the getroot ele'
#    print tree.getroot()
    root=tree.getroot()
#    print 'print the debug of getwip() info'
#    print getwip(tree)
    if wip in getwip(tree):
        for ele in root:
#            print 'equle'
#            print ele.attrib['ip']==wip
            if ele.attrib['ip']==wip:
#                print 'start debug'
#                print ele.attrib
#                print 'print the attrib value'
#                print ele.attrib['ip']
                ele.text=pip
    else:
#        print 'add the net wip'
        add=ET.Element('wip')
        add.text=pip
        add.set('ip',wip)
        root.append(add)
#            wipl=tree.getroot()
#            print 'print the wipl type'
#            print wipl
    return tree

def write_xml(tree,path):
    tree.write(path, encoding="utf-8",xml_declaration=True)

def getwip(tree):
    '''获取当前XML内所有的work_ip 返回一个list'''
    wlist=[]
    root=tree.getroot()
    #获取所有WIP的ip地址，并保存进列表wlist中
    for ele in root:
#        print 'debug echo'
#        print ele.attrib['ip']
        wlist.append(ele.attrib['ip'])
    return wlist


if __name__ == '__main__':
    path01=r"f:/python/proxy.xml"
    tree01=ET.parse(path01)
    #change_xml(tree01,'12.3.1','2134')
    tree01=change_xml(tree01,'12.3.1.3','192.164.1.3')
    write_xml(tree01,path01)