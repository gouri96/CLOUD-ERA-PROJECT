#!/usr/bin/python
print "content-type:text/html"
print ""

import commands,cgi,cgitb,random
cgitb.enable()
data=cgi.FormContent()
soft=data['soft'][0]
user=data['user'][0]
pas=data['pas'][0]
port=str(random.randrange(5600,9999))

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
if soft=="python":
	i=commands.getstatusoutput("sudo docker run -itd --privileged=true -p {0}:4200 -v /docker/:/media/ rahul bash".format(port))[1]
	commands.getstatusoutput("sudo touch /docker/{0}.py".format(user))
	commands.getstatusoutput("sudo chmod 777 /docker/{0}.py".format(user))
	f=open("/docker/{0}.py".format(user),"w")
	f.write('#!/usr/bin/python\nimport commands\ncommands.getstatusoutput("useradd -s /usr/bin/python {0}")\ncommands.getstatusoutput("echo {1}| passwd {0} --stdin")\n'.format(user,pas)+'ip=commands.getstatusoutput("hostname -i")[1]\ncommands.getstatusoutput("sed -Ei \'s/OPTS=\\"--disable-ssl-menu -s \/:LOGIN\\"/#OPTS=\\"--disable-ssl-menu -s \/:LOGIN\\"/g\' /etc/sysconfig/shellinaboxd")\ncommands.getstatusoutput("sed -Ei \'s/OPTS=\\"-t -s \/:SSH:172.17.0.2\\"/OPTS=\\"-t -s \/:SSH:{0}\\"/g\' /etc/sysconfig/shellinaboxd".format(ip))\ncommands.getstatusoutput("service shellinaboxd restart")\ncommands.getstatusoutput("passwd -l root")')
	f.close()
	b=commands.getstatusoutput("sudo docker exec -d {0} /media/{1}.py".format(i,user))
elif soft=="ruby":
	i=commands.getstatusoutput("sudo docker run -itd --privileged=true -p {0}:4200 -v /docker/:/media/ rahul bash".format(port))[1]
	commands.getstatusoutput("sudo touch /docker/{0}.py".format(user))
	commands.getstatusoutput("sudo chmod 777 /docker/{0}.py".format(user))
	f=open("/docker/{0}.py".format(user),"w")
	f.write('#!/usr/bin/python\nimport commands\ncommands.getstatusoutput("useradd -s /usr/bin/irb {0}")\ncommands.getstatusoutput("echo {1}| passwd {0} --stdin")\n'.format(user,pas)+'ip=commands.getstatusoutput("hostname -i")[1]\ncommands.getstatusoutput("sed -Ei \'s/OPTS=\\"--disable-ssl-menu -s \/:LOGIN\\"/#OPTS=\\"--disable-ssl-menu -s \/:LOGIN\\"/g\' /etc/sysconfig/shellinaboxd")\ncommands.getstatusoutput("sed -Ei \'s/OPTS=\\"-t -s \/:SSH:172.17.0.2\\"/OPTS=\\"-t -s \/:SSH:{0}\\"/g\' /etc/sysconfig/shellinaboxd".format(ip))\ncommands.getstatusoutput("service shellinaboxd restart")\ncommands.getstatusoutput("passwd -l root")')
	f.close()
	commands.getstatusoutput("sudo docker exec -d {0} /media/{1}.py".format(i,user))

elif soft=="php":
	i=commands.getstatusoutput("sudo docker run -itd --privileged=true -p {0}:4200 -v /docker/:/media/ rahul bash".format(port))[1]
	commands.getstatusoutput("sudo touch /docker/{0}.py".format(user))
	commands.getstatusoutput("sudo chmod 777 /docker/{0}.py".format(user))
	f=open("/docker/{0}.py".format(user),"w")
	f.write('#!/usr/bin/python\nimport commands\ncommands.getstatusoutput("useradd -s /usr/bin/php -a {0}")\ncommands.getstatusoutput("echo {1}| passwd {0} --stdin")\n'.format(user,pas)+'ip=commands.getstatusoutput("hostname -i")[1]\ncommands.getstatusoutput("sed -Ei \'s/OPTS=\\"--disable-ssl-menu -s \/:LOGIN\\"/#OPTS=\\"--disable-ssl-menu -s \/:LOGIN\\"/g\' /etc/sysconfig/shellinaboxd")\ncommands.getstatusoutput("sed -Ei \'s/OPTS=\\"-t -s \/:SSH:172.17.0.2\\"/OPTS=\\"-t -s \/:SSH:{0}\\"/g\' /etc/sysconfig/shellinaboxd".format(ip))\ncommands.getstatusoutput("service shellinaboxd restart")\ncommands.getstatusoutput("passwd -l root")')
	f.close()
	commands.getstatusoutput("sudo docker exec -d {0} /media/{1}.py".format(i,user))

print '<a href="http://192.168.122.1:{0}" target="_blank">click here for {1} prompt</a>'.format(port,soft)
	
	


