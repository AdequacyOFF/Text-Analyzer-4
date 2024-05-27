from flask import request, Response
import json

processedArticle = [] #текст страницы вместе со всей статистикой

def article_update():
    global processedArticle
    processedArticle = request.json.get('array', None)
    print ("processed article:")
    print(processedArticle)
    return Response(str(processedArticle), status=200)

def article_edit(classifier):
    indexToChange = request.headers.get('indexToChange', type = int)
    newSentenceText = request.json.get('inputValue', None)
    processedArticleText = ""
    for sentence in processedArticle[:indexToChange]:
        print ("sentence:\n")
        print(sentence)
        processedArticleText += sentence['text']

    processedArticleText += newSentenceText

    for sentence in processedArticle[indexToChange + 1:len(processedArticle)-2]:
        print ("sentence:\n")
        print(sentence)
        processedArticleText += sentence['text']

    # newSentence = json.loads(classifier.summary(request.json.get('inputValue', None)))
    # processedArticle[request.headers.get('indexToChange', type = int)] = newSentence[0]
    # answer = json.dumps(classifier.summary(processedArticleText), ensure_ascii=False, sort_keys=False)
    return Response(classifier.summary(processedArticleText), content_type="application/json")

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