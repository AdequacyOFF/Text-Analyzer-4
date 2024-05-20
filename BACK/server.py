from Controllers.dragAndDropController import file_process
from Controllers.urlController import url_process
from Controllers.textController import text_process
from Controllers.basicAuthController import basic_auth
from NeuralNetwork.sentiment_classifier import SentimentClassifier
from flask import Flask
from flask_cors import CORS

UPLOAD_FOLDER = "Files"
ALLOWED_EXTENSIONS = set(['txt','pdf','png', 'img', 'jpg', 'jpeg', 'doc', 'docx'])

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
classifier = SentimentClassifier()

@app.before_request
def basic_authentication():
    return basic_auth()
    
@app.route('/text', methods=['GET', 'POST'])
def text_processing():
    return text_process(classifier)

@app.route('/url', methods=['GET', 'POST'])
def url_processing():
    return url_process(classifier)

@app.route('/filesUpload', methods=['GET', 'POST'])
def file_processing():
    return file_process(app.config['UPLOAD_FOLDER'], ALLOWED_EXTENSIONS, classifier)

app.run(host='127.0.0.1', port=8080)