# coding:UTF-8
#!C:/Python27
# Filename: proxy_auto.py\
#Author: shuichon
#Email:shuichon@qq.com
#Version:3.0
'''
设计理念：
通过控制台参数，实现根据主机网络环境进行自动代理切换
运行后先检查本机IP是否在需要代理的IP地址列表范围内。如果在则根据对应的代理IP地址自动切换代理
如果不在，则提示是否为该IP设置代理，如果不需要设置代理，则退出。
代理服务器地址pip包括，proxy_ip:proxy_port
主机网络环境主要为work_ip
根据host_ip的值，设置相对应的IE代理，如果无匹配的值，则禁用代理
'''

import io, sys, time,os,socket
import _winreg,p_xml
#复杂字符串分析，为chkip()模块提供支持
import re

#输出程序说明
print '''
	proxy_auto 3.0 python script by shuichon
	Email:shuichon@qq.com
	Version:3.0'''

#获取当前IP地址
ip=(socket.gethostbyname(socket.gethostname()))
print('now ip is '+ip)

#设置代理设置路径
xpath = "Software\Microsoft\Windows\CurrentVersion\Internet Settings"
key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, xpath, 0, _winreg.KEY_WRITE)

#声明下面需要用到path和tree
path=r"f:/python/proxy.xml"
tree=p_xml.read_xml(path)

#2013-01-19已完成，待调试
#待实现。思路，通过p_xml获取到已经存在代理设置的work_ip列表
work_ip=[]
work_ip=p_xml.getwip(tree)

#临时使用
tmpip=''

#思路：删除上面的work_ip列表，直接由p_xml返回work_ip列表
#检查当前IP是否已经在work_ip列表内，返回bool值
def chkhave(m):
	for i in work_ip:
		if m==i:
			return True
		else:
			return False
	else:
		return False

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
	#修改判断方式，主要是针对argv[3]，此处需要进一步优化
	if chkip(sys.argv[2]):
		return True
	else:
		return False

#切换至相应代理(此处n为work_ip)
def swithpy(n):
	#获得该IP对应的pyip
	proxy=p_xml.getpip(tree,ip)
	try:
		_winreg.SetValueEx(key, "ProxyEnable", 0, _winreg.REG_DWORD, 1)
		_winreg.SetValueEx(key, "ProxyServer", 0, _winreg.REG_SZ, proxy)
		print("have enable proxy!")
	except Exception as e:
		print("ERROR: " + str(e.args))
	finally:
		None


#进入主程序
if __name__ == '__main__':
	#假如直接运行程序，没有任何参数，则进行一下操作
	if len(sys.argv)<2:
		if chkhave(ip)==False:
			proxy=''
			#如果没有当前环境的IP，则尝试禁用代理设置，并提醒输出程序操作说明
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
	#程序携带参数运行
	else:
		#判断参数是否以‘--’开始，并且判断参数是否合法，然后继续操作
		if sys.argv[1].startswith('--') and chkargv():
			#取得argv参数列表内的第二个参数，去除前两个字符“--”
			option=sys.argv[1][2:]

			#假如键入的参数是‘version’
			if option=='version':
				print('''Proxy_auto 2.0 python script by shuichon''')
			elif option=='help':
				print('''
				This program prints files to the standard output.
				Any number of files can be specified.
				Options include:
				--version : The version number of the pychon script
				--help    : Display this help
				--add     : Add using ip to using ip poor
					   exp:proxy_auto --add [work_ip] [proxy_ip:proxy_prot]
				--del     : Del unusing ip from using ip poor
					   exp:proxy_auto --dell [work_ip]
				--show    :show the list of all
				''')
			#假如是要进行添加操作
			elif option=='add':
				#传入需要添加的当前IP，
				wip=sys.argv[2]
				#传入新增proxy代理的pip参数
				pyip=sys.argv[3]
				p_xml.change_xml(tree,ip,pyip)
				print('have add the '+pyip+' to the xml')
			#删除操作
			elif option=='del':
				p_xml.delxml(tree,ip)
				print('have del the '+ip+' config from the xml')
			elif option=='show':
				print('debug')
				print p_xml.show(tree)
		#假如携带的参数不正确，则提示
		else:
			print('''	Unknown option !
	please input '--help' behind the script.''')

