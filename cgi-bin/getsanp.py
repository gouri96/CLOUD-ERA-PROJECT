#!/usr/bin/python
print "content-type:text/html"
print ""

import commands,cgi,time,sys,cgitb
cgitb.enable()
data=cgi.FormContent()
lvname=data['lvname'][0]
sname=data['sname'][0]
user="test"
sip="192.168.122.1"
pas="akshay"

def clientsshfs():
	w=commands.getstatusoutput("sudo touch /snapshot/{0}.py".format(sname))
	e=commands.getstatusoutput("sudo chmod 777 /snapshot/{0}.py".format(sname))
	print w
	print e
	p=open("/snapshot/{0}.py".format(sname),"w")
	p.write('#!/usr/bin/python\nimport commands\ncommands.getstatusoutput("mkdir /media/{3}")\ncommands.getstatusoutput("sshpass -p {0} sshfs {1}@{2}:/snapshot/{3} /media/{3} ")\nraw_input()'.format(pas,user,sip,sname))
	p.close()
	h=commands.getstatusoutput("sudo tar -cvf /snapshot/{0}.tar /snapshot/{0}.py".format(sname))
	print h 
	q=commands.getstatusoutput("sudo mv /snapshot/{0}.tar /var/www/html".format(sname))
	print "<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.122.1/{0}.tar\">\n".format(sname)	


commands.getstatusoutput("sudo chmod 777 /etc/exports")
d=commands.getstatusoutput("sudo echo '/snapshot/{0} *(rw,no_root_squash)' >> /etc/exports".format(sname))
l=commands.getstatusoutput("sudo chown {0} /snapshot/{1}  ".format(user,sname))
k=commands.getstatusoutput("sudo chmod o-rwx,g-rwx /snapshot/{0}".format(sname))
clientsshfs()