#!/usr/bin/python
print "content-type:text/html"
print ""

import commands,cgi,time,sys,cgitb
cgitb.enable()
data=cgi.FormContent()
size=data['s'][0]
protocol=data['p'][0]
storage_type=data['st'][0]
f=data['fname'][0]
sip="192.168.122.1"
cip=data['i'][0]
user="test"
pas="akshay"
x=200
print size
print protocol
print  storage_type
print f
print cip
def clientnfs():
	z=commands.getstatusoutput("sudo touch /{0}.py".format(f))
	print z
	p=commands.getstatusoutput("sudo chmod 777 /{0}.py".format(f))
	print p
	g=open("/{0}.py".format(f),"w")
	g.write('#!/usr/bin/python\nimport commands\ncommands.getstatusoutput("mkdir /media/{1}")\ncommands.getstatusoutput("mount {0}:/media/{1} /media/{1} >/dev/null 2>/dev/null")\nraw_input()'.format(sip,f))
	g.close()
	h=commands.getstatusoutput("sudo tar -cvf {0}.tar /{0}.py".format(f))
	print h 
	q=commands.getstatusoutput("sudo mv {0}.tar /var/www/html".format(f))
	print "<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.122.1/{0}.tar\">\n".format(f)	
	#r=commands.getstatusoutput("sudo sshpass -p {0} scp {1}:/{2}.py root@{3}:/".format(sysp,sip,f,cip))
	#print r



def clientsshfs():
	w=commands.getstatusoutput("sudo touch /{0}.py".format(f))
	e=commands.getstatusoutput("sudo chmod 777 /{0}.py".format(f))
	print w
	print e
	p=open("/{0}.py".format(f),"w")
	p.write('#!/usr/bin/python\nimport commands\ncommands.getstatusoutput("mkdir /media/{3}")\ncommands.getstatusoutput("sshpass -p {0} sshfs {1}@{2}:/media/{3} /media/{3} >/dev/null 2>/dev/null")\nraw_input()'.format(pas,user,sip,f))
	p.close()
	h=commands.getstatusoutput("sudo tar -cvf {0}.tar /{0}.py".format(f))
	print h 
	q=commands.getstatusoutput("sudo mv {0}.tar /var/www/html".format(f))
	print "<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.122.1/{0}.tar\">\n".format(f)	
	#commands.getstatusoutput("sudo scp {0}:/{1}.py {2}:/{1}.py".format(sip,f,cip))

def clientiscsi():
	commands.getstatusoutput("sudo touch /{0}.py".format(f))
	commands.getstatusoutput("sudo chmod 777 /{0}.py".format(f))
	g=open("/{0}.py".format(f),"w")
	g.write('#!/usr/bin/python\nimport commands\na=commands.getstatusoutput("iscsiadm --mode discoverydb --type sendtargets --portal {0} --discover ")'.format(sip)+'\nb=a[1].split()[0][:-2]\nc=a[1].split()[1]\ncommands.getstatusoutput("iscsiadm --mode node --targetname {0} --portal {1} --login  >/dev/null 2>/dev/null".format(c,b))')
	g.close()
	h=commands.getstatusoutput("sudo tar -cvf {0}.tar /{0}.py".format(f))
	print h 
	q=commands.getstatusoutput("sudo mv {0}.tar /var/www/html".format(f))
	print "<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.122.1/{0}.tar\">\n".format(f)	
	#commands.getstatusoutput("sudo scp {0}:/{1}.py {2}:/{1}.py".format(sip,f,cip))

def clientsamba():
	commands.getstatusoutput("sudo touch /{0}.py".format(f))
	commands.getstatusoutput("sudo chmod 777 /{0}.py".format(f))
	g=open("/{0}.py".format(f),"w")
	g.write('#!/usr/bin/python\nimport commands,os\ncommands.getstatusoutput("mkdir /media/{2}")\nos.system("mount -o username={0}1 //{1}/{2} /media/{2}")\nraw_input()'.format(user,sip,f))
	g.close()
	h=commands.getstatusoutput("sudo tar -cvf {0}.tar /{0}.py".format(f))
	print h 
	q=commands.getstatusoutput("sudo mv {0}.tar /var/www/html".format(f))
	print "<META HTTP-EQUIV=refresh CONTENT=\"0; URL=http://192.168.122.1/{0}.tar\">\n".format(f)	
	#commands.getstatusoutput("sudo scp {0}:/{1}.py {2}:/{1}.py".format(sip,f,cip))




def nfs(size):
	q=commands.getstatusoutput("sudo systemctl restart nfs-server")
	print q
	clientnfs()

def sshfs(size):
	l=commands.getstatusoutput("sudo chown {0} /media/{1}  >/dev/null 2>/dev/null".format(user,f))
	k=commands.getstatusoutput("sudo chmod o-rwx,g-rwx /media/{0}".format(f))
	print l
	print k
	clientsshfs()
def iscsi(size):
	v=commands.getstatusoutput("sudo chmod 777 /etc/tgt/conf.d/ ")
	print v
	f1=open("/etc/tgt/conf.d/{0}.conf".format(f),"w")
	f1.write("<target mycloud>\n backing-store /dev/cloud/{0} \n </target>".format(f))
	f1.close()
	commands.getstatusoutput("sudo systemctl restart tgtd  >/dev/null 2>/dev/null")
	clientiscsi()

def samba(size):
	a=commands.getstatusoutput("sudo useradd -s /sbin/nologin {0}1".format(user))
	print a
	b=commands.getstatusoutput('sudo echo -e "123\n123" | sudo smbpasswd -a {0}1'.format(user))
	print b 
	print '<p style="color:red"> samba username={0}1 password=123 </p>'.format(user)
	f1=open("/etc/samba/smb.conf","a")
	f1.write('\n\n[{0}]\npath=/media/{0}\nwritable=yes\nvalid users={1}1'.format(f,user))
	f1.close()
	commands.getstatusoutput("sudo chmod o+w /media/{0}".format(f))
	commands.getstatusoutput("sudo systemctl restart smb")
	clientsamba()

def blocksamba(size):
	a=commands.getstatusoutput("sudo useradd -s /sbin/nologin {0}1".format(user))
	print a
	b=commands.getstatusoutput('sudo echo -e "123\n123" | sudo smbpasswd -a {0}1'.format(user))
	print b
	print '<p style="color:red"> samba username={0}1 password=123 </p>'.format(user)

	f1=open("/etc/samba/smb.conf","a")
	f1.write('\n\n[{0}]\npath=/dev/cloud/{0}\nwritable=yes\nvalid users={1}1'.format(f,user))
	f1.close()
	commands.getstatusoutput("sudo chmod o+w /media/{0}".format(f))
	commands.getstatusoutput("sudo systemctl restart smb")
	clientsamba()
	



def filestorage(protocol,size):
	z=commands.getstatusoutput("sudo lvcreate --name {0} --size +{1} /dev/cloud  >/dev/null 2>/dev/null".format(f,size))
	print z
	x=commands.getstatusoutput("sudo mkfs.ext4 /dev/cloud/{0}  >/dev/null 2>/dev/null".format(f))
	print x
	commands.getstatusoutput("sudo mkdir /media/{0}".format(f))
	c=commands.getstatusoutput("sudo mount /dev/cloud/{0} /media/{0}".format(f))
	print c
	if protocol=="nfs" or protocol=="sshfs":
		commands.getstatusoutput("sudo chmod 777 /etc/exports")
		d=commands.getstatusoutput("sudo echo '/media/{0} *(rw,no_root_squash)' >> /etc/exports".format(f))
		print d
		if protocol=="nfs":
			nfs(size)
		else:
			sshfs(size)
	else:
		samba(size)

def blockstorage(protocol,size):
	commands.getstatusoutput("sudo lvcreate --name {0} --size +{1} /dev/cloud  >/dev/null 2>/dev/null".format(f,size))
	if protocol=="iscsi":
		iscsi(size)
	else:
		blocksamba(size)


if True:
	if storage_type=="file-storage":
		filestorage(protocol,size)
	else:
		blockstorage(protocol,size)

else:
	print "location://192.168.122.1/index.html"
	print "<body> Sorry,sever not found"
	print "</body></html>"

