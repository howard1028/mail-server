import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart #暫存附件

server = smtplib.SMTP('smtp.office365.com', 587) #host,port
# server.connect("smtp.world4you.com",465)
server.ehlo() #start the server

with open('password.txt','r') as f: #讀密碼
    password = f.read()

# server.login('m103040072@g-mail.nsysu.edu.tw',password) #有需要密碼才要加

msg = MIMEMultipart()
msg['from'] = 'howard1028'
msg['to'] = 'dyk31584@cdfaq.com'
msg['subject'] = 'a Test'

with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message,'plain')) #header和text加入message object

filename = 'chenchen.jpg'
attachment = open(filename,'rb') #open with binary
p = MIMEBase('application' , 'octet-stream') 
p.set_payload(attachment.read()) #讀的attachment的payload

encoders.encode_base64(p)
p.add_header('Content-Disposition' , f'attachment={attachment}') #要傳的payload加上header才能當附件
msg.attach(p)

text = msg.as_string() 
server.sendmail('m103040072@g-mail.nsysu.edu.tw','dyk31584@cdfaq.com',text)