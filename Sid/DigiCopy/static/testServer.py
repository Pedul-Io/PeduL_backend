from flask import *


f = open('yo.html','r')
s = f.read()
f.close()
app = Flask(__name__)

@app.route('/')
def my_form():
    
        return s 
 

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

