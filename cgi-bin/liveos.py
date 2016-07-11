#!/usr/bin/python
print "content-type:text/html"
print ""

import commands,cgi,time,sys,cgitb
cgitb.enable()
data=cgi.FormContent()
shost="akshay"
sip="192.168.122.1"
cip=data['cip'][0]
chost=data['chost'][0]
f=open("/etc/hosts","a")
f.write("{0}  {1}".format(cip,chost))
f.close()
commands.getstatusoutput("sudo echo '/var/lib/libvirt/images/  *(rw)' >>/etc/exports")
commands.getstatusoutput("sudo systemctl restart nfs-server")
commands.getstatusoutput("sudo touch /{0}.py".format(chost))
commands.getstatusoutput("sudo chmod 777 /{0}.py".format(chost))
g=open("/{0}.py".format(chost),"w")
g.write('#!/usr/bin/python\nimport commands\ncommands.getstatusoutput("sudo echo \'{0} {1}\' >>/etc/hosts")\n'.format(sip,shost)+'command.getstatusoutput("sudo mount {0}://var/lib/libvirt/images/ /var/lib/libvirt/images/")'.format(sip))
g.close()
commands.getstatusoutput("sudo sshpass {0} scp {1}:/{2}.py  {3}:/ strictHostKeyChecking=no".format(pas,sip,chost,cip))
commands.getstatusoutput("sudo ssh strictHostKeyChecking=no root@{0} /{1}.py".format(cip,chost))
commands.getstatusoutput("virsh migrate --live rhel7.1 qemu+ssh://{0}/system".format(cip))