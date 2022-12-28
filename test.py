#傳送郵件給多個人

#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

host = 'smtp.126.com'  # 設定發件伺服器地址
port = 25  # 設定發件伺服器埠號。注意，這裡有SSL和非SSL兩種形式

#傳送郵箱
sender = 'wm8993@126.com'

#接收郵箱
receiver = ['328464035@qq.com','wm8993@sina.com','wm8993@126.com']

#傳送郵件主題
subject = 'Python email test'

#傳送郵箱伺服器
smtpserver = 'smtp.126.com'

username = 'wm8993@126.com'  #傳送郵箱使用者
password = '**************'                #郵箱密碼或授權碼

#編寫 text 型別的郵件正文
msg = MIMEText('<html><h1>比你更忙的人都在學習！</h1></html>','html','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'wm8993@126.com'
msg['To'] =','.join(receiver) 

smtp = smtplib.SMTP()
smtp.connect('smtp.126.com',25)
smtp.login(username, password)  # 登陸郵箱
smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())  # 傳送郵件！
print("郵件傳送成功!")