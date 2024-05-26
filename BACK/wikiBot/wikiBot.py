import requests

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
        print(loginResponse)
        assert loginResponse['login']['result'] == 'Success'

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

    def article_save(self, newArticleText, articleTitle):
        params = {
        "action": "edit",
        "title": articleTitle,
        "format": "json",
        "text": newArticleText,
        "token": self.csrfToken
        }

        responce = self.session.post(self.wikiApiLink, data=params)
        saveResponse = responce.json()
        assert saveResponse['edit']['result'] == 'Success'
        return 0
    
    def article_get(self, articleTitle):
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
        articleText = getResponce["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"]

        print(articleText)
        return articleText