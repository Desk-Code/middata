
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/princy')
def name():
    return "helllo princy!"

@app.route('/user/<username>')
def user(username):
    return f"hello {username} !!"

@app.route('/add/<int:num1>/<int:num2>')
def addition(num1,num2):
    return f"{num1} + {num2} = {num1+num2}"

def autocall(name):
    return f"I am call using to url rule and my argument is {name}"

app.add_url_rule('/addurlrule/<name>','autocall',autocall)

if __name__ == '__main__':
    app.run(debug=True)