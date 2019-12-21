import smtplib
import numpy as np
import os
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email import encoders
from PIL import Image, ImageDraw, ImageFont


def make_certi(n, e):                              #This function take will add info about participant in certificate 
    image = Image.open('certificate.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('font.ttf', size=150)

    message = n
    w, h = draw.textsize(message, font)
    mx, my = image.size
    (x, y) = ((mx-w)/2, 850)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font, align='center')

    message = e
    w, h = draw.textsize(message, font)
    mx, my = image.size
    (x, y) = ((mx-w)/2, 1300)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font, align='center')

    image.save('certi.png')
    # image.show()


def SendMail(Form, mto):                               # this function will send mail with customize certificate as attachment
    ImgFileName = "certi.png"
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'About ....'
    msg['From'] = 'abc@gmail.com'
    msg['To'] = mto

    text = MIMEText("Dear " + name[i]+", \n\n      Find Certificate in Attachments ")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s.sendmail(UserName, mto, msg.as_string())


data = pd.read_excel("data.xlsx")             #  taking name email id and name of event from excel sheet
mails = data['Mail'].iloc
name = data['name'].iloc
event = data['event'].iloc

UserName = "abc@gmail.com"                # Mail id and passward from which we have to send certificate
UserPassword = "xyz"

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(UserName, UserPassword)


for i in range(len(data['Mail'])):
    print("sending mail to "+mails[i])
    make_certi(data['name'].iloc[i], data['event'].iloc[i])
    SendMail(UserName, mails[i])
    print("sent!")


s.quit()
