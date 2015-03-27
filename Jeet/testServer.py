from flask import *

app = Flask(__name__)

@app.route('/')
def my_form():
    
    return render_template("testpage.html")   

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)

