from Controllers.dragAndDropController import file_process
from Controllers.urlController import url_process
from Controllers.textController import text_process
from Controllers.basicAuthController import basic_auth
from Controllers.outputTextController import article_edit, article_put, article_publish
from NeuralNetwork.text_analyser import TextAnalyser
from flask import Flask
from flask_cors import CORS

UPLOAD_FOLDER = "Files"
ALLOWED_EXTENSIONS = set(['txt','pdf','png', 'img', 'jpg', 'jpeg', 'doc', 'docx'])

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
classifier = TextAnalyser()

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

@app.route('/outputText/articleEdit', methods=['POST'])
def article_editing():
    return article_edit(classifier)

@app.route('/outputText/articlePut', methods=['POST'])
def article_puting():
    return article_put()

@app.route('/outputText/articlePublish', methods=['GET'])
def article_publishing():
    return article_publish()

app.run(host='127.0.0.1', port=8080)