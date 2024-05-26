import requests
from urllib.parse import unquote

class wikiBot:
    
    def __init__(self, wikiApiLink):
        self.session = requests.Session()
        self.wikiApiLink = wikiApiLink #ссылка на апи вики
        #получаем login токен
        loginTokenUrl = self.wikiApiLink + "?action=query&meta=tokens&format=json&type=login"
        response = self.session.get(loginTokenUrl)
        response_json = response.json()
        self.loginToken = response_json["query"]["tokens"]["logintoken"] 
        print("Login token: " + self.loginToken)

        botLogin = "Stalnoy Voin" 
        botPassword = "Andrey1Andrey"
        
        loginParams = {
            'action': "login",
            'lgname': botLogin,
            'lgpassword': botPassword,
            'lgtoken': self.loginToken,
            'format': "json"
        }

        response = self.session.post(self.wikiApiLink, data=loginParams)
        loginResponse = response.json()
        
        assert loginResponse['login']['result'] == 'Success'
        print("Bot logged in successfully")

        #получаем csrf токен
        CsrfParams = { 
        "action": "query",
        "meta": "tokens",
        "format": "json"
        }
        responce = self.session.get(url=self.wikiApiLink, params=CsrfParams)
        csrfResponse = responce.json()
        self.csrfToken = csrfResponse['query']['tokens']['csrftoken']
        print("CSRF Token: " + self.csrfToken)

    def get_article_from_link(self, link):
        splitUrl = link.split('/')
        articleTitle = splitUrl[len(splitUrl)-1]
        finalTitle = articleTitle[:len(articleTitle)-1]
        ruArticleTitle = unquote(finalTitle) 
        print("ruArticleTitle: " + ruArticleTitle)
        return ruArticleTitle

    def article_publish(self, newArticleText, articleLink):
        articleTitle = self.get_article_from_link(articleLink)
        print("newArticleText: " + newArticleText)
        print("articleTitle: " + articleTitle)
        params = {
        "action": "edit",
        "title": articleTitle,
        "format": "json",
        "text": newArticleText,
        "token": self.csrfToken
        }
        print("Params: " + str(params))
        responce = self.session.post(self.wikiApiLink, data=params)
        saveResponse = responce.json()
        print("Response: " + str(saveResponse))
        assert saveResponse['edit']['result'] == 'Success'
        return 0
    
    def article_get(self, articleLink):
        articleTitle = self.get_article_from_link(articleLink)
        params = {
        "action": "query",
        "prop": "revisions",
        "titles": articleTitle,
        "rvslots": "*",
        "rvprop": "content",
        "formatversion": 2,
        "format": "json"
        }
        
        responce = self.session.get(url=self.wikiApiLink, params=params)
        getResponce = responce.json()
        print("Response: " + str(getResponce))
        assert getResponce["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"] != None
        articleText = getResponce["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"]

        print(articleText)
        return articleText
    
    