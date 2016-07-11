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

def storage():
	commands.getstatusoutput("sudo lvcreate --name {0} --size +{1} /dev/cloud ".format(name,size))
	
if ost=="redhat":
	storage()
	commands.getstatusoutput('sudo virt-install --hvm --name {0} --vcpus {1} --memory {2} --os-type linux  --os-variant rhel7 --location ftp://192.168.122.1/pub/rhel7/  --disk /dev/cloud/{0} --graphics vnc,password=akshay,listen=0.0.0.0,port={3} --extra-args "ks=ftp://192.168.122.1/pub/ks.cfg"  --noautoconsole'.format(name,vcpu,ram,port1))
elif ost=="windows":
	storage()
	commands.getstatusoutput("sudo virt-install --hvm --name {0} --vcpus {1} --memory {2}  --cdrom /root/Desktop/win-07.iso  --disk /dev/cloud/{0} --graphics vnc,password=akshay,listen=0.0.0.0,port={3} --noautoconsole".format(name,vcpu,ram,port1))

elif ost=="fedora":
	storage()
	commands.getstatusoutput("sudo virt-install --hvm --name {0} --vcpus {1} --memory {2}  --cdrom /root/Desktop/Fedora-14-x86_64-DVD/Fedora-14-x86_64-DVD.iso  --disk /dev/cloud/{0} --graphics vnc,password=akshay,listen=0.0.0.0,port={3} --noautoconsole".format(name,vcpu,ram,port1))
elif ost=="kalilinux":
	storage()
	commands.getstatusoutput("sudo virt-install --hvm --name {0} --vcpus {1} --memory {2}  --cdrom /root/Desktop/kali-linux-2.0-amd64.iso  --disk /dev/cloud/{0} --graphics vnc,password=akshay,listen=0.0.0.0,port={3} --noautoconsole".format(name,vcpu,ram,port1))

elif ost=="ubuntu":
	storage()
	commands.getstatusoutput("sudo virt-install --hvm --name {0} --vcpus {1} --memory {2}  --cdrom /root/Desktop/ubuntu-11.04-desktop-i386.iso  --disk /dev/cloud/{0} --graphics vnc,password=akshay,listen=0.0.0.0,port={3} --noautoconsole".format(name,vcpu,ram,port1))

elif ost=="centos":
	storage()
	commands.getstatusoutput("sudo virt-install --hvm --name {0} --vcpus {1} --memory {2}  --cdrom /root/Desktop/CentOS-6.6-x86_64-minimal.iso  --disk /dev/cloud/{0} --graphics vnc,password=akshay,listen=0.0.0.0,port={3} --noautoconsole".format(name,vcpu,ram,port1))
else:
	print "wrong selection"
	
commands.getstatusoutput("sudo python /websockify-master/run -D 192.168.122.1:{0}  192.168.122.1:{1}".format(port2,port1))


print '<link type="text/css" rel="stylesheet" href="http://192.168.122.1/os.css"></link>'
print '<a  class="amenu" target="os" href="http://192.168.122.1:80/vnc/?ip=192.168.122.1&port={0}&password=akshay">Launch os</a>'.format(port2)
print '<div ><iframe name="os" ></iframe></div>'

