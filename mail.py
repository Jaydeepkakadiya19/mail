import smtplib
import numpy as np
import os


import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

data = pd.read_excel("data.xlsx")
mails = data['Mail']
name = data['name']
event = data['event']


gmailaddress = "synapse.pr2019@gmail.com"
gmailpassword = "xxxxxx"
mailto = mails[0]

msg = MIMEMultipart()
msg['From'] = gmailaddress
msg['To'] = mailto
msg['Subject'] = "Synapse Participation Certificate"
body = "Cheers from Synapse \n \n         We hope that you have enjoyed the synapse. Find your Participation Certificate in Attachments"
msg.attach(MIMEText(body, 'plain'))
filename = "certificate.png"
attachment = open(r"C:\Users\jaydeep\Desktop\automail\certificate.png", "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(p)
mailServer = smtplib.SMTP('smtp.gmail.com', 587)
mailServer.starttls()
mailServer.login(gmailaddress, gmailpassword)
mailServer.sendmail(gmailaddress, mailto, msg)
print(" \n Sent!")

mailServer.quit()
# print(mails[0])
