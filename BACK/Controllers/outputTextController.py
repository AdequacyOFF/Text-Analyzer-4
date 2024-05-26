from flask import request, Response
import json

processedArticle = [] #текст страницы вместе со всей статистикой

def article_update():
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

def article_publish(bot):
    processedArticleText = ""
    for sentence in processedArticle[:len(processedArticle)-2]:
        print ("sentence: ")
        print(sentence)
        processedArticleText += sentence['text']
    articleLink = request.headers.get('articleLink')
    print(articleLink)
    print ("Publishing article:")
    print(processedArticleText)
    bot.article_publish(processedArticleText, articleLink)
    return Response('Article has been published successfully', status=200)