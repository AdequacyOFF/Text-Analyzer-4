import requests

class wikiBot:
    def __init__(self):
        session = requests.Session()
        wikiApiLink = "https://baza.znanierussia.ru/mediawiki/api.php"
        tokenUrl = wikiApiLink + "?action=query&meta=tokens&format=json&type=login" #для получения login токена
        response = session.get(tokenUrl)
        response_json = response.json()
        botToken = response_json["query"]["tokens"]["logintoken"] #получили токен
        print(botToken)

        botLogin = "Stalnoy Voin" 
        botPassword = "Andrey1Andrey"
        
        loginParams = {
            'action': "login",
            'lgname': botLogin,
            'lgpassword': botPassword,
            'lgtoken': botToken,
            'format': "json"
        }

        response = session.post(wikiApiLink, data=loginParams)
        loginResponse = response.json()
        print(loginResponse)
        assert loginResponse['login']['result'] == 'Success'
       