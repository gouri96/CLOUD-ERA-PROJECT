#!/usr/bin/python
print "content-type:text/html"
print

import commands,cgi,cgitb
cgitb.enable()
import mysql.connector as mariadb
data=cgi.FormContent()
prof=data['p'][0]
user=data['user'][0]
pas=data['pas'][0]

mcon=mariadb.connect(user='root',password='akshay',database='signup')
cursor=mcon.cursor()
cursor.execute('select username from student where password=%s and profile=%s',(user,prof))
check=0
for x in cursor:
	if x[0]==user:
		check=1
if check==1:
	print """
	<link type="text/css" rel="stylesheet" href="http://192.168.122.1/home.css"></link>	
	<style>
	img.c
	{
		width:100%;
		height:100%;
	}
	div.two
	{
	position: absolute;
	top:4%;
	left: 0%;
	margin-top:2px;
	height:50%;
	}
	div.four
	{
	position: absolute;
	top:55%;
	left: 0%;
	width:20%;
	height:70%;
	background:url(/web/b2.jpg);
	background-size: 100% 100%;
	}
	iframe.front1
	{
	position: absolute;
	top:55%;
	left: 20%;
	width:80%;
	height:70%;
	background:url(/web/b2.jpg);
	background-size: 100% 100%;
	}


	a.amenu
	{
	background:pink;
	width:90%;
	margin-left:4%;
	}
	a.amenu1
	{
	background:#ff5187;
	margin-bottom:5px;
	}

	</style>



<script language="JavaScript">
var i = 0;
var path = new Array();
path[0] = "/web/j7.jpg";
path[1] = "/web/q1.jpg";
path[2] = "/web/q3.jpg";
path[3] = "/web/q2.png";
path[4] = "/web/q6.jpg";
path[5] = "/web/q8.jpg";
path[6] = "/web/q5.jpg";

function swapImage()
{
   document.slide.src = path[i];
  	if(i < path.length - 1) 
   	i++; 
	else 
	i = 0;
   setTimeout("swapImage()",4000);
}
window.onload=swapImage;
</script>

	<div class="top">
		<div class="top1">
		<img class="i1" src="/web/link.png">
		<img class="i1" src="/web/tw.png">
		<img class="i1" src="/web/f.png">
		<img class="i1" src="/web/gog.png">
		</div>

	<input class="top" type="text" placeholder=" google search"/><a class="go" href="http://www.google.com">Go</a>
		<select class="s1">
			<option class="o1">English </option>
			<option class="o1">Hindi</option>
			<option class="o1">spanish</option>
		</select>
	</div>
	<div class="two">
		<img  class="c" name="slide" src="/web/q7.jpg">
	</div>
	<div class="four">
		<a href='' class="amenu1" style="margin-top:20px;">PROFILE</a>
		<a class='amenu' target="front1" href=''>Update</a>
		<a class='amenu' target="front1" href=''>Notifiaction</a>
		<a class='amenu' target="front1" href=''>Edit Profile</a>
		<a class='amenu' target="front1" href=''>Settings</a>
		<a class='amenu1' target="front1" href='http://192.168.122.1/service.html'>SERVICES</a>
		<a class='amenu1' href=''>LOGOUT</a>
	</div>
	<iframe name="front1" class="front1">


	</iframe>


	"""


else:
	print '<script>alert("sorry!Wrong details...login again!!!")</script>'
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
	