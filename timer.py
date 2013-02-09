#Author:Shruti Kapoor
#!/usr/bin/python

import re
import os
import sys
import datetime
import smtplib
from email.mime.text import MIMEText

#---------------SEARCH THE FILE FOR FOLLOWING STRINGS----------
datefield="date_submitted"
admin_email="hwason@eos.ubc.ca"
sender= "webadmin@slimweb.eos.ubc.ca"
#dateformat = '%m/%d/%Y'  # Date should be in the format: month/date/year eg: 12/22/2012
timer_days=45
typename="@unpublished"
#--------------------DECLARATIONS------------
num_files=len(sys.argv)
int_keys=[]
setlist=[]
error_list=[]
key=[]
#---------------BEGIN PROCESSING------------------------
fileIN=open(sys.argv[1],"r")

def sendmail(error_list):
	errors=" "
	if error_list:
		for each in error_list:
			errors = errors + " " + each
		text="Please update the following entries in unpublished.bib -" + errors  
		msg = MIMEText(text)
	
		msg['Subject'] = 'Update unpublished.bib in SVN repository'
		msg['From'] = sender
		msg['To'] = admin_email
		s = smtplib.SMTP()
		s.connect(host='smtp.eos.ubc.ca',port=25)
		s.sendmail(msg['From'],[admin_email], msg.as_string())
		print "Message sent"
		s.close()
	else:	
		print "All entries updated"
print "Reading..."
for line in fileIN:	
	line=line.strip()
	if typename.lower() in line.lower():
		entries=line.split('@')
		entry=entries[1].strip()
		split_entry=entry.split("{")[1]
		key=split_entry.split(",")[0]
		setlist.append(key)
	if datefield.lower() in line.lower():
		temp=line.split(datefield)
		date=re.sub('[^A-Za-z0-9/]+', '', temp[1])
		setlist.append
		end_date=datetime.datetime.utcnow()
		start_date = datetime.datetime.strptime(date,'%m/%d/%Y')
		diff = (end_date - start_date).days
		if diff > timer_days:
			error_list.append(key)
		if diff < 0:
			print "Error:Invalid Date"
			quit() 
sendmail(error_list)
fileIN.close()		


