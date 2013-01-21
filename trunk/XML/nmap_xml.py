from  xml.dom import  minidom
def get_attrvalue(node, attrname):
     return node.getAttribute(attrname) if node else ''
def get_nodevalue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''
def get_xmlnode(node,name):
    return node.getElementsByTagName(name) if node else []
doc = minidom.parse(r"c:\.xml")
root = doc.documentElement
host=root.getElementsByTagName("address")
ipaddress=host[0].getAttribute("addr")
# ........................
s=root.getElementsByTagName("hostname")
hostname=s[0].getAttribute("name")

host_ip=ipaddress+"__"+hostname
# 
ports=root.getElementsByTagName("port")
for i in ports:
    port_id=i.getAttribute("portid")#
    print port_id
    # input db
    state=i.getElementsByTagName("state")
    state_port=state[0].getAttribute("state")#
    print state_port
    service=i.getElementsByTagName("service")
    print service[0].getAttribute("product")
     


