#!C:/Python32
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
import winreg
#复杂字符串分析，为chkip()模块提供支持
import re

print('''
	proxy_auto 1.0 python script by KING RING
	Email:shuichon@qq.com
	Version:2.0''')

#获取当前IP地址
ip=(socket.gethostbyname(socket.gethostname()))
print('now ip is '+ip)


#本地网络地址列表
#work_ip={"127.0.0.1":None}
work_ip=['127.0.0.1']

#代理IP地址字典
pyips={}
pyip=sys.argv[2]+':'sys.argv[3]
tmpip=''

#检查当前IP是否已经存在work_ip列表内
def chkhave(m):
	for i in work_ip:
		if m=i:
			return True
		else:
			return False
	else:
		return False

#获取用户输入的IP地址
#tmpip=input()

#定义check模块，检查是否是合法的IPv4地址
def chkip(s):
    ipv4Pattern = r"\b(25[0-4]|2[0-4[0-9]|[01]?[0-9][0-9]?)\.(25[0-4]|2[0-4[0-9]|[01]?[0-9][0-9]?)\.(25[0-4]|2[0-4[0-9]|[01]?[0-9][0-9]?)\.(25[0-4]|2[0-4[0-9]|[01]?[0-9][0-9]?)\b"
    if re.match(ipv4Pattern,s):
        ip=re.findall(ipv4Pattern,s)
        return True
    else:
        print('The ip address you input is invalid')
        return False

#判断参数是否合法
def chkargv():
	if chkip(sys.argv[2]) and (0<int(sys.argv[3])<65535):
		return True
	else:
		return False

#切换至相应代理(此处n为work_ip)
def swithpy(n):
	xpath = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
	key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, xpath, 0, winreg.KEY_WRITE)
	获得该IP对应的pyip
	if chkhave(ip)
		proxy=''
		try:
			winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
			winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, proxy)
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
			winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, 1)
			winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, proxy)
			print("have enable proxy!")
		except Exception as e:
			print("ERROR: " + str(e.args))
		finally:
			None

#输出检查第一个参数
print(sys.argv[1])

if sys.argv[1].startswith('--') and chkargv():

	#取得argv参数列表内的第二个参数，去除前两个字符“--”
	option=sys.argv[1][2:]
	if option=='version':
		print('''proxy_auto 2.0 python script by KING RING''')
                print('Version 0.2')
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
		tmpipip=sys.argv[2]
		print(tmpipip)
		print(sys.argv[3])
	elif option=='del':
		print('del work_ip and proxy')
	else:
		print('Unknown option.')
#	sys.exit()
else:
	swithpy()


###############################################################
#调用check模块，对输入IP进行检查
chkip(tmpip)

#字典
ippoor={"127.0.0.1":"proxyip0",
		"192.168.0.123":"proxyip1"
       }

print(ippoor['127.0.0.1'])
#列表
liebiao=['1','2','4']

#元组
yuanzu=('wolf', 'elephant', 'penguin')

testpoor={"1":ippoor,"2":liebiao}

#
def readfile(filename):
	'''Print a file to the standard output.'''
	f=file(filename)
	while True:
		line=f.readline()
		if len(line)==0:
			break
		print(line)
		# notice comma
	f.close()

# Script starts from here
if len(sys.argv)<2:
	print('No action specified.')
	sys.exit()

if sys.argv[1].startswith('--'):
	option=sys.argv[1][2:]
	# fetch sys.argv[1] but without the first two characters
	if option=='version':
                print('Version 0.1')
	elif option=='help':
		print ('''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
  --version : Prints the version number
  --help    : Display this help
  --add     : Add using ip to using ip poor
  --dell    : Del unusing ip from using ip poor''')
	elif option=='add':
                print('add IP & mode')
	elif option=='del':
                print('del ip or mode')
	else:
		print('Unknown option.')
	sys.exit()
else:
	for filename in sys.argv[1:]:
		readfile(filename)

