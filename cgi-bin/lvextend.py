#!/usr/bin/python
print "content-type:text/html"
print ""

import commands,cgi,time,sys,cgitb
cgitb.enable()
data=cgi.FormContent()
lvname=data['lvname'][0]
lsize=data['esize'][0]
a=commands.getstatusoutput("sudo lvextend --size +{0} /dev/cloud/{1}".format(lsize,lvname))[0]
if a==0:
	b=commands.getstatusoutput("sudo resize2fs /dev/cloud/{0}".format(lvname))[0]
	if b==0:
		print '<p style="color:red;font-size:25px"> Successfully !!!\n size is extended by {}</p>'.format(lsize)
	else:
		print '<p style="color:red;font-size:25px"> failure!!! check again</p>'

else:
	print '<p style="color:red;font-size:25px"> Sorry!!!lv does not exist</p>'