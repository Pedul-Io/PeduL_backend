from smtplib import *
from email import *
from email.mime import *
from email.mime.text import *

msg = MIMEText('''Dear User,\nThank you for registering for Pedul updates! We will email roughly one a month on our periodic updates and major accomplishments.
               \n Sincerely, \n\n The Pedul Team''')

msg['From'] = 'pedulserver@gmail.com'
msg['To'] = 'sid.ghoshal@yahoo.com'
msg['Subject'] = "Thank you for registering for Pedul Updates"



server = SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('pedulserver@gmail.com','quaternions')
print "made it here"
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print "hi"
