#!/usr/bin/python
print "content-type:text/html"
print

import commands,cgi,cgitb
cgitb.enable()
import mysql.connector as mariadb
data=cgi.FormContent()
prof=data['prof'][0]
user=data['user'][0]
pas=data['pas'][0]
mobile=data['mobile'][0]
mcon=mariadb.connect(user='root',password='akshay',database='signup')
cursor=mcon.cursor()
cursor.execute('select username from student')
check=0
for x in cursor:
	if x[0]==user:
		check=1
if check==0:
	cursor.execute("insert into student values(%s,%s,%s,%s)",(user,pas,mobile,prof))
	mcon.commit()
	print '<script>alert("successfully registered")</script>'
	print """
		<link type="text/css" rel="stylesheet" href="http://192.168.122.1/register.css"></link>
		<div class="register">
		</div>

		<form method="post" action="http://192.168.122.1/cgi-bin/login.py">
		<p class="a">Login Details</p><br />
		
		<select name="p">
		<option value="Student">Student</option>
		<option value="Employee">Employee</option>
		</select><br />
		<input type="text" name="user" placeholder="User name"><br />
		<input type="password" name="pas" placeholder="Password"><br />
		
		<input class="sub" type="submit" value="login" background="blue">
        <p class="m"> New User?<a href="http://192.168.122.1/registration.html">Register</a></p>
        </form>
		"""

	
else:
	print '<script>alert("sorry!user name is already registered ")</script>'
	print """

		<link type="text/css" rel="stylesheet" href="http://192.168.122.1/register.css"></link>
	<div class="register">
	</div>
		<form method="post" action="http://192.168.122.1/cgi-bin/regestration.py">
		<p class="a">Create Account</p><br />
		
		<select name="prof"> 
		<option value="Student">Student</option>
		<option value="Employee">Employee</option>
		</select>  <br />
		<input type="text" name="user" placeholder="User name"><br />
		<input type="password" name="pas" placeholder="Password"><br />
		
		<input type="text" name="mobile" placeholder="Mobile number"><br />
			
		
		
		<input class="sub" type="submit" value="Join now" background="blue">
        <p class="m"> Already account?<a href="http://192.168.122.1/login.html">login</a></p>
        <p class="b"> <b>By clicking Join,you agree <u>cloud agreement</u> and <u> privacy policy</u></b></p>
        </form>
	"""
	
