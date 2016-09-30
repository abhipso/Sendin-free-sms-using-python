import urllib2
import cookielib
from getpass import getpass
import os
import sys
#------------Enter the username and password for your way2sms account-------------------
username = 'Enter-your-username-here'
passwd = 'Enter-your-password-here'
#-----------------Take the message as input-------------------
message = raw_input("Enter Message :")
#-----------------Enter the number to send SMS-------------------
number = 1234  #This is an example number. Enter the number where you want to send sms

message = "+".join(message.split(' '))

url = 'http://site24.way2sms.com/Login1.action?'#Part of link for authentication
data = 'username='+str(username)+'&password='+str(passwd)
#-------------------------Set up the cookie jar to store Cookie--------------------------------
cj = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
#	Try to authenticate. If authentication fails, some I/O error will be thrown in try part.
#	In that case the error message "Authentication failed" will be printed

try:
    usock = opener.open(url, data)
except IOError:
    print "\nAuthentication Failed!"
    sys.exit(1)

jession_id = str(cj).split('~')[1].split(' ')[0]
send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
#-------------Now after authentication visit final link to send the sms--------------- 
send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+str(number)+'&message='+message+'&msgLen=136'
opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]

#	Try to send the SMS.
#	In case of I/O error, the error message will be printed.

try:
    sms_sent_page = opener.open(send_sms_url,send_sms_data)
except IOError:

    print "\nError Occured! Could not send SMS"
    sys.exit(1)

print "\nSMS Sent!"

  
