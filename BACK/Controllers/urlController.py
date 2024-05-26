from flask import request, Response
# from Parser.Parser import parse_url

def url_process(classifier, bot):
    tmpUrl = str(request.data)
    url = tmpUrl[:len(tmpUrl)-1]
    text = bot.article_get(url)
    return Response(classifier.summary(text), content_type="application/json")


    
