from flask import *
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin!'

@app.route('/guest/<guestname>')
def hello_guest(guestname):
    return 'Hello %s' % guestname

@app.route('/user/<username>')
def user(username):
    if username == 'Admin' or username == 'admin' :
        return redirect(url_for('hello_admin'))
    else :
        return redirect(url_for('hello_guest',guestname=username))

if __name__ == '__main__':
    app.run(debug=True)
    