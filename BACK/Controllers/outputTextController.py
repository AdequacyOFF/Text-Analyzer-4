from flask import request, Response
from Parser.Parser import parse_url
import json

processedArticle = []

def article_put():
    global processedArticle
    processedArticle = request.json.get('array', None)
    print ("processed article:")
    print(processedArticle)
    return Response('Article has been updated successfully', status=200)

def article_edit(classifier):
    newSentence = json.loads(classifier.summary(request.json.get('inputValue', None)))
    processedArticle[request.headers.get('indexToChange', type = int)] = newSentence[0]
    answer = json.dumps(processedArticle, ensure_ascii=False, sort_keys=False)
    return Response(answer, content_type="application/json")
    
def article_publish():
    return Response(status=200, headers={'articlePublished': 1})
