import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication#傳送附件
from email.mime.multipart import MIMEMultipart #傳送mail的各部分

server = smtplib.SMTP('smtp.gmail.com', 587) #host,port
server.starttls()
server.ehlo() #start the server

with open('password.txt','r') as f: #讀密碼
    password = f.read()
server.login('your email@g-mail.nsysu.edu.tw',password) 

#填新郵件
msg = MIMEMultipart()
msg['from'] = 'howard1028'
msg['to'] = 'wyi67441@nezid.com' #收件者
msg['subject'] = 'a Test' #主旨
with open('message.txt','r') as f: 
    message = f.read()
msg.attach(MIMEText(message,'plain')) #內文

#加附件
file = 'chenchen.jpg'
p = MIMEApplication(open(file,'rb').read()) 
p.add_header('Content-Disposition','attachment',filename=file)
msg.attach(p)


text = msg.as_string() 
server.sendmail('your email@g-mail.nsysu.edu.tw','wyi67441@nezid.com',text) #真正寄，回送寄件備份
print("Sent successful!")