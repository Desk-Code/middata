from flask import *
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')   
def main():   
    return render_template("p6_file_upload.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
       f = request.files['file']
       f.save('templates/'+ secure_filename(f.filename))
       return render_template('p6_upload_success.html', name=f.filename)

if __name__ == '__main__':
    app.run(debug=True) 