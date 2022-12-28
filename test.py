# Import smtplib for the actual sending function
# import smtplib

# # Import the email modules we'll need
# from email.message import EmailMessage

# # Open the plain text file whose name is in textfile for reading.
# with open('message.txt') as fp:
#     # Create a text/plain message
#     msg = EmailMessage()
#     msg.set_content(fp.read())

# # me == the sender's email address
# # you == the recipient's email address
# msg['Subject'] = 'yes'
# msg['From'] = "example1@hotmail.com"
# msg['To'] = "example2@hotmail.com"

# # Login
# s =server = smtplib.SMTP('smtp.office365.com', 587)
# s.starttls()
# s.login('example1@hotmail.com',"password")

# # Sending the message
# s.send_message(msg)
# s.quit()


import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart #暫存附件
fromaddr = "test1@example.com"
toaddr = "test2@example.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Mail"
body = "Test mail from python"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.office365.com', 25)
server.connect("smtp.office365.com",465)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()