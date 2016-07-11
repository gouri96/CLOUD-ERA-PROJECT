#!/usr/bin/python
print "content-type:text/html"
print ""

import commands,cgi,time,sys,cgitb
cgitb.enable()
data=cgi.FormContent()
lvname=data['lvname'][0]
sname=data['sname'][0]
a=commands.getstatusoutput("sudo lvcreate --name {0} --size 100M -s /dev/cloud/{1}".format(sname,lvname))[0]
if a==0:
	b=commands.getstatusoutput("sudo mkdir /snapshot/{0}".format(sname))
	c=commands.getstatusoutput("sudo mount /dev/cloud/{0} /snapshot/{0}".format(sname))[0]
	if c==0:
		print '<p style="color:red;font-size:25px"> Successfully !!! <br /> snapshot created with name {}</p>'.format(sname)
	else:
		print '<p style="color:red;font-size:25px"> failure!!! check again</p>'

else:
	print '<p style="color:red;font-size:25px"> Sorry!!!lv does not exist</p>'