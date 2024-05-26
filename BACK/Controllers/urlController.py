from flask import request, Response
# from Parser.Parser import parse_url

def url_process(classifier, bot):
    url = str(request.data)
    print(url)
    splitUrl = url.split('/')
    articleTitle = splitUrl[len(splitUrl)-1]
    finalTitle = articleTitle[:len(articleTitle)-1]
    print(articleTitle[:len(articleTitle)-1])
    text = bot.article_get(finalTitle)
    return Response(classifier.summary(text), content_type="application/json")


    
