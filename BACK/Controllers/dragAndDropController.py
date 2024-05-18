import os
import docx
from flask import request, Response
from werkzeug.utils import secure_filename
from extensionConverters.pdfConverter import pdfConvert
from extensionConverters.image2text import ImageReader

def allowed_file(filename, allowedExtensions):
    return '.' in filename and filename.rsplit('.', 1)[1] in allowedExtensions

def file_process(uploadFolder, allowedExtensions, classifier):
    if (not os.path.exists("Files")):
        os.mkdir("Files")
    if request.method == 'POST':
        if 'files' not in request.files:
            return Response("No file part", status=507)
        
        file = request.files['files']

        if file.filename == '':
            return Response("No selected file", status=507)
        
        if file and allowed_file(file.filename, allowedExtensions):
            filename = secure_filename(file.filename)
            file.save(os.path.join(uploadFolder, filename))

            filepath = (uploadFolder +"\\"+ filename).replace('/','\\')
            fileExtension = file.filename.rsplit('.', 1)[1]
            print (filepath)
            match fileExtension:
                case "txt":
                    s_file = open(filepath, encoding='utf-8')
                    text = s_file.read()
                case  "doc" | "docx":
                    doc = docx.Document(filepath)
                    text = ""
                    for paragraph in doc.paragraphs:
                        text += paragraph.text
                case "pdf":
                    text = pdfConvert(filepath)
                case "png" | "img" | "jpg" | "jpeg": 
                    reader = ImageReader()
                    text = reader.read(filepath)
                case _: return Response("Unsuported extension", status=507)

            
            return Response(classifier.summary(text), content_type="application/json")
        
    