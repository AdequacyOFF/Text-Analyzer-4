from flask import request, Response
from Parser.Parser import parse_url

def url_process(classifier):
    url = request.data
    print(url)
    text = parse_url(url)
    return Response(classifier.summary(text), content_type="application/json")
