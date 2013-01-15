#! /usr/bin/env python
#coding=utf-8

from xml.etree import ElementTree as ET

path=r"f:/python/proxy.xml"
tree=ET.parse(path)
root=tree.getroot()
m=1
for ele in root:
    print 'print the %d th  elems tag:'% m
    print ele.tag
    print '\r\n'
    print 'print the %d elems text:'% m
    print ele.text
    print '\r\n'
    print 'print the %d th      elems attrib'% m
    print ele.attrib
    print '\r\n'
    print 'print the %d th  elems attrib  ip value'% m
    #attrib返回一个字典，用来表示属性和属性的值
    print ele.attrib
    print ele.attrib['ip']
    print '\r\n'
    print 'print the children elems'
    print ele.getchildren()
    print '================================='
    m=m+1
print 'print root tag:'
print root.tag
print '\r\n'
print 'print root text:'
print root.text
print '\r\n'
print 'print root attrib'
print root.attrib
print '================================'
print 'print the version value'
print root.attrib['version']
print '\r\n'

print 'print the 2 subelems'
print root[0:2]
print '\r\n'
print "print the wip ele"
print root.find('wip')
print '\r\n'
#print root.find('wip').key()
print 'print the wip items'
print '\r\n'
print root.find('wip').items()
print '\r\n'
#print root.attrib('version')

#创建新的children element
#new=ET.Element('wip')
#new.set('wip','004')
#
#newp=ET.Element('pip')
#newp.text='00330'
#
#new.append(newp)
#
#tree.write(r"f:/python/proxy.xml")