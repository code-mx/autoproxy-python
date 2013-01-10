#! /usr/bin/env python
#coding=utf-8
import re
def check(s):
    ipv4Pattern = r"\b(25[0-4]|2[0-4[0-9]|[01]?[0-9][0-9]?)\.(25[0-4]|2[0-4[0-9]|[01]?[0-9][0-9]?)\.(25[0-4]|2[0-4[0-9]|[01]?[0-9][0-9]?)\.(25[0-4]|2[0-4[0-9]|[01]?[0-9][0-9]?)\b"
    if re.match(ipv4Pattern,s):
        ip=re.findall(ipv4Pattern,s)
    else:
        print('The ip address you input is invalid')
