from flask import *
from flask import request
from smtplib import *
from email import *
from email.mime import *
from email.mime.text import *
import xlrd
import xlwt
import sys, traceback

fromaddr = 'pedulserver@gmail.com'
toaddrs = 'cegbelu@gmail.com'
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

        #try:
         #       emailval = request.form['EmailForm']
        #except:
         #       return "Error"
        #return "hi"
        return render_template("untitled.html")


@app.route('/', methods=['POST'])
def my_form_post():
        #print "hello world"
        try:
                emailval = request.form['emailInput']
                msg = MIMEText("Thank you for registering for updates!")


                try:
                        emailfile = open('emails.txt','r')
                        good = emailfile.read()
                        good += (str(emailval)+"\n")
                        emailfile.close()
                        emailfile = open('emails.txt','w')
                        emailfile.write(good)
                        emailfile.close()
                except:
                        print "file writing error"

                return render_template("untitled.html")
                
                try:
                        msg['From'] = fromaddr
                        msg['To'] = emailval
                        msg['Subject'] = "Thank you for registering for Pedul Updates"
                except:
                        print "error in setting up inform"

                try:
                        server = SMTP('smtp.gmail.com:587')
                        server.starttls()
                        
                        server.login(username,password)
                        print "made it here"
                        server.sendmail(msg['From'], msg['To'], msg.as_string())
                        server.quit()
                except:
                        print "error in server"
                return render_template("untitled.html")

        
        except:
                #This needs to be modified to include email sending
                print "fuck!"
                return "Sorry there was an error"
        return "hi"
        
        

de = '''
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
        
        return my_form() '''

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)

