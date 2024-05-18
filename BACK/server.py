from Controllers.dragAndDropController import file_process
from Controllers.urlController import url_process
from Controllers.textController import text_process
from Controllers.basicAuthController import basic_auth
from flask import Flask
from flask_cors import CORS

UPLOAD_FOLDER = "Files"
ALLOWED_EXTENSIONS = set(['txt','pdf','png', 'img', 'jpg', 'jpeg', 'doc', 'docx'])

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.before_request
def basic_authentication():
    return basic_auth()
    
@app.route('/text', methods=['POST'])
def text_processing():
    return text_process()

@app.route('/url', methods=['GET', 'POST'])
def url_processing():
    return url_process()

@app.route('/filesUpload', methods=['POST'])
def file_processing():
    return file_process(app.config['UPLOAD_FOLDER'], ALLOWED_EXTENSIONS)

app.run(host='127.0.0.1', port=8080)