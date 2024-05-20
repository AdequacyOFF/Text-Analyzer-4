from flask import request, Response
from Parser.Parser import parse_url

def url_process(classifier):
    url = request.data
    print(url)
    text = parse_url(url)
    return Response(classifier.summary(text), content_type="application/json")

import json

def wiki_edit(classifier):
    processedArticle = []
    if request.method == 'GET':
        if request.headers.get('publishArticle') == True:
            #жоска заливаем это говно на вики
            return Response(status=200, headers={'articlePublished': 1})
        if (request.headers.get('publishArticle') == False and request.args.get('wikiLink') != None):
            wikiLink = request.args.get('wikiLink')
            #жоска считываем всю статью по адресу wikiLink в text и обрабатываем
            text = "пока что хуй, сначала настрой апи"
            neuralNetAnswer = classifier.summary(text)
            processedArticle = json.loads(neuralNetAnswer)
            return Response(processedArticle, content_type="application/json")
        else:
            return Response(status=507, headers={'error': "header error"})
        
    if request.method == 'POST':
        if request.mimetype == 'application/json':
            changeToSave = json.loads(request.json) #ждем массив объектов формата 'key': 0, 'inputValue': '...'
            return Response(classifier.summary(text), content_type="application/json")
    
