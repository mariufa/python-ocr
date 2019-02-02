from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import os
from ocr import ocr

app = Flask(__name__)
cors = CORS(app)


UPLOAD_FOLDER = 'images/'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['POST', 'GET'] )
@cross_origin()
def ocr_endpoint():
    if request.method == 'POST': 
        file = request.files['file']
        if file.filename == '':
            return 'no file selected'
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        text = ocr(file_path)
        os.remove(file_path)
        return text
    else:
        return "Welcome to ocr"

if __name__ == "__main__":
    app.run()