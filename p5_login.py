from flask import *
app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('p3_login.html')

@app.route('/success')
def success():
    return "You Have Logged In Successfully"

@app.route('/islogin', methods=['GET', 'POST'])
def islogin():
    if request.method == "POST" and request.form['username'] == 'princy' :
        return redirect(url_for('success'))
    
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True) 

