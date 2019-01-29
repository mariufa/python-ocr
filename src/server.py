from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from ocr import ocr

app = Flask(__name__)

UPLOAD_FOLDER = 'images/'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['POST'] )
def hello():
    file = request.files['file']
    if file.filename == '':
        return 'no file selected'
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    text = ocr(file_path)
    os.remove(file_path)
    return text

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')