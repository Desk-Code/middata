from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/hellobuddy') 

@app.route('/hellobuddy')
def hello_buddy():
    return "Hello Budyy !!!"

if __name__ == '__main__':
    app.run(debug=True) 