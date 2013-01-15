#! /usr/bin/env python
#coding=utf-8

from xml.etree import ElementTree as ET

def read_xml(path):
    tree =ET.parse(path)
#    root=tree.getroot()
    return tree

def write_xml(tree,path):
    tree.write(path, encoding="utf-8",xml_declaration=True)

#def insert_xml(tree,path)

def change_xml(tree,wip,pip):
#    print 'print the getroot ele'
#    print tree.getroot()
    root=tree.getroot()
    for ele in root:
        print 'start debug'
        print ele.attrib
        print 'print the attrib value'
        print ele.attrib['ip']
        #此处逻辑处理有问题，功能实现已解决
        if ele.attrib['ip']==wip:
            ele.text=pip
        else:
            ele=ET.Element('wip')
            ele.text=pip
            ele.set('ip',wip)
#            wipl=tree.getroot()
#            print 'print the wipl type'
#            print wipl
            root.append(ele)
        return tree


#需要进一步调试
def del_xml(tree,wip):
    root=tree.getroot()
    for ele in root:
        if ele.attrib['ip']==wip:

            return True
        return False

#插入新的配置项
#def insert_xml(wip,pip):
#    subelem=tree.find('')

def getwip(tree):
    '''获取当前XML内所有的work_ip 返回一个list'''
    wlist=[]
    root=tree.getroot()
    #获取所有WIP的ip地址，并保存进列表wlist中
    for ele in root:
        print 'debug echo'
        print ele.attrib['ip']
        wlist.append(ele.attrib['ip'])
    return wlist

def getpip(tree,ip):
    '''获取当前IP地址对应的代理IP地址
    返回proxy_ip的值'''
    root=tree.getroot()
    for ele in root:
        if ele.attrib['ip']==ip:
            return ele.text

#def find_nodes(tree,path):
#    return tree.findall(path)

if __name__ == '__main__':
    path01=r"f:/python/proxy.xml"
    tree01=read_xml(path01)
    #为调试DEL函数
    print tree01.getroot()
    print 'tree01 test print'
    print tree01
    print tree01.iterfind('wip')
    #结束

    print getwip(tree01)
    print getpip(tree01,'127.0.0.2')
    #del_xml(tree01,'127.0.0.1')
    change_xml(tree01,'12.3.1','2134')
    write_xml(tree01,path01)