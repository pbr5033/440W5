import string
import base64
import binascii
import random
import hashlib
import cherrypy
import subprocess
from time import gmtime, strftime


#Make the CherryPy server answer on any IP address that is received by this server. This makes the CherryPy server run from inside of a NAT boundary where the inside and outside IP addresses may be different.
cherrypy.server.socket_host = '0.0.0.0'

class PolyEncrypt(object):

	global rot47

	def rot47(s):
    		x = []
	    	for i in xrange(len(s)):
        		j = ord(s[i])
        		if j >= 33 and j <= 126:
            			x.append(chr(33 + ((j + 14) % 94)))
        		else:
            			x.append(s[i])
    		return ''.join(x)

	global rot13

	def rot13(s):
    		rotate = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    		return ''.join(string.translate(s, rotate))

#============================================================
#studentinputs
#============================================================
#Student Section
student_name = raw_input("What is your first name")

#Email Section
@cherrypy.expose
        def index(self):
        # This is the page that the user hits when they first find the system.  They need to provide an email
        # address.
        # This web form collects the email address and sends it off to be confirmed.

                return """<html>
                        <head>
                                <title>PolyEncrypt</title>
                                <link rel="stylesheet" href="polylab/style.css" type="text/css" />
                        </head>
                <body>
                <div id="content">
                        <h1>PolyEncrypt</h1>
                        <h2>Delivery System</h2>
                        <br>
                        <br>
                        <h3>Please enter your email address</h3>
                        <p><i>(e.g. abc1234@psu.edu)</i></p>
                        <form method="get" action="encryptchallenges">
                                <input type="text" value="" name="email" />
                                <button type="submit">Submit</button>
                        </form>
                </body>
		</html>"""




psu_email = raw_input("What is your Penn State Email")
class Polynet(object):
    global checkmail

    def checkmail(email):
        #this function validates the email address's format
        #we expect the emailaddress to be in the form aaa###@psu.edu

        email= email
        from validate_email import validate_email
        is_valid = validate_email(email)
        return is_valid








date = raw_input("What is the date(example 01/10/98) today?")


#Studentvariables: convert the stored input to strings
inputstudent_name = str(student_name)
inputpsu_email = str(psu_email)
inputdate = str(date)

# concatenate into one string
inputdata = inputstudent_name + inputpsu_email + inputdate

# convert to MD5
convData = hashlib.md5()
convData.update(inputdata)
