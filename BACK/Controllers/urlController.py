from flask import request, Response
# from Parser.Parser import parse_url

def url_process(classifier, bot):
    url = request.data
    print(url)
    articleTitle = url.split
    text = print(bot.article_get("Кадацкий,_Иван_Федосеевич"))
    return Response(classifier.summary(text), content_type="application/json")


    
