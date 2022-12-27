import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart #暫存附件

server = smtplib.SMTP('smtp.google.com',25)

server.ehlo() #start the server
with open('password.txt','r') as f:
    password = f.read()

server.login('test.com',password)

msg = MIMEMultipart()
