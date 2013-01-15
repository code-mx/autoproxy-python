#! /usr/bin/env python
#coding=utf-8
from xml.etree import ElementTree as ET

def change_xml(tree,wip,pip):
#    print 'print the getroot ele'
#    print tree.getroot()
    root=tree.getroot()
    for ele in root:
        print 'start debug'
        print ele.attrib
        print 'print the attrib value'
        print ele.attrib['ip']
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

def write_xml(tree,path):
    tree.write(path, encoding="utf-8",xml_declaration=True)


if __name__ == '__main__':
    path01=r"f:/python/proxy.xml"
    tree01=ET.parse(path01)
    #change_xml(tree01,'12.3.1','2134')
    tree01=change_xml(tree01,'12.3.1.3','2134')
    write_xml(tree01,path01)
