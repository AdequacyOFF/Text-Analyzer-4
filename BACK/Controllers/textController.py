from flask import request, Response

def text_process(classifier):
    text = request.json.get('inputValue', None)
    return Response(classifier.summary(text), content_type="application/json")
