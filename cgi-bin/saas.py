#!/usr/bin/python
print "content-type:text/html"
print ""

import commands,cgi,cgitb
data=cgi.FormContent()
user=data['u'][0]
soft=data['s'][0]
pas="akshay"
commands.getstatusoutput("sudo usermod -s /usr/bin/{0} {1}".format(soft,user))
commands.getstatusoutput("sudo sed -Ei 's/X11Forwarding no/X11Forwarding yes/g' /etc/ssh/sshd_config ")
commands.getstatusoutput("sudo touch /saas/{0}_{1}.py".format(user,soft))
commands.getstatusoutput("sudo chmod 777 /saas/{0}_{1}.py".format(user,soft))
f=open("/saas/{0}_{1}.py".format(user,soft),"w")
f.write("sshpass -p {0} ssh -X -l {1} -o strictHostkeychecking=no 192.168.122.1 {2}".format(pas,user,soft))
f.close()
commands.getstatusoutput("sudo tar -cvf /saas/{0}_{1}.tar /saas/{0}_{1}.py".format(user,soft))
commands.getstatusoutput("sudo mv /saas/{0}_{1}.tar /var/www/html".format(user,soft))
print "<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.122.1/{0}_{1}.tar\">\n".format(user,soft)	