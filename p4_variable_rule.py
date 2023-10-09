from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/vstring/<name>')
def string_method(name):
    return "String Value is %s" % name

@app.route('/vint/<int:num>')
def int_method(num):
    return "Int Value is %d" % num

@app.route('/vfloat/<float:num>')
def float_method(num):
    return "Float Value is %f" % num 

if __name__ == '__main__':
    app.run(debug=True)