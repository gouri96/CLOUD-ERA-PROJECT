#!/usr/bin/python
print "content-type:text/html"
print ""

import commands,cgi,cgitb,os,random
cgitb.enable()
data=cgi.FormContent()
name=data['osn'][0]
ost=data['os'][0]
ram=data['ram'][0]
vcpu=data['cpu'][0]
size=data['disk'][0]
port1=str(random.randrange(5900,9999))
port2=str(random.randrange(5555,7777))
if ost=="redhat6":
	commands.getstatusoutput("sudo virt-install --import --hvm --name {0} --vcpus {1} --memory {2}  --disk path=/root/Desktop/automateos/rhel6.4-1.qcow2 --graphics vnc,password=akshay,listen=0.0.0.0,port={3} --noautoconsole".format(name,vcpu,ram,port1))

elif ost=="redhat6_terminal":
	commands.getstatusoutput("sudo virt-install --import --hvm --name {0} --vcpus {1} --memory {2}  --disk path=/root/Desktop/automateos/rhel6.4.qcow2 --graphics vnc,password=akshay,listen=0.0.0.0,port={3} --noautoconsole".format(name,vcpu,ram,port1))

elif ost=="windows":
	commands.getstatusoutput("sudo virt-install --import --hvm --name {0} --vcpus {1} --memory {2}  --disk path=/root/Desktop/automateos/generic.qcow2 --graphics vnc,password=akshay,listen=0.0.0.0,port={3} --noautoconsole".format(name,vcpu,ram,port1))
elif ost=="ubuntu":
	commands.getstatusoutput("sudo virt-install --import --hvm --name {0} --vcpus {1} --memory {2}  --disk path=/root/Desktop/automateos/ubuntu11.04.qcow2 --graphics vnc,password=akshay,listen=0.0.0.0,port={3} --noautoconsole".format(name,vcpu,ram,port1))



commands.getstatusoutput("sudo python /websockify-master/run -D 192.168.122.1:{0}  192.168.122.1:{1}".format(port2,port1))


print '<link type="text/css" rel="stylesheet" href="http://192.168.122.1/os.css"></link>'
print '<a  class="amenu" target="os" href="http://192.168.122.1:80/vnc/?ip=192.168.122.1&port={0}&password=akshay">Launch os</a>'.format(port2)
print '<div ><iframe name="os" ></iframe></div>'
