# coding:UTF-8
#!C:/Python27
# Filename: proxy_auto.py\
#Author: shuichon
#Email:shuichon@qq.com
#Version:2.0
'''
设计理念：
通过控制台参数，实现根据主机网络环境进行自动代理切换
运行后先检查本机IP是否在需要代理的IP地址字典KEY的范围内。如果在
则根据对应的value自动切换代理
如果无，则提示是否为该IP设置代理，如果不需要设置代理，则退出。
代理服务器包括，proxy_ip proxy_port
主机网络环境主要为work_ip
根据host_ip的值，设置相对应的IE代理，如果无匹配的值，则禁用代理
'''

import io, sys, time,os,socket
import _winreg
#复杂字符串分析，为chkip()模块提供支持
import re

print('''
	proxy_auto 2.0 python script by KING RING
	Email:shuichon@qq.com
	Version:2.0''')

#获取当前IP地址
ip=(socket.gethostbyname(socket.gethostname()))
print('		now ip is '+ip)
xpath = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, xpath, 0, _winreg.KEY_WRITE)


#本地网络地址列表
#work_ip={"127.0.0.1":None}
work_ip=['127.0.0.1']

#代理IP地址字典
pyips={}
pyip=''
#pyip=sys.argv[2]+':'+sys.argv[3]
tmpip=''

#检查当前IP是否已经存在work_ip列表内，返回bool值
def chkhave(m):
	for i in work_ip:
		if m==i:
			return True
		else:
			return False
	else:
		return False

#获取用户输入的IP地址
#tmpip=input()

#定义check模块，检查是否是合法的IPv4地址，返回bool值
def chkip(s):
    ipv4Pattern = r"\b(25[0-4]|2[0-4[0-9]|[01]?[0-9][0-9]?)\.(25[0-4]|2[0-4[0-9]|[01]?[0-9][0-9]?)\.(25[0-4]|2[0-4[0-9]|[01]?[0-9][0-9]?)\.(25[0-4]|2[0-4[0-9]|[01]?[0-9][0-9]?)\b"
    if re.match(ipv4Pattern,s):
        ip=re.findall(ipv4Pattern,s)
        return True
    else:
        print('The ip address you input is invalid')
        return False

#判断参数是否合法，返回bool值
def chkargv():
	if chkip(sys.argv[2]) and (0<int(sys.argv[3])<65535):
		return True
	else:
		return False

#切换至相应代理(此处n为work_ip)
def swithpy(n):
	#获得该IP对应的pyip
	if chkhave(n):
		proxy=''
		try:
			_winreg.SetValueEx(key, "ProxyEnable", 0, _winreg.REG_DWORD, 0)
			_winreg.SetValueEx(key, "ProxyServer", 0, _winreg.REG_SZ, proxy)
			print('''
	work_ip don't have this ip address!
	please input '--help' behind the script.''')
		except Exception as e:
			print("ERROR: " + str(e.args))
		finally:
			None
	else:
		proxy=pyips[n]
		try:
			_winreg.SetValueEx(key, "ProxyEnable", 0, _winreg.REG_DWORD, 1)
			_winreg.SetValueEx(key, "ProxyServer", 0, _winreg.REG_SZ, proxy)
			print("have enable proxy!")
		except Exception as e:
			print("ERROR: " + str(e.args))
		finally:
			None
if len(sys.argv)<2:
	if chkhave(ip)==False:
		proxy=''
		try:
			_winreg.SetValueEx(key, "ProxyEnable", 0, _winreg.REG_DWORD, 0)
			_winreg.SetValueEx(key, "ProxyServer", 0, _winreg.REG_SZ, proxy)
			print('''
		work_ip don't have this ip address!
		please input '--help' behind the script.''')
		except Exception as e:
			print("ERROR: " + str(e.args))
		finally:
			None
else:
	if sys.argv[1].startswith('--') and chkargv():
		#新增proxy代理
		pyip=sys.argv[2]+':'+sys.argv[3]

		#取得argv参数列表内的第二个参数，去除前两个字符“--”
		option=sys.argv[1][2:]
		if option=='version':
			print('''Proxy_auto 2.0 python script by KING RING''')
		elif option=='help':
			print('''
			This program prints files to the standard output.
			Any number of files can be specified.
			Options include:
			  --version : The version number of the pychon script
			  --help    : Display this help
			  --add     : Add using ip to using ip poor
			         exp:proxy_auto --add [proxy_ip]:[proxy_prot]
			  --dell    : Del unusing ip from using ip poor
			         exp:proxy_dell [work_ip]
			''')
		elif option=='add':
			print('add IP & mode')
			tmpip=sys.argv[2]
			print(tmpipip)
			print(sys.argv[3])
			pyips[work_ip]=pyip
		elif option=='del':
			print('del work_ip and proxy')
	else:
		print('''Unknown option !
please input '--help' behind the script.''')
		#sys.exit()
#	else:
#		swithpy(ip)
