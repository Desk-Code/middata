from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        if request.args.get('username') == None:
            return render_template('p3_login.html')
        elif request.args.get('username') == '':
            return "<html><body>Please Input Valid UserName</body></html>"
        else :
            username = request.args.get('username') 
            return render_template('p3_login_out.html',user = username)
    elif request.method == "POST":
        if request.form['username'] == None:
            return render_template('p3_login.html')
        elif request.form['username'] == '':
            return "<html><body><p1>Pleasee Enter a Valid Input !!!</p1></body></html>"
        else:
            username = request.form['username']
            return render_template('p3_login_out.html',user = username)

if __name__ == '__main__':
    app.run(debug=True)

