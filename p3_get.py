from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sqareNumber():
    if request.method == 'GET':
        if request.args.get('num') == None :
            return render_template('p3_squarenum.html')
        elif request.args.get('num') == '' :
            return "<html><body>Please Enter a Valid Input...</body></html>"
        else :
            number = request.args.get('num')
            sq = int(number) * int(number)
            return render_template('p3_answer.html',num = number,squareeOfNumber = sq)

if __name__ == '__main__':
    app.run(debug=True)