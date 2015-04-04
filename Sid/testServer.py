from flask import *
from smtplib import *
from email import *
from email.mime import *
from email.mime.text import *

fromaddr = 'pedulserver@gmail.com'
toaddrs = 'sid.ghoshal@gmail.com'
subject = 'We can now send registration confirmation'
username = 'pedulserver'
password = 'quaternions'
app = Flask(__name__)

q = '''@app.route('/#', methods=['GET', 'POST'])
def my_form2():
                
        msg = MIMEText("This is a test registration email")
        msg['From'] = fromaddr
        msg['To'] = toaddrs
        msg['Subject'] = subject

        
        server = SMTP('smtp.gmail.com:587')
        print "hi"
        server.starttls()
        
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()
        return render_template("yo.html")'''



@app.route('/')
def my_form():
    
        return render_template("yo.html")
@app.route('/', methods=['POST'])
def my_form_post():
        
        msg = MIMEText("This is a test registration email")
        msg['From'] = fromaddr
        msg['To'] = toaddrs
        msg['Subject'] = subject

        
        server = SMTP('smtp.gmail.com:587')
        print "hi"
        server.starttls()
        
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg.as_string())
        server.quit()
        
        return render_template("yo.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)

