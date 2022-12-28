import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart #暫存附件

server = smtplib.SMTP('smtp.gmail.com', 587) #host,port
server.starttls()
server.ehlo() #start the server

with open('password.txt','r') as f: #讀密碼
    password = f.read()
server.login('a@g-mail.nsysu.edu.tw',password) 

#填新郵件
msg = MIMEMultipart()
msg['from'] = 'howard1028'
msg['to'] = 'wyi67441@nezid.com' #收件者
msg['subject'] = 'a Test' #主旨
with open('message.txt','r') as f: 
    message = f.read()
msg.attach(MIMEText(message,'plain')) #內文

#加附件
filename = 'chenchen.jpg'
attachment = open(filename,'rb') #open with binary
p = MIMEBase('application' , 'octet-stream') 
p.set_payload(attachment.read()) #讀的attachment的payload

encoders.encode_base64(p)
p.add_header('Content-Disposition' , f'attachment={attachment}') #要傳的payload加上header才能當附件
msg.attach(p)

text = msg.as_string() 
server.sendmail('a@g-mail.nsysu.edu.tw','wyi67441@nezid.com',text) #真正寄，回送寄件備份