#!/usr/bin/python
print "content-type:text/html"
print ""

import commands,cgi,cgitb
cgitb.enable()
data=cgi.FormContent()
n=data['n'][0]
service=data['soft'][0]
user=data['user'][0]
pas=data['pas'][0]
port=5586
c=int(n)

while(c!=0):

	print """
	<style>
		a.menu
		{
		width: 200px;
		font-size: 20px;
		font-weight: bold;
		color: black;
		text-align: center;
		text-decoration: none;
		border-radius: 10px 5px;
		margin-left: 20px;
		margin-right: 10px;
		margin-top:30px;
		background:grey;
		border:1px groove grey;
		}
	</style>
	"""
	if service=="apach":
		i=commands.getstatusoutput("sudo docker run -itd --privileged=true -p {0}:4200 -v /docker/:/media/ httpd bash".format(port))[1]
	elif service=="ftp":
		i=commands.getstatusoutput("sudo docker run -itd --privileged=true -p {0}:4200 -v /docker/:/media/ ftp bash".format(port))[1]
	elif service=="samba":
		i=commands.getstatusoutput("sudo docker run -itd --privileged=true -p {0}:4200 -v /docker/:/media/ samba-server bash".format(port))[1]
	elif service=="mysql":
		i=commands.getstatusoutput("sudo docker run -itd --privileged=true -p {0}:4200 -v /docker/:/media/ mysql-server bash".format(port))[1]
	elif service=="nis":
		i=commands.getstatusoutput("sudo docker run -itd --privileged=true -p {0}:4200 -v /docker/:/media/ nis-server bash".format(port))[1]
	
	commands.getstatusoutput("sudo touch /docker/{0}.py".format(user))
	commands.getstatusoutput("sudo chmod 777 /docker/{0}.py".format(user))
	f=open("/docker/{0}.py".format(user),"w")
	f.write('#!/usr/bin/python\nimport commands\ncommands.getstatusoutput("useradd {1}")\ncommands.getstatusoutput("echo {0}| passwd {1} --stdin")\n'.format(pas,user)+'ip=commands.getstatusoutput("hostname -i")[1]\ncommands.getstatusoutput("sed -Ei \'s/OPTS=\\"--disable-ssl-menu -s \/:LOGIN\\"/#OPTS=\\"--disable-ssl-menu -s \/:LOGIN\\"/g\' /etc/sysconfig/shellinaboxd")\ncommands.getstatusoutput("sed -Ei \'s/OPTS=\\"-t -s \/:SSH:172.17.0.2\\"/OPTS=\\"-t -s \/:SSH:{0}\\"/g\' /etc/sysconfig/shellinaboxd".format(ip))\ncommands.getstatusoutput("service shellinaboxd restart")')
	f.close()
	commands.getstatusoutput("sudo docker exec -d {0} /media/{1}.py".format(i,user))
	print '<a href="http://192.168.122.1:{0}" target="_blank">click here for conatiner {1}</a>'.format(port,c)
	port+=1
	c=c-1
	
	


